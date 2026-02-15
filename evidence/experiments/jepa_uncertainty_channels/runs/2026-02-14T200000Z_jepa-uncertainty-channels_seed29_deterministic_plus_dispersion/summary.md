# Experiment Run Summary

## Scenario
- claim_id: `MECH-059`
- experiment_type: `jepa_uncertainty_channels`
- condition: `deterministic_plus_dispersion`
- run_id: `2026-02-14T200000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`
- timestamp_utc: `2026-02-14T20:00:00Z`
- seed: `29`
- seed_cohort: `11`, `29`, `47`

## Outcome
- status: **FAIL**
- evidence_direction: `weakens`

## Key Metrics
- latent_prediction_error_mean: 0.186996
- latent_uncertainty_calibration_error: 0.123819
- precision_input_completeness_rate: 0.833574
- uncertainty_coverage_rate: 0.720286

## PASS/FAIL Thresholds
- `latent_prediction_error_mean <= 0.17` (observed: `0.186996`)
- `latent_uncertainty_calibration_error <= 0.11` (observed: `0.123819`)
- `precision_input_completeness_rate >= 0.88` (observed: `0.833574`)
- `uncertainty_coverage_rate >= 0.8` (observed: `0.720286`)

## Interpretation
- threshold logic is explicit above for REE_assembly auditability.
- proposed evidence_direction for this run: `weakens`.
