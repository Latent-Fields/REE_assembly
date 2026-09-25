"""modetrace probe (bt0925-modetrace): tick-by-tick SalienceCoordinator trace +
CeA fast-route input trace, under driver-scheduled hazard onsets.

usage: python modetrace_probe.py <repo_root> <arm> <seed> [steps]
arms:
  A0_0787     EXP-0787 probe config (coordinator + CeA + override + PAG + closure/habenula),
              dACC OFF, AIC OFF -- the config MECH-157 / EXP-0787 measured "no switch" in.
  A1_dacc_cap A0 + use_dacc=True + salience_affinity_input_cap=2.0 (the lineage's
              competing input, bounded as in V3-EXQ-464e/934/935a training).
  A2_dacc_nocap A0 + use_dacc=True, no cap (pre-occupancy-fix lineage substrate).
  A3_cea_thr0 A0 with cea_fast_route_threshold=0.0 (INSTRUMENT: forces CeA fire every
              tick; asks what the downstream coordinator does WITH a fire, not whether
              the native gate fires).
  A4_dacc_cap_etd  A1 + use_external_task_drive (affinity 3.0, salience 2.0, the 935a
              weights), goal gate off (engagement = beta-elevated commitment + 0 proximity).
              THE D2 INTERVENTION: an independent external_task-arguing input.
  A5_dacc_cap_etd_nosal  A4 with external_task_drive_salience_weight=0 (affinity half only).
Run: cd <ree-v3 worktree @ 23714f0>; python modetrace_probe.py . <arm> <seed> 300
Untrained agent, CausalGridWorldV2(size=10, 3 hazards, 3 resources), world_dim=32 (deployed),
self_dim=32, alpha_world=0.9. torch threads = 2. Prints one JSON line (ASCII).
"""
import json, sys, math
root = sys.argv[1]; sys.path.insert(0, root)
arm = sys.argv[2]; seed = int(sys.argv[3])
steps = int(sys.argv[4]) if len(sys.argv) > 4 else 300
import torch, random, numpy as np
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from ree_core.cingulate import salience_coordinator as scmod
from experiments._harness import StepHarness

torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
env = CausalGridWorldV2(seed=seed, size=10, num_hazards=3, num_resources=3)
flags = dict(alpha_world=0.9, use_harm_stream=True, use_affective_harm_stream=True,
             use_amygdala_analog=True, use_cea_analog=True, use_broadcast_override=True,
             use_salience_coordinator=True, use_pag_freeze_gate=True, use_closure_operator=True,
             use_lateral_pfc_analog=True, use_habenula_decommit=True)
if arm in ("A1_dacc_cap", "A2_dacc_nocap", "A4_dacc_cap_etd", "A5_dacc_cap_etd_nosal"):
    flags["use_dacc"] = True
if arm in ("A1_dacc_cap", "A4_dacc_cap_etd", "A5_dacc_cap_etd_nosal"):
    flags["salience_affinity_input_cap"] = 2.0
if arm in ("A4_dacc_cap_etd", "A5_dacc_cap_etd_nosal"):
    # the lineage's independent external_task input (V3-EXQ-935a weights); goal gate off
    # because this untrained probe has no z_goal -- engagement = beta-elevated commitment.
    flags.update(use_external_task_drive=True, external_task_drive_affinity_weight=3.0,
                 external_task_drive_salience_weight=(0.0 if arm == "A5_dacc_cap_etd_nosal" else 2.0),
                 external_task_drive_require_goal_active=False)
cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
    action_dim=env.action_dim, self_dim=32, world_dim=32,
    reafference_action_dim=env.action_dim, **flags)
if arm == "A3_cea_thr0":
    cfg.cea_fast_route_threshold = 0.0
agent = REEAgent(cfg)
if arm == "A3_cea_thr0":
    agent.cea.config.fast_route_threshold = 0.0
coord = agent.salience
MODES = list(coord.mode_names)

trace = []
orig_tick = coord.tick
state = {"ep": 0, "t": 0}

def logits_from_inputs(c):
    cfgc = c.config
    lg = {m: 0.0 for m in c.mode_names}
    lg["external_task"] += cfgc.external_task_bias
    contrib = {}
    cap = cfgc.affinity_input_cap
    for sig, mm in cfgc.affinity_weights.items():
        v = c._input_signals.get(sig, 0.0)
        if v == 0.0:
            continue
        if cap is not None:
            v = max(-cap, min(cap, v))
        for m, w in mm.items():
            if m in lg:
                lg[m] += v * w
                contrib[sig + "->" + m] = contrib.get(sig + "->" + m, 0.0) + v * w
    return lg, contrib

def wrapped(*a, **k):
    out = orig_tick(*a, **k)
    lg, contrib = logits_from_inputs(coord)
    srt = sorted(lg.values(), reverse=True)
    sal_parts = {s: w * coord._input_signals.get(s, 0.0) for s, w in coord.config.salience_weights.items()}
    trace.append(dict(ep=state["ep"], t=state["t"], logits=lg, contrib=contrib,
                      margin_top2=srt[0] - srt[1],
                      argmax=max(lg.items(), key=lambda kv: kv[1])[0],
                      sal=out["salience_aggregate"], sal_parts=sal_parts,
                      enter=out["enter_threshold"], cur=out["current_mode"],
                      trig=out["mode_switch_trigger"],
                      inputs={k: coord._input_signals.get(k, 0.0) for k in (
                          "dacc_pe", "dacc_foraging", "dacc_difficulty", "drive_level",
                          "cea_mode_prior", "cea_fast_prime", "override_signal",
                          "aic_salience", "pcc_stability", "external_task_drive")}))
    return out
coord.tick = wrapped

h = StepHarness(agent, env, train_mode=True, seed=seed)
flat, obs = env.reset(); agent.reset(); h.reset()
inj = []; lf = []; fires = 0; lf_post = []; lf_pre = []
last_inj = -999
for t in range(steps):
    state["t"] = t
    if t % 30 == 15:
        if env._inject_external_hazard():
            inj.append(t); last_inj = t
    res = h.step(obs); obs = res.next_obs_dict
    co = agent._cea_last_output
    if co is not None:
        lf.append(float(co.low_freq_magnitude)); fires += int(bool(co.urgency_fire))
        if 0 <= t - last_inj <= 10:
            lf_post.append(float(co.low_freq_magnitude))
        elif t - last_inj > 10:
            lf_pre.append(float(co.low_freq_magnitude))
    if res.done:
        state["ep"] += 1
        flat, obs = env.reset(); agent.reset(); h.reset()

def mean(x):
    return sum(x) / len(x) if x else None

n = len(trace)
sw_by_ep = {}
for r in trace:
    sw_by_ep.setdefault(r["ep"], 0)
    sw_by_ep[r["ep"]] += int(r["trig"])
within_extra = sum(max(0, v - 1) for v in sw_by_ep.values())
fail_argmax = sum(1 for r in trace if r["argmax"] == r["cur"])
fail_sal = sum(1 for r in trace if r["sal"] <= r["enter"])
both_ok = sum(1 for r in trace if r["argmax"] != r["cur"] and r["sal"] > r["enter"])
argmax_counts = {m: sum(1 for r in trace if r["argmax"] == m) for m in MODES}
cur_counts = {m: sum(1 for r in trace if r["cur"] == m) for m in MODES}
inp_stats = {}
for k in trace[0]["inputs"] if trace else []:
    vals = [r["inputs"][k] for r in trace]
    inp_stats[k] = dict(mean=round(mean(vals), 4), max=round(max(vals), 4), min=round(min(vals), 4))
contrib_keys = sorted({ck for r in trace for ck in r["contrib"]})
contrib_stats = {ck: round(mean([r["contrib"].get(ck, 0.0) for r in trace]), 4) for ck in contrib_keys}
sal_part_stats = {s: dict(mean=round(mean([r["sal_parts"].get(s, 0.0) for r in trace]), 4),
                          max=round(max([r["sal_parts"].get(s, 0.0) for r in trace]), 4))
                  for s in (trace[0]["sal_parts"] if trace else {})}
# ext logit - best non-ext logit: how far from the argmax flipping, per tick
gap = [r["logits"]["external_task"] - max(v for m, v in r["logits"].items() if m != "external_task") for r in trace]
into = {m: sum(1 for r in trace if r["trig"] and r["cur"] == m) for m in MODES}
first_mode_ticks = sum(1 for r in trace if r["trig"])
out = dict(switch_into_counts=into, arm=arm, seed=seed, steps=steps, n_coord_ticks=n, n_episodes=state["ep"] + 1,
           switches_total=sum(sw_by_ep.values()), switches_by_ep=sw_by_ep,
           within_life_switches_beyond_first=within_extra,
           ticks_argmax_eq_current=fail_argmax, ticks_sal_le_thr=fail_sal, ticks_both_conditions_met=both_ok,
           argmax_counts=argmax_counts, current_mode_counts=cur_counts,
           ext_minus_best_other_logit=dict(mean=round(mean(gap), 4), min=round(min(gap), 4), max=round(max(gap), 4)) if gap else None,
           sal_aggregate=dict(mean=round(mean([r["sal"] for r in trace]), 4), max=round(max([r["sal"] for r in trace]), 4)) if trace else None,
           enter_threshold_mean=round(mean([r["enter"] for r in trace]), 4) if trace else None,
           sal_parts=sal_part_stats, inputs=inp_stats, affinity_contrib_mean=contrib_stats,
           cea=dict(n_ticks=len(lf), fires=fires, lowfreq_max=round(max(lf), 4) if lf else None,
                    lowfreq_mean=round(mean(lf), 4) if lf else None,
                    lowfreq_post_inj_mean=round(mean(lf_post), 4) if lf_post else None,
                    lowfreq_other_mean=round(mean(lf_pre), 4) if lf_pre else None,
                    threshold=agent.cea.config.fast_route_threshold),
           n_inj=len(inj))
print(json.dumps(out))
