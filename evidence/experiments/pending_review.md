# Pending Experiment Review

Generated: `2026-05-16T17:32:59Z`  
Last review: `2026-05-15T21:22:39Z`  
Pending: **14** item(s) -- 8 PASS, 6 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_569_wpb_matched_entropy_sweep_20260516T003830Z_v3` | 2026-05-16T00:38 | ARC-065 | — |
| `v3_exq_572_intervention_a_dual_attractor_20260516T063719Z_v3` | 2026-05-16T06:37 | ARC-065 | — |
| `v3_exq_572_intervention_a_dual_attractor_20260516T063813Z_v3` | 2026-05-16T06:38 | ARC-065 | — |
| `v3_exq_572_intervention_a_dual_attractor_20260516T064121Z_v3` | 2026-05-16T06:41 | ARC-065 | — |
| `v3_exq_573_arc065_bias_scale_sweep_20260516T083605Z_v3` | 2026-05-16T08:36 | ARC-065, MECH-313, MECH-314, MECH-320 | — |
| `v3_exq_572_intervention_a_dual_attractor_20260516T095117Z_v3` | 2026-05-16T09:51 | ARC-065 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_567_wpb_natural_entropy_sp_cem_20260515T212425Z_v3` | 2026-05-15T21:24 | ARC-065 |
| `v3_exq_570_e2_rollout_collapse_diagnostic_20260515T233019Z_v3` | 2026-05-15T23:30 | ARC-065 |
| `v3_exq_540g_mech307_criterion_fix_20260515T233121Z_v3` | 2026-05-15T23:31 | MECH-295, MECH-307 |
| `v3_exq_570_e2_rollout_collapse_diagnostic_20260515T233240Z_v3` | 2026-05-15T23:32 | ARC-065 |
| `v3_exq_570_e2_rollout_collapse_diagnostic_20260515T233308Z_v3` | 2026-05-15T23:33 | ARC-065 |
| `v3_exq_571_e3_score_variance_decomp_20260515T234624Z_v3` | 2026-05-15T23:46 | ARC-065, MECH-313, MECH-314, MECH-320 |
| `v3_exq_571_e3_score_variance_decomp_20260516T004017Z_v3` | 2026-05-16T00:40 | ARC-065, MECH-313, MECH-314, MECH-320 |
| `v3_exq_574_mech273_self_model_aggregator_validation_20260516T105859Z_v3` | 2026-05-16T10:58 | MECH-273 |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
