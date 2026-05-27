# Pending Experiment Review

Generated: `2026-05-27T04:20:02Z`  
Last review: `2026-05-26T23:08:08Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_543l_arc062_mode_separation_gap_b_falsifier_20260526T023059Z_v3` | 2026-05-26T02:30 | ARC-062, INV-074, MECH-309, MECH-334 | — |
| `v3_exq_591_isef005_curriculum_vs_flat_20260526T184231Z_v3` | 2026-05-26T18:42 | ARC-046 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
