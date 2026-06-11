# V3-EXQ-671 -- MECH-025b: Precision-Responsibility Attribution

**Status:** FAIL
**Claim:** MECH-025b -- high-precision action mode carries responsibility attribution
**Prerequisite:** MECH-025 (doing mode produces internal signature)
**alpha_world:** 0.9
**Warmup:** 500 eps  |  Eval: 50 eps
**Seed:** 0

## Motivation

MECH-025b tests the philosophical bridge: does precision level modulate
responsibility weight? Actions committed at higher precision should accumulate
proportionally more residue (ethical accountability) than low-precision actions,
because high-precision implies the agent had finer discrimination capacity.

## Results

| Metric | Value |
|--------|-------|
| Precision-Residue Correlation | 0.0000 |
| High/Low Precision Residue Ratio | 0.0000 |
| Committed Steps Sampled | 778 |
| World Forward R2 | 0.9324 |
| Harm Pred Std | 0.1948 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: precision_residue_correlation > 0.15 | FAIL | 0.0000 |
| C2: high_precision_residue_ratio > 1.1 | FAIL | 0.0000 |
| C3: committed_step_count >= 20 | PASS | 778 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9324 |
| C5: harm_pred_std > 0.01 | PASS | 0.1948 |
| C6: No fatal errors | PASS | 0 |

Criteria met: 4/6 -> **FAIL**

## Failure Notes

- C1 FAIL: precision_residue_correlation=0.0000 <= 0.15
- C2 FAIL: high_precision_residue_ratio=0.0000 <= 1.1
