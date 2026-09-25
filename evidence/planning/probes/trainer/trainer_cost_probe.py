#!/opt/local/bin/python3
"""Cost-per-tick probe for the native waking trainer options (bt0925-trainer).

Native REEConfig.from_dims defaults (world_dim=32, deployed), CausalGridWorldV2(seed).
Fills the replay buffers with 60 StepHarness ticks, then times (median of 30):
  act     one StepHarness tick (train_mode=False)
  e1      compute_prediction_loss + backward + Adam(e1).step
  e2s     compute_e2_loss + backward + Adam(e2 self heads).step
  e2w     compute_e2_world_loss + backward + Adam(e2 world heads).step
  harm    harm_eval_head MSE on a 16-row replay batch + backward + step
Also checks RNG neutrality of the fork_rng + private-state wrapper: the global torch RNG state
after a wrapped trainer update equals the state before it (bit-identity for the act path).
ASCII-only output.
"""
import os
import statistics
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(HERE, "ree-v3-wt")
sys.path.insert(0, WT)
sys.path.insert(0, os.path.join(WT, "experiments"))
os.chdir(WT)

import torch  # noqa: E402
import torch.nn.functional as F  # noqa: E402
torch.set_num_threads(2)
torch.manual_seed(42)

from ree_core.agent import REEAgent  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402

env = CausalGridWorldV2(seed=42)
cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
                          action_dim=env.action_dim)
agent = REEAgent(cfg)
h = StepHarness(agent, env, train_mode=True, seed=42)
_, obs = env.reset()
agent.reset()
h.reset()
harm_buf = []
for _ in range(60):
    r = h.step(obs)
    obs = r.next_obs_dict
    harm_buf.append((r.latent.z_world.detach(), abs(min(float(r.harm_signal), 0.0))))
    if r.done:
        _, obs = env.reset()
print("buffers: world=%d e2=%d" % (len(agent._world_experience_buffer),
                                    len(agent._e2_transition_buffer)))

opt_e1 = torch.optim.Adam(agent.e1.parameters(), lr=1e-4)
opt_e2s = torch.optim.Adam(list(agent.e2.self_transition.parameters())
                           + list(agent.e2.self_action_encoder.parameters()), lr=1e-4)
opt_e2w = torch.optim.Adam(list(agent.e2.world_transition.parameters())
                           + list(agent.e2.world_action_encoder.parameters()), lr=1e-4)
opt_h = torch.optim.Adam(agent.e3.harm_eval_head.parameters(), lr=1e-4)


def step(opt, loss):
    if loss.requires_grad:
        opt.zero_grad()
        loss.backward()
        opt.step()


def harm_loss():
    idx = torch.randint(0, len(harm_buf), (16,))
    z = torch.cat([harm_buf[i][0] for i in idx.tolist()])
    t = torch.tensor([[harm_buf[i][1]] for i in idx.tolist()])
    return F.mse_loss(agent.e3.harm_eval_head(z), t)


fns = {
    "e1": lambda: step(opt_e1, agent.compute_prediction_loss()),
    "e2s": lambda: step(opt_e2s, agent.compute_e2_loss()),
    "e2w": lambda: step(opt_e2w, agent.compute_e2_world_loss()),
    "harm": lambda: step(opt_h, harm_loss()),
}
h_eval = StepHarness(agent, env, train_mode=False, seed=43)


def act():
    global obs
    r = h_eval.step(obs)
    obs = r.next_obs_dict
    if r.done:
        _, obs = env.reset()


times = {}
for name, fn in [("act", act)] + list(fns.items()):
    ts = []
    for _ in range(30):
        t0 = time.perf_counter()
        fn()
        ts.append(time.perf_counter() - t0)
    times[name] = statistics.median(ts) * 1000.0
for k, v in times.items():
    print("median_ms %-5s %.2f" % (k, v))
tr = times["e1"] + times["e2s"] + times["e2w"] + times["harm"]
print("trainer_all_four_ms %.2f  ratio_to_act_tick %.2f" % (tr, tr / times["act"]))

# RNG-neutrality of the wrapper: private generator state swapped into a forked global RNG.
priv = torch.Generator().manual_seed(1234).get_state()
before = torch.get_rng_state().clone()
with torch.random.fork_rng(devices=[]):
    torch.set_rng_state(priv)
    for fn in fns.values():
        fn()
    priv = torch.get_rng_state().clone()
after = torch.get_rng_state()
print("rng_neutral_with_fork_rng %s" % bool(torch.equal(before, after)))
before = torch.get_rng_state().clone()
fns["e1"]()
print("rng_neutral_without_wrapper %s" % bool(torch.equal(before, torch.get_rng_state())))
