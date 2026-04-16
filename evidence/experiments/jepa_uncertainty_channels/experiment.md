# Experiment: jepa_uncertainty_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `exp_0014_20260215T153519688188Z` at `2026-02-15T15:35:19.688188Z` signatures: none
- `exp_0017_20260215T095123788473Z` at `2026-02-15T09:51:23.788473Z` signatures: none
- `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z` at `2026-02-14T18:53:25.225836Z` signatures: mech059:calibration_slope_break, mech059:uncertainty_metric_gaming_detected

Recurring signatures:
- `mech059:calibration_slope_break` occurred in 10 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`
- `mech059:uncertainty_metric_gaming_detected` occurred in 10 FAIL run(s); latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`
- `mech059:abstention_reliability_collapse` occurred in 4 FAIL run(s); latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`

Suggested design TODOs:
- [ ] Investigate signature `mech059:calibration_slope_break` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (4 FAIL run(s), latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
