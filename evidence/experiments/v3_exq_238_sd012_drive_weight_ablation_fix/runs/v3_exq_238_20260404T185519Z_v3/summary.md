# V3-EXQ-238 -- SD-012 Drive Weight Ablation Fix

**Status:** FAIL  **Criteria met:** 0/3
**Claims:** SD-012, MECH-112  **Purpose:** evidence

**Supersedes:** V3-EXQ-233 (design error: proximity_benefit_scale=0.03)

## Context

EXQ-233 failed because proximity_benefit_scale=0.03 (default) produced benefit_exposure~0.025/step, below benefit_threshold=0.1 in both conditions. This experiment uses proximity_benefit_scale=0.18 (from EXQ-189) and energy_decay=0.005 to ensure sufficient benefit_exposure for the drive modulation to produce a measurable difference between conditions.

## Conditions

- SD012_ACTIVE: drive_weight=2.0 (SD-012 on)
- SD012_ABLATED: drive_weight=0.0 (ablation baseline)

## Results by Seed

| Seed | goal_norm_active | goal_norm_ablated | corr | C1 | C2 | C3 |
|------|-----------------|------------------|------|----|----|---|
| 42 | 0.0746 | 0.0718 | 0.4982 | FAIL | FAIL | PASS |
| 7 | 0.1555 | 0.1463 | -0.7662 | PASS | FAIL | FAIL |
| 13 | 0.1417 | 0.1305 | -0.9611 | PASS | FAIL | FAIL |

## Interpretation

SD-012 NOT CONFIRMED: Causal role of drive_weight not established. Check benefit_exposure rates and energy/drive_level wiring.

## Failure Notes

- C1 FAIL: mean_z_goal_norm ACTIVE < 0.1: [0.0746, 0.1555, 0.1417]
- C2 FAIL: mean_z_goal_norm ABLATED >= 0.05: [0.0718, 0.1463, 0.1305]
- C3 FAIL: benefit_goal_corr ACTIVE < 0.2: [0.4982, -0.7662, -0.9611]
