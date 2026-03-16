# selective_residue_attribution

**Claim:** MECH-072  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-15T20:57:15.002247+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `naive_mean_final_harm`: 1.2396
- `foreseeable_mean_final_harm`: 1.2396
- `oracle_mean_final_harm`: 1.2289
- `naive_mean_false_attribution_rate`: 0.2618
- `foreseeable_mean_false_attribution_rate`: 0.2618
- `oracle_mean_false_attribution_rate`: 0.0
- `naive_mean_true_attribution_rate`: 0.7382
- `foreseeable_mean_true_attribution_rate`: 0.7382
- `oracle_mean_true_attribution_rate`: 0.7334
- `criterion_1_foreseeable_reduces_false_attribution`: False
- `criterion_2_foreseeable_no_harm_regression`: True

## Config

- `num_episodes`: 300
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `num_resources`: 5
- `environment`: CausalGridWorld
- `attribution_threshold`: 0.3
- `harm_regression_tolerance`: 1.05
- `final_quartile_fraction`: 0.25
- `e1_lr`: 0.0001
- `e2_lr`: 0.001
- `policy_lr`: 0.001