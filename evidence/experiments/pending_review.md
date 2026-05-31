# Pending Experiment Review

Generated: `2026-05-31T10:53:04Z`  
Last review: `2026-05-31T08:35:00Z`  
Pending: **2** item(s) -- 0 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_483e_sd037_consumer_cascade_4arm_20260530T195925Z_v3` | 2026-05-30T19:59 | MECH-280, MECH-281, SD-037 | — |
| `v3_exq_569e_sd056_mechanism_probe_pathway_a_vs_b_20260531T004944Z_v3` | 2026-05-31T00:49 | ARC-065, MECH-341 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
