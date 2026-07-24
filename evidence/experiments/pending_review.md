# Pending Experiment Review

Generated: `2026-07-24T16:22:12Z`  
Last review: `2026-07-24T08:05:35Z`  
Pending: **30** item(s) -- 6 PASS, 24 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 7 diagnostic self-route(s) flagged for adjudication; 1 run(s) with recorded (non-gating) preconditions

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_734_env_difficulty_competence_recovery_sweep_20260722T202649Z_v3` | 2026-07-22T20:26 | (no claim tags) | — |
| `v3_exq_802_arc005_control_plane_routing_double_dissociation_20260722T212125Z_v3` | 2026-07-22T21:21 | ARC-005 | — |
| `v3_exq_669c_mech329_wanting_first_goal_seeding_20260722T214724Z_v3` | 2026-07-22T21:47 | MECH-189, MECH-329 | — |
| `v3_exq_811_mech477_dualsystem_arbitration_falsifier_20260723T054309Z_v3` | 2026-07-23T05:43 | MECH-163, MECH-477 | — |
| `v3_exq_798_sdmelproducer_graded_nonconverging_world_20260723T081627Z_v3` | 2026-07-23T08:16 | (no claim tags) | — |
| `v3_exq_804_arc003_e3_selection_authority_20260723T085056Z_v3` | 2026-07-23T08:50 | ARC-003 | — |
| `v3_exq_805_arc016_eval_derived_commit_threshold_20260723T092739Z_v3` | 2026-07-23T09:27 | ARC-016 | — |
| `v3_exq_799_mech048_stability_temperature_behavioural_did_20260723T095928Z_v3` | 2026-07-23T09:59 | MECH-048 | — |
| `v3_exq_120a_arc018_viability_map_pair_20260723T120339Z_v3` | 2026-07-23T12:03 | ARC-018 | — |
| `v3_exq_707c_arc110_loop_segregation_c2_release_repair_20260723T151429Z_v3` | 2026-07-23T15:14 | ARC-110 | — |
| `v3_exq_114a_arc007_path_memory_probe_20260723T152445Z_v3` | 2026-07-23T15:24 | ARC-007 | — |
| `v3_exq_266b_q020_valence_geometry_pair_20260723T185013Z_v3` | 2026-07-23T18:50 | Q-020 | — |
| `v3_exq_708b_mech440_precommit_distribution_shape_falsifier_20260723T215332Z_v3` | 2026-07-23T21:53 | MECH-440 | — |
| `v3_exq_810_arc071_chunk_accumulator_readiness_20260723T222726Z_v3` | 2026-07-23T22:27 | ARC-071, MECH-323, MECH-324 | — |
| `v3_exq_801_arc018_rollout_depth_ablation_20260723T223210Z_v3` | 2026-07-23T22:32 | ARC-018 | — |
| `v3_exq_629c_mech342_ecological_maintenance_release_evidence_20260723T230514Z_v3` | 2026-07-23T23:05 | MECH-342 | — |
| `v3_exq_808_return_decomposition_objective_misspecification_20260724T044039Z_v3` | 2026-07-24T04:40 | (no claim tags) | — |
| `v3_exq_800_arc007_residue_scramble_dissociation_20260724T063057Z_v3` | 2026-07-24T06:30 | ARC-007 | — |
| `v3_exq_794a_mech204_phase7_sd076_calibration_loop_2x2_20260724T063301Z_v3` | 2026-07-24T08:15 | MECH-204, SD-076 | — |
| `v3_exq_812_mech295_cue_authority_sd054_20260724T085838Z_v3` | 2026-07-24T08:58 | (no claim tags) | — |
| `v3_exq_699b_pcomp_demotion_x_gonogo_fresh_select_20260724T123550Z_v3` | 2026-07-24T12:35 | MECH-448, MECH-449 | — |
| `v3_exq_786b_mech163_dual_system_recruitment_20260724T123825Z_v3` | 2026-07-24T12:38 | MECH-163 | — |
| `v3_exq_813_survival_zeroed_ppo_latent_policy_probe_20260724T143333Z_v3` | 2026-07-24T14:33 | (no claim tags) | — |
| `v3_exq_689j_mech448_factor_b_noise_control_repower_20260724T155840Z_v3` | 2026-07-24T15:58 | MECH-448 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_792a_mech457_retention_consolidation_20260722T212954Z_v3` | 2026-07-22T21:29 | MECH-457 |
| `v3_exq_797_mech266_external_task_engagement_instrumentation_20260722T213650Z_v3` | 2026-07-22T21:36 | MECH-266, SD-032a |
| `v3_exq_791a_channel_routing_cross_class_magnitude_replication_20260723T044051Z_v3` | 2026-07-23T04:40 | (no claim tags) |
| `v3_exq_809_sd080_action_object_init_invariance_20260723T061050Z_v3` | 2026-07-23T06:10 | SD-004 |
| `v3_exq_815_mech321_policy_decomposition_readiness_20260724T144151Z_v3` | 2026-07-24T14:41 | ARC-070, MECH-321 |
| `v3_exq_814_mech288_input_stream_isolation_diagnostic_20260724T144155Z_v3` | 2026-07-24T14:41 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_792a_mech457_retention_consolidation_20260722T212954Z_v3` | PASS | retention_consolidation_protects_competence | **vacuous_pass** |
| `v3_exq_797_mech266_external_task_engagement_instrumentation_20260722T213650Z_v3` | PASS | commitment_layer_starved | **precondition_unmet** |
| `v3_exq_798_sdmelproducer_graded_nonconverging_world_20260723T081627Z_v3` | FAIL | producer_graded_but_not_learnable | **precondition_unmet** |
| `v3_exq_812_mech295_cue_authority_sd054_20260724T085838Z_v3` | FAIL | INVALID_HARNESS | **precondition_unmet** |
| `v3_exq_699b_pcomp_demotion_x_gonogo_fresh_select_20260724T123550Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_813_survival_zeroed_ppo_latent_policy_probe_20260724T143333Z_v3` | FAIL | substrate_not_ready_requeue | **precondition_unmet** |
| `v3_exq_689j_mech448_factor_b_noise_control_repower_20260724T155840Z_v3` | FAIL | matched_noise_control_repowered_still_unmeetable | **precondition_unmet** |

## Recorded (non-gating) preconditions

**No action is required on account of this section.** These runs declare a readiness finding in `interpretation.recorded_preconditions[]` that did NOT hold -- but the author deliberately did not gate the run on it, because the run's premise survives the finding (e.g. a shared symmetric prior that biases every arm identically, or a readout-side question with an unaffected control). The entries are kept out of the adjudicating `interpretation.preconditions[]` on purpose: that list is read flat and arm-blind, so an entry there would return a whole-run `precondition_unmet` and bury a valid result. Each run's own `preconditions_scope_note` states the reasoning. Read this as an audit trail when interpreting the run -- it is NOT an adjudication flag, does not block a governance action, and does not exclude the run from scoring. See evidence/planning/zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md.

| Run ID | Status | Recorded precondition(s) not met | Scope note |
|--------|--------|----------------------------------|------------|
| `v3_exq_708b_mech440_precommit_distribution_shape_falsifier_20260723T215332Z_v3` | FAIL | temperature_control_raises_precommit_entropy, weight_noise_raises_precommit_entropy | The two entries temperature_control_raises_precommit_entropy and weight_noise_raises_precommit_entropy are carried under 'recorded_preconditions', NOT under the adjudicating flat 'preconditions' li... |

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
