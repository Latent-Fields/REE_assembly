---
closure_plan:
  id: object_reasoning_abstraction_v4
  generation: v4
  title: "Object-reasoning abstraction (V4 roadmap: theta-packaged units, options, chunks, relational maps)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [SD-040, MECH-296, MECH-297, SD-045, SD-042, MECH-299, MECH-300, Q-057]
  sibling_plans: [object_representation, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims / substrate
    tracks) that must land before that V4 abstraction step is honest to build.
    This plan is the "more abstraction of object reasoning" cluster: it sits
    ABOVE the object_representation pillar plan (which decides what an object
    IS -- type / token / anchor) and asks the next-level question: once the
    substrate vocabulary can name reusable units (chunks, types, options),
    how do the packaging machinery (theta), the retrieval operators
    (prototype-readout, type-V_s gating), and the cognitive-map traversal
    scale to operate AT the active abstraction level rather than at the fixed
    atomic level V3 is locked to. generation: v4 keeps these nodes OUT of the
    V3 closure percentage (serve.py read_closure, generate_closure_snapshot.py,
    check_closure_drift.py are all generation-aware). A node graduates from
    roadmap to closure-tracked by gaining an owner_exq once its first V4
    experiment is queued.
  nodes:
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-1"
      title: "Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-299, MECH-300]
      depends_on: []
      cross_plan_link: ["object_representation:OBJ-1"]
      readiness_gate:
        - "V3 substrate vocabulary is FIXED at z_world + atomic actions (per MECH-299 notes: no second granularity exists for theta to scale into)"
        - "At least one reusable-unit substrate must land before the abstraction-scaling claims become testable: SD-045 action-chunk cache, OR SD-040/MECH-296 type-instance match, OR SD-042 option library"
        - "DECISION the fork forces: which reusable-unit substrate is built FIRST (chunk vs type vs option) -- that choice determines the first non-atomic granularity theta and the cognitive map can traverse"
      last_updated: 2026-06-10
      completion_note: "This node is the entry condition for the whole plan: every downstream abstraction claim (MECH-299/300 packaging, MECH-296/297 readout/gating) is meaningful only once the substrate stack carries a unit ABOVE the atomic action. V3 cannot pull these forward because there is nothing for the abstraction to scale into. Not a missing flag -- a missing substrate layer."
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-2"
      title: "PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [SD-045]
      depends_on: ["object_reasoning_abstraction_v4:OBJ-ABS-1"]
      cross_plan_link: []
      blocking_on: "Gated on ARC-021 three-loop framework (dorsolateral-loop slot) + SD-004 action-object substrate (the sequences chunks are made of) + MECH-290 backward credit sweep (chunk reinforcement). All three exist as claims; SD-045 is the cache that sits in their DLS slot."
      readiness_gate:
        - "ARC-021 three-BG-loop framework present (chunk cache lives in the dorsolateral-loop slot)"
        - "SD-004 action_object substrate (chunks are cached sequences of this) + MECH-290 backward credit sweep (updates chunk reinforcement) landed"
        - "V3 PULL-FORWARD TRIGGER (per SD-045 notes): if EXQ-495 V3-full-completion-gate or successors surface monostrategy persistence the planner-only architecture cannot escape, SD-045 is the highest-priority extension to pull into late-V3 (missing-habit-cache hypothesis for behavioural rigidity)"
      last_updated: 2026-06-10
      completion_note: "SD-045 is the lightest and most likely-first reusable-unit substrate, and the only one with an explicit V3 pull-forward condition (monostrategy / OCD-ritual modelling via SD-033/SD-034). It is the natural first granularity for MECH-299 theta-packaging and MECH-300 chunk-graph traversal to test against."
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-3"
      title: "PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world"
      phase: 2
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [SD-040]
      depends_on: ["object_reasoning_abstraction_v4:OBJ-ABS-1"]
      cross_plan_link: ["object_representation:OBJ-1"]
      blocking_on: "Gated on MECH-269 AnchorSet substrate (the pool getting a new type-key projection) + SD-039 anchor payload schema (the entry SD-040 adds a field to). Both V3-live; SD-040 extends them, it does not replace them."
      readiness_gate:
        - "MECH-269 AnchorSet / V_s substrate live in V3 (SD-040 adds a type-key projection alongside the existing z_world payload)"
        - "SD-039 anchor payload schema present (SD-040 populates a new type-key field on the entry)"
        - "BEHAVIOURAL PRECONDITION (per SD-040 notes): a multi-instance environment with several distinct instances sharing one type-signature -- V3 gridworld with discrete entity types lacks the instance-variability to surface the type-vs-instance dissociation; V4 environment richness is required"
      last_updated: 2026-06-10
      completion_note: "SD-040 is the type-vs-token-vs-anchor fork's TYPE arm at the abstraction level: a regularity-extracted type-encoder mirroring the EC->CA1 monosynaptic pathway, distinct from the instance-encoder. It feeds the MECH-296 prototype-readout and MECH-297 type-V_s gating. Note this is type-LEVEL identity (apples), distinct from the object_representation plan's token-instance object-file (this apple)."
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-4"
      title: "PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-296, MECH-297]
      depends_on: ["object_reasoning_abstraction_v4:OBJ-ABS-3"]
      cross_plan_link: []
      blocking_on: "Gated on SD-040 type-encoder (OBJ-ABS-3) -- the operators consume type-keys that do not exist until SD-040 lands. MECH-296 additionally depends on MECH-285 sleep-replay sampler for the offline refinement pass; MECH-297 extends MECH-269's per-stream/per-region V_s with a per-type dimension."
      readiness_gate:
        - "SD-040 type-keyed AnchorSet entries exist (MECH-296 softmax-attention readout has nothing to match against otherwise)"
        - "MECH-285 priority-weighted sleep-replay sampler live (drives MECH-296's offline type-anchor-pool refinement pass)"
        - "MECH-269 per-stream + per-region V_s confirmed live (MECH-297 adds the per-type V_s dimension on top -- could alternatively register as MECH-269 Phase 4 per its own notes)"
      last_updated: 2026-06-10
      completion_note: "MECH-296 gives moment-to-moment type recognition (waking) + sleep-consolidation refinement; MECH-297 lets the proposer/E3 gate stream contributions by combined per-stream AND per-type V_s, so a novel instance of a known type (low per-type V_s) fires the MECH-269 probe channel. These are the retrieval/gating operators that make the SD-040 type substrate behaviourally load-bearing."
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-5"
      title: "PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [SD-042]
      depends_on: ["object_reasoning_abstraction_v4:OBJ-ABS-1"]
      cross_plan_link: ["goal_pipeline"]
      blocking_on: "Gated on ARC-021 three-loop framework (where option arbitration sits) + SD-004 continuous action substrate (which options refine into an indexable library) + a V4 environment with tool use / social coordination / hierarchical task structure (gridworld is too simple to validate options per SD-042 notes)."
      readiness_gate:
        - "ARC-021 three-BG-loop framework present (option arbitration slot)"
        - "SD-004 continuous action_object_decoder live (SD-042 is the indexable-library refinement of it, not a replacement)"
        - "ENVIRONMENT PRECONDITION (per SD-042 notes): V4 environment with tool use, social coordination, OR hierarchical task structure -- gridworld is definitively too simple to validate options"
        - "MECH-292 ghost-goal bank present (option-initiation-match becomes an additional ghost-probe seeding key once the library exists)"
      last_updated: 2026-06-10
      completion_note: "SD-042 is the richest reusable-unit substrate -- a discrete codebook of Sutton-Precup-Singh options, distinct from SD-004's continuous decoder. It is the option-graph that MECH-300 traverses and the option-invocation unit MECH-299 packages into theta. Definitively V4: it needs an environment with genuine hierarchical structure to be non-vacuous, which is why it is the most environment-gated pillar in this plan."
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-6"
      title: "PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)"
      phase: 4
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-299, MECH-300]
      depends_on:
        - "object_reasoning_abstraction_v4:OBJ-ABS-2"
        - "object_reasoning_abstraction_v4:OBJ-ABS-3"
        - "object_reasoning_abstraction_v4:OBJ-ABS-5"
      cross_plan_link: []
      blocking_on: "Gated on AT LEAST ONE reusable-unit substrate landing (SD-045 chunks OR SD-040 types OR SD-042 options). The claims are refinements of MECH-089 theta-gamma nesting and depend on MECH-269 for the cognitive-map nodes; both are V3-live, but the SCALING prediction is untestable until a non-atomic granularity exists."
      readiness_gate:
        - "MECH-089 theta-gamma packaging primitive + MECH-294 theta-burst-as-E3-packet sibling confirmed live in V3"
        - "MECH-269 anchor pool live (defines the cognitive-map nodes MECH-300 traverses)"
        - "At least one of SD-045 / SD-040+MECH-296 / SD-042 landed (supplies the non-atomic unit -- without it MECH-299's 'smallest reusable item' is just the atomic action and the claim is vacuous)"
        - "LONGITUDINAL DESIGN (per MECH-299 notes): measure theta-sequence content before vs after the agent acquires a chunked/typed/optioned skill; prediction = gamma-count per theta cycle stays constant while unit granularity scales"
      last_updated: 2026-06-10
      completion_note: "MECH-299 (content axis: what unit goes in the theta packet) and MECH-300 (map axis: what graph is being traversed) are the capstone of this plan -- they assert the packaging machinery is FIXED while granularity scales with the substrate vocabulary. They cannot be the first thing built: they are the validation that the lower pillars (chunks/types/options) actually re-grain the theta-packet, not separate substrates."
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-7"
      title: "Developmental sparsification policy for the abstraction substrates (Q-057): deletion vs down-weighting vs gating vs residue-tag de-authorization"
      phase: 4
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: [Q-057]
      depends_on:
        - "object_reasoning_abstraction_v4:OBJ-ABS-3"
        - "object_reasoning_abstraction_v4:OBJ-ABS-5"
      cross_plan_link: []
      blocking_on: "Q-057 is epistemic_category: substrate_conditional -- a V4-parked question awaiting an upstream developmental substrate (ARC-019 / MECH-362 CA3 developmental intake). DO NOT queue a V3 experiment against it (per its notes). It becomes answerable only once a type/option/anchor pool exists to over-connect then sparsify."
      readiness_gate:
        - "ARC-019 + MECH-362 developmental-pruning substrate present (Q-057's depends_on)"
        - "A populated abstraction pool exists to sparsify (SD-040 type-anchors OR SD-042 option library) -- there is nothing to prune in an atomic-only substrate"
        - "Sub-question routing (per Q-057 notes): (1) does V3 cue-authority weakness reflect immature single-cue authority? (2) can offline integration act as pruning/contextualisation, not merely consolidation? (3) what developmental gates should precede a trace influencing action release?"
      last_updated: 2026-06-10
      completion_note: "Q-057 asks whether the abstraction substrates need an early over-connected exploratory phase distinct from a mature sparse one, and how sparsification is modelled. Deferred (not merely blocked): it is a design question to resolve once the substrates it would sparsify exist, and is explicitly tagged substrate_conditional so the narrow_open_question recommendation stays suppressed."
    - id: "object_reasoning_abstraction_v4:OBJ-ABS-8"
      title: "Biology grounding completion for the abstraction substrates (chunking / options / type-prototype / theta-scaling lit-pulls)"
      phase: 2
      status: in_progress
      severity: medium
      owner_exq: null
      unblocks_claims: [SD-040, SD-045, SD-042]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "L-type type-prototype substrate (Quiroga 2005, Schapiro 2016/2017, Constantinescu 2016, Hennies 2017) -- DONE: targeted_review_hpc_type_prototype_substrate (grounds SD-040 / MECH-296 / MECH-297)"
        - "L-action action-policy decomposition (Graybiel 2008, Daw 2005, Dolan & Dayan 2013, Botvinick 2009) -- DONE: targeted_review_action_policy_decomposition (grounds SD-045 / SD-042)"
        - "L-theta theta-abstraction-scaling (Gupta 2012, Bellmund 2018, Constantinescu 2016) -- DONE: targeted_review_theta_abstraction_scaling (grounds MECH-299 / MECH-300)"
        - "REMAINING DEBT: biology-before-formal-definitions check on any V4 SD/MECH that operationalises options as a formal Sutton-Precup-Singh construct before its substrate is built (per project rule feedback_biology_before_formal_definitions)"
      last_updated: 2026-06-10
      completion_note: "Unlike the object_representation pillar plan, the abstraction cluster was registered WITH its lit-pulls (three targeted reviews dated 2026-04-28). This node tracks the remaining biology-before-formal-definitions discipline for the options pillar specifically (SD-042 imports a formal RL construct) and confirms the existing grounding is sufficient before substrate build."
---
# Object-Reasoning Abstraction -- V4 Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the abstraction layer that sits ABOVE the object-representation
pillars -- once the substrate vocabulary can name reusable units (action chunks,
category types, options), how do the packaging machinery (theta), the retrieval
operators (prototype-readout, type-V_s gating), and the cognitive-map traversal
scale to operate at the ACTIVE abstraction level rather than at the fixed atomic
level V3 is locked to.

This is the user-named "more abstraction of object reasoning" cluster. It is a
*forward roadmap*, not a closure map: V4 has no experiments yet, so nodes carry
no `owner_exq` and the drift checker stays dormant against them. The value is the
**readiness gates** -- for each abstraction substrate, exactly which V3-era
prerequisites (claims / tracks / environment conditions) must land before the V4
step is honest to build.

---

## One-line framing

> V3 packages experience at one granularity -- the atomic action and the z_world
> point -- because that is the only vocabulary its substrate has. The abstraction
> claims (MECH-299/300) assert the packaging machinery is FIXED and the
> granularity SCALES with the substrate vocabulary: build a chunk cache (SD-045),
> a type-encoder (SD-040), or an option library (SD-042), and theta re-grains to
> package chunks / types / options, and the cognitive map re-grains to traverse
> chunk- / type- / option-graphs. The whole plan is gated on one fork: there must
> be a unit ABOVE the atomic action for the abstraction to scale into.

---

## The abstraction substrates (ordered by readiness, not by phase number)

| Pillar | Node | Claim(s) | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| (fork) vocabulary expansion | OBJ-ABS-1 | MECH-299/300 (entry) | V4 (first decision) | one reusable-unit substrate must land; pick chunk vs type vs option first |
| A -- action-chunk cache | OBJ-ABS-2 | SD-045 | V3-pull-forward / V4 | ARC-021 DLS slot + SD-004 + MECH-290; monostrategy trigger pulls it to late-V3 |
| B -- type-encoder | OBJ-ABS-3 | SD-040 | V4 | MECH-269 + SD-039 live; needs multi-instance environment |
| B -- prototype-readout + type-V_s | OBJ-ABS-4 | MECH-296, MECH-297 | V4 | SD-040 + MECH-285 sleep sampler + MECH-269 V_s |
| C -- option library | OBJ-ABS-5 | SD-042 | V4 | ARC-021 + SD-004 + hierarchical/tool/social environment |
| D -- theta packaging + map traversal | OBJ-ABS-6 | MECH-299, MECH-300 | V4 (capstone) | MECH-089/294 + MECH-269 + >=1 unit substrate |
| developmental sparsification | OBJ-ABS-7 | Q-057 | V4/V5 (deferred) | ARC-019 + MECH-362; a populated pool to sparsify |
| grounding debt | OBJ-ABS-8 | SD-040/045/042 | cross-cutting | three lit-pulls DONE 2026-04-28; options-formalism check remains |

---

## What this plan deliberately does NOT pull into V3

- **No reusable-unit substrate is built in V3 unless its explicit pull-forward
  trigger fires.** Only SD-045 has one: a confirmed monostrategy-persistence /
  OCD-ritual finding (via EXQ-495 successors or SD-033 OCD-axis work) that the
  planner-only architecture cannot escape. Absent that trigger, all of
  SD-040/042/045 stay V4. The chunk-cache pull-forward is owned jointly with the
  monostrategy / `goal_pipeline` work; this roadmap does not initiate it.
- **MECH-299/300 are NOT V3-tractable.** V3's vocabulary is fixed at z_world +
  atomic actions, so there is no second granularity for theta to scale into and
  no chunk-/type-/option-graph for the cognitive map to traverse. A V3 probe
  would be vacuous.
- **Q-057 is substrate_conditional and parked.** It awaits the ARC-019 / MECH-362
  developmental substrate AND a populated abstraction pool to sparsify. Do not
  queue a V3 experiment against it; the narrow_open_question recommendation is
  intentionally suppressed.
- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour. The first real substrate step (whichever
  reusable-unit substrate is chosen at OBJ-ABS-1) is V4 and must not enter the
  V3 closure %.

---

## Relationship to the object_representation pillar plan

This plan is the **abstraction layer above** the `object_representation` plan, not
a duplicate of it:

- `object_representation` decides what an object IS at the representational level
  -- the type-vs-token-vs-anchor fork and the four pillars (permanence, self,
  tools, others). Its TYPE arm is type-LEVEL identity.
- This plan takes the reusable-unit vocabulary as given and asks how the
  PACKAGING, RETRIEVAL, and TRAVERSAL machinery re-grains to operate at that
  vocabulary's level. SD-040 here is the type-encoder feeding prototype-readout
  and type-V_s gating; the object_representation plan's token-instance object-file
  is a different (token-level) construct. The two share OBJ-1 / OBJ-ABS-1 as a
  cross-plan link because both depend on the same vocabulary-expansion decision.

---

## Source artefacts

| Artefact | Role |
|---|---|
| docs/thoughts/2026-04-28_action_object_type_abstraction.md | SD-040 / MECH-296 / MECH-297 type-prototype seeds |
| docs/thoughts/2026-04-28_action_policy_and_multi_goal.md | SD-042 / SD-045 / MECH-299 / MECH-300 action-policy + theta-scaling seeds |
| evidence/literature/targeted_review_hpc_type_prototype_substrate/ | biology grounding for the type pillar (Quiroga 2005, Schapiro 2016/17, Constantinescu 2016, Hennies 2017) |
| evidence/literature/targeted_review_action_policy_decomposition/ | biology grounding for chunks + options (Graybiel 2008, Daw 2005, Dolan & Dayan 2013, Botvinick 2009) |
| evidence/literature/targeted_review_theta_abstraction_scaling/ | biology grounding for theta scaling (Gupta 2012, Bellmund 2018, Constantinescu 2016) |
| docs/architecture/developmental_pruning_and_sparse_memory_cognifold.md | Q-057 developmental sparsification anchor (CA3 intake / MECH-362) |
| claims.yaml SD-040 / SD-042 / SD-045 / MECH-296 / MECH-297 / MECH-299 / MECH-300 / Q-057 | the abstraction cluster (all implementation_phase: v4) |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap. Nodes seeded from the
  2026-04-28 action/object/theta abstraction cluster (SD-040/042/045,
  MECH-296/297/299/300, Q-057). Readiness gates pinned per substrate. The entry
  fork (OBJ-ABS-1) records that V3's atomic-only vocabulary gives nothing for the
  abstraction to scale into, making vocabulary expansion the gating decision.
  SD-045's monostrategy pull-forward condition noted as the only V3-entry path.
  `generation: v4` set so the V3 closure % is unaffected. No claims.yaml edits.
