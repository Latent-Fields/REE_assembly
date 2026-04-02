# V3-EXQ-182a -- SD-015 Handcrafted Goal Cue Diagnostic

**Status:** PASS
**Claims:** SD-015
**Decision:** retain_ree
**Seeds:** [42, 7, 13]

## Design

Ceiling test: oracle goal signal (1/(1+manhattan_dist_to_resource))
computed directly from env state. No learned representation.
Action selection: score(a) = -lambda_goal*prox(a) + lambda_harm*hazard(a)
GOAL_ABSENT: random action selection.

**lambda_goal:** 2.0  **lambda_harm:** 1.0
**Warmup:** 200 eps  **Eval:** 100 eps
**Steps:** 200/ep

## Results

| Condition | benefit/ep | harm/ep |
|---|---|---|
| GOAL_HANDCRAFTED | 2.190 | 1.353 |
| GOAL_ABSENT | 0.197 | 1.167 |

**Benefit ratio (handcrafted/absent): 11.14x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: benefit_ratio >= 1.3x | PASS | 11.14x |
| C2: benefit_handcrafted > 0.5 | PASS | 2.190 |

Criteria met: 2/2 -> **PASS**

## Interpretation

If PASS: The bottleneck in SD-015 goal navigation is in learned
goal representation (z_goal), not in the action-selection mechanism.
A perfect signal is sufficient -- z_goal learning must improve.

If C2 FAIL: Even a perfect goal signal is insufficient -- the
harm-avoidance tradeoff or env layout is the true bottleneck.
Improving z_goal learning alone will not fix SD-015.

## Per-Seed

GOAL_HANDCRAFTED:
  seed=42: benefit/ep=2.190 harm/ep=1.349 oracle_prox=0.185
  seed=7: benefit/ep=2.430 harm/ep=1.393 oracle_prox=0.197
  seed=13: benefit/ep=1.950 harm/ep=1.318 oracle_prox=0.183

GOAL_ABSENT:
  seed=42: benefit/ep=0.160 harm/ep=1.174
  seed=7: benefit/ep=0.180 harm/ep=1.158
  seed=13: benefit/ep=0.250 harm/ep=1.169

