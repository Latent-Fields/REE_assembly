# V3-EXQ-191 -- ARC-038 Schema Assimilation Probe

**Status:** FAIL
**Claims:** ARC-038
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**Env seed pairs:** [(100, 200), (300, 400)]

## Design

Schema transfer test: agent trained on Environment-1 (schema building),
then evaluated on Environment-2 (novel but structurally similar). Compared
to naive agent seeing Environment-2 for the first time.
Both conditions use harm_eval-based action selection and online learning
during evaluation. Measure: episodes to reach target harm rate.

## Results

| Condition | Eps to Target | Final Harm Rate | Mean Harm Rate |
|---|---|---|---|
| SCHEMA_PRIMED | 200.0 | 0.196423 | 0.159307 |
| NAIVE | 200.0 | 0.200586 | 0.185941 |
| RANDOM | 200.0 | 0.259709 | 0.268245 |

**Speedup ratio (naive_ett / primed_ett):** 1.00x

## PASS Criteria

| Criterion | Result | Detail |
|---|---|---|
| C1: primed_ett < naive_ett | FAIL | 200.0 vs 200.0 |
| C2: primed_final < naive_final | PASS | 0.196423 vs 0.200586 |
| C3: primed_ett < budget | FAIL | 200.0 vs 200 |

Criteria met: 1/3 -> **FAIL**

## Per-Seed

  seed=42 env_a=100 env_b=200: primed_ett=200 naive_ett=200 primed_final=0.201317 naive_final=0.298236
  seed=42 env_a=300 env_b=400: primed_ett=200 naive_ett=200 primed_final=0.263024 naive_final=0.135664
  seed=7 env_a=100 env_b=200: primed_ett=200 naive_ett=200 primed_final=0.202644 naive_final=0.198200
  seed=7 env_a=300 env_b=400: primed_ett=200 naive_ett=200 primed_final=0.118706 naive_final=0.170243

## Failure Notes

- C1 FAIL: primed_ett=200.0 >= naive_ett=200.0. Schema-primed agent did not reach target faster.
- C3 FAIL: primed_ett=200.0 >= eval_budget=200. Schema-primed agent never reached target harm rate.
