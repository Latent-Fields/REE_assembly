# V3-EXQ-071d -- Rollout-Batched SD-003 Attribution

**Status:** FAIL
**Claims:** SD-003, ARC-024, MECH-071
**Predecessor:** EXQ-030b PASS (sequential attribution baseline)
**Supersedes:** V3-EXQ-071b
**Warmup:** 150 eps | **Eval:** 30 eps x 3 distractor levels
**alpha_world:** 0.9 | **world_forward R2:** 0.9452

## Attribution Results by Distractor Level

| n_hazards | batch_sig_approach | seq_sig_approach | rank_corr | batch_gap | n_approach |
|---|---|---|---|---|---|
| 2 | -0.000126 | -0.000126 | 1.0000 | +0.001959 | 681 |
| 4 | +0.000956 | +0.000956 | 1.0000 | +0.005164 | 513 |
| 6 | +0.001020 | +0.001020 | 1.0000 | +0.012481 | 379 |


## Pass Criteria

| Criterion | Result |
|---|---|
| C1: batched attribution_gap > 0 (all levels) | PASS |
| C2: rank_corr(batched, sequential) > 0.90 (all levels) | PASS |
| C3: batched causal_sig_approach > 0.005 (all levels) | FAIL |
| C4: world_forward_r2 > 0.05 | PASS (0.9452) |
| C5: n_approach >= 20 per level | PASS |

Criteria met: 4/5 -> **FAIL**

## Failure Notes

- C3 FAIL n_hazards=2: batch_sig_approach=-0.000126 <= 0.005
- C3 FAIL n_hazards=4: batch_sig_approach=0.000956 <= 0.005
- C3 FAIL n_hazards=6: batch_sig_approach=0.001020 <= 0.005
