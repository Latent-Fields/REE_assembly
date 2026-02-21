# Experiment Run Summary

## Scenario
- claim_id: `MECH-059`
- experiment_type: `jepa_uncertainty_channels`
- condition: `deterministic_plus_dispersion`
- run_id: `2026-02-21T151223Z_jepa-uncertainty-channels_seed11_deterministic_plus_dispersion`
- timestamp_utc: `2026-02-21T15:12:23Z`
- seed: `11`
- seed_cohort: `11`, `29`

## Outcome
- status: **FAIL**
- evidence_direction: `weakens`

## Key Metrics
- latent_prediction_error_mean: 0.171908
- latent_uncertainty_calibration_error: 0.128581
- precision_input_completeness_rate: 0.867255
- uncertainty_coverage_rate: 0.730045

## PASS/FAIL Thresholds
- `latent_prediction_error_mean <= 0.17` (observed: `0.171908`)
- `latent_uncertainty_calibration_error <= 0.11` (observed: `0.128581`)
- `precision_input_completeness_rate >= 0.88` (observed: `0.867255`)
- `uncertainty_coverage_rate >= 0.8` (observed: `0.730045`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `weakens`.
