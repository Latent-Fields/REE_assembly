# Pending Experiment Review

Generated: `2026-06-02T05:52:02Z`  
Last review: `2026-06-02T05:23:00Z`  
Pending: **1** item(s) -- 0 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_592f_mech090_commitment_state_transition_probe_20260601T194325Z_v3` | 2026-06-01T19:43 | MECH-090 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
