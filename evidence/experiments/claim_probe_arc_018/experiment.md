# Experiment: claim_probe_arc_018

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `20260315T125844_rollout_viability_mapping_v2` at `2026-03-15T12:58:44.288398+00:00` signatures: v2_verdict_fail:rollout_viability_mapping
- `2026-02-15T213637Z_claim-probe-arc-018_seed1002_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:37Z` signatures: ledger_editing, domination_lock_in
- `2026-02-15T213608Z_claim-probe-arc-018_seed1001_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:08Z` signatures: ledger_editing

Recurring signatures:
- `ledger_editing` occurred in 4 FAIL run(s); latest `2026-02-15T213637Z_claim-probe-arc-018_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 3 FAIL run(s); latest `2026-02-15T213637Z_claim-probe-arc-018_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `v2_verdict_fail:rollout_viability_mapping` occurred in 1 FAIL run(s); latest `20260315T125844_rollout_viability_mapping_v2`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (4 FAIL run(s), latest `2026-02-15T213637Z_claim-probe-arc-018_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (3 FAIL run(s), latest `2026-02-15T213637Z_claim-probe-arc-018_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `v2_verdict_fail:rollout_viability_mapping` (1 FAIL run(s), latest `20260315T125844_rollout_viability_mapping_v2`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
