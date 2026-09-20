"""AMBER smoke v2 for V3-EXQ-1043b -- all six seeds, and the variance DECOMPOSITION.

v1 measured seed 42 only. Two things it surfaced make the wider sweep necessary:

  1. `x1002._train_adapter` NEVER SEEDS ANYTHING -- its `seed` / `arm_id` arguments are
     print labels only; `_make_adapter` and `torch.randperm` both draw from the AMBIENT
     global RNG. So repeated fits of the SAME subspace differ, and a "reference
     distribution over B random draws" mixes SUBSPACE-ORIENTATION variance with
     DECODER-TRAINING variance. This run separates them: B independent draws (both
     sources) against K refits of ONE FIXED draw (decoder source alone).
  2. The candidate readiness-gate formulas give OPPOSITE verdicts on seed 42, so the
     per-seed numbers for all six seeds are what a human needs to choose between them.

No warmup, no RRR on real receiver data: the randrank arm reads only the sender X and the
oracle labels y (see v1's docstring). r is PINNED per seed to the parsimonious rank
V3-EXQ-1043a actually recorded for that seed.
"""
import json
import os
import sys
import time
from pathlib import Path

REPO = Path(os.environ.get("REE_V3_ROOT", "/Users/dgolden/REE_Working/ree-v3"))
sys.path.insert(0, str(REPO))

import numpy as np
import torch

import experiments.v3_exq_1002_zworld_actor_adequacy_oracle_adapter as x1002
import experiments.v3_exq_734_env_difficulty_competence_recovery_sweep as x734
import experiments.v3_exq_1043a_mech537_communication_subspace_permutation_null as x1043a

MANIFEST = Path(os.environ.get("REE_ASSEMBLY_ROOT",
                               "/Users/dgolden/REE_Working/REE_assembly")) / ("evidence/experiments/"
                "v3_exq_1043a_mech537_communication_subspace_permutation_null_"
                "20260919T030056Z_v3.json")
B = 24          # independent random rank-r draws per seed
K_FIXED = 8     # refits of ONE fixed draw, to isolate decoder-training variance
OUT = Path(__file__).resolve().parent / "v3_exq_1043b_randrank_reference_smoke_20260920.json"

m = json.load(MANIFEST.open())
recorded = {int(r["seed"]): r for r in m["per_seed_results"]}
SEEDS = sorted(recorded)

t_all = time.time()
env_kwargs = x734._env_kwargs_for_rung(x1043a.RUNG)
action_dim = int(x734._make_env(SEEDS[0], env_kwargs).action_dim)

rows = []
for seed in SEEDS:
    rec = recorded[seed]
    r_pars = int(rec["parsimonious_rank"])
    t0 = time.time()
    ep_oracle = x1002._collect_episodes(seed, env_kwargs, "oracle",
                                        x1043a.BC_EPISODES, x1043a.STEPS_PER_EPISODE)
    tr_eps, te_eps = x1002._split_episodes(ep_oracle)
    x_tr, y_tr, _g = x1043a._ws250_features(tr_eps)
    x_te, y_te, _g2 = x1043a._ws250_features(te_eps)
    st = x1002._fit_standardiser(x_tr)
    xs_tr = x1002._apply_standardiser(x_tr, st)
    xs_te = x1002._apply_standardiser(x_te, st)
    keep = x1043a._live_sender_dims(st, x1043a.WORLD_STATE_DIM)
    n_live = int(keep.numel())
    trivial = x1043a._trivial_agreement(tr_eps, te_eps, y_tr, y_te, action_dim)
    strongest = float(trivial["strongest_trivial_agreement"])

    # PIPELINE FIDELITY CHECK against the landed run -- these three must match exactly,
    # or this probe is not reproducing 1043a's dataset and nothing below is comparable.
    fidelity = {
        "n_sender_dims_live": [n_live, int(rec["n_sender_dims_live"])],
        "heldout_steps": [int(xs_te.shape[0]), int(rec["heldout_steps"])],
        "strongest_trivial": [strongest,
                              float(rec["trivial_predictors"]["strongest_trivial_agreement"])],
    }
    ok = (fidelity["n_sender_dims_live"][0] == fidelity["n_sender_dims_live"][1]
          and fidelity["heldout_steps"][0] == fidelity["heldout_steps"][1]
          and abs(fidelity["strongest_trivial"][0] - fidelity["strongest_trivial"][1]) < 1e-9)
    print("seed %d r_pars=%d live=%d heldout=%d trivial=%.4f fidelity=%s (%.1fs)"
          % (seed, r_pars, n_live, int(xs_te.shape[0]), strongest,
             "OK" if ok else "MISMATCH", time.time() - t0), flush=True)

    def _fit(basis):
        f_tr = x1043a._project(xs_tr, basis)
        f_te = x1043a._project(xs_te, basis)
        net, _ts = x1002._train_adapter(f_tr, y_tr, action_dim, x1043a.ADAPTER_PASSES,
                                        seed, "randrank_smoke")
        return float(x1002._agreement(net, f_te, y_te))

    # ---- B independent draws (orientation + decoder variance) --------------------------
    draws, draw_seeds = [], []
    for b in range(B):
        ds = seed * 7919 + 131 + 1000 * b   # draw 0 IS 1043a's own recorded draw seed
        basis = x1043a._embed_basis(x1043a._random_orthonormal(n_live, r_pars, seed=ds),
                                    keep, x1043a.WORLD_STATE_DIM)
        draws.append(_fit(basis))
        draw_seeds.append(ds)
    # ---- K refits of ONE FIXED draw (decoder variance alone) ---------------------------
    fixed_basis = x1043a._embed_basis(
        x1043a._random_orthonormal(n_live, r_pars, seed=seed * 7919 + 131),
        keep, x1043a.WORLD_STATE_DIM)
    fixed = [_fit(fixed_basis) for _ in range(K_FIXED)]

    a = np.asarray(draws, float)
    f = np.asarray(fixed, float)
    sd_total = float(a.std(ddof=1))
    sd_dec = float(f.std(ddof=1))
    # Orientation component, by variance subtraction. Clamped at 0: a negative estimate
    # means the two are indistinguishable at this K, not that variance is negative.
    var_or = max(sd_total ** 2 - sd_dec ** 2, 0.0)
    row = {
        "seed": seed, "r_pars": r_pars, "n_sender_dims_live": n_live,
        "heldout_steps": int(xs_te.shape[0]), "strongest_trivial_agreement": strongest,
        "fidelity_vs_1043a": fidelity, "fidelity_ok": bool(ok),
        "recorded_1043a_randrank_parsrank": float(rec["agreements"]["ws250_randrank_parsrank"]),
        "recorded_1043a_comm_parsrank": float(rec["agreements"]["ws250_comm_parsrank"]),
        "draw_seeds": draw_seeds, "d_randrank_draws": draws,
        "d_randrank_mean": float(a.mean()), "d_randrank_sd_total": sd_total,
        "d_randrank_min": float(a.min()), "d_randrank_max": float(a.max()),
        "fixed_draw_refits": fixed, "d_randrank_sd_decoder_only": sd_dec,
        "d_randrank_sd_orientation_component": float(np.sqrt(var_or)),
        # the three candidate readiness-gate readings, per seed
        "gate_margin_single_draw_1043a": float(rec["agreements"]["ws250_randrank_parsrank"]
                                               - strongest),
        "gate_margin_draw_mean": float(a.mean() - strongest),
        "gate_margin_draw_max": float(a.max() - strongest),
        "gate_draw_spread_sd": sd_total,
        # where 1043a's recorded D_comm sits inside this seed's random-draw reference
        # distribution (RECORDED D_comm, from a DIFFERENT encoder-bearing run -- indicative
        # only, NOT a measurement of 1043b's statistic)
        "frac_draws_at_or_below_recorded_comm": float(
            (a <= float(rec["agreements"]["ws250_comm_parsrank"])).mean()),
        "c2_using_draw_mean_vs_recorded_comm": float(
            a.mean() - float(rec["agreements"]["ws250_comm_parsrank"])),
    }
    rows.append(row)
    print("  draws mean=%.4f sd_total=%.4f  fixed-draw sd_decoder=%.4f  "
          "sd_orientation=%.4f" % (a.mean(), sd_total, sd_dec,
                                   row["d_randrank_sd_orientation_component"]), flush=True)
    print("  gate margins: single(1043a)=%.4f  draw_mean=%.4f  draw_max=%.4f"
          % (row["gate_margin_single_draw_1043a"], row["gate_margin_draw_mean"],
             row["gate_margin_draw_max"]), flush=True)

res = {"B": B, "K_FIXED": K_FIXED, "seeds": SEEDS, "per_seed": rows,
       "total_seconds": float(time.time() - t_all),
       "box": "ree-cloud-4 linux-x86_64 torch %s py%s" % (torch.__version__,
                                                          sys.version.split()[0])}
OUT.write_text(json.dumps(res, indent=2))

print("\n==== SUMMARY ====", flush=True)
print("seed  r  single(1043a)  draw_mean  draw_max  sd_tot  sd_dec  sd_orient", flush=True)
for r in rows:
    print("%4d %3d       %+.4f    %+.4f   %+.4f  %.4f  %.4f   %.4f"
          % (r["seed"], r["r_pars"], r["gate_margin_single_draw_1043a"],
             r["gate_margin_draw_mean"], r["gate_margin_draw_max"],
             r["d_randrank_sd_total"], r["d_randrank_sd_decoder_only"],
             r["d_randrank_sd_orientation_component"]), flush=True)
for nm, key in (("single draw (1043a, the gate as shipped)", "gate_margin_single_draw_1043a"),
                ("draw MEAN over B", "gate_margin_draw_mean"),
                ("draw MAX over B", "gate_margin_draw_max")):
    v = [r[key] for r in rows]
    print("gate '%s' at floor 0.05: %d/6 seeds clear (worst %.4f)"
          % (nm, sum(1 for x in v if x >= 0.05), min(v)), flush=True)
print("wrote %s  total %.1fs" % (OUT, res["total_seconds"]), flush=True)
