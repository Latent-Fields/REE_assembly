# V3-EXQ-085f -- MECH-071/112/117 Goal-Wired Navigation Fix

**Status:** FAIL
**Claims:** MECH-071, MECH-112, MECH-117, SD-012
**Decision:** retire_ree_claim
**Seeds:** [42]
**alpha_world:** 0.9  (SD-008)
**SD-010:** use_proxy_fields=True (harm_obs wired)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**Curriculum:** first 0 episodes place resource near spawn
**Warmup:** 1 eps (random actions, same for both conditions)
**Eval:** 1 eps (GOAL_PRESENT: E2-lookahead goal guidance; GOAL_ABSENT: random)
**Supersedes:** V3-EXQ-085e

## Root Cause Fix (Wiring Bug)

EXQ-085 through 085e all shared the same bug: goal_state was maintained (seeding worked, norm=0.135) but NEVER used for action selection. Both conditions used random.randint() in eval -- a disconnected signal cannot change behavior, guaranteeing benefit_ratio=1.00.

Fix: GOAL_PRESENT eval uses _goal_guided_action() -- E2.world_forward(z_world, a) for each candidate action, goal_state.goal_proximity() scores each prediction, greedy selection. GOAL_ABSENT still random. Same training for both.

## New Diagnostics

**goal_resource_correlation (Pearson r):** 0.000
  > 0.2: z_goal points toward resources (directionally consistent seeding)
  < 0.2: z_goal seeded but not pointing toward resources (seeding quality fail)

**goal_vs_harm_cost_ratio:** 0.000
  MECH-124 V4 risk: < 0.3 = z_goal salience not competitive with harm.

## Pre-Registered Thresholds

C1: z_goal_norm > 0.1 (goal seeded -- same as 085e)
C2: benefit_goal_present > benefit_goal_absent * 1.3
C3: calibration_gap_goal_present > 0.02
C4: no fatal errors

## Results

| Condition | benefit/ep | z_goal_norm | cal_gap | goal_resource_r | goal_vs_harm |
|-----------|-----------|-------------|--------|----------------|-------------|
| GOAL_PRESENT | 0.000 | 0.000 | 0.0000 | 0.000 | 0.000 |
| GOAL_ABSENT  | 0.000 | -- | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.00x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm > 0.1 | FAIL | 0.000 |
| C2: benefit ratio >= 1.3x | FAIL | 0.00x |
| C3: cal_gap > 0.02 | FAIL | 0.0000 |
| C4: no fatal errors | PASS | -- |

Criteria met: 1/4 -> **FAIL**

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.000 z_goal_norm=0.000 cal_gap=0.0000 goal_resource_r=0.000 goal_vs_harm=0.000

GOAL_ABSENT:
  seed=42: benefit/ep=0.000 resource_events=0

## Failure Notes

- C1 FAIL: z_goal_norm=0.000 <= 0.1 (goal not seeded -- check drive_level is non-zero)
- C2 FAIL: benefit_ratio=0.00x < 1.3x (goal_present=0.000 vs goal_absent=0.000)
-   -> goal_resource_r=0.000 < 0.2: z_goal is seeded but not pointing toward resources. Seeding quality problem -- next step: warm-start z_goal init.
- C3 FAIL: calibration_gap=0.0000 <= 0.02
