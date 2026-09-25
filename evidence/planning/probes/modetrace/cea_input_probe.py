"""CeA fast-route input probe (bt0925-modetrace, Q2).

usage: python cea_input_probe.py <repo_root> <seed> [steps]

Q2a: does training e3.harm_eval_head with the native WakingTrainer (cc20be5,
     HarmEvalMember) move the CeA gate's input? CeA reads
     low_freq = mean|z_harm_a| where z_harm_a = LatentStack.affective_harm_encoder(harm_obs_a).
     Measured by (i) hashing affective_harm_encoder params and harm_eval_head params before/after
     a trainer-ON run, and (ii) low_freq on a FIXED battery of recorded harm_obs_a inputs before/after.
Q2b: dynamic range of the gate at init: low_freq on recorded inputs, on the all-ones input
     (every hazard/resource field cell saturated), and on k x recorded inputs.
EXP-0787 probe config + waking_trainer_enabled=True. world_dim=32, 2 threads. ASCII JSON out.
"""
import json, sys, hashlib
root = sys.argv[1]; sys.path.insert(0, root)
seed = int(sys.argv[2]); steps = int(sys.argv[3]) if len(sys.argv) > 3 else 300
import torch, random, numpy as np
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from experiments._harness import StepHarness

torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
env = CausalGridWorldV2(seed=seed, size=10, num_hazards=3, num_resources=3)
cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
    action_dim=env.action_dim, self_dim=32, world_dim=32, reafference_action_dim=env.action_dim,
    alpha_world=0.9, use_harm_stream=True, use_affective_harm_stream=True,
    use_amygdala_analog=True, use_cea_analog=True, use_broadcast_override=True,
    use_salience_coordinator=True, use_pag_freeze_gate=True, use_closure_operator=True,
    use_lateral_pfc_analog=True, use_habenula_decommit=True,
    waking_trainer_enabled=True, waking_trainer_guard_min_steps=0)
agent = REEAgent(cfg)
enc = agent.latent_stack.affective_harm_encoder
head = agent.e3.harm_eval_head

def phash(mod):
    h = hashlib.sha256()
    for p in mod.parameters():
        h.update(p.detach().cpu().numpy().tobytes())
    return h.hexdigest()[:16]

def lowfreq(x):
    with torch.no_grad():
        z, _ = enc(x)
    return (z.abs().mean(dim=-1)).tolist()

h = StepHarness(agent, env, train_mode=True, seed=seed)
flat, obs = env.reset(); agent.reset(); h.reset()
battery = []; hz_mass = []
enc0, head0 = phash(enc), phash(head)
last_inj = -999; lf_trace = []
for t in range(steps):
    if t % 30 == 15 and env._inject_external_hazard():
        last_inj = t
    hoa = obs.get("harm_obs_a")
    if hoa is not None and len(battery) < 400:
        v = torch.as_tensor(hoa, dtype=torch.float32).reshape(1, -1)
        battery.append(v); hz_mass.append(float(v[0, :25].sum()))
    res = h.step(obs); obs = res.next_obs_dict
    co = agent._cea_last_output
    if co is not None:
        lf_trace.append((t - last_inj, float(co.low_freq_magnitude)))
    if res.done:
        flat, obs = env.reset(); agent.reset(); h.reset()
enc1, head1 = phash(enc), phash(head)
wt = getattr(agent, "waking_trainer", None) or getattr(agent, "_waking_trainer", None)
B = torch.cat(battery, 0)
lf_rec = lowfreq(B)
# correlation of low_freq with hazard-field mass in harm_obs_a
hm = np.array(hz_mass); lr = np.array(lf_rec)
corr = float(np.corrcoef(hm, lr)[0, 1]) if hm.std() > 0 and lr.std() > 0 else None
ones = torch.ones(1, B.shape[1])
ranges = {"recorded_max": max(lf_rec), "recorded_mean": float(np.mean(lf_rec)),
          "zeros": lowfreq(torch.zeros(1, B.shape[1]))[0], "all_ones": lowfreq(ones)[0],
          "hazard_half_ones": lowfreq(torch.cat([torch.ones(1, 25), torch.zeros(1, B.shape[1] - 25)], 1))[0]}
for k in (2, 5, 10):
    ranges["x%d_recorded_max" % k] = max(lowfreq(B * k))
post = [v for d, v in lf_trace if 0 <= d <= 10]; other = [v for d, v in lf_trace if d > 10]
out = dict(seed=seed, steps=steps, harm_obs_a_dim=int(B.shape[1]),
           harm_obs_a_value_range=[float(B.min()), float(B.max())],
           encoder_hash_before=enc0, encoder_hash_after=enc1, encoder_changed=enc0 != enc1,
           harm_eval_head_hash_before=head0, harm_eval_head_hash_after=head1, harm_eval_head_changed=head0 != head1,
           waking_trainer_present=wt is not None,
           lowfreq_ranges={k: round(float(v), 4) for k, v in ranges.items()},
           corr_lowfreq_vs_hazard_field_mass=None if corr is None else round(corr, 4),
           lowfreq_post_inj_mean=round(float(np.mean(post)), 4) if post else None,
           lowfreq_other_mean=round(float(np.mean(other)), 4) if other else None,
           threshold=agent.cea.config.fast_route_threshold)
print(json.dumps(out))
