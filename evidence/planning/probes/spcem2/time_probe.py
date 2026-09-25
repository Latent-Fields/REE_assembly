"""Timing probe (bt0925-spcem2): measure per-step warmup cost at world_dim=self_dim=32
so the full V3-EXQ-1061 warmup schedule (600 eps x 200 steps) can be budgeted against
the ~25 min Mac wall-clock cap per seed. Read-only: monkeypatches the driver module's
SELF_DIM/WORLD_DIM constants in this process only (no file edits).
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.environ.get("REE_V3_WT", os.path.join(HERE, "ree-v3-wt"))
sys.path.insert(0, WT)
sys.path.insert(0, os.path.join(WT, "experiments"))

import torch  # noqa: E402
torch.set_num_threads(2)

import v3_exq_1061_mech131_anticipatory_residue_lesion as X  # noqa: E402

X.SELF_DIM = 32
X.WORLD_DIM = 32

seed = 11
t0 = time.time()
agent, env, cfg = X.build_agent(True, True, seed, X.PRODUCTION_FLOOR)
t_build = time.time() - t0
assert cfg.hippocampal.self_dim if hasattr(cfg.hippocampal, "self_dim") else True

n_eps, n_steps = 5, 200
t1 = time.time()
warm = X.warmup_train(agent, env, seed, n_eps, n_steps)
t_warm = time.time() - t1

print("build_seconds", round(t_build, 2))
print("warm_seconds_for_%d_eps_x_%d_steps" % (n_eps, n_steps), round(t_warm, 2))
per_step = t_warm / (n_eps * n_steps)
print("per_step_seconds", round(per_step, 5))
full = 600 * 200 * per_step
print("estimated_full_1061_warmup_seconds", round(full, 1), "=", round(full / 60, 1), "min")
