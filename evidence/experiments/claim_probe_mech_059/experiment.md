# Experiment: claim_probe_mech_059

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T151442Z_claim-probe-mech-059_seed71_explicit_uncertainty_head_toyenv_internal_minimal` at `2026-02-21T15:14:42Z` signatures: mech059:uncertainty_metric_gaming_detected
- `2026-02-21T150649Z_claim-probe-mech-059_seed47_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-21T15:06:49Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse
- `2026-02-21T150649Z_claim-probe-mech-059_seed29_deterministic_plus_dispersion_toyenv_internal_minimal` at `2026-02-21T15:06:49Z` signatures: mech059:uncertainty_metric_gaming_detected, mech059:abstention_reliability_collapse

Recurring signatures:
- `mech059:uncertainty_metric_gaming_detected` occurred in 21 FAIL run(s); latest `2026-02-21T151442Z_claim-probe-mech-059_seed71_explicit_uncertainty_head_toyenv_internal_minimal`
- `mech059:abstention_reliability_collapse` occurred in 17 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-059_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (21 FAIL run(s), latest `2026-02-21T151442Z_claim-probe-mech-059_seed71_explicit_uncertainty_head_toyenv_internal_minimal`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (17 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-059_seed47_deterministic_plus_dispersion_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
