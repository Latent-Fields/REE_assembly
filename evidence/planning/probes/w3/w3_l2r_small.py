"""Feasibility of the L2R bar on a small fixed dataset through E2WorldMember (contract sizing)."""
import sys, time, random, argparse, numpy as np, torch
sys.path.insert(0, ".")
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from experiments._lib import coupled_acceptance as CA
ap = argparse.ArgumentParser()
ap.add_argument("--seed", type=int, default=3); ap.add_argument("--nb", type=int, default=800)
ap.add_argument("--pre", type=int, default=1000); ap.add_argument("--npol", type=int, default=300)
ap.add_argument("--ups", type=int, default=6); ap.add_argument("--size", type=int, default=8)
ap.add_argument("--shuffle", action="store_true"); ap.add_argument("--noreplay", action="store_true")
ap.add_argument("--objective", default="mse"); ap.add_argument("--alpha", type=float, default=0.9)
ap.add_argument("--starts", type=int, default=150)
a = ap.parse_args()
S = a.seed
def env_(k): return CausalGridWorldV2(size=a.size, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=S * 1000 + k)
e = env_(0)
cfg = REEConfig.from_dims(body_obs_dim=e.body_obs_dim, world_obs_dim=e.world_obs_dim, action_dim=e.action_dim,
    self_dim=32, world_dim=32, alpha_world=a.alpha, waking_trainer_enabled=True, waking_trainer_e2_world_enabled=True,
    waking_trainer_e2_world_updates_per_step=0 if False else 1, waking_trainer_e2_world_objective=a.objective,
    waking_trainer_e2_world_replay_frac=0.0 if a.noreplay else 0.25, waking_trainer_guard_min_steps=8)
torch.manual_seed(S); np.random.seed(S); random.seed(S)
ag = REEAgent(cfg); ag.eval(); tr = ag.waking_trainer; m = tr.members["e2_world"]
tr.every_k = 10 ** 9   # collection only; updates driven explicitly below
from ree_core.developmental.structured_babbling import StructuredBabbler
bab = StructuredBabbler(5, 4, seed=S)
PERM = [1, 2, 3, 4, 0]
def run(n, policy, k0):
    k = k0; env = env_(k); _f, obs = env.reset(); ag.reset(); t = 0; steps = 0
    while steps < n:
        ag.sense(torch.as_tensor(obs["body_state"]).float(), torch.as_tensor(obs["world_state"]).float(),
                 obs_harm=obs.get("harm_obs"), obs_harm_a=obs.get("harm_obs_a"), obs_harm_history=obs.get("harm_history"))
        c = policy()
        ag.record_executed_action(torch.nn.functional.one_hot(torch.tensor([c]), 5).float())
        _f, h, done, _i, obs = env.step(c); t += 1; steps += 1
        ag.update_residue(float(h))
        yield steps
        if done or t >= 50:
            k += 1; env = env_(k); _f, obs = env.reset(); ag.reset(); t = 0
t0 = time.time()
tr.set_e2_world_source("babble")
for _ in run(a.nb, bab.next_class, 0): pass
if a.shuffle:
    for r in m._retained:
        c = int(r["a"].argmax()); r["a"] = torch.nn.functional.one_hot(torch.tensor([PERM[c]]), 5).float()
for _ in range(a.pre): tr._update("e2_world", m)
te = CA.collect_uniform_random_episodes(ag, env_(900), 1500, seed=S + 991)
def meas():
    return CA.action_discrimination(CA.e2_world_predictor(ag.e2), te, action_dim=5, max_starts=a.starts, seed=S, bar_disc4_h1=0.47)
pre = meas()
tr.set_e2_world_source("on_policy")
g = np.random.default_rng(S + 5); c0 = int(g.integers(0, 4))
mono = lambda: c0 if g.random() < 0.9 else int(g.integers(0, 5))
for st in run(a.npol, mono, 100):
    if len(m._on_policy) >= m.batch_size:
        for _ in range(a.ups): tr._update("e2_world", m)
post = meas()
print("seed %d shuffle=%s noreplay=%s obj=%s | pre disc4 %.3f k %d | post disc4 %.3f disc5 %.3f k %d verdict %s | ret %d onpol %d drawn r/o %d/%d | guard %s | t %.0fs" % (
    S, a.shuffle, a.noreplay, a.objective, pre["disc4_h1"], pre["k"], post["disc4_h1"], post["disc5_h1"], post["k"], post.get("verdict"),
    len(m._retained), len(m._on_policy), m.n_drawn_retained, m.n_drawn_on_policy, {k: v.status for k, v in tr.guard_results.items()}, time.time() - t0))
