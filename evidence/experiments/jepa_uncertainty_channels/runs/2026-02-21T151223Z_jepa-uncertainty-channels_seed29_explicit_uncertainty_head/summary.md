# Experiment Run Summary

## Scenario
- claim_id: `MECH-059`
- experiment_type: `jepa_uncertainty_channels`
- condition: `explicit_uncertainty_head`
- run_id: `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_explicit_uncertainty_head`
- timestamp_utc: `2026-02-21T15:12:23Z`
- seed: `29`
- seed_cohort: `11`, `29`

## Outcome
- status: **PASS**
- evidence_direction: `supports`

## Key Metrics
- latent_prediction_error_mean: 0.124824
- latent_uncertainty_calibration_error: 0.075794
- precision_input_completeness_rate: 0.923363
- uncertainty_coverage_rate: 0.871405

## PASS/FAIL Thresholds
- `latent_prediction_error_mean <= 0.17` (observed: `0.124824`)
- `latent_uncertainty_calibration_error <= 0.11` (observed: `0.075794`)
- `precision_input_completeness_rate >= 0.88` (observed: `0.923363`)
- `uncertainty_coverage_rate >= 0.8` (observed: `0.871405`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `supports`.
