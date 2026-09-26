"""ASP gate (c) under the decided statistic, all 4 EMA reset-init knobs ON
(bt0926-decprobe, orchestrate-20260924-breakthrough-c2,
chip_ref chip-20260926-gate-reread-under-user-decisions).

Decided statistic (2026-09-26T09:33Z decision log entry (1), PROVISIONAL
orchestrator decision under standing delegation --
coupled_loop_repair_campaign_plan.md, 45d9c1d83f4 / 86d2b2d021b):
gate (c)'s growth leg PASSES iff, for every candidate, the model's predicted
per-step growth (max over the H=30 rollout -- the SAME statistic every prior
record in this line calls "pooled_max_growth" / "max_growth_all") is
<= 1.05x the environment's OWN TRUE per-step growth at the SAME held-out
state, for the SAME first-action class the candidate actually took --
PLUS the late-window (steps 21-30) mean-growth bound gate (e) already
defines (<= 1.2, per w3_e2_world_member_build_20260925.md).

STOP-RULE SIMPLIFICATION (COMMON.md rule 10; re-measured in THIS probe's own
data below, sec "predicted-side step-1 dominance check", not assumed from
citation alone): every prior record in this line (asp_gate_c_readout_
20260925.md, gate_c_pool_controls_20260925.md, w3_step1_spike_attribution_
20260925.md, gate_c_with_ema_reset_init_20260926.md) found the model's OWN
max growth over the full H=30 rollout equals its step-1 growth to 3-4
significant figures, in every pool/seed/knob-state measured so far.
w3_step1_spike_attribution_20260925.md (d5f3bdc2fd) additionally showed the
environment's TRUE dynamics reach their OWN max growth at step 1 too
(corr(real,true) 0.89-0.93 pooled over all state x class pairs, worst-cell
agreement within 0.01-0.05) -- that record's own I1 instrument
(encode_next_side_effect_free) was independently validated there to
max_abs_diff 0.0 against the next live agent.sense() tick. This probe
therefore uses the env's TRUE STEP-1 growth (per candidate's actual FIRST
action class) as "the env's TRUE per-step growth at the same state", and
VERIFIES (not assumes) in its own data that the model's predicted
max_growth_all == first1_max_growth, printing any counterexample rather than
silently relying on the cited pattern holding again.

Env-true growth instrument: u3_step1_attribution_probe.py's method
(gen_policy_env: deep-copy env snapshot at each held-out segment's start,
replay that segment's OWN recorded actions to reconstruct the live env state
at t_pick, then step + encode_next_side_effect_free per class) -- reused
near-verbatim, extended here to ALL 5 action classes per state (needed
because ASP-E/ASP-0 candidates span all 5 first-action classes by
construction, unlike u3's own per-class table which was already computed
this way -- reused, not re-derived from scratch).

Knobs: all four EMA reset-init flags ON (use_zworld_ema_reset_init,
use_zself_ema_reset_init, use_shared_ema_reset_init, use_zharm_ema_reset_init)
per decision (4), set on BOTH ref's config and the training agent's config
before any sense()/encode() call (gate_c_with_ema_reset_init_20260926.md's
own pattern, extended to all four). The canary arm (all four knobs OFF) must
reproduce asp_gate_c_readout_20260925.md's (cbf0f87173) literal per-seed
pooled_max_growth numbers (~1.71-1.74).

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
from experiments._lib.coupled_acceptance import encode_next_side_effect_free, onehot  # noqa: E402

S = a.seed
A = 5
t0 = time.time()

PRE_UPDATES = 30 if a.quick else 3000
N_BABBLE_EP = 2 if a.quick else 12
POST_STEPS = 200 if a.quick else 1200
N_STATES = a.n_states

KNOBS = (
    "use_zworld_ema_reset_init",
    "use_zself_ema_reset_init",
    "use_shared_ema_reset_init",
    "use_zharm_ema_reset_init",
)

assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__


def log(m):
    print("[decprobe s%d t=%4.0fs] %s" % (S, time.time() - t0, m), flush=True)


def set_knobs(cfg, on: bool):
    for k in KNOBS:
        setattr(cfg, k, bool(on))


def growth_stats(norms_1d):
    """norms_1d: 1D array length H+1 (t=0..H). Per-candidate predicted-side stat dict."""
    v = np.asarray(norms_1d, dtype=float)
    n0 = float(v[0])
    ratio = float(v[-1] / n0) if n0 > 0 else None
    g = v[1:] / np.clip(v[:-1], 1e-12, None)
    Hn = len(g)
    out = {"ratio": ratio, "max_growth_all": float(g.max()) if Hn else None,
           "first1_max_growth": float(g[0]) if Hn >= 1 else None}
    if Hn >= 30:
        late = g[20:30]
    else:
        late = g[max(0, Hn - 10):Hn]
    out["late_window_mean_growth"] = float(late.mean()) if len(late) else None
    return out


def gen_policy_env(seed, n_eps, k0, policy):
    """BB.gen_policy, bit-identical segs, ALSO returns a deep-copied env snapshot per segment
    (right after that segment's own env.reset(), before any of its actions). Verbatim from
    u3_step1_attribution_probe.py."""
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


def run_arm(knob: bool):
    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    set_knobs(ref.latent_stack.config, knob)
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())

    # ---------------------------------------------------------------- train ----
    agent = BB.fresh_agent(S, ref_enc)
    set_knobs(agent.latent_stack.config, knob)
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
    retained_n = len(member._retained)
    for _u in range(PRE_UPDATES):
        tr._update("e2_world", member)
    log("knob=%s pre-phase done: retained %d classes %s" % (knob, retained_n, counts))

    tr.set_e2_world_source("on_policy")
    tr.every_k = 1
    member.updates_per_step = 8
    agent.reset()
    R.seed_all(S + 500)
    for ep in range(POST_STEPS // BB.EP_STEPS):
        env = BB.make_env(S, 50 + ep)
        hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
        _f, od = env.reset(); agent.reset(); hh.reset()
        for _s in range(BB.EP_STEPS):
            r = hh.step(od)
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); hh.reset()
    head_post = BP.get_head(agent)
    log("knob=%s post-phase done (%d steps, 8 upd/step)" % (knob, POST_STEPS))

    # ---------------------------------------------------------- load head ----
    BP.set_head(ref, head_post)
    Hh = int(ref.hippocampal.config.horizon)
    K = int(ref.hippocampal.config.num_candidates)
    WD = int(ref.hippocampal.config.world_dim)
    log("knob=%s ref.hippocampal deployed dims: H=%d K=%d WD=%d" % (knob, Hh, K, WD))

    # -------------------------------------------- held-out states + env truth ----
    ref.eval()
    te_segs, env_snaps = gen_policy_env(S, N_STATES, 300, BB.pol_uniform(S * 11 + 17))
    g = np.random.default_rng(S * 97 + 5)

    states = []  # each: zw, zs, true_g1[5], val_maxabs
    for seg, env0 in zip(te_segs, env_snaps):
        if len(seg["a"]) < 1:
            continue
        ref.reset()
        t_pick = int(g.integers(0, len(seg["obs"])))
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
        zw = lat_at_pick.z_world.detach().clone()
        zs = lat_at_pick.z_self.detach().clone()
        z0_norm = max(float(zw.norm()), 1e-9)

        # reconstruct the exact live env state at t_pick by replaying this
        # segment's own actions onto its own start snapshot
        env_at_pick = copy.deepcopy(env0)
        for ai in seg["a"][:t_pick]:
            env_at_pick.step(ai)

        true_g1 = [None] * A
        with torch.no_grad():
            for c in range(A):
                ec = copy.deepcopy(env_at_pick)
                _f, _h, _d, _i, obs_next = ec.step(c)
                z_true = encode_next_side_effect_free(ref, obs_next, lat_at_pick, onehot(c, A))
                true_g1[c] = float(z_true.reshape(-1).norm()) / z0_norm

        val_maxabs = None
        if lat_next_live is not None and t_pick < len(seg["a"]):
            executed_c = int(seg["a"][t_pick])
            ec = copy.deepcopy(env_at_pick)
            _f, _h, _d, _i, obs_next = ec.step(executed_c)
            with torch.no_grad():
                z_true_exec = encode_next_side_effect_free(ref, obs_next, lat_at_pick,
                                                             onehot(executed_c, A))
            val_maxabs = float((z_true_exec.reshape(-1)
                                 - lat_next_live.z_world.detach().reshape(-1)).abs().max())

        states.append({"zw": zw, "zs": zs, "true_g1": true_g1, "val_maxabs": val_maxabs})

    n_validated = sum(1 for st in states if st["val_maxabs"] is not None)
    val_max = max((st["val_maxabs"] for st in states if st["val_maxabs"] is not None), default=None)
    log("knob=%s collected %d held-out states; instrument validated %d, max|diff|=%s"
        % (knob, len(states), n_validated, val_max))

    # ------------------------------------------------------------- gate (c) ----
    MODES = [("ASP-E", "stratified"), ("ASP-0", "stratified_uniform")]
    results = {}
    for mi, (name, mode) in enumerate(MODES):
        ref.hippocampal.config.use_action_space_proposals = True
        ref.hippocampal.config.action_space_first_action_mode = mode
        per_cand = []
        for si, st in enumerate(states):
            torch.manual_seed(S * 10000 + si * 13 + mi * 3)
            with torch.no_grad():
                pool = ref.hippocampal.propose_trajectories(st["zw"], z_self=st["zs"])
            for tr_ in pool:
                seq = tr_.get_world_state_sequence()
                if seq is None:
                    continue
                seq = seq.detach()
                norms = seq.norm(dim=-1).mean(dim=0).numpy()
                stat = growth_stats(norms)
                first_c = int(tr_.actions[0, 0].argmax())
                stat["state_idx"] = si
                stat["first_class"] = first_c
                stat["true_g1_first_class"] = st["true_g1"][first_c]
                per_cand.append(stat)
        ref.hippocampal.config.use_action_space_proposals = False

        ratios = [c["ratio"] for c in per_cand if c["ratio"] is not None]
        pooled_ratio_median = float(np.median(ratios)) if ratios else None
        gate_ratio_ok = pooled_ratio_median is not None and 0.5 <= pooled_ratio_median <= 2.0

        max_growth_vals = [c["max_growth_all"] for c in per_cand if c.get("max_growth_all") is not None]
        pooled_max_growth = float(np.max(max_growth_vals)) if max_growth_vals else None
        gate_growth_ok_literal = pooled_max_growth is not None and pooled_max_growth <= 1.05
        gate_c_pass_literal = bool(gate_ratio_ok and gate_growth_ok_literal)

        # predicted-side step-1 dominance check (re-measured, not assumed)
        dom_diffs = [abs(c["max_growth_all"] - c["first1_max_growth"]) for c in per_cand
                     if c.get("max_growth_all") is not None and c.get("first1_max_growth") is not None]
        n_dom_violation = sum(1 for d in dom_diffs if d > 1e-6)
        max_dom_diff = float(np.max(dom_diffs)) if dom_diffs else None

        # decided statistic: predicted max_growth_all <= 1.05 * true_g1(state, first_class)
        excess_ratios = []
        decided_pass_flags = []
        for c in per_cand:
            tg1 = c.get("true_g1_first_class")
            mg = c.get("max_growth_all")
            if tg1 is None or mg is None or tg1 <= 0:
                continue
            bound = 1.05 * tg1
            er = mg / bound if bound > 0 else float("inf")
            excess_ratios.append(er)
            decided_pass_flags.append(bool(mg <= bound))
        pooled_max_excess_ratio = float(np.max(excess_ratios)) if excess_ratios else None
        gate_growth_ok_decided = pooled_max_excess_ratio is not None and pooled_max_excess_ratio <= 1.0
        frac_candidates_decided_pass = (float(np.mean(decided_pass_flags))
                                         if decided_pass_flags else None)

        late_vals = [c["late_window_mean_growth"] for c in per_cand
                     if c.get("late_window_mean_growth") is not None]
        pooled_max_late = float(np.max(late_vals)) if late_vals else None
        gate_late_ok = pooled_max_late is not None and pooled_max_late <= 1.2

        gate_c_pass_decided = bool(gate_ratio_ok and gate_growth_ok_decided and gate_late_ok)

        # per-first-class breakdown (diagnostic)
        per_class_excess = {}
        for cl in range(A):
            vals = []
            for c in per_cand:
                if c.get("first_class") != cl:
                    continue
                tg1 = c.get("true_g1_first_class")
                mg = c.get("max_growth_all")
                if tg1 is None or mg is None or tg1 <= 0:
                    continue
                vals.append(mg / (1.05 * tg1))
            if vals:
                per_class_excess[str(cl)] = {"n": len(vals), "max_excess_ratio": float(np.max(vals)),
                                              "mean_excess_ratio": float(np.mean(vals))}

        results[name] = {
            "mode_config": mode, "n_states": len(states), "n_candidates_pooled": len(per_cand),
            "pooled_ratio_median": pooled_ratio_median, "gate_ratio_ok": gate_ratio_ok,
            "pooled_max_growth_literal": pooled_max_growth,
            "gate_growth_ok_literal": gate_growth_ok_literal,
            "gate_c_pass_literal": gate_c_pass_literal,
            "predicted_step1_dominance_n_violation": n_dom_violation,
            "predicted_step1_dominance_max_diff": max_dom_diff,
            "pooled_max_excess_ratio_decided": pooled_max_excess_ratio,
            "gate_growth_ok_decided": gate_growth_ok_decided,
            "frac_candidates_decided_pass": frac_candidates_decided_pass,
            "pooled_max_late_window_mean_growth": pooled_max_late,
            "gate_late_ok": gate_late_ok,
            "gate_c_pass_decided": gate_c_pass_decided,
            "per_class_excess_ratio": per_class_excess,
        }
        log("knob=%s %s: literal max_growth=%.4f pass_literal=%s | decided max_excess=%s "
            "frac_cand_pass=%s late_max=%s pass_decided=%s | dominance_violations=%d/%d" % (
                knob, name, pooled_max_growth or -1.0, gate_c_pass_literal,
                ("%.4f" % pooled_max_excess_ratio) if pooled_max_excess_ratio is not None else "None",
                ("%.4f" % frac_candidates_decided_pass) if frac_candidates_decided_pass is not None else "None",
                ("%.4f" % pooled_max_late) if pooled_max_late is not None else "None",
                gate_c_pass_decided, n_dom_violation, len(per_cand)))

    true_g1_all = [st["true_g1"][c] for st in states for c in range(A)]
    meta = {
        "horizon": Hh, "num_candidates": K, "world_dim": WD, "n_states": len(states),
        "retained_n": retained_n, "n_validated": n_validated, "val_max_abs_diff": val_max,
        "true_g1_summary": {"min": float(np.min(true_g1_all)), "median": float(np.median(true_g1_all)),
                             "max": float(np.max(true_g1_all))},
    }
    return results, meta


out = {"seed": S, "n_states_arg": N_STATES, "quick": bool(a.quick),
       "pre_updates": PRE_UPDATES, "post_steps": POST_STEPS, "knobs": list(KNOBS), "arms": {}}

for knob in (False, True):
    tA = time.time()
    results, meta = run_arm(knob)
    key = "on" if knob else "off"
    out["arms"][key] = {"results": results, "meta": meta, "arm_wall_s": time.time() - tA}

out["t_total_s"] = time.time() - t0
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE -> %s" % a.out)
