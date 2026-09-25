"""Q2b (bt0925-modetrace): does the ONLY existing training objective for the CeA input encoder
(SD-011 harm_accum aux, agent.compute_harm_accum_loss -> AffectiveHarmEncoder.harm_accum_head,
Linear+Sigmoid, MSE to accumulated_harm) lift CeA low_freq = mean|z_harm_a| toward 0.5?

usage: python cea_harmaccum_probe.py <repo_root> <seed> [steps] [train_iters]
Records (harm_obs_a, harm_history, accumulated_harm) from a harness run (harm_history_len=10),
then trains the encoder offline with the same loss compute_harm_accum_loss applies
(MSE(harm_accum_pred, accumulated_harm) -- the SD-020 surprise variant is off by default),
Adam lr 1e-3. Reports low_freq on the recorded inputs before/after. 2 threads, world_dim=32.
"""
import json, sys
root = sys.argv[1]; sys.path.insert(0, root)
seed = int(sys.argv[2]); steps = int(sys.argv[3]) if len(sys.argv) > 3 else 300
iters = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
import torch, random, numpy as np
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from experiments._harness import StepHarness
HL = 10
torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
env = CausalGridWorldV2(seed=seed, size=10, num_hazards=3, num_resources=3, harm_history_len=HL)
cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
    action_dim=env.action_dim, self_dim=32, world_dim=32, reafference_action_dim=env.action_dim,
    alpha_world=0.9, use_harm_stream=True, use_affective_harm_stream=True, harm_history_len=HL,
    use_amygdala_analog=True, use_cea_analog=True, use_salience_coordinator=True)
agent = REEAgent(cfg)
enc = agent.latent_stack.affective_harm_encoder
assert enc.harm_accum_head is not None
h = StepHarness(agent, env, train_mode=False, seed=seed)
flat, obs = env.reset(); agent.reset(); h.reset()
X, H, Y = [], [], []
for t in range(steps):
    if t % 30 == 15:
        env._inject_external_hazard()
    X.append(torch.as_tensor(obs["harm_obs_a"], dtype=torch.float32).reshape(1, -1))
    H.append(torch.as_tensor(obs["harm_history"], dtype=torch.float32).reshape(1, -1))
    Y.append(float(obs["accumulated_harm"]))
    res = h.step(obs); obs = res.next_obs_dict
    if res.done:
        flat, obs = env.reset(); agent.reset(); h.reset()
X = torch.cat(X); H = torch.cat(H); Y = torch.tensor(Y).reshape(-1, 1)

def lf():
    with torch.no_grad():
        z, _ = enc(X, H)
    v = z.abs().mean(-1)
    return float(v.mean()), float(v.max())
b_mean, b_max = lf()
opt = torch.optim.Adam(enc.parameters(), lr=1e-3)
losses = []
for i in range(iters):
    idx = torch.randint(0, X.shape[0], (32,))
    _, pred = enc(X[idx], H[idx])
    loss = torch.nn.functional.mse_loss(pred, Y[idx])
    opt.zero_grad(); loss.backward(); opt.step()
    if i % max(1, iters // 4) == 0 or i == iters - 1:
        losses.append(round(float(loss), 5))
a_mean, a_max = lf()
print(json.dumps(dict(seed=seed, steps=steps, iters=iters, n=int(X.shape[0]),
    accumulated_harm_range=[round(float(Y.min()), 4), round(float(Y.max()), 4)],
    loss_trace=losses, lowfreq_before=dict(mean=round(b_mean, 4), max=round(b_max, 4)),
    lowfreq_after=dict(mean=round(a_mean, 4), max=round(a_max, 4)), threshold=0.5)))
