"""ASP gate (c) readout on the REAL W3 head (bt0925-aspc, orchestrate-20260924-breakthrough-c2).

Design of record: action_space_proposals_design_20260925.md (412882b845) sec 4
row (c): "bounded rollouts: the median candidate world_states norm at t = H
stays within [0.5, 2] x the t = 0 norm, with no per-step growth > 1.05 ...
Read with the W3 head."

Build status this closes: action_space_proposals_build_20260925.md sec 4 row
(c) "NOT ASSESSABLE before W3 ... Readout built and verified [on an untrained
E2]"; w3_e2_world_member_build_20260925.md sec 5 "ASP gate (c) is now
runnable ... Not run here."

Training recipe: probes/w3/w3_l2r_member_probe.py verbatim, real arm only (the
SHUF twin tests a different property -- action-map durability -- not needed
for a rollout-boundedness readout). Trains E2WorldMember through babbling
(W2a StructuredBabbler, 12 Phase-0 episodes, 3000 updates) then 1200
closed-loop on-policy steps (8 member updates/step, 25% retained replay,
re-encoded), exactly as the W3 record.

Readout: the trained e2.world_transition / e2.world_action_encoder state
dicts are loaded into `ref`, a full production REEAgent built via
rollout_fidelity_probe.build_B (REEConfig.from_dims, CausalGridWorldV2 8x8,
world_dim 32) -- so ref.hippocampal is the REAL deployed HippocampalModule,
not an ad-hoc-scale stand-in (contrast the W1-alt build's asp_smoke.py /
codec_growth.py, which used horizon=10, num_candidates=32 ad hoc, deliberately
not the deployed cfg, and were pre-W3 so untrained anyway).

PREMISE RE-MEASURED: tests/contracts/test_action_space_proposals.py hardcodes
H = 10 and labels it "deployed horizon". Empirically, REEConfig.from_dims's
computed hippocampal.horizon is 30 (config.hippocampal.horizon =
config.e2.rollout_horizon, whose from_dims default is 30) -- confirmed by
direct construction, not by re-reading the comment. This script reads gate
(c) at ref.hippocampal.config.horizon, i.e. the TRUE production H, and prints
it, rather than trusting the contract file's H=10 label. See the readout
record for how this affects (or does not affect) the verdict.

Held-out states: BB.gen_policy at a k0 range (300+) disjoint from every
k-range the training touched (babble k=0..11, post-phase k=50..55), stepped
through ref.sense() at each tick -- the same "native read path" babble_probe.
encode_segs() uses for the TE test set, extended here to also keep z_self
(encode_segs keeps only z_world). One (z_world, z_self) sample per episode,
at a per-episode-random tick.

Gate (c) verdict per mode: pool every candidate's rollout ratio (norm at
t=H / norm at t=0) and per-step growth (norm at step i / norm at step i-1)
across all N_STATES x K candidates for that seed; PASS iff the pooled median
ratio in [0.5, 2] AND the pooled max growth <= 1.05. Cross-checked against
the module's own action_space_rollout_norm_ratio_median /
action_space_rollout_max_step_growth_max diagnostics (independent
recomputation, same pattern as
test_gate_c_rollout_norm_readout_matches_independent_recomputation).

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

S = a.seed
t0 = time.time()


def log(m):
    print("[aspc s%d t=%4.0fs] %s" % (S, time.time() - t0, m), flush=True)


assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__

R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())

# ---------------------------------------------------------------- train ----
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
    for k in range(12):
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
for _u in range(3000):
    tr._update("e2_world", member)
log("pre-phase done: retained %d classes %s" % (retained_n, counts))

tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = 8
agent.reset()
R.seed_all(S + 500)
for ep in range(1200 // BB.EP_STEPS):
    env = BB.make_env(S, 50 + ep)
    hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
    _f, od = env.reset(); agent.reset(); hh.reset()
    for _s in range(BB.EP_STEPS):
        r = hh.step(od)
        od = r.next_obs_dict
        if r.done:
            _f, od = env.reset(); agent.reset(); hh.reset()
head_post = BP.get_head(agent)
log("post-phase done (1200 steps, 8 upd/step)")

# ---------------------------------------------------------- load head ----
BP.set_head(ref, head_post)
Hh = int(ref.hippocampal.config.horizon)
K = int(ref.hippocampal.config.num_candidates)
WD = int(ref.hippocampal.config.world_dim)
A = int(ref.hippocampal.config.action_dim)
I = int(ref.hippocampal.config.num_cem_iterations)
log("ref.hippocampal deployed dims: H=%d K=%d WD=%d A=%d I=%d "
    "(contract test file's own H=10 label does NOT match this; see docstring)" % (Hh, K, WD, A, I))

# ------------------------------------------------------- held-out states ----
ref.eval()
te_segs, _ = BB.gen_policy(S, a.n_states, 300, BB.pol_uniform(S * 11 + 17))
g = np.random.default_rng(S * 97 + 5)
states = []
for seg in te_segs:
    if len(seg["a"]) < 1:
        continue
    ref.reset()
    t_pick = int(g.integers(0, len(seg["obs"])))
    lat = None
    with torch.no_grad():
        for ti, o in enumerate(seg["obs"]):
            lat = ref.sense(o["body_state"], o["world_state"], obs_harm=o.get("harm_obs"),
                             obs_harm_a=o.get("harm_obs_a"), obs_harm_history=o.get("harm_history"))
            if ti == t_pick:
                states.append((lat.z_world.detach().clone(), lat.z_self.detach().clone()))
                break
log("collected %d held-out (z_world, z_self) states (k0=300, disjoint from training k-ranges)"
    % len(states))

# ------------------------------------------------------------- gate (c) ----
MODES = [("ASP-E", "stratified"), ("ASP-0", "stratified_uniform"), ("ASP-R", "refit")]
results = {}
for mi, (name, mode) in enumerate(MODES):
    ref.hippocampal.config.use_action_space_proposals = True
    ref.hippocampal.config.action_space_first_action_mode = mode
    ratios, growths, per_state = [], [], []
    ratios_asp_only, growths_asp_only = [], []
    for si, (zw, zs) in enumerate(states):
        torch.manual_seed(S * 10000 + si * 13 + mi * 3)
        with torch.no_grad():
            pool = ref.hippocampal.propose_trajectories(zw, z_self=zs)
        diag = dict(ref.hippocampal._last_propose_diagnostics)
        st_ratios, st_growth = [], []
        st_ratios_asp, st_growth_asp = [], []  # source == "action_space_cem" only
        non_asp_sources = set()
        worst_growth, worst_source = -1.0, None
        for tr_ in pool:
            seq = tr_.get_world_state_sequence()
            if seq is None:
                continue
            seq = seq.detach()
            norms = seq.norm(dim=-1).mean(dim=0)
            n0 = float(norms[0])
            if n0 <= 0.0:
                continue
            src = (tr_.metadata or {}).get("source") if hasattr(tr_, "metadata") else None
            ratio = float(norms[-1]) / n0
            steps = norms[1:] / norms[:-1].clamp_min(1e-12)
            growth = float(steps.max())
            st_ratios.append(ratio)
            st_growth.append(growth)
            if src == "action_space_cem":
                st_ratios_asp.append(ratio)
                st_growth_asp.append(growth)
            else:
                non_asp_sources.add(str(src))
            if growth > worst_growth:
                worst_growth, worst_source = growth, src
        ratios.extend(st_ratios)
        growths.extend(st_growth)
        ratios_asp_only.extend(st_ratios_asp)
        growths_asp_only.extend(st_growth_asp)
        rc_med = float(np.median(st_ratios)) if st_ratios else None
        gc_max = float(np.max(st_growth)) if st_growth else None
        diag_med = diag.get("action_space_rollout_norm_ratio_median")
        diag_gmax = diag.get("action_space_rollout_max_step_growth_max")
        mismatch = False
        if rc_med is not None and diag_med is not None:
            mismatch = mismatch or abs(rc_med - diag_med) > 1e-6
        if gc_max is not None and diag_gmax is not None:
            mismatch = mismatch or abs(gc_max - diag_gmax) > 1e-6
        per_state.append({
            "state": si, "n_cand": len(pool), "ratio_median": rc_med, "max_growth": gc_max,
            "diag_ratio_median": diag_med, "diag_max_growth": diag_gmax,
            "readout_mismatch": bool(mismatch),
            "non_asp_sources_present": sorted(non_asp_sources),
            "worst_growth_source": worst_source,
            "support_preserving_active": diag.get("support_preserving_active"),
            "support_preserving_injected_candidates": diag.get("support_preserving_injected_candidates"),
        })
    ref.hippocampal.config.use_action_space_proposals = False
    pooled_ratio_median = float(np.median(ratios)) if ratios else None
    pooled_max_growth = float(np.max(growths)) if growths else None
    gate_ratio_ok = pooled_ratio_median is not None and 0.5 <= pooled_ratio_median <= 2.0
    gate_growth_ok = pooled_max_growth is not None and pooled_max_growth <= 1.05
    # ASP-only (source == "action_space_cem") companion: excludes any candidate
    # injected by machinery outside the ASP mechanism itself (support-preserving
    # CEM injection, scaffold, chunk splice, ghost probes) -- all of which are
    # config-gated separately from ASP and can in principle fire on the FULL
    # production agent even though the isolated W1-alt contract harness never
    # exercises them. See per_state[]["non_asp_sources_present"].
    pooled_ratio_median_asp_only = float(np.median(ratios_asp_only)) if ratios_asp_only else None
    pooled_max_growth_asp_only = float(np.max(growths_asp_only)) if growths_asp_only else None
    gate_ratio_ok_asp_only = (
        pooled_ratio_median_asp_only is not None and 0.5 <= pooled_ratio_median_asp_only <= 2.0
    )
    gate_growth_ok_asp_only = (
        pooled_max_growth_asp_only is not None and pooled_max_growth_asp_only <= 1.05
    )
    any_mismatch = any(x["readout_mismatch"] for x in per_state)
    any_non_asp_source = any(x["non_asp_sources_present"] for x in per_state)
    results[name] = {
        "mode_config": mode, "n_states": len(states), "n_candidates_pooled": len(ratios),
        "pooled_ratio_median": pooled_ratio_median, "pooled_max_growth": pooled_max_growth,
        "gate_ratio_in_bounds_0.5_2": gate_ratio_ok, "gate_no_step_growth_over_1.05": gate_growth_ok,
        "gate_c_pass": bool(gate_ratio_ok and gate_growth_ok),
        "n_candidates_pooled_asp_only": len(ratios_asp_only),
        "pooled_ratio_median_asp_only": pooled_ratio_median_asp_only,
        "pooled_max_growth_asp_only": pooled_max_growth_asp_only,
        "gate_c_pass_asp_only": bool(gate_ratio_ok_asp_only and gate_growth_ok_asp_only),
        "any_non_asp_source_in_final_pool": any_non_asp_source,
        "diagnostics_readout_mismatch_any": any_mismatch,
        "per_state": per_state,
    }
    log("%s (%s): ratio_median=%.4f max_growth=%.4f pass=%s | asp_only ratio=%.4f growth=%.4f pass=%s | "
        "non_asp_source=%s diag_mismatch=%s" % (
            name, mode, pooled_ratio_median or -1.0, pooled_max_growth or -1.0,
            results[name]["gate_c_pass"],
            pooled_ratio_median_asp_only or -1.0, pooled_max_growth_asp_only or -1.0,
            results[name]["gate_c_pass_asp_only"], any_non_asp_source, any_mismatch))

out = {
    "seed": S, "horizon": Hh, "num_candidates": K, "world_dim": WD, "action_dim": A,
    "num_cem_iterations": I, "n_states": a.n_states, "retained_n": retained_n,
    "results": results, "t_total_s": time.time() - t0,
}
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE -> %s" % a.out)
