# Pending Experiment Review

Generated: `2026-04-29T18:49:08Z`  
Last review: `2026-04-28T22:00:00Z`  
Pending: **2** item(s) -- 1 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_490c_mech269b_with_liking_bridge_20260429T055859Z_v3` | 2026-04-29T05:58 | Q-040 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_499_mech094_hypothesis_tag_writegate_discriminative_20260429T184730Z_v3` | 2026-04-29T18:47 | MECH-094 |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
