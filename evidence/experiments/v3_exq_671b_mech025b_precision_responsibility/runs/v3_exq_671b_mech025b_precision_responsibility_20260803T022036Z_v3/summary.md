# V3-EXQ-671b -- MECH-025b: Precision-Responsibility Attribution (corrected)

**Status:** FAIL
**Label:** precision_does_not_modulate_residue_responsibility_weight
**Claim:** MECH-025b -- high-precision action mode carries responsibility attribution
**Prerequisite:** MECH-025 (doing mode produces internal signature)
**Supersedes:** V3-EXQ-671a (asymmetric positive-control gap on the independent
variable + underpowered single-seed n=29, per failure_autopsy_V3-EXQ-671a_2026-08-02)
**alpha_world:** 0.9
**Warmup:** 500 eps/seed  |  Eval: 50 eps/seed
**Seeds:** [0, 1, 2, 3]

## Motivation

MECH-025b tests the philosophical bridge: does precision level modulate
responsibility weight? Actions committed at higher precision should accumulate
proportionally more residue (ethical accountability) than low-precision actions,
because high-precision implies the agent had finer discrimination capacity.

## Positive-Control Gates

| Check | Measured | Floor | Met |
|---|---|---|---|
| residue_accumulates_under_committed_harm | 14.76 | 1e-06 | True |
| precision_shows_adequate_variance (pooled) | 160658 | 1 | True |

C1 non-degeneracy (pooled residue_delta_samples spread + per-seed precision_samples groups):
True (ok)

## Pooled Results (n=179, 4 seeds)

| Metric | Value |
|--------|-------|
| Precision-Residue Correlation | -0.0446 |
| High/Low Precision Residue Ratio | 1.0618 |
| Committed Steps Sampled | 179 |
| World Forward R2 (mean across seeds) | 0.9602 |
| Harm Pred Std (mean across seeds) | 0.1021 |
| Total Residue Accumulated | 46.980026 |

## Per-Seed Diagnostics (non-gating)

| Seed | Committed | Precision Spread | Correlation | Ratio | WF R2 | Harm Std |
|---|---|---|---|---|---|---|
| 0 | 29 | 160611.7646 | 0.0505 | 0.9214 | 0.9324 | 0.1485 |
| 1 | 72 | 5674.2348 | 0.1017 | 1.1327 | 0.9844 | 0.0616 |
| 2 | 77 | 4300.2487 | 0.0651 | 1.1471 | 0.9621 | 0.0536 |
| 3 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.9620 | 0.1446 |

0/4 seeds individually show C1>0.15; 2/4 show C2>1.1.

## PASS Criteria (computed on pooled samples)

| Criterion | Result | Value |
|---|---|---|
| C1: precision_residue_correlation > 0.15 | FAIL | -0.0446 |
| C2: high_precision_residue_ratio > 1.1 | FAIL | 1.0618 |
| C3: committed_step_count >= 20 | PASS | 179 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9602 |
| C5: harm_pred_std > 0.01 | PASS | 0.1021 |
| C6: No fatal errors | PASS | 0 |

Criteria met: 4/6 -> **FAIL** (label: precision_does_not_modulate_residue_responsibility_weight)

## Failure Notes

- C1 FAIL: precision_residue_correlation=-0.0446 <= 0.15
- C2 FAIL: high_precision_residue_ratio=1.0618 <= 1.1
