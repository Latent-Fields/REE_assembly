# Pending Experiment Review

Generated: `2026-08-01T12:26:57Z`  
Last review: `2026-07-30T19:16:11Z`  
Pending: **15** item(s) -- 4 PASS, 11 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication; 1 run(s) with a DEAD z_goal stream

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_841_mech163_q085_grain_dose_response_20260731T080537Z_v3` | 2026-07-31T08:05 | MECH-163, Q-085 | — |
| `v3_exq_845_mech180_ecological_novelty_sleep_consolidation_dose_response_20260731T235634Z_v3` | 2026-07-31T23:56 | MECH-180 | — |
| `v3_exq_836a_mech476_dose_dependent_consolidation_redesign_20260801T000533Z_v3` | 2026-08-01T00:05 | MECH-476 | — |
| `v3_exq_850_mech204_sd076_h1_f1_damping_probe_20260801T000749Z_v3` | 2026-08-01T00:48 | MECH-204, SD-076 | — |
| `v3_exq_844_mech321_r4_midexec_task_effect_20260801T013315Z_v3` | 2026-08-01T01:33 | MECH-321 | — |
| `v3_exq_836d_mech476_novelty_tagging_consolidation_redesign_20260801T030035Z_v3` | 2026-08-01T03:00 | MECH-476 | — |
| `v3_exq_850_mech204_sd076_h2_exposure_budget_probe_20260801T005937Z_v3` | 2026-08-01T03:28 | SD-076 | — |
| `v3_exq_475b_q040c_dacc_pe_weight_delta_correlation_20260801T050027Z_v3` | 2026-08-01T05:00 | Q-040 | — |
| `v3_exq_828a_inv091_cross_stream_similarity_band_null_validated_20260801T073417Z_v3` | 2026-08-01T07:34 | INV-091 | — |
| `v3_exq_851_arc062_pa_lateral_pfc_route_source_gapfanout_20260801T110851Z_v3` | 2026-08-01T11:08 | ARC-062, MECH-309 | — |
| `v3_exq_840b_mech294_theta_packet_binding_committed_action_falsifier_20260801T120516Z_v3` | 2026-08-01T12:05 | MECH-294 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_846_arc005_control_plane_channel_occupancy_attribution_20260731T205951Z_v3` | 2026-07-31T20:59 | ARC-005 |
| `v3_exq_849_q081_reach_preflight_scan_20260801T005934Z_v3` | 2026-08-01T00:59 | Q-081 |
| `v3_exq_854_sd036_gaba_tone_dose_response_20260801T062503Z_v3` | 2026-08-01T06:25 | SD-036 |
| `v3_exq_829a_mech324_rapid_reacquisition_window_isolation_fix_20260801T062510Z_v3` | 2026-08-01T06:25 | MECH-323, MECH-324 |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_850_mech204_sd076_h1_f1_damping_probe_20260801T000749Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_850_mech204_sd076_h2_exposure_budget_probe_20260801T005937Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_845_mech180_ecological_novelty_sleep_consolidation_dose_response_20260731T235634Z_v3` | FAIL | 38959 | **0** | 0.000 | live |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
