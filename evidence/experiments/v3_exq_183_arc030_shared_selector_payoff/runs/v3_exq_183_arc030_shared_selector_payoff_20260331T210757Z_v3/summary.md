# V3-EXQ-183 -- ARC-030 Shared Selector Payoff

**Status:** FAIL
**Claims:** ARC-030, MECH-112
**Decision:** retire_ree_claim
**Seeds:** [42, 7, 13]

## Design

Shared harm+goal selector (E3 with benefit_eval_head) vs harm-only vs random.
benefit_eval_head trained with F.binary_cross_entropy (Sigmoid already applied).
Labels: is_near_resource = manhattan_dist <= 2.
Action selection: score = harm_eval(z_world_next) - benefit_weight * benefit_eval(z_world_next).

## Results

| Condition | benefit_rate | mean_benefit | harm_rate |
|---|---|---|---|
| COMBINED | 0.153 | 0.00300 | 0.14609 |
| HARM_ONLY | 0.127 | 0.00185 | 0.18431 |
| RANDOM | 0.210 | 0.00689 | 0.25319 |

**benefit_eval_auc:** 0.5384
**benefit_ratio (combined/harm_only):** 1.21x
**harm_ratio (combined/harm_only):** 0.79x

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: benefit_ratio >= 1.2x | PASS | 1.21x |
| C2: benefit_eval_auc >= 0.65 | FAIL | 0.5384 |
| C3: harm_ratio <= 1.2x | PASS | 0.79x |

Criteria met: 2/3 -> **FAIL**

## Per-Seed

  seed=42: auc=0.5671 combined_br=0.140 harm_only_br=0.170 random_br=0.250
  seed=7: auc=0.5621 combined_br=0.170 harm_only_br=0.200 random_br=0.230
  seed=13: auc=0.4859 combined_br=0.150 harm_only_br=0.010 random_br=0.150

## Failure Notes

- C2 FAIL: benefit_eval_auc=0.5384 < 0.65. Benefit head cannot discriminate near-resource states.
