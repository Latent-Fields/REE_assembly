# Pending Experiment Review

Generated: `2026-03-22T15:45:39Z`  
Last review: `2026-03-22T14:10:00Z`  
Pending: **3** item(s) -- 0 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_047d_sd005_info_probe_v2_20260322T132106Z_v3` | 2026-03-22T13:21 | SD-005 | — |
| `v3_exq_062a_mech104_surprise_gate_committed_only_20260322T134008Z_v3` | 2026-03-22T13:40 | MECH-090, MECH-104 | — |
| `v3_exq_047d_sd005_info_probe_v2_20260322T134050Z_v3` | 2026-03-22T13:40 | SD-005 | — |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
