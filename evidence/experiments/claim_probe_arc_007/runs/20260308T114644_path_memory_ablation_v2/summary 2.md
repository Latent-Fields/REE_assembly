# path_memory_ablation

**Claim:** ARC-007  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-08T11:46:44.792784+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `memory_agent_harm_last_quarter`: 0.896
- `ablated_agent_harm_last_quarter`: 0.912
- `memory_total_harm_last_quarter`: 1.2093
- `ablated_total_harm_last_quarter`: 1.212
- `criterion_1_agent_harm_met`: False
- `criterion_2_total_harm_met`: True
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
- `path_memory_obs_slice`: [252, 278]
- `agent_harm_factor`: 0.95
- `total_harm_ceiling`: 1.05