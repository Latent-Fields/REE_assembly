# Pending Experiment Review

Generated: `2026-03-20T19:49:41Z`  
Last review: `2026-03-20T14:18:01.555870+00:00`  
Pending: **8** run(s) — 1 PASS, 7 FAIL

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `20260320T155338Z_v3_exq_056_sd010_harm_stream_baseline_v3` | 2026-03-20T15:53 | ARC-027, SD-010 | — |
| `20260320T155354Z_v3_exq_058_sd010_sd003_attribution_v3` | 2026-03-20T15:53 | SD-003, SD-010 | — |
| `20260320T155429Z_v3_exq_059_sd010_mech102_advantage_v3` | 2026-03-20T15:54 | MECH-102, SD-010 | — |
| `20260320T165149Z_v3_exq_020_event_contrastive_v3` | 2026-03-20T16:51 | MECH-100, SD-003, SD-009 | — |
| `20260320T171130Z_v3_exq_022_combined_contrastive_lstsq_v3` | 2026-03-20T17:11 | MECH-098, MECH-100, SD-003, SD-007 | — |
| `20260320T172009Z_v3_exq_018_arc016_dynamic_precision_v3` | 2026-03-20T17:20 | ARC-016 | — |
| `20260320T180545Z_v3_exq_054_mech072_world_delta_gating_v3` | 2026-03-20T18:05 | MECH-072 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `20260320T191345Z_v3_exq_055_mech033_kernel_chaining_v3` | 2026-03-20T19:13 | MECH-033 |

---

## How to mark runs as reviewed

Add run IDs to `reviewed_run_ids` in `evidence/experiments/review_tracker.json`,
update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
