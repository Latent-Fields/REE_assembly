# path_memory_ablation

**Claim:** ARC-007  
**Verdict:** PASS  
**Run timestamp:** 2026-03-16T06:19:08.594368+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `memory_agent_harm_last_quarter`: 0.8747
- `ablated_agent_harm_last_quarter`: 0.9413
- `memory_total_harm_last_quarter`: 1.228
- `ablated_total_harm_last_quarter`: 1.2313
- `criterion_1_agent_harm_met`: True
- `criterion_2_total_harm_met`: True
- `criteria_met`: 2

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `e1_lr`: 0.0001
- `policy_lr`: 0.001
- `path_memory_obs_slice`: [252, 278]
- `agent_harm_factor`: 0.95
- `total_harm_ceiling`: 1.05