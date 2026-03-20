# Pending Experiment Review

Generated: `2026-03-20T08:00:16Z`  
Last review: `2026-03-20T07:54:35.595606+00:00`  
Pending: **18** run(s) — 1 PASS, 17 FAIL

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `20260319T054938Z_v3_exq_030c_sd003_attribution_largescale_v3` | 2026-03-19T05:49 | ARC-024, MECH-071, SD-003 | — |
| `20260319T055000Z_v3_exq_032c_mech102_dense_grid_v3` | 2026-03-19T05:50 | ARC-024, MECH-102, SD-003 | — |
| `20260319T060618Z_v3_exq_036_sd003_multistep_attribution_v3` | 2026-03-19T06:06 | ARC-024, MECH-071, SD-003 | — |
| `20260319T060720Z_v3_exq_039_training_progression_v3` | 2026-03-19T06:07 | ARC-024, MECH-071 | — |
| `20260319T061623Z_v3_exq_038_arc016_precision_sweep_v3` | 2026-03-19T06:16 | ARC-016, MECH-093 | — |
| `20260319T104327Z_v3_exq_043_sd003_trajectory_attribution_v3` | 2026-03-19T10:43 | MECH-102, SD-003 | — |
| `20260319T201606Z_v3_exq_044_sd003_attribution_fixed_v3` | 2026-03-19T20:16 | MECH-102, SD-003 | — |
| `20260319T201636Z_v3_exq_045_mech102_ethical_ttype_v3` | 2026-03-19T20:16 | ARC-024, MECH-102 | — |
| `20260319T213410Z_v3_exq_047_unified_vs_split_latent_v3` | 2026-03-19T21:34 | MECH-069, SD-005 | — |
| `20260319T222723Z_v3_exq_048_mech057b_completion_gate_v3` | 2026-03-19T22:27 | MECH-057b | — |
| `20260319T233641Z_v3_exq_050_mech025_doing_mode_probe_v3` | 2026-03-19T23:36 | MECH-025 | — |
| `20260320T032058Z_v3_exq_051_q007_valence_precision_v3` | 2026-03-20T03:20 | Q-007 | — |
| `20260320T042636Z_v3_exq_052_sd006_multirate_validation_v3` | 2026-03-20T04:26 | MECH-089, SD-006 | — |
| `20260320T051926Z_v3_exq_049_mech090_beta_gate_v3` | 2026-03-20T05:19 | MECH-090 | — |
| `20260320T062233Z_v3_exq_056_sd010_harm_stream_baseline_v3` | 2026-03-20T06:22 | ARC-027, SD-010 | — |
| `20260320T062250Z_v3_exq_058_sd010_sd003_attribution_v3` | 2026-03-20T06:22 | SD-003, SD-010 | — |
| `20260320T062330Z_v3_exq_059_sd010_mech102_advantage_v3` | 2026-03-20T06:23 | MECH-102, SD-010 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `20260320T073809Z_v3_exq_053_arc018_rollout_viability_v3` | 2026-03-20T07:38 | ARC-018 |

---

## How to mark runs as reviewed

Add run IDs to `reviewed_run_ids` in `evidence/experiments/review_tracker.json`,
update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
