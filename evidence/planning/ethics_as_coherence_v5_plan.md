---
closure_plan:
  id: ethics_as_coherence_v5
  generation: v5
  title: "Ethics-as-coherence + failure-mode taxonomy + moral-residue / guilt-repair cluster (V5 SOCIAL roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-12
  scope_claims: [ARC-056, MECH-164, MECH-145, MECH-146, ARC-086, MECH-367, MECH-371, INV-067, INV-068, INV-069, INV-070, INV-071, INV-072, ARC-054]
  sibling_plans: [relational_harm_moral_semantics_v5, mirror_modelling, self_model_v4, object_representation_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. This is the V5 (SOCIAL mind) tier of the
    3-tier partition: V4 = individual mind (object permanence + self-model;
    already seeded), V5 = social, V6 = linguistic. The spine is
    ARC-059 / DEV-NEED-021: self -> objects -> OTHERS -> language. Ethics-as-
    coherence is the SHARED-temporal-depth objective over self AND represented
    others; it cannot be honest before there are stable represented others to
    extend D_V over, which is itself gated on object permanence (V4) + a stable
    self (V4) + the multi-agent substrate (V5). So every node carries
    owner_exq: null and the drift checker stays dormant. The value here is the
    readiness_gate per node -- the V3-completion items (esp. MECH-163 multi-step
    hippocampal planning, the V4-social entry gate) AND the V4-tier prerequisites
    (object permanence, self-model) AND the upstream V5 social substrate
    (relational_harm_moral_semantics_v5 + mirror_modelling) that must land before
    each ethics step is buildable. generation: v5 keeps these nodes OUT of the V3
    closure percentage (serve.py read_closure, generate_closure_snapshot.py and
    check_closure_drift.py are all generation-aware). A node graduates from
    roadmap to closure-tracked by gaining an owner_exq once its first V5
    experiment is queued.
  nodes:
    - id: "ethics_as_coherence_v5:ETH-1"
      title: "Multi-agent D_V substrate: extend temporal-depth coherence optimisation over self AND represented others (ARC-056 entry)"
      phase: 1
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-6, SENT-9]
        requires_welfare_review: false
        note: "Extends temporal-depth coherence optimisation over represented others; social-entry node."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-056]
      depends_on: []
      cross_plan_link: ["mirror_modelling", "relational_harm_moral_semantics_v5", "object_representation_v4:OBJ-5"]
      blocking_on: "ARC-056's J_ethical(pi) = beta_self*D_V_self + sum_j beta_j*D_V_j requires a per-agent D_{V,j} term, which needs a per-agent representation (others-as-object, object_representation_v4:OBJ-5 / ARC-083) that does not exist in V3. Gated additionally on MECH-163 multi-step hippocampal planning (V4-social entry gate) and on the mirror-modelling other-terrain readout."
      readiness_gate:
        - "V3/V4 PREREQUISITE (DEV-NEED-021): otherness inference REQUIRES object persistence (object_representation_v4:OBJ-2) + a stable self (object_representation_v4:OBJ-3 / self_model_v4); a beta_j-weighted other has no referent until a per-agent token-keyed slot exists (object_representation_v4:OBJ-5 / ARC-083)"
        - "MECH-163 multi-step hippocampal planning PASS -- the V3-completion item that is the shared V4-social entry gate; the D_V rollout over another agent's trajectory presupposes a working multi-step rollout"
        - "V3 BEGINNING present: ARC-054 (D_V trajectory selection) was promoted v4->v3 2026-04-26 in rollout-horizon synaptic-EMA form and computes D_V_pi(t+k) for SELF; ARC-056 is the multi-agent generalisation of that single-agent V3 form"
        - "The beta_j weighting law depends on inferred similarity (INV-028), relational commitment (INV-029) and responsibility structure (INV-042) -- the relational substrate owned by relational_harm_moral_semantics_v5 + mirror_modelling"
      last_updated: 2026-06-10
      completion_note: "ARC-056 is the V4/V5 multi-agent form of ARC-054 (which has a live V3 single-agent form). It is intrinsically social: the ethical objective is shared temporal-depth coherence across self + represented others. Flagged v4->v5 (see generation_flags). No substrate today; this node tracks the multi-agent D_V cutover once the per-agent slot + MECH-163 land."
    - id: "ethics_as_coherence_v5:ETH-2"
      title: "Typed causal-attribution ontology: ownership tags for self / world / body / model / commitment / OTHER / shared / accidental / repairable outcomes"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-096"]
      depends_on: ["ethics_as_coherence_v5:ETH-1"]
      cross_plan_link: ["self_model_v4", "relational_harm_moral_semantics_v5"]
      blocking_on: "The OTHER / shared ownership classes require a represented other (ETH-1 / ARC-083); the self / commitment classes require the V4 self-model (self_model_v4). The typed ontology is the precondition for guilt-repair (ETH-3): repair requires causal ownership tags, not merely harm detection."
      readiness_gate:
        - "V3/V4 BEGINNING present: ARC-015 (self-impact attribution + responsibility flow, provisional) and SD-003 (self-attribution / counterfactual harm, superseded-by MECH-256/SD-029) supply the 'this harm is mine' signal; the typed 8+-class ontology is the NEW refinement layered on top"
        - "SELF/COMMITMENT tags need the self_model_v4 stateful self-model (self-attribution comparator topology, self_model_v4:SELF-2) so a 'mine' tag binds to a stable subject"
        - "OTHER/SHARED tags need a per-agent slot (ARC-083) + the mirror-modelling other-terrain readout; an other-caused or jointly-caused outcome is untaggable without a represented other"
        - "Biology rule (feedback_biology_before_formal_definitions): a typed-causal-attribution lit anchor should precede registration (ETH-8)"
      last_updated: 2026-06-10
      completion_note: "Stub ARC-TBD-ATTRIBUTION-ONTOLOGY from the 2026-05-31 V4-musings cluster (docs/thoughts/2026-05-31_musings_on_V4.md; intake evidence/planning/thought_intake_2026-05-31_musings_on_v4.md). NOT yet registered (TBD id). The intake calls it the head of the dependency chain ATTRIBUTION-ONTOLOGY -> GUILT-REPAIR -> {REPAIR-SEARCH, RESIDUE-RELEASE}. Proposed here as a v5 NEWCLAIM (the OTHER/SHARED ownership classes are intrinsically social, hence v5 not v4). Orchestrator assigns the real ARC id."
    - id: "ethics_as_coherence_v5:ETH-3"
      title: "Guilt-as-repair routing: self-attributed harm opens repair-search + policy-update pathways (E3 repair-trajectory generation) and releases residue on completion"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9, SENT-12, SENT-13]
        requires_welfare_review: false
        forbidden_combinations: [relational_harm_without_repair_channel]
        note: "Self-attributed-harm + residue; the guilt-as-repair pathway is itself the required scaffold (repair, not punishment)."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-097", "MECH-411", "MECH-412"]
      depends_on: ["ethics_as_coherence_v5:ETH-2"]
      cross_plan_link: ["relational_harm_moral_semantics_v5"]
      blocking_on: "Guilt routed to repair requires (a) a typed ownership tag (ETH-2) to know harm is self-attributed, and (b) a represented other to repair toward (ETH-1). E3 repair-trajectory generation extends the V3 E3 trajectory-scoring machinery but needs the attribution tag to seed the repair target."
      readiness_gate:
        - "V3 BEGINNING present: the moral-residue cluster (MECH-056 et al.) already RECORDS residue; the NEW pieces are (i) E3 generating repair trajectories vs avoidance/concealment/goal-continuation, and (ii) repair-completion-or-impossibility converting active guilt residue into bounded historical memory"
        - "Depends on ETH-2 typed ownership tags (a repair target requires knowing what is owned and to whom)"
        - "PRECISION GUARDRAIL (feedback_psychosis_confabulation_distinction): keep guilt (reparative) distinct from shame (global self-negation, ETH-4) and from confabulation/psychosis; the six-stub decomposition already respects this -- preserve it"
        - "Repair toward an other is social: the repair target is another agent's D_{V,j}, owned by relational_harm_moral_semantics_v5"
      last_updated: 2026-06-10
      completion_note: "Three stubs from the 2026-05-31 cluster: ARC-TBD-GUILT-REPAIR (architectural_commitment), MECH-TBD-REPAIR-SEARCH (e3.repair_trajectory_generation), MECH-TBD-RESIDUE-RELEASE (residue.repair_completion_release). NOT yet registered. Grouped here because they form one mechanism: ownership -> repair-search -> residue release. The intake's central move is 'ownership of harm WITHOUT shame-collapse' -- guilt gets an action outlet so it does not perseverate. Proposed as v5 NEWCLAIMs; orchestrator assigns real ARC/MECH ids."
    - id: "ethics_as_coherence_v5:ETH-4"
      title: "Anti-shame safety invariants: no-global-self-condemnation write + containment-not-shame autonomy suspension"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: high
        applicable_ethics_gates: [SENT-9, SENT-13]
        requires_welfare_review: false
        note: "Anti-shame safety invariant: no global-self-condemnation write, containment-not-shame. A required guardrail before any correction/harm node."
      severity: high
      owner_exq: null
      unblocks_claims: ["INV-081", "ARC-098"]
      depends_on: ["ethics_as_coherence_v5:ETH-2"]
      cross_plan_link: ["self_model_v4"]
      blocking_on: "The no-global-self-badness invariant constrains WRITES to the self-model, so it needs the self_model_v4 stateful self-model to constrain; it is meaningless against a V3 EMA body-state latent. Containment-not-shame needs a self-state-detection + autonomy-suspension surface that presupposes the same self-model."
      readiness_gate:
        - "Self-attributed harm must bind to actions / commitments / predictions / repair obligations (ETH-3), NOT to unbounded negative self-worth -- so this invariant is the safety pair to the guilt-repair mechanism, gated on the same ETH-2 tags"
        - "Constrains writes to the self-model: requires self_model_v4 (z_self promoted from body-state latent to a stateful self-model) before there is a self-worth quantity to bound"
        - "Containment-not-shame: dangerous self-state detection MAY suspend autonomy but must preserve evidence + seek correction; this is the 'nuclear safety option as containment, not shame' framing -- extends existing safety/containment concepts"
        - "Optional lit-pull before registration (guilt-as-reparative-motivation vs shame-as-withdrawal; ETH-8) -- the intake explicitly flags these two as the safety invariants warranting grounding first"
      last_updated: 2026-06-10
      completion_note: "Two stubs from the 2026-05-31 cluster: INV-TBD-NO-GLOBAL-SELF-CONDEMNATION (self_model.no_global_self_badness_write) and ARC-TBD-CONTAINMENT-NOT-SHAME (safety.autonomy_suspension_without_shame). NOT yet registered. The intake names these the paired safety invariants and flags them as high-value (anti-shame-collapse, anti-concealment, anti-defensive-distortion). Clinically load-bearing -- keep guilt/shame/self-condemnation as distinct mechanisms. Proposed as v5 NEWCLAIMs."
    - id: "ethics_as_coherence_v5:ETH-5"
      title: "Love as agent-indexed terrain inference: infer another agent's goal/harm gradients and weight them with self-equal motivational force in E3 (MECH-164)"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-6, SENT-9]
        requires_welfare_review: false
        note: "Love as agent-indexed terrain inference (MECH-164): other goal/harm gradients weighted with self-equal force; other-directed."
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-164]
      depends_on: ["ethics_as_coherence_v5:ETH-1"]
      cross_plan_link: ["mirror_modelling", "object_representation_v4:OBJ-5"]
      blocking_on: "MECH-164 requires the hippocampal terrain to be instantiable from ANOTHER agent's perspective (their goal/harm gradients) -- an other-indexed terrain readout that needs the mirror-modelling substrate + a per-agent slot (ARC-083). Depends on MECH-163 (already in MECH-164 depends_on) and SD-011 dual nociceptive streams (V3-live)."
      readiness_gate:
        - "V3 BEGINNING present: INV-005 (harm to others via mirror modelling) is the negative-side precursor and SD-011 (dual nociceptive streams) is V3-live (provisional 2026-04-18); MECH-164 generalises INV-005 to the FULL terrain -- harm gradient AND goal gradient -- with explicit other-indexing"
        - "MECH-163 multi-step hippocampal planning (already in MECH-164 depends_on; V4-social entry gate) + ARC-007 hippocampal rollout substrate"
        - "Other-indexed terrain instantiation is the mirror_modelling substrate; self-like gradient weighting (structural symmetry, not a discounted proxy) is the positive complement to ETH-1's beta_j weighting"
        - "This is the POSITIVE ethics half (care emerges from ordinary E3 selection, no separate ethics module, consistent with INV-001/ARC-012); ETH-1's D_V optimisation is the objective, MECH-164 is how care enters the gradient"
      last_updated: 2026-06-10
      completion_note: "MECH-164 (love.agent_indexed_terrain_inference) is implementation_phase: v4 in claims.yaml but is intrinsically social/relational -- care for OTHERS via inferring and self-equally weighting their terrain. Flagged v4->v5 (see generation_flags). It is the mechanistic instantiation of Axiom V (love) and the positive counterpart to the INV-072 violence corollary. No substrate today; this node tracks the love-as-care cutover once mirror-modelling + the per-agent slot land."
    - id: "ethics_as_coherence_v5:ETH-6"
      title: "Prescriptive + diagnostic ethical-trajectory certification: CBF forward-invariance + backward-reachability barrier certificates (MECH-145 / MECH-146)"
      phase: 4
      status: blocked
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-145, MECH-146]
      depends_on: ["ethics_as_coherence_v5:ETH-1", "ethics_as_coherence_v5:ETH-5"]
      cross_plan_link: []
      blocking_on: "Both certificates require a formally-specified ethical constraint set (the ARC-056 D_V attractor) + validated potential-game structure (Q-023) + MECH-127 counterfactual characterisation -- none available before the multi-agent D_V substrate (ETH-1) exists and the ethics objective is differentiable. MECH-146 additionally depends_on MECH-145."
      readiness_gate:
        - "MECH-145 (prescriptive CBF certificate, already implementation_phase: v5) needs (1) the REE ethical constraint set as an implicit surface h(x)=0, (2) differentiable dynamics for CBF gradient, (3) validated potential-game structure (Q-023) -- all downstream of ETH-1's multi-agent D_V"
        - "MECH-146 (diagnostic backward-reachability, already implementation_phase: v5) is the structurally-distinct verification tool for MECH-127's counterfactual 'could this trajectory have caused more harm under an alternative policy?'; the two certificate types are NOT interchangeable"
        - "Sequenced last among the mechanism nodes: certification presupposes a working, differentiable ethics objective (ETH-1 + ETH-5); this is the formal-guarantee capstone, not an entry step"
      last_updated: 2026-06-10
      completion_note: "MECH-145 / MECH-146 are already implementation_phase: v5 in claims.yaml -- no reassignment flag needed. They are the prescriptive (forward-invariance, will-stay-ethical) and diagnostic (backward-reachability, was-counterfactually-ethical) halves of formal ethical certification. Registered 2026-03-29 from the Q-024 lit-pull. This node tracks them as the V5 formal-guarantee layer over the ETH-1 ethics objective."
    - id: "ethics_as_coherence_v5:ETH-7"
      title: "Two-axis failure-mode taxonomy: named failure modes x cross-cutting vulnerability axes, with the depressive-regime vector and the global-instability (p-factor) axis"
      phase: 4
      status: deferred
      ethical_metadata:
        welfare_relevance: hard_review
        applicable_ethics_gates: [SENT-2, SENT-9, SENT-13]
        requires_welfare_review: true
        forbidden_combinations: [suffering_like_accumulator_without_boundedness]
        note: "Models depressive-regime / global-instability (p-factor) distress-like states; explicit welfare review before instantiating these regimes."
      severity: medium
      owner_exq: null
      unblocks_claims: [ARC-086, MECH-367, MECH-371]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "ARC-086 (two-axis index) is epistemic_category substrate_conditional / implementation_phase v4 (version_relevance v4_v5): the documentation INDEXING can begin now, but the syndrome-as-weighted-axis-vector READ-OUT (Q-064) has no substrate in V3/V4"
        - "MECH-367 (depressive failure mode as multi-axis vector) is substrate_conditional / v4: each axis exists piecemeal in V3 (INV-034 goal-coupling, MECH-124 residue/rumination, Q-021 anhedonia, MECH-082/086 future-trajectory access) but the JOINT-vector readout + a named large-scale-network-coupling substrate are not built"
        - "MECH-371 (global-instability / p-factor axis) is substrate_conditional / v4: REE has the control plane (ARC-005 + MECH-251 precision family) but no measurable global control-plane-stability scalar; a Caspi-Moffitt p-factor lit-pull (ETH-8) would sharpen it before promotion"
        - "The taxonomy spans BOTH individual axes (precision, commitment, provenance, residue) AND social axes (self-other coupling, social-contagion / cross-agent coupling); the social axes are the part that lives naturally in V5; the index as a whole is documentation-first and off the V3/GAP-7 critical path"
      last_updated: 2026-06-10
      completion_note: "ARC-086 / MECH-367 / MECH-371 are all substrate_conditional and version_relevance v4_v5; they are the clinical/diagnostic READ-OUT side of ethics-as-coherence (a failure-mode taxonomy is the inverse map of the coherence objective). Status deferred (not blocked) because the documentation-indexing layer can proceed independently of the substrate; only the vector READ-OUT is gated. NOT flagged v4->v5 in generation_flags: the taxonomy is primarily an individual-mind failure index that merely INCLUDES social axes, not an intrinsically social/relational/ethical claim. PRECISION GUARDRAIL: the axis layer is an INDEXING layer, never a merging layer -- psychosis / confabulation / derealization / OCD / depressive attractor / catatonia stay mechanistically distinct."
    - id: "ethics_as_coherence_v5:ETH-8"
      title: "Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-factor lit-pulls"
      phase: 2
      status: closed
      severity: medium
      owner_exq: null
      unblocks_claims: ["ARC-097", "INV-081", MECH-371]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "L1 guilt-vs-shame (guilt-as-reparative-motivation vs shame-as-withdrawal/concealment) -- the intake explicitly flags this lit-pull as optional-but-warranted BEFORE registering the two safety invariants (ETH-4)"
        - "L2 moral-repair / restitution literature -- grounds the repair-search + residue-release mechanism (ETH-3)"
        - "L3 typed causal-attribution / theory-of-causal-ownership -- grounds the attribution ontology (ETH-2) per feedback_biology_before_formal_definitions"
        - "L4 general-psychopathology / p-factor (Caspi & Moffitt) -- the intake/claim notes flag this to sharpen MECH-371 before any promotion"
      last_updated: 2026-06-12
      governance_2026_06_12: >
        Biology-grounding debt DISCHARGED via /lit-pull (IGW-20260612-054). Five literature_evidence/v1
        entries filed under evidence/literature/ across all four sub-pulls (all evidence_direction=supports):
        targeted_review_guilt_repair_moral_emotion/ holds (L1) Tangney, Stuewig & Mashek 2007 Annu Rev Psychol
        (guilt=bad-act/approach-repair vs shame=bad-self/withdrawal; conf 0.82; -> INV-081 + ARC-097),
        (L2) de Hooge, Zeelenberg & Breugelmans 2007 Cognition & Emotion (induced guilt selects reparative/
        prosocial action toward the victim, regulated by repair-completion; conf 0.74; -> ARC-097 + MECH-411),
        (L3) Weiner 1985 Psychological Review (typed causal attribution -- locus/controllability -- selects the
        moral emotion; controllable-internal -> guilt, uncontrollable-global -> shame; conf 0.70; -> ARC-096 +
        ARC-097), and the biology anchor Piretti et al. 2023 Brain Sciences voxel-based meta-analysis (34 fMRI
        studies; dissociable signatures -- guilt=left TPJ/social-cognition, shame=dACC social-pain + premotor
        behavioural-inhibition; conf 0.70; -> INV-081 + ARC-097). targeted_review_mech_371/ holds (L4) Caspi
        et al. 2014 Clin Psychol Sci the p factor (single transdiagnostic general-psychopathology dimension,
        Dunedin 20yr cohort; conf 0.72; -> MECH-371). Index rebuilt: literature_confidence now ARC-097=0.87,
        INV-081=0.78, MECH-371=0.71, ARC-096=0.70 (was 0 for all). This discharges the
        feedback_biology_before_formal_definitions grounding debt for the guilt-repair cluster + the p-factor
        axis; it does NOT promote any claim -- ARC-096/097, INV-081 and MECH-371 stay candidate /
        substrate_conditional / v3_pending, gated on the unbuilt V4/V5 self-model + social substrate. The L3
        Weiner anchor flags the controllability/responsibility entanglement (ownership tags less orthogonal
        than a formal ontology assumes) and the L4 anchor flags that the p factor grounds the AXIS/loading
        premise but NOT MECH-371's control-plane (ARC-005) mechanistic identification -- both carried as
        explicit mapping_caveats / failure_signatures for the eventual promotion review.
      completion_note: "Per project rule feedback_biology_before_formal_definitions: the guilt-repair cluster and the p-factor axis are formal/clinical constructs that need a biology lit-pull before registration. This node tracked closing that grounding debt. CLOSED 2026-06-12 -- all four sub-pulls (L1 guilt-vs-shame, L2 moral-repair, L3 typed-causal-attribution, L4 p-factor) filed (see governance_2026_06_12). The pull discharges the grounding debt only; the grounded claims remain unpromotable on substrate grounds (ETH-2/3/4 readiness gates unchanged)."
---
# Ethics-as-Coherence + Failure-Mode Taxonomy + Moral-Residue / Guilt-Repair -- V5 SOCIAL Roadmap

**Registered:** 2026-06-10
**Generation:** v5 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the V5 SOCIAL-tier ethics work -- (1) the multi-agent
temporal-depth-coherence objective (ethics-as-coherence, ARC-056), (2) the
typed causal-attribution ontology, (3) the guilt-as-repair / repair-search /
residue-release cluster with its (4) anti-shame safety invariants, (5) love as
agent-indexed terrain inference (MECH-164), (6) the prescriptive + diagnostic
ethical-certification mechanisms (MECH-145/146), (7) the two-axis failure-mode
taxonomy (ARC-086 + MECH-367 + MECH-371) as the diagnostic inverse-map, and
(8) the biology grounding debt -- so V5 substrate work slots in against a
registered spine instead of accreting ethics as a bolt-on module.

This is a **V5 (SOCIAL mind)** plan in the 3-tier partition: V4 = individual
mind (object permanence + self-model; already seeded), V5 = social, V6 =
linguistic. The spine is **ARC-059 / DEV-NEED-021: self -> objects -> OTHERS ->
language.** Ethics-as-coherence is the shared-temporal-depth objective over
self AND represented others; otherness inference REQUIRES object-permanence +
a stable self, both V4. It is a *forward roadmap*, not a closure map: V5 has no
experiments yet, so nodes carry no `owner_exq` and the drift checker stays
dormant. The value here is the **readiness gates** -- for each ethics step,
exactly which V3-completion items, V4-tier prerequisites, and upstream V5
social substrate must land first.

---

## One-line framing

> Ethics already EXISTS in REE as invariants (INV-067..072 the V(t)/D_V/violence
> system; INV-005/028/029 the mirror/similarity/love substrate) and has a live
> V3 SINGLE-AGENT coherence form (ARC-054 D_V trajectory selection). What is NOT
> done is the SOCIAL cutover: extending D_V over represented OTHERS (ARC-056),
> giving harm a typed causal owner (attribution ontology), routing self-owned
> harm to REPAIR rather than shame (guilt-repair cluster), making care emergent
> from other-indexed terrain weighting (MECH-164), certifying the resulting
> trajectories formally (MECH-145/146), and reading the failure space back out
> as a two-axis taxonomy (ARC-086). Every one of those presupposes a represented
> other -- which DEV-NEED-021 gates behind object permanence + a stable self
> (V4) and MECH-163 multi-step planning (the V4-social entry gate).

---

## The ethics cutover sequence (mapped to nodes)

| Step | Node | Claim(s) | Phase leaning | The readiness gate |
|---|---|---|---|---|
| multi-agent D_V objective | ETH-1 | ARC-056 | V5 (entry) | MECH-163 + per-agent slot (ARC-083) + mirror-modelling |
| typed attribution ontology | ETH-2 | NEWCLAIM (attribution) | V5 | ETH-1; self-model (self/commitment tags); other-slot (other/shared tags) |
| guilt -> repair-search -> release | ETH-3 | 3x NEWCLAIM | V5 | ETH-2 tags; moral-residue cluster live; repair-target = other's D_{V,j} |
| anti-shame safety invariants | ETH-4 | 2x NEWCLAIM | V5 | ETH-2/ETH-3; self-model to bound self-worth write |
| love as terrain inference | ETH-5 | MECH-164 | V5 | mirror-modelling + per-agent slot; MECH-163; SD-011 live |
| prescriptive + diagnostic certs | ETH-6 | MECH-145, MECH-146 | V5 (already) | differentiable ETH-1 objective; Q-023 potential game; MECH-127 |
| two-axis failure taxonomy | ETH-7 | ARC-086, MECH-367, MECH-371 | V4/V5 (doc-first) | vector READ-OUT substrate (Q-064); p-factor lit-pull |
| biology grounding debt | ETH-8 | grounds ETH-2/3/4 + MECH-371 | cross-cutting | guilt-vs-shame, moral-repair, attribution, p-factor pulls |

---

## How this plan relates to its siblings

- **`relational_harm_moral_semantics_v5`** -- supplies the relational substrate
  (similarity inference INV-028, relational commitment INV-029, responsibility
  INV-042) that the ETH-1 beta_j weighting law and the ETH-3 repair-target read.
  Harm-to-an-other semantics live there; ethics-as-coherence consumes them.
- **`mirror_modelling`** -- supplies the other-indexed terrain readout (ARC-010
  mirror modelling + coupling) that ETH-1 (other D_{V,j}) and ETH-5 (MECH-164
  other-terrain instantiation) both depend on. A represented other's gradients
  come from the mirror substrate.
- **`object_representation_v4` (OBJ-5 / ARC-083)** -- supplies the per-agent
  token-keyed object-file slot that is the referent of every beta_j-weighted
  other; without it there is no "other" to extend D_V over.
- **`self_model_v4`** -- supplies the stateful self-model that the attribution
  ontology binds SELF/COMMITMENT tags to (ETH-2) and that the
  no-global-self-condemnation invariant constrains writes to (ETH-4).

---

## What this plan deliberately does NOT pull earlier

- **No V3 substrate code, no experiments, no claim promotions.** Registering
  this roadmap changes no V3 (or V4) behaviour. The ethics invariants stay as
  invariants; ARC-054 stays the live V3 single-agent D_V form; the moral-residue
  cluster keeps recording residue without the repair-search / release extension.
- **ARC-056 is NOT pulled into V4.** It is the multi-agent generalisation of the
  V3 single-agent ARC-054 and is honest only once a represented other exists. It
  is flagged v4->v5, not advanced.
- **The taxonomy (ETH-7) documentation can proceed; its vector READ-OUT cannot.**
  ARC-086's two-axis index is documentation-first and off the critical path; only
  the syndrome-as-weighted-vector substrate (Q-064) is gated to V4/V5.
- **No new claims registered here.** The guilt-repair cluster (six 2026-05-31
  stubs) is proposed as v5 NEWCLAIMs for the orchestrator to register, NOT
  written into claims.yaml by this plan. Already-owned claims (ARC-056, MECH-164,
  MECH-145/146, ARC-086/MECH-367/MECH-371, the INV-067..072 ethics block) are
  cited as scope, not duplicated.

---

## The 2026-05-31 guilt-repair cluster (six stubs -> proposed_claims)

The cluster is internally coherent and already drafted in registry YAML shape in
`docs/thoughts/2026-05-31_musings_on_V4.md` (intake:
`evidence/planning/thought_intake_2026-05-31_musings_on_v4.md`). It was
deliberately NOT registered (TBD ids) and was intended for V4; this plan
proposes it at **V5** because the OTHER/SHARED attribution classes and the
repair-toward-an-other target are intrinsically social. The dependency chain:

> ATTRIBUTION-ONTOLOGY (ETH-2) -> GUILT-REPAIR (ETH-3) -> {REPAIR-SEARCH,
> RESIDUE-RELEASE} (ETH-3); with NO-GLOBAL-SELF-CONDEMNATION + CONTAINMENT-NOT-
> SHAME (ETH-4) as the paired safety invariants.

Anchors: ARC-015 (self-impact attribution), SD-003 (self-attribution /
counterfactual harm), the moral-residue cluster (MECH-056 et al.).

---

## Source artefacts

| Artefact | Role |
|---|---|
| claims.yaml ARC-056 | ethics-as-coherence: J_ethical = beta_self*D_V_self + sum_j beta_j*D_V_j (multi-agent; `implementation_phase: v4`) |
| claims.yaml MECH-164 | love as agent-indexed terrain inference (`implementation_phase: v4`) |
| claims.yaml MECH-145 / MECH-146 | prescriptive CBF + diagnostic backward-reachability ethical certs (`implementation_phase: v5`) |
| claims.yaml ARC-086 / MECH-367 / MECH-371 | two-axis failure-mode taxonomy + depressive-regime vector + p-factor axis (substrate_conditional, v4_v5) |
| claims.yaml INV-067..072 | V(t) / D_V / self / epistemic-responsibility / language-as-similarity-repair / violence-corollary ethics block |
| claims.yaml ARC-054 | the V3-live single-agent D_V trajectory-selection form ARC-056 generalises |
| docs/thoughts/2026-05-31_musings_on_V4.md | the six guilt-repair stubs (TBD ids; not registered) |
| evidence/planning/thought_intake_2026-05-31_musings_on_v4.md | structured intake of the guilt-repair cluster |
| docs/architecture/developmental_needs_register.md DEV-NEED-021 | otherness inference requires object permanence + self-stability |

---

## Decision log

- **2026-06-10** -- Plan registered as a V5 SOCIAL forward-roadmap, sibling to
  `relational_harm_moral_semantics_v5`, `mirror_modelling`, `self_model_v4`,
  `object_representation_v4`. Eight nodes: ETH-1 (multi-agent D_V / ARC-056),
  ETH-2 (attribution ontology), ETH-3 (guilt-repair / repair-search / residue-
  release), ETH-4 (anti-shame safety invariants), ETH-5 (love-as-terrain /
  MECH-164), ETH-6 (CBF + backward-reachability certs / MECH-145/146), ETH-7
  (two-axis failure taxonomy / ARC-086 + MECH-367 + MECH-371), ETH-8 (biology
  grounding debt). Readiness gates pinned per node. `generation: v5` set so the
  V3 closure % is unaffected. No claims.yaml edits.
- **2026-06-10** -- Reassignment flags raised: ARC-056 (ethics-as-coherence,
  intrinsically multi-agent) and MECH-164 (love as care-for-others via terrain
  inference) are `implementation_phase: v4` in claims.yaml but belong in the V5
  SOCIAL tier; flagged v4->v5. MECH-163 deliberately NOT flagged (it is the V3
  completion gate -- stays v3). MECH-145/146 already v5 -- no flag. ARC-086 /
  MECH-367 / MECH-371 NOT flagged -- they are primarily individual-mind failure
  indices that include social axes, not intrinsically social/relational claims.
- **2026-06-10** -- Six guilt-repair stubs proposed as v5 NEWCLAIMs (placeholders
  attribution_typed_causal_ontology, ethics_guilt_like_repair_routing,
  e3_repair_trajectory_generation, residue_repair_completion_release,
  self_model_no_global_self_badness_write, safety_autonomy_suspension_without_shame).
  Proposed at V5 (not the intake's original V4) because the OTHER/SHARED
  attribution classes and the repair-toward-an-other target are intrinsically
  social. Orchestrator assigns real ids + wires depends_on.
