"""U4: root-cause the occasional near-collapsed single-tick ||z_world|| and the
low PR at alpha_world 0.3 (bt0926-u4, chip chip-20260926-zworld-near-collapse-rootcause).

For each seed x alpha_world in {0.3, 0.9, 1.0}: build a fresh UNTRAINED REEAgent
(deployed dims world_dim=self_dim=32) and drive it with its OWN NATIVE action
selection (act_with_split_obs) over several episodes of a CausalGridWorldV2.
Per tick, without a second sense() call (which would double-advance the EMA),
read agent._current_latent right after act_with_split_obs -- this is the exact
LatentState act_with_split_obs's internal sense() call produced, carrying both
z_world (post-EMA) and z_world_raw (pre-EMA, pre-SD-007-reafference-correction,
alpha-independent by construction: the reafference predictor's own prev-input
prev_state.z_world_raw is likewise pre-EMA, so the raw path never depends on
alpha_world at all -- only the returned z_world does).

Per tick we record: seed, alpha, episode idx, tick-in-episode, ||z_world||,
||z_world_raw||, the environment TRIGGER that produced this tick's observation
(reset / hazard / benefit / wallpush / noop / move -- from the PRECEDING
env.step's harm_signal and the agent's position delta), and the action class
taken.

Outputs one JSON per alpha: probes/u4/results/u4_alpha_<a>.json
Usage: u4_zworld_collapse_probe.py <tree> <alpha> <n_episodes> <ep_len> <seed> [<seed>...]
"""
import sys, time, json
import numpy as np, torch

tree = sys.argv[1]
alpha = float(sys.argv[2])
n_episodes = int(sys.argv[3])
ep_len = int(sys.argv[4])
seeds = [int(s) for s in sys.argv[5:]]
sys.path.insert(0, tree)
torch.set_num_threads(2)

from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig, CAUSAL_GRID_WORLD_STAY_ACTION_CLASS

STAY = CAUSAL_GRID_WORLD_STAY_ACTION_CLASS


def make_env(seed):
    return CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=seed)


def pr(z):
    z = z - z.mean(0, keepdim=True)
    cov = (z.T @ z) / max(z.shape[0] - 1, 1)
    ev = torch.linalg.eigvalsh(cov).clamp(min=0)
    denom = float((ev ** 2).sum())
    return float(ev.sum() ** 2 / denom) if denom > 0 else float("nan")


def run_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)
    env0 = make_env(1000 * seed)
    cfg = REEConfig.from_dims(
        body_obs_dim=env0.body_obs_dim, world_obs_dim=env0.world_obs_dim,
        action_dim=env0.action_dim, self_dim=32, world_dim=32,
        alpha_world=alpha,
    )
    agent = REEAgent(cfg)
    rows = []
    ep_base = 1000 * seed
    for ep in range(n_episodes):
        env = make_env(ep_base + ep)
        _flat, od = env.reset()
        agent.reset()
        t = 0
        prev_pos = env.get_agent_position()
        trigger = "reset"
        while t < ep_len:
            with torch.no_grad():
                a = agent.act_with_split_obs(
                    torch.as_tensor(od["body_state"]).float(),
                    torch.as_tensor(od["world_state"]).float(),
                )
            lat = agent._current_latent
            zvec = lat.z_world.detach().reshape(-1)
            zw = float(zvec.norm())
            zwr = float(lat.z_world_raw.detach().norm()) if lat.z_world_raw is not None else float("nan")
            cls = int(a.detach().argmax(dim=-1).flatten()[0].item())
            rows.append(dict(
                seed=seed, ep=ep, t=t, zw=zw, zwr=zwr, trigger=trigger, cls=cls,
                z=zvec.tolist(),
            ))
            _flat, h, done, _info, od = env.step(a)
            new_pos = env.get_agent_position()
            if h < 0:
                trigger = "hazard"
            elif h > 0:
                trigger = "benefit"
            elif new_pos == prev_pos:
                trigger = "noop" if cls == STAY else "wallpush"
            else:
                trigger = "move"
            prev_pos = new_pos
            t += 1
            if done:
                break
    return rows


t0 = time.time()
all_rows = []
for s in seeds:
    all_rows.extend(run_seed(s))
secs = time.time() - t0

zw = torch.tensor([r["zw"] for r in all_rows])
zwr = torch.tensor([r["zwr"] for r in all_rows])
zmat = torch.tensor([r["z"] for r in all_rows])
n = len(all_rows)
p1 = float(torch.quantile(zw, 0.01))
p50 = float(torch.quantile(zw, 0.50))
collapse_idx = [i for i, r in enumerate(all_rows) if r["zw"] <= p1]

base_counts = {}
collapse_counts = {}
for r in all_rows:
    base_counts[r["trigger"]] = base_counts.get(r["trigger"], 0) + 1
for i in collapse_idx:
    trg = all_rows[i]["trigger"]
    collapse_counts[trg] = collapse_counts.get(trg, 0) + 1

# reset-tick exact identity check: at t==0, z_world_final == alpha * z_world_raw
reset_rows = [r for r in all_rows if r["t"] == 0]
reset_ratio = [r["zw"] / r["zwr"] for r in reset_rows if r["zwr"] > 1e-12]
reset_ratio_mean = float(np.mean(reset_ratio)) if reset_ratio else float("nan")
reset_ratio_max_abs_err = float(np.max(np.abs(np.array(reset_ratio) - alpha))) if reset_ratio else float("nan")

# among collapse ticks, is the RAW also collapsed, or only the post-EMA value?
collapse_zwr = [all_rows[i]["zwr"] for i in collapse_idx]
collapse_zwr_pctile_of_overall = None
if collapse_zwr:
    overall_sorted = sorted(r["zwr"] for r in all_rows)
    ranks = [sum(1 for v in overall_sorted if v <= x) / n for x in collapse_zwr]
    collapse_zwr_pctile_of_overall = float(np.mean(ranks))

result = dict(
    alpha=alpha, n_ticks=n, n_seeds=len(seeds), seeds=seeds,
    n_episodes=n_episodes, ep_len=ep_len,
    mean_zw=float(zw.mean()), median_zw=p50, p1_zw=p1, max_zw=float(zw.max()),
    mean_zwr=float(zwr.mean()), median_zwr=float(torch.quantile(zwr, 0.5)),
    pr_zw=pr(zmat),
    base_trigger_counts=base_counts,
    collapse_trigger_counts=collapse_counts,
    n_collapse=len(collapse_idx),
    reset_ratio_mean=reset_ratio_mean,
    reset_ratio_max_abs_err_vs_alpha=reset_ratio_max_abs_err,
    n_reset_ticks=len(reset_rows),
    collapse_zwr_mean_percentile_of_overall_zwr=collapse_zwr_pctile_of_overall,
    wall_secs=secs,
)
print(json.dumps(result, indent=2))

out_path = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/u4/results/u4_alpha_%s.json" % str(alpha).replace(".", "p")
with open(out_path, "w") as f:
    json.dump(dict(result=result, rows=all_rows), f)
print("WROTE", out_path, flush=True)
