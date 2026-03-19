# control_plane_precision_separation

**Claim:** MECH-059  
**Verdict:** PASS  
**Run timestamp:** 2026-03-14T20:21:43.211016+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `merged_harm_last_quarter`: 1.2367
- `separated_harm_last_quarter`: 1.22
- `abs_corr_dispersion_pe_merged`: 0.1224
- `abs_corr_dispersion_pe_separated`: 0.2258
- `independence_threshold`: 0.3
- `signals_independent`: True
- `separation_helps`: True

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `dispersion_modulation_strength`: 0.02
- `max_dispersion_scale`: 5.0