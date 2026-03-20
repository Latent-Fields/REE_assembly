# Experiment: claim_probe_q_007

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `20260320T032058Z_v3_exq_051_q007_valence_precision_v3` at `2026-03-20T03:20:58Z` signatures: none
- `20260315T150155_valence_regime_correlation_v2` at `2026-03-15T15:01:55.006956+00:00` signatures: v2_verdict_fail:valence_regime_correlation
- `2026-02-15T213646Z_claim-probe-q-007_seed1002_trajectory_first_enabled_toyenv_internal_minimal` at `2026-02-15T21:36:46Z` signatures: ledger_editing, domination_lock_in

Recurring signatures:
- `ledger_editing` occurred in 4 FAIL run(s); latest `2026-02-15T213646Z_claim-probe-q-007_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `domination_lock_in` occurred in 3 FAIL run(s); latest `2026-02-15T213646Z_claim-probe-q-007_seed1002_trajectory_first_enabled_toyenv_internal_minimal`
- `v2_verdict_fail:valence_regime_correlation` occurred in 1 FAIL run(s); latest `20260315T150155_valence_regime_correlation_v2`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (4 FAIL run(s), latest `2026-02-15T213646Z_claim-probe-q-007_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (3 FAIL run(s), latest `2026-02-15T213646Z_claim-probe-q-007_seed1002_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `v2_verdict_fail:valence_regime_correlation` (1 FAIL run(s), latest `20260315T150155_valence_regime_correlation_v2`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
