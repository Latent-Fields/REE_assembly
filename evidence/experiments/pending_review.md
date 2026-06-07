# Pending Experiment Review

Generated: `2026-06-07T07:47:27Z`  
Last review: `2026-06-07T07:07:13Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_624b_arc068_mech320_niv_salamone_dissociation_20260607T051206Z_v3` | 2026-06-07T05:12 | ARC-068, MECH-320 | — |
| `v3_exq_614e_mech341_within_class_temperature_authority_on_20260607T070701Z_v3` | 2026-06-07T07:07 | MECH-341 | — |

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
