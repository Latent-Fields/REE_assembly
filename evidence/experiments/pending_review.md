# Pending Experiment Review

Generated: `2026-08-09T05:12:04Z`  
Last review: `2026-08-08T08:32:29Z`  
Pending: **23** item(s) -- 7 PASS, 15 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 1 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication; 3 diagnostic run(s) with no confirmed autopsy; 1 run(s) with a DEAD z_goal stream

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_897_sd009_event_ce_ablation_decodability_20260808T100554Z_v3` | 2026-08-08T10:05 | SD-009 | — |
| `v3_exq_894a_mech074d_bla_remap_attribution_selectivity_20260808T101157Z_v3` | 2026-08-08T10:11 | MECH-074d | — |
| `v3_exq_898_sd016_lega_encoder_fix_retest_20260808T101631Z_v3` | 2026-08-08T10:16 | (no claim tags) | — |
| `v3_exq_901_inv051_mel_dose_rigidity_sweep_20260808T152754Z_v3` | 2026-08-08T15:27 | INV-051 | — |
| `v3_exq_821b_mech457_consummation_binding_20260808T161718Z_v3` | 2026-08-08T16:17 | MECH-457 | — |
| `v3_exq_812a_mech295_cue_authority_sd054_20260808T185904Z_v3` | 2026-08-08T18:59 | (no claim tags) | — |
| `v3_exq_878a_mech332_commitment_calibration_20260808T193223Z_v3` | 2026-08-08T19:32 | MECH-332, SD-021, SD-032c | — |
| `v3_exq_866c_inv034_q021_goal_maintenance_agency_onboarded_20260808T195345Z_v3` | 2026-08-08T19:53 | INV-034, Q-021 | — |
| `v3_exq_899_arc030_mech307_g0_readiness_20260808T214833Z_v3` | 2026-08-08T21:48 | (no claim tags) | — |
| `v3_exq_903_mech075_ventral_vta_rpe_probe_20260808T222748Z_v3` | 2026-08-08T22:27 | MECH-075 | — |
| `v3_exq_603r_instrumental_avoidance_combined_fix_retest_20260808T230931Z_v3` | 2026-08-08T23:09 | MECH-357 | — |
| `v3_exq_905_mech075_dorsal_lc_arousal_probe_20260808T232406Z_v3` | 2026-08-08T23:24 | MECH-075 | — |
| `v3_exq_902_sd048_default_scale_calibration_sweep_20260809T002118Z_v3` | 2026-08-09T00:21 | SD-048 | — |
| `v3_exq_190a_mech022_hypothesis_injection_probe_wellpowered_20260809T002451Z_v3` | 2026-08-09T00:24 | MECH-022 | — |
| `v3_exq_228b_arc032_theta_bypass_onboarded_20260809T030541Z_v3` | 2026-08-09T03:05 | ARC-032 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_887b_sd014_node_valence_repfunc_sensitized_20260808T095101Z_v3` | 2026-08-08T09:51 | SD-014 |
| `v3_exq_900_sd024_da_cluster_allocation_representational_functional_20260808T103846Z_v3` | 2026-08-08T10:38 | SD-024 |
| `v3_exq_896_mech322_replay_confirmatory_evidence_20260808T170954Z_v3` | 2026-08-08T17:09 | MECH-322 |
| `v3_exq_703a_mech276_scientist_attribution_readiness_20260808T191524Z_v3` | 2026-08-08T19:15 | (no claim tags) |
| `v3_exq_904_arc070_decomposition_trigger_selectivity_20260808T201150Z_v3` | 2026-08-08T20:11 | ARC-070 |
| `v3_exq_244b_mech165_replay_diversity_validation_v3` | 2026-08-09T00:20 | MECH-165 |
| `v3_exq_906_full_stack_observational_fishtank_20260809T003857Z_v3` | 2026-08-09T00:38 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_812a_mech295_cue_authority_sd054_20260808T185904Z_v3` | FAIL | INVALID_HARNESS | **precondition_unmet** |
| `v3_exq_906_full_stack_observational_fishtank_20260809T003857Z_v3` | PASS | full_stack_observational_showcase_live | **vacuous_pass** |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_899_arc030_mech307_g0_readiness_20260808T214833Z_v3` | FAIL | readiness_fail_curriculum_gate_blocks_retest |
| `v3_exq_244b_mech165_replay_diversity_validation_v3` | PASS | balanced_replay_improves_retention |
| `v3_exq_906_full_stack_observational_fishtank_20260809T003857Z_v3` | PASS | full_stack_observational_showcase_live |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_901_inv051_mel_dose_rigidity_sweep_20260808T152754Z_v3` | FAIL | 48576 | **0** | 0.000 | live |

## Needs diagnosis (ERROR manifests -> /diagnose-errors)

These are durable ERROR-class result manifests on disk -- most commonly a runner-synthesized record for a crash-before-manifest (a script that exited non-zero before writing any manifest; incident V3-EXQ-654e). They are scoring-neutral (no claim tags) so they never weight claim confidence, but each is a real code crash that needs `/diagnose-errors` and a re-queue under a NEW letter. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs`.

| Outcome | Manifest stem | Queue ID | Machine | Summary |
|---------|---------------|----------|---------|---------|
| ERROR | `v3_v3_exq_821a_runner_error_20260808T111711Z_v3` | V3-EXQ-821a | ree-cloud-3 | Non-zero exit code 1; no runner sentinel (stdout-derived 'FAIL' not trusted on c |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Diagnostic (`experiment_purpose: "diagnostic"`), no confirmed autopsy: ALL diagnostic PASS/FAIL results require a confirmed `/failure-autopsy` target before governance marks them reviewed -- not only ones the indexer flagged untrustworthy. Run `/failure-autopsy` (accepts a PASS target too), then mark reviewed once confirmed.
- Reviewed FAIL with no confirmed autopsy (blind-spot net): a claim-tagged, non-diagnostic FAIL that is already `reviewed` but was never autopsied. Run `/failure-autopsy` on it; the row clears automatically once a CONFIRMED autopsy target covers the run_id. Do NOT re-mark it reviewed to silence it (it is already reviewed -- that is the blind spot). Legacy such runs are grandfathered in `fail_autopsy_grandfather.json` and never listed; do not hand-edit that file.
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
