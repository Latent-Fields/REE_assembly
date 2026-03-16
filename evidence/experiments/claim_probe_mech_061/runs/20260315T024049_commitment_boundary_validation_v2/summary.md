# commitment_boundary_validation

**Claim:** MECH-061  
**Verdict:** PASS  
**Run timestamp:** 2026-03-15T02:40:49.515478+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `with_boundary_harm_last_quarter`: 1.246
- `blended_harm_last_quarter`: 1.2307
- `mean_abs_pre_post_corr_with_boundary`: 0.0721
- `corr_threshold`: 0.7
- `harm_tolerance_factor`: 1.05
- `distinct_signals_criterion_met`: True
- `boundary_helps_criterion_met`: True

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `blend_alpha`: 0.5
- `e1_lr`: 0.0001
- `policy_lr`: 0.001