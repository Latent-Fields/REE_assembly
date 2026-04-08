# Pending Experiment Review

Generated: `2026-04-08T05:54:39Z`  
Last review: `2026-04-07T04:30:00Z`  
Pending: **21** item(s) -- 8 PASS, 10 FAIL, 3 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_245_mech120_shy_normalisation_20260405T131647Z_v3` | 2026-04-05T13:16 | MECH-120 | — |
| `v3_exq_244_mech165_reverse_replay_diversity_20260405T132907Z_v3` | 2026-04-05T13:29 | MECH-165 | — |
| `v3_exq_235_mech112_arc030_clean_goal_gate_1775399046_v3` | 2026-04-05T14:24 | ARC-030, MECH-112 | — |
| `v3_exq_251_mech186_valence_wanting_floor_1775504875_v3` | 2026-04-06T19:47 | MECH-186 | — |
| `v3_exq_251_mech186_valence_wanting_floor_1775549211_v3` | 2026-04-07T08:06 | MECH-186 | — |
| `v3_exq_245_mech120_shy_normalisation_20260407T091221Z_v3` | 2026-04-07T09:12 | MECH-120 | — |
| `v3_exq_253_mech188_zgoal_injection_1775556946_v3` | 2026-04-07T10:15 | MECH-188 | — |
| `v3_exq_247_sd011_sd012_integration_20260407T105051Z_v3` | 2026-04-07T10:55 | ARC-030, ARC-033, SD-011, SD-012 | — |
| `v3_exq_238_20260407T125051Z_v3` | 2026-04-07T12:50 | MECH-112, SD-012 | — |
| `v3_exq_258_mech205_surprise_gated_replay_1775567619_v3` | 2026-04-07T13:13 | MECH-205 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_246_mech122_spindle_coordination_20260405T132145Z_v3` | 2026-04-05T13:21 | MECH-122 |
| `v3_exq_250_inv054_phase_transition_recovery_1775520080_v3` | 2026-04-07T00:01 | INV-054 |
| `v3_exq_249_inv053_depression_attractor_replication_1775525563_v3` | 2026-04-07T01:32 | INV-053 |
| `v3_exq_249_inv053_depression_attractor_replication_1775528989_v3` | 2026-04-07T02:29 | INV-053 |
| `v3_exq_250_inv054_phase_transition_recovery_1775541543_v3` | 2026-04-07T05:59 | INV-054 |
| `v3_exq_248_q034_threshold_sweep_1775553137_v3` | 2026-04-07T09:12 | Q-034 |
| `v3_exq_254_inv052_single_mechanism_sufficiency_1775580022_v3` | 2026-04-07T16:40 | INV-052 |
| `v3_exq_254_inv052_single_mechanism_sufficiency_1775591316_v3` | 2026-04-07T19:48 | INV-052 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-238c` | FAIL | `?` | FAIL (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-250b` | UNKNOWN | `?` | UNKNOWN |
| `V3-ONBOARD-smoke-EWIN-PC-b` | PASS | `?` | smoke run |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
