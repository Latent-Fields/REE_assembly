# V3-EXQ-085l -- SD-015 Proximity Regression Encoder

**Status:** FAIL
**Claims:** SD-015, SD-012, MECH-112
**Decision:** hybridize
**Seeds:** [42, 7, 13]
**Supersedes:** V3-EXQ-085k

## Architecture

ProximityEncoder (25->16) trained via MSE regression on resource_proximity = 1/(1+manhattan_dist). Replaces binary contact BCE (085j/k).

**Rationale:** Binary BCE (085j/k) trained encoder to separate contact (is_contact=1) from everything else. Near-resource steps labelled 0 -- encoder didn't distinguish near-resource from far-resource. Proximity regression forces smooth graded z_resource: high near resources, low far away. cosine_sim(z_resource_current, z_goal) now a smooth resource-proximity gradient for action selection.

Action selection: cosine_sim(enc.encode(RFM(rf,a)), z_goal) -- same as 085k.

**alpha_world:** 0.9  (SD-008)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**lr_enc:** 0.001  **lr_rfm:** 0.0005
**enc_final_loss (avg):** 0.0011
**rfm_final_loss (avg):** 0.0076
**prox_r2 (avg):** 0.908
**Warmup:** 800 eps (curriculum=100 eps)
**Eval:** 100 eps (GOAL_PRESENT: RFM+enc hybrid; GOAL_ABSENT: random)

## Diagnostic Series Summary

| Variant | Enc type | goal_r | benefit_ratio | Note |
|---|---|---|---|---|
| 085i | raw rf (no enc) | 0.218 | 1.03x | spatially specific |
| 085j | BCE contact enc | 0.819 | 0.034x | E2Resource degenerate |
| 085k | BCE contact enc + RFM | 0.582 | 0.977x | near-random action selection |
| 085l | Prox regression enc + RFM | 0.869 | 0.42x | this run |

## Navigation Results

| Condition | benefit/ep | z_goal_norm_enc | r_enc | prox_r2 |
|---|---|---|---|---|
| GOAL_PRESENT | 0.270 | 0.731 | 0.869 | 0.908 |
| GOAL_ABSENT  | 0.643 | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.42x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm_enc > 0.1 | PASS | 0.731 |
| C2: benefit ratio >= 1.3x | FAIL | 0.42x |
| C3: goal_resource_r_enc > 0.2 | PASS | 0.869 |
| C4: prox_r2 > 0.3 | PASS | 0.908 |

Criteria met: 3/4 -> **FAIL**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 1.647 (< 0.3 = V4 risk)

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.130 z_goal_norm_enc=0.501 r_enc=0.882 prox_r2=0.892 rfm_loss=0.0075
  seed=7: benefit/ep=0.480 z_goal_norm_enc=0.921 r_enc=0.818 prox_r2=0.912 rfm_loss=0.0070
  seed=13: benefit/ep=0.200 z_goal_norm_enc=0.770 r_enc=0.908 prox_r2=0.919 rfm_loss=0.0083

GOAL_ABSENT:
  seed=42: benefit/ep=0.680
  seed=7: benefit/ep=0.730
  seed=13: benefit/ep=0.520

## Failure Notes

- C2 FAIL: benefit_ratio=0.42x < 1.3x BUT C3 PASS (r=0.869). Proximity regression gives graded representation but nav gap remains. Consider: more eval eps, stronger goal bias in action selection, or wiring z_goal into REEAgent action scoring directly.
