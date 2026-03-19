# write_locus_contamination

**Claim:** MECH-060  
**Verdict:** PASS  
**Run timestamp:** 2026-03-14T23:59:33.224038+00:00  
**Substrate:** ree-v2  

## Aggregate Results

- `full_last_quarter_harm`: 1.2447
- `contaminated_durable_last_quarter_harm`: 1.224
- `contaminated_residue_last_quarter_harm`: 1.2087
- `full_total_residue`: 247.7667
- `contaminated_residue_total_residue`: 2535.5296
- `full_abs_attr_corr`: 0.0641
- `contaminated_durable_abs_attr_corr`: 0.0714
- `contaminated_residue_abs_attr_corr`: 0.1591
- `residue_criterion_factor`: 1.1
- `harm_tolerance_factor`: 1.05
- `residue_criterion_met`: True
- `harm_criterion_met`: True

## Config

- `num_episodes`: 200
- `max_steps`: 100
- `seeds`: [7, 42, 99]
- `grid_size`: 10
- `num_hazards`: 4
- `environment`: CausalGridWorld
- `contam_e1_weight`: 3.0
- `residue_criterion_factor`: 1.1
- `harm_tolerance_factor`: 1.05
- `e1_lr`: 0.0001
- `policy_lr`: 0.001