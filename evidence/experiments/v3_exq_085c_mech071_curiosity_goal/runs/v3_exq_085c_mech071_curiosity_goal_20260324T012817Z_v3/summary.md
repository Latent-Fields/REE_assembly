# V3-EXQ-085c -- MECH-071 / INV-034 Curiosity + Goal Calibration

**Status:** FAIL
**Claims:** MECH-071, INV-034
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**novelty_bonus_weight:** 0.1  (MECH-111)
**SD-010:** use_proxy_fields=True (harm_obs wired)
**Warmup:** 500 eps  **Eval:** 100 eps
**Root cause fix:** Circular seeding broken via MECH-111 curiosity. Metric redesigned: benefit acquisition rate (not harm event count).

## Pre-Registered Thresholds

C1: z_goal_norm > 0.1 (goal seeded via exploration)
C2: benefit_goal_present > benefit_goal_absent * 1.3
C3: calibration_gap_goal_present > 0.02
C4: no fatal errors

## Results

| Condition | benefit/ep | z_goal_norm | cal_gap |
|-----------|-----------|-------------|--------|
| GOAL_PRESENT | 0.405 | 0.000 | 0.1767 |
| GOAL_ABSENT  | 0.405 | -- | -- |

**Benefit ratio (goal/no-goal): 1.00x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm > 0.1 | FAIL | 0.000 |
| C2: benefit ratio >= 1.3x | FAIL | 1.00x |
| C3: cal_gap > 0.02 | PASS | 0.1767 |
| C4: no fatal errors | PASS | -- |

Criteria met: 2/4 -> **FAIL**

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.420 z_goal_norm=0.000 cal_gap=0.2474 resource_events=203
  seed=7: benefit/ep=0.390 z_goal_norm=0.000 cal_gap=0.1060 resource_events=201

GOAL_ABSENT:
  seed=42: benefit/ep=0.420 resource_events=203
  seed=7: benefit/ep=0.390 resource_events=201

## Failure Notes

- C1 FAIL: z_goal_norm=0.000 <= 0.1 (goal never seeded -- curiosity insufficient to encounter benefit)
- C2 FAIL: benefit_ratio=1.00x < 1.3x (goal_present=0.405 vs goal_absent=0.405)
