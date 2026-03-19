# valence_regime_correlation

**Claim:** Q-007  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-15T15:01:55.006956+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `rich_mean_health`: 0.7311
- `sparse_mean_health`: 0.6996
- `rich_mean_precision`: 0.5
- `sparse_mean_precision`: 0.5
- `rich_valence_precision_corr`: 0.0
- `criterion_1_corr_met`: False
- `criterion_2_precision_delta_met`: False
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
- `resource_rich_count`: 10
- `resource_sparse_count`: 1
- `corr_threshold`: 0.1
- `precision_delta`: 0.1