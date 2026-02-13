# Experiment: trajectory_integrity

## What it tests

- Whether policy execution preserves trajectory ledger integrity under replay, intervention, and post-commit updates.
- Whether explanation traces remain aligned with selected policy outcomes.

## Failure modes it detects

- ledger editing
- domination/lock-in dynamics
- explanation-policy divergence

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-13T070000Z_dummy-fail` at `2026-02-13T07:00:00Z` signatures: ledger_editing, explanation_policy_divergence, stop:ledger_edit_detected_count>0, stop:explanation_policy_divergence_rate>0.05, stop:domination_lock_in_events>0

Recurring signatures:
- `ledger_editing` occurred in 1 FAIL run(s); latest `2026-02-13T070000Z_dummy-fail`
- `explanation_policy_divergence` occurred in 1 FAIL run(s); latest `2026-02-13T070000Z_dummy-fail`
- `stop:ledger_edit_detected_count>0` occurred in 1 FAIL run(s); latest `2026-02-13T070000Z_dummy-fail`
- `stop:explanation_policy_divergence_rate>0.05` occurred in 1 FAIL run(s); latest `2026-02-13T070000Z_dummy-fail`
- `stop:domination_lock_in_events>0` occurred in 1 FAIL run(s); latest `2026-02-13T070000Z_dummy-fail`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (1 FAIL run(s), latest `2026-02-13T070000Z_dummy-fail`).
- [ ] Investigate signature `explanation_policy_divergence` (1 FAIL run(s), latest `2026-02-13T070000Z_dummy-fail`).
- [ ] Investigate signature `stop:ledger_edit_detected_count>0` (1 FAIL run(s), latest `2026-02-13T070000Z_dummy-fail`).
- [ ] Investigate signature `stop:explanation_policy_divergence_rate>0.05` (1 FAIL run(s), latest `2026-02-13T070000Z_dummy-fail`).
- [ ] Investigate signature `stop:domination_lock_in_events>0` (1 FAIL run(s), latest `2026-02-13T070000Z_dummy-fail`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
