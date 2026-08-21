# Claims-Doc Status Drift Report

Generated: 2026-08-21T02:10:38Z

Mirror of the closure-plan drift report, for architecture docs. Flags docs whose status has fallen out of step with `docs/claims/claims.yaml`. Resolution + derivation are shared with `docs/apply_status_frontmatter.py`. Only the **Frontmatter drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Docs resolved to a claim: 100

## Frontmatter drift -- HARD (0)

Stamped `status:` frontmatter != the value re-derived from claims.yaml now. Re-run `docs/apply_status_frontmatter.py`; if it persists, the frontmatter was hand-edited or claims.yaml changed without a governance run.

_None._

## Unstamped but resolvable -- SOFT (0)

Docs that resolve to a registered claim but have no `status:` frontmatter. Run `docs/apply_status_frontmatter.py`.

_None._

## Hand-line contradiction -- REVIEW (0)

Residual hand-typed `**Status:**` lines (the stamper leaves prose lines in place per the non-destructive razor) whose epistemic status word or v3_pending assertion contradicts the registry. Lift/rewrite by hand, then the frontmatter carries the machine-checkable truth.

_None._

## Unresolved with a hand status line -- INFO (129)

Docs with a hand `**Status:**` line but no derivable claim id (no `**Claim:**` line, no registered filename stem). Outside the stamper's reach; listed for visibility only.

- `active_inference_bridge.md` -- "first pass (WS-5 of `evidence/planning/ree_ai_design_critique_plan.md`)"
- `affect_terminology_instinct_protoemotion.md` -- "provisional terminology / architecture note"
- `agency_responsibility_flow.md` -- "provisional"
- `anticipatory_affect_conjunction_vs_dual_channel.md` -- "MECH-307 SUBSTRATE READY (IGW-20260521-023 closed 2026-05-21). Landed 2026-05-08/11; canonical validation V3-EXQ-540g PA"
- `architecture_scaling_needs.md` -- "planning hypothesis"
- `arcuate_fasciculus.md` -- "candidate"
- `astrocyte_regulatory_stack.md` -- "candidate"
- `axiom_chain_adversarial_audit.md` -- "first pass (WS-13 of `evidence/planning/ree_ai_design_critique_plan.md`)"
- `bitter_lesson_position.md` -- "first pass (WS-6 of `evidence/planning/ree_ai_design_critique_plan.md`)"
- `canonical_profile_admission_criteria.md` -- "design doctrine, 2026-08-12. Derived verbatim from"
- `claim_phase_provenance.md` -- "design proposal + landed checker, 2026-06-09"
- `cognifold_signed_coupling.md` -- "candidate cluster, V4/V5, off the V3 critical path. Registered 2026-06-09 from the competitive-interactions thought inta"
- `cognitive_architecture_graveyard.md` -- "first pass (WS-8 of `evidence/planning/ree_ai_design_critique_plan.md`)"
- `compact_consolidation_principle.md` -- "candidate"
- `contextmemory_write_address_selection.md` -- "IMPLEMENTED (two mechanisms) 2026-08-19 -- VALIDATION PENDING for both"
- `control_plane.md` -- "stable"
- `control_plane_heartbeat.md` -- "candidate"
- `control_plane_signal_map.md` -- "candidate"
- `control_vector_logging.md` -- "IMPLEMENTED"
- `corrigibility_positioning.md` -- "first pass (WS-7 of `evidence/planning/ree_ai_design_critique_plan.md`)"
- `critical_period_crystallization.md` -- "IMPLEMENTED 2026-05-17"
- `default_mode.md` -- "stable"
- `developmental_bootstrapping_hippo_retrieval.md` -- "Draft -- claims INV-073, MECH-325, MECH-326, ARC-072 registered (candidate)"
- `developmental_curriculum.md` -- "provisional"
- `developmental_experiment_priorities.md` -- "Planning document — not a registered claim. Informs experiment queue decisions and session governance."
- `developmental_governance_review.md` -- "Review document -- synthesis only, not a registered claim."
- `dr10_z_self_in_e3_viability.md` -- "IMPLEMENTED 2026-07-01"
- `dr12_pe_conditioned_e3_confidence.md` -- "IMPLEMENTED 2026-06-17"
- `dr13_self_recurrence_temporal_depth.md` -- "IMPLEMENTED 2026-07-01"
- `dv_temporal_depth_v3_form.md` -- "candidate, implementation_phase: v3, v3_pending: true (V3 form);"
- `e1.md` -- "stable"
- `e1_e2_constraint_propagation.md` -- "candidate"
- `e2.md` -- "stable"
- `e3.md` -- "stable"
- `efficiency_dimensionality_hypothesis.md` -- "Working hypothesis — Phase 2 ablations pending"
- `effort_dissociation_env.md` -- "IMPLEMENTED 2026-07-09."
- `entities_and_binding.md` -- "provisional"
- `established_ethical_systems.md` -- "architecture derivation note"
- `ethical_agency_derivation.md` -- "architecture note"
- `externalised_dmn_play_private_speech.md` -- "V4+ developmental-architecture cluster (candidate). Off the REE-v3 critical"
- `formal_ancestor_mapping.md` -- "first pass (WS-4 of `evidence/planning/ree_ai_design_critique_plan.md`)"
- `founder_ontology.md` -- "plan-of-record for *intent* (how the architecture was meant to be read)."
- `frontal_cue_integration.md` -- "candidate"
- `ghost_goal_search.md` -- "design sketch (2026-04-26) + **Retrieval-Cue Reframe (2026-05-19)** -- see Section 0"
- `goal_wanting_signal_chain.md` -- "Diagnostic / architectural note"
- `hippocampal_anchor_selection.md` -- "candidate"
- `hippocampal_braid.md` -- "stable"
- `hippocampal_map_tagged_channels.md` -- "design reference (V4 scope; informs V3 SD-011 generalization)"
- `hippocampal_systems.md` -- "stable"
- `hook_surface_contract.md` -- "candidate"
- `infant_substrate_expansion.md` -- "SD-049 `multi_resource_heterogeneity_enabled` with `resource_introduction_schedule`"
- `invariant_types.md` -- "architecture doc, 2026-04-17"
- `jepa_e1e2_integration_contract.md` -- "stable"
- `jepa_ree_hybrid_diagram_spec.md` -- "stable"
- `l_space.md` -- "stable"
- `landing_integration_worker_investigation.md` -- "investigated, decided — no dedicated worker; one narrow follow-on chipped"
- `language.md` -- "stable"
- `learned_cross_loop_arbitration.md` -- "IMPLEMENTED 2026-07-01. PROMOTES NOTHING. Behind a no-op-default flag, byte-identical OFF."
- `mode_manager.md` -- "legacy"
- `modes_of_cognition.md` -- "provisional"
- `modulatory_bias_selection_authority.md` -- "IMPLEMENTED 2026-06-03 (substrate-readiness validation pending V3-EXQ)."
- `monostrategy_developmental_analysis.md` -- "Analysis document — not a registered claim. Findings feed into developmental register, experiment design, and governance"
- `natural_commit_occupancy_release.md` -- "IMPLEMENTED 2026-06-20 (substrate; PROMOTES NOTHING)"
- `neuromodulatory_control_planes.md` -- "candidate"
- `non_deficit_action_drives.md` -- "family slot registered 2026-05-10 (ARC-066 + ARC-067 + ARC-068 candidate / pending_design)."
- `overview.md` -- "legacy"
- `papez_circuit.md` -- "provisional"
- `path_authority_and_interrupts.md` -- "provisional"
- `phased_rule_state_training_curriculum.md` -- "IMPLEMENTED 2026-05-17. Design questions O-1..O-5 RESOLVED"
- `plasticity_write_authority_gating.md` -- "candidate-claim home doc. NOT a substrate-design memo, NOT a V3 critical-path item."
- `play_substrate_design.md` -- "Draft — 2026-05-16"
- `policy_primitive_granularity.md` -- "family slot registered 2026-05-10 (ARC-069 parent + ARC-070 + ARC-071 candidate / pending_design)."
- `precision_control.md` -- "provisional"
- `precision_scoping.md` -- "provisional"
- `prioritized_replay_write_gating.md` -- "candidate (registered 2026-06-19). Architecture stub for two"
- `psychiatric_failure_modes.md` -- "WORKING HYPOTHESIS (registered 2026-06-03). Not an established mechanism;"
- `quality_diversity_committed_archive.md` -- "architecture stub for candidate claim MECH-442 (candidate / substrate_conditional / implementation_phase v3 / version_re"
- `receptor_subtype_intervention_layer.md` -- "working abstraction layer (not a claim cluster; no claims.yaml entries created here)"
- `ree_v2_repo_bootstrap_spec.md` -- "candidate"
- `ree_v2_spec.md` -- "candidate"
- `replay_development_analysis.md` -- "Analysis document — not a registered claim. Proposals feed into experiment design and register maintenance."
- `residue_geometry.md` -- "stable"
- `rule_apprehension_layer.md` -- "registered architectural slot. Weak reading (ARC-062) at implementation_phase=v3 candidate, **BLOCKED** (GAP-B status=bl"
- `rule_distinguishability_maintenance.md` -- "architecture stub for candidate claims MECH-437 / MECH-438 (candidate / substrate_conditional / implementation_phase v4 "
- `sd_085_e3_reality_cost_weight.md` -- "PENDING"
- `sd_actor_critic_action_learning.md` -- "SUBSTRATE IMPLEMENTED 2026-07-12 (module + agent hooks + config-switchable A0–A3 arms landed, smoke-tested — see §7). **"
- `sd_cross_stream_binding_substrate.md` -- "IMPLEMENTED -- two modes. FIXED field (2026-07-08; retest V3-EXQ-720 RAN, SPEC 3/6, gate not cleared). LEARNED (plastic)"
- `sd_e3_scorer_completion.md` -- "IMPLEMENTED"
- `sd_hazard_aware_policy_decomposition.md` -- "IMPLEMENTED 2026-08-01"
- `sd_mech267_cem_selection_fix.md` -- "IMPLEMENTED"
- `sd_mech267_horizon_depth_modulation.md` -- "IMPLEMENTED 2026-08-02"
- `sd_mech303_threshold_sourcing.md` -- "IMPLEMENTED"
- `sd_mech457_approach_extinction.md` -- "IMPLEMENTED"
- `sd_mech457_bc_aux_schedule.md` -- "IMPLEMENTED (2026-07-18)"
- `sd_mech457_competence_bootstrap_explorer.md` -- "IMPLEMENTED"
- `sd_mech457_consummatory_act.md` -- "IMPLEMENTED"
- `sd_mech457_distributional_critic.md` -- "IMPLEMENTED"
- `sd_mech457_retention_trajectory_probe.md` -- "IMPLEMENTED"
- `sd_mel_consumer.md` -- "IMPLEMENTED"
- `sd_mel_producer.md` -- "VALIDATED (V3-EXQ-798a, 2026-07-29; confirmed failure_autopsy_V3-EXQ-798a_2026-07-30)"
- `sd_orienting_decision_scale.md` -- "IMPLEMENTED"
- `sd_queue_seed_enforcement.md` -- "IMPLEMENTED"
- `sd_residue_valence_bound.md` -- "IMPLEMENTED"
- `sd_v4_loop_segregation.md` -- "IMPLEMENTED 2026-06-27; finer-channel plumbing DEFECT fixed 2026-06-28; **C2 RELEASE (per-named-channel range-preserving"
- `self_attribution_per_stream.md` -- "Active roadmap document. Supersedes the narrow SD-003 counterfactual architecture."
- `sensory_stream_tags.md` -- "provisional"
- `serotonin.md` -- "provisional"
- `sleep.md` -- "stable"
- `sleep_aggregation_cluster.md` -- "candidate, v3_pending (all four)"
- `slow_modulatory_state_and_compulsive_loops.md` -- "V4/V5 compass. Location anchor for the candidate claims reaped from the"
- `social.md` -- "stable"
- `soft_competitive_disinhibition_settling.md` -- "IMPLEMENTED 2026-07-02. PROMOTES NOTHING. Behind a no-op-default flag, byte-identical OFF"
- `spintronic_memristive_cognifold_substrate.md` -- "candidate compass — POST-V5 / future physical instantiation."
- `sustained_drive_anticipatory_wanting.md` -- "goal_pipeline:GAP-3 **DONE** 2026-05-20. Option 1 (`drive_ema_alpha`)"
- `temporal_dynamics.md` -- "provisional"
- `three_loop_learning_channels.md` -- "candidate"
- `tpj_agency_comparator.md` -- "candidate"
- `trainable_relief_safety_affordance_learners.md` -- "candidate cluster, registered 2026-06-09. Home doc for the trainable"
- `trajectory_selection.md` -- "candidate"
- `v2_v3_transition_roadmap.md` -- "Living document — update after each major V2 experiment batch"
- `v3_v4_phase_substrate_boundary.md` -- "active architectural commitment for the V3 working-model phase"
- `v4_developmental_harness_spec.md` -- "design sketch, not a full spec. Reserved as the V4 flagship harness so V3 work doesn't accidentally close off options th"
- `v4_planning_index.md` -- "consolidation map"
- `v_s_invalidation_runtime.md` -- "candidate, v3_pending"
- `valenced_hippocampal_map.md` -- "candidate"
- `version_layering_doctrine.md` -- "architecture doctrine, 2026-06-17"
- `vmPFC.md` -- "candidate"
- `what_is_ree_made_of.md` -- "architecture note (whole-system presentation framing; not a registered falsifiable claim)"
- `why_attention_must_be_fragmented.md` -- "provisional"

