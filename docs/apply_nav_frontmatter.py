"""
apply_nav_frontmatter.py
Re-runnable script: stamps Jekyll (Just-the-Docs) nav frontmatter across docs/
to produce a clean, themed left-hand sidebar for the GitHub Pages site.

Run from repo root:
  /opt/local/bin/python3 docs/apply_nav_frontmatter.py

Structure produced:
  TOP LEVEL (ordered):
    Home / Why This Architecture? / What Is REE Made Of? / Architecture (section) /
    Foundations / Invariants / Roadmap / Research Status / Related Work / Glossary /
    Failure Modes / Vignettes / REE for Psychiatrists / Closure Dashboard /
    Governance (section) / Contribute Compute
  ARCHITECTURE -> 16 themed collapsible sub-sections (3-level nav):
    Architecture (overview.md, has_children)
      -> <Theme> section stub (architecture/sections/<key>.md, has_children)
        -> the design docs for that theme (parent=<Theme>, grandparent=Architecture)
  GOVERNANCE -> 2 children.

Design docs that are scratch / session-prompts / narrow impl notes are kept
nav_exclude (still build + reachable by URL, just hidden from the sidebar).

Safe to re-run: reads each file, strips existing frontmatter, re-stamps.
Adjust the ASSIGN map below to move a page between themes.
"""

import os
import re

DOCS = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.join(DOCS, "architecture")
SECTIONS_DIR = os.path.join(ARCH, "sections")

# ---------------------------------------------------------------------------
# 1. Top-level pages (ordered). Key = path relative to docs/.
# ---------------------------------------------------------------------------

TOP_LEVEL = {
    "index.md":                                  {"title": "Home",                  "nav_order": 1},
    "architecture/ethical_agency_derivation.md": {"title": "Why This Architecture?","nav_order": 2},
    "architecture/what_is_ree_made_of.md":       {"title": "What Is REE Made Of?",  "nav_order": 3},
    "architecture/overview.md":                  {"title": "Architecture",          "nav_order": 4, "has_children": True},
    "architecture/five_axioms_foundations.md":   {"title": "Foundations",           "nav_order": 5},
    "invariants.md":                             {"title": "Invariants",            "nav_order": 6},
    "substrate_versions.md":                     {"title": "Roadmap",               "nav_order": 7, "has_children": True},
    "roadmap.md":                                {"title": "Status Log",            "nav_order": 17},
    "research_status.md":                        {"title": "Research Status",       "nav_order": 8},
    "related_work.md":                           {"title": "Related Work",          "nav_order": 9},
    "glossary.md":                               {"title": "Glossary",              "nav_order": 10},
    "REE_failure_modes.md":                      {"title": "Failure Modes",         "nav_order": 11},
    "vignettes.md":                              {"title": "Vignettes",             "nav_order": 12},
    "ree_for_psychiatrists.md":                  {"title": "REE for Psychiatrists", "nav_order": 13},
    "ree_for_my_parents.md":                     {"title": "REE for My Parents",    "nav_order": 14},
    "closure_dashboard.md":                      {"title": "Closure Dashboard",     "nav_order": 15},
    "visualizations.md":                         {"title": "Visualizations",        "nav_order": 16},
    "contribute.html":                           {"title": "Contribute Compute",    "nav_order": 19},
}

# ---------------------------------------------------------------------------
# 2. Governance section (top-level parent + children)
# ---------------------------------------------------------------------------

# Roadmap (substrate versions) children -- the per-generation deep-dives that
# would otherwise be orphaned (V1 had no inbound nav link at all before 2026-08-26).
VERSIONS_CHILDREN = {
    "V1_PROGRESS_AND_LEARNING.md": {"title": "V1: Progress and Learning", "parent": "Roadmap", "nav_order": 1},
}

GOVERNANCE_PARENT = {"title": "Governance", "nav_order": 18, "has_children": True}
GOVERNANCE_CHILDREN = {
    "governance_verification_gate.md":            {"title": "Governance Verification Gate",     "parent": "Governance", "nav_order": 1},
    "architecture/evaluation_channel_integrity.md": {"title": "Evaluation-Channel Integrity",   "parent": "Governance", "nav_order": 2},
}

# ---------------------------------------------------------------------------
# 3. Architecture themed sub-sections (key -> (Title, nav_order))
#    Each becomes a stub page architecture/sections/<key>.md (created if absent).
# ---------------------------------------------------------------------------

SECTIONS = [
    ("engines",        "Core Engines & Forward Models",         1),
    ("foundations",    "Foundations & Rationale",               2),
    ("representation", "Perception, Representation & Dynamics",  3),
    ("attention",      "Attention, Binding & Objects",          4),
    ("control",        "Control, Precision & Neuromodulation",  5),
    ("memory",         "Memory & Hippocampus",                  6),
    ("modes",          "Modes, Agency & Default Mode",          7),
    ("goals",          "Goals, Drives & Motivation",            8),
    ("affect",         "Affect, Harm & Nociception",            9),
    ("pfc",            "Executive & PFC Control",               10),
    ("language",       "Language",                              11),
    ("sleep",          "Sleep & Offline Integration",           12),
    ("social",         "Social & Clinical",                     13),
    ("development",    "Development & Curriculum",              14),
    ("specs",          "Specs, Diagrams & Versions",            15),
    ("roadmap",        "Roadmap & Planning (V4+)",              16),
]
SECTION_TITLE = {key: title for key, title, _ in SECTIONS}

# ---------------------------------------------------------------------------
# 4. Assignment: architecture/<basename> -> theme key  (or None to exclude)
# ---------------------------------------------------------------------------

ASSIGN = {
    # --- Core Engines & Forward Models ---
    "e1.md": "engines", "e2.md": "engines", "e3.md": "engines", "l_space.md": "engines",
    "state.md": "engines", "founder_ontology.md": "engines",
    "sd_004_sd_005_encoder_codesign.md": "engines", "sd_015_z_resource_encoder.md": "engines",
    "sd_030_e2_self_forward_model.md": "engines", "sd_031_e2_world_forward_model.md": "engines",
    "sd_056_e2_action_conditional_divergence.md": "engines",
    "contextmemory_write_address_selection.md": "engines", "sd_e3_scorer_completion.md": "engines",

    # --- Foundations & Rationale ---
    "post_hoc_filter_insufficiency.md": "foundations", "established_ethical_systems.md": "foundations",
    "ethics_and_governance_posture.md": "foundations",
    "efficiency_dimensionality_hypothesis.md": "foundations", "invariant_types.md": "foundations",
    "policy_primitive_granularity.md": "foundations", "claim_phase_provenance.md": "foundations",
    "reafference_comparator_family.md": "foundations", "non_deficit_action_drives.md": "foundations",
    "version_layering_doctrine.md": "foundations",
    "arc_106_biology_grounding_framework.md": "foundations",
    "canonical_profile_admission_criteria.md": "foundations",
    "active_inference_bridge.md": "foundations", "bitter_lesson_position.md": "foundations",
    "cognitive_architecture_graveyard.md": "foundations", "corrigibility_positioning.md": "foundations",
    "formal_ancestor_mapping.md": "foundations", "work_graph_debt_vocabulary.md": "foundations",
    "causal_reach_and_installability.md": "foundations",

    # --- Perception, Representation & Dynamics ---
    "residue_geometry.md": "representation", "sensory_stream_tags.md": "representation",
    "sense_specific_perceptual_manifolds.md": "representation", "temporal_dynamics.md": "representation",
    "e1_e2_constraint_propagation.md": "representation", "dv_temporal_depth_v3_form.md": "representation",

    # --- Attention, Binding & Objects ---
    "why_attention_must_be_fragmented.md": "attention", "entities_and_binding.md": "attention",
    "frontal_cue_integration.md": "attention", "sd_016_frontal_cue_integration.md": "attention",
    "sd_032_cingulate_integration_substrate.md": "attention", "event_segmenter.md": "attention",
    "mech_045_object_file_buffer.md": "attention", "arc_080_object_representation_primitive.md": "attention",
    "mech_294_multi_content_theta_packet.md": "attention",
    "sd_cross_stream_binding_substrate.md": "attention",

    # --- Control, Precision & Neuromodulation ---
    "control_plane.md": "control", "control_plane_heartbeat.md": "control",
    "control_plane_signal_map.md": "control", "neuromodulatory_control_planes.md": "control",
    "precision_control.md": "control", "precision_scoping.md": "control",
    "path_authority_and_interrupts.md": "control", "plasticity_write_authority_gating.md": "control",
    "serotonin.md": "control", "astrocyte_regulatory_stack.md": "control",
    "receptor_subtype_intervention_layer.md": "control", "sd_024_da_modulated_rbf_density.md": "control",
    "mech_313_stochastic_noise_floor.md": "control", "sd_036_gabaergic_decay_regulator.md": "control",
    "sd_037_broadcast_override_regulator.md": "control", "mech_271_routing_v3_substrate_plan.md": "control",
    "state_conditioned_exploration_noise_floor.md": "control",
    "sd_091_coalition_topology_control.md": "control",
    "reusable_computational_motifs.md": "control",

    # --- Memory & Hippocampus ---
    "hippocampal_systems.md": "memory", "hippocampal_braid.md": "memory",
    "hippocampal_anchor_selection.md": "memory", "hippocampal_literature_synthesis_2026.md": "memory",
    "hippocampal_map_tagged_channels.md": "memory", "hippocampal_valence_asymmetry.md": "memory",
    "valenced_hippocampal_map.md": "memory", "papez_circuit.md": "memory",
    "developmental_bootstrapping_hippo_retrieval.md": "memory", "sd_039_anchor_goal_payload.md": "memory",
    "mech_189_super_ordinal_goal_anchors.md": "memory",
    "autobiographical_temporality_and_future_simulation.md": "memory",
    "sd_mech267_cem_selection_fix.md": "memory",
    "ephaptic_hippocampal_now_construction.md": "memory",

    # --- Modes, Agency & Default Mode ---
    "mode_manager.md": "modes", "modes_of_cognition.md": "modes", "default_mode.md": "modes",
    "play_mode.md": "modes", "play_substrate_design.md": "modes",
    "externalised_dmn_play_private_speech.md": "modes", "agency_responsibility_flow.md": "modes",
    "trajectory_selection.md": "modes", "three_loop_learning_channels.md": "modes",
    "self_attribution_per_stream.md": "modes", "tpj_agency_comparator.md": "modes",
    "v_s_invalidation_runtime.md": "modes", "mech_269b_vs_rollout_gating.md": "modes",

    # --- Goals, Drives & Motivation ---
    "goal_wanting_signal_chain.md": "goals", "sustained_drive_anticipatory_wanting.md": "goals",
    "ghost_goal_search.md": "goals", "mech_292_ghost_goal_bank.md": "goals",
    "mech_293_ghost_goal_probe_search.md": "goals", "mech_295_drive_liking_approach_bridge.md": "goals",
    "mech_303_contextual_safety_terrain.md": "goals", "sd_012_homeostatic_drive.md": "goals",
    "sd_050_suffering_derivative_comparator.md": "goals", "sd_051_conditioned_safety_store.md": "goals",
    "sd_065_conditioned_safety_cue_channel.md": "goals",
    "sd_057_object_bound_incentive_salience.md": "goals", "sd_058_instrumental_avoidance_acquisition.md": "goals",
    "sd_059_escape_affordance_bridge.md": "goals", "trainable_relief_safety_affordance_learners.md": "goals",
    "sd_actor_critic_action_learning.md": "goals",
    "mech_111_per_candidate_novelty.md": "goals", "mech_314_structured_curiosity_bonus.md": "goals",
    "mech_314a_phase2_novelty_source_design.md": "goals",
    "sd_061_difficulty_gated_proposal_entropy.md": "goals",
    "sd_hazard_aware_policy_decomposition.md": "goals",
    "sd_092_cross_level_subgoal_credit.md": "goals",
    "sd_093_progress_velocity_maintenance.md": "goals",
    "sd_mech267_horizon_depth_modulation.md": "memory",
    "competence_bootstrap_mechanisms.md": "goals", "sd_mech303_threshold_sourcing.md": "goals",
    "sd_mech457_approach_extinction.md": "goals", "sd_mech457_bc_aux_schedule.md": "goals",
    "sd_mech457_competence_bootstrap_explorer.md": "goals", "sd_mech457_consummatory_act.md": "goals",
    "sd_mech457_distributional_critic.md": "goals", "sd_mech457_retention_trajectory_probe.md": "goals",

    # --- Affect, Harm & Nociception ---
    "affect_primitives.md": "affect", "affect_terminology_instinct_protoemotion.md": "affect",
    "anticipatory_affect_conjunction_vs_dual_channel.md": "affect",
    "candidate_differentiated_affective_gradients.md": "affect",
    "emotion_as_anti_collapse_architecture.md": "affect", "vmPFC.md": "affect",
    "arc_033_e2_harm_s_forward_model.md": "affect", "sd_010_harm_stream_separation.md": "affect",
    "sd_011_dual_nociceptive_streams.md": "affect", "sd_013_e2_harm_s_interventional_training.md": "affect",
    "sd_019_harm_nonredundancy.md": "affect", "sd_020_harm_surprise_pe.md": "affect",
    "sd_021_descending_pain_modulation.md": "affect", "sd_022_directional_limb_damage.md": "affect",
    "sd_023_environmental_gradient_texture.md": "affect", "sd_035_amygdala_analog.md": "affect",
    "sd_048_interoceptive_noise_dynamics.md": "affect", "mech_219_hysteretic_integrator.md": "affect",
    "mech_353_blocked_agency_zblock.md": "affect",

    # --- Executive & PFC Control ---
    "sd_033_pfc_subdivision_architecture.md": "pfc", "sd_033a_lateral_pfc_analog.md": "pfc",
    "sd_033b_ofc_analog.md": "pfc", "sd_033d_premotor_sma_analog.md": "pfc",
    "sd_034_governance_closure_operator.md": "pfc", "mech_090_commit_entry_predicate.md": "pfc",
    "mech_319_simulation_mode_rule_gate.md": "pfc", "mech_341_e3_score_diversity_preservation.md": "pfc",
    "mech_342_commit_maintenance_release.md": "pfc", "rule_apprehension_layer.md": "pfc",
    "arc_063_candidate_rule_field.md": "pfc", "phased_rule_state_training_curriculum.md": "pfc",
    "sd_055_differentiable_cem_selection.md": "pfc",
    "dr10_z_self_in_e3_viability.md": "pfc", "dr12_pe_conditioned_e3_confidence.md": "pfc",
    "dr13_self_recurrence_temporal_depth.md": "pfc", "mech_448_f_eligibility_demotion.md": "pfc",
    "mech_449_go_nogo_constitution.md": "pfc",
    "natural_commit_occupancy_release.md": "pfc", "quality_diversity_committed_archive.md": "pfc",
    "rule_distinguishability_maintenance.md": "pfc",
    "dopamine_into_gating.md": "pfc", "arc_108_job2_control_plane.md": "pfc",
    "mech_451_finer_channel_granularity.md": "pfc",
    "persistent_process_termination_taxonomy.md": "pfc",
    "temporally_displaced_actionable_present.md": "pfc",

    # --- Language ---
    "language.md": "language", "arcuate_fasciculus.md": "language",

    # --- Sleep & Offline Integration ---
    "sleep.md": "sleep", "sleep_aggregation_cluster.md": "sleep",
    "sd_017_sleep_phase_architecture.md": "sleep", "compact_consolidation_principle.md": "sleep",
    "prioritized_replay_write_gating.md": "sleep",
    "sd_mel_consumer.md": "sleep", "sd_mel_producer.md": "sleep",
    "offline_representational_reindexing.md": "sleep",

    # --- Social & Clinical ---
    "social.md": "social", "psychiatric_failure_axes.md": "social",
    "psychiatric_failure_modes.md": "social", "depressive_network_regimes.md": "social",
    "slow_modulatory_state_and_compulsive_loops.md": "social", "laughter_social_load_release.md": "social",

    # --- Development & Curriculum ---
    "developmental_curriculum.md": "development", "developmental_metrics.md": "development",
    "developmental_needs_register.md": "development", "developmental_experiment_priorities.md": "development",
    "developmental_governance_review.md": "development", "monostrategy_developmental_analysis.md": "development",
    "infant_substrate_expansion.md": "development", "scientist_agent_developmental_ordering.md": "development",
    "developmental_pruning_and_sparse_memory_cognifold.md": "development", "replay_development_analysis.md": "development",
    "critical_period_crystallization.md": "development", "sd_047_multi_source_dynamics.md": "development",
    "sd_049_multi_resource_heterogeneity.md": "development", "sd_054_reef_enrichment_substrate.md": "development",
    "effort_dissociation_env.md": "development",

    # --- Specs, Diagrams & Versions ---
    "diagram_views.md": "specs", "jepa_e1e2_integration_contract.md": "specs",
    "jepa_ree_hybrid_diagram_spec.md": "specs", "ree_v2_spec.md": "specs",
    "ree_v2_repo_bootstrap_spec.md": "specs", "brain_map.md": "specs",
    "hook_surface_contract.md": "specs", "streams.md": "specs",
    "v2_v3_transition_roadmap.md": "specs", "v3_v4_transition_boundary.md": "specs",
    "v3_v4_phase_substrate_boundary.md": "specs",
    "sd_queue_seed_enforcement.md": "specs",

    # --- Roadmap & Planning (V4+) ---
    "architecture_scaling_needs.md": "roadmap", "substrate_roadmap.md": "roadmap",
    "v4_planning_index.md": "roadmap", "v4_spec.md": "roadmap",
    "v4_developmental_harness_spec.md": "roadmap", "mech_423_superadditivity_readiness_substrate.md": "roadmap",
    "cognifold_signed_coupling.md": "roadmap", "spintronic_memristive_cognifold_substrate.md": "roadmap",
}

# Subdir pages (all language/* -> language; all sleep/* -> sleep)
SUBDIR_ASSIGN = {
    "language/emergence_and_bootstrapping.md": "language",
    "language/language_and_institutions.md": "language",
    "language/language_and_learning.md": "language",
    "language/language_failure_modes.md": "language",
    "language/minimal_signalling_channel.md": "language",
    "language/trust_and_deception.md": "language",
    "sleep/medications_dementia.md": "sleep",
    "sleep/offline_phases.md": "sleep",
    "sleep/precision_recalibration.md": "sleep",
    "sleep/reality_consolidation.md": "sleep",
    "sleep/residue_integration.md": "sleep",
    "sleep/serotonergic_cross_state_substrate.md": "sleep",
    "comparisons/meta_kaust_neural_computers.md": "specs",
}

# Architecture pages deliberately hidden from the sidebar (scratch / session
# prompts / narrow impl notes). Still build + reachable by URL.
ARCH_SCRATCH = [
    "context_memory_writepath_fix.md",
    "control_vector_logging.md",
    "landing_integration_worker_investigation.md",
    "mech163_planned_system_gate_session_prompt.md",
    "mech188_vs_mech295_dual_path.md",
    "mech_318_absorption_check.md",
    "modulatory_bias_selection_authority.md",
    "precision_update_callsite.md",
    "sd015_hippocampal_nav_session_prompt.md",
    "sd_003_experiment_design.md",
    "sd_016_writepath_v3_diversification_loss.md",
    "threshold_supervisor_survey.md",
]

# Top-level docs hidden from sidebar (reachable by link).
TOP_EXCLUDE = [
    "FINAL_OUTPUT.md", "MIGRATION.md", "REE_ARCHITECTURE_SNAPSHOT_2026-02-17.md",
    "REE_MIN_SPEC.md", "REE_overview.md",
    "changelog.md", "repo_meta.md", "README.md", "repo_meta.md",
    # Reachable by URL / linked from Home, deliberately kept out of the themed sidebar.
    "START_HERE_HOW_REE_DEVELOPS.md", "public_explorer_policy.md",
    # Sanitized public overview of the mobile-access runbook; operational, not architecture.
    # mobile_access.local.md is gitignored and absent on most checkouts -- stamp() no-ops
    # via its exists() check when it isn't there, so listing it here is safe everywhere.
    "mobile_access.md", "mobile_access.local.md",
]

# Whole subdirectories whose .md/.html pages are excluded from the sidebar.
EXCLUDE_SUBDIRS = ["claims", "conflicts", "governance", "examples", "session_prompts", "processed"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_existing_frontmatter(text):
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    return text[end + 5:]


# SHP-5 co-tenancy: docs/apply_status_frontmatter.py stamps status_* keys into the
# SAME frontmatter block this script owns and re-strips every run. To let the two
# stampers compose in either order, we carry the status_* lines across a nav re-stamp
# instead of clobbering them. Keep this key set in sync with STATUS_KEYS there.
_STATUS_KEYS_RE = re.compile(r"^(status|status_asof|status_claim):")


def _extract_status_lines(text):
    """Raw status_* frontmatter lines from an existing block, preserved verbatim so a
    nav re-stamp does not wipe docs/apply_status_frontmatter.py's SHP-5 keys."""
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---\n", 4)
    if end == -1:
        return []
    return [ln for ln in text[4:end].split("\n") if _STATUS_KEYS_RE.match(ln)]


def render_frontmatter(fm, extra_lines=None):
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, bool):
            lines.append("{}: {}".format(k, str(v).lower()))
        elif isinstance(v, int):
            lines.append("{}: {}".format(k, v))
        else:
            special = [":", "{", "}", "[", "]", "#", "&", "*", "!", "|", ">", "'", '"', "%", "@", "`"]
            if any(c in str(v) for c in special):
                lines.append('{}: "{}"'.format(k, str(v).replace('"', '\\"')))
            else:
                lines.append("{}: {}".format(k, v))
    if extra_lines:
        lines.extend(extra_lines)
    lines.append("---")
    return "\n".join(lines) + "\n"


def stamp(rel_path, fm):
    abs_path = os.path.join(DOCS, rel_path)
    if not os.path.exists(abs_path):
        print("SKIP (not found): {}".format(rel_path))
        return False
    with open(abs_path, "r", encoding="utf-8") as f:
        text = f.read()
    carried = _extract_status_lines(text)
    body = strip_existing_frontmatter(text)
    new_text = render_frontmatter(fm, carried) + "\n" + body.lstrip("\n")
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True


def title_of(abs_path):
    """First markdown H1, else prettified filename."""
    try:
        for line in open(abs_path, encoding="utf-8", errors="ignore"):
            s = line.strip()
            if s.startswith("# "):
                return s[2:].strip()
    except Exception:
        pass
    base = os.path.splitext(os.path.basename(abs_path))[0]
    return base.replace("_", " ").replace("-", " ").title()


# ---------------------------------------------------------------------------
# Tidiness sweep: hide any titled-but-unplaced page so new docs never leak
# raw into the left sidebar. This is the self-maintaining guard the nightly
# routine relies on -- see scripts/governance.sh and the /update-docs skill.
# ---------------------------------------------------------------------------

def _placed_set():
    """Every docs-relative path this script explicitly positions in the nav."""
    placed = set(TOP_LEVEL.keys())
    placed |= set(GOVERNANCE_CHILDREN.keys())
    placed |= set(VERSIONS_CHILDREN.keys())
    placed |= {"architecture/" + b for b in ASSIGN}
    placed |= {"architecture/" + k for k in SUBDIR_ASSIGN}
    placed |= {"architecture/" + b for b in ARCH_SCRATCH}
    placed |= set(TOP_EXCLUDE)
    placed.add("governance_section.md")
    placed.add("architecture/overview.md")
    # CURRENT_FRONT.md is generated by scripts/generate_current_front.py (SHP-6):
    # it owns its own body and is a repo-read routing doc, not a site-sidebar page.
    # Mark it placed so the tidiness sweep neither flags it as a leak nor nags it
    # as unplaced, and never rewrites the generator's output.
    placed.add("CURRENT_FRONT.md")
    return placed


def _has_frontmatter(text):
    return text.startswith("---\n")


def _fm_block(text):
    if not _has_frontmatter(text):
        return ""
    end = text.find("\n---\n", 4)
    return text[4:end] if end != -1 else ""


# Top-level directories (relative to docs/) this script actually positions in
# the nav -- the only two page classes it is entitled to touch: bare top-level
# docs/*.md|*.html files, and the architecture/ subtree. Every other docs/
# subdirectory (thoughts/, notes/, strategy/, design/, experiment_profiles/,
# fishtank/, public_explorer/, brain_map/, plus build dirs like _data/,
# _includes/, assets/, __pycache__) is owned by some other convention -- e.g.
# docs/thoughts/*.md carries thought-digestion metadata (date/scope/
# related_claims/processed_in) that has nothing to do with the sidebar -- and
# must never be walked by the tidiness sweep below, regardless of whether a
# given file happens to have a `title:` key in frontmatter.
#
# 2026-08-02 incident: the sweep used to walk ALL of docs/ (os.walk(DOCS) with
# no top-dir filter) and treated any titled, non-nav_exclude page outside the
# explicitly-registered placed set as a "leak" to auto-hide. That reached
# thoughts/2026-08-01_metacognitive_control_selective_cognitive_coalition_
# instantiation.md (the first docs/thoughts/ file to carry a frontmatter
# block) and wholesale-overwrote its date/scope/related_claims/processed_in
# fields down to bare {title, nav_exclude: true}. Manually reverted same
# night; this SWEEP_DIRS allowlist is the structural fix -- see also the
# placement-preserving check in scan_unplaced() below for the architecture/
# half of the same incident (sd_hazard_aware_policy_decomposition.md).
SWEEP_DIRS = {"architecture"}


def _has_deliberate_placement(fm_block):
    """True if an existing frontmatter block already sets both `parent:` and
    `nav_order:` -- i.e. someone (a landing session, a hand-edit) already gave
    this page a real sidebar position, as opposed to a bare `title:` with
    nothing else. Distinguishes "freshly created, never placed, safe to
    auto-hide" from "was deliberately filed, just not yet mirrored into this
    script's ASSIGN map" -- collapsing both to nav_exclude is exactly what
    destroyed sd_hazard_aware_policy_decomposition.md's placement in the
    2026-08-02 incident."""
    import re as _re
    has_parent = bool(_re.search(r'(?m)^parent:\s*\S', fm_block))
    has_order = bool(_re.search(r'(?m)^nav_order:\s*\S', fm_block))
    return has_parent and has_order


def scan_unplaced():
    """Return (leaks, hidden_no_fm, unregistered_placed), scoped to SWEEP_DIRS.

    leaks              = pages with a `title:` and no `nav_exclude`, not
                         explicitly placed and with no deliberate placement of
                         their own -> these WOULD render raw in the sidebar
                         (the drift) and are safe to auto-hide.
    unregistered_placed = same "not explicitly placed" condition, but the page
                         ALREADY has its own parent+nav_order set (someone
                         filed it by hand) -> the drift is a stale ASSIGN map,
                         not an unfiled doc. Never auto-hidden; report only.
    hidden_no_fm       = architecture/top-level pages with no frontmatter and
                         not in ASSIGN/TOP_LEVEL -> invisible today (just-the-
                         docs needs a title), surfaced only as a reminder to
                         file them into a theme.
    """
    placed = _placed_set()
    leaks, hidden_no_fm, unregistered_placed = [], [], []
    import re as _re
    for root, dirs, files in os.walk(DOCS):
        rel_root = os.path.relpath(root, DOCS).replace("\\", "/")
        parts = [] if rel_root == "." else rel_root.split("/")
        if parts and parts[0] not in SWEEP_DIRS:
            dirs[:] = []  # prune -- never descend into an unowned top dir
            continue
        if any(p in EXCLUDE_SUBDIRS for p in parts):
            continue
        if "sections" in parts:
            continue
        for fn in files:
            if not fn.endswith((".md", ".html")):
                continue
            rel = os.path.relpath(os.path.join(root, fn), DOCS).replace("\\", "/")
            if rel in placed:
                continue
            try:
                text = open(os.path.join(root, fn), encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            if _has_frontmatter(text):
                fm = _fm_block(text)
                has_title = bool(_re.search(r"(?m)^title:\s*\S", fm))
                excluded = bool(_re.search(r"(?m)^nav_exclude:\s*true", fm))
                if has_title and not excluded:
                    if _has_deliberate_placement(fm):
                        unregistered_placed.append(rel)
                    else:
                        leaks.append(rel)
            else:
                # No frontmatter: invisible in nav. Only nag for top-of-tree
                # architecture docs + bare top-level docs (where a real design
                # doc would want a home); ignore deep scratch.
                depth = rel.count("/")
                if rel.startswith("architecture/") and depth == 1:
                    hidden_no_fm.append(rel)
                elif depth == 0:
                    hidden_no_fm.append(rel)
    return sorted(leaks), sorted(hidden_no_fm), sorted(unregistered_placed)


def sweep_unplaced():
    """Stamp nav_exclude on every titled-but-truly-unplaced page (preserving
    title). Deliberately does NOT touch unregistered_placed pages (see
    scan_unplaced) -- those already carry real placement and must be fixed by
    adding them to ASSIGN, never by overwriting their frontmatter. Returns the
    list of paths hidden this pass."""
    leaks, _, _ = scan_unplaced()
    for rel in leaks:
        abs_path = os.path.join(DOCS, rel)
        text = open(abs_path, encoding="utf-8", errors="ignore").read()
        title = title_of(abs_path)
        fm = {"title": title, "nav_exclude": True}
        carried = _extract_status_lines(text)
        body = strip_existing_frontmatter(text)
        open(abs_path, "w", encoding="utf-8").write(
            render_frontmatter(fm, carried) + "\n" + body.lstrip("\n"))
    return leaks


def check():
    """Report-only drift check for the nightly routine. Exit non-zero if any
    titled-but-unplaced page would leak into the sidebar, or if a page that
    was already deliberately filed (parent+nav_order set by hand) is missing
    from ASSIGN -- the latter is flagged, never silently auto-hidden (see
    scan_unplaced's unregistered_placed and the 2026-08-02 incident note)."""
    leaks, hidden, unregistered = scan_unplaced()
    if leaks:
        print("NAV DRIFT: {} titled page(s) not placed -- would render RAW in the sidebar:".format(len(leaks)))
        for r in leaks:
            print("   LEAK  " + r)
        print("Fix: add each to ASSIGN/TOP_LEVEL in docs/apply_nav_frontmatter.py, or it will be auto-hidden on the next run.")
    if unregistered:
        print("NAV DRIFT: {} page(s) already have a deliberate parent+nav_order but are NOT in ASSIGN:".format(len(unregistered)))
        for r in unregistered:
            print("   UNREGISTERED (placement preserved, NOT auto-hidden)  " + r)
        print("Fix: add each to ASSIGN in docs/apply_nav_frontmatter.py to match the theme its own frontmatter already claims.")
    if hidden:
        print("FYI: {} architecture/top-level doc(s) have no frontmatter (hidden from nav until filed into a theme):".format(len(hidden)))
        for r in hidden:
            print("   hidden  " + r)
    if not leaks and not hidden and not unregistered:
        print("Nav is tidy: every titled page is explicitly placed; no orphan design docs.")
    return 1 if (leaks or unregistered) else 0


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

def run():
    count = 0

    # 1. Top-level pages
    for rel, fm in TOP_LEVEL.items():
        if stamp(rel, fm):
            count += 1

    # 2. Governance section
    if stamp("architecture/overview.md", TOP_LEVEL["architecture/overview.md"]):
        pass  # already done above; harmless
    # Governance parent is a dedicated stub page so the section has a landing page.
    gov_stub = "governance_section.md"
    gov_fm = dict(GOVERNANCE_PARENT)
    gov_path = os.path.join(DOCS, gov_stub)
    if not os.path.exists(gov_path):
        with open(gov_path, "w", encoding="utf-8") as f:
            f.write(render_frontmatter(gov_fm) + "\n# Governance\n\n"
                    "How REE governs its own claims: the verification gate and the "
                    "evaluation-channel integrity model. Select a page from the navigation.\n")
        count += 1
    else:
        stamp(gov_stub, gov_fm)
    for rel, fm in GOVERNANCE_CHILDREN.items():
        if stamp(rel, fm):
            count += 1
    for rel, fm in VERSIONS_CHILDREN.items():
        if stamp(rel, fm):
            count += 1

    # 3. Architecture section stub pages
    if not os.path.isdir(SECTIONS_DIR):
        os.makedirs(SECTIONS_DIR)
    for key, title, order in SECTIONS:
        rel = "architecture/sections/{}.md".format(key)
        fm = {"title": title, "parent": "Architecture", "has_children": True, "nav_order": order}
        path = os.path.join(DOCS, rel)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(render_frontmatter(fm) + "\n# {}\n\n".format(title)
                        + "Architecture documents in this area. Select a page from the navigation.\n")
            count += 1
        else:
            stamp(rel, fm)

    # 4. Architecture doc pages -> theme child, sorted by title within theme
    #    First gather (rel, key, title) so we can assign nav_order per theme.
    members = {}  # key -> list of (title, rel)
    def add_member(rel, key):
        abs_path = os.path.join(DOCS, rel)
        if not os.path.exists(abs_path):
            print("SKIP (not found): {}".format(rel))
            return
        members.setdefault(key, []).append((title_of(abs_path), rel))

    for base, key in ASSIGN.items():
        add_member("architecture/" + base, key)
    for rel, key in SUBDIR_ASSIGN.items():
        add_member("architecture/" + rel, key)

    for key, items in members.items():
        for order, (title, rel) in enumerate(sorted(items), start=1):
            fm = {"title": title, "parent": SECTION_TITLE[key],
                  "grandparent": "Architecture", "nav_order": order}
            if stamp(rel, fm):
                count += 1

    # 5. Exclusions
    for base in ARCH_SCRATCH:
        if stamp("architecture/" + base, {"nav_exclude": True}):
            count += 1
    for base in TOP_EXCLUDE:
        if stamp(base, {"nav_exclude": True}):
            count += 1
    for sub in EXCLUDE_SUBDIRS:
        subpath = os.path.join(DOCS, sub)
        if not os.path.isdir(subpath):
            continue
        for root, _dirs, files in os.walk(subpath):
            for fn in files:
                if fn.endswith((".md", ".html")):
                    rel = os.path.relpath(os.path.join(root, fn), DOCS)
                    if stamp(rel, {"nav_exclude": True}):
                        count += 1

    # 6. Tidiness guard: hide any titled-but-unplaced page so a newly-added
    #    plan/design doc never leaks raw into the sidebar. Reports what it hid
    #    and what design docs are still un-filed (no frontmatter).
    hidden = sweep_unplaced()
    if hidden:
        print("\nAuto-hidden {} unplaced titled page(s) (add to ASSIGN to surface):".format(len(hidden)))
        for r in hidden:
            print("   nav_exclude  " + r)
        count += len(hidden)
    _, no_fm, unregistered = scan_unplaced()
    if no_fm:
        print("\nFYI -- {} architecture/top-level doc(s) without frontmatter (hidden until filed into a theme):".format(len(no_fm)))
        for r in no_fm:
            print("   unfiled  " + r)
    if unregistered:
        # Deliberately NOT auto-hidden -- these already carry a real
        # parent+nav_order, just not yet mirrored into ASSIGN. Report loudly
        # instead of overwriting; see the 2026-08-02 incident note above
        # scan_unplaced().
        print("\nNAV DRIFT -- {} page(s) already placed by hand but missing from ASSIGN (frontmatter left untouched):".format(len(unregistered)))
        for r in unregistered:
            print("   unregistered  " + r)

    print("\nDone. {} files stamped.".format(count))


if __name__ == "__main__":
    import sys
    if "--check" in sys.argv:
        sys.exit(check())
    run()
