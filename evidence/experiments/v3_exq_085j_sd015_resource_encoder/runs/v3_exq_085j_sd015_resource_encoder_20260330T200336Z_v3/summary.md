# V3-EXQ-085j -- SD-015 ResourceEncoder with Spatial Invariance

**Status:** FAIL
**Claims:** SD-015, SD-012, MECH-112
**Decision:** hybridize
**Seeds:** [42, 7, 13]
**Supersedes:** V3-EXQ-085i

## Architecture

ResourceEncoder (25->16) trained with contact prediction BCE for spatial invariance. E2Resource (16+5->64->64->16) forward model in encoded space. z_goal seeded from enc.encode(rf) at contact events only. Action selection: E2Resource lookahead maximising cosine_sim to z_goal.

**SD-015 fix vs 085i:** 085i used raw resource_field_view (25-dim) for z_goal -- spatially specific, so resource respawn to new grid position broke goal tracking (2/3 seeds goal harmful). ResourceEncoder learns position-invariant features via contact prediction BCE.

**alpha_world:** 0.9  (SD-008)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**lr_enc:** 0.001  **lr_e2r:** 0.0005
**enc_final_loss (avg):** 0.2258
**e2r_final_loss (avg):** 0.0414
**enc_contact_acc (avg):** 0.927
**Warmup:** 800 eps (curriculum=100 eps)
**Eval:** 100 eps (GOAL_PRESENT: E2Resource-lookahead; GOAL_ABSENT: random)

## Key Diagnostic Comparison

| Representation | goal_resource_r | Note |
|---|---|---|
| z_world-seeded (085g) | 0.232 | baseline ~0.066 |
| enc-seeded (085i raw rf) | ~0.218 | 085i result |
| ResourceEncoder-seeded (085j) | 0.819 | need > 0.2 |

z_goal_norm_world: 0.386  z_goal_norm_enc: 1.173

## Navigation Results

| Condition | benefit/ep | z_goal_norm_enc | cal_gap | r_enc |
|---|---|---|---|---|
| GOAL_PRESENT | 0.020 | 1.173 | 0.3531 | 0.819 |
| GOAL_ABSENT  | 0.587 | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.03x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm_enc > 0.1 | PASS | 1.173 |
| C2: benefit ratio >= 1.3x | FAIL | 0.03x |
| C3: goal_resource_r_enc > 0.2 | PASS | 0.819 |
| C4: enc_contact_acc > 0.7 | PASS | 0.927 |

Criteria met: 3/4 -> **FAIL**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 0.605 (< 0.3 = V4 risk)

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.060 z_goal_norm_enc=0.976 r_enc=0.811 r_world=-0.026 enc_acc=0.898 enc_loss=0.2298 e2r_loss=0.0507
  seed=7: benefit/ep=0.000 z_goal_norm_enc=1.366 r_enc=0.848 r_world=0.684 enc_acc=0.953 enc_loss=0.2324 e2r_loss=0.0229
  seed=13: benefit/ep=0.000 z_goal_norm_enc=1.176 r_enc=0.799 r_world=0.037 enc_acc=0.930 enc_loss=0.2154 e2r_loss=0.0506

GOAL_ABSENT:
  seed=42: benefit/ep=0.500
  seed=7: benefit/ep=0.650
  seed=13: benefit/ep=0.610

## Failure Notes

- C2 FAIL: benefit_ratio=0.03x < 1.3x BUT C3 PASS (goal_resource_r_enc=0.819 > 0.2). Goal representation works; navigation gap. Check action selection / nav_bias strength. Consider stronger lookahead or more eval eps.
