# Pending Experiment Review

Generated: `2026-03-26T22:07:40Z`  
Last review: `2026-03-25T07:00:00Z`  
Pending: **23** item(s) -- 1 PASS, 5 FAIL, 17 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_085e_mech071_drive_modulated_goal_20260326T180934Z_v3` | 2026-03-26T18:09 | INV-034, MECH-071 | — |
| `v3_exq_097_mech093_heartbeat_rate_20260326T214212Z_v3` | 2026-03-26T21:42 | MECH-093 | — |
| `v3_exq_098_mech099_three_stream_20260326T214750Z_v3` | 2026-03-26T21:47 | MECH-099 | — |
| `v3_exq_098_mech099_three_stream_20260326T214928Z_v3` | 2026-03-26T21:49 | MECH-099 | — |
| `v3_exq_099_mech098_reafference_upgrade_20260326T220544Z_v3` | 2026-03-26T22:05 | MECH-098 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_099_mech098_reafference_upgrade_20260326T220524Z_v3` | 2026-03-26T22:05 | MECH-098 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-051b` | ERROR | `?` | ERROR |
| `V3-EXQ-072` | ERROR | `?` | ERROR |
| `V3-EXQ-073` | ERROR | `?` | ERROR |
| `V3-EXQ-074` | ERROR | `?` | ERROR |
| `V3-EXQ-075` | ERROR | `?` | ERROR |
| `V3-EXQ-071b` | ERROR | `?` | ERROR |
| `V3-EXQ-074b` | ERROR | `?` | ERROR |
| `V3-EXQ-076` | ERROR | `?` | ERROR |
| `V3-EXQ-084` | ERROR | `?` | ERROR |
| `V3-EXQ-074c` | ERROR | `?` | ERROR |
| `V3-EXQ-075b` | ERROR | `?` | ERROR |
| `V3-EXQ-076b` | ERROR | `?` | ERROR |
| `V3-EXQ-084b` | ERROR | `?` | ERROR |
| `V3-EXQ-074d` | ERROR | `?` | ERROR |
| `V3-EXQ-075c` | ERROR | `?` | ERROR |
| `V3-EXQ-076c` | ERROR | `?` | ERROR |
| `V3-EXQ-084c` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
