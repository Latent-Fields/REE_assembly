# Experiment: claim_probe_mech_065

## What it tests

- Whether the reality-coherence lane emits `RC_conflict` on provenance/authority/identity mismatch scenarios.
- Whether elevated `RC_conflict` dampens associative/motor loop lock-in signals and raises commitment thresholds.
- Whether nociceptive and veto pathways are up-weighted under high `RC_conflict` before execution commitment.

## Failure modes it detects

- `rc_conflict_miss_on_authority_mismatch`
- `rc_conflict_miss_on_identity_drift`
- `da_lock_in_under_high_rc`
- `motor_commit_without_rc_clearance`
- `nociceptive_veto_not_elevated_by_rc`
- `rc_false_positive_chronic_suppression`

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
No recent FAIL runs. Keep monitoring key stop metrics.
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
