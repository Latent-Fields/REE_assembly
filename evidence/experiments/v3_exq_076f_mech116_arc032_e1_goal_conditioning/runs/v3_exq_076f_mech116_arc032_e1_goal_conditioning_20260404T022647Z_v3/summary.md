# V3-EXQ-076f -- MECH-116 / ARC-032 E1 Goal Conditioning 10k-step

**Status:** FAIL
**Claims:** MECH-116, ARC-032
**Seed:** 42  **Steps:** 10000  **Resource removal:** step 5000  **Checkpoint:** step 6000
**Bug fixed (076f):** config.e1.goal_dim now set to world_dim=32 for goal_conditioned condition. In 076e (and all prior iterations), E1Config.goal_dim was never set by from_dims(), so goal_input_proj was None in both conditions -- E1 was goal-agnostic in both cases.

## Conditions

- goal_unconditioned: z_goal_enabled=True, e1_goal_conditioned=False, config.e1.goal_dim=0 (goal_input_proj=None)
- goal_conditioned: z_goal_enabled=True, e1_goal_conditioned=True, config.e1.goal_dim=32 (goal_input_proj active: Linear(96, 64))

## Results

| Metric | unconditioned | conditioned |
|---|---|---|
| resource_visit_rate (pre-removal) | 0.2490 | 0.2490 |
| goal_halflife (steps post-removal) | 10000 | 10000 |
| halflife ratio | -- | 1.00 |
| peak_goal_norm | 0.3806 | 0.3793 |
| goal_norm at step 6000 | 0.0025 | 0.0024 |
| harm_rate | 0.6875 | 0.6875 |

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: halflife ratio >= 1.5x | FAIL |
| C2: resource gap >= 0.03 | FAIL |
| C3: goal_norm_conditioned > 0.05 at step 6000 | FAIL |

Criteria met: 0/3 -> **FAIL**

## Interpretation

MECH-116 / ARC-032 NOT SUPPORTED: E1 conditioning does not demonstrably extend goal persistence at 10,000-step budget. z_goal decay may dominate over E1 recurrent maintenance, or benefit signal is insufficient to establish a strong z_goal prior to removal.

## Failure Notes

- C1 FAIL: halflife ratio=1.00 < 1.5 (uncond=10000 cond=10000)
- C2 FAIL: resource_rate gap=0.0000 < 0.03
- C3 FAIL: goal_norm_conditioned_at_r1000=0.0024 <= 0.05 (E1 conditioning not maintaining detectable goal signal at step 6000)
