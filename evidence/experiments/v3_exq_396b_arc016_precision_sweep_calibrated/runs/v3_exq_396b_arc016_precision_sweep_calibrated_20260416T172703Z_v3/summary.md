# V3-EXQ-396b -- ARC-016 Precision Sweep (EXP-0094 auto-calibration)

**Status:** FAIL
**Claims:** ARC-016, MECH-093
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Hazard harm levels:** [0.005, 0.01, 0.02, 0.05, 0.1]
**Calibration factor:** 2.0x (EXP-0094)
**Supersedes:** V3-EXQ-396a -> V3-EXQ-396 -> V3-EXQ-038

## Root Cause Fixed

EXQ-396a fixed training/eval variance bugs but still failed: fixed threshold (0.40)
>> post-training variance (~0.07); agent always committed; C3/C4 always failed.

EXQ-396b fixes:
1. EXP-0094 auto-calibration: threshold = 2x mean(last 100 ep variances).
   threshold ~= 2 * baseline, so stable eval commits and perturbed eval can break it.
2. Truly static training env (drift_prob=0.0): baseline drops from ~0.07 to ~0.001.
3. C3 criterion requires +0.05 margin to avoid passing on noise.

Biological analog: SWS recalibrates prediction-error baseline;
waking thresholds are 2x that baseline (EXQ-018b: same factor, PASS).

## Sweep Results

| hazard_harm | baseline_var | cal_threshold | var_stable | var_perturbed | var_diff | commit_stable | commit_perturbed |
|---|---|---|---|---|---|---|---|
| 0.005 | 0.000032 | 0.000064 | 0.001175 | 0.001148 | -0.000027 | 0.014 | 0.015 |
| 0.010 | 0.000032 | 0.000064 | 0.001171 | 0.001147 | -0.000024 | 0.014 | 0.014 |
| 0.020 | 0.000032 | 0.000064 | 0.001170 | 0.001136 | -0.000034 | 0.014 | 0.015 |
| 0.050 | 0.000032 | 0.000063 | 0.001144 | 0.001140 | -0.000004 | 0.014 | 0.016 |
| 0.100 | 0.000032 | 0.000064 | 0.001154 | 0.001157 | 0.000003 | 0.014 | 0.015 |
**Pearson r(hazard_harm, var_diff):** 0.891
**Monotone increases in var_diff:** 3/4

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: var_diff monotone (3+ consec) | PASS | 3/4 |
| C2: Pearson r > 0.6 | PASS | 0.891 |
| C3: >= 3 levels commit_stable > commit_perturbed+0.05 | FAIL | 0/5 |
| C4: >= 3 levels cal_threshold > var_stable | FAIL | 0/5 |
| C5: no fatal errors | PASS | 0 errors |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C3 FAIL: only 0/5 levels show commit_stable > commit_perturbed + 0.05
- C4 FAIL: only 0/5 levels have calibrated_threshold > var_stable

## Per-Claim Evidence Direction

- ARC-016 (dynamic precision drives commitment): weakens
  (C3 + C4; mechanism works regardless of hazard_harm scaling)
- MECH-093 (precision scales with hazard danger): supports
  (C1 + C2; hazard_harm magnitude must modulate var_diff)
