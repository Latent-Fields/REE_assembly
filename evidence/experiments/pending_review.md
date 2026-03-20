# Pending Experiment Review

Generated: `2026-03-20T22:08:32Z`  
Last review: `2026-03-20T19:30:00.000000+00:00`  
Pending: **6** run(s) — 4 PASS, 2 FAIL

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_058c_sd010_sd003_attribution_fixed_20260320T212335Z_v3` | 2026-03-20T21:23 | SD-003, SD-010 | — |
| `20260320T204910Z_v3_exq_059_arc016_beta_gate_fixed_threshold_v3` | 2026-03-20T21:45 | ARC-016, MECH-057b, MECH-090 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_031_arc016_gradient_world_20260318T201853Z_v3` | 2026-03-18T20:18 | ARC-016 |
| `v3_exq_034_arc025_engine_ablation_20260318T202555Z_v3` | 2026-03-18T20:25 | ARC-025, MECH-071, SD-003 |
| `v3_exq_018b_arc016_relative_threshold_20260320T193340Z_v3` | 2026-03-20T19:33 | ARC-016 |
| `20260320T200725Z_v3_exq_058_arc027_harm_stream_calibration_v3` | 2026-03-20T21:45 | ARC-027, MECH-071, SD-010 |

---

## How to mark runs as reviewed

Add run IDs to `reviewed_run_ids` in `evidence/experiments/review_tracker.json`,
update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
