# Experiment: claim_probe_mech_056

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-21T13:01:41Z` signatures: ledger_editing
- `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal` at `2026-02-21T13:01:41Z` signatures: ledger_editing, explanation_policy_divergence, domination_lock_in
- `2026-02-21T130141Z_claim-probe-mech-056_seed29_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-21T13:01:41Z` signatures: ledger_editing, domination_lock_in

Recurring signatures:
- `ledger_editing` occurred in 18 FAIL run(s); latest `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 12 FAIL run(s); latest `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`
- `explanation_policy_divergence` occurred in 9 FAIL run(s); latest `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (18 FAIL run(s), latest `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (12 FAIL run(s), latest `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
- [ ] Investigate signature `explanation_policy_divergence` (9 FAIL run(s), latest `2026-02-21T130141Z_claim-probe-mech-056_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
