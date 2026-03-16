# kernel_chaining_interface

**Claim:** MECH-033  
**Verdict:** FAIL  
**Run timestamp:** 2026-03-15T16:59:27.955457+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `with_chain_harm_last_quarter`: 1.23
- `no_chain_harm_last_quarter`: 1.2527
- `with_chain_slope`: 0.0027
- `no_chain_slope`: 0.0126
- `criterion_1_harm_met`: False
- `criterion_2_slope_met`: False
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
- `harm_factor`: 0.9
- `slope_margin`: 0.05