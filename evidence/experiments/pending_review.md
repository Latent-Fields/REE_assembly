# Pending Experiment Review

Generated: `2026-06-03T06:46:13Z`  
Last review: `2026-06-03T06:44:51Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_514l_sd049_phase3_mech229_wanting_liking_identity_20260602T170106Z_v3` | 2026-06-03T05:49 | MECH-229, MECH-230, SD-015, SD-049 | — |
| `v3_exq_610c_inv074_crystallization_necessity_20260602T191404Z_v3` | 2026-06-03T05:49 | INV-074, MECH-333, MECH-334 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
