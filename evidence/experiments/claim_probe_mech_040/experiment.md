# Experiment: claim_probe_mech_040

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-15T213634Z_claim-probe-mech-040_seed1002_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:34Z` signatures: ledger_editing, domination_lock_in
- `2026-02-15T213605Z_claim-probe-mech-040_seed1001_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:05Z` signatures: ledger_editing
- `2026-02-15T180526Z_claim-probe-mech-040_seed29_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T18:05:26Z` signatures: ledger_editing, domination_lock_in

Recurring signatures:
- `ledger_editing` occurred in 4 FAIL run(s); latest `2026-02-15T213634Z_claim-probe-mech-040_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 3 FAIL run(s); latest `2026-02-15T213634Z_claim-probe-mech-040_seed1002_trajectory_first_enabled_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (4 FAIL run(s), latest `2026-02-15T213634Z_claim-probe-mech-040_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (3 FAIL run(s), latest `2026-02-15T213634Z_claim-probe-mech-040_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
