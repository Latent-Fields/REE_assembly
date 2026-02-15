# Experiment: jepa_uncertainty_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `exp_0017_20260215T095123788473Z` at `2026-02-15T09:51:23.788473Z` signatures: none
- `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion` at `2026-02-14T20:00:00Z` signatures: threshold:latent_prediction_error_mean, threshold:latent_uncertainty_calibration_error, threshold:precision_input_completeness_rate, threshold:uncertainty_coverage_rate
- `2026-02-14T200000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion` at `2026-02-14T20:00:00Z` signatures: threshold:latent_prediction_error_mean, threshold:latent_uncertainty_calibration_error, threshold:precision_input_completeness_rate, threshold:uncertainty_coverage_rate

Recurring signatures:
- `mech059:calibration_slope_break` occurred in 10 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`
- `mech059:uncertainty_metric_gaming_detected` occurred in 10 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`
- `threshold:latent_prediction_error_mean` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:latent_uncertainty_calibration_error` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:precision_input_completeness_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `threshold:uncertainty_coverage_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`
- `mech059:abstention_reliability_collapse` occurred in 4 FAIL run(s); latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`

Suggested design TODOs:
- [ ] Investigate signature `mech059:calibration_slope_break` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:latent_uncertainty_calibration_error` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:precision_input_completeness_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:uncertainty_coverage_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
