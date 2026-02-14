# Experiment Run Summary

## Scenario
- claim_id: `MECH-059`
- experiment_type: `jepa_uncertainty_channels`
- condition: `explicit_uncertainty_head`
- run_id: `2026-02-14T030000Z_jepa-uncertainty-channels_seed11_explicit_uncertainty_head`
- timestamp_utc: `2026-02-14T03:00:00Z`
- seed: `11`
- seed_cohort: `11`, `29`

## Outcome
- status: **PASS**
- evidence_direction: `supports`

## Key Metrics
- latent_prediction_error_mean: 0.126039
- latent_uncertainty_calibration_error: 0.079123
- precision_input_completeness_rate: 0.941659
- uncertainty_coverage_rate: 0.851944

## PASS/FAIL Thresholds
- `latent_prediction_error_mean <= 0.17` (observed: `0.126039`)
- `latent_uncertainty_calibration_error <= 0.11` (observed: `0.079123`)
- `precision_input_completeness_rate >= 0.88` (observed: `0.941659`)
- `uncertainty_coverage_rate >= 0.8` (observed: `0.851944`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `supports`.
