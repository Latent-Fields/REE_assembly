# V3-EXQ-085i -- SD-015 Contact-Only Seeding Fix

**Status:** FAIL
**Claims:** SD-015, SD-012, MECH-112
**Decision:** hybridize
**Seeds:** [42, 7, 13]
**Supersedes:** V3-EXQ-085h

## Diagnostic Design

Fixes 085h secondary seeding contamination. 085h: z_goal_resource seeded from both contact events AND any near-resource step (secondary path), producing z_goal_norm~2.7 and goal_resource_r=-0.169 (seeds 42/7). Seed 13 (contact-dominated) achieved r=+0.223. Fix: z_goal_resource updated ONLY on resource contact (ttype=='resource'). z_goal_world retains secondary seeding. alpha_goal_resource raised 0.3->0.5 to compensate for reduced update frequency.

**alpha_world:** 0.9  (SD-008)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**RFM lr:** 0.0005
**rfm_final_loss (avg):** 0.0078
**Warmup:** 600 eps (curriculum=100 eps)
**Eval:** 100 eps (GOAL_PRESENT: RFM-lookahead goal guidance; GOAL_ABSENT: random)

## Key Diagnostic Comparison

| Representation | goal_resource_r | Note |
|---|---|---|
| z_world-seeded (085g) | -0.038 | expected ~0.066 |
| resource_field_view-seeded (SD-015) | 0.218 | DIAGNOSTIC: need > 0.2 |

z_goal_norm_world: 0.381  z_goal_norm_resource: 3.396

## Navigation Results

| Condition | benefit/ep | z_goal_norm_res | cal_gap | r_rfm | r_world |
|---|---|---|---|---|---|
| GOAL_PRESENT | 0.650 | 3.396 | -0.0387 | 0.218 | -0.038 |
| GOAL_ABSENT  | 0.633 | -- | -- | -- | -- |

**Benefit ratio (goal/no-goal): 1.03x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm_resource > 0.1 | PASS | 3.396 |
| C2: benefit ratio >= 1.3x | FAIL | 1.03x |
| C3: goal_resource_r_rfm > 0.2 | PASS | 0.218 |
| C4: no fatal errors | PASS | -- |

Criteria met: 3/4 -> **FAIL**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 0.963 (< 0.3 = V4 risk)

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.640 z_goal_norm_res=3.308 r_rfm=0.243 r_world=-0.087 rfm_loss=0.0073
  seed=7: benefit/ep=0.800 z_goal_norm_res=3.728 r_rfm=0.297 r_world=-0.134 rfm_loss=0.0075
  seed=13: benefit/ep=0.510 z_goal_norm_res=3.154 r_rfm=0.113 r_world=0.106 rfm_loss=0.0085

GOAL_ABSENT:
  seed=42: benefit/ep=0.790
  seed=7: benefit/ep=0.560
  seed=13: benefit/ep=0.550

## Failure Notes

- C2 FAIL: benefit_ratio=1.03x < 1.3x BUT C3 PASS (goal_resource_r_rfm=0.218 > 0.2). SD-015 representation confirmed. RFM insufficient for navigation. Next: full ResourceEncoder + E2_resource forward model (EXQ-085j).
