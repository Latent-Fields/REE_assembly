# Pending Experiment Review

Generated: `2026-08-03T10:49:16Z`  
Last review: `2026-08-02T12:05:51Z`  
Pending: **26** item(s) -- 6 PASS, 19 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 1 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication; 1 run(s) with a DEAD z_goal stream

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_848a_arc005_precision_only_decoupled_ladder_calibrated_20260802T120712Z_v3` | 2026-08-02T12:07 | ARC-005 | — |
| `v3_exq_108b_mech135_inv088_zworld_disambiguation_20260802T121643Z_v3` | 2026-08-02T12:16 | INV-088, MECH-135 | — |
| `v3_exq_870a_mech480_dacc_execution_gain_dissociation_20260802T135309Z_v3` | 2026-08-02T13:53 | MECH-480 | — |
| `v3_exq_871a_mech090_commit_latch_persistence_diagnostic_20260802T174141Z_v3` | 2026-08-02T17:41 | ARC-071, MECH-090 | — |
| `v3_exq_847a_arc062_pd_context_modeswitch_committed_class_divergence_20260802T182826Z_v3` | 2026-08-02T18:28 | (no claim tags) | — |
| `v3_exq_862a_q040c_dacc_pe_weight_delta_correlation_20260802T195935Z_v3` | 2026-08-02T19:59 | Q-040 | — |
| `v3_exq_869a_mech267_mode_conditioning_content_persistence_retest_20260802T195943Z_v3` | 2026-08-02T19:59 | MECH-267 | — |
| `v3_exq_867a_mech321_harm_aware_selection_hazard_tuned_20260802T203309Z_v3` | 2026-08-02T20:33 | MECH-321 | — |
| `v3_exq_873_mech322_sleep_replay_carveout_20260802T213319Z_v3` | 2026-08-02T21:33 | MECH-322 | — |
| `v3_exq_876_mech025_doing_mode_causal_signal_20260802T214005Z_v3` | 2026-08-02T21:40 | MECH-025 | — |
| `v3_exq_877_mech072_discriminator_gate_full_20260802T214050Z_v3` | 2026-08-02T21:40 | MECH-072 | — |
| `v3_exq_861a_mech180_mech122_spindle_content_selection_validation_20260802T215005Z_v3` | 2026-08-02T21:50 | MECH-122, MECH-180 | — |
| `v3_exq_436c_sd017_mech166_repr_confirmer_20260802T221621Z_v3` | 2026-08-02T22:16 | ARC-045, MECH-166, SD-017 | — |
| `v3_exq_874_mech467_distractor_resistance_20260802T222132Z_v3` | 2026-08-02T22:21 | MECH-467 | — |
| `v3_exq_671b_mech025b_precision_responsibility_20260803T022036Z_v3` | 2026-08-03T02:20 | MECH-025b | — |
| `v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding_20260803T022131Z_v3` | 2026-08-03T02:21 | MECH-428 | — |
| `v3_exq_878_mech332_efference_aic_dissociation_20260803T023041Z_v3` | 2026-08-03T02:30 | MECH-332 | — |
| `v3_exq_866a_inv034_q021_goal_maintenance_agency_onboarded_20260803T075813Z_v3` | 2026-08-03T07:58 | INV-034, Q-021 | — |
| `v3_exq_882_mech472_context_memorization_generalization_20260803T080441Z_v3` | 2026-08-03T08:04 | MECH-472 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_863_arc062_lateral_pfc_route_mech448_449_full_replication_20260802T121313Z_v3` | 2026-08-02T12:13 | (no claim tags) |
| `v3_exq_864a_sd076_wci_rv_trajectory_crossover_diagnostic_20260802T095052Z_v3` | 2026-08-02T14:41 | SD-076 |
| `v3_exq_872_inv087_proxy_tethering_constraint_20260802T145757Z_v3` | 2026-08-02T14:57 | INV-087 |
| `v3_exq_881_mech293_ghost_probe_seed_efficacy_20260802T151542Z_v3` | 2026-08-02T15:15 | MECH-293 |
| `v3_exq_880_arc014_simulation_mode_commitment_20260802T214058Z_v3` | 2026-08-02T21:40 | ARC-014 |
| `v3_exq_883_mech427_cross_level_subgoal_credit_20260803T022051Z_v3` | 2026-08-03T02:20 | MECH-427 |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_863_arc062_lateral_pfc_route_mech448_449_full_replication_20260802T121313Z_v3` | PASS | mixed_partial_result_needs_expert_review | **vacuous_pass** |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_861a_mech180_mech122_spindle_content_selection_validation_20260802T215005Z_v3` | FAIL | 38959 | **0** | 0.000 | live |

## Needs diagnosis (ERROR manifests -> /diagnose-errors)

These are durable ERROR-class result manifests on disk -- most commonly a runner-synthesized record for a crash-before-manifest (a script that exited non-zero before writing any manifest; incident V3-EXQ-654e). They are scoring-neutral (no claim tags) so they never weight claim confidence, but each is a real code crash that needs `/diagnose-errors` and a re-queue under a NEW letter. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs`.

| Outcome | Manifest stem | Queue ID | Machine | Summary |
|---------|---------------|----------|---------|---------|
| ERROR | `v3_v3_exq_870_runner_error_20260802T105035Z_v3` | V3-EXQ-870 | ree-cloud-4 | Non-zero exit code 1; no runner sentinel (stdout-derived 'PASS' not trusted on c |

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
