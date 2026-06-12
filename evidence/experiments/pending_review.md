# Pending Experiment Review

Generated: `2026-06-12T10:41:29Z`  
Last review: `2026-06-12T06:36:18Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_468c_sd034_mech268_commitment_vs_contradiction_behavioural_20260612T080105Z_v3` | 2026-06-12T08:01 | MECH-090, MECH-268, SD-034 | — |
| `v3_exq_460c_sd034_verified_but_not_released_behavioural_20260612T090021Z_v3` | 2026-06-12T09:00 | MECH-260, MECH-261, SD-034 | — |

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
