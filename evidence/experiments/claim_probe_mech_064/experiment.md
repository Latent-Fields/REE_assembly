# Experiment: claim_probe_mech_064

## What it tests

- Whether typed authority boundaries enforce `EXTERNAL -> {OBS, INS}` and reject `EXTERNAL -> {POL, ID, CAPS}` writes.
- Whether tool outputs remain observational by default unless elevated through trusted capability checks.
- Whether privileged commits are denied when verifier checks fail or authority metadata does not match trusted channels.

## Failure modes it detects

- `type_boundary_bypass`
- `authority_label_spoof_acceptance`
- `policy_store_write_from_external`
- `identity_store_write_from_external`
- `capability_escalation_without_verifier`
- `unverified_privileged_commit`

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
No recent FAIL runs. Keep monitoring key stop metrics.
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
