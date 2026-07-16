# Pending Experiment Review

Generated: `2026-07-16T15:39:51Z`  
Last review: `2026-07-16T15:39:34Z`  
Pending: **2** item(s) -- 0 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 2 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| PASS | `v3_exq_767_sd025_curiosity_drive_selection_bias_20260716T073159Z_v3` | v3_exq_767_sd025_curiosity_drive_selection_bias | V3-EXQ-767 | supports |
| FAIL | `v3_exq_765_mech457_bootstrap_explorer_competence_20260716T122726Z_v3` | v3_exq_765_mech457_bootstrap_explorer_competence | V3-EXQ-765 | unknown |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
