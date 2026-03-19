# action_doing_mode_probe

**Claim:** MECH-025  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-08T13:20:31.377993+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `high_causal_precision_lift`: 0.0
- `low_causal_precision_lift`: 0.0
- `high_causal_slope`: 0.0211
- `low_causal_slope`: 0.0174
- `criterion_1_lift_met`: False
- `criterion_2_slope_met`: False
- `criteria_met`: 0

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `condition_hazards`: {'HIGH_CAUSAL': 8, 'LOW_CAUSAL': 1}
- `environment`: CausalGridWorld
- `e1_lr`: 0.0001
- `policy_lr`: 0.001
- `lift_margin`: 0.05
- `slope_margin`: 0.05