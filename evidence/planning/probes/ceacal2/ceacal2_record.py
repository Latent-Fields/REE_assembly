"""CeA onset-input re-probe, RECORD stage (bt0925-ceacal2). EVAL only (no TRAIN/regime-B
this round -- probe1 P3 showed the relative gates are scale-invariant across encoder
training, so this reprobe isolates INPUT choice/env config, regime A (untrained) only).

usage: cd <ree-v3 worktree @ 2ea0e3c>; python ceacal2_record.py . <seed> <steps> <num_hazards> <decay> <out.pt>
  env/agent seed = seed + 1000 (EVAL convention, matches ceacal_record.py).
Records, per step t, aligned to obs_t (the obs CeA/HarmEncoder read on the step-t sense()):
  harm_obs_a[50] (X), harm_obs[51] (HO, SD-010 input for z_harm_s), harm_history[10] (H),
  hazard_field/resource_field at the agent cell (HZ/RZ), nearest-hazard Manhattan distance
  (DM), transition_type (TT), episode index (EP), steps-into-episode (TE),
  agent's own CeA low_freq_magnitude (SA, z_harm_a instrument check) and mean|z_harm| from
  agent._current_latent.z_harm (SS, z_harm_s instrument check).
EXP-0787 probe config + harm_history_len=10, num_hazards/hazard_field_decay overridden per
arg. world_dim=self_dim=32. 2 threads. ASCII out.
"""
import json, sys, time
root = sys.argv[1]; sys.path.insert(0, root)
seed0 = int(sys.argv[2]); steps = int(sys.argv[3])
num_hazards = int(sys.argv[4]); decay = float(sys.argv[5]); outp = sys.argv[6]
seed = seed0 + 1000
import torch, random, numpy as np
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from experiments._harness import StepHarness
HL = 10
torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
env = CausalGridWorldV2(seed=seed, size=10, num_hazards=num_hazards, num_resources=3,
    harm_history_len=HL, hazard_field_decay=decay)
cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
    action_dim=env.action_dim, self_dim=32, world_dim=32, reafference_action_dim=env.action_dim,
    alpha_world=0.9, use_harm_stream=True, use_affective_harm_stream=True, harm_history_len=HL,
    use_amygdala_analog=True, use_cea_analog=True, use_broadcast_override=True,
    use_salience_coordinator=True, use_pag_freeze_gate=True, use_closure_operator=True,
    use_lateral_pfc_analog=True, use_habenula_decommit=True)
agent = REEAgent(cfg)
assert agent.latent_stack.harm_encoder is not None
assert agent.latent_stack.affective_harm_encoder is not None
h = StepHarness(agent, env, train_mode=False, seed=seed)
flat, obs = env.reset(); agent.reset(); h.reset()
X, HO, H, HZ, RZ, TT, EP, SA, SS, DM, TE, RD = [], [], [], [], [], [], [], [], [], [], [], []
t_ep = 0
ep = 0; t0 = time.time(); n_inj = 0
for t in range(steps):
    ax, ay = int(env.agent_x), int(env.agent_y)
    HZ.append(float(np.clip(env.hazard_field[ax, ay], 0.0, 1.0)))
    RZ.append(float(np.clip(env.resource_field[ax, ay], 0.0, 1.0)))
    TT.append(str(env._last_transition_type)); EP.append(ep); TE.append(t_ep)
    DM.append(min(abs(ax - int(hx)) + abs(ay - int(hy)) for hx, hy in env.hazards) if env.hazards else 99)
    RD.append(min(abs(ax - int(rx)) + abs(ay - int(ry)) for rx, ry in env.resources) if env.resources else 99)
    X.append(torch.as_tensor(obs["harm_obs_a"], dtype=torch.float32).reshape(1, -1))
    HO.append(torch.as_tensor(obs["harm_obs"], dtype=torch.float32).reshape(1, -1))
    H.append(torch.as_tensor(obs["harm_history"], dtype=torch.float32).reshape(1, -1))
    if t % 30 == 15 and env._inject_external_hazard():
        n_inj += 1
    res = h.step(obs); obs = res.next_obs_dict
    co = agent._cea_last_output
    SA.append(float(co.low_freq_magnitude) if co is not None else float("nan"))
    zh = agent._current_latent.z_harm if agent._current_latent is not None else None
    SS.append(float(zh.abs().mean()) if zh is not None else float("nan"))
    t_ep += 1
    if res.done:
        ep += 1; t_ep = 0
        flat, obs = env.reset(); agent.reset(); h.reset()
enc_state_a = {k: v.clone() for k, v in agent.latent_stack.affective_harm_encoder.state_dict().items()}
enc_state_s = {k: v.clone() for k, v in agent.latent_stack.harm_encoder.state_dict().items()}
torch.save(dict(X=torch.cat(X), HO=torch.cat(HO), H=torch.cat(H), HZ=torch.tensor(HZ),
                RZ=torch.tensor(RZ), TT=TT, EP=torch.tensor(EP), SA=torch.tensor(SA),
                SS=torch.tensor(SS), DM=torch.tensor(DM), TE=torch.tensor(TE), RD=torch.tensor(RD),
                enc_state_a=enc_state_a, enc_state_s=enc_state_s,
                seed=seed, steps=steps, n_inj=n_inj, num_hazards=num_hazards, decay=decay), outp)
print(json.dumps(dict(seed=seed, steps=steps, episodes=ep + 1, n_inj=n_inj,
                      num_hazards=num_hazards, decay=decay,
                      wall_s=round(time.time() - t0, 1), adj_steps=int(sum(1 for v in DM if v <= 1)),
                      dmin_hist={str(k): int(sum(1 for v in DM if v == k)) for k in range(0, 6)},
                      hz_mean=round(float(np.mean(HZ)), 4), hz_min=round(float(np.min(HZ)), 4))))
