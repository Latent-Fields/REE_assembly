# e1_e2_terrain_timescale

**Claim:** MECH-058  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-15T04:59:33.847875+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `separated_harm_last_quarter`: 1.232
- `collapsed_fast_harm_last_quarter`: 1.238
- `collapsed_slow_harm_last_quarter`: 1.2553
- `separated_avoidance_rate_last_quarter`: 0.9323
- `collapsed_fast_avoidance_rate_last_quarter`: 0.9323
- `separated_post_drift_harm_rate_last_quarter`: 0.1235
- `collapsed_slow_post_drift_harm_rate_last_quarter`: 0.1155
- `criterion_1_terrain_timescale_met`: False
- `criterion_2_drift_timescale_met`: False
- `criterion_3_overall_performance_met`: True
- `criteria_met`: 1

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `e1_lr_slow`: 5e-05
- `policy_lr_fast`: 0.001
- `post_drift_window`: 3
- `avoidance_margin`: 0.03
- `drift_harm_margin`: 0.02
- `harm_tolerance`: 1.1