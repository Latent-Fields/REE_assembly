# V3-EXQ-180 -- Resource Proximity Gradient Diagnostic

**Status:** FAIL
**Claims:** MECH-112, SD-012, ARC-030
**Seeds:** [42, 7]

## Context

EXQ-179 confirmed: goal_tracking_r=-0.056 (H-A), selection_bias~0 (H-B). z_goal seeding from z_world is scene noise, not a resource gradient. This experiment tests whether benefit_eval_head (ARC-030) can provide the missing gradient by learning resource_prox from z_world directly.

## Two-Part Design

**Part 1 (linear probe):** Is resource proximity linearly decodable from z_world?
  probe_r2 = R^2 of ridge regression z_world -> resource_prox on 10 random-action probe episodes post-warmup.

**Part 2 (navigation test):** Does training benefit_eval_head on resource_prox labels improve E3 trajectory selection?
  benefit_head_r = Pearson r(benefit_eval(z_world_t), resource_prox_t) in eval
  benefit_ratio = benefit_EVAL_ON / benefit_EVAL_OFF

**alpha_world:** 0.9  (SD-008)
**benefit_weight:** 1.0
**Warmup:** 400 eps (curriculum=80 eps)
**Probe:** 10 eps (random actions, post-warmup)
**Eval:** 60 eps per condition

## Key Results

| Metric | Value | Threshold | Interpretation |
|---|---|---|---|
| probe_r2 (Part 1) | 0.6187 | > 0.05 = signal in z_world | C1 PASS: probe_r2=0.6187 > 0.05. z_world DOES contain resour... |
| benefit_head_r | 0.275 | > 0.1 = head tracks gradient | C2 PASS: benefit_head_r=0.275 > 0.1. Head tracks resource pr... |
| benefit_ratio | 0.29x | > 1.2 = navigation improved | C3 FAIL: benefit_ratio=0.29x <= 1.2. Head tracks proximity b... |

## Navigation Results

| Condition | benefit/ep | probe_r2 | benefit_head_r |
|---|---|---|---|
| BENEFIT_EVAL_ON | 0.192 | 0.6187 | 0.275 |
| BENEFIT_EVAL_OFF (random) | 0.667 | -- | -- |

**Benefit ratio: 0.29x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: probe_r2 > 0.05 | PASS | 0.6187 |
| C2: benefit_head_r > 0.1 | PASS | 0.275 |
| C3: benefit_ratio > 1.2 | FAIL | 0.29x |
| C4: n_probe_steps >= 500 | FAIL | 216 |

Criteria met: 2/4 -> **FAIL**

## Interpretation

C1 PASS: probe_r2=0.6187 > 0.05. z_world DOES contain resource proximity signal.

C2 PASS: benefit_head_r=0.275 > 0.1. Head tracks resource proximity in eval.

C3 FAIL: benefit_ratio=0.29x <= 1.2. Head tracks proximity but E3 scoring does not improve navigation. Consider increasing benefit_weight or checking trajectory diversity.

**benefit_r2_probe (head fit on probe data):** 0.0876

## Per-Seed

BENEFIT_EVAL_ON:
  seed=42: benefit/ep=0.183 probe_r2=0.6143 benefit_head_r=0.255 n_trained=8646
  seed=7: benefit/ep=0.200 probe_r2=0.6231 benefit_head_r=0.296 n_trained=8658

BENEFIT_EVAL_OFF:
  seed=42: benefit/ep=0.767
  seed=7: benefit/ep=0.567

## Failure Notes

- C3 FAIL: benefit_ratio=0.29x <= 1.2. Head tracks proximity but E3 scoring does not improve navigation. Consider increasing benefit_weight or checking trajectory diversity.
- C4 FAIL: n_probe_steps=216 < 500. Increase probe_episodes.
