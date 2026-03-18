# V3-EXQ-021 — lstsq Linear Reafference Correction

**Status:** FAIL
**Warmup:** 300 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**Probe eval:** 10 grid resets
**Seed:** 1

## Motivation (SD-007 / MECH-098, EXQ-016 bug fixes)

EXQ-016 failed on C2 (R²_test=0.118 vs threshold 0.2) and C3 (metric was broken).
This experiment fixes both issues:
  1. **lstsq**: torch.linalg.lstsq on [z_self|a|1] → Δz_world (expected R²≈0.333)
  2. **Fixed C3**: dz_corrected = dz_raw - pred (subtract ONCE, not from each endpoint)

## lstsq Predictor

| Metric | Value |
|---|---|
| Feature dim | 38 = self_dim(32) + actions(5) + 1 |
| n_empty_steps | 4977 |
| R²_train | 0.582 |
| R²_test | 0.310 |

## Δz_world Before/After Correction (Fixed Metric)

| Event Type | Raw Δz_world | Corrected Δz_world | Reduction |
|---|---|---|---|
| empty_move (locomotion) | 0.0479 | 0.0366 | 0.0114 |
| env_caused_hazard | 0.0444 | 0.0397 | 0.0048 |

## SD-003 Attribution (lstsq-Corrected z_world)

| Position | mean(causal_sig) |
|---|---|
| Near-hazard | -0.0013 |
| Safe | -0.0015 |
| **calibration_gap** | **0.0002** |

Warmup: harm=771  benefit=111

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.05 (lstsq-corrected) | FAIL | 0.0002 |
| C2: R²_test > 0.25 | PASS | 0.310 |
| C3: Δz_corrected(empty) < Δz_raw(empty) | PASS | 0.0366 vs 0.0479 |
| C4: Warmup harm events > 100 | PASS | 771 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=0.0002 <= 0.05
