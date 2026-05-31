# Flat-vs-runs evidence_direction mismatch triage -- one-time scan 2026-05-31

## Context

build_experiment_indexes.py at evidence/experiments/scripts/build_experiment_indexes.py:294 globs `**/runs/**/manifest.json` only. The top-level flat JSON at `evidence/experiments/<run_id>.json` (emitted by experiment scripts via emit_outcome) is NOT read by the indexer. When a manifest is reclassified post-hoc (governance review changing `evidence_direction` / `evidence_direction_per_claim` / `evidence_direction_note`), the reclassification is sometimes applied only to the flat JSON and never propagated to the canonical runs manifest. Result: indexer-invisible reclassification.

Canonical incident: v3_exq_573_arc065_bias_scale_sweep had a 2026-05-16 governance reclassification of all four tagged claims (ARC-065 / MECH-313 / MECH-314 / MECH-320) to `non_contributory` applied to the flat JSON only. Fixed in REE_assembly commit c4d080082e 2026-05-31; that one entry cleared MECH-314 from the active conflicts table entirely.

This scan is the one-off follow-up the canonical-fix commit message recommended: walk every flat JSON and compare against its canonical runs manifest. Categorise mismatches; mirror the (a) cases where the runs manifest is missing a reclassification that's on the flat side; flag (b) and (c) for human review.

## Methodology

scripts/scan_flat_vs_runs_direction_mismatch.py walks every `evidence/experiments/<run_id>.json` flat manifest, pairs it with `evidence/experiments/<experiment_type>/runs/<run_id>/manifest.json`, compares three fields:

- evidence_direction
- evidence_direction_per_claim (full dict equality)
- evidence_direction_note (presence + value)

and assigns one of:

- (a) flat has reclassification (per_claim override and/or note) the runs manifest lacks -- mirror onto runs
- (b) runs has reclassification the flat lacks -- flag only (regenerating flat is out of scope this pass)
- (c) both have reclassifications that disagree on the value -- flag for human review
- (d) agree -- skip

## Summary

| Bucket | Count |
|---|---|
| Total flat manifests scanned | 231 |
| Skipped (no canonical runs manifest -- flat-only V2 manifests etc.) | 17 |
| (a) flat reclassification mirrored onto runs | 37 |
| (b) runs reclassification, flat stale (flagged only) | 7 |
| (c) genuine disagreement (flagged only) | 84 |
| (d) agree | 140 |

## Category (a) impact (applied this pass)

37 runs manifests had their `evidence_direction` / `evidence_direction_per_claim` / `evidence_direction_note` updated to mirror the flat JSON. After indexer rebuild + generate_pending_review.py, the active conflicts table is unchanged in membership (95 claims before and after) and identical in row content. Two below-the-fold deltas observed:

- MECH-333 and MECH-334 each gained a small exp_conf bump (0.423 -> 0.425) from absorbing the v3_exq_610a per_claim override.
- SD-016 entries v3_exq_418f / v3_exq_418h reclassified from `supports` / `weakens` (confidence 0.75 each) to `unknown` (confidence 0.45) -- the indexer now sees the `diagnostic` direction propagated from the flat JSON and correctly excludes these probes from active scoring.

The Category (a) work here is metadata-correctness rather than headline-moving. The reason: in 35 of 37 cases the flat and runs top-level `evidence_direction` agreed; what was missing on runs was the `evidence_direction_note` and/or `evidence_direction_per_claim` override -- which don't change indexer scoring when the top-level direction already covers them. The v3_exq_573 canonical case was unusual: its top-level direction itself was reclassified (weakens -> non_contributory), which is what moved MECH-314 out of conflicts.

## Per-entry Category (a) list (run_id + per_claim keys propagated)

| run_id | flat_dir (==runs_dir post-mirror) | per_claim keys propagated | note propagated |
|---|---|---|---|
| `v3_exq_255_mech203_benefit_tagging_v3` | non_contributory | (none) | yes |
| `v3_exq_256_mech203_balanced_replay_v3` | non_contributory | (none) | yes |
| `v3_exq_418a_sd016_sd017_context_conditioned_action_20260419T102434Z_v3` | non_contributory | SD-017 | yes |
| `v3_exq_418a_sd016_sd017_context_conditioned_action_20260420T033519Z_v3` | non_contributory | SD-017 | yes |
| `v3_exq_418e_sd016_diversification_loss_20260427T015954Z_v3` | does_not_support | (none) | yes |
| `v3_exq_418e_sd016_diversification_loss_20260427T054442Z_v3` | does_not_support | (none) | yes |
| `v3_exq_418f_sd016_attention_uniformity_probe_20260428T203014Z_v3` | diagnostic | (none) | yes |
| `v3_exq_418f_sd016_attention_uniformity_probe_20260428T211430Z_v3` | diagnostic | (none) | yes |
| `v3_exq_418h_sd016_env_entropy_precondition_20260428T205850Z_v3` | diagnostic | (none) | yes |
| `v3_exq_418i_sd016_divweight_sweep_20260504T221922Z_v3` | does_not_support | (none) | yes |
| `v3_exq_449_sd016_cue_action_proj_wiring_probe_20260420T143953Z_v3` | diagnostic | (none) | yes |
| `v3_exq_449a_sd016_cue_action_proj_forward_path_probe_20260421T181058Z_v3` | diagnostic | (none) | yes |
| `v3_exq_449a_sd016_cue_action_proj_forward_path_probe_20260421T202422Z_v3` | diagnostic | (none) | yes |
| `v3_exq_449b_sd016_cue_action_proj_consumer_fix_20260424T021756Z_v3` | diagnostic | (none) | yes |
| `v3_exq_477_sd016_context_memory_slot_store_diagnostic_20260424T080649Z_v3` | diagnostic | (none) | yes |
| `v3_exq_484_sd033a_distractor_resistance_20260427T054449Z_v3` | supports | MECH-261, MECH-262, SD-033a | yes |
| `v3_exq_490j_mech295_cascade_gap4_tier1_severed_bridge_baseline_20260531T112417Z_v3` | weakens | MECH-295 | yes |
| `v3_exq_493_mech295_liking_bridge_validation_20260427T080304Z_v3` | supports | MECH-117, MECH-295, SD-012, SD-014, SD-015 | yes |
| `v3_exq_541_mech204_precision_recalibration_consumer_20260508T234302Z_v3` | superseded | MECH-204 | yes |
| `v3_exq_543_arc062_phase2a_monomodal_collapse_falsifier_20260509T214517Z_v3` | non_contributory | ARC-062, MECH-309, SD-029 | yes |
| `v3_exq_543i_arc062_differential_heads_falsifier_20260518T191052Z_v3` | non_contributory | ARC-062, INV-074, MECH-309, MECH-334 | yes |
| `v3_exq_543i_arc062_differential_heads_falsifier_20260521T035802Z_v3` | non_contributory | ARC-062, INV-074, MECH-309, MECH-334 | yes |
| `v3_exq_563b_candidate_support_repair_20260514T205949Z_v3` | non_contributory | ARC-065, MECH-320 | yes |
| `v3_exq_563c_stratified_cem_bias_calibration_20260515T201559Z_v3` | non_contributory | ARC-065, MECH-320 | yes |
| `v3_exq_567_wpb_natural_entropy_sp_cem_20260515T203126Z_v3` | supports | (none) | yes |
| `v3_exq_567_wpb_natural_entropy_sp_cem_20260515T212425Z_v3` | supports | (none) | yes |
| `v3_exq_569d_sd056_action_contrastive_diversity_falsifier_floor_recal_20260531T053648Z_v3` | supports | ARC-065, MECH-341 | yes |
| `v3_exq_583_spcem_mainpath_default_wiring_20260517T092510Z_v3` | non_contributory | (none) | yes |
| `v3_exq_598_gap1_sd033a_bias_head_trainable_ablation_20260521T070715Z_v3` | non_contributory | SD-033a | yes |
| `v3_exq_604_q044_mech314_subflavour_three_arm_ablation_20260521T112110Z_v3` | non_contributory | MECH-314, MECH-314a, MECH-314b, MECH-314c, Q-044 | yes |
| `v3_exq_605_q043_noise_floor_curiosity_weight_sweep_20260521T115421Z_v3` | non_contributory | ARC-065, MECH-313, MECH-314, Q-043 | yes |
| `v3_exq_608_mech341_e3_score_collapse_diagnostic_20260526T025832Z_v3` | non_contributory | (none) | yes |
| `v3_exq_610a_inv074_crystallization_necessity_20260529T224419Z_v3` | mixed | INV-074, MECH-333, MECH-334, MECH-341 | yes |
| `v3_exq_611_mech341_substrate_readiness_4arm_20260527T130213Z_v3` | non_contributory | (none) | yes |
| `v3_exq_611c_mech341_retune_6arm_20260529T184549Z_v3` | non_contributory | (none) | yes |
| `v3_exq_614a_mech341_p3_behavioural_falsifier_3arm_20260530T193245Z_v3` | supports | ARC-065, MECH-341 | yes |
| `v3_exq_616_q054_mech341_entropy_bias_scale_sweep_20260531T141508Z_v3` | weakens | MECH-341, Q-054 | yes |

## Category (b) -- runs has reclassification, flat is stale (FLAG; do NOT mutate flat in this pass)

Reverse of category (a). Flat JSON predates the runs-side reclassification. Conservative: surface only, do not regenerate flat in this pass (out of scope per user brief).

| run_id | flat_dir | runs_dir | runs_per_claim_keys | runs_note? |
|---|---|---|---|---|
| `v3_exq_151_q006_ethics_developmental_20260329T131721Z_v3` | mixed | mixed | - | yes |
| `v3_exq_172_arc018_rollout_viability_pair_20260329T213638Z_v3` | inconclusive | inconclusive | - | yes |
| `v3_exq_266a_q020_valence_geometry_pair_fixed_20260411T095750Z_v3` | non_contributory | non_contributory | Q-020 | yes |
| `v3_exq_570_e2_rollout_collapse_diagnostic_20260515T232232Z_v3` | - | unknown | - | no |
| `v3_exq_584_gap7_traj_cosine_validation_20260518T222522Z_v3` | - | unknown | - | no |
| `v3_exq_612_phase3_cutover_smoke_20260528T175700Z_v3` | - | unknown | - | no |
| `v3_exq_612_phase3_cutover_smoke_20260529T214609Z_v3` | - | unknown | - | no |

## Category (c) -- genuine disagreement (FLAG; do not auto-resolve)

Total: 84. Bucketed by likely shape for review.

### (c.1) flat=superseded, runs=supports/weakens (14 entries)

Likely same propagation-failure shape as category (a): supersession reclassification applied to flat only; runs kept the original verdict. The indexer reads runs and so it still scores these as supports/weakens. The conservative-because-asymmetric move is to mirror these onto runs (same pattern as the v3_exq_573 canonical fix); deferred this pass per user direction ('Be conservative with category (c)').

| run_id | flat_dir | runs_dir |
|---|---|---|
| `v3_exq_265_sd017_sleep_phase_methods_validation_20260409T181835Z_v3` | superseded | supports |
| `v3_exq_484_sd033a_distractor_resistance_20260426T101114Z_v3` | superseded | weakens |
| `v3_exq_484_sd033a_distractor_resistance_20260426T101225Z_v3` | superseded | supports |
| `v3_exq_484_sd033a_distractor_resistance_20260427T014901Z_v3` | superseded | supports |
| `v3_exq_484_sd033a_distractor_resistance_20260427T015957Z_v3` | superseded | supports |
| `v3_exq_485_sd033b_ofc_analog_landing_20260426T104928Z_v3` | superseded | supports |
| `v3_exq_485_sd033b_ofc_analog_landing_20260427T014906Z_v3` | superseded | supports |
| `v3_exq_485_sd033b_ofc_analog_landing_20260427T020003Z_v3` | superseded | supports |
| `v3_exq_493_mech295_liking_bridge_validation_20260427T020011Z_v3` | superseded | supports |
| `v3_exq_493_mech295_liking_bridge_validation_20260427T033832Z_v3` | superseded | supports |
| `v3_exq_500_sd017_sleep_phase_readiness_20260429T192752Z_v3` | superseded | supports |
| `v3_exq_503_sd017_sleep_phase_discriminative_20260501T201518Z_v3` | superseded | supports |
| `v3_exq_543g_arc062_outcome_coupled_falsifier_20260517T144716Z_v3` | superseded | weakens |
| `v3_exq_543h_arc062_crystallization_falsifier_20260518T060905Z_v3` | superseded | weakens |

### (c.1b) flat=superseded, runs=non_contributory (7 entries)

Same shape as c.1 but runs already scores as inert (non_contributory) -- the disagreement is metadata-only. Lower priority.

| run_id | flat_dir | runs_dir |
|---|---|---|
| `v3_exq_429_inv044_bayesian_prior_before_posterior_20260415T143340Z_v3` | superseded | non_contributory |
| `v3_exq_543b_arc062_phase3_optimized_falsifier_20260510T172558Z_v3` | superseded | non_contributory |
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T125958Z_v3` | superseded | non_contributory |
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130046Z_v3` | superseded | non_contributory |
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130300Z_v3` | superseded | non_contributory |
| `v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T140320Z_v3` | superseded | non_contributory |
| `v3_exq_543h_arc062_crystallization_falsifier_20260518T000930Z_v3` | superseded | non_contributory |

### (c.2) flat=non_contributory, runs=weakens/does_not_support (15 entries)

Same shape as c.1: governance soft-deprecation applied to flat only. Runs is more harsh than flat; indexer is reading runs, so weakens / does_not_support counts may be inflated. Flag for human review.

| run_id | flat_dir | runs_dir |
|---|---|---|
| `v3_exq_355a_arc038_schema_assimilation_probe_20260418T225626Z_v3` | non_contributory | does_not_support |
| `v3_exq_418g_sd016_selectivity_first_4arm_20260428T203517Z_v3` | non_contributory | does_not_support |
| `v3_exq_418l_sd017_action_bias_div_phase2_20260509T215331Z_v3` | non_contributory | does_not_support |
| `v3_exq_430_inv010_offline_integration_necessity_20260419T123934Z_v3` | non_contributory | does_not_support |
| `v3_exq_436a_sd017_arc045_mech166_context_harm_phase2_20260509T214636Z_v3` | non_contributory | weakens |
| `v3_exq_517_mech302_relief_completion_discriminative_pair_20260504T132505Z_v3` | non_contributory | weakens |
| `v3_exq_517_mech302_relief_completion_discriminative_pair_20260504T132543Z_v3` | non_contributory | weakens |
| `v3_exq_517_mech302_relief_completion_discriminative_pair_20260504T150341Z_v3` | non_contributory | weakens |
| `v3_exq_549_arc066_tonic_vigor_discriminative_pair_20260511T190124Z_v3` | non_contributory | weakens |
| `v3_exq_569_wpb_matched_entropy_sweep_20260516T003830Z_v3` | non_contributory | weakens |
| `v3_exq_572_intervention_a_dual_attractor_20260516T063719Z_v3` | non_contributory | weakens |
| `v3_exq_572_intervention_a_dual_attractor_20260516T063813Z_v3` | non_contributory | weakens |
| `v3_exq_572_intervention_a_dual_attractor_20260516T064121Z_v3` | non_contributory | weakens |
| `v3_exq_572_intervention_a_dual_attractor_20260516T095117Z_v3` | non_contributory | weakens |
| `v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T111759Z_v3` | non_contributory | weakens |

### (c.3) runs=superseded, flat!=superseded (13 entries)

Reverse shape: supersession was applied to runs (or runs was always superseded) but never propagated to flat. Indexer correctly excludes these from scoring (reads runs); flag is metadata-consistency only.

| run_id | flat_dir | runs_dir |
|---|---|---|
| `v3_exq_150_q005_sleep_anneal_20260329T131504Z_v3` | mixed | superseded |
| `v3_exq_154_q014_jepa_invariance_blind_spot_20260329T190928Z_v3` | mixed | superseded |
| `v3_exq_155_q015_commit_boundary_minimal_contract_20260329T191541Z_v3` | mixed | superseded |
| `v3_exq_156_q016_tri_loop_arbitration_policy_20260329T192850Z_v3` | mixed | superseded |
| `v3_exq_157_q017_control_axis_minimal_subset_20260329T081401Z_v3` | mixed | superseded |
| `v3_exq_157_q017_control_axis_minimal_subset_20260329T185928Z_v3` | mixed | superseded |
| `v3_exq_159_q020_arc007_valence_constraint_pair_20260329T193606Z_v3` | weakens | superseded |
| `v3_exq_160_q023_multiagent_convergence_pair_20260329T194510Z_v3` | mixed | superseded |
| `v3_exq_161_q024_trajectory_representation_triple_20260329T104847Z_v3` | mixed | superseded |
| `v3_exq_161_q024_trajectory_representation_triple_20260329T200440Z_v3` | mixed | superseded |
| `v3_exq_264_arc033_e2_harm_s_forward_20260409T170322Z_v3` | does_not_support | superseded |
| `v3_exq_266_q020_valence_geometry_pair_20260410T023257Z_v3` | does_not_support | superseded |
| `v3_exq_266_q020_valence_geometry_pair_20260410T034439Z_v3` | does_not_support | superseded |

### (c.4) Other direction-disagreement (14 entries)

Mixed directions, weakens vs non_contributory, does_not_support vs inconclusive. Harder to attribute a clean sync direction without per-entry inspection. Listed for completeness; recommend per-entry triage at next governance pass.

| run_id | flat_dir | runs_dir |
|---|---|---|
| `v3_exq_157_q017_control_axis_minimal_subset_20260330T065453Z_v3` | mixed | inconclusive |
| `v3_exq_177_sd008_integration_test_20260329T215657Z_v3` | weakens | mixed |
| `v3_exq_214_arc039_entorhinal_consolidation_probe_20260403T202345Z_v3` | weakens | non_contributory |
| `v3_exq_260_sd020_harm_surprise_pe_20260408T231126Z_v3` | weakens | non_contributory |
| `v3_exq_261_sd021_descending_pain_mod_20260408T231136Z_v3` | weakens | non_contributory |
| `v3_exq_267_arc038_waking_consolidation_discriminative_20260410T093618Z_v3` | does_not_support | non_contributory |
| `v3_exq_324a_sd020_harm_surprise_pe_20260416T172747Z_v3` | does_not_support | inconclusive |
| `v3_exq_355_arc038_schema_assimilation_probe_20260414T220207Z_v3` | does_not_support | non_contributory |
| `v3_exq_385_inv049_offline_consolidation_necessity_20260414T220308Z_v3` | does_not_support | non_contributory |
| `v3_exq_418_sd017_context_conditioned_action_20260416T172742Z_v3` | does_not_support | non_contributory |
| `v3_exq_548_sd054_bipartite_substrate_readiness_20260511T162233Z_v3` | non_contributory | supports |
| `v3_exq_596_mech204_sleep_cluster_stepharness_integration_20260520T044151Z_v3` | inconclusive_measurement | non_contributory |
| `v3_exq_596_mech204_sleep_cluster_stepharness_integration_20260521T085838Z_v3` | inconclusive_measurement | non_contributory |
| `v3_exq_603b_q045_mech313_mech260_four_arm_ablation_20260526T071458Z_v3` | non_contributory | mixed |

### (c.5) per_claim-only disagreement (5 entries)

evidence_direction agrees but the per-claim dict disagrees on at least one claim. Lowest priority; per-claim values can drift legitimately as governance refines a single-claim attribution.

| run_id | dir | flat_per_claim | runs_per_claim |
|---|---|---|---|
| `v3_exq_257_sd018_resource_prox_validation_20260406T171952Z_v3` | mixed | `{'SD-018': 'weakens', 'ARC-030': 'weakens', 'MECH-112': 'weakens'}` | `{'SD-018': 'weakens', 'ARC-030': 'non_contributory', 'MECH-112': 'non_contributory'}` |
| `v3_exq_485_sd033b_ofc_analog_landing_20260427T054454Z_v3` | supports | `{'SD-033b': 'supports', 'MECH-261': 'supports', 'MECH-263': 'non_contributory'}` | `{'SD-033b': 'supports', 'MECH-261': 'supports', 'MECH-263': 'supports'}` |
| `v3_exq_543d_arc062_mech260_factorial_falsifier_20260512T010638Z_v3` | non_contributory | `{'ARC-062': 'non_contributory', 'MECH-309': 'non_contributory'}` | `{'ARC-062': 'weakens', 'MECH-309': 'non_contributory'}` |
| `v3_exq_543e_arc062_spcem_falsifier_20260517T010202Z_v3` | non_contributory | `{'ARC-062': 'non_contributory', 'MECH-309': 'non_contributory'}` | `{'ARC-062': 'weakens', 'MECH-309': 'non_contributory'}` |
| `v3_exq_598b_gap1_sd033a_bias_head_trainable_ablation_20260527T120345Z_v3` | mixed | `{'SD-033a': 'supports', 'MECH-262': 'non_contributory'}` | `{'SD-033a': 'supports', 'MECH-262': 'weakens'}` |

### (c.6) mixed_extras (16 entries)

Both flat and runs carry non-trivial reclassification content but neither strictly dominates along the three fields. Most are entries where one side has a note and the other has a per_claim override (or vice versa). Listed for completeness.

| run_id | flat_dir | runs_dir | flat_note? | runs_note? |
|---|---|---|---|---|
| `v3_exq_196_arc018_rollout_viability_pair_20260404T164611Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_262_mech220_harm_hub_20260408T231100Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_385a_inv049_offline_consolidation_necessity_20260418T210738Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_385a_inv049_offline_consolidation_necessity_20260418T212839Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_385a_inv049_offline_consolidation_necessity_20260418T225721Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_418a_sd016_sd017_context_conditioned_action_20260418T230019Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_418d_sd016_writepath_modes_comparison_20260425T141932Z_v3` | does_not_support | does_not_support | y | y |
| `v3_exq_523_sd029_reef_comparator_20260505T180800Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_543j_arc062_differential_heads_xmachine_confirm_20260519T080741Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_563_action_bias_actuator_test_20260514T183416Z_v3` | superseded | superseded | y | y |
| `v3_exq_563a_action_bias_scaffold_actuator_test_20260514T194658Z_v3` | superseded | superseded | y | y |
| `v3_exq_569c_sd056_action_contrastive_diversity_falsifier_20260530T124450Z_v3` | superseded | superseded | y | y |
| `v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T142648Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T204222Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_603a_q045_mech313_mech260_four_arm_ablation_20260524T170349Z_v3` | non_contributory | non_contributory | y | y |
| `v3_exq_606_arc064_gap_i_mech318_multi_rule_empirical_gate_20260521T090253Z_v3` | non_contributory | non_contributory | y | y |

## Active conflicts table -- before vs after delta

- Claims in table: 95 -> 95 (no membership change)
- Claim rows in the conflict queue table: byte-identical pre/post

The mirrored category (a) entries did not move the headline. The two visible scoring changes are below-the-fold:
- MECH-333 / MECH-334 exp_conf bump 0.423 -> 0.425 from v3_exq_610a per_claim absorption
- SD-016 v3_exq_418f / v3_exq_418h re-tagged from supports / weakens (conf=0.75) to unknown (conf=0.45) per `diagnostic` direction now visible on runs side

## Root-cause follow-up recommendation (separate session)

The asymmetry surfaced here re-confirms the c4d080082e follow-up note: the reclassify workflow should write to the canonical `runs/<run_id>/manifest.json` as primary. The top-level flat JSON should either be auto-synced (write-through) or dropped from the schema entirely -- it is currently silently authoritative-looking but indexer-invisible. The category (c.1) / (c.2) buckets below total 29 entries with the same pathology -- a follow-on session that takes a less-conservative line (mirror flat->runs when one side is `superseded` or `non_contributory` and the other is `supports` / `weakens`) would likely flush more weakens / does_not_support entries from active scoring than this pass did.

