# Pending Experiment Review

Generated: `2026-06-10T14:44:13Z`  
Last review: `2026-06-10T14:44:12Z`  
Pending: **1** item(s) -- 0 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 1 unclaimed manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| FAIL | `v3_exq_603m_scaffolded_sd054_full_curriculum_readiness_20260610T133806Z_v3` | v3_exq_603m_scaffolded_sd054_full_curriculum_readiness | V3-EXQ-603m | non_contributory |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
