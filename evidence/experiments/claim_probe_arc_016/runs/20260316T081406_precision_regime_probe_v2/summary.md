# precision_regime_probe

**Claim:** ARC-016  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-16T08:14:06.998592+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `high_mean_precision`: 1.9975
- `low_mean_precision`: 0.3
- `precision_gap_observed`: 1.6975
- `high_commit_rate_last_quarter`: 1.0
- `low_commit_rate_last_quarter`: 0.0
- `high_harm_last_quarter`: 1.2387
- `low_harm_last_quarter`: 1.2467
- `criterion_1_precision_gap_met`: True
- `criterion_2_behavioral_distinction_met`: False
- `criteria_met`: 1

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `e1_lr`: 0.0001
- `policy_lr`: 0.001
- `high_precision_max`: 2.0
- `high_precision_min`: 1.0
- `low_precision_max`: 0.5
- `low_precision_min`: 0.1
- `precision_gap`: 0.3
- `commit_rate_margin`: 0.05
- `harm_factor`: 0.95