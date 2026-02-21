# Experiment: claim_probe_mech_056

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T151442Z_claim-probe-mech-056_seed71_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-21T15:14:42Z` signatures: ledger_editing
- `2026-02-21T151442Z_claim-probe-mech-056_seed53_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-21T15:14:42Z` signatures: ledger_editing
- `2026-02-21T150649Z_claim-probe-mech-056_seed47_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-21T15:06:49Z` signatures: ledger_editing

Recurring signatures:
- `ledger_editing` occurred in 25 FAIL run(s); latest `2026-02-21T151442Z_claim-probe-mech-056_seed71_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 16 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`
- `explanation_policy_divergence` occurred in 12 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (25 FAIL run(s), latest `2026-02-21T151442Z_claim-probe-mech-056_seed71_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (16 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
- [ ] Investigate signature `explanation_policy_divergence` (12 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
