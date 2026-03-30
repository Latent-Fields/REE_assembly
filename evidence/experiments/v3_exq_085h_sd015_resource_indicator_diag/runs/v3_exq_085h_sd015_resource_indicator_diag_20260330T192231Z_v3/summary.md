# V3-EXQ-085h -- SD-015 Resource Indicator Diagnostic

**Status:** FAIL
**Claims:** SD-015, SD-012, MECH-112
**Decision:** retire_ree_claim
**Seeds:** [42, 7, 13]
**Supersedes:** V3-EXQ-085g

## Diagnostic Design

Tests SD-015 hypothesis: resource_field_view (5x5 proximity grid) provides a better goal representation than z_world at resource contact. ResourceForwardModel (RFM) trained during warmup to predict resource_field_view_next given (resource_field_view_curr, action). TWO goal states maintained: z_world-seeded (085g baseline) and resource_field_view-seeded (SD-015). KEY DIAGNOSTIC: goal_resource_r_rfm > 0.2.

**alpha_world:** 0.9  (SD-008)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**RFM lr:** 0.0005
**rfm_final_loss (avg):** 0.0078
**Warmup:** 600 eps (curriculum=100 eps)
**Eval:** 100 eps (GOAL_PRESENT: RFM-lookahead goal guidance; GOAL_ABSENT: random)

## Key Diagnostic Comparison

| Representation | goal_resource_r | Note |
|---|---|---|
| z_world-seeded (085g) | -0.010 | expected ~0.066 |
| resource_field_view-seeded (SD-015) | -0.169 | DIAGNOSTIC: need > 0.2 |

z_goal_norm_world: 0.381  z_goal_norm_resource: 2.704

## Navigation Results

| Condition | benefit/ep | z_goal_norm_res | cal_gap | r_rfm | r_world |
|---|---|---|---|---|---|
| GOAL_PRESENT | 0.407 | 2.704 | 0.0486 | -0.169 | -0.010 |
| GOAL_ABSENT  | 0.633 | -- | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.64x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm_resource > 0.1 | PASS | 2.704 |
| C2: benefit ratio >= 1.3x | FAIL | 0.64x |
| C3: goal_resource_r_rfm > 0.2 | FAIL | -0.169 |
| C4: no fatal errors | PASS | -- |

Criteria met: 2/4 -> **FAIL**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 1.212 (< 0.3 = V4 risk)

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.530 z_goal_norm_res=2.464 r_rfm=-0.503 r_world=-0.024 rfm_loss=0.0073
  seed=7: benefit/ep=0.280 z_goal_norm_res=2.775 r_rfm=-0.227 r_world=-0.062 rfm_loss=0.0075
  seed=13: benefit/ep=0.410 z_goal_norm_res=2.872 r_rfm=0.223 r_world=0.057 rfm_loss=0.0085

GOAL_ABSENT:
  seed=42: benefit/ep=0.790
  seed=7: benefit/ep=0.560
  seed=13: benefit/ep=0.550

## Failure Notes

- C2 FAIL: benefit_ratio=0.64x < 1.3x (goal_present=0.407 vs goal_absent=0.633)
- C3 FAIL: goal_resource_r_rfm=-0.169 < 0.2 despite rfm_loss=0.0078. Deeper problem: resource_field_view itself may not be useful for goal. Check: does CausalGridWorldV2 provide adequate resource_field_view variation? Are resources respawning as expected?
- UNEXPECTED: z_world goal (085g approach) OUTPERFORMS resource_field_view. SD-015 hypothesis may be wrong. Investigate env dynamics.
