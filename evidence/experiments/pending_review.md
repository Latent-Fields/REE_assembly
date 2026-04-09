# Pending Experiment Review

Generated: `2026-04-09T17:03:35Z`  
Last review: `2026-04-09T13:00:00Z`  
Pending: **14** item(s) -- 0 PASS, 5 FAIL, 9 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_258a_mech205_surprise_gated_replay_1775693658_v3` | 2026-04-09T00:14 | MECH-205 | — |
| `v3_exq_260_sd020_harm_surprise_pe_20260408T231126Z_v3` | 2026-04-09T06:26 | SD-011, SD-020 | — |
| `v3_exq_261_sd021_descending_pain_mod_20260408T231136Z_v3` | 2026-04-09T06:26 | SD-011, SD-021 | — |
| `v3_exq_262_mech220_harm_hub_20260408T231100Z_v3` | 2026-04-09T17:03 | MECH-220, SD-011 | — |
| `v3_exq_241b_sd011_second_source_info_gain_20260408T231939Z_v3` | 20260408T231939Z | SD-011 | — |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-262` | ERROR | `?` | ERROR |
| `V3-EXQ-260` | ERROR | `?` | ERROR |
| `V3-EXQ-261` | ERROR | `?` | ERROR |
| `V3-EXQ-262a` | ERROR | `?` | ERROR |
| `V3-EXQ-260a` | ERROR | `?` | ERROR |
| `V3-EXQ-261a` | ERROR | `?` | ERROR |
| `V3-EXQ-263` | ERROR | `?` | ERROR |
| `V3-EXQ-263a` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-241b` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
