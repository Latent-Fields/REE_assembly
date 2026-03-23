# V3-EXQ-079 -- MECH-071 Harm Calibration Discriminative Pair

**Status:** FAIL
**Claims:** MECH-071
**Decision:** hybridize
**Seeds:** [42, 7]
**SHARP_WORLD alpha_world:** 0.9  (SD-008)
**SMOOTH_WORLD alpha_world:** 0.3  (baseline)
**Warmup:** 350 eps  **Eval:** 60 eps

## Pre-Registered Thresholds

C1: delta_calibration_gap        > 0.015
C2: calibration_gap_SHARP        > 0.025
C3: calibration_gap_SMOOTH       < 0.020
C4: per-seed SHARP > SMOOTH directionality

## Results

| Condition | calibration_gap | env_gap | approach_gap | mean_none | mean_agent |
|-----------|----------------|---------|--------------|-----------|------------|
| SHARP_WORLD  | 0.1689  | 0.2711 | 0.2305 | 0.3630 | 0.5319 |
| SMOOTH_WORLD | 0.1123 | 0.1918 | 0.1505 | 0.4086 | 0.5209 |

**delta_calibration_gap (SHARP - SMOOTH): +0.0566**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_calibration_gap > 0.015    | PASS | 0.0566 |
| C2: calibration_gap_SHARP > 0.025    | PASS | 0.1689 |
| C3: calibration_gap_SMOOTH < 0.020   | FAIL | 0.1123 |
| C4: per-seed SHARP > SMOOTH           | PASS | [True, True] |

Criteria met: 3/4 -> **FAIL**

## Interpretation

Weak positive: SHARP_WORLD shows higher calibration gap but discriminative margin vs SMOOTH_WORLD is below threshold. SD-008 helps but the mechanism is marginal -- z_world may encode some hazard structure even at alpha=0.3.

## Per-Seed

SHARP_WORLD:
  seed=42: calibration_gap=0.2176 env_gap=0.3733 approach_gap=0.2745 n_agent=35 n_env=16
  seed=7: calibration_gap=0.1203 env_gap=0.1690 approach_gap=0.1864 n_agent=37 n_env=20

SMOOTH_WORLD:
  seed=42: calibration_gap=0.1568 env_gap=0.2741 approach_gap=0.1852
  seed=7: calibration_gap=0.0679 env_gap=0.1094 approach_gap=0.1158

## Failure Notes

- C3 FAIL: calibration_gap_SMOOTH=0.1123 >= 0.020 (calibration gap unexpectedly large without SD-008 -- confound present)
