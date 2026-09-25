"""OFF identity across trees: same rollout on the pre-build tree (arg 1) and the build tree
(arg 2), W6a knob OFF, (i) default config and (ii) trainer ON with harm_eval + T1 + W3 +
codec. Prints a sha256 over actions, z_world, final state_dict and RNG states."""
import hashlib, subprocess, sys
CODE = r'''
import sys, hashlib, random, numpy as np, torch
torch.set_num_threads(2)
from experiments._harness import StepHarness
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
def env(s): return CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=s)
e = env(5)
flags = {} if sys.argv[1] == "default" else dict(
    waking_trainer_enabled=True, waking_trainer_batch_size=4, waking_trainer_e1_enabled=True,
    waking_trainer_e2_self_enabled=True, waking_trainer_codec_enabled=True,
    waking_trainer_e2_world_enabled=True, waking_trainer_e2_world_batch_size=4)
cfg = REEConfig.from_dims(body_obs_dim=e.body_obs_dim, world_obs_dim=e.world_obs_dim,
    action_dim=e.action_dim, self_dim=32, world_dim=32, alpha_world=0.9, **flags)
torch.manual_seed(5); np.random.seed(5); random.seed(5)
a = REEAgent(cfg); h = StepHarness(a, e, train_mode=True, seed=5)
H = hashlib.sha256(); n = 0
while n < 60:
    for r in h.run_episode(max_steps=20):
        n += 1; H.update(r.action.detach().numpy().tobytes()); H.update(r.latent.z_world.detach().numpy().tobytes())
for k, v in a.state_dict().items(): H.update(k.encode()); H.update(v.detach().numpy().tobytes())
H.update(torch.get_rng_state().numpy().tobytes()); H.update(np.random.get_state()[1].tobytes())
H.update(repr(random.getstate()).encode())
print(H.hexdigest(), (a.waking_trainer.report() if a.waking_trainer else None))
'''
for mode in ("default", "trainer_on"):
    outs = []
    for tree in sys.argv[1:3]:
        r = subprocess.run([sys.executable, "-c", CODE, mode], cwd=tree, capture_output=True, text=True)
        outs.append(r.stdout.strip() or r.stderr[-300:])
    print(mode, "IDENTICAL" if outs[0].split()[0] == outs[1].split()[0] else "DIFFERENT")
    for o in outs: print("   ", o[:200])
