"""Gate (c) with z_world EMA reset-init probe (bt0926-gatec3, orchestrate-20260924-
breakthrough-c2, chip_ref chip-20260926-gate-c-with-ema-reset-init).

Diagnostic: does the gate-(c) per-step growth-leg failure on the W3 head
(gate_c_pool_controls_20260925.md, fc8340fb87: FAIL 5/5 seeds x 4 pools) still
occur when the z_world EMA reset-init fix (zworld_ema_reset_init_build_20260926.md,
3969d212ba, ree-v3 main 298cb8ffd3, LatentStackConfig.use_zworld_ema_reset_init)
is turned ON for the WHOLE pipeline (training + readout), not just spot-checked
at readout time? w3_step1_spike_attribution_20260925.md (d5f3bdc2fd) found the
step-1 growth spike concentrated at the smallest-||z0|| held-out states, and the
EMA-reset-init build record's own sec 3 flags this as the cheapest D2-adjacent
follow-on ("Not re-run with the knob ON -- that is the cheap next check").

Method: BYTE-IDENTICAL to gate_c_pool_controls_probe.py (aspc2) -- same training
recipe (E2WorldMember babble+on-policy, CodecMember), same held-out-state
protocol (BB.gen_policy, k0=300, pol_uniform(seed*11+17), t_pick draws from
default_rng(seed*97+5)), same 4 pools, same growth_stats/pool_and_gate/bound --
run TWICE per seed as one process: once with use_zworld_ema_reset_init=False
(canary: must reproduce aspc2's stored gatec2_s<seed>.json within noise) and
once with it True, set on BOTH the training agent's config (before babbling
starts) and ref's config (before held-out state generation), so the fix is live
for the whole pipeline, not spliced in only at readout.

Per held-out state this script ALSO records t_pick (the tick since that
episode's own reset -- BB.gen_policy's segments start their obs list right
after env.reset(), so the loop index ti IS ticks-since-reset; ti==t_pick is the
picked tick). Reports: fraction of held-out states with t_pick < 8 (within the
zero-init build record's own measured ~8-tick transient window), and -- OFF arm
only -- the SAME 4-pool gate-(c) growth stat restricted to states with
t_pick >= 8 (a second, orthogonal route to the same "is this the reset
artefact" question: if excluding early-tick states removes the failure even
with the knob OFF, that also implicates the reset transient without needing the
fix at all).

REPORT ONLY: no verdict is decided in-script; the verdict (ARTEFACT-EXPLAINED /
RESIDUAL) is written by the calling session into the record after reading this
script's JSON output for all 5 seeds.

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
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--n-states", type=int, default=20)
p.add_argument("--quick", action="store_true",
                help="shrink all update counts for a fast correctness smoke test")
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
from ree_core.utils.waking_trainer_codec import CodecMember  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

S = a.seed
t0 = time.time()

PRE_UPDATES = 30 if a.quick else 3000
CODEC_UPDATES = 20 if a.quick else 1000
N_BABBLE_EP = 2 if a.quick else 12
POST_STEPS = 200 if a.quick else 1200

assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__


def log(m):
    print("[gatec3 s%d t=%4.0fs] %s" % (S, time.time() - t0, m), flush=True)


def growth_stats(norms_1d):
    """norms_1d: 1D array length H+1 (t=0..H). Returns per-candidate stat dict."""
    v = np.asarray(norms_1d, dtype=float)
    n0 = float(v[0])
    ratio = float(v[-1] / n0) if n0 > 0 else None
    g = v[1:] / np.clip(v[:-1], 1e-12, None)
    Hn = len(g)
    out = {"ratio": ratio, "max_growth_all": float(g.max()) if Hn else None}
    if Hn >= 30:
        late = g[20:30]
    else:
        late = g[max(0, Hn - 10):Hn]
    out["late_window_mean_growth"] = float(late.mean()) if len(late) else None
    for D in (1, 3, 5):
        d = min(D, Hn)
        out["first%d_max_growth" % D] = float(g[:d].max()) if d > 0 else None
    return out


def pool_and_gate(per_cand):
    ratios = [c["ratio"] for c in per_cand if c["ratio"] is not None]
    out = {"n_candidates_pooled": len(per_cand)}
    out["pooled_ratio_median"] = float(np.median(ratios)) if ratios else None
    out["gate_ratio_ok"] = (out["pooled_ratio_median"] is not None
                             and 0.5 <= out["pooled_ratio_median"] <= 2.0)
    for key in ("max_growth_all", "first1_max_growth", "first3_max_growth", "first5_max_growth"):
        vals = [c[key] for c in per_cand if c.get(key) is not None]
        out["pooled_max_%s" % key] = float(np.max(vals)) if vals else None
    lw = [c["late_window_mean_growth"] for c in per_cand if c.get("late_window_mean_growth") is not None]
    out["pooled_median_late_window_mean_growth"] = float(np.median(lw)) if lw else None
    out["pooled_max_late_window_mean_growth"] = float(np.max(lw)) if lw else None
    out["gate_growth_ok_literal"] = (out["pooled_max_max_growth_all"] is not None
                                      and out["pooled_max_max_growth_all"] <= 1.05)
    out["gate_c_pass_literal"] = bool(out["gate_ratio_ok"] and out["gate_growth_ok_literal"])
    return out


def run_arm(knob: bool):
    """Full aspc2 pipeline (train world head + codec, 4 pools) with
    use_zworld_ema_reset_init set to `knob` on BOTH the training agent and ref,
    from before any sense()/encode() call. Returns (results_dict, states_meta)."""
    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    ref.latent_stack.config.use_zworld_ema_reset_init = bool(knob)
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    orig_codec = {
        "enc": copy.deepcopy(ref.e2.action_object_head.state_dict()),
        "dec": copy.deepcopy(ref.hippocampal.action_object_decoder.state_dict()),
    }

    # ---------------------------------------------- train world head + codec ----
    agent = BB.fresh_agent(S, ref_enc)
    agent.latent_stack.config.use_zworld_ema_reset_init = bool(knob)
    cfg = agent.config
    cfg.waking_trainer_guard_min_steps = 8
    member = WT.E2WorldMember(
        agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
        replay_frac=0.25, reencode_window=0, replay_latent="reencode",
        objective="mse", grad_clip=1.0, updates_per_step=1,
    )
    codec = CodecMember(agent, lr=1e-3, batch_size=16, buffer_max=2000, code_l2=1e-3)
    codec.updates_per_step = 0  # manual-only: no auto-update inside on_waking_step
    tr = WT.WakingTrainer(agent, cfg, members=[member, codec])
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
                lat = agent.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                                   obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
                codec.add_states([lat.z_world])
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
    for _u in range(CODEC_UPDATES):
        tr._update("codec", codec)
    log("knob=%s pre-phase done: retained %d classes %s, codec buf %d, codec updates %d"
        % (knob, retained_n, counts, len(codec._buf), CODEC_UPDATES))

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
    codec_post = {
        "enc": copy.deepcopy(agent.e2.action_object_head.state_dict()),
        "dec": copy.deepcopy(agent.hippocampal.action_object_decoder.state_dict()),
    }
    log("knob=%s post-phase done (%d steps, 8 upd/step world; codec frozen after pre-phase)"
        % (knob, POST_STEPS))

    # ------------------------------------------------------------- load head ----
    BP.set_head(ref, head_post)
    Hh = int(ref.hippocampal.config.horizon)
    K = int(ref.hippocampal.config.num_candidates)
    WD = int(ref.hippocampal.config.world_dim)
    A = int(ref.hippocampal.config.action_dim)
    I = int(ref.hippocampal.config.num_cem_iterations)
    log("knob=%s ref.hippocampal deployed dims: H=%d K=%d WD=%d A=%d I=%d" % (knob, Hh, K, WD, A, I))

    # --------------------------------------------------------- held-out states ----
    ref.eval()
    te_segs, _ = BB.gen_policy(S, a.n_states, 300, BB.pol_uniform(S * 11 + 17))
    g = np.random.default_rng(S * 97 + 5)
    states = []
    t_picks = []
    for seg in te_segs:
        if len(seg["a"]) < 1:
            continue
        ref.reset()
        t_pick = int(g.integers(0, len(seg["obs"])))
        with torch.no_grad():
            for ti, o in enumerate(seg["obs"]):
                lat = ref.sense(o["body_state"], o["world_state"], obs_harm=o.get("harm_obs"),
                                 obs_harm_a=o.get("harm_obs_a"), obs_harm_history=o.get("harm_history"))
                if ti == t_pick:
                    states.append((lat.z_world.detach().clone(), lat.z_self.detach().clone()))
                    t_picks.append(ti)
                    break
    log("knob=%s collected %d held-out (z_world, z_self) states (k0=300, disjoint from training k-ranges)"
        % (knob, len(states)))
    n_within8 = sum(1 for t in t_picks if t < 8)
    frac_within8 = float(n_within8) / len(t_picks) if t_picks else None
    keep_idx = set(i for i, t in enumerate(t_picks) if t >= 8)

    results = {}
    per_cand_by_pool = {}

    # ---- Pool 2: native default (ASP off, codec knobs off, codec UNTRAINED) ------
    ref.hippocampal.config.use_action_space_proposals = False
    ref.hippocampal.config.use_codec_bounded_decode = False
    ref.hippocampal.config.use_codec_iter0_image_match = False
    ref.e2.action_object_head.load_state_dict(orig_codec["enc"])
    ref.hippocampal.action_object_decoder.load_state_dict(orig_codec["dec"])
    per_cand = []
    for si, (zw, zs) in enumerate(states):
        torch.manual_seed(S * 30000 + si * 13 + 1)
        with torch.no_grad():
            pool = ref.hippocampal.propose_trajectories(zw, z_self=zs)
        for tr_ in pool:
            seq = tr_.get_world_state_sequence()
            if seq is None:
                continue
            norms = seq.detach().norm(dim=-1).mean(dim=0).numpy()
            stat = growth_stats(norms)
            stat["state_idx"] = si
            per_cand.append(stat)
    per_cand_by_pool["native_default"] = per_cand
    results["native_default"] = pool_and_gate(per_cand)
    results["native_default"]["n_states"] = len(states)
    log("knob=%s native_default: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
        knob, results["native_default"]["pooled_ratio_median"] or -1.0,
        results["native_default"]["pooled_max_max_growth_all"] or -1.0,
        results["native_default"]["gate_c_pass_literal"], results["native_default"]["n_candidates_pooled"]))

    # ---- Pool 1: native codec, W1 parts ON, codec TRAINED -------------------------
    ref.hippocampal.config.use_action_space_proposals = False
    ref.hippocampal.config.use_codec_bounded_decode = True
    ref.hippocampal.config.use_codec_iter0_image_match = True
    ref.e2.action_object_head.load_state_dict(codec_post["enc"])
    ref.hippocampal.action_object_decoder.load_state_dict(codec_post["dec"])
    per_cand = []
    for si, (zw, zs) in enumerate(states):
        torch.manual_seed(S * 30000 + si * 13 + 2)
        with torch.no_grad():
            pool = ref.hippocampal.propose_trajectories(zw, z_self=zs)
        for tr_ in pool:
            seq = tr_.get_world_state_sequence()
            if seq is None:
                continue
            norms = seq.detach().norm(dim=-1).mean(dim=0).numpy()
            stat = growth_stats(norms)
            stat["state_idx"] = si
            per_cand.append(stat)
    per_cand_by_pool["native_codec_w1_on"] = per_cand
    results["native_codec_w1_on"] = pool_and_gate(per_cand)
    results["native_codec_w1_on"]["n_states"] = len(states)
    log("knob=%s native_codec_w1_on: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
        knob, results["native_codec_w1_on"]["pooled_ratio_median"] or -1.0,
        results["native_codec_w1_on"]["pooled_max_max_growth_all"] or -1.0,
        results["native_codec_w1_on"]["gate_c_pass_literal"], results["native_codec_w1_on"]["n_candidates_pooled"]))

    # reset knobs to OFF (hygiene; controls below bypass hippocampal entirely anyway)
    ref.hippocampal.config.use_codec_bounded_decode = False
    ref.hippocampal.config.use_codec_iter0_image_match = False

    # ---- Pool 3: control, K random one-hot sequences, uniform class PER STEP -----
    per_cand = []
    for si, (zw, zs) in enumerate(states):
        torch.manual_seed(S * 30000 + si * 13 + 3)
        idx = torch.randint(0, A, (K, Hh))
        act_seq = F.one_hot(idx, num_classes=A).float()
        zw_b = zw.repeat(K, 1)
        zs_b = zs.repeat(K, 1)
        with torch.no_grad():
            traj = ref.e2.rollout_with_world(zs_b, zw_b, act_seq, compute_action_objects=False)
        seq = traj.get_world_state_sequence()
        norms_all = seq.detach().norm(dim=-1).numpy()
        for k in range(K):
            stat = growth_stats(norms_all[k])
            stat["state_idx"] = si
            per_cand.append(stat)
    per_cand_by_pool["control_random_per_step"] = per_cand
    results["control_random_per_step"] = pool_and_gate(per_cand)
    results["control_random_per_step"]["n_states"] = len(states)
    log("knob=%s control_random_per_step: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
        knob, results["control_random_per_step"]["pooled_ratio_median"] or -1.0,
        results["control_random_per_step"]["pooled_max_max_growth_all"] or -1.0,
        results["control_random_per_step"]["gate_c_pass_literal"],
        results["control_random_per_step"]["n_candidates_pooled"]))

    # ---- Pool 4: control, K constant-action sequences, one per class, cycled ----
    per_cand = []
    classes = torch.tensor([i % A for i in range(K)])
    idx_const = classes.unsqueeze(1).expand(K, Hh)
    act_seq_const = F.one_hot(idx_const, num_classes=A).float()
    for si, (zw, zs) in enumerate(states):
        torch.manual_seed(S * 30000 + si * 13 + 4)  # no randomness used; kept for parity
        zw_b = zw.repeat(K, 1)
        zs_b = zs.repeat(K, 1)
        with torch.no_grad():
            traj = ref.e2.rollout_with_world(zs_b, zw_b, act_seq_const, compute_action_objects=False)
        seq = traj.get_world_state_sequence()
        norms_all = seq.detach().norm(dim=-1).numpy()
        for k in range(K):
            stat = growth_stats(norms_all[k])
            stat["state_idx"] = si
            per_cand.append(stat)
    per_cand_by_pool["control_constant_per_class"] = per_cand
    results["control_constant_per_class"] = pool_and_gate(per_cand)
    results["control_constant_per_class"]["n_states"] = len(states)
    log("knob=%s control_constant_per_class: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
        knob, results["control_constant_per_class"]["pooled_ratio_median"] or -1.0,
        results["control_constant_per_class"]["pooled_max_max_growth_all"] or -1.0,
        results["control_constant_per_class"]["gate_c_pass_literal"],
        results["control_constant_per_class"]["n_candidates_pooled"]))

    meta = {
        "horizon": Hh, "num_candidates": K, "world_dim": WD, "action_dim": A,
        "num_cem_iterations": I, "n_states": len(states), "retained_n": retained_n,
        "t_picks": t_picks, "n_within8ticks": n_within8, "frac_within8ticks": frac_within8,
    }

    # ---- second route: same 4 pools restricted to states with t_pick >= 8 -----
    restricted = {}
    if keep_idx and len(keep_idx) < len(states):
        for pool_name, per_cand in per_cand_by_pool.items():
            filt = [c for c in per_cand if c["state_idx"] in keep_idx]
            restricted[pool_name] = pool_and_gate(filt)
            restricted[pool_name]["n_states"] = len(keep_idx)
        log("knob=%s restricted (t_pick>=8, %d/%d states) native_default max_growth=%.4f pass=%s"
            % (knob, len(keep_idx), len(states),
               restricted["native_default"]["pooled_max_max_growth_all"] or -1.0,
               restricted["native_default"]["gate_c_pass_literal"]))
    else:
        log("knob=%s restricted t_pick>=8 subset empty or == full set (keep=%d of %d); skipped"
            % (knob, len(keep_idx), len(states)))

    return results, meta, restricted


out = {"seed": S, "n_states_arg": a.n_states, "quick": bool(a.quick),
       "pre_updates": PRE_UPDATES, "codec_updates": CODEC_UPDATES, "arms": {}}

for knob in (False, True):
    tA = time.time()
    results, meta, restricted = run_arm(knob)
    key = "on" if knob else "off"
    out["arms"][key] = {"results": results, "meta": meta,
                         "restricted_t_pick_ge8_off_only": restricted if not knob else {},
                         "arm_wall_s": time.time() - tA}

out["t_total_s"] = time.time() - t0
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE -> %s" % a.out)
