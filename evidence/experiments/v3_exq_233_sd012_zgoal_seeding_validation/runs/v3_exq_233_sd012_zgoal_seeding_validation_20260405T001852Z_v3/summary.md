# V3-EXQ-233 -- SD-012 z_goal Seeding Causal Validation

**Status:** FAIL  **Criteria met:** 0/3
**Claims:** SD-012, MECH-112  **Purpose:** evidence

## Context

SD-012 implemented drive_weight=2.0 (GoalConfig default). EXQ-189 showed z_goal_norm=0.30 confirming the fix works. This experiment provides clean ablation confirming drive_weight is causal.

## Conditions

- SD012_ACTIVE: drive_weight=2.0 (SD-012 on)
- SD012_ABLATED: drive_weight=0.0 (ablation baseline)

## Results by Seed

| Seed | goal_norm_active | goal_norm_ablated | corr | C1 | C2 | C3 |
|------|-----------------|------------------|------|----|----|---|
| 42 | 0.0580 | 0.0442 | -0.0522 | FAIL | PASS | FAIL |
| 7 | 0.0787 | 0.0609 | 0.0618 | FAIL | FAIL | FAIL |
| 13 | 0.0234 | 0.0172 | 0.1765 | FAIL | PASS | FAIL |

## Interpretation

SD-012 NOT CONFIRMED: Causal role of drive_weight not established. Check benefit_exposure rates and energy/drive_level wiring.

## Failure Notes

- C1 FAIL: mean_z_goal_norm ACTIVE < 0.1: [0.058, 0.0787, 0.0234]
- C2 FAIL: mean_z_goal_norm ABLATED >= 0.05: [0.0442, 0.0609, 0.0172]
- C3 FAIL: benefit_goal_corr ACTIVE < 0.2: [-0.0522, 0.0618, 0.1765]
