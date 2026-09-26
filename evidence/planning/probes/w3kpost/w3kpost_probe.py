"""Probe (bt0926-w3kpost): is W3's k=10 (beats persistence at all 10 horizons,
fix OFF) carried by near-reset ticks? Re-score evaluate()'s own readout
(disc4, k, per-horizon err/persistence ratio) restricted to held-out ticks
with ticks-since-reset >= 8, vs < 8, vs all -- for the SAME per-start rollouts
already computed (no extra rollout, no extra RNG draw), on 6 of the 15 seeds
bt0926-w3rel registered (901-915): 902, 904, 912 (OFF-pass) and 903, 906, 909
(OFF-miss), all in the benign A1 stratum (avoids the 901/905/908/913/914
hazard-trapped cost blowup to keep this probe's wall time small).

Pre-registration: chip-20260926-w3-k-excluding-reset-ticks (Z_w3kpost.md).
Recipe reused BYTE-IDENTICALLY from probes/w3relon/w3relon_probe.py
(bt0926-w3relon), itself reused from probes/w3rel/w3rel_probe.py (bt0926-w3rel):
babbling 2400 steps (StructuredBabbler, 5 classes incl. stay, k=0..11) ->
FROZEN retained set -> 3000 member updates (pre) -> 1200 native closed-loop
StepHarness steps (k=50.., 8 member updates/step, 25% retained mix,
re-encoded) -> evaluate() on the held-out disc4/disc5 test set (3000 uniform
{0..3}, k=120..134). --knob true/false controls
LatentStackConfig.use_zworld_ema_reset_init exactly as w3relon_probe.py wired
it (live for the WHOLE pipeline: ref's config before held-out-state
generation, and each arm's training agent's config before babbling starts).

SCOPE REDUCTION vs w3relon_probe.py (stated, not silent): this probe skips
the B0 phase (babble_probe's on-policy-data head) and the shuf arm entirely.
Neither is part of this probe's question (the k==10 conjunct is read off the
REAL arm's post-phase evaluate() only; B0 is a pre-training predictor, not a
readout). Skipping them is SAFE for bit-exact reproduction of the real arm's
post-phase numbers because BB.fresh_agent(seed, ref_enc) unconditionally
re-seeds (R.seed_all(seed)) at its own top every time it is called, so the
real arm's RNG state at the point BB.fresh_agent(S, ref_enc) is called for the
real arm does not depend on whatever ran before it in this process (verified
by the P1 canary below, not merely assumed).

evaluate_tagged()/pool_evaluate() below duplicate babble_probe.evaluate()'s
own per-start rollout and aggregation logic EXACTLY (same rng seed+77 draw,
same starts sampling, same per-horizon median-err/median-pers streak rule for
k, same disc4 argmin-over-CLASSES rule) but keep every start's own tick index
t (== ticks-since-reset, per gate_c_ema_reset_init_probe.py's P3 finding that
BB.gen_policy's per-segment tick index is ticks-since-that-episode's-own-reset,
and BB.encode_segs calls ref.reset() at the start of every segment it encodes,
so t=0 is always the first ref.sense() after a reset here too) instead of
immediately pooling across all of them. This lets ONE set of rollouts (no
extra compute, no extra RNG draw) be re-pooled three ways: all ticks (must
reproduce babble_probe.evaluate()'s own committed numbers bit-exact -- the
canary), ticks with t >= 8 only, ticks with t < 8 only.

ASCII output only.
"""
from __future__ import annotations

import argparse, copy, json, sys, time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--seeds", required=True, help="comma-separated seed list")
p.add_argument("--wt", required=True)
p.add_argument("--out-dir", required=True)
p.add_argument("--tag", required=True, help="output filename prefix, e.g. OFF or ON")
p.add_argument("--knob", choices=["true", "false"], required=True)
p.add_argument("--post", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--budget-s", type=float, default=900.0, help="stop starting new seeds once this much wall time has elapsed")
a = p.parse_args()

KNOB = (a.knob == "true")
SEEDS = [int(s) for s in a.seeds.split(",") if s.strip()]

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
from experiments._lib import coupled_acceptance as CA  # noqa: E402
from ree_core.utils import waking_trainer as WT  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__

t_batch0 = time.time()
completed = []

H_DEFAULT = 10
MAX_STARTS = 300
A_ENV = BB.A_ENV
CLASSES = BB.CLASSES
TICK_SPLIT = 8  # brief: ticks-since-reset >= 8 vs < 8


def log(S, m):
    print("[w3kpost %s s%d t=%4.0fs] %s" % (a.tag, S, time.time() - t_batch0, m), flush=True)


@torch.no_grad()
def evaluate_tagged(ref, head, te, key, seed, H=H_DEFAULT, max_starts=MAX_STARTS):
    """Exact duplicate of babble_probe.evaluate()'s per-start rollout logic,
    but returns the per-start (i, t, err[h], pers[h], disc4[h], disc5_1)
    records instead of immediately pooling them, so the SAME rollouts can be
    re-pooled by a tick-index filter with no extra compute or RNG draw."""
    BP.set_head(ref, head)
    e2 = ref.e2
    g = np.random.default_rng(seed + 77)
    starts = [(i, t) for i, e in enumerate(te) for t in range(e["a"].shape[0] - H + 1)]
    if len(starts) > max_starts:
        starts = [starts[j] for j in sorted(g.choice(len(starts), max_starts, replace=False))]
    zs = torch.zeros(1, 32)
    per_start = []
    for i, t in starts:
        x = te[i][key]
        acts = F.one_hot(te[i]["a"][t:t + H], A_ENV).float().unsqueeze(0)
        x0 = x[t:t + 1]
        tr = e2.rollout_with_world(zs, x0, acts, compute_action_objects=False)
        err, pers = {}, {}
        for h in range(1, H + 1):
            y = x[t + h:t + h + 1]
            err[h] = float((tr.world_states[h] - y).norm())
            pers[h] = float((x0 - y).norm())
        ex = int(te[i]["a"][t])
        disc4, disc5_1 = {}, None
        for h in (1, 3, 5):
            y = x[t + h:t + h + 1]
            errs = []
            for c in range(A_ENV):
                a2 = acts[:, :h].clone(); a2[0, 0] = 0.0; a2[0, 0, c] = 1.0
                errs.append(float((e2.rollout_with_world(zs, x0, a2, compute_action_objects=False).world_states[h] - y).norm()))
            e4 = [errs[c] for c in CLASSES]
            disc4[h] = (int(np.argmin(e4)) == CLASSES.index(ex))
            if h == 1:
                disc5_1 = (int(np.argmin(errs)) == ex)
        per_start.append({"i": i, "t": t, "err": err, "pers": pers, "disc4": disc4, "disc5_1": disc5_1})
    return per_start


def pool_evaluate(per_start, H=H_DEFAULT):
    """Exact duplicate of babble_probe.evaluate()'s pooling/streak logic,
    applied to whatever subset of per_start records it is given."""
    n = len(per_start)
    rows = {h: {"err": [], "pers": []} for h in range(1, H + 1)}
    disc4 = {1: [], 3: [], 5: []}
    disc5 = {1: []}
    for ps in per_start:
        for h in range(1, H + 1):
            rows[h]["err"].append(ps["err"][h])
            rows[h]["pers"].append(ps["pers"][h])
        for h in (1, 3, 5):
            disc4[h].append(ps["disc4"][h])
        disc5[1].append(ps["disc5_1"])
    k = 0
    eop = {}
    for h in range(1, H + 1):
        if len(rows[h]["err"]) == 0:
            eop[h] = None
            continue
        me, mp = float(np.median(rows[h]["err"])), float(np.median(rows[h]["pers"]))
        eop[h] = me / mp if mp > 0 else None
        if mp > 0 and me < mp and k == h - 1:
            k = h
    return {
        "n_starts": n,
        "disc4_h1": float(np.mean(disc4[1])) if disc4[1] else None,
        "disc4_h3": float(np.mean(disc4[3])) if disc4[3] else None,
        "disc4_h5": float(np.mean(disc4[5])) if disc4[5] else None,
        "disc5_h1": float(np.mean(disc5[1])) if disc5[1] else None,
        "k": k,
        "err_over_pers_h1": eop[1],
        "err_over_pers_h5": eop[5],
        "err_over_pers_all": eop,
    }


def three_way(per_start, H=H_DEFAULT, split=TICK_SPLIT):
    all_ = pool_evaluate(per_start, H)
    ge8 = pool_evaluate([p for p in per_start if p["t"] >= split], H)
    lt8 = pool_evaluate([p for p in per_start if p["t"] < split], H)
    return {"all": all_, "ge8": ge8, "lt8": lt8}


def run_seed(S):
    t0 = time.time()
    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    ref.latent_stack.config.use_zworld_ema_reset_init = bool(KNOB)
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    init = BP.get_head(ref)
    te_segs, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
    TE = BB.encode_segs(ref, te_segs)
    ev_init = BB.evaluate(ref, init, TE, "z", S)
    log(S, "INIT disc4 %.4f k %d knob=%s" % (ev_init["disc4_h1"], ev_init["k"], KNOB))

    log(S, "== arm real (B0/shuf skipped -- see script docstring scope note) ==")
    agent = BB.fresh_agent(S, ref_enc)
    agent.latent_stack.config.use_zworld_ema_reset_init = bool(KNOB)
    cfg = agent.config
    cfg.waking_trainer_guard_min_steps = 8
    member = WT.E2WorldMember(agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
                              replay_frac=0.25, reencode_window=0, replay_latent="reencode",
                              objective="mse", grad_clip=1.0, updates_per_step=1)
    tr = WT.WakingTrainer(agent, cfg, members=[member])
    agent.waking_trainer = tr

    bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
    tr.set_e2_world_source("babble")
    tr.every_k = 10 ** 9
    counts_bab = [0] * 5
    with torch.no_grad():
        for k in range(12):
            env = BB.make_env(S, k)
            _f, od = env.reset(); agent.reset(); bab.reset()
            for _s in range(BB.EP_STEPS):
                agent.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                            obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
                act = bab.next_action()
                c = int(act.argmax()); counts_bab[c] += 1
                agent.record_executed_action(act)
                _f, h, done, _i, od = env.step(c)
                tr.on_waking_step(float(h))
                if done:
                    _f, od = env.reset(); agent.reset(); bab.reset()
    retained_n = len(member._retained)
    snap = [(r["step"], r["a"].clone(), r["obs"][-1][1].clone()) for r in member._retained]
    for _u in range(3000):
        tr._update("e2_world", member)
    ev_pre = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
    log(S, "pre disc4 %.4f k %d" % (ev_pre["disc4_h1"], ev_pre["k"]))

    tr.set_e2_world_source("on_policy")
    tr.every_k = 1
    member.updates_per_step = a.ups
    agent.reset()
    R.seed_all(S + 500)
    dones_all = []
    for ep in range(a.post // BB.EP_STEPS):
        env = BB.make_env(S, 50 + ep)
        hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
        _f, od = env.reset(); agent.reset(); hh.reset()
        for _s in range(BB.EP_STEPS):
            r = hh.step(od)
            dones_all.append(bool(r.done))
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); hh.reset()
    head_post = BP.get_head(agent)

    # standard (unfiltered) evaluate() call -- this IS the canary target: must
    # reproduce babble_probe.evaluate()'s own committed numbers bit-exact.
    ev_post_std = BB.evaluate(ref, head_post, TE, "z", S)
    # tagged re-derivation of the SAME rollouts, for the tick-split re-pool
    per_start = evaluate_tagged(ref, head_post, TE, "z", S)
    tw = three_way(per_start)

    canary_match = (
        abs(tw["all"]["disc4_h1"] - ev_post_std["disc4_h1"]) < 1e-12
        and tw["all"]["k"] == ev_post_std["k"]
        and abs(tw["all"]["err_over_pers_h1"] - ev_post_std["err_over_pers_h1"]) < 1e-12
    )

    frozen_ok = len(snap) == len(member._retained) and all(
        s == rr["step"] and torch.equal(aa, rr["a"]) and torch.equal(o, rr["obs"][-1][1])
        for (s, aa, o), rr in zip(snap, member._retained))

    stratum = CA.classify_stratum(dones_all, window=min(600, len(dones_all)))

    n_ge8 = tw["ge8"]["n_starts"]
    n_lt8 = tw["lt8"]["n_starts"]
    n_all = tw["all"]["n_starts"]

    res = {
        "seed": S, "knob": KNOB, "post_n": a.post,
        "init": ev_init,
        "pre": {"disc4_h1": ev_pre["disc4_h1"], "k": ev_pre["k"]},
        "post_std": ev_post_std,
        "post_tagged": tw,
        "n_starts_all": n_all, "n_starts_ge8": n_ge8, "n_starts_lt8": n_lt8,
        "frac_lt8": n_lt8 / n_all if n_all else None,
        "canary_match_std_vs_tagged_all": canary_match,
        "gate_a_all": bool(tw["all"]["disc4_h1"] >= 0.47 and tw["all"]["k"] == 10),
        "gate_a_ge8": bool(tw["ge8"]["disc4_h1"] is not None and tw["ge8"]["disc4_h1"] >= 0.47 and tw["ge8"]["k"] == 10),
        "guard": {kk: v.status for kk, v in tr.guard_results.items()},
        "frozen_retained_unchanged_after_post": frozen_ok,
        "retained_n": retained_n,
        "hazard_stratum_A1": stratum,
        "t_seed_s": time.time() - t0,
    }
    log(S, "RESULT post disc4_h1=%.4f k=%d gate_a=%s || ge8 disc4_h1=%s k=%s gate_a=%s || lt8 disc4_h1=%s k=%s || n_all=%d n_ge8=%d n_lt8=%d canary=%s" % (
        ev_post_std["disc4_h1"], ev_post_std["k"], res["gate_a_all"],
        ("%.4f" % tw["ge8"]["disc4_h1"]) if tw["ge8"]["disc4_h1"] is not None else "NA", tw["ge8"]["k"], res["gate_a_ge8"],
        ("%.4f" % tw["lt8"]["disc4_h1"]) if tw["lt8"]["disc4_h1"] is not None else "NA", tw["lt8"]["k"],
        n_all, n_ge8, n_lt8, canary_match))

    out = {"seed": S, "post": a.post, "knob": KNOB, "result": res, "t_total_s": time.time() - t0}
    outp = Path(a.out_dir) / ("%s_s%d.json" % (a.tag, S))
    json.dump(out, open(outp, "w"), indent=1, default=str)
    log(S, "DONE t_seed=%.0fs -> %s" % (time.time() - t0, outp))
    return out


for S in SEEDS:
    if time.time() - t_batch0 > a.budget_s:
        print("[w3kpost %s BUDGET] stopping before seed %d, elapsed %.0fs > budget %.0fs" % (
            a.tag, S, time.time() - t_batch0, a.budget_s), flush=True)
        break
    out = run_seed(S)
    completed.append(S)

print("[w3kpost %s BATCH DONE] completed=%s t_total=%.0fs" % (
    a.tag, completed, time.time() - t_batch0), flush=True)
