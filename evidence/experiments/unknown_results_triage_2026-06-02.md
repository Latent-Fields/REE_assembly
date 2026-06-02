# UNKNOWN Results Triage — 2026-06-02

**Session:** `triage-unknown-results-20260602T063513Z`  
**Scope:** classification/cleanup of `result==UNKNOWN` entries in `evidence/experiments/runner_status.json`. No experiments requeued.  
**Context:** cloud-worker silent-drop bug (`experiment_runner.py:1394`) left `result=UNKNOWN` rows whose result manifest was never linked back into the status log.

## Summary

| Outcome | Count |
|---------|------:|
| **Recovered** (manifest found, true PASS/FAIL/ERROR written back) | 160 |
| **Recovered — non-binary** (manifest found; status PARTIAL/MIXED/INCONCLUSIVE/etc. or governance evidence_direction) | 23 |
| **Genuinely lost — runner-log outcome known** (no manifest on disk; left UNKNOWN; runner summary recorded an outcome) | 8 |
| **Genuinely lost — no outcome** (no manifest, no parseable runner-log verdict; left UNKNOWN) | 2 |
| **Total UNKNOWN triaged** | 193 |

Net: **183 of 193** UNKNOWN rows relinked to a real manifest and reclassified; **10** remain UNKNOWN (manifest genuinely absent).

Method: each row matched to its manifest by (1) explicit `Result written to <file>` reference in `result_summary`, else (2) exact experiment-name prefix `v3_exq_<num><letter>_` (flat file or `<dir>/manifest.json` run-pack form), choosing the candidate whose embedded timestamp (ISO `YYYYMMDDTHHMMSSZ` or unix-epoch) is nearest `completed_at`, else (3) numeric-only sibling prefix accepted **only** within 120 s of `completed_at` (script-name drift). Manifest `status`/`outcome` cross-checked against the runner-log outcome parsed from `result_summary`: **0 disagreements** across all 183 recoveries. `_dry`, `_partial`, `_episode_log` and `runs/<run_id>/` duplicate files were excluded as match targets.

## Recovered — PASS/FAIL/ERROR (160 entries)

### PASS (59)

| queue_id | claim_id | manifest | match |
|----------|----------|----------|-------|
| V3-EXQ-058b | ARC-027 | `evidence/experiments/v3_exq_058_arc027_harm_stream_calibration/v3_exq_058_arc027_harm_stream_calibration_20260320T200725Z.json` | written_ref |
| V3-EXQ-158 | Q-018 | `evidence/experiments/v3_exq_158_q018_rc_conflict_threshold_calibration_20260329T192854Z_v3.json` | exact_letter_unique |
| V3-EXQ-166e |  | `evidence/experiments/v3_exq_166e_sd003_harm_delta_predictor/v3_exq_166e_sd003_harm_delta_predictor_20260330T195516Z_v3.json` | exact_letter_unique |
| V3-EXQ-171 |  | `evidence/experiments/v3_exq_171_mech033_kernel_chain_pair_20260329T213946Z_v3.json` | exact_letter_nearest |
| V3-EXQ-171a | MECH-033 | `evidence/experiments/v3_exq_171_mech033_kernel_chain_pair_20260330T070404Z_v3.json` | num_fallback_near |
| V3-EXQ-178b |  | `evidence/experiments/v3_exq_178b_sd011_dual_stream_dissociation_20260330T193525Z_v3/manifest.json` | exact_letter_unique |
| V3-EXQ-184 |  | `evidence/experiments/v3_exq_184_mech033_kernel_chain_pair_20260401T185611Z_v3.json` | exact_letter_nearest |
| V3-EXQ-198 |  | `evidence/experiments/v3_exq_198_sd011_dual_stream_stability_20260401T232341Z_v3/manifest.json` | exact_letter_unique |
| V3-EXQ-208 | ARC-022 | `evidence/experiments/v3_exq_208_arc022_hierarchical_pipeline_probe/v3_exq_208_arc022_hierarchical_pipeline_probe_1775182116.json` | exact_letter_nearest |
| V3-EXQ-213 | MECH-072 | `evidence/experiments/v3_exq_213_mech072_foreseeable_harm_gating_20260403T202320Z_v3.json` | written_ref |
| V3-EXQ-246 |  | `evidence/experiments/v3_exq_246_mech122_spindle_coordination/v3_exq_246_mech122_spindle_coordination_20260405T132145Z_v3.json` | exact_letter_nearest |
| V3-EXQ-263a | MECH-216 | `evidence/experiments/v3_exq_263a_mech216_e1_predictive_wanting_20260409T084115Z_v3.json` | exact_letter_unique |
| V3-EXQ-265 |  | `evidence/experiments/v3_exq_265_sd017_sleep_phase_methods_validation_20260409T181835Z_v3.json` | exact_letter_unique |
| V3-EXQ-320 |  | `evidence/experiments/v3_exq_320_sd013_interventional_training/v3_exq_320_sd013_interventional_training_20260410T155756Z_v3.json` | exact_letter_unique |
| V3-EXQ-321b |  | `evidence/experiments/v3_exq_321b_mech090_bistable_holdrate/v3_exq_321b_mech090_bistable_holdrate_20260418T065913Z_v3.json` | exact_letter_nearest |
| V3-EXQ-323a |  | `evidence/experiments/v3_exq_323a_sd019_harm_nonredundancy/v3_exq_323a_sd019_harm_nonredundancy_20260416T172811Z_v3.json` | exact_letter_unique |
| V3-EXQ-326a | SD-015 | `evidence/experiments/v3_exq_326a_wanting_gradient_nav_fix/v3_exq_326a_wanting_gradient_nav_fix_20260413T172004Z_v3.json` | exact_letter_nearest |
| V3-EXQ-328a |  | `evidence/experiments/v3_exq_328a_mech112_zgoal_structured_latent/v3_exq_328a_mech112_zgoal_structured_latent_20260414T135044Z_v3.json` | exact_letter_nearest |
| V3-EXQ-329 | ARC-033 | `evidence/experiments/v3_exq_329_arc033_e2_harm_s_counterfactual/v3_exq_329_arc033_e2_harm_s_counterfactual_20260411T193133Z_v3.json` | exact_letter_nearest |
| V3-EXQ-353 |  | `evidence/experiments/v3_exq_353_arc033_sd003_interventional_vs_observational/v3_exq_353_arc033_sd003_interventional_vs_observational_20260415T060945Z_v3.json` | exact_letter_nearest |
| V3-EXQ-407 |  | `evidence/experiments/v3_exq_407_mech231_e2_short_horizon/v3_exq_407_mech231_e2_short_horizon_1776142217_v3.json` | exact_letter_nearest |
| V3-EXQ-446 |  | `evidence/experiments/v3_exq_446_sd032a_salience_coordinator/v3_exq_446_sd032a_salience_coordinator_20260420T013457Z_v3.json` | exact_letter_nearest |
| V3-EXQ-447 |  | `evidence/experiments/v3_exq_447_sd032d_pcc_stability/v3_exq_447_sd032d_pcc_stability_20260419T212315Z_v3.json` | exact_letter_nearest |
| V3-EXQ-447a |  | `evidence/experiments/v3_exq_447_sd032d_pcc_stability/v3_exq_447_sd032d_pcc_stability_20260423T204632Z_v3.json` | num_fallback_near |
| V3-EXQ-448 |  | `evidence/experiments/v3_exq_448_sd032e_pacc_autonomic/v3_exq_448_sd032e_pacc_autonomic_20260419T212521Z_v3.json` | exact_letter_unique |
| V3-EXQ-449a |  | `evidence/experiments/v3_exq_449a_sd016_cue_action_proj_forward_path_probe_20260421T202422Z_v3.json` | exact_letter_nearest |
| V3-EXQ-449b |  | `evidence/experiments/v3_exq_449b_sd016_cue_action_proj_consumer_fix_20260424T021756Z_v3.json` | exact_letter_unique |
| V3-EXQ-455 |  | `evidence/experiments/v3_exq_455_sd032a_salience_behavioral/v3_exq_455_sd032a_salience_behavioral_20260420T223056Z_v3.json` | exact_letter_unique |
| V3-EXQ-456 |  | `evidence/experiments/v3_exq_456_sd033a_lateral_pfc_analog_landing/v3_exq_456_sd033a_lateral_pfc_analog_landing_v3_20260421T202344Z.json` | exact_letter_nearest |
| V3-EXQ-460 |  | `evidence/experiments/v3_exq_460_sd034_verified_but_not_released/v3_exq_460_sd034_verified_but_not_released_v3_20260421T202347Z.json` | exact_letter_nearest |
| V3-EXQ-462 |  | `evidence/experiments/v3_exq_462_mech267_rule_binding/v3_exq_462_mech267_rule_binding_v3_20260421T202405Z.json` | exact_letter_nearest |
| V3-EXQ-463 |  | `evidence/experiments/v3_exq_463_mech268_dacc_conflict_saturation/v3_exq_463_mech268_dacc_conflict_saturation_v3_20260421T202354Z.json` | exact_letter_nearest |
| V3-EXQ-464 |  | `evidence/experiments/v3_exq_464_mech266_competing_goals/v3_exq_464_mech266_competing_goals_v3_20260421T202359Z.json` | exact_letter_nearest |
| V3-EXQ-465 |  | `evidence/experiments/v3_exq_465_mech267_intrusive_simulation_filtering/v3_exq_465_mech267_intrusive_simulation_filtering_v3_20260421T202408Z.json` | exact_letter_nearest |
| V3-EXQ-466 |  | `evidence/experiments/v3_exq_466_sd034_satisficing_residue_discharge/v3_exq_466_sd034_satisficing_residue_discharge_v3_20260421T202351Z.json` | exact_letter_nearest |
| V3-EXQ-467 |  | `evidence/experiments/v3_exq_467_mech266_mode_stickiness/v3_exq_467_mech266_mode_stickiness_v3_20260421T202402Z.json` | exact_letter_nearest |
| V3-EXQ-468 |  | `evidence/experiments/v3_exq_468_sd034_mech268_commitment_vs_contradiction/v3_exq_468_sd034_mech268_commitment_vs_contradiction_v3_20260421T202356Z.json` | exact_letter_nearest |
| V3-EXQ-473 |  | `evidence/experiments/v3_exq_473_sd035_cea_mode_prior/v3_exq_473_sd035_cea_mode_prior_20260421T195533Z_v3.json` | exact_letter_nearest |
| V3-EXQ-474 |  | `evidence/experiments/v3_exq_474_sd035_bla_encoding_remap/v3_exq_474_sd035_bla_encoding_remap_20260421T195558Z_v3.json` | exact_letter_nearest |
| V3-EXQ-484 | SD-033a | `evidence/experiments/v3_exq_484_sd033a_distractor_resistance_20260427T054449Z_v3.json` | exact_letter_nearest |
| V3-EXQ-485 | SD-033b | `evidence/experiments/v3_exq_485_sd033b_ofc_analog_landing_20260427T054454Z_v3.json` | exact_letter_nearest |
| V3-EXQ-485a |  | `evidence/experiments/v3_exq_485a_sd033b_ofc_oracle_landing_20260504T150333Z_v3.json` | exact_letter_unique |
| V3-EXQ-493 | MECH-295 | `evidence/experiments/v3_exq_493_mech295_liking_bridge_validation_20260427T080304Z_v3.json` | exact_letter_nearest |
| V3-EXQ-494 | SD-039 | `evidence/experiments/v3_exq_494_sd039_anchor_payload_validation/v3_exq_494_sd039_anchor_payload_validation_20260427T094326Z_v3.json` | exact_letter_unique |
| V3-EXQ-496 | MECH-292 | `evidence/experiments/v3_exq_496_mech292_ghost_goal_bank_validation/v3_exq_496_mech292_ghost_goal_bank_validation_20260427T094339Z_v3.json` | exact_letter_nearest |
| V3-EXQ-497 | MECH-293 | `evidence/experiments/v3_exq_497_mech293_ghost_probes_validation/v3_exq_497_mech293_ghost_probes_validation_20260427T094353Z_v3.json` | exact_letter_nearest |
| V3-EXQ-499 | MECH-094 | `evidence/experiments/v3_exq_499_mech094_hypothesis_tag_writegate_discriminative_20260429T184730Z_v3.json` | exact_letter_unique |
| V3-EXQ-503 | SD-017 | `evidence/experiments/v3_exq_503_sd017_sleep_phase_discriminative_20260501T201518Z_v3.json` | exact_letter_unique |
| V3-EXQ-505 | MECH-093 | `evidence/experiments/v3_exq_505_mech093_zbeta_precision_dissociation_20260503T021711Z_v3.json` | exact_letter_unique |
| V3-EXQ-507 | ARC-026 | `evidence/experiments/v3_exq_507_arc026_capacity_scaling_20260503T014741Z_v3.json` | exact_letter_unique |
| V3-EXQ-509 | SD-047 | `evidence/experiments/v3_exq_509_sd047_multi_source_substrate_readiness/v3_exq_509_sd047_multi_source_substrate_readiness_20260503T103241Z_v3.json` | exact_letter_unique |
| V3-EXQ-513 |  | `evidence/experiments/v3_exq_513_sd049_multi_resource_heterogeneity_substrate_readiness/v3_exq_513_sd049_multi_resource_heterogeneity_substrate_readiness_20260503T132415Z_v3.json` | exact_letter_unique |
| V3-EXQ-515 | MECH-302 | `evidence/experiments/v3_exq_515_mech302_suffering_derivative_comparator_substrate_readiness/v3_exq_515_mech302_suffering_derivative_comparator_substrate_readiness_20260504T010417Z_v3.json` | exact_letter_unique |
| V3-EXQ-516 | MECH-302 | `evidence/experiments/v3_exq_516_mech302_suffering_derivative_integration_20260504T041122Z_v3.json` | exact_letter_unique |
| V3-EXQ-518 | SD-019a | `evidence/experiments/v3_exq_518_sd019a_20260504T150257Z/manifest.json` | exact_letter_unique |
| V3-EXQ-521 |  | `evidence/experiments/v3_exq_521_reef_enrichment_20260504T223858Z_v3.json` | exact_letter_unique |
| V3-EXQ-522 |  | `evidence/experiments/v3_exq_522_reef_monostrategy_break_20260505T064610Z_v3.json` | exact_letter_unique |
| V3-EXQ-533 | MECH-102 | `evidence/experiments/v3_exq_533_mech102_harm_stream_ablation/manifest.json` | exact_letter_unique |
| V3-EXQ-534 | SD-016 | `evidence/experiments/v3_exq_534_sd016_cue_terrain_training/manifest.json` | exact_letter_unique |

### FAIL (101)

| queue_id | claim_id | manifest | match |
|----------|----------|----------|-------|
| V3-EXQ-059b | ARC-016 | `evidence/experiments/v3_exq_059_arc016_beta_gate_fixed_threshold/v3_exq_059_arc016_beta_gate_fixed_threshold_20260320T204910Z.json` | num_fallback_near |
| V3-EXQ-154 | Q-014 | `evidence/experiments/v3_exq_154_q014_jepa_invariance_blind_spot_20260329T190928Z_v3.json` | exact_letter_unique |
| V3-EXQ-155 | Q-015 | `evidence/experiments/v3_exq_155_q015_commit_boundary_minimal_contract_20260329T191541Z_v3.json` | exact_letter_unique |
| V3-EXQ-156 | Q-016 | `evidence/experiments/v3_exq_156_q016_tri_loop_arbitration_policy_20260329T192850Z_v3.json` | exact_letter_unique |
| V3-EXQ-159 | Q-020 | `evidence/experiments/v3_exq_159_q020_arc007_valence_constraint_pair_20260329T193606Z_v3.json` | exact_letter_unique |
| V3-EXQ-160 | Q-023 | `evidence/experiments/v3_exq_160_q023_multiagent_convergence_pair_20260329T194510Z_v3.json` | exact_letter_unique |
| V3-EXQ-161 | Q-024 | `evidence/experiments/v3_exq_161_q024_trajectory_representation_triple_20260329T200440Z_v3.json` | exact_letter_nearest |
| V3-EXQ-163 | MECH-141 | `evidence/experiments/v3_exq_163_mech141_dual_timescale_arbitration_20260329T203824_v3.json` | exact_letter_unique |
| V3-EXQ-164a |  | `evidence/experiments/v3_exq_164a_mech142_axis_decorrelation_a7622089_v3.json` | written_ref |
| V3-EXQ-165 | MECH-143 | `evidence/experiments/v3_exq_165_mech143_hippocampal_value_sensitivity_f3319520_v3.json` | exact_letter_nearest |
| V3-EXQ-166 |  | `evidence/experiments/v3_exq_166_sd003_obs_space_forward_model/v3_exq_166_sd003_obs_space_forward_model_20260329T210513Z_v3.json` | exact_letter_unique |
| V3-EXQ-166a |  | `evidence/experiments/v3_exq_166a_sd003_obs_space_forward_model/v3_exq_166a_sd003_obs_space_forward_model_20260329T213108Z_v3.json` | exact_letter_unique |
| V3-EXQ-166b |  | `evidence/experiments/v3_exq_166b_sd003_harm_latent_reconstruction/v3_exq_166b_sd003_harm_latent_reconstruction_20260330T191503Z_v3.json` | written_ref |
| V3-EXQ-166c |  | `evidence/experiments/v3_exq_166c_sd003_harm_latent_shuffled_ablation/v3_exq_166c_sd003_harm_latent_shuffled_ablation_20260330T192815Z_v3.json` | written_ref |
| V3-EXQ-166d |  | `evidence/experiments/v3_exq_166d_sd003_harm_decoder_discrimination/v3_exq_166d_sd003_harm_decoder_discrimination_20260330T194416Z_v3.json` | written_ref |
| V3-EXQ-170 |  | `evidence/experiments/v3_exq_170_q002_r_field_resolution_pair_20260329T213812Z_v3.json` | exact_letter_nearest |
| V3-EXQ-170a | Q-002 | `evidence/experiments/v3_exq_170_q002_r_field_resolution_pair_20260330T070234Z_v3.json` | num_fallback_near |
| V3-EXQ-172a | ARC-018 | `evidence/experiments/v3_exq_172_arc018_rollout_viability_pair_20260330T070425Z_v3.json` | num_fallback_near |
| V3-EXQ-176 | ARC-036 | `evidence/experiments/v3_exq_176_arc036_valence_dimension_probe_20260329T213701Z_v3.json` | exact_letter_nearest |
| V3-EXQ-176a | ARC-036 | `evidence/experiments/v3_exq_176_arc036_valence_dimension_probe_20260330T070447Z_v3.json` | num_fallback_near |
| V3-EXQ-177 | SD-008 | `evidence/experiments/v3_exq_177_sd008_integration_test_20260329T215657Z_v3.json` | exact_letter_unique |
| V3-EXQ-178 |  | `evidence/experiments/v3_exq_178_sd011_dual_stream_dissociation_20260330T185813Z_v3/manifest.json` | exact_letter_unique |
| V3-EXQ-178a |  | `evidence/experiments/v3_exq_178a_sd011_dual_stream_dissociation_20260330T191926Z_v3/manifest.json` | exact_letter_unique |
| V3-EXQ-196 |  | `evidence/experiments/v3_exq_196_arc018_rollout_viability_pair_20260401T195627Z_v3.json` | exact_letter_nearest |
| V3-EXQ-203 |  | `evidence/experiments/v3_exq_203_mech057a_completion_gate_breath/v3_exq_203_mech057a_completion_gate_breath_20260402T230445Z.json` | exact_letter_unique |
| V3-EXQ-207 | MECH-155 | `evidence/experiments/v3_exq_207_mech155_general_indexing_probe/v3_exq_207_mech155_general_indexing_probe_1775181944.json` | exact_letter_nearest |
| V3-EXQ-212 | MECH-070 | `evidence/experiments/v3_exq_212_mech070_e2_motor_model_pair/v3_exq_212_mech070_e2_motor_model_pair_1775203063_v3.json` | exact_letter_nearest |
| V3-EXQ-214 | ARC-039 | `evidence/experiments/v3_exq_214_arc039_entorhinal_consolidation_probe_20260403T202345Z_v3.json` | exact_letter_unique |
| V3-EXQ-215 | Q-002 | `evidence/experiments/v3_exq_215_q002_residue_resolution_pair_20260403T202434Z_v3.json` | exact_letter_unique |
| V3-EXQ-228a |  | `evidence/experiments/v3_exq_228a_arc032_theta_bypass_behavioral/v3_exq_228a_arc032_theta_bypass_behavioral_1775398618.json` | exact_letter_unique |
| V3-EXQ-229 |  | `evidence/experiments/v3_exq_229_mech128_e1_goal_conditioning_pair/v3_exq_229_mech128_e1_goal_conditioning_pair_1775299023.json` | exact_letter_unique |
| V3-EXQ-241a |  | `evidence/experiments/v3_exq_241a_sd011_second_source_validation/v3_exq_241a_sd011_second_source_validation_output.json` | exact_letter_unique |
| V3-EXQ-241b |  | `evidence/experiments/v3_exq_241b_sd011_second_source_info_gain/v3_exq_241b_sd011_second_source_info_gain_output.json` | exact_letter_unique |
| V3-EXQ-242 |  | `evidence/experiments/v3_exq_242_sd017_sleep_phase_ablation/v3_exq_242_sd017_sleep_phase_ablation_1775394244_v3.json` | exact_letter_unique |
| V3-EXQ-243 |  | `evidence/experiments/v3_exq_243_inv045_phase_ordering_necessity/v3_exq_243_inv045_phase_ordering_necessity_20260405T131554Z_v3.json` | exact_letter_unique |
| V3-EXQ-244 |  | `evidence/experiments/v3_exq_244_mech165_reverse_replay_diversity/v3_exq_244_mech165_reverse_replay_diversity_20260405T141709Z_v3.json` | exact_letter_nearest |
| V3-EXQ-259 |  | `evidence/experiments/v3_exq_259_wanting_gradient_navigation/v3_exq_259_wanting_gradient_navigation_1775666895.json` | exact_letter_unique |
| V3-EXQ-263b |  | `evidence/experiments/v3_exq_263b_sd023_mech216_landmark_wanting_20260410T093942Z_v3.json` | exact_letter_unique |
| V3-EXQ-264 | ARC-033 | `evidence/experiments/v3_exq_264_arc033_e2_harm_s_forward_20260409T170322Z_v3.json` | exact_letter_unique |
| V3-EXQ-267 | ARC-038 | `evidence/experiments/v3_exq_267_arc038_waking_consolidation_discriminative_20260410T093618Z_v3.json` | exact_letter_unique |
| V3-EXQ-318 | SD-022 | `evidence/experiments/v3_exq_318_sd022_limb_damage_stream_separation/v3_exq_318_sd022_limb_damage_stream_separation_1775783716_v3.json` | exact_letter_unique |
| V3-EXQ-321 |  | `evidence/experiments/v3_exq_321_mech090_bistable_gate/v3_exq_321_mech090_bistable_gate_20260410T155906Z_v3.json` | exact_letter_unique |
| V3-EXQ-321a |  | `evidence/experiments/v3_exq_321a_mech090_bistable_gate/v3_exq_321a_mech090_bistable_gate_20260416T200620Z_v3.json` | exact_letter_unique |
| V3-EXQ-322 |  | `evidence/experiments/v3_exq_322_sd015_resource_encoder_seeding/v3_exq_322_sd015_resource_encoder_seeding_20260410T222041Z_v3.json` | exact_letter_nearest |
| V3-EXQ-322a |  | `evidence/experiments/v3_exq_322a_sd015_resource_encoder_seeding/v3_exq_322a_sd015_resource_encoder_seeding_20260414T105631Z_v3.json` | exact_letter_unique |
| V3-EXQ-323 |  | `evidence/experiments/v3_exq_323_sd019_harm_nonredundancy/v3_exq_323_sd019_harm_nonredundancy_20260410T184158Z_v3.json` | exact_letter_nearest |
| V3-EXQ-324 |  | `evidence/experiments/v3_exq_324_sd020_harm_surprise_pe/v3_exq_324_sd020_harm_surprise_pe_20260410T220218Z_v3.json` | exact_letter_nearest |
| V3-EXQ-325 |  | `evidence/experiments/v3_exq_325_sd021_descending_pain_modulation/v3_exq_325_sd021_descending_pain_modulation_20260410T160919Z_v3.json` | exact_letter_unique |
| V3-EXQ-325a |  | `evidence/experiments/v3_exq_325a_sd021_descending_pain_modulation/v3_exq_325a_sd021_descending_pain_modulation_20260418T065916Z_v3.json` | exact_letter_nearest |
| V3-EXQ-326 | SD-015 | `evidence/experiments/v3_exq_326_wanting_gradient_nav_fix/v3_exq_326_wanting_gradient_nav_fix_20260413T144759Z_v3.json` | exact_letter_nearest |
| V3-EXQ-328 | MECH-112 | `evidence/experiments/v3_exq_328_mech112_zgoal_structured_latent/v3_exq_328_mech112_zgoal_structured_latent_20260411T134736Z_v3.json` | exact_letter_nearest |
| V3-EXQ-328b | MECH-230 | `evidence/experiments/v3_exq_328b_mech112_zgoal_structured_latent/v3_exq_328b_mech112_zgoal_structured_latent_20260413T082606Z_v3.json` | exact_letter_nearest |
| V3-EXQ-332 |  | `evidence/experiments/v3_exq_332_mech216_predictive_wanting_20260414T234204Z_v3.json` | exact_letter_unique |
| V3-EXQ-332a |  | `evidence/experiments/v3_exq_332a_mech216_predictive_wanting_dense_20260418T040810Z_v3.json` | exact_letter_nearest |
| V3-EXQ-385 | INV-049 | `evidence/experiments/v3_exq_385_inv049_offline_consolidation_necessity_20260414T220308Z_v3.json` | exact_letter_unique |
| V3-EXQ-418 | SD-017 | `evidence/experiments/v3_exq_418_sd017_context_conditioned_action_20260416T172742Z_v3.json` | exact_letter_unique |
| V3-EXQ-418k |  | `evidence/experiments/v3_exq_418k_sd016_context_memory_reef_20260505T223834Z_v3.json` | exact_letter_unique |
| V3-EXQ-431 |  | `evidence/experiments/v3_exq_431_sd003_causal_discrimination/v3_exq_431_sd003_causal_discrimination_20260417T152531Z_v3.json` | exact_letter_nearest |
| V3-EXQ-432 |  | `evidence/experiments/v3_exq_432_sd014_replay_gate_prioritization_20260418T212738Z_v3.json` | exact_letter_unique |
| V3-EXQ-433b |  | `evidence/experiments/v3_exq_433b_sd029_extended_interventional/v3_exq_433b_sd029_extended_interventional_20260420T155256Z_v3.json` | exact_letter_unique |
| V3-EXQ-433c |  | `evidence/experiments/v3_exq_433c_sd029_eventcond_comparator/v3_exq_433c_sd029_eventcond_comparator_20260423T232350Z_v3.json` | exact_letter_unique |
| V3-EXQ-433d | SD-029 | `evidence/experiments/v3_exq_433d_sd029_eventcond_comparator/v3_exq_433d_sd029_eventcond_comparator_20260427T012142Z_v3.json` | exact_letter_unique |
| V3-EXQ-433e |  | `evidence/experiments/v3_exq_433e_sd029_eventcond_comparator_reef/v3_exq_433e_sd029_eventcond_comparator_reef_20260505T072754Z_v3.json` | exact_letter_unique |
| V3-EXQ-433f |  | `evidence/experiments/v3_exq_433f_sd029_eventcond_comparator_reef/v3_exq_433f_sd029_eventcond_comparator_reef_20260507T213949Z_v3.json` | exact_letter_unique |
| V3-EXQ-445 |  | `evidence/experiments/v3_exq_445_sd032b_dacc_analog/v3_exq_445_sd032b_dacc_analog_20260419T205642Z_v3.json` | exact_letter_unique |
| V3-EXQ-445a |  | `evidence/experiments/v3_exq_445a_sd032b_dacc_full_pipeline/v3_exq_445a_sd032b_dacc_full_pipeline_20260420T232934Z_v3.json` | exact_letter_nearest |
| V3-EXQ-445b |  | `evidence/experiments/v3_exq_445b_sd032b_dacc_epsilon_diversity/v3_exq_445b_sd032b_dacc_epsilon_diversity_20260421T025042Z_v3.json` | exact_letter_nearest |
| V3-EXQ-445c |  | `evidence/experiments/v3_exq_445c_sd032b_dacc_larger_env/v3_exq_445c_sd032b_dacc_larger_env_20260421T043443Z_v3.json` | exact_letter_nearest |
| V3-EXQ-445f |  | `evidence/experiments/v3_exq_445f_sd032b_dacc_reef/v3_exq_445f_sd032b_dacc_reef_20260505T174448Z_v3.json` | exact_letter_unique |
| V3-EXQ-445g |  | `evidence/experiments/v3_exq_445g_sd032b_dacc_reef/v3_exq_445g_sd032b_dacc_reef_20260505T223845Z_v3.json` | exact_letter_unique |
| V3-EXQ-445h |  | `evidence/experiments/v3_exq_445h_sd032b_dacc_reef/v3_exq_445h_sd032b_dacc_reef_20260508T002953Z_v3.json` | exact_letter_nearest |
| V3-EXQ-449 |  | `evidence/experiments/v3_exq_449_sd016_cue_action_proj_wiring_probe_20260420T143953Z_v3.json` | exact_letter_unique |
| V3-EXQ-476a |  | `evidence/experiments/v3_exq_476a_mech269_vs_validation_probe/v3_exq_476a_mech269_vs_validation_probe_20260424T064215Z_v3.json` | exact_letter_unique |
| V3-EXQ-476b |  | `evidence/experiments/v3_exq_476b_mech269_vs_validation_probe/v3_exq_476b_mech269_vs_validation_probe_20260424T073240Z_v3.json` | exact_letter_unique |
| V3-EXQ-476c |  | `evidence/experiments/v3_exq_476c_mech269_vs_validation_probe/v3_exq_476c_mech269_vs_validation_probe_20260507T214359Z_v3.json` | exact_letter_nearest |
| V3-EXQ-478 | MECH-284 | `evidence/experiments/v3_exq_478_mech284_phase3_diagnostic/v3_exq_478_mech284_phase3_diagnostic_20260424T131455Z_v3.json` | exact_letter_unique |
| V3-EXQ-480 | MECH-284 | `evidence/experiments/v3_exq_480_mech284_phase3_param_sweep/v3_exq_480_mech284_phase3_param_sweep_20260425T014558Z_v3.json` | exact_letter_unique |
| V3-EXQ-481 |  | `evidence/experiments/v3_exq_481_vs_commit_release/v3_exq_481_vs_commit_release_20260425T101332Z_v3.json` | exact_letter_unique |
| V3-EXQ-482 |  | `evidence/experiments/v3_exq_482_sd029_baseline_monostrategy_diagnostic/v3_exq_482_sd029_baseline_monostrategy_diagnostic_20260425T101638Z_v3.json` | exact_letter_unique |
| V3-EXQ-490 | MECH-269b | `evidence/experiments/v3_exq_490_mech269b_vs_rollout_gating/v3_exq_490_mech269b_vs_rollout_gating_20260427T080413Z_v3.json` | exact_letter_nearest |
| V3-EXQ-490b | Q-040 | `evidence/experiments/v3_exq_490b_mech269b_vs_rollout_gating/v3_exq_490b_mech269b_vs_rollout_gating_20260428T171429Z_v3.json` | exact_letter_unique |
| V3-EXQ-498 | SD-034 | `evidence/experiments/v3_exq_498_ocd_layer1_closure_threshold_sweep/v3_exq_498_ocd_layer1_closure_threshold_sweep_20260428T201903Z_v3.json` | exact_letter_unique |
| V3-EXQ-504 | MECH-153 | `evidence/experiments/v3_exq_504_mech153_supervised_context_labeling_3arm_20260503T021659Z_v3.json` | exact_letter_unique |
| V3-EXQ-506 | MECH-095 | `evidence/experiments/v3_exq_506_mech095_agency_comparator_substrate_20260503T021729Z_v3.json` | exact_letter_unique |
| V3-EXQ-508 | ARC-033 | `evidence/experiments/v3_exq_508_arc033_e2_harm_s_body_damage_ablation_20260503T021914Z_v3.json` | written_ref |
| V3-EXQ-510 | MECH-095 | `evidence/experiments/v3_exq_510_sd047_mech095_live_env_comparator_gap/v3_exq_510_sd047_mech095_live_env_comparator_gap_20260504T074619Z_v3.json` | exact_letter_unique |
| V3-EXQ-511 |  | `evidence/experiments/v3_exq_511_sd048_interoceptive_noise_substrate_readiness/v3_exq_511_sd048_interoceptive_noise_substrate_readiness_20260503T113836Z_v3.json` | exact_letter_unique |
| V3-EXQ-514 |  | `evidence/experiments/v3_exq_514_sd049_phase_2_behavioural_validation/v3_exq_514_sd049_phase_2_behavioural_validation_20260504T100649Z_v3.json` | exact_letter_unique |
| V3-EXQ-514d |  | `evidence/experiments/v3_exq_514d_sd049_bg_gating_diagnostic/v3_exq_514d_sd049_bg_gating_diagnostic_20260506T013506Z_v3.json` | exact_letter_unique |
| V3-EXQ-514e |  | `evidence/experiments/v3_exq_514e_bg_gating_seaweed_diagnostic/v3_exq_514e_bg_gating_seaweed_diagnostic_20260506T064842Z_v3.json` | exact_letter_unique |
| V3-EXQ-517a |  | `evidence/experiments/v3_exq_517a_mech302_relief_completion_discriminative_pair_20260504T222032Z_v3.json` | exact_letter_unique |
| V3-EXQ-517b |  | `evidence/experiments/v3_exq_517b_mech302_relief_completion_discriminative_pair_20260506T013515Z_v3.json` | exact_letter_unique |
| V3-EXQ-523 |  | `evidence/experiments/v3_exq_523_sd029_reef_comparator_20260505T180800Z_v3.json` | exact_letter_unique |
| V3-EXQ-531 | SD-015 | `evidence/experiments/v3_exq_531_sd015_resource_encoder_ablation/manifest.json` | exact_letter_unique |
| V3-EXQ-532 | SD-005 | `evidence/experiments/v3_exq_532_sd005_latent_domain_selectivity/v3_exq_532_sd005_latent_domain_selectivity_20260506T090607Z_v3.json` | exact_letter_unique |
| V3-EXQ-535 |  | `evidence/experiments/v3_exq_535_sd029_p1_target_fix/v3_exq_535_sd029_p1_target_fix_20260506T214852Z_v3.json` | exact_letter_unique |
| V3-EXQ-535a |  | `evidence/experiments/v3_exq_535a_sd029_p3_eval_fix/v3_exq_535a_sd029_p3_eval_fix_20260507T203343Z_v3.json` | exact_letter_unique |
| V3-EXQ-536 |  | `evidence/experiments/v3_exq_536_goal_seeding_lift_ablation/v3_exq_536_goal_seeding_lift_ablation_20260507T202858Z_v3.json` | exact_letter_unique |
| V3-EXQ-537 |  | `evidence/experiments/v3_exq_537_sd029_single_pass_residual/v3_exq_537_sd029_single_pass_residual_20260508T135430Z_v3.json` | exact_letter_nearest |
| V3-EXQ-537a |  | `evidence/experiments/v3_exq_537_sd029_single_pass_residual/v3_exq_537_sd029_single_pass_residual_20260508T135638Z_v3.json` | num_fallback_near |
| V3-EXQ-537b | SD-029 | `evidence/experiments/v3_exq_537b_sd029_decoupled_curricula/v3_exq_537b_sd029_decoupled_curricula_20260508T180253Z_v3.json` | exact_letter_unique |

## Recovered — non-binary / governance-normalized (23 entries)

Manifest found and linked, but the run's outcome is not a clean PASS/FAIL: either an explicit non-binary status (PARTIAL / MIXED / INCONCLUSIVE / DIAGNOSTIC_COMPLETE / INCONCLUSIVE_UNDERTRAINED / PARTIAL_*) or a governance-normalized manifest carrying only an `evidence_direction` (no PASS/FAIL verdict). `result` was set to the manifest's true outcome value (source noted).

| queue_id | claim_id | true_result | source | manifest |
|----------|----------|-------------|--------|----------|
| V3-EXQ-147a | MECH-128 | PARTIAL | manifest_status | `evidence/experiments/v3_exq_147a_mech128_e1_goal_conditioning_pair/v3_exq_147a_mech128_e1_goal_conditioning_pair_1775184659.json` |
| V3-EXQ-157 | Q-017 | PARTIAL_COLLAPSE_ADEQUATE | manifest_status | `evidence/experiments/v3_exq_157_q017_control_axis_minimal_subset_20260329T185928Z_v3.json` |
| V3-EXQ-162 | MECH-137 | PARTIAL_NO_CANCEL | manifest_status | `evidence/experiments/v3_exq_162_mech137_commit_token_structure_9e3b4eaa_v3.json` |
| V3-EXQ-172 | ARC-018 | INCONCLUSIVE | manifest_status | `evidence/experiments/v3_exq_172_arc018_rollout_viability_pair_20260329T213638Z_v3.json` |
| V3-EXQ-181 |  | MIXED | manifest_status | `evidence/experiments/v3_exq_181_e1_prior_context_discrimination/v3_exq_181_e1_prior_context_discrimination_20260331T072201Z.json` |
| V3-EXQ-194 | MECH-152 | MIXED | manifest_status | `evidence/experiments/v3_exq_194_direct_terrain_pathway/v3_exq_194_direct_terrain_pathway_20260401T025000Z.json` |
| V3-EXQ-194a | MECH-152 | MIXED | manifest_status | `evidence/experiments/v3_exq_194a_direct_terrain_phased/v3_exq_194a_direct_terrain_phased_20260401T185253Z.json` |
| V3-EXQ-209 | MECH-075 | PARTIAL | manifest_status | `evidence/experiments/v3_exq_209_mech075_bg_hippocampal_gain_probe/v3_exq_209_mech075_bg_hippocampal_gain_probe_1775182286.json` |
| V3-EXQ-210 | MECH-156 | PARTIAL | manifest_status | `evidence/experiments/v3_exq_210_mech156_theta_traversal_probe/v3_exq_210_mech156_theta_traversal_probe_1775184493.json` |
| V3-EXQ-211 | MECH-153 | PARTIAL | manifest_status | `evidence/experiments/v3_exq_211_mech153_arc042_supervised_labeling/v3_exq_211_mech153_arc042_supervised_labeling_1775203010.json` |
| V3-EXQ-250 | INV-054 | INCONCLUSIVE | manifest_status | `evidence/experiments/v3_exq_250_inv054_phase_transition_recovery/v3_exq_250_inv054_phase_transition_recovery_1775520080.json` |
| V3-EXQ-250b | INV-054 | INCONCLUSIVE | manifest_status | `evidence/experiments/v3_exq_250_inv054_phase_transition_recovery/v3_exq_250_inv054_phase_transition_recovery_1775541543.json` |
| V3-EXQ-470 |  | WEAKENS | evidence_direction | `evidence/experiments/v3_exq_470_sd029_balanced_curriculum_20260421T202341Z_v3.json` |
| V3-EXQ-470a |  | WEAKENS | evidence_direction | `evidence/experiments/v3_exq_470a_sd029_balanced_curriculum/v3_exq_470a_sd029_balanced_curriculum_20260423T204626Z_v3.json` |
| V3-EXQ-471 |  | NON_CONTRIBUTORY | evidence_direction | `evidence/experiments/v3_exq_471_best_agent_fishtank_showcase/v3_exq_471_best_agent_fishtank_showcase_20260421T211059Z.json` |
| V3-EXQ-475 |  | NON_CONTRIBUTORY | evidence_direction | `evidence/experiments/v3_exq_475_sd036_decay_unlocks_exq471/v3_exq_475_sd036_decay_unlocks_exq471_20260422T173839Z.json` |
| V3-EXQ-479 | SD-029 | SUPPORTS | evidence_direction | `evidence/experiments/v3_exq_479_sd029_balanced_curriculum_fix/v3_exq_479_sd029_balanced_curriculum_fix_20260424T173508Z_v3.json` |
| V3-EXQ-523a |  | INCONCLUSIVE_UNDERTRAINED | manifest_status | `evidence/experiments/v3_exq_523a_sd029_reef_comparator/v3_exq_523a_sd029_reef_comparator_20260506T064939Z_v3.json` |
| V3-EXQ-523b |  | INCONCLUSIVE_UNDERTRAINED | manifest_status | `evidence/experiments/v3_exq_523b_sd029_reef_comparator/v3_exq_523b_sd029_reef_comparator_20260508T043308Z_v3.json` |
| V3-EXQ-524 |  | NON_CONTRIBUTORY | evidence_direction | `evidence/experiments/v3_exq_524_reef_fishtank_showcase/v3_exq_524_reef_fishtank_showcase_20260506T093201Z.json` |
| V3-EXQ-528 | SD-029 | INCONCLUSIVE_UNDERTRAINED | manifest_status | `evidence/experiments/v3_exq_528_sd029_comparator_trained/v3_exq_528_sd029_comparator_trained_20260506T094030Z_v3.json` |
| V3-EXQ-536a |  | DIAGNOSTIC_COMPLETE | manifest_status | `evidence/experiments/v3_exq_536a_goal_seeding_instrumentation/v3_exq_536a_goal_seeding_instrumentation_20260508T043659Z_v3.json` |
| V3-EXQ-536b |  | DIAGNOSTIC_COMPLETE | manifest_status | `evidence/experiments/v3_exq_536b_goal_seeding_inject_forcearm/v3_exq_536b_goal_seeding_inject_forcearm_20260508T045233Z_v3.json` |

## Genuinely lost — left as UNKNOWN (10 entries)

No result manifest exists on disk under any name/timestamp variant (verified by exhaustive `find` on the exact-letter experiment token, dir-form and nested `manifest.json` included). These are the true casualties of the silent-drop bug. **Left as `result=UNKNOWN`**; a `unknown_triage_2026_06_02` marker was added to each so future sweeps don't re-scan them.

### Runner-log outcome known (manifest lost) (8)

The runner computed an outcome (still in `result_summary`) but the manifest was never committed. Outcome shown is from the runner log, **not** authoritative evidence.

| queue_id | claim_id | runner-log outcome | predecessor manifest on disk (sibling) |
|----------|----------|--------------------|----------------------------------------|
| V3-EXQ-173 | MECH-096 | FAIL | — |
| V3-EXQ-174 | ARC-023 | FAIL | — |
| V3-EXQ-385b |  | FAIL | `evidence/experiments/v3_exq_385_inv049_offline_consolidation_necessity_20260414T220308Z_v3.json` |
| V3-EXQ-418b |  | FAIL | `evidence/experiments/v3_exq_418_sd017_context_conditioned_action_20260416T172742Z_v3.json` |
| V3-EXQ-418c |  | FAIL | `evidence/experiments/v3_exq_418_sd017_context_conditioned_action_20260416T172742Z_v3.json` |
| V3-EXQ-445e |  | FAIL | `evidence/experiments/v3_exq_445_sd032b_dacc_analog/v3_exq_445_sd032b_dacc_analog_20260419T205642Z_v3.json` |
| V3-EXQ-490a | MECH-269b | FAIL | `evidence/experiments/v3_exq_490_mech269b_vs_rollout_gating/v3_exq_490_mech269b_vs_rollout_gating_20260427T080413Z_v3.json` |
| V3-EXQ-530b |  | FAIL | `evidence/experiments/v3_exq_530_arc016_precision_commit/v3_exq_530_arc016_precision_commit_20260507T205242Z_v3.json` |

### No outcome recoverable (2)

| queue_id | claim_id | predecessor manifest on disk (sibling) |
|----------|----------|----------------------------------------|
| V3-EXQ-157a | Q-017 | `evidence/experiments/v3_exq_157_q017_control_axis_minimal_subset_20260330T065453Z_v3.json` |
| V3-EXQ-321c |  | `evidence/experiments/v3_exq_321_mech090_bistable_gate/v3_exq_321_mech090_bistable_gate_20260410T155906Z_v3.json` |

## Duplicates / supersession notes

Out of scope to re-flag in `claims.yaml` or manifests (this is a runner_status cleanup pass), but recorded for governance:

- **Lettered variant manifests lost while the predecessor base manifest survives (8):** these re-runs (per EXQ versioning, a lettered iteration supersedes its predecessor) dropped their own manifest; only the *earlier* base run's manifest is on disk. The runner-log outcome was kept in the report but **not** linked to the predecessor manifest (it is a different run). Governance should treat the variant's evidence as missing, not as the predecessor's result:
  - V3-EXQ-157a (log outcome none) — predecessor `evidence/experiments/v3_exq_157_q017_control_axis_minimal_subset_20260330T065453Z_v3.json`
  - V3-EXQ-321c (log outcome none) — predecessor `evidence/experiments/v3_exq_321_mech090_bistable_gate/v3_exq_321_mech090_bistable_gate_20260410T155906Z_v3.json`
  - V3-EXQ-385b (log outcome FAIL) — predecessor `evidence/experiments/v3_exq_385_inv049_offline_consolidation_necessity_20260414T220308Z_v3.json`
  - V3-EXQ-418b (log outcome FAIL) — predecessor `evidence/experiments/v3_exq_418_sd017_context_conditioned_action_20260416T172742Z_v3.json`
  - V3-EXQ-418c (log outcome FAIL) — predecessor `evidence/experiments/v3_exq_418_sd017_context_conditioned_action_20260416T172742Z_v3.json`
  - V3-EXQ-445e (log outcome FAIL) — predecessor `evidence/experiments/v3_exq_445_sd032b_dacc_analog/v3_exq_445_sd032b_dacc_analog_20260419T205642Z_v3.json`
  - V3-EXQ-490a (log outcome FAIL) — predecessor `evidence/experiments/v3_exq_490_mech269b_vs_rollout_gating/v3_exq_490_mech269b_vs_rollout_gating_20260427T080413Z_v3.json`
  - V3-EXQ-530b (log outcome FAIL) — predecessor `evidence/experiments/v3_exq_530_arc016_precision_commit/v3_exq_530_arc016_precision_commit_20260507T205242Z_v3.json`

- **Name-drift recoveries (8):** the lettered variant ran but wrote its manifest under the *base* experiment name/dir (script-name drift); accepted only because the manifest timestamp is within 120 s of the row's `completed_at`. These are genuine recoveries, not mislinks:
  - V3-EXQ-059b -> `evidence/experiments/v3_exq_059_arc016_beta_gate_fixed_threshold/v3_exq_059_arc016_beta_gate_fixed_threshold_20260320T204910Z.json` (FAIL, +1.5s)
  - V3-EXQ-170a -> `evidence/experiments/v3_exq_170_q002_r_field_resolution_pair_20260330T070234Z_v3.json` (FAIL, +1.2s)
  - V3-EXQ-171a -> `evidence/experiments/v3_exq_171_mech033_kernel_chain_pair_20260330T070404Z_v3.json` (PASS, +1.2s)
  - V3-EXQ-172a -> `evidence/experiments/v3_exq_172_arc018_rollout_viability_pair_20260330T070425Z_v3.json` (FAIL, +1.4s)
  - V3-EXQ-176a -> `evidence/experiments/v3_exq_176_arc036_valence_dimension_probe_20260330T070447Z_v3.json` (FAIL, +0.8s)
  - V3-EXQ-250b -> `evidence/experiments/v3_exq_250_inv054_phase_transition_recovery/v3_exq_250_inv054_phase_transition_recovery_1775541543.json` (INCONCLUSIVE, +1.2s)
  - V3-EXQ-447a -> `evidence/experiments/v3_exq_447_sd032d_pcc_stability/v3_exq_447_sd032d_pcc_stability_20260423T204632Z_v3.json` (PASS, +1.0s)
  - V3-EXQ-537a -> `evidence/experiments/v3_exq_537_sd029_single_pass_residual/v3_exq_537_sd029_single_pass_residual_20260508T135638Z_v3.json` (FAIL, +1.0s)

## Provenance

Each reclassified row carries a `reclassified_from_unknown` object (`manifest`, `result_source`, `match_basis`, `delta_sec`, `at`, `by`) and, where it was empty, `output_file` now points at the recovered manifest. Each left-UNKNOWN row carries an `unknown_triage_2026_06_02` marker. No `claims.yaml`, manifest, `review_tracker.json`, queue or evidence_direction edits were made; nothing was requeued.
