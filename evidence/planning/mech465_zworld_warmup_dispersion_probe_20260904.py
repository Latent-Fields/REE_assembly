"""Scratch SPIKE (NOT an experiment, no manifest): does warming up z_world remove the
confound under MECH-465's three declined gate-rescale probes?

All three probes (2026-07-20 EMA spike, 2026-07-21 SD-063 stage-2, 2026-08-27 boundary
regime) measured running-variance dispersion on an UNTRAINED z_world -- a frozen random
projection -- because their shared release condition sd_zworld_warmup_optimizer_group was
read as pending when it had in fact been status: validated since 2026-07-22. This spike is
the 2026-08-27 harness verbatim (same config, same URG grid, same post-warmup tick>=90 window)
plus an ON arm that calls the validated run_zworld_p0 warmup before measuring.

A SPIKE LICENSES NOTHING. It does not build the gate rescale regardless of outcome; see
mech465_zworld_warmup_dispersion_spike_20260904.md for what it does and does not license.
"""
import sys, json
sys.path.insert(0, "/Users/dgolden/REE_Working/ree-v3")
import numpy as np, torch
from ree_core.utils.config import REEConfig
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from experiments._lib.zworld_p0_warmup import run_zworld_p0
from experiments._lib.capability_eval import RandomPolicy

URG = [0.04, 0.10, 0.16, 0.22, 0.28, 0.34]
BASE_W = 0.12

def build(seed, thr, warm=False, p0_episodes=60, p0_steps=40):
    env = CausalGridWorldV2(use_proxy_fields=True, seed=seed, hazard_harm=0.5)
    _o, od = env.reset()
    kw = dict(
        body_obs_dim=od["body_state"].shape[-1], world_obs_dim=od["world_state"].shape[-1],
        action_dim=env.action_dim, alpha_world=0.9,
        use_harm_stream=True, use_affective_harm_stream=True, urgency_weight=BASE_W,
        use_support_preserving_cem=True, support_preserving_min_first_action_classes=2,
        support_preserving_stratified_elites=True, support_preserving_ao_std_floor=0.2,
        use_per_stream_vs=True, use_per_region_vs=True, use_event_segmenter=True,
        use_invalidation_trigger=True, use_anchor_sets=True,
        e2_action_contrastive_enabled=True, e2_action_contrastive_weight=0.1,
        e2_rollout_output_norm_clamp_enabled=True, e2_rollout_output_norm_clamp_ratio=4.0,
        use_structured_curiosity=True, use_curiosity_novelty=True,
        curiosity_bias_scale=0.1, curiosity_novelty_weight=0.05,
        use_modulatory_selection_authority=True, modulatory_authority_gain=0.5,
        modulatory_authority_min_range_floor=1e-6,
        use_e3_score_diversity=False, use_e3_diversity_entropy_bonus=False,
        commitment_threshold=thr,          # DOES THIS LAND THROUGH from_dims?
    )
    cfg = REEConfig.from_dims(**kw)
    cfg.e3.use_finer_channel_gating = True
    agent = REEAgent(cfg); agent.eval()
    agent.e3.e3_score_decomp_enabled = True
    warm_diag = None
    if warm:
        wenv = CausalGridWorldV2(use_proxy_fields=True, seed=seed, hazard_harm=0.5)
        wenv.reset()
        # NON-VACUITY CONTROL: the whole point of this spike is that the encoder was NEVER
        # trained in the three prior probes. Measure the world-encoder weight delta directly
        # rather than trusting that the call ran -- an ON arm with delta 0 is vacuous.
        we = agent.latent_stack.split_encoder.world_encoder
        before = {n: p.detach().clone() for n, p in we.named_parameters()}
        warm_diag = run_zworld_p0(agent, wenv, seed=seed, episodes=p0_episodes,
                                  steps_per_episode=p0_steps, policy=RandomPolicy(seed),
                                  label="mech465_spike_20260904")
        deltas = {n: float((p.detach() - before[n]).norm().item())
                  for n, p in we.named_parameters()}
        warm_diag = dict(warm_diag)
        warm_diag["world_encoder_weight_delta_l2"] = deltas
        warm_diag["world_encoder_tensors_changed"] = sum(1 for v in deltas.values() if v > 0)
        warm_diag["world_encoder_n_tensors"] = len(deltas)
    landed = float(agent.e3.config.commitment_threshold)
    agent.e3.config.commitment_threshold = float(thr)   # post-construction idiom
    return agent, env, od, landed, warm_diag

def run(seed, thr, n_ticks, rng, warm=False, p0_episodes=60):
    agent, env, od, landed, warm_diag = build(seed, thr, warm=warm, p0_episodes=p0_episodes)
    rows = []; zp = None; ap = None; nfresh = 0; nlat = 0
    for tick in range(n_ticks):
        assigned = float(rng.choice(URG))
        with torch.no_grad():
            lat = agent.sense(od["body_state"].unsqueeze(0), od["world_state"].unsqueeze(0),
                              obs_harm=od.get("harm_obs"), obs_harm_a=od.get("harm_obs_a"),
                              obs_harm_history=od.get("harm_history"))
            zc = lat.z_world.detach()
            if zp is not None and ap is not None:
                agent.e3.update_running_variance(zc - agent.e2.world_forward(zp, ap).detach())
            sig = lat.z_harm_a
            if getattr(agent.config.latent, "use_harm_un", False) and lat.z_harm_un is not None:
                sig = lat.z_harm_un
            sn = float(sig.norm(dim=-1).mean().item()) if sig is not None else 0.0
            agent.e3.config.urgency_weight = (assigned / sn) if sn > 1e-9 else 0.0
            agent.e3.last_score_diagnostics = None
            td = agent.clock.advance()
            e1 = (agent._e1_tick(lat) if td["e1_tick"]
                  else torch.zeros(1, agent.config.latent.world_dim, device=agent.device))
            cands = agent.generate_trajectories(lat, e1, td)
            action = agent.select_action(cands, td, 1.0)
        agent._step_count += 1
        d = agent.e3.last_score_diagnostics
        if d is None or "urgency_applied" not in d:
            nlat += 1
        else:
            nfresh += 1
            rows.append(dict(tick=tick, u=assigned, rv=float(d["commit_variance"]),
                             eff=float(d["effective_threshold"]),
                             realized=float(d["urgency_applied"])))
        act_idx = int(action.argmax().item()) if torch.is_tensor(action) else int(action)
        ap = torch.zeros(1, env.action_dim); ap[0, act_idx % env.action_dim] = 1.0
        zp = zc
        _o, _r, done, _i, od = env.step(act_idx % env.action_dim)
        if done:
            _o, od = env.reset()
    return rows, nfresh, nlat, landed, warm_diag

if __name__ == "__main__":
    import time
    thr = float(sys.argv[1]); seed = int(sys.argv[2]); n = int(sys.argv[3])
    warm = (len(sys.argv) > 4 and sys.argv[4] == "warm")
    p0_eps = int(sys.argv[5]) if len(sys.argv) > 5 else 60
    t0 = time.time()
    rng = np.random.default_rng(1234 + seed)
    rows, nf, nl, landed, wd = run(seed, thr, n, rng, warm=warm, p0_episodes=p0_eps)
    post = [r for r in rows if r["tick"] >= 90]
    rv = np.array([r["rv"] for r in post]) if post else np.array([np.nan])
    p99 = float(np.percentile(rv, 99)); p1 = float(np.percentile(rv, 1))
    wsum = None
    if wd is not None:
        wsum = {k: v for k, v in wd.items() if not isinstance(v, (list, tuple))}
    print(json.dumps(dict(
        arm=("WARM" if warm else "COLD"), p0_episodes=(p0_eps if warm else 0), seed=seed, thr=thr, elapsed_s=round(time.time()-t0, 1),
        from_dims_landed=landed, n_fresh=nf, n_latched=nl, n_post=len(post),
        rv_med=float(np.median(rv)), rv_p1=p1, rv_p99=p99,
        dispersion_p99_over_p1=float(p99/p1) if p1 > 0 else float("inf"),
        iqr_over_med=float((np.percentile(rv,75)-np.percentile(rv,25))/np.median(rv)),
        commit_rate_by_level={str(u): float(np.mean([r["rv"] < r["eff"] for r in post if r["u"]==u]))
                              for u in URG},
        n_by_level={str(u): sum(1 for r in post if r["u"]==u) for u in URG},
        max_fidelity_err=float(max((abs(r["realized"]-r["u"]) for r in post), default=float("nan"))),
        warmup=wsum,
    ), indent=1))
