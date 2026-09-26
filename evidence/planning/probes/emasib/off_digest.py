"""OFF pre/post digest: native-policy agent rollout, default config (flag absent),
hash z_world/z_self bytes + actions over several resets. Same machine both trees."""
import sys, hashlib, warnings
warnings.filterwarnings("ignore")
tree = sys.argv[1]; sys.path.insert(0, tree)
import numpy as np, torch
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
h = hashlib.sha256(); n = 0
for alpha in (0.3, 0.9):
    torch.manual_seed(106); np.random.seed(106)
    env = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=106)
    cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
        action_dim=env.action_dim, self_dim=32, world_dim=32, alpha_world=alpha)
    agent = REEAgent(cfg)
    for ep in range(3):
        env = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=106000 + ep)
        _f, od = env.reset(); agent.reset()
        for t in range(20):
            with torch.no_grad():
                a = agent.act_with_split_obs(torch.as_tensor(od["body_state"]).float(), torch.as_tensor(od["world_state"]).float())
            lat = agent._current_latent
            for x in (lat.z_world, lat.z_self, lat.z_beta, lat.z_theta, lat.z_delta, a):
                h.update(x.detach().contiguous().numpy().tobytes())
            n += 1
            _f, _h, done, _i, od = env.step(a)
            if done: break
print("ticks", n, "digest", h.hexdigest())
