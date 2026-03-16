# causal_attribution_calibration

**Claim:** MECH-071  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-15T18:37:57.097148+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `trained_mean_calibration_gap`: -0.0041
- `random_mean_calibration_gap`: -0.0005
- `criterion_1_trained_gap_above_threshold`: False
- `criterion_2_random_gap_below_max`: True
- `criterion_3_both_types_observed`: True

## Config

- `num_warmup_episodes`: 200
- `num_eval_episodes`: 50
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `num_resources`: 5
- `environment`: CausalGridWorld
- `calibration_gap_threshold`: 0.05
- `random_gap_abs_max`: 0.1
- `e1_lr`: 0.0001
- `e2_lr`: 0.001
- `policy_lr`: 0.001