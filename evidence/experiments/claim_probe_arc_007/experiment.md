# Experiment: claim_probe_arc_007

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `20260308T114644_path_memory_ablation_v2` at `2026-03-08T11:46:44.792784+00:00` signatures: v2_verdict_fail:path_memory_ablation
- `2026-02-15T213601Z_claim-probe-arc-007_seed1001_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:01Z` signatures: ledger_editing
- `2026-02-15T181023Z_claim-probe-arc-007_seed29_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T18:10:23Z` signatures: ledger_editing, domination_lock_in

Recurring signatures:
- `ledger_editing` occurred in 4 FAIL run(s); latest `2026-02-15T213601Z_claim-probe-arc-007_seed1001_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 3 FAIL run(s); latest `2026-02-15T181023Z_claim-probe-arc-007_seed29_trajectory_first_enabled_toyenv_internal_minimal`
- `v2_verdict_fail:path_memory_ablation` occurred in 1 FAIL run(s); latest `20260308T114644_path_memory_ablation_v2`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (4 FAIL run(s), latest `2026-02-15T213601Z_claim-probe-arc-007_seed1001_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (3 FAIL run(s), latest `2026-02-15T181023Z_claim-probe-arc-007_seed29_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `v2_verdict_fail:path_memory_ablation` (1 FAIL run(s), latest `20260308T114644_path_memory_ablation_v2`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
