# V3-EXQ-078 -- SD-005 Split vs Unified Latent: Harm Calibration Pair

**Status:** PASS
**Claims:** SD-005
**Decision:** retain_ree
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 350 eps  **Eval:** 50 eps

## Pre-Registered Thresholds

C1: delta_approach_gap (SPLIT - UNIFIED) > 0.02
C2: gap_approach_SPLIT > 0.06
C3: gap_approach_UNIFIED > 0

## Results

| Condition | gap_approach | gap_contact | mean_none | mean_approach |
|-----------|-------------|-------------|-----------|---------------|
| SPLIT   | 0.1968 | 0.1738 | 0.3817 | 0.5785 |
| UNIFIED | 0.1475 | 0.1318 | 0.4124 | 0.5598 |

**delta_approach_gap (SPLIT - UNIFIED): +0.0494**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_approach_gap > 0.02 | PASS | 0.0494 |
| C2: gap_approach_SPLIT > 0.06 | PASS | 0.1968 |
| C3: gap_approach_UNIFIED > 0  | PASS | 0.1475 |

Criteria met: 3/3 -> **PASS**

## Interpretation

SD-005 SUPPORTED: z_self/z_world split improves hazard approach detection. gap_approach_SPLIT=0.1968 vs UNIFIED=0.1475, delta=+0.0494. Separate world-state latent (free of motor/body-state dilution) gives E3 cleaner spatial hazard signal. Consistent with EXQ-047 (3.4pp calibration improvement, 82% attribution improvement).

## Per-Seed

SPLIT:
  seed=42: gap_approach=0.2010 gap_contact=0.1889 n_approach=858 train_approach=5523
  seed=7: gap_approach=0.1927 gap_contact=0.1587 n_approach=830 train_approach=5689

UNIFIED:
  seed=42: gap_approach=0.1428 gap_contact=0.1397 n_approach=858
  seed=7: gap_approach=0.1521 gap_contact=0.1239 n_approach=830

