# Pending Experiment Review

Generated: `2026-05-01T20:17:03Z`  
Last review: `2026-04-30T20:50:54Z`  
Pending: **2** item(s) -- 1 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_490e_mech295_seeding_strengthening_20260430T220232Z_v3` | 2026-04-30T22:02 | Q-040 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_503_sd017_sleep_phase_discriminative_20260501T201518Z_v3` | 2026-05-01T20:15 | SD-017 |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
