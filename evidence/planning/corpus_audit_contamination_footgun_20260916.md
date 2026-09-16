# Corpus audit 1 -- agent_health contamination footgun exposure (read-only)

**Status: COMPLETE 2026-09-16T23:06:31Z (chip `chip-20260916-corpus-audits-contamination-immobility`, worktree `angry-leakey-c8b0a0`). Read-only: no manifest touched, no regen run, nothing queued. Companion report: `corpus_audit_immobility_signature_20260916.md`.**

## 0. Provenance

- Trigger: `mech467_govfanout_portfolio_staged_2026-08-19.md` item 5 ("consider a corpus-wide contamination-footgun audit if V3-EXQ-940 confirms C1"); C1 PASSED (`failure_autopsy_940-941-mech467-cluster_2026-08-20.md`); user decision 2026-09-16 to run both audits as reports.
- The footgun, as documented in `ree-v3/ree_core/environment/causal_grid_world.py` (module docstring SD-094 note 2, constructor comment at `hazard_free_contamination_gate`, lines ~60-79 and ~180-200): `contamination_spread` defaults to **0.5** and is applied to EVERY cell the agent enters regardless of `num_hazards`; a cell crossing `contamination_threshold` (2.0, i.e. four entries) becomes `contaminated` and drains `contaminated_harm` (0.4) per re-entry, so ~three contacts are lethal from full health. A `num_hazards=0` ("hazard-free") probe therefore still kills its own agent unless it opts out with `contamination_spread=0.0` (V3-EXQ-513 precedent) or `hazard_free_contamination_gate=True` (no effect when `num_hazards > 0`). Toroidal wrap (`toroidal=True`, default False) removes the walls that channel exploration into fresh cells and so makes the revisitation that accumulates contamination faster (`navigation_immobility_scoping_2026-08-18.md` section 4) -- it is an amplifier, not the trigger; V3-EXQ-874b was non-toroidal and still exposed.

**Exposure definition used here (from the env source, not guessed):** environment is `CausalGridWorld`/`CausalGridWorldV2` AND some configured arm sets `num_hazards=0` AND neither opt-out (`contamination_spread=0.0`, `hazard_free_contamination_gate=True`) is set anywhere in that run. `toroidal=True` is reported as a column (the chip's wording "wrap on, opt-out absent" is the narrower amplified case; it is a strict subset of the definition above and is called out separately). `num_hazards > 0` configs at stock contamination defaults are NOT counted as exposed: there contamination is the intended hazard ecology, not a footgun.

## 1. What was scanned

| Corpus | Count |
|---|---|
| Per-run pack manifests `evidence/experiments/*/runs/*/manifest.json` (authoritative scoring source; memory `reference_indexer_reads_runs_pack_not_flat`) | 2958 |
| ... of which `claim_ids_tested` non-empty | 2698 |
| ... of which "scored" under the chip definition (claim_ids non-empty AND `evidence_direction != superseded`) | 2519 |
| Flat top-level manifests `evidence/experiments/*.json` | 1042 |
| ... of which have NO pack sibling (flat-only, inert for scoring) | 18 |
| Experiment scripts `ree-v3/experiments/*.py` consulted for env kwargs | 1501 (CausalGridWorld referenced in 1251) |
| `claim_evidence.v1.json` experimental entries used for the per-claim share | 2293 chip-def / 685 indexer-scored (`scoring_excluded` null) |

## 2. Schema keys used (real, observed -- not guessed)

- Env identity: manifest `environment.env_id == "ree.causal_grid_world_v3"` (1745 packs; 1141 packs carry `environment: null`) OR the run's script references `CausalGridWorld`.
- Env kwargs in manifests, wherever nested (the four key names are searched at every depth): most common paths `config.env_kwargs.num_hazards` (100), `config.num_hazards` (97), `config.env_kwargs.toroidal` (78), `config.env.num_hazards` (51), `config.env_base.{num_hazards,toroidal}` (20), `config.contamination_spread` (9), `config.env_kwargs_gated.hazard_free_contamination_gate` (V3-EXQ-940), per-arm slices `config.arm_config_slices.<ARM>.env.num_hazards`, `config.{threat,neutral,familiar,novel}_env_kwargs.*`. Only ~300 of 2958 packs record ANY of the four kwargs, so the manifest alone is under-determined.
- Script fallback: `ree-v3/experiments/<pack dir name>.py` (1325 of 1427 pack dirs map exactly; a unique `v3_exq_<id>_*.py` glob recovers most of the rest). Kwargs are read by AST -- `Call` keywords and dict literals for the four names, with module-level constants (`N_HAZARDS = 4`, `NUM_HAZARDS = {...}`), and function-default parameters (`num_hazards: int = 3`) resolved; comment/docstring mentions are ignored. A script whose value is computed at runtime (e.g. `B.NUM_HAZARDS` from a `_lib` module, a CLI arg) is `UNDETERMINED`.
- Scoring: `claim_ids_tested`, `evidence_direction`, `status` from the pack manifest; `claim_evidence.v1.json` entries with `source_type == experimental`, matched to packs on `run_id` with or without the `_YYYYMMDDTHHMMSSZ` stamp (31 entries could not be matched to a pack and are excluded from the per-claim share).
- Autopsy coverage: `scripts/check_autopsy_coverage.py <run_id>... --repo REE_assembly --format json` (content-based, over the 513 `failure_autopsy_*.json` artifacts).

## 3. Exposure classes over the whole pack corpus

| Class | Packs | Of which chip-scored |
|---|---|---|
| **EXPOSED** -- hazard-free arm(s), no opt-out | 92 | 60 |
| Hazard-free with an opt-out present (940: one arm deliberately un-gated as its reproduction arm; 1004/1007/1039: gate/spread=0 set) | 4 | 4 |
| Opt-out set with num_hazards > 0 (contamination off entirely) | 19 | 9 |
| CausalGridWorld with num_hazards > 0 (stock 3 when unset) -- contamination is the intended ecology | 1444 | 1110 |
| CausalGridWorld, `num_hazards` mentioned in the script but not resolvable statically | 120 | 80 |
| CausalGridWorld env_id, no script found, no kwargs recorded | 84 | 68 |
| Not a CausalGridWorld run (legacy `claim_probe_*`, `jepa_*`, `commit_dual_*`, bridging/JEPA qualification, ...) | 1195 | 1188 |

Toroidal runs in the whole corpus: 6 (V3-EXQ-642/642a/642b/642c exposed+toroidal; V3-EXQ-577/577a/223a/981a toroidal but hazards > 0 or not in the pack corpus). So the chip's literal 'wrap on + no opt-out' set is **4 runs, none chip-scored**; the documented footgun (hazard-free + no opt-out, any wrap) is **92 runs, 60 chip-scored**.

## 4. Table A -- EXPOSED runs (92; 'S' = chip-scored)

| # | queue_id | run_id | date | claim_ids | status / direction | S | exposure detail | existing autopsy |
|---|---|---|---|---|---|---|---|---|
| 1 | V3-EXQ-067 | v3_exq_067_mech026_ready_vigilance_20260322T234028Z_v3 | 2026-03-22 | MECH-026 | FAIL / unknown | S | all arms hazard-free; src=script | grandfathered-r6-closure-sweep_2026-08-08 (confirmed) |
| 2 | V3-EXQ-1002 | v3_exq_1002_zworld_actor_adequacy_oracle_adapter_20260905T005017Z_v3 | 2026-09-05 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=manifest | V3-EXQ-1002_2026-09-05 (confirmed) |
| 3 | V3-EXQ-1008 | v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis_20260907T233826Z_v3 | 2026-09-07 | (none) | PASS / non_contributory |  | all arms hazard-free; src=manifest | V3-EXQ-1008_2026-09-08 (confirmed) |
| 4 | V3-EXQ-1010 | v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3 | 2026-09-09 | (none) | PASS / non_contributory |  | all arms hazard-free; src=manifest | V3-EXQ-1010_2026-09-11 (confirmed) |
| 5 | V3-EXQ-1023 | v3_exq_1023_sd106_bottleneck_preservation_validation_20260912T045319Z_v3 | 2026-09-12 | SD-106 | FAIL / mixed | S | all arms hazard-free; src=manifest | V3-EXQ-1023_2026-09-14 (confirmed) |
| 6 | V3-EXQ-1040 | v3_exq_1040_sd077_centered_super_ordinal_cue_key_20260915T021006Z_v3 | 2026-09-15 | SD-077 | PASS / supports | S | all arms hazard-free; src=script | no |
| 7 | V3-EXQ-1041 | v3_exq_1041_sd106_preservation_step_budget_metric_diagnostic_20260915T203743Z_v3 | 2026-09-15 | SD-106 | PASS / non_contributory | S | all arms hazard-free; src=manifest | V3-EXQ-1041_2026-09-16 (confirmed) |
| 8 | V3-EXQ-1043 | v3_exq_1043_mech537_communication_subspace_routing_20260916T111630Z_v3 | 2026-09-16 | MECH-537 | FAIL / mixed | S | all arms hazard-free; src=manifest | no |
| 9 | V3-EXQ-1044 | v3_exq_1044_hippocampal_assay_a_access_mechanism_20260916T141717Z_v3 | 2026-09-16 | (none) | FAIL / weakens |  | all arms hazard-free; src=manifest | no |
| 10 | V3-EXQ-206 | v3_exq_206_inv043_ethical_capacity_probe_20260402T230611Z_v3 | 2026-04-02 | INV-043 | PASS / supports | S | hazard-free arm(s) only (num_hazards seen: 0, 4); src=script | no |
| 11 | V3-EXQ-231a | v3_exq_231a_mech106_bg_hysteresis_redesign_20260404T231335Z_v3 | 2026-04-04 | MECH-106 | PASS / supports | S | hazard-free arm(s) only (num_hazards seen: 0, 2, 5); src=script | no |
| 12 | V3-EXQ-278 | v3_exq_278_inv054_depression_recovery_phase_transition_1775764609_v3 | 2026-04-09 | INV-054 | FAIL / does_not_support | S | hazard-free arm(s) only (num_hazards seen: 0, 3); src=script | grandfathered-r6-closure-sweep_2026-08-08 (confirmed) |
| 13 | V3-EXQ-435 | v3_exq_435_inv054_phase_transition_sustained_recovery_1776556189_v3 | 2026-04-18 | INV-054 | FAIL / non_contributory | S | hazard-free arm(s) only (num_hazards seen: 0, 3); src=script | grandfathered-r6-closure-sweep_2026-08-08 (confirmed) |
| 14 | V3-EXQ-435 | v3_exq_435_inv054_phase_transition_sustained_recovery_1776660122_v3 | 2026-04-20 | INV-054 | FAIL / non_contributory | S | hazard-free arm(s) only (num_hazards seen: 0, 3); src=script | grandfathered-r6-closure-sweep_2026-08-08 (confirmed) |
| 15 | V3-EXQ-514b | v3_exq_514b_sd049_phase_2_behavioural_validation_20260505T005802Z_v3 | 2026-05-05 | SD-049, SD-015, MECH-229, MECH-230 | FAIL / weakens | S | all arms hazard-free; src=script | grandfathered-goalseeding-cluster_2026-08-08 (confirmed) |
| 16 | V3-EXQ-514d | v3_exq_514d_sd049_bg_gating_diagnostic_20260506T013506Z_v3 | 2026-05-06 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=script | no |
| 17 | V3-EXQ-514e | v3_exq_514e_bg_gating_seaweed_diagnostic_20260506T064842Z_v3 | 2026-05-06 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=script | no |
| 18 | V3-EXQ-519b | v3_exq_519b_sd051_conditioned_safety_store_readiness_20260531T065940Z_v3 | 2026-05-31 | MECH-304 | PASS / supports | S | all arms hazard-free; src=script | no |
| 19 | V3-EXQ-590b | v3_exq_590b_mech314a_novelty_goldilocks_20260611T211806Z_v3 | 2026-06-11 | MECH-314a | FAIL / does_not_support | S | all arms hazard-free; src=manifest+script | batch9_2026-06-12 (confirmed) |
| 20 | V3-EXQ-590c | v3_exq_590c_mech314_novelty_goldilocks_20260624T105537Z_v3 | 2026-06-24 | MECH-314, DEV-NEED-003 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-590c_2026-06-24 (confirmed) |
| 21 | V3-EXQ-590c | v3_exq_590c_mech314_novelty_goldilocks_20260719T172632Z_v3 | 2026-07-19 | MECH-314, DEV-NEED-003 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 22 | V3-EXQ-626b | v3_exq_626b_goal_pipeline_forced_seed_positive_control_20260603T211703Z_v3 | 2026-06-03 | (none) | PASS / unknown |  | all arms hazard-free; src=script | no |
| 23 | V3-EXQ-636 | v3_exq_636_sd057_object_bound_incentive_mechanism_20260604T073038Z_v3 | 2026-06-04 | (none) | PASS / unknown |  | all arms hazard-free; src=script | no |
| 24 | V3-EXQ-642 | v3_exq_642_blocked_agency_zblock_discriminative_20260606T055351Z_v3 | 2026-06-06 | (none) | FAIL / unknown |  | all arms hazard-free; TOROIDAL; src=script | V3-EXQ-642_2026-06-06 (confirmed) |
| 25 | V3-EXQ-642a | v3_exq_642a_blocked_agency_zblock_discriminative_20260829T185417Z_v3 | 2026-08-29 | (none) | FAIL / non_contributory |  | all arms hazard-free; TOROIDAL; src=manifest+script | V3-EXQ-642a_2026-08-30 (confirmed); V3-EXQ-642b_2026-09-01 (confirmed) |
| 26 | V3-EXQ-642b | v3_exq_642b_blocked_agency_calibrated_floor_validation_20260831T131011Z_v3 | 2026-08-31 | (none) | FAIL / non_contributory |  | all arms hazard-free; TOROIDAL; src=manifest | V3-EXQ-642b_2026-09-01 (confirmed); V3-EXQ-642c_2026-09-05 (confirmed) |
| 27 | V3-EXQ-642c | v3_exq_642c_blocked_agency_headroom_dv_validation_20260904T214459Z_v3 | 2026-09-04 | (none) | PASS / non_contributory |  | all arms hazard-free; TOROIDAL; src=manifest | V3-EXQ-642c_2026-09-05 (confirmed) |
| 28 | V3-EXQ-648 | v3_exq_648_mech314a_phase2_substrate_readiness_20260607T025417Z_v3 | 2026-06-07 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=manifest+script | V3-EXQ-648_2026-06-07 (confirmed) |
| 29 | V3-EXQ-648a | v3_exq_648a_mech314a_phase2_substrate_readiness_20260607T105407Z_v3 | 2026-06-07 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=manifest+script | gapA-cluster-604b-648a-649_2026-06-07 (confirmed) |
| 30 | V3-EXQ-649 | v3_exq_649_arc065_gapa_shared_candidate_summary_source_20260607T131429Z_v3 | 2026-06-07 | (none) | PASS / non_contributory |  | all arms hazard-free; src=manifest+script | gapA-cluster-604b-648a-649_2026-06-07 (confirmed) |
| 31 | V3-EXQ-651 | v3_exq_651_arc060_blocked_goal_recovery_20260607T131928Z_v3 | 2026-06-07 | ARC-060 | FAIL / non_contributory | S | all arms hazard-free; src=script | V3-EXQ-651_2026-06-07 (confirmed) |
| 32 | V3-EXQ-651a | v3_exq_651a_arc060_blocked_goal_recovery_20260607T150734Z_v3 | 2026-06-07 | ARC-060 | FAIL / non_contributory | S | all arms hazard-free; src=script | V3-EXQ-603g-624c-651a_2026-06-07 (confirmed) |
| 33 | V3-EXQ-659 | v3_exq_659_mech074a_bla_encoding_gain_replay_bias_20260609T200751Z_v3 | 2026-06-09 | MECH-074a | PASS / supports | S | hazard-free arm(s) only (num_hazards seen: 0, 4); src=script | no |
| 34 | V3-EXQ-662 | v3_exq_662_modulatory_channel_routing_substrate_readiness_20260610T104730Z_v3 | 2026-06-10 | (none) | PASS / non_contributory |  | all arms hazard-free; src=manifest | no |
| 35 | V3-EXQ-663 | v3_exq_663_modulatory_channel_routing_substrate_readiness_20260610T134823Z_v3 | 2026-06-10 | (none) | PASS / non_contributory |  | all arms hazard-free; src=manifest+script | no |
| 36 | V3-EXQ-669b | v3_exq_669b_mech329_wanting_first_goal_seeding_20260613T123433Z_v3 | 2026-06-13 | MECH-329, MECH-189 | FAIL / non_contributory | S | all arms hazard-free; src=script | grandfathered-r5-batch01-mixed-findings_2026-08-08 (confirmed) |
| 37 | V3-EXQ-669c | v3_exq_669c_mech329_wanting_first_goal_seeding_20260722T214724Z_v3 | 2026-07-22 | MECH-329, MECH-189 | FAIL / mixed | S | all arms hazard-free; src=script | backlog_2026-07-24 (confirmed) |
| 38 | V3-EXQ-681 | v3_exq_681_sd057_wl_channel_write_forced_contact_microdiagnostic_20260614T201458Z_v3 | 2026-06-14 | (none) | PASS / non_contributory |  | all arms hazard-free; src=script | no |
| 39 | V3-EXQ-705 | v3_exq_705_mech314_curiosity_conversion_demotion_20260625T033702Z_v3 | 2026-06-25 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-705_2026-06-25 (confirmed) |
| 40 | V3-EXQ-705 | v3_exq_705_mech314_curiosity_conversion_demotion_20260719T170212Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 41 | V3-EXQ-705 | v3_exq_705_mech314_curiosity_conversion_demotion_20260719T174907Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 42 | V3-EXQ-705b | v3_exq_705b_mech314_curiosity_conversion_demotion_adaptive_floor_20260625T100722Z_v3 | 2026-06-25 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-705b_2026-06-25 (confirmed) |
| 43 | V3-EXQ-705b | v3_exq_705b_mech314_curiosity_conversion_demotion_adaptive_floor_20260719T170150Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 44 | V3-EXQ-705b | v3_exq_705b_mech314_curiosity_conversion_demotion_adaptive_floor_20260719T180841Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 45 | V3-EXQ-706 | v3_exq_706_mech314_curiosity_conversion_double_gated_20260626T015604Z_v3 | 2026-06-26 | MECH-314 | FAIL / superseded |  | all arms hazard-free; src=manifest+script | V3-EXQ-706_2026-06-26 (confirmed) |
| 46 | V3-EXQ-706 | v3_exq_706_mech314_curiosity_conversion_double_gated_20260719T170215Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 47 | V3-EXQ-706 | v3_exq_706_mech314_curiosity_conversion_double_gated_20260719T182801Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 48 | V3-EXQ-706b | v3_exq_706b_mech314_curiosity_conversion_double_gated_validity_20260626T073417Z_v3 | 2026-06-26 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | 704b-706b-conversion-ceiling_2026-06-27 (confirmed) |
| 49 | V3-EXQ-706b | v3_exq_706b_mech314_curiosity_conversion_double_gated_validity_20260719T165649Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 50 | V3-EXQ-706b | v3_exq_706b_mech314_curiosity_conversion_double_gated_validity_20260719T184255Z_v3 | 2026-07-19 | MECH-314 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 51 | V3-EXQ-731 | v3_exq_731_q080b_least_effort_prior_20260709T211800Z_v3 | 2026-07-09 | Q-080 | FAIL / non_contributory | S | all arms hazard-free; src=script | no |
| 52 | V3-EXQ-732a | v3_exq_732a_policy_learning_discriminator_20260710T103144Z_v3 | 2026-07-10 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=script | V3-EXQ-732a_2026-07-10 (confirmed) |
| 53 | V3-EXQ-734 | v3_exq_734_env_difficulty_competence_recovery_sweep_20260711T092149Z_v3 | 2026-07-11 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=script | 734-737-conversion-ceiling-competence_2026-07-11 (confirmed) |
| 54 | V3-EXQ-734 | v3_exq_734_env_difficulty_competence_recovery_sweep_20260721T084355Z_v3 | 2026-07-21 | (none) | FAIL / superseded |  | all arms hazard-free; src=script | competence-objective-cluster-734-737b-742a_2026-07-22 (confirmed) |
| 55 | V3-EXQ-734 | v3_exq_734_env_difficulty_competence_recovery_sweep_20260722T202649Z_v3 | 2026-07-22 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=script | backlog_2026-07-24 (confirmed) |
| 56 | V3-EXQ-736 | v3_exq_736_curriculum_competence_recovery_diagnostic_20260711T200431Z_v3 | 2026-07-11 | (none) | FAIL / non_contributory |  | hazard-free arm(s) only (num_hazards seen: 0, 2, 4); src=script | 734-737-conversion-ceiling-competence_2026-07-11 (confirmed) |
| 57 | V3-EXQ-790 | v3_exq_790_channel_routing_cross_class_magnitude_replication_20260722T021558Z_v3 | 2026-07-22 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=manifest+script | V3-EXQ-790_2026-07-22 (confirmed) |
| 58 | V3-EXQ-790 | v3_exq_790_channel_routing_cross_class_magnitude_replication_20260722T142736Z_v3 | 2026-07-22 | (none) | FAIL / non_contributory |  | all arms hazard-free; src=manifest+script | V3-EXQ-790-run2_2026-07-24 (confirmed) |
| 59 | V3-EXQ-791a | v3_exq_791a_channel_routing_cross_class_magnitude_replication_20260723T044051Z_v3 | 2026-07-23 | (none) | PASS / non_contributory |  | all arms hazard-free; src=manifest+script | no |
| 60 | V3-EXQ-806 | v3_exq_806_sd078_centered_rule_field_context_key_20260725T191042Z_v3 | 2026-07-25 | SD-078 | PASS / supports | S | all arms hazard-free; src=manifest+script | no |
| 61 | V3-EXQ-807 | v3_exq_807_sd079_centered_goal_anchor_match_20260725T191402Z_v3 | 2026-07-25 | SD-079 | PASS / supports | S | all arms hazard-free; src=manifest+script | no |
| 62 | V3-EXQ-808 | v3_exq_808_return_decomposition_objective_misspecification_20260724T044039Z_v3 | 2026-07-24 | (none) | FAIL / unknown |  | all arms hazard-free; src=manifest | backlog_2026-07-24 (confirmed) |
| 63 | V3-EXQ-810 | v3_exq_810_arc071_chunk_accumulator_readiness_20260723T222726Z_v3 | 2026-07-23 | ARC-071, MECH-323, MECH-324 | FAIL / unknown | S | all arms hazard-free; src=manifest+script | V3-EXQ-822b-834_2026-07-29 (confirmed); backlog_2026-07-24 (confirmed) |
| 64 | V3-EXQ-813 | v3_exq_813_survival_zeroed_ppo_latent_policy_probe_20260724T143333Z_v3 | 2026-07-24 | (none) | FAIL / unknown |  | all arms hazard-free; src=manifest | backlog_2026-07-24 (confirmed) |
| 65 | V3-EXQ-815 | v3_exq_815_mech321_policy_decomposition_readiness_20260724T144151Z_v3 | 2026-07-24 | ARC-070, MECH-321 | PASS / supports | S | all arms hazard-free; src=manifest+script | no |
| 66 | V3-EXQ-819 | v3_exq_819_mech457_inv088_zworld_trained_vs_random_20260726T005930Z_v3 | 2026-07-26 | MECH-457, INV-088 | FAIL / unknown | S | all arms hazard-free; src=manifest | batch-793a-817-819_2026-07-26 (confirmed) |
| 67 | V3-EXQ-819a | v3_exq_819a_mech457_inv088_zworld_trained_vs_random_gatefix_20260727T005012Z_v3 | 2026-07-27 | MECH-457, INV-088 | PASS / unknown | S | all arms hazard-free; src=manifest | V3-EXQ-819a_2026-07-30 (confirmed) |
| 68 | V3-EXQ-823 | v3_exq_823_sd079_ghost_goal_retrieval_consumer_20260726T075327Z_v3 | 2026-07-26 | SD-079 | PASS / supports | S | all arms hazard-free; src=manifest+script | no |
| 69 | V3-EXQ-840 | v3_exq_840_mech294_theta_packet_binding_committed_action_falsifier_20260730T170540Z_v3 | 2026-07-30 | MECH-294 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | batch-687a-707c-840-748a-833-842-810b-673-614-798afail_2026-07-30 (confirmed) |
| 70 | V3-EXQ-840b | v3_exq_840b_mech294_theta_packet_binding_committed_action_falsifier_20260801T120516Z_v3 | 2026-08-01 | MECH-294 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-840b_2026-08-01 (confirmed) |
| 71 | V3-EXQ-842 | v3_exq_842_mech217_offline_wanting_spread_readiness_20260730T173047Z_v3 | 2026-07-30 | MECH-217 | PASS / supports | S | all arms hazard-free; src=script | batch-687a-707c-840-748a-833-842-810b-673-614-798afail_2026-07-30 (confirmed) |
| 72 | V3-EXQ-857a | v3_exq_857a_q086_gentler_env_fingerprint_redesign_20260802T015401Z_v3 | 2026-08-02 | Q-086 | FAIL / unknown | S | hazard-free arm(s) only (num_hazards seen: 0, 1); src=manifest+script | V3-EXQ-857a_2026-08-02 (confirmed) |
| 73 | V3-EXQ-874 | v3_exq_874_mech467_distractor_resistance_20260802T222132Z_v3 | 2026-08-02 | MECH-467 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-874_2026-08-03 (confirmed) |
| 74 | V3-EXQ-874b | v3_exq_874b_mech467_distractor_three_leg_battery_20260816T222900Z_v3 | 2026-08-16 | MECH-467 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-874b_2026-08-17 (confirmed) |
| 75 | V3-EXQ-883 | v3_exq_883_mech427_cross_level_subgoal_credit_20260803T022051Z_v3 | 2026-08-03 | MECH-427 | PASS / supports | S | all arms hazard-free; src=script | no |
| 76 | V3-EXQ-884 | v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding_20260803T022131Z_v3 | 2026-08-03 | MECH-428 | FAIL / non_contributory | S | all arms hazard-free; src=script | V3-EXQ-884_2026-08-03 (confirmed) |
| 77 | V3-EXQ-888 | v3_exq_888_mech074_readwrite_head_route_dissociation_20260804T075257Z_v3 | 2026-08-04 | MECH-074, MECH-074a, MECH-074b | PASS / supports | S | hazard-free arm(s) only (num_hazards seen: 0, 4); src=manifest+script | no |
| 78 | V3-EXQ-894 | v3_exq_894_mech074d_bla_remap_attribution_selectivity_20260808T005219Z_v3 | 2026-08-08 | MECH-074d | FAIL / weakens | S | hazard-free arm(s) only (num_hazards seen: 0, 4); src=manifest+script | V3-EXQ-894_2026-08-08 (confirmed) |
| 79 | V3-EXQ-894a | v3_exq_894a_mech074d_bla_remap_attribution_selectivity_20260808T101157Z_v3 | 2026-08-08 | MECH-074d | FAIL / weakens | S | hazard-free arm(s) only (num_hazards seen: 0, 4); src=manifest+script | V3-EXQ-894a_2026-08-08 (confirmed); V3-EXQ-906a_894b_2026-08-09 (confirmed) |
| 80 | V3-EXQ-894b | v3_exq_894b_mech074d_bla_trainable_attribution_head_20260809T081623Z_v3 | 2026-08-09 | MECH-074d | FAIL / weakens | S | hazard-free arm(s) only (num_hazards seen: 0, 4); src=manifest+script | V3-EXQ-894c_2026-08-11 (confirmed); V3-EXQ-906a_894b_2026-08-09 (confirmed) |
| 81 | V3-EXQ-894c | v3_exq_894c_mech074d_bla_entropy_weight_sweep_20260810T212602Z_v3 | 2026-08-10 | MECH-074d | FAIL / mixed | S | hazard-free arm(s) only (num_hazards seen: 0, 4); src=manifest+script | V3-EXQ-894c_2026-08-11 (confirmed) |
| 82 | V3-EXQ-904 | v3_exq_904_arc070_decomposition_trigger_selectivity_20260808T201150Z_v3 | 2026-08-08 | ARC-070 | PASS / supports | S | all arms hazard-free; src=manifest+script | V3-EXQ-904_2026-08-09 (confirmed) |
| 83 | V3-EXQ-914 | v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T055126Z_v3 | 2026-08-11 | MECH-236 | FAIL / superseded |  | all arms hazard-free; src=manifest+script | V3-EXQ-914-914a_2026-08-13 (confirmed) |
| 84 | V3-EXQ-914 | v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T065911Z_v3 | 2026-08-11 | MECH-236 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-914-914a_2026-08-13 (confirmed) |
| 85 | V3-EXQ-939 | v3_exq_939_mech303_proximity_gated_contextual_safety_vigilance_release_20260818T213039Z_v3 | 2026-08-18 | MECH-303 | FAIL / non_contributory | S | hazard-free arm(s) only (num_hazards seen: 0, 8); src=manifest | V3-EXQ-939_2026-08-20 (confirmed) |
| 86 | V3-EXQ-939a | v3_exq_939a_mech303_proximity_gated_contextual_safety_vigilance_release_20260821T235047Z_v3 | 2026-08-21 | MECH-303 | PASS / supports | S | hazard-free arm(s) only (num_hazards seen: 0, 8); src=manifest | no |
| 87 | V3-EXQ-941 | v3_exq_941_mech467_approach_decomposition_20260819T142245Z_v3 | 2026-08-19 | MECH-467 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | 940-941-mech467-cluster_2026-08-20 (confirmed) |
| 88 | V3-EXQ-948 | v3_exq_948_observation_interface_re_representation_probe_20260825T142115Z_v3 | 2026-08-25 | (none) | PASS / unknown |  | all arms hazard-free; src=manifest | V3-EXQ-948_2026-08-25 (confirmed) |
| 89 | V3-EXQ-966 | v3_exq_966_mech143_144_hippocampal_value_sensitivity_causal_20260830T115037Z_v3 | 2026-08-30 | MECH-143, MECH-144 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | 966-436g-951-959-822d-cluster_2026-08-30 (confirmed) |
| 90 | V3-EXQ-967 | v3_exq_967_mech144_shuffle_inertness_confirmer_20260901T062344Z_v3 | 2026-09-01 | (none) | PASS / non_contributory |  | all arms hazard-free; src=manifest+script | V3-EXQ-967_2026-09-01 (confirmed) |
| 91 | V3-EXQ-978 | v3_exq_978_sd018_directional_field_fishtank_20260903T111718Z_v3 | 2026-09-03 | INV-088, MECH-457 | FAIL / non_contributory | S | all arms hazard-free; src=manifest | V3-EXQ-1008_2026-09-08 (confirmed); V3-EXQ-978_2026-09-03 (confirmed) |
| 92 | V3-EXQ-997 | v3_exq_997_mech162_zresource_zworld_planning_reconvergence_20260904T032212Z_v3 | 2026-09-04 | MECH-162 | FAIL / non_contributory | S | all arms hazard-free; src=manifest+script | V3-EXQ-997_2026-09-04 (confirmed) |

Autopsy coverage over the 92 exposed runs: 60 already have a confirmed or draft autopsy artifact; 32 do not. Note that an autopsy existing does NOT mean it considered self-contamination -- only the 874b/884/940/941 cluster autopsies name it explicitly (grep `contamination` in `failure_autopsy_*.json` if that matters for a claim below).

## 5. Table B -- claims whose evidence base is >= 50% footgun-exposed

Two denominators, because the chip's definition and the indexer's differ: **chip-def** = experimental `claim_evidence` entries not superseded (includes `non_contributory`, `diagnostic_probe`, `stale_*`, `degenerate` entries that the indexer does not score); **indexer-scored** = entries with `scoring_excluded` null (what actually moves `exp_conf`). A claim can be 100% exposed under chip-def and have zero scored entries -- its exposure is then latent (it would surface if any of those runs were re-scored), not currently moving confidence.

| claim | indexer-scored exposed / total | chip-def exposed / total | exposed runs (queue ids) |
|---|---|---|---|
| ARC-060 | 0 / 0 | 2 / 2 | 651_arc060_blocked_goal_recovery, 651a_arc060_blocked_goal_recovery |
| ARC-070 | 1 / 1 ** | 2 / 5 | 815_mech321_policy_decomposition_readiness, 904_arc070_decomposition_trigger_selectivity |
| DEV-NEED-003 | 0 / 0 | 1 / 1 | 590c_mech314_novelty_goldilocks |
| INV-043 | 0 / 0 | 1 / 1 | 206_inv043_ethical_capacity_probe |
| INV-054 | 1 / 1 ** | 3 / 5 | 278_inv054_depression_recovery_phase_transition, 435_inv054_phase_transition_sustained_recovery |
| MECH-026 | 0 / 0 | 1 / 2 | 067_mech026_ready_vigilance |
| MECH-074 | 1 / 1 ** | 1 / 1 | 888_mech074_readwrite_head_route_dissociation |
| MECH-074a | 2 / 2 ** | 2 / 4 | 659_mech074a_bla_encoding_gain_replay_bias, 888_mech074_readwrite_head_route_dissociation |
| MECH-074b | 1 / 1 ** | 1 / 1 | 888_mech074_readwrite_head_route_dissociation |
| MECH-074d | 4 / 4 ** | 4 / 6 | 894_mech074d_bla_remap_attribution_selectivity, 894a_mech074d_bla_remap_attribution_selectivity, 894b_mech074d_bla_trainable_attribution_head, 894c_mech074d_bla_entropy_weight_sweep |
| MECH-106 | 1 / 1 ** | 1 / 1 | 231a_mech106_bg_hysteresis_redesign |
| MECH-162 | 0 / 0 | 1 / 1 | 997_mech162_zresource_zworld_planning_reconvergence |
| MECH-189 | 1 / 2 ** | 2 / 5 | 669b_mech329_wanting_first_goal_seeding, 669c_mech329_wanting_first_goal_seeding |
| MECH-217 | 0 / 0 | 1 / 1 | 842_mech217_offline_wanting_spread_readiness |
| MECH-236 | 0 / 0 | 1 / 1 | 914_mech236_hippocampal_zgoal_channel_ablation |
| MECH-294 | 0 / 0 | 2 / 2 | 840_mech294_theta_packet_binding_committed_action_falsifier, 840b_mech294_theta_packet_binding_committed_action_falsifier |
| MECH-303 | 1 / 2 ** | 2 / 5 | 939_mech303_proximity_gated_contextual_safety_vigilance_release, 939a_mech303_proximity_gated_contextual_safety_vigilance_release |
| MECH-329 | 1 / 1 ** | 2 / 2 | 669b_mech329_wanting_first_goal_seeding, 669c_mech329_wanting_first_goal_seeding |
| MECH-427 | 1 / 1 ** | 1 / 1 | 883_mech427_cross_level_subgoal_credit |
| MECH-467 | 0 / 0 | 3 / 4 | 874_mech467_distractor_resistance, 874b_mech467_distractor_three_leg_battery, 941_mech467_approach_decomposition |
| MECH-537 | 0 / 0 | 1 / 1 | 1043_mech537_communication_subspace_routing |
| Q-080 | 0 / 0 | 1 / 1 | 731_q080b_least_effort_prior |
| Q-086 | 0 / 0 | 1 / 2 | 857a_q086_gentler_env_fingerprint_redesign |
| SD-077 | 1 / 1 ** | 1 / 1 | 1040_sd077_centered_super_ordinal_cue_key |
| SD-079 | 1 / 1 ** | 2 / 2 | 807_sd079_centered_goal_anchor_match, 823_sd079_ghost_goal_retrieval_consumer |
| SD-106 | 0 / 0 | 2 / 2 | 1023_sd106_bottleneck_preservation_validation, 1041_sd106_preservation_step_budget_metric_diagnostic |

**13 claims are >= 50% exposed among INDEXER-SCORED entries** (marked `**`): ARC-070, INV-054, MECH-074, MECH-074a, MECH-074b, MECH-074d, MECH-106, MECH-189, MECH-303, MECH-329, MECH-427, SD-077, SD-079. **23 claims are >= 50% exposed under the chip definition**; the table is the union of both sets (26 claims). Claims touched by at least one exposed chip-def entry but below 50%: ARC-071 (1/7), INV-088 (3/9), MECH-143 (1/3), MECH-144 (1/3), MECH-229 (1/13), MECH-230 (1/10), MECH-304 (1/5), MECH-314 (3/13), MECH-314a (1/5), MECH-321 (1/9), MECH-323 (1/6), MECH-324 (1/4), MECH-428 (1/4), MECH-457 (3/29), SD-015 (1/22), SD-049 (1/13), SD-078 (1/8).

## 6. Undetermined runs that ARE chip-scored (148)

These are CausalGridWorld runs where neither the manifest nor a static read of the script settles `num_hazards`. They are NOT counted as exposed above and NOT counted as clean; a reader who needs one settled must open the script. Queue ids: V3-EXQ-080, V3-EXQ-106, V3-EXQ-111, V3-EXQ-118, V3-EXQ-228b, V3-EXQ-228c, V3-EXQ-228d, V3-EXQ-235, V3-EXQ-248, V3-EXQ-288, V3-EXQ-451, V3-EXQ-460c, V3-EXQ-460d, V3-EXQ-460e, V3-EXQ-460h, V3-EXQ-460i, V3-EXQ-460j, V3-EXQ-460k, V3-EXQ-460l, V3-EXQ-461c, V3-EXQ-464c, V3-EXQ-464d, V3-EXQ-464e, V3-EXQ-466c, V3-EXQ-466e, V3-EXQ-467c, V3-EXQ-467d, V3-EXQ-467e, V3-EXQ-468c, V3-EXQ-468d, V3-EXQ-468e, V3-EXQ-468f, V3-EXQ-514f, V3-EXQ-514j, V3-EXQ-514k, V3-EXQ-514l, V3-EXQ-514m, V3-EXQ-514n, V3-EXQ-514o, V3-EXQ-514p, V3-EXQ-514q, V3-EXQ-514r, V3-EXQ-514t, V3-EXQ-514u, V3-EXQ-526, V3-EXQ-603d, V3-EXQ-603e, V3-EXQ-603l, V3-EXQ-603o, V3-EXQ-603q, V3-EXQ-603r, V3-EXQ-652, V3-EXQ-687, V3-EXQ-687a, V3-EXQ-693, V3-EXQ-693a, V3-EXQ-715, V3-EXQ-715a, V3-EXQ-717, V3-EXQ-733a, V3-EXQ-760, V3-EXQ-793, V3-EXQ-793a, V3-EXQ-797, V3-EXQ-826, V3-EXQ-826a, V3-EXQ-846, V3-EXQ-866a, V3-EXQ-866c, V3-EXQ-917, V3-EXQ-927, V3-EXQ-930, V3-EXQ-934, V3-EXQ-935, V3-EXQ-935a, V3-EXQ-951, V3-EXQ-951c, claim_probe_arc_016, claim_probe_arc_018, claim_probe_arc_021, claim_probe_arc_024, claim_probe_arc_025, claim_probe_mech_025, claim_probe_mech_033, claim_probe_mech_057b, claim_probe_mech_058, claim_probe_mech_069, claim_probe_mech_071, claim_probe_mech_089, claim_probe_mech_090, claim_probe_mech_095, claim_probe_mech_099, claim_probe_mech_100, claim_probe_mech_102, claim_probe_q_007, claim_probe_sd_003, claim_probe_sd_004, claim_probe_sd_005, claim_probe_sd_006, claim_probe_sd_007, claim_probe_sd_008, claim_probe_sd_010, v3_exq_060_arc016_beta_gate_fi.

## 7. Flat-only manifests (flagged separately, as the chip asked)

18 flat manifest(s) have no pack sibling and therefore never enter scoring (memory `reference_indexer_reads_runs_pack_not_flat`): `v3_exq_542_arc062_gated_policy_substrate_readiness_v3_20260509T202211Z` (claims=False, dir=supports), `v3_exq_544_mech313_noise_floor_substrate_readiness_v3_20260510T104458Z` (claims=False, dir=supports), `v3_exq_617_sd056_multistep_substrate_readiness_v3_20260531T113129Z` (claims=False, dir=supports), `v4_exq_001_dr12_pe_conditioned_confidence_falsifier_20260617T105251Z_v4` (claims=False, dir=None), `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T164550Z` (claims=False, dir=non_contributory), `v4_exq_003_dr10_z_self_viability_falsifier_20260701T074023Z_v4` (claims=False, dir=None), `v3_exq_547_mech320_tonic_vigor_substrate_readiness_v3_20260510T205612Z` (claims=False, dir=non_contributory), `v3_exq_544a_mech313_noise_floor_substrate_readiness_v3_20260529T154903Z` (claims=False, dir=supports), `v4_exq_002_dr13_self_recurrence_falsifier_20260701T065002Z_v4` (claims=False, dir=None), `v3_exq_613_sd056_e2_action_contrastive_substrate_readiness_v3_20260529T083242Z` (claims=False, dir=supports), `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T002616Z` (claims=False, dir=non_contributory), `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T164557Z` (claims=False, dir=non_contributory), `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T172610Z` (claims=False, dir=non_contributory), `v3_exq_324b_sd020_harm_surprise_pe_dry` (claims=False, dir=does_not_support), `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T041617Z` (claims=False, dir=non_contributory), `v3_exq_639_arc063_candidate_rule_field_readiness_v3_20260604T154034Z` (claims=False, dir=non_contributory), `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T172604Z` (claims=False, dir=non_contributory), `v3_exq_542a_arc062_gated_policy_substrate_readiness_onehot_v3_20260520T002633Z` (claims=False, dir=non_contributory). All other flats are duplicates of a pack and were not separately classified.

## 8. What this does and does not show

- It DOES show, from real config keys and real script literals, which runs were configured so that a hazard-free agent could poison itself, and which claims' evidence bases rest mostly on such runs. The list is exposure, i.e. the *possibility* of self-contamination death shortening the measurement window.
- It does NOT show that any of these runs actually died of contamination. Almost no manifest records `agent_health`, a termination reason, or a death count (1 of the 92 exposed packs carries any health/termination-like key at all), so the observed-symptom column the chip would ideally want does not exist in the corpus. Whether a given run was actually truncated is only knowable from its per-episode telemetry or a re-run; V3-EXQ-940 is the one place that was measured (C1 PASSED, 11% margin, `ARM_STOCK` vs `ARM_CONTAM_OFF`).
- Exposure severity varies with geometry: contamination needs ~4 entries of the same cell plus ~3 re-entries. Small arenas with revisiting agents (874b's 6x6; the 642 series' toroidal grids) are the high-risk shape; a large non-toroidal grid with a mobile agent may never cross the threshold. This audit does not weight by geometry.
- Runs that resolve `num_hazards` at runtime (120 `UNDETERMINED` packs, 148 chip-scored across both undetermined classes) are neither cleared nor accused here.
- The `MIXED-ARMS` class is mostly opted-out (1004/1007/1039 set the gate or spread=0 alongside `num_hazards=0`); only V3-EXQ-940's `ARM_STOCK` is exposed, and deliberately so.
- Static script resolution can mis-attribute when the same script contains several env constructions (e.g. a `num_hazards=4` training env and a `num_hazards=0` probe env in one file): such runs are listed as "hazard-free arm(s) only" and the exposure applies to that arm's window, not necessarily to the arm carrying the DV.

## 9. Routing (recommendation only -- nothing applied)

One `evidence_discrepancy` governance flag for this audit, listing the claims in Table B, so `/governance` can decide per claim whether the exposed runs need a re-measurement with the opt-out set (the V3-EXQ-940 pattern) or a `pending_retest_after_substrate`-style annotation. **Not raised by this session:** `task_claim.py` arbitration found `REE_assembly/evidence/planning/governance_flags.v1.json` owned by the active claim `campaign-w-scripts-corpus-20260916` (claimed 2026-09-16T22:56:02Z), and a non-owner verdict is binding. The exact command, to run once that claim closes:

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/governance_flag.py raise --flag-type evidence_discrepancy \
  --claim-id ARC-060 --claim-id ARC-070 --claim-id DEV-NEED-003 --claim-id INV-043 --claim-id INV-054 --claim-id MECH-026 --claim-id MECH-074 --claim-id MECH-074a --claim-id MECH-074b --claim-id MECH-074d --claim-id MECH-106 --claim-id MECH-162 --claim-id MECH-189 --claim-id MECH-217 --claim-id MECH-236 --claim-id MECH-294 --claim-id MECH-303 --claim-id MECH-329 --claim-id MECH-427 --claim-id MECH-467 --claim-id MECH-537 --claim-id Q-080 --claim-id Q-086 --claim-id SD-077 --claim-id SD-079 --claim-id SD-106 \
  --summary "Corpus audit corpus_audit_contamination_footgun_20260916.md: 92 CausalGridWorld runs (60 chip-scored) were configured hazard-free (num_hazards=0) without the contamination opt-out, so a self-poisoning agent could truncate their measurement window (the V3-EXQ-874b/940 mechanism, C1 confirmed). The 26 claims listed have >= 50% of their non-superseded experimental entries on such runs (23 claims) or >= 50% of their indexer-scored entries (13 of them >= 50% among indexer-scored entries: ARC-070, INV-054, MECH-074, MECH-074a, MECH-074b, MECH-074d, MECH-106, MECH-189, MECH-303, MECH-329, MECH-427, SD-077, SD-079); decide per claim whether a gated re-measurement is owed."
```

**RAISED 2026-09-16T23:22:05Z as `GFLAG-0304`** (`evidence_discrepancy`, 26 claims) by session `angry-leakey-c8b0a0`, once the blocking claim `campaign-w-scripts-corpus-20260916` closed. Landed `REE_assembly` `d0fbfb090a`, verified on `origin/master`; `status: open`, awaiting `/governance` adjudication.
