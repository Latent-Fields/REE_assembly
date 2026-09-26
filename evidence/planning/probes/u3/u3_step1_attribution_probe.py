"""W3 step-1 rollout-norm-spike attribution probe (bt0925-u3, orchestrate-20260924-breakthrough-c2,
chip_ref chip-20260925-w3-step1-spike-attribution).

Question: gate_c_pool_controls_20260925.md (fc8340fb87) found the gate-(c) growth-leg FAIL is
driven entirely by STEP 1 of the H=30 rollout (first-step max == all-step max, every pool x
seed cell), and is GENERAL across proposer/no-proposer pools. This probe attributes THAT
step-1 spike (g1 = ||z_1||/||z_0|| under ref.e2.world_forward) to:
  (A) STATE      -- g1 vs ||z_0||, and vs distance of z_0 from the training-time z_world
                     distribution. Tests the "ratio artefact / regression-to-mean-norm of the
                     predictor" reading.
  (B) ACTION CLASS -- g1 by class 0..4 (4 = stay, structured_babbling.py "5-class env
                     includes stay = 4").
  (C) TRAINING   -- same readout on the UNTRAINED head (ref's own construction, before any
                     E2WorldMember update) and on the SHUF twin (w3_l2r_member_probe.py's
                     fixed-permutation retained-action relabelling, PERM = [1,2,3,4,0]).
  (D) TRUTH      -- the env's OWN true ||z_1||/||z_0|| at the same states for the same
                     actions: cloned env (copy.deepcopy, same pattern as
                     experiments/_lib/coupled_acceptance.py collect_probe_states), true next
                     obs encoded side-effect-free via that module's encode_next_side_effect_free
                     (I1 instrument 2; independently re-validated per state here, not merely
                     trusted from its own contract, see val_maxabs in the output).
                     If the true encoded next state ALSO grows ~1.7x, the "spike" is a correct
                     prediction, not instability.

Training recipe: byte-identical to w3_l2r_member_probe.py / gate_c_probe.py (E2WorldMember,
babble pre-phase into the FROZEN retained set + 3000 pre-updates, then 1200 native closed-loop
on-policy steps at 8 updates/step, 25% retained replay, re-encoded). Held-out states: SAME
protocol as gate_c_probe.py / gate_c_pool_controls_probe.py (BB.gen_policy at k0=300+,
pol_uniform(seed*11+17), one (z_world, z_self) per segment at rng(seed*97+5)-drawn tick) --
reimplemented here (gen_policy_env) to ALSO retain, per segment, a deep-copied env snapshot at
the segment's start, so the exact live env state at the picked tick can be reconstructed by
replaying that segment's OWN recorded actions (bit-identical env state to the original
generation: no extra RNG is consumed by the snapshot or the replay).

ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--n-states", type=int, default=20)
p.add_argument("--quick", action="store_true")
a = p.parse_args()

PROBES = Path("/Users/dgolden/REE_Working/REE_assembly/evidence/planning/probes")
sys.path.insert(0, str(PROBES / "babble"))
sys.path.insert(0, str(PROBES / "rollout"))
sys.path.insert(0, str(Path(a.wt) / "experiments"))
sys.path.insert(0, a.wt)
torch.set_num_threads(2)

import babble_probe as BB  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402
from ree_core.utils import waking_trainer as WT  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402
from experiments._lib.coupled_acceptance import (  # noqa: E402
    encode_next_side_effect_free, onehot, spearman,
)

S = a.seed
t0 = time.time()
PERM = [1, 2, 3, 4, 0]
A = 5

PRE_UPDATES = 30 if a.quick else 3000
N_BABBLE_EP = 2 if a.quick else 12
POST_STEPS = 200 if a.quick else 1200


def log(m):
    print("[u3 s%d t=%4.0fs] %s" % (S, time.time() - t0, m), flush=True)


assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__

R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
head_untrained = BP.get_head(ref)
Hh_cfg = int(ref.hippocampal.config.horizon)
log("ref.hippocampal deployed dims: H=%d K=%d WD=%d A=%d" % (
    Hh_cfg, int(ref.hippocampal.config.num_candidates),
    int(ref.hippocampal.config.world_dim), int(ref.hippocampal.config.action_dim)))


# ------------------------------------------------------------ train one arm ----
def train_arm(arm):
    agent = BB.fresh_agent(S, ref_enc)
    cfg = agent.config
    cfg.waking_trainer_guard_min_steps = 8
    member = WT.E2WorldMember(
        agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
        replay_frac=0.25, reencode_window=0, replay_latent="reencode",
        objective="mse", grad_clip=1.0, updates_per_step=1,
    )
    tr = WT.WakingTrainer(agent, cfg, members=[member])
    agent.waking_trainer = tr

    bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
    tr.set_e2_world_source("babble")
    tr.every_k = 10 ** 9
    counts = [0] * 5
    with torch.no_grad():
        for k in range(N_BABBLE_EP):
            env = BB.make_env(S, k)
            _f, od = env.reset(); agent.reset(); bab.reset()
            for _s in range(BB.EP_STEPS):
                agent.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                            obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
                act = bab.next_action()
                c = int(act.argmax()); counts[c] += 1
                agent.record_executed_action(act)
                _f, h, done, _i, od = env.step(c)
                tr.on_waking_step(float(h))
                if done:
                    _f, od = env.reset(); agent.reset(); bab.reset()
    if arm == "shuf":
        for r in member._retained:
            r["a"] = torch.nn.functional.one_hot(torch.tensor([PERM[int(r["a"].argmax())]]), 5).float()
    retained_n = len(member._retained)
    for _u in range(PRE_UPDATES):
        tr._update("e2_world", member)

    tr.set_e2_world_source("on_policy")
    tr.every_k = 1
    member.updates_per_step = 8
    agent.reset()
    R.seed_all(S + 500)
    train_zworld_norms = []
    for ep in range(POST_STEPS // BB.EP_STEPS):
        env = BB.make_env(S, 50 + ep)
        hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
        _f, od = env.reset(); agent.reset(); hh.reset()
        for _s in range(BB.EP_STEPS):
            r = hh.step(od)
            train_zworld_norms.append(float(r.latent.z_world.detach().norm()))
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); hh.reset()
    head_post = BP.get_head(agent)
    log("%s arm done: retained %d classes %s train_zworld_norm mean=%.3f std=%.3f" % (
        arm, retained_n, counts, float(np.mean(train_zworld_norms)), float(np.std(train_zworld_norms))))
    return head_post, train_zworld_norms


head_real, train_norms_real = train_arm("real")
head_shuf, train_norms_shuf = train_arm("shuf")

# ------------------------------------------------------- held-out states, with env replay ----
def gen_policy_env(seed, n_eps, k0, policy):
    """BB.gen_policy, bit-identical segs, ALSO returns a deep-copied env snapshot per segment
    (taken right after that segment's own env.reset(), before any of its actions)."""
    segs, env_snaps = [], []
    for ep in range(n_eps):
        env = BB.make_env(seed, k0 + ep)
        _f, od = env.reset()
        seg = {"obs": [BB.snap_obs(od)], "a": []}
        seg_env0 = copy.deepcopy(env)
        for _s in range(BB.EP_STEPS):
            ai = policy()
            _o, harm, done, info, od = env.step(ai)
            seg["a"].append(ai); seg["obs"].append(BB.snap_obs(od))
            if done:
                segs.append(seg); env_snaps.append(seg_env0)
                _f, od = env.reset()
                seg = {"obs": [BB.snap_obs(od)], "a": []}
                seg_env0 = copy.deepcopy(env)
        segs.append(seg); env_snaps.append(seg_env0)
    return segs, env_snaps


te_segs, env_snaps = gen_policy_env(S, a.n_states, 300, BB.pol_uniform(S * 11 + 17))
g = np.random.default_rng(S * 97 + 5)

states = []  # each: z0, s0, z0_norm, z_true[5], val_maxabs (or None)
for seg, env0 in zip(te_segs, env_snaps):
    if len(seg["a"]) < 1:
        continue
    t_pick = int(g.integers(0, len(seg["obs"])))
    ref.reset()
    lat_at_pick = None
    lat_next_live = None
    with torch.no_grad():
        for ti, o in enumerate(seg["obs"]):
            lat = ref.sense(o["body_state"], o["world_state"], obs_harm=o.get("harm_obs"),
                             obs_harm_a=o.get("harm_obs_a"), obs_harm_history=o.get("harm_history"))
            if ti == t_pick:
                lat_at_pick = lat
            elif ti == t_pick + 1:
                lat_next_live = lat
                break
    z0 = lat_at_pick.z_world.detach().clone()
    s0 = lat_at_pick.z_self.detach().clone()

    # reconstruct the exact live env state at t_pick by replaying this segment's own actions
    env_at_pick = copy.deepcopy(env0)
    for ai in seg["a"][:t_pick]:
        env_at_pick.step(ai)

    z_true = []
    with torch.no_grad():
        for c in range(A):
            ec = copy.deepcopy(env_at_pick)
            _f, _h, _d, _i, obs_next = ec.step(c)
            z_true.append(encode_next_side_effect_free(ref, obs_next, lat_at_pick, onehot(c, A))
                          .reshape(-1).clone())

    val_maxabs = None
    if lat_next_live is not None and t_pick < len(seg["a"]):
        executed_c = int(seg["a"][t_pick])
        val_maxabs = float((z_true[executed_c] - lat_next_live.z_world.detach().reshape(-1)).abs().max())

    states.append({
        "z0": z0, "s0": s0, "z0_norm": float(z0.norm()),
        "z_true": z_true, "val_maxabs": val_maxabs,
    })

log("collected %d held-out states (k0=300, disjoint from training k-ranges); "
    "validated %d against the next live tick" % (
        len(states), sum(1 for s in states if s["val_maxabs"] is not None)))


# ---------------------------------------------------------------- readout ----
def g1_table(head, states):
    """Per state, per class: g1 = ||world_forward(z0, onehot(c))|| / ||z0||."""
    BP.set_head(ref, head)
    out = np.zeros((len(states), A), dtype=float)
    with torch.no_grad():
        for si, st in enumerate(states):
            z0 = st["z0"]
            for c in range(A):
                z1 = ref.e2.world_forward(z0, onehot(c, A))
                out[si, c] = float(z1.norm() / max(float(z0.norm()), 1e-9))
    return out


g1_real = g1_table(head_real, states)
g1_shuf = g1_table(head_shuf, states)
g1_untrained = g1_table(head_untrained, states)

z0_norms = np.asarray([st["z0_norm"] for st in states])
g1_true = np.zeros((len(states), A), dtype=float)
for si, st in enumerate(states):
    n0 = max(st["z0_norm"], 1e-9)
    for c in range(A):
        g1_true[si, c] = float(st["z_true"][c].norm()) / n0

val_vals = [st["val_maxabs"] for st in states if st["val_maxabs"] is not None]

# (A) STATE: g1(real) vs ||z0|| and vs nearest-neighbor distance from the training z_world pool
max_g1_real_per_state = g1_real.max(axis=1)
train_pool = np.asarray((train_norms_real[::4] if len(train_norms_real) > 400 else train_norms_real))
# proxy: |z0_norm - nearest training-time norm| (cheap 1-D nearest-neighbor-in-norm proxy;
# a full nearest-neighbor-in-z-space would need the training z vectors, not saved here)
nn_dist_norm = np.asarray([float(np.min(np.abs(train_pool - n))) for n in z0_norms])

corr_g1_vs_z0norm = spearman(z0_norms.tolist(), max_g1_real_per_state.tolist())
corr_g1_vs_nndist = spearman(nn_dist_norm.tolist(), max_g1_real_per_state.tolist())

# (B) ACTION CLASS
per_class_real = {str(c): {"median": float(np.median(g1_real[:, c])), "max": float(np.max(g1_real[:, c])),
                            "mean": float(np.mean(g1_real[:, c]))} for c in range(A)}
per_class_true = {str(c): {"median": float(np.median(g1_true[:, c])), "max": float(np.max(g1_true[:, c])),
                            "mean": float(np.mean(g1_true[:, c]))} for c in range(A)}
worst_class_real = int(np.argmax(g1_real.max(axis=0)))
worst_class_true = int(np.argmax(g1_true.max(axis=0)))

# (C) TRAINING: untrained + shuf twin, pooled
def pooled(mat):
    return {"median": float(np.median(mat)), "max": float(np.max(mat)), "mean": float(np.mean(mat))}


# (D) TRUTH vs REAL prediction, pooled and per (state,class) correlation
flat_real = g1_real.reshape(-1)
flat_true = g1_true.reshape(-1)
corr_real_vs_true = spearman(flat_real.tolist(), flat_true.tolist())
abs_diff = np.abs(flat_real - flat_true)

# state/class of the single worst REAL g1 cell, cross-referenced against TRUE at that same cell
worst_idx = int(np.argmax(g1_real))
worst_si, worst_c = divmod(worst_idx, A)

out = {
    "seed": S, "n_states": len(states), "quick": bool(a.quick),
    "hippocampal_horizon_cfg": Hh_cfg,
    "instrument_validation": {
        "n_validated": len(val_vals),
        "max_abs_diff": (float(np.max(val_vals)) if val_vals else None),
        "note": "encode_next_side_effect_free vs the next live agent.sense() tick, on the "
                "EXECUTED action only (per collect_probe_states/probe_state_validation "
                "convention); re-derived on THIS probe's own states, not merely cited from "
                "the I1 contract.",
    },
    "state_A": {
        "corr_g1max_vs_z0norm_spearman": corr_g1_vs_z0norm,
        "corr_g1max_vs_nn_train_norm_dist_spearman": corr_g1_vs_nndist,
        "z0_norm": {"min": float(z0_norms.min()), "median": float(np.median(z0_norms)),
                    "max": float(z0_norms.max())},
        "train_zworld_norm_real": {"mean": float(np.mean(train_norms_real)),
                                    "std": float(np.std(train_norms_real)),
                                    "min": float(np.min(train_norms_real)),
                                    "max": float(np.max(train_norms_real))},
        "worst_state_z0_norm": float(z0_norms[worst_si]),
        "worst_state_z0_norm_percentile_vs_trainpool": float(
            100.0 * np.mean(train_pool <= z0_norms[worst_si])),
    },
    "class_B": {
        "real": per_class_real, "true": per_class_true,
        "worst_class_real": worst_class_real, "worst_class_true": worst_class_true,
    },
    "training_C": {
        "real": pooled(g1_real), "shuf": pooled(g1_shuf), "untrained": pooled(g1_untrained),
        "shuf_per_class": {str(c): pooled(g1_shuf[:, c]) for c in range(A)},
        "untrained_per_class": {str(c): pooled(g1_untrained[:, c]) for c in range(A)},
    },
    "truth_D": {
        "real": pooled(g1_real), "true": pooled(g1_true),
        "corr_real_vs_true_spearman": corr_real_vs_true,
        "mean_abs_diff_real_minus_true": float(np.mean(abs_diff)),
        "max_abs_diff_real_minus_true": float(np.max(abs_diff)),
        "worst_real_cell": {"state_idx": worst_si, "class": worst_c,
                             "g1_real": float(g1_real[worst_si, worst_c]),
                             "g1_true": float(g1_true[worst_si, worst_c]),
                             "z0_norm": float(z0_norms[worst_si])},
    },
    "t_total_s": time.time() - t0,
}
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE -> %s" % a.out)
log("SUMMARY real=%.4f/%.4f true=%.4f/%.4f shuf=%.4f/%.4f untrained=%.4f/%.4f "
    "corr(g1max,z0norm)=%s corr(real,true)=%s val_max=%s" % (
        out["truth_D"]["real"]["median"], out["truth_D"]["real"]["max"],
        out["truth_D"]["true"]["median"], out["truth_D"]["true"]["max"],
        out["training_C"]["shuf"]["median"], out["training_C"]["shuf"]["max"],
        out["training_C"]["untrained"]["median"], out["training_C"]["untrained"]["max"],
        corr_g1_vs_z0norm, corr_real_vs_true, out["instrument_validation"]["max_abs_diff"]))
