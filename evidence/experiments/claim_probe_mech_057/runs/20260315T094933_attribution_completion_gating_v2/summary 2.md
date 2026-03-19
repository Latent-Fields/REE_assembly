# attribution_completion_gating

**Claim:** MECH-057  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-15T09:49:33.165765+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `gated_agent_harm_last_quarter`: 0.8427
- `free_agent_harm_last_quarter`: 0.864
- `blind_agent_harm_last_quarter`: 0.8187
- `gated_total_harm_last_quarter`: 1.2527
- `free_total_harm_last_quarter`: 1.244
- `criterion_1_gated_vs_free_met`: False
- `criterion_2_gated_vs_blind_met`: False
- `criterion_3_total_harm_parity_met`: True
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
- `agent_harm_reduction_factor`: 0.95
- `total_harm_tolerance`: 1.1