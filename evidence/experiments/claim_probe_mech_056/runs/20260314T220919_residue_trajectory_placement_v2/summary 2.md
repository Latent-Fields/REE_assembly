# residue_trajectory_placement

**Claim:** MECH-056  
**Verdict:** PASS  
**Run timestamp:** 2026-03-14T22:09:19.450396+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `trajectory_wide_harm_last_quarter`: 1.2493
- `endpoint_only_harm_last_quarter`: 1.2273
- `trajectory_wide_mean_intermediate_residue_mass`: 18.1105
- `harm_tolerance_factor`: 1.05
- `path_spread_criterion_met`: True
- `harm_avoidance_criterion_met`: True

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `intermediate_weight_scheme`: linear_ramp_i_over_H