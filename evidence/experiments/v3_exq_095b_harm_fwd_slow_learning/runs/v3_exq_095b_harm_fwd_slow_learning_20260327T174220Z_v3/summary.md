# V3-EXQ-095b -- ARC-033 / SD-011 HarmForwardModel Slow-Learning Extension

**Status:** FAIL
**Claims:** ARC-033, SD-011
**Supersedes:** V3-EXQ-095a (SLOW_LEARNING at 900 eps)
**Phase 1:** 1800 eps (2x EXQ-095a)
**Parallel tests:** FULL (51d) vs HAZARD (25d) forward models

## Diagnosis: SLOW_LEARNING_PERSISTENT

## Key Metrics

| Metric | Value | Criterion |
|--------|-------|-----------|
| Max grad norm (FULL fwd) | 0.064849 | > 1e-5 (C1) |
| HF loss (early/mid/late) | early=0.00118  mid=0.00095  late=0.00093 | late < 0.5x early (C2) |
| R2 FULL | 0.0000 | > 0.20 (C4) |
| R2 HAZARD | 0.0000 | > 0.10 (C3) |
| causal_approach | 0.000488 | > 0.001 (C5) |
| calibration_gap | 0.0821 | -- |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: gradients flowing | PASS | 0.064849 |
| C2: loss halved | PASS | 0.00094 vs 0.00426 |
| C3: hazard R2 > 0.10 | FAIL | 0.0000 |
| C4: full R2 > 0.20 | FAIL | 0.0000 |
| C5: causal_approach > 0.001 | FAIL | 0.000488 |

Criteria met: 2/5 -> **FAIL**

## Diagnosis Codes

- GRADIENT_DETACH: No gradients -- detach bug.
- NOT_LEARNABLE: Signal lacks action-conditional structure at this scale.
- HAZARD_ONLY_WORKS: Use hazard-only (25d) for ARC-033 forward model.
- SLOW_LEARNING_PERSISTENT: Still converging to mean at 1800 eps -- need larger model.
- BOTH_LEARN: Full pipeline viable -- proceed to ARC-033 counterfactual validation.

## Failure Notes

- C3 FAIL: hazard_r2=0.0000 -- not action-learnable
- C4 FAIL: full_r2=0.0000 -- full harm stream not learnable
- C5 FAIL: causal_approach=0.000488
