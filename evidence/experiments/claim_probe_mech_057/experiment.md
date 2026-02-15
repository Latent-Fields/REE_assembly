# Experiment: claim_probe_mech_057

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-15T213702Z_claim-probe-mech-057_seed1003_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:37:02Z` signatures: domination_lock_in
- `2026-02-15T213650Z_claim-probe-mech-057_seed1002_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:50Z` signatures: ledger_editing, domination_lock_in
- `2026-02-15T213621Z_claim-probe-mech-057_seed1001_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:21Z` signatures: ledger_editing

Recurring signatures:
- `ledger_editing` occurred in 4 FAIL run(s); latest `2026-02-15T213650Z_claim-probe-mech-057_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 4 FAIL run(s); latest `2026-02-15T213702Z_claim-probe-mech-057_seed1003_trajectory_first_enabled_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (4 FAIL run(s), latest `2026-02-15T213650Z_claim-probe-mech-057_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (4 FAIL run(s), latest `2026-02-15T213702Z_claim-probe-mech-057_seed1003_trajectory_first_enabled_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
