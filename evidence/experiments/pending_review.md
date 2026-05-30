# Pending Experiment Review

Generated: `2026-05-30T07:01:12Z`  
Last review: `2026-05-30T06:53:14Z`  
Pending: **2** item(s) -- 1 PASS, 0 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_612_phase3_cutover_smoke_20260529T214609Z_v3` | 2026-05-30T07:00 | (no claim tags) |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-612b` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
