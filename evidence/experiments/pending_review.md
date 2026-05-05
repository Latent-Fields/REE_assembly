# Pending Experiment Review

Generated: `2026-05-05T22:12:13Z`  
Last review: `2026-05-05T22:04:33Z`  
Pending: **4** item(s) -- 0 PASS, 3 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_454a_arc016_adaptive_commitment_reef_20260505T184703Z_v3` | 2026-05-05T18:47 | ARC-016 | — |
| `v3_exq_452a_mech257_dual_function_e2_reef_20260505T215753Z_v3` | 2026-05-05T21:57 | ARC-033, MECH-257, SD-013 | — |
| `v3_exq_525_sd003_attribution_anchor_20260505T220444Z_v3` | 2026-05-05T22:04 | ARC-033, SD-003 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-418j` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
