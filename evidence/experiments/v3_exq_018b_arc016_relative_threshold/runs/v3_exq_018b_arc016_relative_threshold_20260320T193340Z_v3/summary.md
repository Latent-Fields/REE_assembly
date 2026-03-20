# V3-EXQ-018b — ARC-016 Relative Threshold

**Status:** PASS
**Training:** 1000 eps (stable: num_hazards=2, drift_interval=200, drift_prob=0.0)
**Eval stable:** 50 eps | **Eval perturbed:** 50 eps (num_hazards=25, drift_interval=1, drift_prob=1.0)
**Recovery:** 30 eps
**Seed:** 0

## Fix vs EXQ-018: Relative Threshold (Sleep Recalibration)

EXQ-018 FAIL: commit_threshold=0.40 was 100× the operating variance range
(stable≈0.0026, perturbed≈0.0036). Absolute threshold calibration is fragile.

Fix: **relative threshold** calibrated from training baseline:
  `commit_threshold = 2.0 × training_baseline_variance`

`training_baseline_variance` = mean running_variance over last 100 training episodes.

Biological analogy (sleep recalibration): Slow-wave sleep resets the prediction error
baseline. Waking commitment thresholds are calibrated relative to that baseline.
An agent "waking into" a stable environment establishes a reference variance level,
then commits when variance stays within 2× of that reference, and withholds
commitment when variance exceeds that margin.

## Calibration Results

| Metric | Value |
|---|---|
| training_baseline_variance | 0.002315 |
| calibration_factor | 2.0 |
| calibrated_commit_threshold | 0.004630 |
| C1 relative threshold (0.5 × baseline) | 0.001157 |

## Phase Results

| Phase | mean_var | mean_precision | commit_rate | n_decisions |
|---|---|---|---|---|
| Training (stable) | 0.001911 | 681.875 | 1.000 | 18884 |
| Eval stable | 0.003979 | 381.123 | 0.901 | 936 |
| Eval perturbed | 0.005963 | 215.508 | 0.502 | 803 |
| Recovery | 0.004669 | 382.443 | 0.883 | 574 |

**Key differences:**
- running_variance: perturbed - stable = 0.001984  (c1_threshold = 0.001157)
- precision: stable - perturbed = 165.6149
- commit_rate: stable - perturbed = 0.3988

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C0: training_baseline_variance > 0 (calibration succeeded) | PASS | 0.002315 |
| C1: var_diff > 0.5 × baseline=0.001157 (relative criterion) | PASS | 0.001984 |
| C2: precision_stable > precision_perturbed | PASS | 165.6149 |
| C3: commit_rate_stable > commit_rate_perturbed (ARC-016) | PASS | 0.3988 |
| C4: n_stable_decisions >= 20 | PASS | 936 |

Criteria met: 5/5 → **PASS**

## Sleep Recalibration Note

This experiment models the biological observation that sleep establishes a "prediction
error baseline." The training phase (stable environment) corresponds to the waking
period during which the agent learns about its environment. The last 100
episodes before sleep are used to compute the baseline variance — this is the agent's
best estimate of "normal" operating variance. The calibrated commit_threshold
(0.004630 = 2.0 × 0.002315) is then used in
the subsequent waking period (eval phases). An agent experiencing a perturbed
environment will have running_variance > threshold → withholds commitment → explores.
An agent in a familiar stable environment will have running_variance < threshold →
commits → exploits.

