# V3-EXQ-085g -- MECH-071/112/117 Contact-Gated Goal Seeding

**Status:** FAIL
**Claims:** MECH-071, MECH-112, MECH-117, SD-012
**Decision:** retire_ree_claim
**Seeds:** [42, 7, 13]
**alpha_world:** 0.9  (SD-008)
**alpha_goal:** 0.3  (raised from 0.1 -- faster convergence per contact event)
**SD-010:** use_proxy_fields=True (harm_obs wired)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**Curriculum:** first 100 episodes place resource near spawn
**Warmup:** 500 eps (random actions, same for both conditions)
**Eval:** 100 eps (GOAL_PRESENT: E2-lookahead goal guidance; GOAL_ABSENT: random)
**Supersedes:** V3-EXQ-085f

## Root Cause Fix (Seeding Quality)

EXQ-085f had z_goal_norm=0.228 (seeded) but benefit_ratio=0.28x (goal guidance WORSE than random). Diagnostic: goal_resource_r=0.087 -- z_goal seeded to random z_world states from noisy proximity signal, not resource-specific representations.

Fix: PRIMARY seeding now triggered only on actual resource contact events (ttype=='resource'), using benefit_exposure=1.0 to force threshold crossing. This anchors z_goal to z_world observed at the moment of resource acquisition. Proximity seeding retained as secondary (prevents decay between contacts).

avg_resource_seedings_warmup: 382

## MECH-124 Diagnostics

**goal_resource_correlation (Pearson r):** 0.066
  > 0.2: z_goal points toward resources (contact-gated seeding working)
  < 0.2: z_world at contact too noisy -- need dedicated z_resource

**goal_vs_harm_cost_ratio:** 2.249
  MECH-124 V4 risk: < 0.3 = z_goal salience not competitive with harm.

## Pre-Registered Thresholds

C1: z_goal_norm > 0.1 (goal seeded)
C2: benefit_goal_present > benefit_goal_absent * 1.3
C3: calibration_gap_goal_present > 0.02
C4: no fatal errors

## Results

| Condition | benefit/ep | z_goal_norm | cal_gap | goal_resource_r | goal_vs_harm |
|-----------|-----------|-------------|--------|----------------|-------------|
| GOAL_PRESENT | 0.237 | 0.399 | 0.2181 | 0.066 | 2.249 |
| GOAL_ABSENT  | 0.637 | -- | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.37x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm > 0.1 | PASS | 0.399 |
| C2: benefit ratio >= 1.3x | FAIL | 0.37x |
| C3: cal_gap > 0.02 | PASS | 0.2181 |
| C4: no fatal errors | PASS | -- |

Criteria met: 3/4 -> **FAIL**

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.310 z_goal_norm=0.377 n_resource_seedings=393 cal_gap=0.2321 goal_resource_r=0.070 goal_vs_harm=2.466
  seed=7: benefit/ep=0.210 z_goal_norm=0.421 n_resource_seedings=375 cal_gap=0.3238 goal_resource_r=0.028 goal_vs_harm=1.906
  seed=13: benefit/ep=0.190 z_goal_norm=0.400 n_resource_seedings=379 cal_gap=0.0984 goal_resource_r=0.101 goal_vs_harm=2.374

GOAL_ABSENT:
  seed=42: benefit/ep=0.620 resource_events=393
  seed=7: benefit/ep=0.700 resource_events=375
  seed=13: benefit/ep=0.590 resource_events=379

## Failure Notes

- C2 FAIL: benefit_ratio=0.37x < 1.3x (goal_present=0.237 vs goal_absent=0.637)
-   -> goal_resource_r=0.066 < 0.2: z_goal still not pointing toward resources despite contact-gated seeding. z_world at resource contact may be too noisy/low-dimensional to encode location. Next step: dedicated z_resource representation.
