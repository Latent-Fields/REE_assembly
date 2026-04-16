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
- `exp_0004_20260215T173859619527Z` at `2026-02-15T17:38:59.619527Z` signatures: none
- `exp_0011_20260215T153519572504Z` at `2026-02-15T15:35:19.572504Z` signatures: none

Recurring signatures:

Suggested design TODOs:
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
