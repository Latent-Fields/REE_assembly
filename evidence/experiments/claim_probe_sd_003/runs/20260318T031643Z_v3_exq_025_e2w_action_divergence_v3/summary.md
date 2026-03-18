# V3-EXQ-025 — E2_world Action-Conditional Divergence Diagnostic

**Status:** FAIL
**alpha_world:** 0.9
**Probe env:** 6 hazards, min_dist > 2
**Seed:** 0

## What This Tests

E2_world action-conditional divergence: `||E2.world_forward(z, a1) - E2.world_forward(z, a2)||`
Measured at near-hazard vs safe positions WITHOUT going through net_eval.

Conditions:
- **A**: Rollout-only (replicates EXQ-023 training)
- **B**: With 1-step direct loss (EXQ-024 fix)
- **C**: Condition B + lstsq reafference correction

## E2_world Quality

| Condition | 1-step MSE | Identity MSE | Improvement ratio |
|---|---|---|---|
| A (rollout-only) | 0.00048 | 0.00052 | 1.08× |
| B (1-step loss)  | 0.00045 | 0.00054 | 1.19× |

## Action-Conditional Divergence

| Condition | near-hazard div | safe div | gap |
|---|---|---|---|
| A (rollout-only, no lstsq) | 0.0553 | 0.0542 | 0.0011 |
| B (1-step loss, no lstsq)  | 0.0618 | 0.0607 | 0.0011 |
| C (1-step + lstsq)         | 0.0593 | 0.0591 | 0.0003 |

n_near=208  n_safe=481  (probe_env: 6 hazards)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: improvement_ratio(B) > 2.0× | FAIL | 1.19× |
| C2: action_div_gap(B) > 0.002 | FAIL | 0.0011 |
| C3: div_near(B) ≥ 1.2× div_near(A) | FAIL | 0.0618 vs 0.0553 |
| C4: n_near >= 50 and n_safe >= 50 | PASS | 208, 481 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C1 FAIL: e2w_improvement_ratio(B)=1.19x <= 2.0
- C2 FAIL: action_div_gap(B)=0.0011 <= 0.002
- C3 FAIL: div_near(B)=0.0618 not ≥1.2× div_near(A)=0.0553
