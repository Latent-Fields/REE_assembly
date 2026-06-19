---
closure_plan:
  id: fast_empathy_v5
  generation: v5
  title: "Fast empathy as stream-binding (NOT a module)"
  registered: 2026-06-10
  last_updated: 2026-06-13
  scope_claims: [ARC-010, MECH-031, MECH-112, SD-011, MECH-183, MECH-191, MECH-359, MECH-360]
  sibling_plans: [mirror_modelling_other_self_v5, self_model_v4, object_representation_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V5 (the SOCIAL mind tier) has no
    experiments yet, so nodes carry no owner_exq and the drift checker stays
    dormant against them. Each node's readiness_gate lists the prerequisites
    that must land first -- BOTH V3-completion items (MECH-163 multi-step
    hippocampal planning, the V4-social entry gate) AND V4-tier substrate
    (object permanence, a stable self, the V4 affect-expression substrate
    MECH-359/360) -- before the V5 social step is honest to build. generation:
    v5 keeps these nodes OUT of the V3 closure percentage (serve.py
    read_closure, generate_closure_snapshot.py, and check_closure_drift.py are
    all generation-aware). The spine is ARC-059 / DEV-NEED-021: self -> objects
    -> OTHERS -> language; otherness inference REQUIRES object-permanence + a
    stable self, both V4. This plan is the empathy-specific specialisation of
    that social pillar: it asserts an ARCHITECTURAL PROHIBITION (no empathy
    module, no empathy scalar) and treats fast empathy as the binding/routing of
    already-existing motivational-affective streams across self -> object ->
    other. A node graduates from roadmap to closure-tracked by gaining an
    owner_exq once its first V5 experiment is queued.
  nodes:
    - id: "fast_empathy_v5:EMP-1"
      title: "No-empathy-scalar architectural prohibition (the load-bearing prohibition)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-094"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "No substrate prerequisite -- this is a DESIGN PROHIBITION, registrable now as the spine of the whole plan: there must be NO empathy_enabled flag and NO empathy_score scalar in any REE version"
        - "Positive form: fast empathy MUST emerge from binding/routing the basic motivational-affective streams (liking, wanting, suffering, threat, relief, frustration, curiosity, attachment/proximity, fatigue/cost, agency/control, prediction-error) across self -> object -> other; it is never a primitive of its own"
        - "Consistency check against the affect register: docs/architecture/affect_primitives.md (SD-011 dual-nociceptive; the three-primitive harm register) is the V3 seed of the stream taxonomy this prohibition extends into the social domain"
      last_updated: 2026-06-13
      completion_note: "The CENTRAL contribution of the 2026-05-04 fast-empathy intake: the prohibition is the claim. It is testable as a negative architectural commitment (any design introducing an empathy scalar violates it) and it constrains every node below. Like ARC-012 (E3 needs no explicit ethical cost term) it is an architectural_commitment about what must NOT exist. Reconciled 2026-06-13: claim ARC-094 registered in claims.yaml (candidate, substrate_conditional); the design prohibition is the deliverable and is landed, downstream binding nodes remain blocked on the V5 social substrate."
    - id: "fast_empathy_v5:EMP-2"
      title: "Open, extensible affect-stream taxonomy (handles, not a final ontology)"
      phase: 1
      status: done
      severity: medium
      owner_exq: null
      unblocks_claims: ["ARC-095"]
      depends_on: ["fast_empathy_v5:EMP-1"]
      cross_plan_link: []
      readiness_gate:
        - "V3 SEED present: affect_primitives.md already registers a three-way harm dissociation (SD-011 z_harm_s / z_harm_a) -- a partial register, not yet the ~11-stream social-extensible taxonomy"
        - "The taxonomy must permit later split / merge / rename; the stream names are HANDLES the binding layer routes, not a frozen ontology"
        - "No substrate gate -- this sharpens the existing register; it is a documentation+claim step, prerequisite to giving EMP-3/EMP-4 a stable vocabulary to bind"
      last_updated: 2026-06-13
      completion_note: "Sharpens affect_primitives.md from the V3 harm-only register to an explicitly extensible social register. Deliberately provisional: a frozen taxonomy would re-create the empathy-scalar error one level down. Cheapest node; can land alongside EMP-1 as the documentation pair. Reconciled 2026-06-13: claim ARC-095 registered in claims.yaml (candidate, substrate_conditional); the design prohibition is the deliverable and is landed, downstream binding nodes remain blocked on the V5 social substrate."
    - id: "fast_empathy_v5:EMP-3"
      title: "Stream-binding mechanism: route own motivational-affective streams across the other-model"
      phase: 2
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-6, SENT-9]
        requires_welfare_review: false
        note: "Routes own motivational-affective streams across the other-model; the substrate empathy + harm-equivalence rest on."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-405"]
      depends_on: ["fast_empathy_v5:EMP-1", "fast_empathy_v5:EMP-2"]
      cross_plan_link: ["mirror_modelling_other_self_v5", "object_representation_v4:OBJ-5"]
      blocking_on: "Requires a stable other-model (ARC-010 mirror modelling materialised as a per-agent object-file slot, object_representation_v4:OBJ-5 / ARC-083), which is gated on MECH-163 multi-step hippocampal planning (V4 social-entry gate) AND DEV-NEED-021 prerequisites (object-permanence + a stable self, both V4)."
      readiness_gate:
        - "MECH-163 multi-step hippocampal planning PASS (V3 full-completion gate; also the V4 social-entry gate) -- no other-directed planning without it"
        - "A stable other-model: ARC-010 (mirror modelling, currently active but unimplemented as an other-slot) realised via the others-as-object pillar (object_representation_v4:OBJ-5 / ARC-083); the binding layer routes self-streams into THIS slot"
        - "DEV-NEED-021: otherness inference REQUIRES object-permanence (object_representation_v4:OBJ-2) + a stable self (self_model_v4 SELF-1/SELF-3) -- both V4 -- before suffering/threat/liking can be other-bound"
        - "V3/V4 SEEDS this builds on: MECH-031 (derived social tags / empathy coupling), MECH-183 (z_beta leakage = attributed other-state activates self z_beta directly), SD-011 (the suffering stream that becomes other-bound), MECH-112 (wanting), MECH-359 (per-candidate affect vector to be routed)"
      last_updated: 2026-06-10
      completion_note: "This is the positive mechanism EMP-1 demands exist instead of a module: other-bound suffering = the SD-011 suffering stream + binding into the other-model slot; other-bound wanting = MECH-112 wanting + the same binding. MECH-183 z_beta leakage is the existing computational shape of one such binding (attribution-gated). Design-only today; gated on the social substrate."
    - id: "fast_empathy_v5:EMP-4"
      title: "Falsifiable dissociation: prediction != reciprocity-reward != residue-aware repair (A/B/C/D)"
      phase: 3
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-406"]
      depends_on: ["fast_empathy_v5:EMP-3"]
      cross_plan_link: ["mirror_modelling_other_self_v5"]
      blocking_on: "The A/B/C/D repeated-cooperation experiment needs a stable other-model substrate (EMP-3) or at minimum a scripted-partner V3/V5 proxy; do NOT queue until that substrate exists (per the 2026-05-04 intake gating note)."
      readiness_gate:
        - "EMP-3 stream-binding mechanism in place (the thing whose absence/presence the four variants dissociate)"
        - "Experiment design (from the intake): four agent variants -- A self-streams only; B other-prediction only (predicts partner cooperation, does NOT bind it into affect); C reciprocity-reward (binds partner cooperation into liking/wanting/trust); D residue-aware (C + residue from exploiting cooperators + repair-goal generation)"
        - "Predicted dissociation: B detects but under-reciprocates; C reciprocates after repeated cooperation; D additionally shows repair/regret-residue after exploitation -- directly tests other_model_prediction != reciprocity_reward != residue_aware_social_commitment"
        - "Lit anchor: Wu et al. 2026 (eLife) adolescent repeated-PD -- adolescents estimate partner cooperation as well as adults but show weaker intrinsic reward for reciprocity"
      last_updated: 2026-06-10
      completion_note: "The standout deliverable: the load-bearing dissociation from Wu et al. -- prediction alone is not ethics; the predicted other-state must become motivationally/ethically relevant to the commitment gate. The A/B/C/D variants are the first V5 experiment candidate (would gain an owner_exq once the social substrate or a scripted-partner proxy exists)."
    - id: "fast_empathy_v5:EMP-5"
      title: "Residue-aware social repair: regret-residue after exploitation generates a repair-goal"
      phase: 4
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9, SENT-12]
        requires_welfare_review: false
        forbidden_combinations: [relational_harm_without_repair_channel]
        note: "Regret-residue after exploitation generates a repair goal; the repair channel is the required scaffold."
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-407"]
      depends_on: ["fast_empathy_v5:EMP-3", "fast_empathy_v5:EMP-4"]
      cross_plan_link: ["self_model_v4"]
      blocking_on: "Repair-goal generation rides the MECH-112/MECH-359 wanting+per-candidate-affect substrate AND a self-state goal channel (self_model_v4 SELF-5 / MECH-214, z_self-domain goals); both are V4. A repair goal is a self-state goal (restore commitment coherence) directed at an other-slot."
      readiness_gate:
        - "EMP-4 variant D requires this: residue from exploiting a cooperator must persist and spawn a repair-goal (the C->D step)"
        - "Self-state goal channel (self_model_v4 SELF-5 / MECH-214 -- z_self-domain goals representable) so 'restore commitment coherence' is a representable goal, not only a world-location goal"
        - "MECH-359 per-candidate affect vector (V4 affect substrate) to carry the regret-residue as a candidate-differentiated signal; INV-029 long-horizon care-investment as the value the repair restores"
      last_updated: 2026-06-10
      completion_note: "Distinguishes genuine prosocial commitment (D) from mere reciprocity bookkeeping (C). The repair-goal is the architectural cash-out of INV-029 (love as long-horizon coherence/care-investment) at the social level: exploitation leaves residue, residue spawns a goal to repair the relationship's coherence."
    - id: "fast_empathy_v5:EMP-6"
      title: "Developmental ordering of other-bound streams: protective streams before appetitive (safety gate)"
      phase: 4
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9, SENT-13]
        requires_welfare_review: false
        note: "Developmental ordering = a SENT-13 social-assembly-routing instance: protective other-bound streams must precede appetitive ones."
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-408", "Q-073"]
      depends_on: ["fast_empathy_v5:EMP-3"]
      cross_plan_link: ["object_representation_v4:OBJ-5"]
      blocking_on: "Sequencing claim over the EMP-3 binding layer; cannot be demonstrated until multiple streams are other-bindable (EMP-3) so their ordering can be manipulated. Sits on the ARC-059 maturational spine (self -> objects -> others)."
      readiness_gate:
        - "EMP-3 stream-binding in place for MULTIPLE streams (suffering/threat AND liking/wanting) so the ordering is manipulable"
        - "Proposed ordering: other-bound suffering/threat come online BEFORE other-bound liking/wanting, because early positive other-reward is destabilising/exploitable (a safety-relevant ordering claim)"
        - "ARC-059 three-stage maturational spine (self -> objects -> others) is the ordering authority; INV-064 (maturational-sequence honesty, self_model_v4 SELF-7) forbids running social binding ahead of a stable self"
      last_updated: 2026-06-10
      completion_note: "Safety-relevant developmental ordering: an other-model that learns to want another's reward before it can register another's suffering/threat is exploitable. Carries an OPEN question (the delay_positive_other_reward_q) about WHY protective streams should precede appetitive ones (protection vs exploitation-vulnerability). Per feedback_biology_before_formal_definitions this ordering claim needs a social-development lit-pull before promotion beyond candidate."
    - id: "fast_empathy_v5:EMP-7"
      title: "Biology grounding for the social affect-binding + reciprocity-development streams (lit-pull)"
      phase: 2
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-405", "MECH-408"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Per project rule feedback_biology_before_formal_definitions: the suffering/empathy social mapping and the developmental-ordering claim need a social-development lit-pull BEFORE registration beyond candidate"
        - "Seed anchors already present: Wu et al. 2026 (eLife) reciprocity development; Preston & de Waal 2002 / Lamm 2011 (PAM, already cited by MECH-183); the affect_primitives.md pain-dissociation anchors (Loffler 2018, Craig, Rainville) for the suffering stream"
        - "Targeted review to commission: developmental ordering of empathic concern vs prosocial reward; mirror/PAM substrate for other-bound affect; reciprocity intrinsic-reward maturation"
      last_updated: 2026-06-10
      completion_note: "Grounding debt tracker. MECH-031/MECH-183 already carry PAM lit anchors; the NEW developmental-ordering and stream-binding claims do not yet have a dedicated social-development pull. Deferred (not blocked) because it can begin independently of the substrate, but it is a registration gate for EMP-3 and EMP-6 promotion."
---
# Fast Empathy as Stream-Binding -- V5 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v5 (forward roadmap; SOCIAL mind tier; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the fast-empathy specialisation of the V5 social pillar
around one architectural prohibition (no empathy module, no empathy scalar) and
the positive mechanism it demands -- fast empathy as the binding/routing of
already-existing motivational-affective streams across self -> object -> other,
with a falsifiable A/B/C/D dissociation and a safety-relevant developmental
ordering.

This is a **V5 (social) tier** plan within the 3-tier partition (V4 = individual
mind, V5 = social, V6 = linguistic). The spine is **ARC-059 / DEV-NEED-021**:
self -> objects -> OTHERS -> language. Otherness inference REQUIRES
object-permanence + a stable self, both V4 -- so every binding node here is gated
behind V4 substrate (object_representation_v4, self_model_v4) and behind the
shared **MECH-163** multi-step hippocampal planning V4-social entry gate. It is a
*forward roadmap*, not a closure map: V5 has no experiments yet, so nodes carry
no `owner_exq` and the drift checker stays dormant. The value here is the
**readiness gates** -- for each step, exactly which V3-completion and V4-tier
prerequisites must land before the V5 social step is honest to build.

---

## One-line framing

> Fast empathy already EXISTS in REE as a capacity (ARC-010 mirror modelling,
> MECH-031 empathy coupling, MECH-183 z_beta leakage, MECH-191 signal
> legibility) and the streams it would bind already exist for the agent's OWN
> modelling (SD-011 suffering, MECH-112 wanting, the affect_primitives register).
> What is NOT done -- and must NOT be done as a module -- is the BINDING: routing
> the agent's own motivational-affective streams across a stable other-model so
> the other's predicted state becomes motivationally/ethically relevant to the
> commitment gate. The load-bearing dissociation (Wu et al. 2026) is that
> other-model prediction != reciprocity reward != residue-aware repair: three
> separable things the A/B/C/D experiment pulls apart.

---

## The empathy stack (one prohibition, one mechanism, one dissociation)

| Step | Node | Claim | Phase leaning | The readiness gate |
|---|---|---|---|---|
| prohibition (no scalar) | EMP-1 | NEWCLAIM (architectural_commitment) | V5 (registrable now) | none -- it is a design prohibition |
| open stream taxonomy | EMP-2 | NEWCLAIM (architectural_commitment) | V5 (doc step) | extends affect_primitives.md (SD-011) |
| stream-binding mechanism | EMP-3 | NEWCLAIM (mechanism) | V5 (blocked) | MECH-163 + stable other-model (OBJ-5) + DEV-NEED-021 |
| A/B/C/D dissociation | EMP-4 | NEWCLAIM (mechanism) | V5 (blocked) | EMP-3 or scripted-partner proxy |
| residue-aware repair | EMP-5 | NEWCLAIM (mechanism) | V5 (blocked) | self-state goal channel (SELF-5/MECH-214) + INV-029 |
| developmental ordering | EMP-6 | NEWCLAIM (mechanism) + Q | V5 (blocked) | EMP-3 multi-stream; ARC-059 spine |
| biology grounding | EMP-7 | (grounding debt) | cross-cutting | social-development lit-pull |

---

## Why these are V5, not V4

The individual-mind substrate this plan consumes is genuinely V4 (object
permanence, a stable self, the MECH-359/360 per-candidate affect + expression
substrate). But the SUBJECT of every node here is intrinsically social /
relational / ethical -- binding affect across an OTHER-model, reciprocity reward,
social repair, the ordering of OTHER-bound streams. That places the empathy work
itself in the V5 social tier, sitting on top of the V4 substrate. The
prerequisite chain is explicit in each readiness_gate; the work is V5.

Several existing social claims this plan builds on are not yet phase-tagged or
are tagged V4 although their subject is intrinsically social; see the
**Reassignment flags** below.

---

## What this plan deliberately does NOT do

- **Does NOT introduce an empathy module or empathy scalar.** That is the whole
  point (EMP-1). Any future design that adds `empathy_enabled` / `empathy_score`
  violates the plan's central claim.
- **Does NOT pull anything into V3.** Registering this roadmap changes no V3
  behaviour. The first real binding step (EMP-3) is gated on MECH-163 +
  V4 substrate and is V5.
- **Does NOT queue the A/B/C/D experiment.** It needs a stable other-model
  substrate (or a scripted-partner proxy) that does not exist yet (per the
  2026-05-04 intake gating note). EMP-4 carries the design; the owner_exq stays
  null until the substrate lands.
- **Does NOT re-litigate the other-model itself.** The "is the other an object?"
  question is owned by `object_representation_v4` (OBJ-5 / ARC-083) and the
  mirror-modelling plan; this plan consumes a stable other-model and binds affect
  into it.

---

## Source artefacts

| Artefact | Role |
|---|---|
| evidence/planning/thought_intake_2026-05-04_fast_empathy_stream_binding.md | the candidate cluster (primary source; A/B/C/D experiment + candidate claims) |
| docs/thoughts/2026-05-04_Empathy_development.md | raw thought (Wu et al. 2026 eLife reframing) |
| docs/architecture/affect_primitives.md | the V3 harm-affect register (SD-011) this extends into the social domain |
| claims.yaml ARC-010 / MECH-031 / MECH-183 / MECH-191 | existing fast-empathy capacity + coupling + legibility seeds |
| claims.yaml SD-011 / MECH-112 / MECH-359 / MECH-360 | the streams to be bound (suffering / wanting / per-candidate affect / expression) |
| claims.yaml MECH-163 | the V3-completion + V4-social entry gate (stays v3 -- NOT flagged for V5) |
| claims.yaml ARC-059 / developmental_needs_register DEV-NEED-021 | the self -> objects -> others maturational spine |

---

## Decision log

- **2026-06-10** -- Plan registered as a V5 (social tier) forward-roadmap.
  Seven nodes: EMP-1 (no-scalar prohibition, the spine), EMP-2 (open taxonomy),
  EMP-3 (stream-binding mechanism), EMP-4 (A/B/C/D dissociation), EMP-5
  (residue-aware repair), EMP-6 (developmental ordering + open Q), EMP-7
  (biology grounding debt). All gated behind MECH-163 + V4 substrate per
  DEV-NEED-021. Six NEW candidate claims proposed (the prohibition, the open
  taxonomy, the binding mechanism, the dissociation, the repair mechanism, the
  developmental-ordering mechanism) plus one open Q (why protective streams
  before appetitive). `generation: v5` set so the V3 closure % is unaffected.
  No claims.yaml edits (orchestrator merges).
- **2026-06-10** -- Reassignment flags raised for the existing social claims
  this plan builds on whose subject is intrinsically social (ARC-010, MECH-031,
  MECH-183, MECH-191). MECH-163 deliberately NOT flagged (it is the v3
  completion gate and stays v3); MECH-359/360 left as-is (v4/v5 substrate,
  consumed not re-scoped).
