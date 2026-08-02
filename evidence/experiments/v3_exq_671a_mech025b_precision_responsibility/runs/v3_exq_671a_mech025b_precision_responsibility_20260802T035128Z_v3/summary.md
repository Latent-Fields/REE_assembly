# V3-EXQ-671a -- MECH-025b: Precision-Responsibility Attribution (corrected)

**Status:** FAIL
**Label:** precision_does_not_modulate_residue_responsibility_weight
**Claim:** MECH-025b -- high-precision action mode carries responsibility attribution
**Prerequisite:** MECH-025 (doing mode produces internal signature)
**Supersedes:** V3-EXQ-671 (degenerate: residue never accumulated -- instrument defect)
**alpha_world:** 0.9
**Warmup:** 500 eps  |  Eval: 50 eps
**Seed:** 0

## Motivation

MECH-025b tests the philosophical bridge: does precision level modulate
responsibility weight? Actions committed at higher precision should accumulate
proportionally more residue (ethical accountability) than low-precision actions,
because high-precision implies the agent had finer discrimination capacity.

## Positive-Control Gate

| Check | Measured | Floor | Met |
|---|---|---|---|
| residue_accumulates_under_committed_harm | 1.86 | 1e-06 | True |

Total residue accumulated during eval (lifetime delta): 13.480013
C1 non-degeneracy (residue_delta_samples spread): True (ok)

## Results

| Metric | Value |
|--------|-------|
| Precision-Residue Correlation | 0.0505 |
| High/Low Precision Residue Ratio | 0.9214 |
| Committed Steps Sampled | 29 |
| World Forward R2 | 0.9324 |
| Harm Pred Std | 0.1485 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: precision_residue_correlation > 0.15 | FAIL | 0.0505 |
| C2: high_precision_residue_ratio > 1.1 | FAIL | 0.9214 |
| C3: committed_step_count >= 20 | PASS | 29 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9324 |
| C5: harm_pred_std > 0.01 | PASS | 0.1485 |
| C6: No fatal errors | PASS | 0 |

Criteria met: 4/6 -> **FAIL** (label: precision_does_not_modulate_residue_responsibility_weight)

## Failure Notes

- C1 FAIL: precision_residue_correlation=0.0505 <= 0.15
- C2 FAIL: high_precision_residue_ratio=0.9214 <= 1.1
