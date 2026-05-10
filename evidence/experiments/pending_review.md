# Pending Experiment Review

Generated: `2026-05-10T12:14:11Z`  
Last review: `2026-05-10T12:13:00Z`  
Pending: **3** item(s) -- 3 PASS, 0 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_500a_sd017_sleep_phase_readiness_phase2_20260509T204158Z_v3` | 2026-05-09T20:41 | SD-017 |
| `v3_exq_543_arc062_phase2a_monomodal_collapse_falsifier_20260509T214517Z_v3` | 2026-05-09T21:45 | ARC-062, MECH-309, SD-029 |
| `v3_exq_503a_sd017_sleep_phase_discriminative_phase2_20260509T214628Z_v3` | 2026-05-09T21:46 | SD-017 |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
