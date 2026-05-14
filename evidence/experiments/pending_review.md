# Pending Experiment Review

Generated: `2026-05-14T06:33:09Z`  
Last review: `2026-05-14T06:32:00Z`  
Pending: **1** item(s) -- 1 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_561_arc065_diversity_stack_heartbeat_20260514T042146Z_v3` | 2026-05-14T04:21 | ARC-065, MECH-313, MECH-314, MECH-320 |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
