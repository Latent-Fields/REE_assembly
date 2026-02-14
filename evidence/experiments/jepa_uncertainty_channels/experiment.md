# Experiment: jepa_uncertainty_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t134314578426z` at `2026-02-14T13:43:14.578626Z` signatures: mech059:calibration_slope_break, mech059:uncertainty_metric_gaming_detected
- `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59021_20260214t134314577803z` at `2026-02-14T13:43:14.578065Z` signatures: mech059:calibration_slope_break, mech059:uncertainty_metric_gaming_detected
- `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion` at `2026-02-14T03:00:00Z` signatures: threshold:latent_prediction_error_mean, threshold:latent_uncertainty_calibration_error, threshold:precision_input_completeness_rate, threshold:uncertainty_coverage_rate

Recurring signatures:
- `mech059:calibration_slope_break` occurred in 6 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t134314578426z`
- `mech059:uncertainty_metric_gaming_detected` occurred in 6 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t134314578426z`
- `mech059:abstention_reliability_collapse` occurred in 4 FAIL run(s); latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`
- `threshold:latent_prediction_error_mean` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`
- `threshold:latent_uncertainty_calibration_error` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`
- `threshold:precision_input_completeness_rate` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`
- `threshold:uncertainty_coverage_rate` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`

Suggested design TODOs:
- [ ] Investigate signature `mech059:calibration_slope_break` (6 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t134314578426z`).
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (6 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t134314578426z`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (4 FAIL run(s), latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:latent_uncertainty_calibration_error` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:precision_input_completeness_rate` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
