# V3-EXQ-185 -- Direct Proximity Argmax Navigation

**Status:** FAIL
**Claims:** MECH-112, SD-015
**Decision:** hybridize
**Seeds:** [42, 7, 13]

## Design

Direct proximity maximization: no z_goal, no cosine_sim.
action = argmax_a enc.predict_proximity(RFM(rf_curr, a))
Pick action whose predicted next-step resource_field_view has
highest predicted proximity.

Key difference from 085l: 085l uses cosine_sim to z_goal snapshot
(fails because z_goal is scene-specific noise per EXQ-179).
EXQ-185 bypasses z_goal entirely.

**alpha_world:** 0.9  (SD-008)
**lr_enc:** 0.001  **lr_rfm:** 0.0005  **lr:** 0.0001
**enc_final_loss (avg):** 0.0009
**rfm_final_loss (avg):** 0.0056
**prox_r2 (avg):** 0.921
**rfm_prox_discrimination (avg):** 0.0540
**Warmup:** 800 eps (curriculum=100 eps)
**Eval:** 100 eps (GOAL_PRESENT: direct prox argmax; GOAL_ABSENT: random)

## Navigation Results

| Condition | benefit/ep | harm/ep |
|---|---|---|
| GOAL_PRESENT | 0.213 | 1.119 |
| GOAL_ABSENT  | 1.007 | 1.307 |

**Benefit ratio (goal/no-goal): 0.21x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: benefit_ratio >= 1.3x | FAIL | 0.21x |
| C2: rfm_prox_disc > 0.05 | PASS | 0.0540 |
| C3: prox_r2 > 0.3 | PASS | 0.921 |
| C4: rfm_loss < 0.02 | PASS | 0.0056 |

Criteria met: 3/4 -- **FAIL**

## Interpretation

If PASS: The ProximityEncoder + RFM pipeline can drive resource
navigation WITHOUT z_goal or cosine_sim. The bottleneck in 085l
was the z_goal mechanism, not the learned representations.

If C1 FAIL + C2 PASS: RFM produces differentiated predictions
but the proximity gradient does not translate to resource collection.
Possible cause: proximity gradient points toward resources but
agent encounters hazards en route, or resources respawn elsewhere.

If C2 FAIL: RFM does not differentiate actions -- forward model
is too coarse for 1-step proximity changes, or the 5x5 rf view
is too local to show action-specific differences.

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.080 harm/ep=1.165 prox_r2=0.923 rfm_loss=0.0050 rfm_prox_disc=0.0552
  seed=7: benefit/ep=0.240 harm/ep=1.019 prox_r2=0.916 rfm_loss=0.0060 rfm_prox_disc=0.0804
  seed=13: benefit/ep=0.320 harm/ep=1.174 prox_r2=0.922 rfm_loss=0.0058 rfm_prox_disc=0.0264

GOAL_ABSENT:
  seed=42: benefit/ep=1.010 harm/ep=1.295
  seed=7: benefit/ep=0.990 harm/ep=1.310
  seed=13: benefit/ep=1.020 harm/ep=1.314

## Failure Notes

- C1 FAIL: benefit_ratio=0.21x < 1.3x. present=0.213 vs absent=1.007. Direct proximity argmax does not produce 30% benefit improvement. If RFM predictions barely differ across actions (C2 fail too), RFM is not learning action-specific predictions. If C2 passes but C1 fails, proximity gradient exists but does not lead to resource collection -- env layout or harm dominance.
