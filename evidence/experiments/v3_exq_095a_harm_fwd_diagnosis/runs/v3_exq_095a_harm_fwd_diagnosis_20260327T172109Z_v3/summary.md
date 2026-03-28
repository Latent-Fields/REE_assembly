# V3-EXQ-095a -- ARC-033 / SD-011 HarmForwardModel Training Diagnosis

**Status:** FAIL
**Claims:** ARC-033, SD-011
**Supersedes:** EXQ-095 (R2=0.0, undiagnosed failure)
**Phase 1:** 900 eps (3x EXQ-095)
**Parallel tests:** FULL (51d) vs HAZARD (25d) forward models

## Diagnosis: SLOW_LEARNING

## Key Metrics

| Metric | Value | Criterion |
|--------|-------|-----------|
| Max grad norm (FULL fwd) | 0.064849 | > 1e-5 (C1) |
| HF loss (early/mid/late) | early=0.00137  mid=0.00098  late=0.00098 | late < 0.5x early (C2) |
| R2 FULL | 0.0000 | > 0.20 (C4) |
| R2 HAZARD | 0.0000 | > 0.10 (C3) |
| causal_approach | 0.003864 | > 0.001 (C5) |
| calibration_gap | 0.0728 | -- |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: gradients flowing | PASS | 0.064849 |
| C2: loss halved | PASS | 0.00113 vs 0.00426 |
| C3: hazard R2 > 0.10 | FAIL | 0.0000 |
| C4: full R2 > 0.20 | FAIL | 0.0000 |
| C5: causal_approach > 0.001 | PASS | 0.003864 |

Criteria met: 3/5 -> **FAIL**

## Interpretation by Diagnosis Code

- GRADIENT_DETACH: z_harm_s is detached from backward graph. Check HarmEncoder calls.
- NOT_LEARNABLE: Forward model gets gradients but can't learn. Signal may lack
  action-conditional structure at this grid size / hazard configuration.
- HAZARD_ONLY_WORKS: Use hazard-only (first 25d) for ARC-033. Resource
  proximity noise contaminates full stream. Proceed to EXQ-095b.
- SLOW_LEARNING: More episodes needed. Try 1800 phase1 eps or larger model.
- BOTH_LEARN: Full pipeline viable. Proceed directly to ARC-033 validation.

## Failure Notes

- C3 FAIL: hazard_r2=0.0000 -- hazard proximity not action-learnable
- C4 FAIL: full_r2=0.0000 -- full harm stream not learnable
