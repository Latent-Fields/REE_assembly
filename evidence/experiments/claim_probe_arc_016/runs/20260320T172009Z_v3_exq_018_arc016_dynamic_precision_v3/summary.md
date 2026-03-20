# V3-EXQ-018 — ARC-016 Dynamic Precision Commitment Test

**Status:** FAIL
**Training:** 1000 eps (stable: num_hazards=3, drift_interval=100, drift_prob=0.0)
**Eval stable:** 50 eps | **Eval perturbed:** 50 eps (num_hazards=20, drift_interval=1, drift_prob=1.0)
**Recovery:** 30 eps
**Seed:** 1

## Motivation (ARC-016)

V2 EXQ-025 FAILED because precision was externally imposed. V3 derives precision
from E3's own prediction error EMA (running_variance). At each step:
  z_world_predicted = E2.world_forward(z_world_t, a_t)
  prediction_error  = z_world_{t+1} - z_world_predicted
  agent.e3.update_running_variance(prediction_error)

  precision        = 1 / (running_variance + ε)
  commit_threshold = 0.003 (variance-space — E3Config.commitment_threshold, calibrated 2026-03-18)
  committed        = running_variance < commit_threshold

## Phase Results

| Phase | mean_var | mean_precision | commit_rate | n_decisions |
|---|---|---|---|---|
| Training (stable) | 0.0012 | 1080.898 | 1.000 | 18889 |
| Eval stable | 0.0026 | 718.633 | 0.999 | 947 |
| Eval perturbed | 0.0036 | 426.064 | 0.999 | 854 |
| Recovery | 0.0033 | 723.746 | 0.998 | 572 |

**Key differences:**
- running_variance: perturbed - stable = 0.0010
- precision: stable - perturbed = 292.5690
- commit_rate: stable - perturbed = 0.0001

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: var_diff > 0.001 (variance diverges; calibrated from stable≈0.0027, perturbed≈0.0038) | FAIL | 0.0010 |
| C2: precision_stable > precision_perturbed | PASS | 292.5690 |
| C3: commit_rate_stable > commit_rate_perturbed | PASS | 0.0001 |
| C4: n_stable_decisions >= 20 | PASS | 947 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C1 FAIL: running_variance perturbed-stable diff=0.0010 <= 0.001 [perturbed=0.0036 stable=0.0026]
