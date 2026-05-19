# Pending Experiment Review

Generated: `2026-05-19T21:33:04Z`  
Last review: `2026-05-19T21:27:25Z`  
Pending: **1** item(s) -- 0 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_588_isef002_transient_benefit_zgoal_seeding_20260518T222457Z_v3` | 2026-05-18T22:24 | MECH-189 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
