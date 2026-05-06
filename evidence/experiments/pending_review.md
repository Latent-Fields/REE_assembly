# Pending Experiment Review

Generated: `2026-05-06T04:19:28Z`  
Last review: `2026-05-05T22:04:33Z`  
Pending: **13** item(s) -- 1 PASS, 7 FAIL, 5 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_452a_mech257_dual_function_e2_reef_20260505T184639Z_v3` | 2026-05-05T18:46 | ARC-033, MECH-257, SD-013 | — |
| `v3_exq_454a_arc016_adaptive_commitment_reef_20260505T184703Z_v3` | 2026-05-05T18:47 | ARC-016 | — |
| `v3_exq_452a_mech257_dual_function_e2_reef_20260505T215753Z_v3` | 2026-05-05T21:57 | ARC-033, MECH-257, SD-013 | — |
| `v3_exq_525_sd003_attribution_anchor_20260505T220444Z_v3` | 2026-05-05T22:04 | ARC-033, SD-003 | — |
| `v3_exq_445g_sd032b_dacc_reef_20260505T223845Z_v3` | 2026-05-05T22:38 | MECH-258, MECH-260, SD-032b | — |
| `v3_exq_517b_mech302_relief_completion_discriminative_pair_20260506T013515Z_v3` | 2026-05-06T01:35 | MECH-302 | — |
| `20260505T223834Z_v3` | 2026-05-06T04:19 | SD-016 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_418f_sd016_attention_uniformity_probe_20260428T211430Z_v3` | 2026-04-28T21:14 | SD-016 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-418k` | UNKNOWN | `?` | UNKNOWN (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-445g` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-514d` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-517b` | UNKNOWN | `?` | UNKNOWN |
| `V3-EXQ-418j` | ERROR | `?` | ERROR |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
