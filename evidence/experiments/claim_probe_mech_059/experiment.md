# Experiment: claim_probe_mech_059

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-15T213803Z_claim-probe-mech-059_seed1008_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T21:38:03Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `2026-02-15T213751Z_claim-probe-mech-059_seed1007_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T21:37:51Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `2026-02-15T213739Z_claim-probe-mech-059_seed1006_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-15T21:37:39Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse

Recurring signatures:
- `mech059:uncertainty_metric_gaming_detected` occurred in 8 FAIL run(s); latest `2026-02-15T213803Z_claim-probe-mech-059_seed1008_deterministic_plus_dispersion_toyenv_internal_minimal`
- `mech059:abstention_reliability_collapse` occurred in 8 FAIL run(s); latest `2026-02-15T213803Z_claim-probe-mech-059_seed1008_deterministic_plus_dispersion_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (8 FAIL run(s), latest `2026-02-15T213803Z_claim-probe-mech-059_seed1008_deterministic_plus_dispersion_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (8 FAIL run(s), latest `2026-02-15T213803Z_claim-probe-mech-059_seed1008_deterministic_plus_dispersion_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
