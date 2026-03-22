# Pending Experiment Review

Generated: `2026-03-22T03:49:05Z`  
Last review: `2026-03-22T01:16:12.066110+00:00`  
Pending: **5** run(s) — 1 PASS, 4 FAIL

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_038_arc016_precision_sweep_20260322T020822Z_v3` | 2026-03-22T02:08 | ARC-016, MECH-093 | — |
| `v3_exq_038_arc016_precision_sweep_20260322T020909Z_v3` | 2026-03-22T02:09 | ARC-016, MECH-093 | — |
| `v3_exq_062_mech104_surprise_gate_20260322T034449Z_v3` | 2026-03-22T03:44 | MECH-090, MECH-104 | — |
| `v3_exq_047c_sd005_info_probe_20260322T034515Z_v3` | 2026-03-22T03:45 | SD-005 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_057_sd010_reafference_isolation_20260322T014230Z_v3` | 2026-03-22T01:42 | MECH-101, SD-007, SD-010 |

---

## How to mark runs as reviewed

Add run IDs to `reviewed_run_ids` in `evidence/experiments/review_tracker.json`,
update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
