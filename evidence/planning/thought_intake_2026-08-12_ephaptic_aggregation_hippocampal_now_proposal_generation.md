# Thought Intake: Ephaptic Aggregation, Hippocampal Proposal Generation, and the Construction of "Now"

**Date:** 2026-08-25
**Raw thought file:** `docs/thoughts/2026-08-12_ephaptic_aggregation_hippocampal_now_proposal_generation.md`
**Companion raw thought (context only, not processed by this intake):**
`docs/thoughts/2026-08-12_affordance_indexed_temporally_displaced_present.md`
**Session:** mech-266-rescore-circling-2d31ca (worktree), 2026-08-25

## Verbatim prompt (core proposal)

> Ephaptic coupling may provide a very fast physical mechanism for aggregating information
> carried in distributed oscillatory activity. The resulting field-level state may help provide
> hippocampal generative machinery with a rapidly updated estimate of the organism's actionable
> "now," from which prospective proposals can be generated.

> Proposals need to come from "now" quickly.

The thought proposes a candidate biological mechanism for rapidly constructing the state from
which the companion thought's affordance-indexed, temporally-displaced present is generated: (a)
ephaptic coupling (non-synaptic influence via the extracellular electric field a neural
population itself generates) as a fast, physical, sub-cycle aggregation mechanism across
distributed oscillatory activity; (b) the aggregate should be read as temporally-structured
population information (amplitude, phase, relative phase, frequency, synchrony, coherence,
cross-frequency relationships), not a single scalar; (c) hippocampal generative machinery
(theta-sequence prospective sweeps, goal-dependent branching) reads this aggregate as its
anchor/starting-state for proposing candidate futures; (d) basal-ganglia-like machinery does
NOT receive the aggregate directly -- its role is constitutional, governing which proposal wins
authority (content authority); (e) a distinct question is WHEN a candidate future has become
sufficiently coherent for commitment to be permitted at all (temporal/readiness authority), and
the same fast coherence process may locate that moving frontier; (f) major prediction violation
should rapidly reorganise the coherence structure and reopen hippocampal branching.

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage | Verdict |
|---|---|---|
| Ephaptic coupling as a fast, non-synaptic, field-level coherence-support mechanism generally | **MECH-228** (`architecture.ephaptic_coupling_coherence`, candidate/v4): "extracellular electric field interactions stabilise phase relationships across neural populations, supporting temporal coherence." | Already owned at the general architectural level. Cross-ref only. |
| Ephaptic coupling specifically in hippocampal CA1/CA3, as the physical substrate for a fast readout that feeds hippocampal proposer machinery | **MECH-270** (`hippocampus.ephaptic_verisimilitude_readout`, candidate/v3_pending): ephaptic field coherence in CA1/CA3 as the candidate substrate for the per-stream verisimilitude `V_s` readout that **MECH-269** anchor selection operates over -- streams whose predictions align produce coherent fields; "anchor-eligible" reduces to "field-coherent at read time." | Already owned, but scoped narrowly to a **confidence/eligibility readout** (is stream `s` trustworthy right now), explicitly NOT content aggregation -- MECH-270's own notes state "`V_s` can be computed directly from per-stream prediction/realization alignment... MECH-270 is the biological-grounding claim, not an implementation requirement." Cross-ref, not re-asserted; see MECH-499 below for what remains open. |
| Hippocampus as generator of candidate/prospective trajectories ("hypothesis injector") for downstream evaluation | **MECH-022** (`hippocampal.hypothesis_injection`, provisional/substrate_conditional) and **ARC-018** (`hippocampus.rollout_viability_mapping`, provisional): hippocampal systems inject hypotheses / generate explicit rollouts from the current latent state, gated by control plane. | Already owned. Cross-ref only, not re-asserted. |
| Trigger for WHEN hippocampal proposal generation should fire more/less densely (novelty-gated) | **MECH-149** (`hippocampus.ca1_mismatch_novelty_gate`, candidate/v4): CA1 mismatch between E1-predicted and CA3-retrieved `z_world` gates trajectory-injection frequency/diversity. | Already owned for the *novelty-gates-rate* axis. Distinct from this thought's *field-aggregate-supplies-the-state-itself* axis -- cross-ref only. |
| Hippocampal theta sequences representing prospective/goal-dependent trajectories extending ahead of current position (the literature review section) | Multiple existing claims already carry this literature: the theta-sequence traversal claim at `multirate`/`hippocampal` subjects (theta implements sequential traversal unifying hippocampal theta sequences, working memory, planning, retrieval), the developmental theta/SWR co-emergence claim, and the alternative-encoding theta-sequence claim (Tang/Shin/Jadhav prospective-choice-at-decision-points literature already cited verbatim in the registry). | Already owned; the specific citations the raw thought gestures at (prospective theta sweeps, goal-dependence, hippocampal-PFC synchrony) are already the evidentiary basis of existing claims. Not re-asserted. |
| Cross-frequency / oscillatory multiplexing as the general mechanism by which shared substrate carries multiple simultaneous streams (perception / imagination / action-commitment) | **MECH-089** (theta-cycle batching of E1 for E3) and **MECH-225** (`perception.oscillatory_multiplexing`, substrate_conditional): gamma/theta/beta/delta phase-channel separation of perception/simulation/action streams; MECH-228 explicitly named there as "one physical substrate that helps enforce or bias phase separation." | Already owned. MECH-225 is about **disambiguating/separating** concurrent streams by phase; this thought's core claim is about **aggregating/fusing** distributed state into one coherent estimate -- a different function on the same substrate family. Cross-ref, not duplicated. |
| Salient-event-triggered reconstruction of the "now" state / interruption reopening branching | **MECH-091** (`control_plane.salient_event_cycle_resync`, candidate/v3): salient events (completion, unexpected harm, commitment-boundary crossing) phase-reset the E3 heartbeat clock, forcing fresh-cycle integration. | Already owned for the *E3 cycle-boundary* reading. The raw thought's "interruption reopens hippocampal branching" is the same event class read through the proposal-generation side rather than the E3-update-cycle side -- close enough that it does not warrant a separate claim; folded as a cross-reference into MECH-499/500 below rather than re-asserted. |
| Beta-gated propagation of committed state to action selection | **MECH-090** (`control_plane.commitment_gated_policy_output`, active): BG-level beta gates propagation of already-decided E3 state to action selection, not E3's internal updating; R-c amendment adds a score-margin / nav-competence-based commit-**entry** readiness conjunction. | Already owned for gating an **already-decided** commit and for a **margin/competence-based** entry-readiness axis. Distinct from this thought's proposal (a **field-coherence-based** readiness signal locating the moment a branching future becomes sufficiently coherent, prior to and orthogonal to margin/competence). Cross-ref only; see MECH-500. |
| Evidence-driven "when is there enough information to commit" | **MECH-434** (`inference.epistemic_commitment_timing`, candidate/v4/substrate_conditional): inference-layer control parameter for WHEN to stop gathering evidence and commit, balancing pragmatic vs. epistemic value, with epistemic-freezing and anti-epistemic-panic failure poles. | Already owned, but scoped to **epistemic uncertainty over the belief-state hypothesis set** (evidence about the world), not to **internal cross-system field coherence** of the proposal-generating machinery itself. Related axis, explicitly distinguished -- see MECH-500's `distinct_from`. |
| "Content authority" (which candidate future wins) vs. "temporal/readiness authority" (whether a future is coherent enough for commitment to land at all) as two SEPARATE constitutional questions | No existing claim states this split explicitly. MECH-090/MECH-341/ARC-003 collectively cover content authority (BG-like selection machinery); MECH-434 covers an evidence-driven readiness axis; none names the field-coherence-based readiness axis or states the two-authority distinction as such. | **Genuinely new -> registered as MECH-500.** |
| Ephaptic/oscillatory field-level aggregation as the physical mechanism CONSTITUTING (not merely gating eligibility for) the hippocampal proposer's actionable-now starting state -- carrying structured temporal-relationship information (phase, relative phase, synchrony, cross-frequency), not a scalar confidence readout | MECH-270 explicitly disclaims this (confidence-readout only, "not an implementation requirement" for content). MECH-225 covers separation, not aggregation. No claim asserts the aggregation-for-content function. | **Genuinely new -> registered as MECH-499.** |
| "The same coherence process locates the moving frontier at which a branching future becomes sufficiently well-predicted for commitment" (readiness-authority mechanism specifically implemented via field coherence) | Covered by the MECH-500 registration above (this is MECH-500's second half, folded into one claim with the content/readiness split rather than split further -- both halves come from the same paragraph of the raw thought and do not resolve by independent experiments). | Folded into MECH-500, not double-registered. |

## Key formulations (verbatim, load-bearing)

> Ephaptic coupling may rapidly aggregate and feed back information embodied in the temporal
> relationships among distributed oscillatory systems, helping stabilise a coherent
> organism-level state from which hippocampal prospective sequences can be generated.

> The coherence of this rapidly aggregated state may help locate the moving frontier where a
> previously branching future becomes sufficiently well predicted for commitment to land.

> ephaptic/oscillatory integration helps establish the state from which proposals are generated;
> basal-ganglia-like machinery governs the proposals.

> content authority: which future should win; temporal/readiness authority: whether that future
> is sufficiently coherent for commitment to land.

## Affected existing claims

- **MECH-228** -- cross-referenced (general ephaptic-coherence substrate), not amended.
- **MECH-270** -- cross-referenced and explicitly distinguished: MECH-270 is a confidence/eligibility
  readout (per-stream `V_s` gating anchor eligibility for MECH-269); MECH-499 is a content-aggregation
  claim (the field-level aggregate constitutes the actionable-now state itself). Not a revision of
  MECH-270 -- both may be true simultaneously, and MECH-270's own notes already leave the content
  question open by disclaiming it.
- **MECH-269 / MECH-022 / MECH-149 / ARC-018** -- named as the existing hippocampal
  proposal-generation machinery this thought's aggregate would feed; not modified.
- **MECH-089 / MECH-225** -- named as the existing oscillatory-substrate family (packaging,
  multiplexing); MECH-499 is functionally distinct (aggregation vs. separation) and depends on
  MECH-089, not a revision of either.
- **MECH-090 / MECH-434** -- both named and explicitly distinguished from MECH-500's field-coherence
  readiness axis (MECH-090 gates an already-decided commit via margin/competence; MECH-434 is
  evidence/posterior-driven at the inference layer). Not amended.
- **MECH-091** -- cross-referenced for the interruption/reconstruction event class; not amended.

No existing claim's status, confidence, or evidence record was touched.

## Candidate claims -- REGISTERED this pass (not "for future registration")

Per standing practice (thought-intake registers genuinely-new ideas into `claims.yaml` in the
same pass, version-scoped, rather than leaving them as prose), the following were registered
directly:

- **MECH-499** -- `hippocampus.ephaptic_actionable_now_aggregation`. Ephaptic/oscillatory
  field-level coherence functions as a fast **content-aggregation** mechanism -- not merely the
  confidence-readout MECH-270 already covers -- synthesising distributed oscillatory information
  (phase, relative phase, synchrony, cross-frequency relationships) into the temporally-coherent
  actionable-now state that seeds hippocampal proposal generation (MECH-022/MECH-149/ARC-018).
  `status: candidate`, `epistemic_category: substrate_conditional` (set explicitly -- gated on the
  MECH-228/MECH-270 ephaptic substrate itself being unbuilt), `implementation_phase: v4`,
  `version_relevance: v4_v5`. `depends_on`: MECH-228, MECH-270, MECH-269, MECH-022, MECH-149,
  ARC-018, MECH-089.
- **MECH-500** -- `control_plane.field_coherence_commitment_readiness`. States the
  content-authority / temporal-readiness-authority distinction explicitly and proposes that fast
  cross-system field coherence (extending MECH-499's aggregate) is a candidate mechanism for the
  readiness axis -- locating the moving frontier at which a branching predicted future becomes
  sufficiently coherent for commitment to be permitted -- as a mechanism DISTINCT FROM MECH-434
  (evidence/posterior-driven epistemic commitment timing at the inference layer) and DISTINCT FROM
  MECH-090 (beta-gated propagation of an already-decided commit; margin/competence-based entry
  readiness). Same status/category/phase pattern as MECH-499. `depends_on`: MECH-499, MECH-228,
  MECH-270, MECH-090, MECH-269, MECH-434, ARC-018. `distinct_from`: MECH-434, MECH-090.

Both: `status: candidate`, `polarity: asserts`, `registered_utc: 2026-08-25`. Compass /
architectural framing only -- promote/demote and `narrow_open_question` are suppressed by the
explicit `epistemic_category: substrate_conditional`; neither claim should be read as a V3 build
authorization -- both require the MECH-228/MECH-270 ephaptic substrate itself (already v4-parked)
to exist first. Full comparison against existing machinery is in the new architecture doc
`docs/architecture/ephaptic_hippocampal_now_construction.md`.

## Next steps

1. **Literature pull, before hardening either claim further**: this thought's own biology section
   already distinguishes established ingredients (endogenous extracellular fields; fields
   influencing spike timing/synchrony under some conditions; oscillatory synchrony as
   behaviourally relevant; hippocampal theta prospective sequences; hippocampal-cortical
   coordination in planning) from the suggestive bridge and the novel integration -- a targeted
   literature pull should verify the specific field-coherence-as-content-aggregation claim
   (MECH-499) against the ephaptic-coupling literature already anchoring MECH-228/270
   (Anastassiou & Koch 2011; Fries 2015 communication-through-coherence; Buzsaki on SWRs) rather
   than assuming it transfers from the confidence-readout framing.
2. **MECH-434 vs. MECH-500 relationship**: both are V4-parked commitment-timing axes gated on
   different unbuilt substrates (belief-state inference vs. field coherence). A future V4
   scoping pass should check whether they are two independent readiness signals that should
   AND-compose (mirroring MECH-090's own R-c two-axis composition precedent) or whether one
   subsumes the other once both substrates exist -- not resolvable now, flagged for that pass.
3. **Companion thought** (`2026-08-12_affordance_indexed_temporally_displaced_present.md`) remains
   unprocessed as of this intake -- it was read for context only, per this session's instructions.
   Its own Stage 2 intake (when done) should cross-reference MECH-499/500, since the "commitment
   horizon" / "predictive tube" framing in that thought is the phenomenological frame these two
   mechanism claims propose a physical substrate for.
4. **Version-routing decision**: both registered claims are parked `v4`/`substrate_conditional` by
   default, per standing practice for thought-intake registrations. A future `/governance` cycle
   can route either onto V3 explicitly only once the MECH-228/MECH-270 ephaptic substrate itself
   has a V3 landing -- currently it does not (MECH-270 is `v3_pending` with prior diagnostic
   experiments, V3-EXQ-720/725/725a, showing the fixed-field ephaptic-analog binder does not yet
   clear its own coherence-specificity gate).
5. Raw thought file
   `docs/thoughts/2026-08-12_ephaptic_aggregation_hippocampal_now_proposal_generation.md` marked
   `Status: processed` with this intake linked, per the Stage 1/2 linking convention.
