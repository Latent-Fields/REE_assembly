# V3-EXQ-238 -- SD-012 Drive Weight Ablation Fix

**Status:** FAIL  **Criteria met:** 2/3
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
| 42 | 0.1834 | 0.1757 | 0.2089 | PASS | FAIL | PASS |
| 7 | 0.2545 | 0.2450 | 0.2387 | PASS | FAIL | PASS |
| 13 | 0.2633 | 0.2510 | 0.3611 | PASS | FAIL | PASS |

## Interpretation

SD-012 PARTIAL: Some criteria met but not all. Drive modulation may be partially causal.

## Failure Notes

- C2 FAIL: mean_z_goal_norm ABLATED >= 0.05: [0.1757, 0.245, 0.251]
