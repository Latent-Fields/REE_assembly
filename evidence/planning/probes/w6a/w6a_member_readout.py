"""W6a member readout (D1, report-only; not a pre-registered gate).

For each seed: build the agent (8x8 CausalGridWorldV2, 3 hazards, 2 resources,
world_dim = self_dim = 32, alpha_world given), drive a uniform-random policy for N waking
steps through REEAgent.sense + update_residue with the waking trainer ON and the W6a member
either ON or OFF (OFF = the trainer holds harm_eval only, so the encoder stays untrained).
Then, with every parameter frozen, collect the SENSED z_world on held-out episodes (fresh env
seeds) and report:
  PR     participation ratio of sensed z_world (SD-070 anti-collapse gate: >= 2.0 and
         >= 0.5 x the untrained PR);
  BA_*   held-out balanced accuracy of a logistic probe (fit on half the held-out episodes,
         scored on the other half) for hazard_present / resource_present / hazard_distance /
         resource_distance (scene_structure_targets of the tick's own world_obs);
  wobs_d relative change of world_obs_encoder.0.weight (the pre-projection).
Usage: w6a_member_readout.py <tree> <alpha> <steps> <seed> [<seed>...]
"""
import sys, time, random
import numpy as np, torch, torch.nn.functional as F
tree, alpha, steps = sys.argv[1], float(sys.argv[2]), int(sys.argv[3])
seeds = [int(s) for s in sys.argv[4:]]
sys.path.insert(0, tree)
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from ree_core.latent.zworld_p0 import scene_structure_targets

def env(s): return CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=s)
def oa(o): return dict(obs_harm=o.get("harm_obs"), obs_harm_a=o.get("harm_obs_a"), obs_harm_history=o.get("harm_history"))

def drive(agent, n, env_seed0, rng, update=True, collect=False, ep_len=60):
    k = env_seed0; e = env(k); _f, o = e.reset(); agent.reset(); t = 0; Z, WO, EP = [], [], []
    for _ in range(n):
        with torch.set_grad_enabled(update):
            lat = agent.sense(torch.as_tensor(o["body_state"]).float(), torch.as_tensor(o["world_state"]).float(), **oa(o))
        if collect:
            Z.append(lat.z_world.detach().reshape(-1).clone()); WO.append(torch.as_tensor(o["world_state"]).float().reshape(1, -1)); EP.append(k)
        c = int(rng.integers(0, 5))
        agent.record_executed_action(F.one_hot(torch.tensor([c]), 5).float())
        _f, h, done, _i, o = e.step(c); t += 1
        if update:
            agent.update_residue(float(h))
        if done or t >= ep_len:
            k += 1; e = env(k); _f, o = e.reset(); agent.reset(); t = 0
            if agent.waking_trainer is not None: agent.waking_trainer.on_env_reset()
    return Z, WO, EP

def pr(z):
    z = z - z.mean(0, keepdim=True); ev = torch.linalg.eigvalsh((z.T @ z) / (z.shape[0] - 1)).clamp(min=0)
    return float(ev.sum() ** 2 / (ev ** 2).sum())

def probe(Z, y, tr, te, k):
    Zt = (Z - Z[tr].mean(0)) / (Z[tr].std(0) + 1e-6)
    g = torch.Generator().manual_seed(0); lin = torch.nn.Linear(Z.shape[1], k)
    opt = torch.optim.Adam(lin.parameters(), lr=0.05)
    cnt = torch.bincount(y[tr], minlength=k).float(); w = torch.where(cnt > 0, cnt.sum() / (cnt * (cnt > 0).sum()), torch.zeros_like(cnt))
    for _ in range(300):
        opt.zero_grad(); F.cross_entropy(lin(Zt[tr]), y[tr], weight=w).backward(); opt.step()
    pred = lin(Zt[te]).argmax(1); yt = y[te]; rec = [float((pred[yt == c] == c).float().mean()) for c in range(k) if int((yt == c).sum()) >= 3]
    return (sum(rec) / len(rec), 1.0 / len(rec)) if rec else (None, None)

for seed in seeds:
    for arm in ("OFF", "ON"):
        env0 = env(seed)
        flags = dict(waking_trainer_enabled=True, waking_trainer_batch_size=16,
                     waking_trainer_world_encoder_enabled=(arm == "ON"))
        cfg = REEConfig.from_dims(body_obs_dim=env0.body_obs_dim, world_obs_dim=env0.world_obs_dim,
                                  action_dim=env0.action_dim, self_dim=32, world_dim=32, alpha_world=alpha, **flags)
        torch.manual_seed(seed); np.random.seed(seed); random.seed(seed)
        agent = REEAgent(cfg)
        w0 = agent.world_obs_encoder[0].weight.detach().clone()
        t0 = time.time()
        drive(agent, steps, 1000 * seed, np.random.default_rng(seed))
        secs = time.time() - t0
        for p in agent.parameters(): p.requires_grad_(False)
        Z, WO, EP = drive(agent, 1200, 1000 * seed + 500, np.random.default_rng(seed + 1), update=False, collect=True)
        Z = torch.stack(Z); WO = torch.cat(WO); EP = np.array(EP)
        tg = scene_structure_targets(WO)
        eps = sorted(set(EP.tolist())); half = set(eps[: len(eps) // 2])
        tr = torch.tensor([e in half for e in EP]); te = ~tr
        ba = {k: probe(Z, tg[k], tr, te, 2 if k.endswith("present") else 4) for k in ("hazard_present", "resource_present", "hazard_distance", "resource_distance")}
        wd = float((agent.world_obs_encoder[0].weight - w0).norm() / w0.norm())
        rep = agent.waking_trainer.report()
        print("seed %d alpha %.1f %-3s PR %.2f  BA hp %.3f rp %.3f hd %.3f rd %.3f (chance .50/.50/%.2f/%.2f)  |z| %.2f  wobs_d %.3f  steps %s guard %s  %.0fs"
              % (seed, alpha, arm, pr(Z), ba["hazard_present"][0], ba["resource_present"][0], ba["hazard_distance"][0], ba["resource_distance"][0],
                 ba["hazard_distance"][1], ba["resource_distance"][1], float(Z.norm(dim=1).mean()), wd,
                 rep.get("world_encoder", {}).get("steps", 0), rep.get("world_encoder", {}).get("guard", "-"), secs), flush=True)
