# V3-EXQ-085 -- MECH-071 Goal-Directed Harm Calibration

**Status:** FAIL
**Claims:** MECH-071, INV-034
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 300 eps  **Eval:** 50 eps
**Design note:** EXQ-079 redesign -- z_goal substrate enables agent-caused events.

## Pre-Registered Thresholds

C1: n_agent_events_goal_present >= 15
C2: calibration_gap_goal_present > 0.02
C3: n_agent_events_goal_present > n_agent_events_goal_absent * 1.5
C4: no fatal errors

## Results

| Condition | n_agent_events | calibration_gap_agent |
|-----------|---------------|----------------------|
| GOAL_PRESENT | 889.5 | 0.1537 |
| GOAL_ABSENT  | 889.5 | 0.1537 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: n_agent_goal >= 15 | PASS | 889.5 |
| C2: cal_gap_agent > 0.02 | PASS | 0.1537 |
| C3: goal > base * 1.5 | FAIL | 889.5 vs 889.5 |
| C4: no fatal errors | PASS | -- |

Criteria met: 3/4 -> **FAIL**

## Per-Seed

GOAL_PRESENT:
  seed=42: n_agent=907 cal_gap=0.1673 train_agent=5389
  seed=7: n_agent=872 cal_gap=0.1402 train_agent=5479

GOAL_ABSENT:
  seed=42: n_agent=907 cal_gap=0.1673
  seed=7: n_agent=872 cal_gap=0.1402

## Failure Notes

- C3 FAIL: goal=889.5 not > base=889.5 * 1.5 (goal condition not reliably increasing agent events)
