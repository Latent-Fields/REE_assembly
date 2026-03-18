# V3-EXQ-022 — Combined Event-Contrastive + lstsq Reafference

**Status:** FAIL
**Warmup:** 1000 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**λ_event:** 0.5
**Probe eval:** 10 grid resets
**Seed:** 0

## Motivation (MECH-100 + MECH-098 combined)

EXQ-020 tests contrastive supervision alone (MECH-100).
EXQ-021 tests lstsq reafference alone (MECH-098 + fixed C3).
This experiment combines both mechanisms to test whether their interaction
produces calibration_gap > 0.05 when neither alone does.

## Results

| Metric | Value |
|---|---|
| event_classification_acc | 0.692 |
| R²_test (lstsq reafference) | 0.000 |
| Δz_raw(empty) | 13.3235 |
| Δz_corrected(empty) | 155.0804 |
| **calibration_gap** | **0.0000** |
| warmup harm events | 55227 |
| n_empty_steps | 119162 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.05 | FAIL | 0.0000 |
| C2: event_classification_acc > 0.5 | PASS | 0.692 |
| C3: R²_test > 0.25 | FAIL | 0.000 |
| C4: Δz_corrected < Δz_raw (empty) | FAIL | 155.0804 vs 13.3235 |
| C5: Warmup harm > 100 | PASS | 55227 |
| C6: No fatal errors | PASS | 0 |

Criteria met: 3/6 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=0.0000 <= 0.05
- C3 FAIL: R²_test=0.000 <= 0.25
- C4 FAIL: dz_corrected=155.0804 >= dz_raw=13.3235
