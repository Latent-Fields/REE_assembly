# Experiment: claim_probe_mech_059

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-17T225337Z_claim-probe-mech-059_seed131_explicit_uncertainty_head_toyenv_internal_minimal` at `2026-02-17T22:53:37Z` signatures: mech059:uncertainty_metric_gaming_detected
- `2026-02-17T225337Z_claim-probe-mech-059_seed101_explicit_uncertainty_head_toyenv_internal_minimal` at `2026-02-17T22:53:37Z` signatures: mech059:uncertainty_metric_gaming_detected
- `2026-02-17T225311Z_claim-probe-mech-059_seed89_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-17T22:53:11Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse

Recurring signatures:
- `mech059:uncertainty_metric_gaming_detected` occurred in 16 FAIL run(s); latest `2026-02-17T225337Z_claim-probe-mech-059_seed131_explicit_uncertainty_head_toyenv_internal_minimal`
- `mech059:abstention_reliability_collapse` occurred in 13 FAIL run(s); latest `2026-02-17T225311Z_claim-probe-mech-059_seed89_deterministic_plus_dispersion_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (16 FAIL run(s), latest `2026-02-17T225337Z_claim-probe-mech-059_seed131_explicit_uncertainty_head_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (13 FAIL run(s), latest `2026-02-17T225311Z_claim-probe-mech-059_seed89_deterministic_plus_dispersion_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
