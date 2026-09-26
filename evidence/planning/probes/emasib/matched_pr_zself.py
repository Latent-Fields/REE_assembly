"""Matched OFF/ON comparison for the sibling reset-init knobs (report-only).
Scripted actions from np.random.default_rng(seed), identical env trajectories,
sense-only. Per-seed PR of z_self (and z_beta) + reset enrichment in the
0-1st pctile ||z_self|| bucket. Same design as emainit/matched_pr.py.
Usage: matched_pr_zself.py <tree>. self_dim=world_dim=32 (deployed),
alpha_world=alpha_self=0.3 (deployed defaults), z_world knob OFF."""
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
def run(knobs, seed, n_ep=8, ep_len=40):
    torch.manual_seed(seed)
    env = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=seed)
    cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
        action_dim=env.action_dim, self_dim=32, world_dim=32, alpha_world=0.3, alpha_self=0.3,
        **{k: True for k in knobs})
    ag = REEAgent(cfg); rng = np.random.default_rng(seed); rows = []
    for ep in range(n_ep):
        env = CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=1000*seed+ep)
        _f, od = env.reset(); ag.reset()
        for t in range(ep_len):
            with torch.no_grad():
                lat = ag.sense(torch.as_tensor(od["body_state"]).float().unsqueeze(0), torch.as_tensor(od["world_state"]).float().unsqueeze(0))
            rows.append((t, lat.z_self.reshape(-1).clone(), lat.z_beta.reshape(-1).clone()))
            _f, _h, done, _i, od = env.step(int(rng.integers(env.action_dim)))
            if done: break
    return rows
def enrich(pooled, idx):
    zn = torch.tensor([float(r[idx].norm()) for r in pooled]); p1 = float(torch.quantile(zn, 0.01))
    b = [r[0] for r, n in zip(pooled, zn) if float(n) <= p1]
    base = sum(1 for r in pooled if r[0] == 0) / len(pooled)
    return (sum(1 for t in b if t == 0) / len(b)) / base, sorted(b)
ARMS = (("OFF", ()), ("zself ON", ("use_zself_ema_reset_init",)),
        ("shared ON", ("use_shared_ema_reset_init",)),
        ("zself+shared ON", ("use_zself_ema_reset_init", "use_shared_ema_reset_init")))
for label, knobs in ARMS:
    prs_s, prs_b, pooled = [], [], []
    for s in (106, 107, 108, 109, 110):
        rows = run(knobs, s); pooled += rows
        prs_s.append(pr(torch.stack([r[1] for r in rows]))); prs_b.append(pr(torch.stack([r[2] for r in rows])))
    es, bs = enrich(pooled, 1); eb, bb = enrich(pooled, 2)
    print("%-16s n=%d | z_self PR %s mean %.2f enrich %.2fx bucket-t %s | z_beta PR %s mean %.2f enrich %.2fx" % (
        label, len(pooled), " ".join("%.2f" % p for p in prs_s), sum(prs_s)/5, es, bs,
        " ".join("%.2f" % p for p in prs_b), sum(prs_b)/5, eb))
