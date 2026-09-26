"""Probe N3POST (bt0926-n3post, orchestrate-20260924-breakthrough-c2,
chip-20260926-n3-gate-a-reset-confound).

Is N3's W4 gate (a) pass (DISC_0.5, Spearman J_pred vs J_true, 4/5 seeds,
n3_e3_aggregation_probe_20260925.md, 9608f3117a) confounded by near-reset
probe states, the same way W3's k criterion was (GFLAG-0560,
w3_k_excluding_reset_ticks_20260926.md)?

Pre-registration: REE_assembly/evidence/planning/n3_gate_a_reset_confound_20260926.md
(committed BEFORE any registered seed ran). One invocation = one seed, one
knob setting (OFF or ON).

This is N3's own probe (probes/n3/n3_probe.py, REUSED byte-identically for
every function it defines: train_member, blind_exact, eval_tew, depth_scores,
aggregate, score_head, tie_set, flip_vs_ref, spearman_n3pre, metrics,
habit_contrast) with exactly two additions:
  1. probe-state collection is replaced by a LOCAL copy of I1's
     collect_probe_states (coupled_acceptance.py) that additionally records
     each state's ticks-since-reset (the StepHarness `step` kwarg the hook
     already receives, which IS ticks-since-last-reset -- StepHarness.reset()
     zeroes _step_count and it increments once per h.step() call, read at
     on_action time before that increment; same reasoning as
     w3_k_excluding_reset_ticks_20260926.md P1, applied to N3's continuous
     320-step native-waking probe run instead of a segmented held-out set).
  2. an optional fix-ON knob (env var N3POST_FIXON=1) that, right after every
     agent construction (ref and every BB.fresh_agent call, via a monkeypatch
     of babble_probe.fresh_agent so train_member/collect need no edits), sets
     agent.config.latent.use_zworld_ema_reset_init = True (SD-008,
     zworld_ema_reset_init_build_20260926.md). No ree_core edits: this is the
     same attribute REEConfig.from_dims sets, applied post-construction.

WT (the ree-v3 worktree) is read from env var N3POST_WT so the SAME script
runs against both the OFF worktree (tag archive/coupled-loop-repair-042895a)
and the ON worktree (that tag + 298cb8ffd3 cherry-picked).

ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import sys
import time
import types
from collections import Counter
from pathlib import Path

import numpy as np

WT = Path(os.environ.get("N3POST_WT", "/Users/dgolden/REE_Working/.scratch/wt-n3post"))
FIXON = bool(int(os.environ.get("N3POST_FIXON", "0")))
N3DIR = Path("/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n3")  # REUSE n3_probe.py fns
PROBES = Path("/Users/dgolden/REE_Working/REE_assembly/evidence/planning/probes")
sys.path.insert(0, str(PROBES / "babble"))
sys.path.insert(0, str(PROBES / "rollout"))
sys.path.insert(0, str(WT / "experiments"))
sys.path.insert(0, str(WT))
sys.path.insert(0, str(N3DIR))

import torch  # noqa: E402
import torch.nn.functional as F  # noqa: E402

torch.set_num_threads(2)

import babble_probe as BB  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
from experiments._harness import StepHarness, StepHooks  # noqa: E402
from experiments._lib import coupled_acceptance as CA  # noqa: E402
from ree_core.predictors.e2_fast import Trajectory  # noqa: E402
from ree_core.utils import waking_trainer as WTR  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

# REUSE n3_probe.py's own functions byte-identically. Loaded by exec (not a plain
# `import n3_probe`) with exactly ONE textual substitution: its hardcoded
# `WT = Path(".../.scratch/wt-n3")` constant is replaced with THIS run's WT (the
# n3post worktree, OFF or ON) before its own module-level self-check asserts run
# (`assert ...WTR.__file__... startswith(str(WT...))`) -- those assert that its
# imports resolve under n3_probe.py's OWN worktree, which is correct behaviour
# but points at a worktree this run does not use (and which no longer exists --
# N3 proper's throwaway worktree was removed at session close per COMMON.md rule
# 3). No other line is touched: every function body (train_member, eval_tew,
# depth_scores, aggregate, score_head, metrics, habit_contrast, ...) is
# byte-identical to the committed probes/n3/n3_probe.py.
_N3_SRC_PATH = N3DIR / "n3_probe.py"
_n3_src = _N3_SRC_PATH.read_text()
_old_wt_line = 'WT = Path("/Users/dgolden/REE_Working/.scratch/wt-n3")'
assert _old_wt_line in _n3_src, "n3_probe.py's WT line text changed -- update the substitution"
_n3_src = _n3_src.replace(_old_wt_line, "WT = Path(%r)" % str(WT))
N3 = types.ModuleType("n3_probe_loaded")
N3.__file__ = str(_N3_SRC_PATH)
exec(compile(_n3_src, str(_N3_SRC_PATH), "exec"), N3.__dict__)  # noqa: S102

A_ENV = N3.A_ENV
EP_STEPS = N3.EP_STEPS
HMAX = N3.HMAX
AGGS = N3.AGGS
TIE_REL = N3.TIE_REL
train_member = N3.train_member
blind_exact = N3.blind_exact
eval_tew = N3.eval_tew
depth_scores = N3.depth_scores
aggregate = N3.aggregate
score_head = N3.score_head
tie_set = N3.tie_set
flip_vs_ref = N3.flip_vs_ref
spearman_n3pre = N3.spearman_n3pre
metrics = N3.metrics
habit_contrast = N3.habit_contrast

assert str(Path(WTR.__file__).resolve()).startswith(str(WT.resolve())), WTR.__file__
assert str(Path(CA.__file__).resolve()).startswith(str(WT.resolve())), CA.__file__
assert hasattr(WTR, "E2WorldMember")
CODE_SHA_OFF = "042895a3a2be3a54e5a74199e8e3950cc058cb31"
CODE_SHA_ON = "f361c336a19d3e44179af6b36070c911296c00a1"  # 042895a + 298cb8ffd3 cherry-picked


def _apply_fix(agent):
    if FIXON:
        agent.config.latent.use_zworld_ema_reset_init = True
    return agent


# n3_probe.train_member / collect both call babble_probe.fresh_agent(seed, ref_enc)
# to build every agent (the pre-phase agent AND the post-phase agent inside
# train_member; the probe agent inside collect()). Monkeypatch at that single
# choke point so train_member/collect are reused UNCHANGED for both arms; the
# patch matches n3_probe.BB (the same babble_probe module object, imported
# separately here but resolving to the same file under WT).
_orig_fresh_agent = BB.fresh_agent


def _patched_fresh_agent(seed, ref_enc):
    return _apply_fix(_orig_fresh_agent(seed, ref_enc))


BB.fresh_agent = _patched_fresh_agent
N3.BB.fresh_agent = _patched_fresh_agent
assert N3.BB is BB, "n3_probe imports the same babble_probe module object"


# ------------------------------------------------------------------ tagged probe states (I1 + ticks_since_reset)
def onehot(c, action_dim):
    return CA.onehot(c, action_dim)


def collect_probe_states_tagged(agent, env, steps, every, seed, *, action_dim=None,
                                 with_q=True, n_cont=6, cont_len=4, with_pool=True):
    """Local copy of CA.collect_probe_states (instrument 2), unchanged except for one
    added field: st["ticks_since_reset"] = the `step` kwarg StepHarness's on_action
    hook already receives. StepHarness.reset() zeroes _step_count; it increments once
    per h.step() call, AFTER on_action fires (agent.py:_harness.py step(), point 11
    "plumbing rotate" runs after point 8 "on_action hook"). So `step` at on_action time
    equals ticks since the last h.reset() (env.reset()/agent.reset() boundary) --
    exactly ticks-since-reset for that probe state. Same reasoning as
    w3_k_excluding_reset_ticks_20260926.md P1, re-derived here for THIS driver
    (StepHarness's own _step_count, not babble_probe's segment/tick indexing)."""
    A = int(action_dim if action_dim is not None else agent.e2.config.action_dim)
    g = np.random.default_rng(seed + 31)
    states = []
    pend = {}

    def on_action(agent, latent, action, obs_dict, ticks, step, **_k):
        if step % every != 0:
            return
        lat_s = agent._current_latent
        z0, s0 = latent.z_world.detach().clone(), latent.z_self.detach().clone()
        zt = []
        for c in range(A):
            e = copy.deepcopy(env)
            zt.append(CA.encode_next_side_effect_free(agent, e.step(c)[4], lat_s, onehot(c, A)))
        a_ex = action.detach().reshape(1, -1).float()
        e = copy.deepcopy(env)
        st = {"z0": z0, "s0": s0, "z_true": zt,
              "executed": int(a_ex.argmax()),
              "exec_is_onehot": bool(float(a_ex.max()) > 0.99 and float(a_ex.abs().sum()) < 1.01),
              "z_exact_exec": CA.encode_next_side_effect_free(agent, e.step(action)[4], lat_s, a_ex),
              "ticks_since_reset": int(step)}
        if with_q:
            st["q"] = CA.env_q_values(env, A, g, n_cont, cont_len)
        if with_pool:
            rs = torch.get_rng_state()
            with torch.no_grad():
                pool = agent.hippocampal.propose_trajectories(z0, z_self=s0)
            torch.set_rng_state(rs)
            st["pool_actions"] = [p.actions.detach().clone() for p in pool]
        pend["i"] = len(states)
        states.append(st)

    h = StepHarness(agent, env, train_mode=False, seed=seed, hooks=StepHooks(on_action=on_action))
    _f, obs = env.reset(); agent.reset(); h.reset()
    n = 0
    while n < steps:
        pend.pop("i", None)
        r = h.step(obs); n += 1
        i = pend.get("i")
        obs = r.next_obs_dict
        if i is not None and not r.done and n < steps:
            r2 = h.step(obs); n += 1
            st = states[i]
            st["validation_exact_maxabs"] = float((r2.latent.z_world - st["z_exact_exec"]).abs().max())
            if st["exec_is_onehot"]:
                st["validation_maxabs"] = float((r2.latent.z_world - st["z_true"][st["executed"]]).abs().max())
            obs = r2.next_obs_dict
            r = r2
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    return states


def metrics_subset(rows_h, states, idxs):
    """metrics() restricted to a subset of (rows_h, states), same index order.
    refs={} because gate (c) (BLIND/BLINDR flip) is out of scope here (brief:
    gate (a) only); metrics() no-ops its ref loop on an empty dict."""
    rs = [rows_h[i] for i in idxs]
    ss = [states[i] for i in idxs]
    return metrics(rs, {}, ss)


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--post", type=int, default=1200)
    ap.add_argument("--ups", type=int, default=8)
    ap.add_argument("--probe-steps", type=int, default=320)
    ap.add_argument("--probe-every", type=int, default=8)
    ap.add_argument("--ncont", type=int, default=6)
    ap.add_argument("--clen", type=int, default=4)
    ap.add_argument("--reset-tick-bar", type=int, default=8)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    S = a.seed
    res = {"args": vars(a), "fixon": FIXON, "wt": str(WT),
           "code_sha": CODE_SHA_ON if FIXON else CODE_SHA_OFF}

    def log(msg):
        print("[n3post s%d fixon=%d t=%4.0fs] %s" % (S, FIXON, time.time() - t0, msg), flush=True)

    ce = CA.canary_e3_structure(seed=S)
    cd = CA.canary_action_discrimination(seed=S)
    res["canary_e3_structure"] = bool(ce["reproduced"])
    res["canary_action_discrimination"] = bool(cd.get("reproduced", False))
    log("I1 canaries e3_structure=%s action_discrimination=%s" % (res["canary_e3_structure"], res["canary_action_discrimination"]))

    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    _apply_fix(ref)
    ref.eval()
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    init = BP.get_head(ref)
    te4_segs, _ = BB.gen_policy(S, 3000 // EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
    g5 = np.random.default_rng(S * 7 + 5)
    tew_segs, _ = BB.gen_policy(S, 3000 // EP_STEPS, 160, lambda: int(g5.integers(0, 5)))
    TE4 = BB.encode_segs(ref, te4_segs)
    TEW = BB.encode_segs(ref, tew_segs)

    heads, res["heads"] = {"INIT": init}, {}
    for arm in ("real", "shuf", "blind"):
        hp, hd, info = train_member(S, ref, ref_enc, arm, a.post, a.ups, log)
        nm = arm.upper()
        heads[nm] = hd
        res["heads"][nm] = {"member": info, "pre_eval4": BB.evaluate(ref, hp, TE4, "z", S)}
    heads["BLINDR"] = heads["BLIND"]
    heads["BLIND"] = blind_exact(heads["BLINDR"])
    res["blind_action_weight_unchanged_from_init"] = bool(torch.equal(heads["BLINDR"]["a"]["weight"], init["a"]["weight"]))
    res["heads"]["BLINDR"] = {}
    fid = {}
    for nm in ("INIT", "REAL", "SHUF", "BLIND", "BLINDR"):
        ev4 = BB.evaluate(ref, heads[nm], TE4, "z", S)
        evw = eval_tew(ref, heads[nm], TEW, S)
        fid[nm] = evw["beats_persistence_by_depth"]
        res["heads"].setdefault(nm, {})
        res["heads"][nm]["eval4"] = ev4; res["heads"][nm]["tew"] = evw
        log("EVAL %-6s disc4=%.3f k=%d disc5(tew)=%.3f fair=%.3f k30=%d norm t1/t30/true=%.2f/%.2f/%.2f" % (
            nm, ev4["disc4_h1"], ev4["k"], evw["disc5_h1_tew"], evw["disc5_h1_tew_tiefair"], evw["k30"],
            evw["rollout_norm_t1_p50"], evw["rollout_norm_t30_p50"], evw["true_norm_p50"]))
    res["l2r_bar_real"] = bool(res["heads"]["REAL"]["eval4"]["disc4_h1"] >= 0.47 and res["heads"]["REAL"]["eval4"]["k"] == 10)
    res["twin_at_chance"] = bool(res["heads"]["SHUF"]["eval4"]["disc4_h1"] <= 0.32 and res["heads"]["SHUF"]["tew"]["disc5_h1_tew"] <= 0.27)

    # probe states, REAL head live, TAGGED with ticks_since_reset
    def collect(steps):
        pa = BB.fresh_agent(S, ref_enc)  # already fix-applied via the monkeypatch
        BP.set_head(pa, heads["REAL"])
        R.seed_all(S + 900)
        env = BB.make_env(S, 100)
        return pa, collect_probe_states_tagged(pa, env, steps, a.probe_every, S, action_dim=A_ENV,
                                                n_cont=a.ncont, cont_len=a.clen)
    pa, states = collect(a.probe_steps)
    res["probe_rerun_640"] = False
    if len(states) < 20:
        pa, states = collect(640)
        res["probe_rerun_640"] = True
    val = CA.probe_state_validation(states)
    ticks = [int(s["ticks_since_reset"]) for s in states]
    n_all = len(states)
    idx_ge8 = [i for i, t in enumerate(ticks) if t >= a.reset_tick_bar]
    idx_lt8 = [i for i, t in enumerate(ticks) if t < a.reset_tick_bar]
    res["probe"] = {"n_states": n_all, "validation": val,
                    "n_informative_q": int(sum(np.ptp(s["q"]) > 1e-9 for s in states)),
                    "ticks_since_reset": ticks,
                    "n_ge8": len(idx_ge8), "n_lt8": len(idx_lt8),
                    "frac_lt8": float(len(idx_lt8) / n_all) if n_all else None,
                    "exec_class_counts": dict(Counter(str(s["executed"]) for s in states))}
    log("PROBE n=%d validation=%s maxdiff=%s n_ge8=%d n_lt8=%d frac_lt8=%.3f ticks=%s" % (
        n_all, val.get("verdict"), val.get("max_abs_diff"), len(idx_ge8), len(idx_lt8),
        res["probe"]["frac_lt8"] or -1, ticks))

    score_fn = CA.e3_score_fn(pa)
    rows = {}
    for nm in ("INIT", "REAL", "SHUF", "BLIND", "BLINDR"):
        BP.set_head(pa, heads[nm])
        rows[nm] = score_head(pa, states, fid[nm], score_fn)
    res["decomp_canary_full_eq_Lmax_max"] = float(max(r["full_eq_Lmax_native"] for nm in rows for r in rows[nm]))
    res["batch_canary_rel_max"] = float(max(r["batch_canary_rel"] for nm in rows for r in rows[nm] if r["batch_canary_rel"] is not None))

    # gate (a) per aggregation, per partition: all / ge8 / lt8 (REAL and SHUF only --
    # gate (c), which needs BLIND/BLINDR, is out of scope for this probe).
    partitions = {"all": list(range(n_all)), "ge8": idx_ge8, "lt8": idx_lt8}
    res["metrics_by_partition"] = {}
    for pname, idxs in partitions.items():
        if not idxs:
            res["metrics_by_partition"][pname] = None
            continue
        res["metrics_by_partition"][pname] = {
            nm: metrics_subset(rows[nm], states, idxs) for nm in ("REAL", "SHUF")
        }
    res["habit_contrast_REAL"] = habit_contrast(rows["REAL"])
    res["fidw_weight_depths"] = {nm: [int(d) for d, b in fid[nm].items() if b and int(d) >= 2] for nm in fid}

    for pname in ("all", "ge8", "lt8"):
        mp = res["metrics_by_partition"][pname]
        if mp is None:
            log("PARTITION %s: empty, skipped" % pname)
            continue
        for ag in ("D1", "DISC_0.5", "DISC_0.8", "FULL"):
            mr, ms = mp["REAL"][ag], mp["SHUF"][ag]
            diff = None
            if mr["rho_scaf"] is not None and ms["rho_scaf"] is not None:
                diff = mr["rho_scaf"] - ms["rho_scaf"]
            log("PART %-4s AGG %-8s rho REAL=%s SHUF=%s diff=%s n=%d" % (
                pname, ag, mr["rho_scaf"], ms["rho_scaf"], diff, len(partitions[pname])))
    res["t_total_s"] = round(time.time() - t0, 1)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump(res, open(a.out, "w"), indent=1, default=str)
    log("wrote %s decomp=%.3g batch_rel=%.3g" % (a.out, res["decomp_canary_full_eq_Lmax_max"], res["batch_canary_rel_max"]))


if __name__ == "__main__":
    main()
