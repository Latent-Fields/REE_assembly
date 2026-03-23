# V3-EXQ-082 -- MECH-098 Reafference vs No-Reafference: Harm Calibration Pair

**Status:** FAIL
**Claims:** MECH-098
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 350 eps  **Eval:** 50 eps

## Pre-Registered Thresholds

C1: delta_approach_gap (REAFFERENCE - NO_REAFFERENCE) > 0.02
C2: gap_approach_REAFFERENCE > 0.06
C3: gap_approach_NO_REAFFERENCE > 0

## Results

| Condition | gap_approach | gap_contact | mean_none | mean_approach |
|-----------|-------------|-------------|-----------|---------------|
| REAFFERENCE    | 0.0924 | 0.0944 | 0.4453 | 0.5377 |
| NO_REAFFERENCE | 0.1968 | 0.1738 | 0.3817 | 0.5785 |

**delta_approach_gap (REAFFERENCE - NO_REAFFERENCE): -0.1044**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_approach_gap > 0.02 | FAIL | -0.1044 |
| C2: gap_approach_REAFFERENCE > 0.06 | PASS | 0.0924 |
| C3: gap_approach_NO_REAFFERENCE > 0  | PASS | 0.1968 |

Criteria met: 2/3 -> **FAIL**

## Interpretation

MECH-098 NOT SUPPORTED: reafference correction does not improve approach detection (delta=-0.1044, gap_REAFFERENCE=0.0924). Perspective-shift noise may not dominate at this model/task scale, or the implicit E2 training signal is insufficient to train the ReafferencePredictor. Consider explicit predictor training (see EXQ-027b pattern) or larger world_dim for more separation.

## Per-Seed

REAFFERENCE:
  seed=42: gap_approach=0.0927 gap_contact=0.1006 n_approach=858 train_approach=5523
  seed=7: gap_approach=0.0921 gap_contact=0.0882 n_approach=830 train_approach=5689

NO_REAFFERENCE:
  seed=42: gap_approach=0.2010 gap_contact=0.1889 n_approach=858
  seed=7: gap_approach=0.1927 gap_contact=0.1587 n_approach=830

## Failure Notes

- C1 FAIL: delta_approach_gap=-0.1044 <= 0.02 (reafference correction does not improve approach detection by 2pp)
