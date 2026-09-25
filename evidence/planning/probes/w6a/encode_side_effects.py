import sys, copy, torch
sys.path.insert(0, "/Users/dgolden/REE_Working/.scratch/wt-w6a")
torch.set_num_threads(2)
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from ree_core.agent import REEAgent
e = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=7)
c = REEConfig.from_dims(body_obs_dim=e.body_obs_dim, world_obs_dim=e.world_obs_dim,
                        action_dim=e.action_dim, self_dim=32, world_dim=32, alpha_world=0.3)
torch.manual_seed(0)
a = REEAgent(c)
f, o = e.reset()
a.sense(torch.as_tensor(o["body_state"]).float(), torch.as_tensor(o["world_state"]).float())
sd0 = {k: v.clone() for k, v in a.state_dict().items()}
def attrs(m):
    return {k: (v.clone() if torch.is_tensor(v) else repr(v)[:80]) for k, v in vars(m).items() if not k.startswith("_modules") and not k.startswith("_parameters") and not k.startswith("_buffers")}
ls = a.latent_stack
before = {n: attrs(m) for n, m in ls.named_modules()}
rng = torch.get_rng_state().clone()
with torch.enable_grad():
    prev = ls.init_state(batch_size=4, device=a.device)
    for j in range(5):
        ob = torch.randn(4, e.body_obs_dim); ow = torch.rand(4, e.world_obs_dim)
        enc = torch.cat([a.body_obs_encoder(ob), a.world_obs_encoder(ow)], -1)
        prev = ls.encode(enc, prev, prev_action=torch.eye(5)[:4])
    prev.z_world.sum().backward()
print("rng same:", torch.equal(rng, torch.get_rng_state()))
print("state same:", all(torch.equal(sd0[k], v) for k, v in a.state_dict().items()))
after = {n: attrs(m) for n, m in ls.named_modules()}
for n in before:
    for k in before[n]:
        x, y = before[n][k], after[n].get(k)
        same = torch.equal(x, y) if torch.is_tensor(x) and torch.is_tensor(y) and x.shape == y.shape else x == y if not torch.is_tensor(x) else False
        if not same:
            print("CHANGED", n, k)
got = sorted(n for n, p in a.named_parameters() if p.grad is not None and p.grad.abs().sum() > 0)
print("grad reached:", got)
