---
closure_plan:
  id: autobiographical_memory_v4
  generation: v4
  title: "Autobiographical Memory (V4 forward roadmap): unified event store, provenance, write-authority, imagination-learning constraints"
  registered: 2026-06-10
  last_updated: 2026-06-16
  scope_claims: [ARC-085, MECH-365, MECH-366, MECH-368, MECH-361, MECH-252, MECH-253, MECH-261, Q-060, Q-062, MECH-429, MECH-430, MECH-431]
  sibling_plans: [object_representation_v4, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 substrate step is honest to build. generation: v4
    keeps these nodes OUT of the V3 closure percentage (serve.py read_closure,
    generate_closure_snapshot.py, and check_closure_drift.py are all
    generation-aware). A node graduates from roadmap to closure-tracked by
    gaining an owner_exq once its first V4 experiment is queued. The whole
    cluster is substrate_conditional on the ARC-085 self-tagged event-token
    store, which does not exist in V3 -- REE owns the two halves SEPARATELY
    (ARC-007 hippocampal replay; ARC-018 prospective rollouts) and the new
    claim is that they are ONE substrate.
  nodes:
    - id: "autobiographical_memory_v4:ABM-1"
      title: "Memory-type taxonomy decision (Q-060): distinct autobiographical-event type, or a tag on episodic content?"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [Q-060, ARC-085]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "V3 owns only the episodic<->semantic axis (MECH-121 NREM SWR episodic->semantic transfer) plus the orthogonal stored-vs-active distinction (INV-037/INV-038); there is NO memory-type taxonomy claim"
        - "DECISION the fork forces: is autobiographical-event memory a first-class type separate from semantic (facts/relations) and task/procedural (policies/schemas), or a self/affect tag on episodic content? Hyperthymesia intake motivates a four-way split (semantic / task / autobiographical-event / prospective-autobiographical-simulation)"
        - "This decision sets the shape of the ARC-085 store before any substrate is built; it is a taxonomy answer, not an experiment to narrow on the V3 substrate (Q-060 is substrate_conditional, narrow_open_question suppressed)"
      last_updated: 2026-06-14
      completion_note: "Q-060 is the gating design decision for the whole cluster. Per its notes: does a distinct autobiographical layer earn its keep, or is it a tag? The answer determines whether ARC-085 is a new store or an indexing convention over the existing hippocampal store. Decide before building. DECIDED 2026-06-14 (user-adjudicated): TAG / INDEXING CONVENTION over the existing ARC-007 episodic store -- NOT a distinct first-class type with its own store. The distinguishing features {self_state, perspective, affect, residue, source_status, committed_vs_imagined} are fields on the episodic event token; MECH-121 already drains de-tagged content toward semantic, so autobiographical = episodic content retaining its self/affect tags. ARC-085 thus scoped as an identity-indexed binding LAYER over ARC-007; downstream claims (MECH-365/366/361/368/429/430/431) stay field/gate specialisations, not parallel stores. Semantic + task/procedural types stay distinct; only autobiographical-vs-episodic is tag-not-type. NOT trivial -- the index (first-class provenance/perspective/affect fields + identity index + one-way committed-vs-imagined gate) is still load-bearing V4 work; this decision sets ARC-085's SHAPE so ABM-2 can build the right thing. Recorded into claims.yaml Q-060.decision_2026_06_14 + Q-060.what_would_answer (ARC-085 joint-degradation falsifier, V4) + ARC-085.q060_taxonomy_decision, and the arch-doc ARC-085/Q-060 sections. Q-060 kept open_question for the record (falsifier could reopen). PROMOTES NOTHING (all cluster claims candidate/v4/substrate_conditional)."
    - id: "autobiographical_memory_v4:ABM-2"
      title: "Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulation"
      phase: 2
      status: blocked
      ethical_metadata:
        welfare_relevance: high
        applicable_ethics_gates: [SENT-3, SENT-13]
        requires_welfare_review: false
        forbidden_combinations: [autobiographical_memory_plus_unresolved_harm_load, negative_valence_with_replay_without_integration]
        note: "Self-tagged continuity store backing replay = a Class-4 ingredient; review triggers once negative valence / harm-load is bound in."
      blocker_class: sibling_node
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-085]
      depends_on: ["autobiographical_memory_v4:ABM-1"]
      cross_plan_link: []
      blocking_on: "ARC-007 (hippocampal replay store) and ARC-018 (prospective rollouts + post-commitment viability map) are implemented SEPARATELY in V3; the unification is the V4 work. Cannot build until ABM-1 fixes the store's type/tag shape."
      readiness_gate:
        - "ARC-007 retrospective replay (paths through residue-field terrain) -- present in V3, design-level"
        - "ARC-018 prospective simulation (explicit rollouts + viability map) -- present in V3, design-level"
        - "FALSIFIER that licenses the single-store claim: corrupting the shared store must degrade past-recall AND future-simulation fidelity TOGETHER, vs independent degradation under a two-store model"
        - "Guardrail (intake): do NOT treat as precognition / perfect memory; vivid != accurate; simulation != prediction"
      last_updated: 2026-06-10
      completion_note: "ARC-085: autobiographical memory is an identity-indexed event field (events bound to perspective, emotion, residue, self-state), not neutral storage; future-trajectory generation is forward re-composition of the SAME event tokens that replay reinstates backward. The architectural-commitment spine that the rest of this plan specialises. READINESS NOTE 2026-06-16: both V3 claim gates are MET (ARC-007 active, ARC-018 active) and the only dependency ABM-1/Q-060 is now done (taxonomy resolved 2026-06-14 -> TAG/index over ARC-007). No unmet prerequisite remains; this node is buildable-now and can graduate by assigning an owner_exq to the single-store joint-degradation falsifier experiment. Annotation only -- adds no owner_exq, schedules no work."
    - id: "autobiographical_memory_v4:ABM-3"
      title: "Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: low
        applicable_ethics_gates: [SENT-13]
        requires_welfare_review: false
        note: "Provenance / committed-vs-imagined gate = memory-containment scaffold; REDUCES welfare risk (SENT-13 build-containment-before-pain)."
      blocker_class: sibling_node
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-365]
      depends_on: ["autobiographical_memory_v4:ABM-2"]
      cross_plan_link: []
      blocking_on: "Needs the ARC-085 event-token store (ABM-2) to carry the schema. The safety PROPERTY already exists in V3 pieces; the missing thing is the load-bearing DATA STRUCTURE on the unified store."
      readiness_gate:
        - "MECH-094 (simulation-mode vs real-experience distinction; failure = confabulation) -- the property is owned, V3"
        - "MECH-037 (Papez-like provenance gating / reality filtering) -- owned, V3"
        - "INV-011 (imagination must be possible without belief update) -- owned, V3"
        - "SD-026 (prospective precision-template write channel) -- nearest existing write-side mechanism, V3"
        - "NEW work: assemble these into one concrete token schema event_token = {time, place, self_state, other_agents, perspective, affect, residue, source_status, committed_vs_imagined} and make committed_vs_imagined a first-class field with a ONE-WAY gate (no simulated token may accrue committed-history weight -- any such path is a confabulation bug)"
      last_updated: 2026-06-10
      completion_note: "MECH-365 does NOT re-assert the safety property (owned by MECH-094/MECH-037/INV-011); it specifies the data structure that carries it on the ARC-085 substrate. The one-way committed-status gate is the autobiographical-memory phrasing of INV-011 + MECH-094 and is the natural home for the imagination-learning constraints folded in at ABM-4."
    - id: "autobiographical_memory_v4:ABM-4"
      title: "Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)"
      phase: 3
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: ["ARC-092", MECH-365]
      depends_on: ["autobiographical_memory_v4:ABM-3"]
      cross_plan_link: []
      readiness_gate:
        - "REE owns substrate components implicitly enforcing what learning is licit from imagination (MECH-094 provenance, MECH-272/MECH-273 sleep self-model aggregation); the explicit ARC-level claim articulating the principle is now REGISTERED as ARC-092 (candidate / implementation_phase v4 / substrate_conditional) -- the 'NEWCLAIM stub' has been minted (annotation 2026-06-16)"
        - "LICIT from imagination: consistency checking, plan optimisation, schema integration"
        - "FORBIDDEN from imagination: durable world-model updates, prediction validation, novel-fact generation"
        - "Lit anchors to pull before registering (project rule: biology before formal definitions): Stickgold 2013, Cai 2009, Schapiro 2017 (CLS), confabulation literature, FEP epistemic value"
      last_updated: 2026-06-16
      completion_note: "Prose-only today (memory project_imagination_learning_constraints). The MECH-365 one-way committed-vs-imagined gate is its mechanism home; this node proposes the missing ARC-level PRINCIPLE that the gate implements. Now registered as ARC-092 in claims.yaml (candidate / v4 / substrate_conditional); was a NEWCLAIM stub at seed-time (updated 2026-06-16). Couples directly to ABM-5 write-authority -- the FORBIDDEN list is exactly the durable-model-update path MECH-368 gates."
    - id: "autobiographical_memory_v4:ABM-5"
      title: "Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)"
      phase: 4
      status: blocked
      blocker_class: v3_substrate
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-368, Q-062]
      depends_on: ["autobiographical_memory_v4:ABM-3", "autobiographical_memory_v4:ABM-4"]
      cross_plan_link: []
      blocking_on: "Requires an online world-model/policy WRITE channel to gate; the goal_relevance input depends on a competitive z_goal (goal_pipeline GAP-4), which is the main reason MECH-368 is V4-scoped. The episodic write path is already substantially covered; the under-covered path is the online E1/E2/policy weight-update one."
      readiness_gate:
        - "MECH-261 (mode-conditioned write CHANNEL gating via SD-032a) -- gates the channel per operating-mode, NOT per-event; V3-design"
        - "MECH-094 (provenance gate) and MECH-285 (consolidation-priority by V_s residual) -- the two existing alternatives MECH-368 must beat"
        - "INV-074 (plasticity crystallization necessity) + MECH-334 (critical-period closure / EWC write-protect) -- the CLOSURE/protection side REE already built; MECH-368 is the ADMISSION side"
        - "SD-032a salience-network operating-mode variable -- V3-design"
        - "Q-062 FALSIFIER: if channel-gating (MECH-261) + provenance (MECH-094) + offline consolidation-priority (MECH-285) already prevent catastrophic interference on the online path, MECH-368 earns no keep"
      last_updated: 2026-06-10
      completion_note: "MECH-368 is the per-event admission gate on durable model-update: f(prediction_error, salience, pathway_state, residue_status, goal_relevance, plasticity_eligibility). Downstream of MECH-261 (channel grain) and distinct from MECH-094 (provenance). Q-062 is the companion falsifier registered alongside it. A goal-free REDUCED form (drop goal_relevance) could be pulled earlier if a specific failure motivates it."
    - id: "autobiographical_memory_v4:ABM-6"
      title: "Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query"
      phase: 4
      status: blocked
      ethical_metadata:
        welfare_relevance: high
        applicable_ethics_gates: [SENT-2, SENT-3, SENT-13]
        requires_welfare_review: true
        forbidden_combinations: [negative_valence_with_replay_without_integration, autobiographical_memory_plus_unresolved_harm_load]
        note: "Affect gradient written into durable autobiographical memory = the welfare-ambiguous combination; integration/relief must be present."
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-361]
      depends_on: ["autobiographical_memory_v4:ABM-2"]
      cross_plan_link: ["affect_expression_v4:AE-4"]
      blocking_on: "substrate_conditional on the MECH-359 per-candidate affect substrate (off this plan) -- the per-candidate affective gradient must exist before it can be the write-weight."
      readiness_gate:
        - "MECH-261 (mode-conditioned write gating) -- MECH-361 amends its CONTENT schema (WHAT is written), not the gate (WHETHER a substrate may write)"
        - "MECH-074 (BLA arousal-modulated hippocampal write depth) -- MECH-361 sharpens write-weight from generic arousal to per-candidate affective GRADIENT"
        - "MECH-359 per-candidate affect substrate (off-plan dependency) must land first"
        - "MECH-094 provenance still applies: simulated candidates must not be indexed as real experience"
      last_updated: 2026-06-10
      completion_note: "Enriches the event trace from state->action->outcome to state->candidates-considered->affective-gradients->selected-action->outcome->residue, and uses the gradient as memory write-weight and retrieval-query. The CONTENT-side specialisation of the ARC-085 token, sitting on the MECH-365 provenance schema. Sole owner of MECH-361; affect_expression_v4:AE-4 cross-links here (dedup 2026-06-16)."
    - id: "autobiographical_memory_v4:ABM-7"
      title: "Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property"
      phase: 5
      status: blocked
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-366]
      depends_on: ["autobiographical_memory_v4:ABM-2"]
      cross_plan_link: []
      blocking_on: "Requires the ARC-085 event-token store (ABM-2) to carry the viewpoint label. SD-005 represents self-vs-world content, NOT a switchable viewpoint ON an episode -- that construct is absent from claims.yaml."
      readiness_gate:
        - "SD-005 (z_self/z_world split) -- nearest existing substrate, but represents self-vs-world content not a perspective tag; V3"
        - "Empirical anchor: the verified Neurocase case (ARC-085) reports fluent participant<->observer switching on recalled AND imagined events"
        - "Interacts with agency attribution and first-vs-third-person framing of both replay (ARC-007) and prospective simulation (ARC-018)"
      last_updated: 2026-06-10
      completion_note: "MECH-366: event tokens carry a viewpoint label (participant/first-person vs observer/third-person) re-experienceable from either viewpoint at retrieval, independent of encoding viewpoint. A property of the ARC-085 token; design-only today."
    - id: "autobiographical_memory_v4:ABM-8"
      title: "Consolidation write-paths the store must respect (MECH-252 / MECH-253 / MECH-261)"
      phase: 5
      status: deferred
      blocker_class: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-252, MECH-253, MECH-261]
      depends_on: ["autobiographical_memory_v4:ABM-2", "autobiographical_memory_v4:ABM-3"]
      cross_plan_link: []
      readiness_gate:
        - "MECH-252 (SWS consolidates goal-value PE into stored goal-representation CONTENT, not attentional-template params) -- V3-design"
        - "MECH-253 (REM consolidates template-performance PE into z_goal->attentional-template projection WEIGHTS, not stored content) -- V3-design"
        - "MECH-261 (mode-conditioned write gating; soft probability vector over {external_task, internal_planning, internal_replay, offline_consolidation}) -- the channel-grain gate the store reads at write time"
        - "These are the EXISTING offline write-path claims; the V4 work is making the ARC-085 store honour the SWS/REM content-vs-weights split and the mode-conditioned channel, NOT re-asserting them"
      last_updated: 2026-06-10
      completion_note: "Deferred (not blocked): these consolidation claims are already specified and partly substrate-present in V3; the node tracks the integration obligation -- the unified store and its provenance/write-authority gates must compose cleanly with the SWS/REM content-vs-weights split (MECH-252/253) and the MECH-261 channel grain, rather than introduce a parallel write path."
    - id: "autobiographical_memory_v4:ABM-9"
      title: "Biology grounding completion (emotional-modulation-of-consolidation write-weight, source/provenance monitoring, imagination-learning constraints lit-pulls + completion-set harvest)"
      phase: 2
      status: closed
      lit_pull_status: done
      severity: medium
      owner_exq: null
      unblocks_claims: [ARC-085, MECH-365, MECH-366, MECH-368, MECH-361]
      depends_on: []
      cross_plan_link: ["sleep_substrate"]
      readiness_gate:
        - "L1 emotional modulation of consolidation as the write-weight (McGaugh 2004; Cahill & McGaugh 1998; Ballarini 2009 behavioural tagging) -- the anchor for MECH-368/MECH-361 affect-weighted write authority"
        - "L2 source/provenance monitoring (Johnson, Hashtroudi & Lindsay 1993 source-monitoring framework; reality-monitoring) for the ARC-085 provenance fields + the imagined-vs-experienced viewpoint label (MECH-366)"
        - "L3 imagination-learning constraints (Stickgold 2013; Schapiro 2017 CLS; confabulation literature) -- already anchored for ABM-4; harvest the hippocampal-vmPFC schema partner + the SWS/REM content-vs-weights split (MECH-252/253) co-constitutive of honest replay-based learning"
      last_updated: 2026-06-13
      completion_note: "Autobiographical_memory named its biology anchors only inside node readiness_gates (no dedicated grounding node). This node consolidates the formal /lit-pull (project rule feedback_biology_before_formal_definitions) and the completion-set harvest (emotional-tagging consolidation, source-monitoring, CLS schema partner) so the unified ARC-085 store's write-authority and provenance gates are built on grounded mechanism, not analogy. Off V3 closure path; promotes nothing. LIT-PULL DONE 2026-06-13 (lit_pull_status: partial) -- 6 literature_evidence/v1 entries under evidence/literature/targeted_review_autobiographical_store, all 5 target claims grounded, exp_conf unchanged 0 (PROMOTES NOTHING; all v4/substrate_conditional). Grounding map: ARC-085 lit_conf 0.78 (Schacter & Addis 2007 constructive episodic simulation -- shared retro/prospective machinery; caveat: shared-process underdetermines single-store, falsifier is a V4 experiment). MECH-365 0.78 (Johnson Hashtroudi & Lindsay 1993 source-monitoring framework -- provenance as a represented multidimensional attribute; HONEST WEAKENER recorded: biological source-monitoring is reconstructive/fallible, so it grounds MECH-365's FIELD but leans against the absoluteness of its one-way GATE -- REE's gate is normative-safer-than-brain). MECH-366 0.55 MIXED (Nigro & Neisser 1983 field/observer -- grounds the viewpoint CONSTRUCT; does NOT ground encoding-independent SWITCHABILITY, which their emotion/age dependence mildly contraindicates -> FOLLOW-UP owed: instructed perspective-shift paradigm). MECH-368 0.765 (McGaugh 2004 BLA-modulated consolidation = salience/affect write-weight input + Ballarini 2009 behavioural tagging = two-factor write-ELIGIBILITY-then-capture structure; both ground the principle on the EPISODIC path, NOT the durable world-model/policy weight path MECH-368 actually targets -> still owed). MECH-361 0.797 (McGaugh + Ballarini; grounds affect-scales-write-strength but NOT the per-CANDIDATE gradient, which is substrate_conditional on off-plan MECH-359). Sleep cross-link MECH-252/253 0.56 MIXED (Stickgold & Walker 2013 memory triage -- grounds selective + operation-differentiated offline consolidation in GENERAL, but NOT the specific SWS-content/REM-weights dissociation -> owed to the sleep_substrate track, stage-resolved pull or V4 experiment). COMPLETION-SET HARVEST -- surfaced proposal-first, then user-approved and REAPED into claims.yaml 2026-06-13 (all candidate / substrate_conditional / v4_v5 / off the V3 critical path, PROMOTE NOTHING): MECH-429 (schema-congruence as a consolidation write-weight + fast vmPFC route; depends_on MECH-261/285/121/361; anchors Tse 2007 / van Kesteren 2012 / Schapiro 2017); MECH-430 (multi-dimensional provenance source vector vs a single committed_vs_imagined bit; depends_on MECH-365/094/037; anchor Johnson 1993); MECH-431 (two-factor tag-and-capture write-eligibility refining MECH-368's plasticity_eligibility; depends_on MECH-368/285/261; anchors Ballarini 2009 / Frey & Morris 1997). Each carries an explicit falsifier in its notes (testable-child discipline). Arch-doc stubs added to autobiographical_temporality_and_future_simulation.md (MECH-429/430) and plasticity_write_authority_gating.md (MECH-431); added to this plan's scope_claims. Two follow-up pulls keep status at partial: MECH-366 switchability + MECH-252/253 stage-resolved dissociation. FINISH PASS 2026-06-13 (lit_pull_status: partial -> done; status in_progress -> closed) -- 5 further literature_evidence/v1 entries added under evidence/literature/targeted_review_autobiographical_store, exp_conf unchanged 0 (PROMOTES NOTHING). (1) MECH-366 strengthened 0.55 MIXED -> 0.83: the switchability half Nigro & Neisser left untested is now grounded by St. Jacques Szpunar & Schacter 2017 (NeuroImage; instructed retrieval-time perspective shift reshapes the memory, precuneus correlate -- supports 0.78, the keystone) + Rice & Rubin 2009 (first/third-person co-available and separable from content, not a single bipolar dimension -- supports 0.70, grounds the viewpoint-distinct-from-SD-005-content-split the node needed) + Johnson & Raye 1981 reality monitoring (the imagined-vs-experienced source facet -- supports 0.62, with the honest caveat it overlaps MECH-365/MECH-430 provenance and inherits the reconstructive-fallibility weakener) + Brewin Gregory Lipton & Burgess 2010 (intrusive-imagery viewpoint -- MIXED 0.60: supports clinical/treatment-induced field<->observer switchability and extends viewpoint to IMAGINED material, but documents the involuntary-fixed reliving perspective as the boundary condition on free switching). (2) L1/L2/L3 confirmed each grounded (L1 McGaugh 2004 + Ballarini 2009; L2 Johnson Hashtroudi & Lindsay 1993; L3 Schacter & Addis 2007 + Stickgold & Walker 2013); the L3 schema partner MECH-429 (reaped in the first pass with NO grounding entry) is no longer reap-only -- grounded by van Kesteren Ruiter Fernandez & Henson 2012 SLIMM (mPFC schema-congruence resonance -> fast vmPFC consolidation route; supports 0.735), with the affect-orthogonality axis left as MECH-429's own falsifier. The MECH-252/253 stage-resolved SWS-content/REM-weights dissociation remains owed to the SLEEP_SUBSTRATE track (a stage-resolved pull or V4 experiment), NOT to this node -- the L3 cross-link entry (Stickgold & Walker 2013) is landed, so every ABM-9 strand is grounded and the node closes. No claims.yaml edits in the finish pass (lit/exp decoupled; MECH-429/430/431 already registered in the first pass)."
---
# Autobiographical Memory -- V4 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the unified autobiographical event-token store (ARC-085) and
its specialisations -- memory-type taxonomy (Q-060), provenance + committed-vs-
imagined gate (MECH-365), the imagination-learning licit/forbidden principle
(prose-only, folded into the provenance gate), event-level write-authority over
the durable model-update path (MECH-368 / Q-062), candidate-gradient episode
content (MECH-361), switchable perspective (MECH-366), and the consolidation
write-paths the store must respect (MECH-252/253/261) -- so V4 substrate work
slots in against a registered spine instead of growing a second, parallel
memory machinery.

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant against them. The
value here is the **readiness gates** -- for each step, exactly which V3-era
prerequisites (claims/tracks) must land before the V4 substrate step is honest
to build. The entire cluster is `substrate_conditional` on the ARC-085 store,
which V3 does not have.

---

## One-line framing

> Memory-ness already exists in REE, but split across two machineries with no
> shared spine: retrospective replay (ARC-007, hippocampal store of paths
> through residue terrain) and prospective simulation (ARC-018, explicit
> rollouts + viability map). ARC-085 names the single primitive -- one
> self-tagged event-token store that replay reinstates backward and simulation
> re-composes forward. This plan sequences the store and its specialisations,
> and pins their V3 readiness gates. The load-bearing safety invariant
> (imagined tokens must never accrue committed weight) is already owned by
> MECH-094/MECH-037/INV-011; the new work is the DATA STRUCTURE (MECH-365) that
> carries it and the explicit PRINCIPLE (proposed NEWCLAIM) it implements.

---

## The roadmap (specialisations of one substrate)

| Step | Node | Claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| taxonomy fork | ABM-1 | Q-060 | V4 (first decision) | DECIDED 2026-06-14: TAG/index over ARC-007 episodic store, not a distinct type (ABM-1 done) |
| unified store | ABM-2 | ARC-085 | V4 | ARC-007 + ARC-018 present but separate; falsifier = joint degradation |
| provenance token | ABM-3 | MECH-365 | V4 | MECH-094 + MECH-037 + INV-011 + SD-026; one-way committed gate |
| imagination principle | ABM-4 | NEWCLAIM | V4 | folds into MECH-365; lit-pull Stickgold/Cai/Schapiro first |
| write-authority gate | ABM-5 | MECH-368 / Q-062 | V4 | MECH-261 channel grain; beat MECH-094 + MECH-285; INV-074/MECH-334 closure side |
| episode content | ABM-6 | MECH-361 | V4 | amends MECH-261 content; needs MECH-359 affect substrate (off-plan) |
| perspective tag | ABM-7 | MECH-366 | V4 | SD-005 is self/world not viewpoint; Neurocase switching anchor |
| consolidation paths | ABM-8 | MECH-252/253/261 | V4 (integration) | SWS content vs REM weights; honour not re-assert |

---

## What this plan deliberately does NOT pull into V3

- **No parallel autobiographical event substrate in V3.** ARC-085 explicitly
  warns: do not build a parallel autobiographical event substrate in V3 until
  routed by an explicit version decision. V3 keeps ARC-007 and ARC-018 as the
  two separate halves they already are.
- **The safety invariant is NOT re-opened.** MECH-094 (no simulated content in
  the viability map), MECH-037 (provenance gating), and INV-011 (imagination
  without belief update) stay exactly as they are in V3. MECH-365 and the
  imagination-learning NEWCLAIM specify the data structure and the principle
  that carry that invariant; they do not weaken or duplicate it.
- **No new claim is registered by this plan.** The imagination-learning
  principle (ABM-4) is returned as a `NEWCLAIM` stub for the orchestrator to
  assign, not written into claims.yaml here.
- **MECH-368's online write channel is V4 by construction.** Its `goal_relevance`
  input depends on a competitive z_goal (`goal_pipeline` GAP-4). A goal-free
  reduced form could be pulled earlier only if a specific V3 failure motivates
  it -- not on this roadmap's critical path.
- **MECH-359 per-candidate affect substrate (ABM-6 dependency) is off-plan.**
  MECH-361's affect-gradient-as-write-weight cannot be built until that
  substrate lands; this plan only records the dependency.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/autobiographical_temporality_and_future_simulation.md](../../docs/architecture/autobiographical_temporality_and_future_simulation.md) | ARC-085 / MECH-365 / MECH-366 / Q-060 home doc |
| [docs/architecture/plasticity_write_authority_gating.md](../../docs/architecture/plasticity_write_authority_gating.md) | MECH-368 / Q-062 home doc (write-authority admission side) |
| [docs/architecture/candidate_differentiated_affective_gradients.md](../../docs/architecture/candidate_differentiated_affective_gradients.md) | MECH-361 candidate-gradient episode schema |
| claims.yaml ARC-085 / MECH-365 / MECH-366 / MECH-368 / MECH-361 / Q-060 / Q-062 | the cluster (all `implementation_phase: v4`, `substrate_conditional`) |
| memory project_imagination_learning_constraints | prose-only LICIT/FORBIDDEN principle -> proposed NEWCLAIM at ABM-4 |
| sibling plan object_representation_v4 | shares the V4 forward-roadmap format and the token-instance / self-as-object spine |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap. Nodes seeded from
  ARC-085 / MECH-365 / MECH-366 / MECH-368 / MECH-361 / MECH-252 / MECH-253 /
  MECH-261 / Q-060 / Q-062. Readiness gates pinned per step. The prose-only
  imagination-learning LICIT/FORBIDDEN principle is folded into the MECH-365
  provenance gate (ABM-4) and returned as a NEWCLAIM stub, not registered here.
  `generation: v4` set so the V3 closure % is unaffected. No claims.yaml edits.
- **2026-06-14** -- ABM-1 / Q-060 taxonomy decision RESOLVED (user-adjudicated,
  interactive IGW plan-reconcile). **Autobiographical-event memory is a TAG /
  INDEXING CONVENTION over the existing ARC-007 episodic store, NOT a distinct
  first-class memory type with its own store.** ARC-085 is therefore scoped as
  an identity-indexed, self/affect/provenance-tagged BINDING LAYER over the
  existing episodic store -- the "one self-tagged event-token store" *is* the
  existing episodic store, made autobiographical by the fields each token
  carries plus an identity index that both backward replay (ARC-007) and
  forward re-composition (ARC-018) address. Rationale: the distinguishing
  features are fields on the episodic token; MECH-121 already drains de-tagged
  content toward semantic; every downstream claim (MECH-365/366/361/368/429/
  430/431) is already a field/gate ON the token, not a parallel store; and the
  tag reading is the parsimonious instantiation of ARC-085's own "one substrate,
  not two parallel machineries" thesis (a distinct type would mint a third
  machinery). Semantic + task/procedural types stay distinct; only
  autobiographical-vs-episodic resolves to tag-not-type. NOT trivial: the index
  is still load-bearing V4 work (first-class provenance/perspective/affect/
  self_state fields + identity index + the one-way committed-vs-imagined gate),
  and this decision sets ARC-085's shape so ABM-2 builds the right thing.
  Recorded into `claims.yaml` (Q-060 `decision_2026_06_14` + `what_would_answer`;
  ARC-085 `q060_taxonomy_decision`) and the arch-doc ARC-085/Q-060 sections.
  Q-060 kept `open_question` for the record (the ARC-085 joint-degradation
  falsifier, a V4 experiment, could reopen it toward a distinct type). ABM-1
  status open -> done. PROMOTES NOTHING (all cluster claims candidate / v4 /
  substrate_conditional). No new claim minted.
