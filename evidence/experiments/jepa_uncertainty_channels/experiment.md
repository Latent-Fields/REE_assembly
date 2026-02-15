# Experiment: jepa_uncertainty_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-15T153621Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T15:36:21Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `2026-02-15T153621Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T15:36:21Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `exp_0014_20260215T153519688188Z` at `2026-02-15T15:35:19.688188Z` signatures: none

Recurring signatures:
- `mech059:uncertainty_metric_gaming_detected` occurred in 18 FAIL run(s); latest `2026-02-15T153621Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`
- `mech059:abstention_reliability_collapse` occurred in 12 FAIL run(s); latest `2026-02-15T153621Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`
- `mech059:calibration_slope_break` occurred in 10 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`
- `threshold:latent_prediction_error_mean` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:latent_uncertainty_calibration_error` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:precision_input_completeness_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:uncertainty_coverage_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`

Suggested design TODOs:
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (18 FAIL run(s), latest `2026-02-15T153621Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (12 FAIL run(s), latest `2026-02-15T153621Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:calibration_slope_break` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:latent_uncertainty_calibration_error` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:precision_input_completeness_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
