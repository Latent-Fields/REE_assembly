import sys, time, torch
sys.path.insert(0, ".")
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
env = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=7)
cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim, action_dim=env.action_dim, self_dim=32, world_dim=32, alpha_world=0.3)
ag = REEAgent(cfg); ag.eval()
_f, obs = env.reset(); ag.reset()
live=[]; raws=[]; acts=[None]
for t in range(12):
    ob = torch.as_tensor(obs["body_state"]).float().reshape(1,-1); ow = torch.as_tensor(obs["world_state"]).float().reshape(1,-1)
    raws.append((ob, ow, obs.get("harm_obs"), obs.get("harm_obs_a"), obs.get("harm_history")))
    lat = ag.sense(ob, ow, obs_harm=obs.get("harm_obs"), obs_harm_a=obs.get("harm_obs_a"), obs_harm_history=obs.get("harm_history"))
    live.append(lat.z_world.detach().clone())
    a = torch.nn.functional.one_hot(torch.tensor([t % 5]), 5).float()
    ag.record_executed_action(a); acts.append(a)
    _f,_h,done,_i,obs = env.step(t % 5)
print("types", [type(x) for x in raws[0][2:]])
@torch.no_grad()
def enc(rs, pas, B=1):
    prev = ag.latent_stack.init_state(batch_size=B, device=ag.device)
    out=[]
    for (ob,ow,h,ha,hh),pa in zip(rs,pas):
        ob=ob.expand(B,-1); ow=ow.expand(B,-1)
        e = torch.cat([ag.body_obs_encoder(ob), ag.world_obs_encoder(ow)], -1)
        f = lambda x: None if x is None else torch.as_tensor(x).float().reshape(1,-1).expand(B,-1)
        prev = ag.latent_stack.encode(e, prev, prev_action=None if pa is None else pa.expand(B,-1), harm_obs=f(h), harm_obs_a=f(ha), harm_history=f(hh))
        out.append(prev.z_world.clone())
    return out
r1 = enc(raws, acts[:12], 1)
print("B1 maxdiff vs live", max(float((a-b).abs().max()) for a,b in zip(r1, live)))
r4 = enc(raws, acts[:12], 4)
print("B4 maxdiff vs live", max(float((a[0:1]-b).abs().max()) for a,b in zip(r4, live)), "rows equal", all(torch.allclose(a[0], a[3]) for a in r4))
t=time.time(); [enc(raws[:10], acts[:10], 32) for _ in range(20)]; print("batched 32x10 per call ms", (time.time()-t)/20*1000)
t=time.time(); [enc(raws[:10], acts[:10], 1) for _ in range(20)]; print("B1 x10 per call ms", (time.time()-t)/20*1000)
