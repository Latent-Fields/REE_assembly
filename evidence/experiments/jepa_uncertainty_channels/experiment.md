# Experiment: jepa_uncertainty_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-15T145637Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T14:56:37Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `2026-02-15T145637Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T14:56:37Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `2026-02-15T145611Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T14:56:11Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse

Recurring signatures:
- `mech059:uncertainty_metric_gaming_detected` occurred in 16 FAIL run(s); latest `2026-02-15T145637Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`
- `mech059:calibration_slope_break` occurred in 10 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`
- `mech059:abstention_reliability_collapse` occurred in 10 FAIL run(s); latest `2026-02-15T145637Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`
- `threshold:latent_prediction_error_mean` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:latent_uncertainty_calibration_error` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:precision_input_completeness_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:uncertainty_coverage_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`

Suggested design TODOs:
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (16 FAIL run(s), latest `2026-02-15T145637Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:calibration_slope_break` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (10 FAIL run(s), latest `2026-02-15T145637Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:latent_uncertainty_calibration_error` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:precision_input_completeness_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
