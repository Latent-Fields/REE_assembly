# Pending Experiment Review

Generated: `2026-04-02T21:42:50Z`  
Last review: `2026-04-01T22:30:00Z`  
Pending: **13** item(s) -- 3 PASS, 9 FAIL, 1 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_071d_rollout_batched_attribution_20260401T231237Z_v3` | 2026-04-01T23:12 | ARC-024, MECH-071, SD-003 | — |
| `v3_exq_071d_rollout_batched_attribution_20260401T232311Z_v3` | 2026-04-01T23:23 | ARC-024, MECH-071, SD-003 | — |
| `v3_exq_187a_mech153_supervised_context_labeling_20260401T232546Z_v3` | 2026-04-01T23:25 | ARC-042, MECH-153 | — |
| `v3_exq_180a_arc030_benefit_eval_phased_20260401T232738Z_v3` | 2026-04-01T23:27 | ARC-030 | — |
| `v3_exq_072b_q021_behavioral_flatness_20260402T012059Z_v3` | 2026-04-02T01:20 | Q-021 | — |
| `v3_exq_073b_mech111_novelty_signal_20260402T021831Z_v3` | 2026-04-02T02:18 | MECH-111 | — |
| `v3_exq_075d_mech113_self_maintenance_20260402T032357Z_v3` | 2026-04-02T03:23 | MECH-113 | — |
| `v3_exq_084d_q022_deff_hopfield_dissociation_20260402T033313Z_v3` | 2026-04-02T03:33 | MECH-118, MECH-119, Q-022 | — |
| `v3_exq_199_mech025_doing_mode_breath_20260402T204835Z_v3` | 2026-04-02T20:48 | MECH-025 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_197_mech104_volatility_interrupt_pair_20260401T231734Z_v3` | 2026-04-01T23:17 | MECH-104 |
| `v3_exq_182a_sd015_handcrafted_goal_diagnostic_20260401T232500Z_v3` | 2026-04-01T23:25 | SD-015 |
| `v3_exq_198_sd011_dual_stream_stability_20260401T232341Z_v3` | 2026-04-02T21:09 | SD-011 |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-198` | UNKNOWN | `?` | UNKNOWN |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
