# REE Claim Index

This index lists all claim IDs with one-line summaries and links. For full metadata, see `claims.yaml`.

**Claim Type:** implementation_note  
**Scope:** Claim index and navigation  
**Depends On:** None  
**Status:** stable  
**Claim ID:** IMPL-018
<a id="impl-018"></a>

---

## Invariants (INV)

- [INV-001](../invariants.md#inv-001) No explicit ethics module or moral scoring layer.
- [INV-002](../invariants.md#inv-002) Coherence includes temporal/phase binding, not just static metrics.
- [INV-003](../invariants.md#inv-003) Language emerges as functional self-representation, not a bolt-on.
- [INV-004](../invariants.md#inv-004) Post-commit consequence traces are persistent, not resettable.
- [INV-005](../invariants.md#inv-005) Harm to others contributes via mirror modelling, not symbolic rules.
- [INV-006](../invariants.md#inv-006) Post-commit consequence traces cannot be erased, only integrated.
- [INV-007](../invariants.md#inv-007) Language cannot override embodied harm sensing.
- [INV-008](../invariants.md#inv-008) Precision is routed and depth-specific, not global.
- [INV-009](../invariants.md#inv-009) Attention is precision modulation, not symbolic control.
- [INV-010](../invariants.md#inv-010) Offline integration exists and is required.
- [INV-011](../invariants.md#inv-011) Imagination must be possible without belief update.
- [INV-012](../invariants.md#inv-012) Responsibility arises through commitment, not prediction alone.
- [INV-013](../invariants.md#inv-013) Cognition is predictive, iterative, and multi-timescale.
- [INV-014](../invariants.md#inv-014) Representation and regulation are strictly separated.
- [INV-015](../invariants.md#inv-015) Ethics emerges from constraint, not optimisation.
- [INV-016](../invariants.md#inv-016) Stability is prioritized over maximal performance.
- [INV-017](../invariants.md#inv-017) Runaway behavior is a control failure, not representational.
- [INV-018](../invariants.md#inv-018) Agency is required; passive predictors are not REE.

---

## Architectural Commitments (ARC)

- [ARC-001](../architecture/e1.md#arc-001) E1 is the persistent predictive substrate.
- [ARC-002](../architecture/e2.md#arc-002) E2 is the fast forward predictor of affordances.
- [ARC-003](../architecture/e3.md#arc-003) E3 selects and commits trajectories.
- [ARC-004](../architecture/l_space.md#arc-004) L-space is a multi-timescale latent stack.
- [ARC-005](../architecture/control_plane.md#arc-005) Control plane routes precision and modes.
- [ARC-006](../architecture/entities_and_binding.md#arc-006) Entities are sparse, persistent, bindable structures.
- [ARC-007](../architecture/hippocampal_systems.md#arc-007) Hippocampal systems store and replay paths.
- [ARC-008](../architecture/temporal_dynamics.md#arc-008) Commitment eligibility is gated by tau, rho, and phi.
- [ARC-009](../architecture/language.md#arc-009) Language is a symbolic mediation and coordination layer.
- [ARC-010](../architecture/social.md#arc-010) Social cognition uses mirror modelling and coupling.
- [ARC-011](../architecture/sleep.md#arc-011) Offline integration (sleep) is required for stability.
- [ARC-012](../architecture/e3.md#arc-012) E3 does not require an explicit ethical cost term.
- [ARC-013](../architecture/residue_geometry.md#arc-013) Residue is persistent latent-space curvature; hippocampal paths form a cognitive map.
- [ARC-014](../architecture/default_mode.md#arc-014) Default Mode enables safe imagination without commitment.
- [ARC-015](../architecture/agency_responsibility_flow.md#arc-015) Self-impact attribution and responsibility flow are required.
- [ARC-016](../architecture/modes_of_cognition.md#arc-016) Modes are control-plane regimes applied to shared predictive machinery.
- [ARC-017](../architecture/sensory_stream_tags.md#arc-017) Minimal sensory stream tags for REE (world, homeostasis, harm, self-sensory, precision, temporal coherence, valence, action, self-impact).
- [ARC-018](../architecture/hippocampal_systems.md#arc-018) Hippocampus generates explicit rollouts and post-commitment viability mapping.
- [ARC-019](../architecture/developmental_curriculum.md#arc-019) REE requires staged developmental training with explicit curriculum gates.

---

## Mechanism Hypotheses (MECH)

- [MECH-001](../architecture/astrocyte_regulatory_stack.md#mech-001) Astrocyte-aware regulatory stack mediates control-plane precision routing.
- [MECH-002](../architecture/precision_control.md#mech-002) Precision control analogues shape cognitive regimes.
- [MECH-003](../architecture/precision_scoping.md#mech-003) Precision must be tau-scoped with lossy projections.
- [MECH-004](../architecture/control_plane_signal_map.md#mech-004) Signal-to-knob wiring map for control plane.
- [MECH-005](../architecture/path_authority_and_interrupts.md#mech-005) Path authority and interruptibility via norepinephrine-like control.
- [MECH-006](../architecture/serotonin.md#mech-006) Serotonin-like modulation governs representational collapse.
- [MECH-007](../architecture/why_attention_must_be_fragmented.md#mech-007) Attention must be fragmented across control axes.
- [MECH-008](../architecture/mode_manager.md#mech-008) Legacy: superseded by AA/PCM + control-channel mode framing (MECH-046/047/048, MECH-039).
- [MECH-010](../architecture/language/emergence_and_bootstrapping.md#mech-010) Language emergence and bootstrapping dynamics.
- [MECH-011](../architecture/language/language_and_learning.md#mech-011) Language and learning dynamics.
- [MECH-012](../architecture/language/language_and_institutions.md#mech-012) Language and institutions interplay.
- [MECH-013](../architecture/language/language_failure_modes.md#mech-013) Language failure modes and pathologies.
- [MECH-014](../architecture/language/minimal_signalling_channel.md#mech-014) Minimal signalling channel requirements.
- [MECH-015](../architecture/language/trust_and_deception.md#mech-015) Trust and deception dynamics.
- [MECH-016](../architecture/sleep/precision_recalibration.md#mech-016) Precision recalibration during sleep.
- [MECH-017](../architecture/sleep/reality_consolidation.md#mech-017) Reality consolidation during sleep.
- [MECH-018](../architecture/sleep/residue_integration.md#mech-018) Residue integration during sleep.
- [MECH-019](../architecture/control_plane.md#mech-019) Control plane shapes modes of cognition, not discrete choices.
- [MECH-020](../architecture/mode_manager.md#mech-020) Legacy: superseded by control-plane mode framing (MECH-019, MECH-039).
- [MECH-021](../architecture/temporal_dynamics.md#mech-021) Subjective “now” is a control surface across horizons.
- [MECH-022](../architecture/hippocampal_systems.md#mech-022) Hippocampal systems inject hypotheses gated by control plane.
- [MECH-023](../architecture/agency_responsibility_flow.md#mech-023) Responsibility is geometric and path-dependent.
- [MECH-024](../architecture/agency_responsibility_flow.md#mech-024) Selfhood, personality, and ethics converge structurally.
- [MECH-025](../architecture/modes_of_cognition.md#mech-025) Action mode prioritizes short-horizon, high-precision, responsibility-linked control.
- [MECH-026](../architecture/modes_of_cognition.md#mech-026) Ready vigilance primes restraint under high sensitivity without action.
- [MECH-027](../architecture/modes_of_cognition.md#mech-027) Pathological modes reflect mis-tuned control-plane regimes.
- [MECH-028](../architecture/modes_of_cognition.md#mech-028) Ethical behavior depends on mode transitions and learning preservation.
- [MECH-029](../architecture/default_mode.md#mech-029) Reflective/DMN mode supports moral simulation via gated replay.
- [MECH-030](../architecture/sleep.md#mech-030) Sleep modes consolidate learning and ethical residue across regimes.
- [MECH-031](../architecture/social.md#mech-031) Derived social tags and empathy coupling via control-plane knobs.
- [MECH-032](../architecture/social.md#mech-032) OTHER_SELFLIKE detection is biased toward high recall to avoid empathy false negatives.
- [MECH-033](../architecture/hippocampal_systems.md#mech-033) E2 forward-prediction kernels seed hippocampal rollouts.
- [MECH-034](../architecture/residue_geometry.md#mech-034) Viability mapping updates are distinct from residue curvature updates.
- [MECH-035](../architecture/sensory_stream_tags.md#mech-035) VALENCE is vector-valued and ranked without scalar collapse.
- [MECH-036](../architecture/social.md#mech-036) Other-harm triggers veto only under high-certainty catastrophic outcomes.
- [MECH-037](../architecture/papez_circuit.md#mech-037) Papez-like loop provides provenance gating / reality filtering.
- [MECH-038](../architecture/arcuate_fasciculus.md#mech-038) Arcuate-like sequence-to-motor channel nudges language emergence.
- [MECH-039](../architecture/control_plane.md#mech-039) Modes are stable regions in control-channel space, not separate modules.
- [MECH-040](../architecture/control_plane.md#mech-040) Safety baseline and volatility are distinct control channels for arousal/readiness.
- [MECH-041](../architecture/social.md#mech-041) Affective expression broadcasts control‑plane regime to reduce social prediction load.
- [MECH-042](../architecture/control_plane.md#mech-042) Telemetry exposure channels report internal control‑plane state for diagnostics.
- [MECH-043](../architecture/precision_control.md#mech-043) Dopamine‑like modulation of precision‑weighting for unsigned prediction errors.
- [MECH-044](../architecture/entities_and_binding.md#mech-044) Hippocampal systems participate in relational binding and comparison.
- [MECH-045](../architecture/entities_and_binding.md#mech-045) Object‑file‑like buffers provide minimal entity persistence across time.
- [MECH-046](../architecture/control_plane.md#mech-046) Amygdala analogue updates control‑plane mode priors from fast salience classification.
- [MECH-047](../architecture/mode_manager.md#mech-047) Pre‑commitment mode manager commits with hysteresis and switching costs.
- [MECH-048](../architecture/control_plane.md#mech-048) μ/κ stability overlays modulate mode entropy and switching pressure.
- [MECH-049](../architecture/temporal_dynamics.md#mech-049) Temporal phase compartmentalisation preserves ethical constraint independence.
- [MECH-050](../architecture/entities_and_binding.md#mech-050) Functional locality supports attribution without requiring anatomical columns.
- [MECH-051](../architecture/social.md#mech-051) Oxytocin/vasopressin analogues modulate relational topology and mode priors.
- [MECH-052](../architecture/social.md#mech-052) Prolactin analogue stabilises care‑investment persistence.
- [MECH-053](../architecture/control_plane.md#mech-053) Habenula‑like aversive PE gate suppresses commitment under negative spikes.
- [MECH-054](../architecture/control_plane.md#mech-054) Signed harm/benefit prediction‑error precision channels remain distinct.
- [MECH-055](../architecture/control_plane.md#mech-055) Affective channel separation keeps hedonic tone, valence, and signed PE distinct.
- [MECH-056](../architecture/residue_geometry.md#mech-056) Residue should constrain trajectories before distorting core representations.
- [MECH-057](../architecture/agency_responsibility_flow.md#mech-057) Agentic latent-predictive models require control-plane completion and self-attribution loops.
- [MECH-058](../architecture/agency_responsibility_flow.md#mech-058) Slow target-anchor dynamics preserve E1/E2 substrate separation under JEPA-style training.
- [MECH-059](../architecture/agency_responsibility_flow.md#mech-059) Confidence channel (uncertainty-derived precision) must remain distinct from residual error for precision routing.
- [MECH-060](../architecture/agency_responsibility_flow.md#mech-060) Dual error channels should be separated across pre-commit simulation and post-commit realized outcomes.
- [MECH-061](../architecture/e3.md#mech-061) Commit-boundary token reclassifies pre-commit vs post-commit error routing.
- [MECH-062](../architecture/e3.md#mech-062) E3 should use coordinated tri-loop gating (motor, cognitive-set, motivational) instead of one global gate.
- [MECH-063](../architecture/control_plane.md#mech-063) Control plane should retain orthogonal tonic/phasic axes rather than collapsing into one scalar regulation signal.

---

## Open Questions (Q)

- [Q-001](../architecture/entities_and_binding.md#q-001) What mechanisms produce entity emergence and binding?
- [Q-002](../architecture/astrocyte_regulatory_stack.md#q-002) Appropriate spatial resolution for R(x,t)?
- [Q-003](../architecture/astrocyte_regulatory_stack.md#q-003) Should R(x,t) be scalar or vector?
- [Q-004](../architecture/astrocyte_regulatory_stack.md#q-004) How to calibrate tau_R relative to E1/E2?
- [Q-005](../architecture/astrocyte_regulatory_stack.md#q-005) Can sleep anneal or reset R(x,t)?
- [Q-006](../architecture/agency_responsibility_flow.md#q-006) Is ethics developmental rather than additive?
- [Q-007](../architecture/control_plane.md#q-007) Do universal expressions map to stable control‑channel regimes?
- [Q-008](../architecture/control_plane.md#q-008) Do μ/κ stability overlays obviate or complement valence vectors? Tracked in `docs/conflicts/valence_vectors_vs_mu_kappa_overlays.md`.
- [Q-009](../architecture/social.md#q-009) Can care‑investment weights override other‑harm veto without ethical failure? Tracked in `docs/conflicts/care_override_vs_other_harm_veto.md`.
- [Q-010](../architecture/control_plane.md#q-010) Legacy: separation question resolved into MECH‑055.
- [Q-011](../architecture/hippocampal_systems.md#q-011) Should REE enforce a minimum rollout-diversity floor under repeated unavoidable harm? Tracked in `docs/conflicts/rollout_entropy_floor_vs_residue_persistence.md`.
- [Q-012](../architecture/agency_responsibility_flow.md#q-012) Can latent predictive world models stay agentically stable without explicit REE-like control constraints?
- [Q-013](../architecture/agency_responsibility_flow.md#q-013) Can deterministic JEPA plus derived dispersion match explicit stochastic uncertainty heads for REE precision routing?
- [Q-014](../architecture/agency_responsibility_flow.md#q-014) Do JEPA invariances hide ethically relevant distinctions in REE attribution contexts?
- [Q-015](../architecture/e3.md#q-015) What is the smallest commit-boundary token that still supports reliable multi-timescale attribution?
- [Q-016](../architecture/e3.md#q-016) What arbitration policy best resolves tri-loop gate conflicts without coupling collapse?
- [Q-017](../architecture/control_plane.md#q-017) What is the minimal orthogonal control-axis subset that preserves observed regime separations?

---

## Implementation Notes (IMPL)

- [IMPL-001](../glossary.md#impl-001) Glossary of canonical REE terms.
- [IMPL-002](../repo_meta.md#impl-002) Repository metadata and contribution process.
- [IMPL-003](../REE_MIN_SPEC.md#impl-003) Minimum instantiation specification.
- [IMPL-004](../REE_overview.md#impl-004) Legacy REE overview summary.
- [IMPL-005](../REE_failure_modes.md#impl-005) Failure mode taxonomy.
- [IMPL-006](../MIGRATION.md#impl-006) Legacy migration mapping.
- [IMPL-007](../FINAL_OUTPUT.md#impl-007) Legacy refactor final output summary.
- [IMPL-008](../roadmap.md#impl-008) Program phases, repository roles, and phase-gate criteria.
- [IMPL-009](../notes/wiring_notes.md#impl-009) Wiring notes and cross-reference summary.
- [IMPL-010](../examples/android_world_environment.md#impl-010) Android world environment contract.
- [IMPL-011](../examples/toy_world_environment.md#impl-011) Toy world environment contract.
- [IMPL-012](../examples/toy_world_scoring_functions.md#impl-012) Toy world scoring functions.
- [IMPL-013](../README.md#impl-013) Documentation operating procedure and prompts.
- [IMPL-014](../changelog.md#impl-014) Documentation change history.
- [IMPL-015](../architecture/overview.md#impl-015) Legacy architecture overview.
- [IMPL-016](../architecture/trajectory_selection.md#impl-016) Trajectory selection detail for E3.
- [IMPL-017](../conflicts/README.md#impl-017) Conflict index and resolution entry point.
- [IMPL-018](../claims/claim_index.md#impl-018) Claim index and navigation.
- [IMPL-019](../architecture/developmental_curriculum.md#impl-019) Self-first, social-later developmental testing order heuristic.
- [IMPL-020](../glossary.md#impl-020) Formal JEPA↔REE terminology alignment glossary for interoperability.
- [IMPL-021](../architecture/jepa_ree_hybrid_diagram_spec.md#impl-021) Hybrid JEPA↔REE architecture diagram contract and rendering checklist.
- [IMPL-022](../architecture/jepa_e1e2_integration_contract.md#impl-022) JEPA-as-E1/E2 integration contract (inputs, outputs, knobs, and failure gates).
- [IMPL-023](../architecture/ree_v2_spec.md#impl-023) REE-v2 substrate-first spec and phase gate for later control completion.
- [IMPL-024](../notes/jepa_language_policy.md#impl-024) v2 JEPA-first wording policy with inline REE translation for docs and user-facing interactions.
- [IMPL-025](../architecture/hook_surface_contract.md#impl-025) Cross-version hook surface contract and registry for v2/v3/v4 extension points.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-018

## References / Source Fragments

- `docs/processed/legacy_tree/docs/claims/claim_index.md`
