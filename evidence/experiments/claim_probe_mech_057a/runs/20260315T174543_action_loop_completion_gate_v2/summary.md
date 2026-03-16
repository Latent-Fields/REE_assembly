# action_loop_completion_gate

**Claim:** MECH-057a  
**Verdict:** PASS  
**Run timestamp:** 2026-03-15T17:45:43.730022+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `full_harm_last_quarter`: 1.0
- `no_gate_harm_last_quarter`: 1.8
- `no_attribution_harm_last_quarter`: 1.2
- `no_gate_vs_full_ratio`: 1.8
- `no_attribution_vs_full_ratio`: 1.2
- `criterion_1_gate_met`: True
- `criterion_2_attribution_met`: True
- `criteria_met`: 2

## Config

- `num_episodes`: 5
- `max_steps`: 100
- `seeds`: [7]
- `grid_size`: 10
- `num_hazards`: 4
- `num_waypoints`: 3
- `waypoint_visit_reward`: 0.2
- `waypoint_completion_reward`: 0.8
- `sequence_commitment_timeout`: 20
- `environment`: CausalGridWorld(subgoal_mode=True)
- `e1_lr`: 0.0001
- `policy_lr`: 0.001
- `e2_lr`: 0.001
- `gate_harm_ratio_threshold`: 1.1
- `attribution_harm_ratio_threshold`: 1.05