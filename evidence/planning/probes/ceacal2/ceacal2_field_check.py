"""Pre-registration field-floor/ceiling check (bt0925-ceacal2). Read-only, no agent.
usage: cd <ree-v3 worktree>; python ceacal2_field_check.py
Instantiates CausalGridWorldV2 with candidate (num_hazards, hazard_field_decay) pairs
on the EXP-0787 size=10 grid, over 5 seeds each, and reports hazard_field floor/ceiling
+ adjacent-vs-far separation so the non-saturated config is picked from measurement,
not assumed. No torch model construction; only env.reset().
"""
import sys, json
root = "."
sys.path.insert(0, root)
import numpy as np
from ree_core.environment.causal_grid_world import CausalGridWorldV2

CANDIDATES = [
    ("baseline_nh3_d0.5", dict(num_hazards=3, hazard_field_decay=0.5)),
    ("nh3_d2.0", dict(num_hazards=3, hazard_field_decay=2.0)),
    ("nh1_d0.5", dict(num_hazards=1, hazard_field_decay=0.5)),
    ("nh1_d2.0", dict(num_hazards=1, hazard_field_decay=2.0)),
]
SEEDS = [21, 22, 23, 24, 25]
out = {}
for name, kw in CANDIDATES:
    rows = []
    for s in SEEDS:
        env = CausalGridWorldV2(seed=s, size=10, num_resources=3, harm_history_len=10, **kw)
        env.reset()
        HF = env.hazard_field
        # Manhattan distance-to-nearest-hazard per cell, for adjacency split
        size = env.size
        DM = np.full((size, size), 99, dtype=np.int32)
        for hx, hy in env.hazards:
            for i in range(size):
                for j in range(size):
                    d = abs(i - hx) + abs(j - hy)
                    if d < DM[i, j]:
                        DM[i, j] = d
        adj = DM <= 1
        far = DM >= 2
        rows.append(dict(
            floor=float(HF.min()), ceiling=float(HF.max()),
            mean_all=float(HF.mean()),
            frac_ge_0p15=float((HF >= 0.15).mean()),
            frac_ge_0p5=float((HF >= 0.5).mean()),
            mean_adj=float(HF[adj].mean()) if adj.any() else None,
            mean_far=float(HF[far].mean()) if far.any() else None,
            n_far=int(far.sum()), n_adj=int(adj.sum()),
        ))
    agg = dict(
        floor_mean=round(float(np.mean([r["floor"] for r in rows])), 4),
        ceiling_mean=round(float(np.mean([r["ceiling"] for r in rows])), 4),
        mean_all_mean=round(float(np.mean([r["mean_all"] for r in rows])), 4),
        frac_ge_0p15_mean=round(float(np.mean([r["frac_ge_0p15"] for r in rows])), 4),
        frac_ge_0p5_mean=round(float(np.mean([r["frac_ge_0p5"] for r in rows])), 4),
        mean_adj_mean=round(float(np.mean([r["mean_adj"] for r in rows if r["mean_adj"] is not None])), 4),
        mean_far_mean=round(float(np.mean([r["mean_far"] for r in rows if r["mean_far"] is not None])), 4),
    )
    out[name] = dict(per_seed=rows, agg=agg)
print(json.dumps(out, indent=1))
