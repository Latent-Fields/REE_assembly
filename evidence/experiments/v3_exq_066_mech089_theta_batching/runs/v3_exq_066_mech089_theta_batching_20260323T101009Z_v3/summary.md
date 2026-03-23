# V3-EXQ-066 -- MECH-089: Theta-Batching Reduces E3 Prediction Error

**Status:** FAIL
**Claims:** MECH-089
**Design:** k=4 (theta buffer size); batched (theta_buffer_size=4, e3_steps=4) vs raw (theta_buffer_size=1, e3_steps=1)
**alpha_world:** 0.9
**Training:** 300 episodes x 200 steps
**Seed:** 0

## Motivation

MECH-089: E3 never sees raw E1 output -- it receives theta-cycle-averaged z_world
from ThetaBuffer. Averaging over k=4 E1 steps should filter within-cycle
noise, reducing E3's harm-prediction error variance vs per-step (raw) sampling.

This experiment isolates the averaging effect by holding all other factors constant
(same seed, same env, same training dynamics, same alpha_world).

## Results

| Metric | Batched (k=4) | Raw (k=1) |
|--------|----------------------|-----------|
| e3_prediction_error_var | 0.00910 | 0.00399 |
| harm_pred_std | 0.2024 | 0.1776 |
| batch_uniformity (mean z_world intra-window var) | 0.00000 | 0.00000 |
| e1_per_e3 | 3.00 | 0.00 |
| e3_count | 15000 | 60000 |
| fatal_errors | 0 | 0 |

Reduction ratio (batched/raw): 2.2779

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: e3_pred_var_batched < raw*0.90 (>=10% reduction) | FAIL | 0.00910 vs 0.00360 |
| C2: e1_per_e3_batched >= k-1 = 3 (batching active) | PASS | 3.00 |
| C3: harm_pred_std_batched > 0.01 (E3 not collapsed) | PASS | 0.2024 |
| C4: harm_pred_std_raw > 0.01 (E3 not collapsed) | PASS | 0.1776 |
| C5: No fatal errors | PASS | batched=0 raw=0 |

Criteria met: 4/5 -> **FAIL**

## Failure Notes

- C1 FAIL: e3_pred_var_batched=0.00910 >= raw*0.90=0.00360
