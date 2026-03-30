# V3-EXQ-085o -- SD-015 Sorted-RF Proximity Encoder

**Status:** FAIL
**Claims:** SD-015, SD-012, MECH-112
**Decision:** hybridize
**Seeds:** [42, 7, 13]
**Supersedes:** V3-EXQ-085l

## Architecture

ProximityEncoder input: sorted_rf = rf.sort(descending=True) -- position-FREE.

**085l root cause:** proximity regression MSE trains 1-dim proximity_head direction; remaining 15 dims of z_resource freely encode spatial position (which cell the resource occupies). After respawn, 15-dim position mismatch in cosine_sim overrides 1-dim proximity signal -- agent steered to old resource location. All seeds below 1.0x (harmful guidance).

**Fix:** sorting rf removes all spatial position information. All contacts at any cell produce identical sorted_rf profile ([1.0, 0.7, ...]). All 16 encoder dims encode proximity order statistics. z_goal is position-invariant. cosine_sim purely proximity-based.

Action selection: cosine_sim(enc.encode(sort(RFM(rf,a))), z_goal).
RFM still operates on raw rf for accurate spatial dynamics.

**alpha_world:** 0.9  (SD-008)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**lr_enc:** 0.001  **lr_rfm:** 0.0005
**enc_final_loss:** 0.0056
**rfm_final_loss:** 0.0076
**prox_r2:** 0.524
**Warmup:** 800 eps (curriculum=100 eps)
**Eval:** 100 eps (GOAL_PRESENT: sorted-RF+enc hybrid; GOAL_ABSENT: random)

## Diagnostic Series Summary

| Variant | Enc input | goal_r | benefit_ratio | Note |
|---|---|---|---|---|
| 085i | raw rf (no enc) | 0.218 | 1.03x | spatially specific |
| 085j | BCE contact, raw rf | 0.819 | 0.034x | E2Resource degenerate |
| 085k | BCE contact, raw rf + RFM | 0.582 | 0.977x | binary enc near-random |
| 085l | prox regression, raw rf + RFM | 0.869 | 0.42x | 15-dim position noise |
| 085m | prox regression, sorted rf + RFM | 0.574 | 0.11x | this run |

## Navigation Results

| Condition | benefit/ep | z_goal_norm_enc | r_enc | prox_r2 |
|---|---|---|---|---|
| GOAL_PRESENT | 0.073 | 0.617 | 0.574 | 0.524 |
| GOAL_ABSENT  | 0.643 | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.11x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm_enc > 0.1 | PASS | 0.617 |
| C2: benefit ratio >= 1.3x | FAIL | 0.11x |
| C3: goal_resource_r_enc > 0.2 | PASS | 0.574 |
| C4: prox_r2 > 0.3 | PASS | 0.524 |

Criteria met: 3/4 -> **FAIL**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 2.346 (< 0.3 = V4 risk)

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.100 z_goal_norm_enc=0.234 r_enc=0.409 prox_r2=0.499 rfm_loss=0.0075
  seed=7: benefit/ep=0.080 z_goal_norm_enc=1.004 r_enc=0.754 prox_r2=0.573 rfm_loss=0.0070
  seed=13: benefit/ep=0.040 z_goal_norm_enc=0.613 r_enc=0.558 prox_r2=0.499 rfm_loss=0.0083

GOAL_ABSENT:
  seed=42: benefit/ep=0.680
  seed=7: benefit/ep=0.730
  seed=13: benefit/ep=0.520

## Failure Notes

- C2 FAIL: benefit_ratio=0.11x < 1.3x BUT C3 PASS (r=0.574). Sorted-rf enc goal tracks proximity but nav gap persists. If ratio > 0.9: proximity guidance nearly working, consider stronger action bias or more eval episodes. If ratio < 0.5: likely residual position-specificity. Next: direct predict_proximity action selection (no cosine_sim).
