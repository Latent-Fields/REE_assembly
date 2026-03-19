# rollout_viability_mapping

**Claim:** ARC-018  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-15T12:58:44.288398+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `viability_mapped_harm_last_quarter`: 1.254
- `viability_fixed_harm_last_quarter`: 1.2313
- `viability_mapped_harm_slope`: -0.0174
- `viability_fixed_harm_slope`: 0.0089
- `criterion_1_slope_met`: False
- `criterion_2_harm_met`: False
- `criteria_met`: 0

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `e1_lr`: 0.0001
- `policy_lr`: 0.001
- `slope_margin`: 0.05
- `harm_factor`: 0.95