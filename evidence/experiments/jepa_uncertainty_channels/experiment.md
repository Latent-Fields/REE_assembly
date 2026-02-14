# Experiment: jepa_uncertainty_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z` at `2026-02-13T23:14:15.719958Z` signatures: mech059:calibration_slope_break, mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `mech_059_ambiguity_fog_dispersion_s59011_20260213t231415719237z` at `2026-02-13T23:14:15.719429Z` signatures: mech059:calibration_slope_break, mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `mech_059_ood_noise_burst_ensemble_s59012_20260213t231415718729z` at `2026-02-13T23:14:15.718916Z` signatures: mech059:calibration_slope_break, mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse

Recurring signatures:
- `mech059:calibration_slope_break` occurred in 4 FAIL run(s); latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`
- `mech059:uncertainty_metric_gaming_detected` occurred in 4 FAIL run(s); latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`
- `mech059:abstention_reliability_collapse` occurred in 4 FAIL run(s); latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`

Suggested design TODOs:
- [ ] Investigate signature `mech059:calibration_slope_break` (4 FAIL run(s), latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`).
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (4 FAIL run(s), latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (4 FAIL run(s), latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
