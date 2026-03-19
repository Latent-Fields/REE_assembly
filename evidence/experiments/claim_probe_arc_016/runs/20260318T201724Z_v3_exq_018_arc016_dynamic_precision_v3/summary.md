# V3-EXQ-018 — ARC-016 Dynamic Precision Commitment Test

**Status:** PASS
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
| Training (stable) | 0.0018 | 866.969 | 0.913 | 18889 |
| Eval stable | 0.0034 | 461.776 | 0.780 | 947 |
| Eval perturbed | 0.0052 | 251.077 | 0.050 | 854 |
| Recovery | 0.0041 | 466.566 | 0.766 | 572 |

**Key differences:**
- running_variance: perturbed - stable = 0.0018
- precision: stable - perturbed = 210.6993
- commit_rate: stable - perturbed = 0.7300

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: var_diff > 0.001 (variance diverges; calibrated from stable≈0.0027, perturbed≈0.0038) | PASS | 0.0018 |
| C2: precision_stable > precision_perturbed | PASS | 210.6993 |
| C3: commit_rate_stable > commit_rate_perturbed | PASS | 0.7300 |
| C4: n_stable_decisions >= 20 | PASS | 947 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 5/5 → **PASS**
