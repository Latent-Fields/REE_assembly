---
closure_plan:
  id: object_representation_v4
  generation: v4
  title: "Object Representation (V4 PILLAR roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-16
  scope_claims: [ARC-080, ARC-081, ARC-082, ARC-083, ARC-006, MECH-045, MECH-278]
  sibling_plans: [goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 substrate step is honest to build. generation: v4
    keeps these nodes OUT of the V3 closure percentage (serve.py read_closure,
    generate_closure_snapshot.py, and check_closure_drift.py are all
    generation-aware). A node graduates from roadmap to closure-tracked by
    gaining an owner_exq once its first V4 experiment is queued.
  nodes:
    - id: "object_representation_v4:OBJ-1"
      title: "Type-vs-token-vs-anchor representational fork (the first design decision)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-080]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "V3 LIVE object work is TYPE-level: SD-049 per-type tag + classifier head; SD-015 location-invariant z_resource; SD-057 IncentiveTokenBank keyed by resource TYPE"
        - "V3 also has a spatial-ANCHOR store (SD-039 / MECH-292 / MECH-293 ghost-goal bank, payload = goal-snapshot)"
        - "DECISION the fork forces: does the V4 object-file key on TYPE (apples), ANCHOR (a location), or TOKEN-INSTANCE (this apple, tracked through occlusion)? Permanence/tools/self/other all need TOKEN-INSTANCE"
      last_updated: 2026-06-14
      completion_note: "RESOLVED 2026-06-14 (IGW plan-reconcile, user decision). The fork is resolved NOT by crowning one of {type, token, anchor} but by making the COORDINATION the primitive: an object is a binding that holds three distinct coordinate facets -- TYPE readout (SD-015/SD-049), SPATIAL ANCHOR (SD-039/MECH-292/293), TOKEN-INSTANCE individuation (ARC-006/MECH-044/MECH-045) -- none reducing to another; the object-file is the coregistration structure. Fits the slot(address)+synchrony(bind)+superposition-catastrophe(why-distinct) lit on file, and the V3-EXQ-641a / z_world dim=32 'bound-representation absent' diagnostics. Recorded on ARC-080 (claims.yaml functional_restatement OBJ-1 RESOLUTION block + SD-039 added to depends_on as the anchor facet) and arch doc arc_080_object_representation_primitive.md SS3. CONSEQUENCE: OBJ-2 reframed from 'pick token over type' to 'build the coregistration structure binding the three facets'; z_object = type-readout OF a coordinate object-file. Open sub-fork (token-vs-type individuation strength within the bound token facet) deferred to the first OBJ-2 build step. Design commitment only -- stays v4/v3_pending, off the V3-closure critical path; no substrate built."
    - id: "object_representation_v4:OBJ-2"
      title: "PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)"
      phase: 2
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-080, ARC-006, MECH-045]
      depends_on: ["object_representation_v4:OBJ-1"]
      cross_plan_link: []
      readiness_gate:
        - "Reactivate ARC-006 / MECH-044 / MECH-045 (object-file + relational binding + object-file persistence; provisional, design-only, NOT in ree-v3 code)"
        - "Generalise the SD-039 / MECH-292 / MECH-293 ghost-goal bank from goal-snapshot payload to an object-TOKEN payload"
        - "MECH-278 object DEFINITION (causally-coherent feature bundle under intervention) -- currently BYPASSED in V3 (z_world engineered pre-split)"
      last_updated: 2026-06-10
      completion_note: "ARC-080 documents PILLAR 1 as a NEW future child (token persistence through occlusion); it is deliberately NOT registered as a separate claim yet (no duplication). DEV-NEED-021 makes this load-bearing for the social pillar."
    - id: "object_representation_v4:OBJ-3"
      title: "PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot"
      phase: 3
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [ARC-081]
      depends_on: ["object_representation_v4:OBJ-2"]
      cross_plan_link: ["self_model_v4"]
      readiness_gate:
        - "V3 BEGINNING present (no gate): SD-005 z_self split, MECH-256 single-pass self-attribution comparator + SD-029 z_harm_s instantiation (these SUPERSEDE SD-003 as of 2026-04-18), MECH-277 + ARC-059 stage 1 self-as-object, ARC-074 reward-free babbling Phase 0"
        - "V4 CUTOVER gated on: DR-10..DR-14 self-model integration audit; MECH-214 (goal E1-representable); MECH-215 (self-model prerequisite for agentive prediction); INV-064 (maturational-sequence necessity); SD-030 (E2 self-forward-model, V4-deferred)"
        - "MECH-163 multi-step hippocampal planning (shared V4-entry gate)"
      last_updated: 2026-06-16
      completion_note: "ARC-081 central correction: self-as-object is NOT flatly V4 -- it has a V3 beginning and a V4 object-file-slot cutover. The beginning is live; the cutover is the work this node tracks. POINTER 2026-06-16: the self-as-object V4 cutover is decomposed per-node in self_model_v4 (SELF-1/2/3/5/7/8 cover DR-10..14 / MECH-214/215 / INV-064 / SD-030). OBJ-3 retains ONLY the object-file-slot framing (z_self as a privileged object-file slot in the ARC-080 coregistration structure) and defers the cutover mechanics to self_model_v4 to avoid two plans tracking the same work."
    - id: "object_representation_v4:OBJ-4"
      title: "PILLAR 3 -- tools/affordances object->action binding (ARC-082)"
      phase: 3
      status: blocked
      blocker_class: v3_substrate
      severity: high
      owner_exq: null
      unblocks_claims: [ARC-082]
      depends_on: ["object_representation_v4:OBJ-2"]
      cross_plan_link: []
      blocking_on: "SD-016 cue_action_proj is inert in V3 (V3-EXQ-449 found 0.0 gradient; non-differentiable CEM severs the path before E3.select). Grounding must land before object->action binding is meaningful."
      readiness_gate:
        - "V3 grounding track (straddles V3, owned separately): EXP-0155 instrumentation of SD-016 cue_action_proj"
        - "SD-055 differentiable-CEM dependency (implemented + substrate-ready 2026-05-21) -- restores gradient to cue_action_proj"
        - "FULL binding via the object-file (afforded actions keyed to a token-instance slot) is V4, once OBJ-2 exists"
      last_updated: 2026-06-10
      completion_note: "ARC-082: the V3 substrate exists but is ungrounded. Grounding is its own existing track; full object->action binding via the object-file is the V4 step this node tracks."
    - id: "object_representation_v4:OBJ-5"
      title: "PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots"
      phase: 4
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [ARC-083]
      depends_on:
        - "object_representation_v4:OBJ-2"
        - "object_representation_v4:OBJ-3"
      cross_plan_link: []
      blocking_on: "Gated on MECH-163 multi-step hippocampal planning before V4 social entry; and on DEV-NEED-021 prerequisites object-permanence (OBJ-2) + self-stability (OBJ-3)."
      readiness_gate:
        - "MECH-163 multi-step hippocampal planning (V4 social-entry gate)"
        - "ARC-010 mirror modelling (stable claim, unimplemented as an other-object slot); ARC-047 SocialGridWorld (candidate V4 harness)"
        - "DEV-NEED-021: otherness inference REQUIRES object persistence (PILLAR 1 / OBJ-2) + a stable self (PILLAR 2 / OBJ-3)"
      last_updated: 2026-06-10
      completion_note: "ARC-083: each other agent j carried as its own token-keyed object-file (z_self_j, z_harm_a_j, drive, commitment chain) -- a specialisation of the ARC-080 object-file. Design-only today."
    - id: "object_representation_v4:OBJ-6"
      title: "Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)"
      phase: 2
      status: in_progress
      lit_pull_status: partial
      severity: medium
      owner_exq: null
      unblocks_claims: [ARC-080, ARC-006]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "L1 object-files & feature-binding (Kahneman/Treisman/Gibbs 1992; Treisman & Gelade 1980 FIT) -- ACTIVE 2026-06-04"
        - "L2 object permanence (Piaget; Baillargeon; Spelke core-knowledge; Kellman & Spelke 1983) -- ACTIVE 2026-06-04"
        - "L3 affordances (Gibson); L4 self-as-object (Gallagher/Botvinick); L5 ToM (Woodward/Csibra) -- follow when their pillars are scheduled"
      last_updated: 2026-06-10
      completion_note: "ARC-006 / MECH-044 / MECH-045 had NO biology lit-pull at ARC-080 registration (project rule feedback_biology_before_formal_definitions). L1/L2 pulls were active 2026-06-04; this node tracks closing that grounding debt before the pillar substrate is built."
---
# Object Representation -- V4 PILLAR Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the four object pillars of the ARC-080 umbrella -- (1)
permanence, (2) self-as-object, (3) tools/affordances, (4) others-as-object --
plus the foundational type-vs-token representational fork and the biology
grounding debt, so V4 substrate work slots in against a registered spine
instead of drifting into a fourth blind per-item store.

This is the **first V4 plan** registered in the closure-map pipeline and the
pilot for the generation-segmented roadmap. It is a *forward roadmap*, not a
closure map: V4 has no experiments yet, so nodes carry no `owner_exq` and the
drift checker stays dormant against them. The value here is the **readiness
gates** -- for each pillar, exactly which V3-era prerequisites (claims/tracks)
must land before the V4 substrate step is honest to build.

---

## One-line framing

> Object-ness already exists in REE, but in three disconnected lineages with no
> shared spine: a dormant representational layer (ARC-006/MECH-044/MECH-045), a
> developmental-ordering layer (ARC-059/MECH-276/277/278, with MECH-278's object
> definition bypassed in V3), and a live resource-bound identity latent
> (SD-015 -> SD-049 -> SD-057). ARC-080 named the single cross-cutting primitive
> and gave the four pillars a parent. This plan sequences the pillars and pins
> their V3 readiness gates.

---

## The four pillars (specialisations of one primitive)

| Pillar | Node | Claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| (fork) type/token/anchor | OBJ-1 | ARC-080 | RESOLVED 2026-06-14 | coordination-is-the-primitive: object = binding of type+anchor+token coordinate facets (none subsumes) |
| 1 -- permanence | OBJ-2 | ARC-080 PILLAR 1 (future child) | V3-straddle / V4 | reactivate MECH-045; generalise SD-039/292/293 bank to object-token |
| 2 -- self-as-object | OBJ-3 | ARC-081 | V3 begins / V4 cutover | DR-10..14 + MECH-214/215 + INV-064 + SD-030 + MECH-163 |
| 3 -- tools/affordances | OBJ-4 | ARC-082 | V3 substrate / V4 binding | EXP-0155 + SD-055 differentiable-CEM (SD-016 grounding) |
| 4 -- others-as-object | OBJ-5 | ARC-083 | V4 | MECH-163 planning; OBJ-2 + OBJ-3 (DEV-NEED-021) |
| grounding debt | OBJ-6 | ARC-006/ARC-080 | cross-cutting | L1..L5 biology lit-pulls (L1/L2 active 2026-06-04) |

---

## What this plan deliberately does NOT pull into V3

- **SD-057 / GAP-7 is NOT a prerequisite here.** SD-057 binds incentive
  salience to the SD-049 per-*type* tag (type-level identity V3 already has,
  `implementation_phase: v3`); ARC-080 lists SD-057 as a **consumer**, not a
  prerequisite. The goal-pipeline GAP-7 wanting!=liking work is owned by
  `goal_pipeline` and is untouched by this roadmap.
- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour. The first real substrate step (generalising
  z_object from a type-tag store to a token-keyed object-file) is V4 and must
  not enter V3 closure.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/arc_080_object_representation_primitive.md](../../docs/architecture/arc_080_object_representation_primitive.md) | ARC-080 umbrella + the four pillars |
| evidence/planning/object_representation_thread_2026-06-04.md | "Option A" spine adopted by the user 2026-06-04 |
| claims.yaml ARC-080 / ARC-081 / ARC-082 / ARC-083 | the umbrella + pillar claims (all `implementation_phase: v4`, `v3_pending: true`) |
| developmental_needs_register DEV-NEED-021 | object-permanence + self-stability are prerequisites for the social pillar |

---

## Decision log

- **2026-06-10** -- Plan registered as the pilot V4 forward-roadmap. Nodes seeded
  from ARC-080/081/082/083. Readiness gates pinned per pillar. `generation: v4`
  set so the V3 closure % is unaffected. No claims.yaml edits.
- **2026-06-14** -- OBJ-1 RESOLVED (IGW plan-reconcile, user decision). The
  type-vs-token-vs-anchor fork is resolved by making the **coordination** the
  primitive, not by crowning one facet: an object is a binding that holds three
  distinct coordinate facets -- TYPE readout (SD-015/SD-049), SPATIAL ANCHOR
  (SD-039/MECH-292/293), TOKEN-INSTANCE individuation (ARC-006/MECH-044/MECH-045)
  -- none reducing to another; the object-file is the coregistration structure
  (slot=address, synchrony=bind, superposition-catastrophe=why-distinct). Recorded
  on ARC-080 (`functional_restatement` OBJ-1 RESOLUTION block; SD-039 added to
  `depends_on` as the anchor facet) and the arch doc (SS3). Consequence: OBJ-2
  reframes from "pick token over type" to "build the coregistration structure
  binding the three facets"; `z_object` = type-readout *of* a coordinate
  object-file. Open sub-fork (token-vs-type individuation strength) deferred to the
  first OBJ-2 build step. Design commitment only; no claims.yaml *claim* added, no
  promotion, off the V3-closure critical path. OBJ-1 status open->done.
