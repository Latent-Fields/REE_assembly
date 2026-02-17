# Experiment: claim_probe_q_009

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `exp_0015_20260217T180028221014Z` at `2026-02-17T18:00:28.221014Z` signatures: none
- `2026-02-15T213648Z_claim-probe-q-009_seed1002_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:48Z` signatures: ledger_editing, domination_lock_in
- `2026-02-15T213619Z_claim-probe-q-009_seed1001_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:19Z` signatures: ledger_editing

Recurring signatures:
- `ledger_editing` occurred in 4 FAIL run(s); latest `2026-02-15T213648Z_claim-probe-q-009_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 3 FAIL run(s); latest `2026-02-15T213648Z_claim-probe-q-009_seed1002_trajectory_first_enabled_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (4 FAIL run(s), latest `2026-02-15T213648Z_claim-probe-q-009_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (3 FAIL run(s), latest `2026-02-15T213648Z_claim-probe-q-009_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
