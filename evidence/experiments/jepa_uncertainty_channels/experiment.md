# Experiment: jepa_uncertainty_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T151442Z_jepa-uncertainty-channels_seed71_explicit_uncertainty_head_toyenv_internal_minimal` at `2026-02-21T15:14:42Z` signatures: mech059:uncertainty_metric_gaming_detected
- `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion` at `2026-02-21T15:12:23Z` signatures: threshold:latent_prediction_error_mean, threshold:latent_uncertainty_calibration_error, threshold:precision_input_completeness_rate, threshold:uncertainty_coverage_rate
- `2026-02-21T151223Z_jepa-uncertainty-channels_seed11_deterministic_plus_dispersion` at `2026-02-21T15:12:23Z` signatures: threshold:latent_prediction_error_mean, threshold:latent_uncertainty_calibration_error, threshold:precision_input_completeness_rate, threshold:uncertainty_coverage_rate

Recurring signatures:
- `mech059:uncertainty_metric_gaming_detected` occurred in 39 FAIL run(s); latest `2026-02-21T151442Z_jepa-uncertainty-channels_seed71_explicit_uncertainty_head_toyenv_internal_minimal`
- `mech059:abstention_reliability_collapse` occurred in 29 FAIL run(s); latest `2026-02-21T150650Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`
- `mech059:calibration_slope_break` occurred in 10 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`
- `threshold:latent_prediction_error_mean` occurred in 7 FAIL run(s); latest `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`
- `threshold:latent_uncertainty_calibration_error` occurred in 7 FAIL run(s); latest `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`
- `threshold:precision_input_completeness_rate` occurred in 7 FAIL run(s); latest `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`
- `threshold:uncertainty_coverage_rate` occurred in 7 FAIL run(s); latest `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`

Suggested design TODOs:
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (39 FAIL run(s), latest `2026-02-21T151442Z_jepa-uncertainty-channels_seed71_explicit_uncertainty_head_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (29 FAIL run(s), latest `2026-02-21T150650Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:calibration_slope_break` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (7 FAIL run(s), latest `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:latent_uncertainty_calibration_error` (7 FAIL run(s), latest `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:precision_input_completeness_rate` (7 FAIL run(s), latest `2026-02-21T151223Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
