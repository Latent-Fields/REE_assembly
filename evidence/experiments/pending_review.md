# Pending Experiment Review

Generated: `2026-05-11T20:02:50Z`  
Last review: `2026-05-11T17:13:06Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_550_zgoal_monostrategy_falsifier_20260511T190132Z_v3` | 2026-05-11T19:01 | MECH-269 | — |
| `v3_exq_543c_arc062_phase3_bipartite_falsifier_20260511T190246Z_v3` | 2026-05-11T19:02 | ARC-062, MECH-309 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
