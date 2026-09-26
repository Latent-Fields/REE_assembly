"""Matched OFF/ON comparison: scripted actions (local rng), identical env trajectories,
sense-only; per-seed PR of z_world and reset enrichment in the 0-1st pctile bucket.
Usage: matched_pr.py <tree>. world_dim=self_dim=32 (deployed)."""
import sys, warnings; warnings.filterwarnings("ignore")
tree = sys.argv[1]; sys.path.insert(0, tree)
import numpy as np, torch
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
def pr(z):
    z = z - z.mean(0, keepdim=True); cov = (z.T @ z) / max(z.shape[0]-1, 1)
    ev = torch.linalg.eigvalsh(cov).clamp(min=0); return float(ev.sum()**2 / (ev**2).sum())
def run(flag, alpha, seed, n_ep=8, ep_len=40):
    torch.manual_seed(seed)
    env = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=seed)
    cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
        action_dim=env.action_dim, self_dim=32, world_dim=32, alpha_world=alpha, use_zworld_ema_reset_init=flag)
    ag = REEAgent(cfg); rng = np.random.default_rng(seed); rows = []
    for ep in range(n_ep):
        env = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=1000*seed+ep)
        _f, od = env.reset(); ag.reset()
        for t in range(ep_len):
            with torch.no_grad():
                lat = ag.sense(torch.as_tensor(od["body_state"]).float().unsqueeze(0), torch.as_tensor(od["world_state"]).float().unsqueeze(0))
            rows.append((t, lat.z_world.reshape(-1).clone()))
            _f, _h, done, _i, od = env.step(int(rng.integers(env.action_dim)))
            if done: break
    return rows
all_rows = {}
for label, flag, alpha in (("OFF a0.3", False, 0.3), ("ON  a0.3", True, 0.3), ("OFF a0.9", False, 0.9), ("ON  a0.9", True, 0.9)):
    prs, pooled = [], []
    for s in (106, 107, 108, 109, 110):
        rows = run(flag, alpha, s); pooled += rows
        prs.append(pr(torch.stack([z for _, z in rows])))
    zn = torch.tensor([float(z.norm()) for _, z in pooled]); p1 = float(torch.quantile(zn, 0.01))
    b = [t for (t, z), n in zip(pooled, zn) if float(n) <= p1]
    base = sum(1 for t, _ in pooled if t == 0) / len(pooled)
    enr = (sum(1 for t in b if t == 0) / len(b)) / base
    print("%s n=%d per-seed PR %s  reset-enrich %.2fx (bucket t-values %s)" % (label, len(pooled), " ".join("%.2f" % p for p in prs), enr, sorted(b)))
