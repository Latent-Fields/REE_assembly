# causal_grid_world_baseline

**Claim:** SD-003-prereq  
**Verdict:** PASS  
**Run timestamp:** 2026-03-15T04:44:40.670153+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `contamination_events_total`: 3888
- `agent_caused_harm_count_total`: 343
- `env_caused_harm_count_total`: 96
- `agent_fraction`: 0.7813
- `criterion_1_contamination_gt_0`: True
- `criterion_2_agent_caused_gt_0`: True
- `criterion_3_env_caused_gt_0`: True
- `criterion_4_agent_fraction_gt_threshold`: True

## Config

- `num_episodes`: 50
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 3
- `num_resources`: 5
- `environment`: CausalGridWorld
- `agent_fraction_threshold`: 0.1
- `e1_lr`: 0.0001
- `policy_lr`: 0.001