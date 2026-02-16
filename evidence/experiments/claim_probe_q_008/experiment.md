# Experiment: claim_probe_q_008

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `exp_0015_20260216T150514802604Z` at `2026-02-16T15:05:14.802604Z` signatures: none
- `2026-02-15T213647Z_claim-probe-q-008_seed1002_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:47Z` signatures: ledger_editing, domination_lock_in
- `2026-02-15T213618Z_claim-probe-q-008_seed1001_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:18Z` signatures: ledger_editing

Recurring signatures:
- `ledger_editing` occurred in 4 FAIL run(s); latest `2026-02-15T213647Z_claim-probe-q-008_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 3 FAIL run(s); latest `2026-02-15T213647Z_claim-probe-q-008_seed1002_trajectory_first_enabled_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (4 FAIL run(s), latest `2026-02-15T213647Z_claim-probe-q-008_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (3 FAIL run(s), latest `2026-02-15T213647Z_claim-probe-q-008_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
