# Pending Experiment Review

Generated: `2026-03-22T13:08:08Z`  
Last review: `2026-03-22T13:07:41Z`  
Pending: **3** item(s) -- 2 PASS, 0 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_057_sd010_reafference_isolation_20260322T014230Z_v3` | 2026-03-22T01:42 | MECH-101, SD-007, SD-010 |
| `v3_onboard_smoke_Daniel_PC_20260322T114824Z_v3` | 2026-03-22T11:48 | onboarding |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-046b` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
