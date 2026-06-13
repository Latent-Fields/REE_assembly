---
closure_plan:
  id: developmental_dmn_v4
  generation: v4
  title: "Play, Private Speech, Externalised DMN, Developmental Compression Ladder (V4 roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [ARC-090, MECH-380, MECH-381, MECH-382, MECH-383, MECH-384, Q-068]
  sibling_plans: [object_representation_v4, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 developmental-curriculum step is honest to build.
    generation: v4 keeps these nodes OUT of the V3 closure percentage (serve.py
    read_closure, generate_closure_snapshot.py, and check_closure_drift.py are
    all generation-aware). A node graduates from roadmap to closure-tracked by
    gaining an owner_exq once its first V4 experiment is queued. The whole
    cluster is substrate_conditional/v4 (except the MECH-384 V3 reduced form),
    so it is correctly invisible to the IGW proposal lane today.
  nodes:
    - id: "developmental_dmn_v4:DMN-1"
      title: "V3 reduced form -- MECH-384 self-narration trace surface (the seed the ladder compresses)"
      phase: 1
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-384, Q-068]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "MECH-384 is the ONLY V3-compatible instantiation: implementation_phase v3, epistemic_category substrate_coherence; a debug/observability trace, not new substrate"
        - "Fields largely re-expose state REE already computes via MECH-094 (goal label, sensed gradient, active prediction, uncertainty, candidate action+reason, expected consequence, affective pressure, conflict flag, commitment threshold, stop condition)"
        - "POST-GREEN-BOARD + OFF the V3 critical path: build only if it helps REE-v3 pass existing tests more cleanly (intake scope guardrail)"
      last_updated: 2026-06-10
      completion_note: "This is the externalised 'private speech' surface in its V3 reduced form, before any developmental compression. simulation_or_commitment + self_reference_frame are its hooks for the Q-068 graded-vocabulary question. It is the only node here that could land in V3; everything below depends on a developmental curriculum and a control-driving narration surface that V3 lacks."
    - id: "developmental_dmn_v4:DMN-2"
      title: "Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [Q-068]
      depends_on: ["developmental_dmn_v4:DMN-1"]
      cross_plan_link: []
      readiness_gate:
        - "V3 already enforces the coarse boundary: MECH-094 simulation/commit write-profiles + MECH-061 commit-boundary error reclassification"
        - "Q-068 epistemic_category set EXPLICITLY substrate_conditional (overrides open_question->answer_state) so narrow_open_question does NOT fire -- DO NOT queue a V3 experiment against it"
        - "DECISION the fork forces: is the finer {simulated, rehearsed, intended, committed, acted} vocabulary + self_reference_frame {first_person, system_state, third_person_model} worth making first-class, or is MECH-094 + MECH-061 sufficient?"
      last_updated: 2026-06-10
      completion_note: "This is the foundational representational decision for the cluster: the graded vocabulary is the substrate that MECH-382 (distancing operator) and MECH-380 (private-speech control) both presuppose. Answering it is V4 -- it awaits the ARC-090 self-narration surface that can actually act on the distinction, surfaced in reduced form by DMN-1's MECH-384 trace."
    - id: "developmental_dmn_v4:DMN-3"
      title: "PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds"
      phase: 2
      status: blocked
      blocker_class: v3_substrate
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-090]
      depends_on: ["developmental_dmn_v4:DMN-2"]
      cross_plan_link:
        - "object_representation_v4:OBJ-2"
      blocking_on: "The V3 play cluster (ARC-049/050, MECH-194-199, INV-058/060) is substrate_blocked: no play_frame_tag, no synthetic-signal seeding, no bilateral frame in ree-v3 code. ARC-090 also needs a temporary-as-if-world surface that does not exist. ARC-049 itself flags full bilateral frame as a V4 multi-agent requirement."
      readiness_gate:
        - "V3 play substrate must land first: ARC-049 play_frame_tag in LatentState (L2 continuous signal), MECH-194 synthetic z_goal/z_harm seeding with raised harm-escalation threshold, INV-059 bilateral frame-drop trigger"
        - "Internal-DMN end-state present as the compression target: ARC-014 (safe imagination without commitment) + MECH-029 (reflective/moral evaluation of replay)"
        - "Object-file substrate for 'this block is a house' role-substitution: cross-plan dependency on object_representation_v4 PILLAR 1 (token-instance permanence, OBJ-2)"
      last_updated: 2026-06-10
      completion_note: "ARC-090 asserts that DMN functions (self-reference, autobiographical memory, social imagination, future simulation, counterfactual thought, narrative construction) first run EXTERNALLY in play before compressing into the internal DMN. NEW relative to ARC-014/MECH-029 (which frame only the END-STATE) and the play cluster (which frames bounded-low-stakes mechanics, not play-AS-externalised-DMN). Design-only today."
    - id: "developmental_dmn_v4:DMN-4"
      title: "PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder"
      phase: 3
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-380]
      depends_on: ["developmental_dmn_v4:DMN-3"]
      cross_plan_link: []
      blocking_on: "Needs a self-narration control surface that can actually DRIVE arbitration -- V3 has nothing beyond the proposed MECH-384 trace, which is read-only observability, not a control input."
      readiness_gate:
        - "INV-034 goal-maintenance target (the thing private speech regulates) must be the live arbitration target"
        - "MECH-029 internal evaluative arm present as the compression endpoint (overt self-regulation -> inner speech)"
        - "DISTINCT from ARC-077/MECH-337 (caregiver-scaffolded candidate-RULE CONTENT via Vygotsky ZPD): MECH-380 scaffolds self-directed CONTROL, not what-to-believe -- keep the two ladders separate when both are built"
      last_updated: 2026-06-10
      completion_note: "MECH-380: private speech is a temporary control surface that makes cognition inspectable before compression (other-regulation -> overt self-regulation -> inner speech -> compressed control). The MECH-384 trace (DMN-1) is its read-only V3 ancestor; the V4 step is making that surface drive attention/action/affect/sequencing arbitration."
    - id: "developmental_dmn_v4:DMN-5"
      title: "PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum"
      phase: 3
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-381]
      depends_on:
        - "developmental_dmn_v4:DMN-3"
        - "developmental_dmn_v4:DMN-4"
      cross_plan_link: []
      blocking_on: "Requires a staged developmental curriculum (sensorimotor -> play -> self-narration -> internal control -> mature arbitration) that V3 does not run, plus the DMN-3/DMN-4 external scaffolds to compress in the first place."
      readiness_gate:
        - "INV-060 + MECH-197 play-type progression (sensorimotor->constructive->pretend->rule-based->cooperative) substrate, the WITHIN-play axis this ladder runs orthogonal to"
        - "MECH-380 private-speech control surface (DMN-4) -- rung 3 of the ladder -- must exist to compress"
        - "ARC-090 externalised-DMN play scaffold (DMN-3) -- rung 2 -- must exist as the thing that compresses into internal simulation (rung 4)"
      last_updated: 2026-06-10
      completion_note: "MECH-381 is the orthogonal externalise->internalise COMPRESSION axis (rungs: sensorimotor -> play -> private speech -> inner speech -> mature arbitration), DISTINCT from INV-060/MECH-197's within-play type sequence. It is the mechanism by which DMN-3 and DMN-4's external scaffolds become internal control; it cannot be built until those scaffolds exist."
    - id: "developmental_dmn_v4:DMN-6"
      title: "Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move"
      phase: 4
      status: blocked
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-382]
      depends_on:
        - "developmental_dmn_v4:DMN-2"
        - "developmental_dmn_v4:DMN-4"
      cross_plan_link: []
      blocking_on: "Needs a self-narration/reframe control surface to operate on (a richer form of the MECH-384 trace), and the DMN-2 self_reference_frame vocabulary to reframe between. The intake notes a cheap V3 variant is conceivable, but the arbitration-altering form is V4."
      readiness_gate:
        - "ARC-005 precision-routing control plane (the thing the reframe acts through) live"
        - "DMN-2 self_reference_frame {first_person, system_state, third_person_model} vocabulary decided"
        - "INV-061 frame-confusion etiology present as the protective target (distancing as a candidate operator against self-referential collapse)"
      last_updated: 2026-06-10
      completion_note: "MECH-382 (Kross/Moser third-person self-talk): reframing a sticky first-person state into a model-like system-state reduces self-referential collapse and routes the state into model-based inspection. Not cosmetic -- it alters arbitration via the ARC-005 control plane. Depends on the self-reference-frame vocabulary (DMN-2) and a reframe-capable surface (DMN-4)."
    - id: "developmental_dmn_v4:DMN-7"
      title: "Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search"
      phase: 4
      status: blocked
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-383]
      depends_on: ["developmental_dmn_v4:DMN-4"]
      cross_plan_link: []
      blocking_on: "Needs a label-generation surface coupled into precision routing -- the MECH-380 private-speech/narration surface (DMN-4) must exist to generate the self-directed labels that then act as control inputs."
      readiness_gate:
        - "ARC-005 precision-routing control plane + the distributed precision-selection cluster (MECH-251/MECH-261) live -- labels ride on these, no parallel attention module is implied"
        - "MECH-029 internal evaluative arm (labels feed the reflective control loop)"
        - "CROSS-REF the attention=distributed-precision-selection map: MECH-383 adds only the specific claim that self-generated LABELS are a control input to precision, not a new attention module"
      last_updated: 2026-06-10
      completion_note: "MECH-383 (Lupyan/Swingley visual search): a self-directed label ('food-gradient', 'danger-gradient', 'blocked-goal') is a top-down tuning signal that biases perceptual search, not a post-perceptual report. DISTINCT from the existing precision cluster: it is the claim that self-generated labels are a control INPUT. Depends on the narration surface (DMN-4) to produce labels."
    - id: "developmental_dmn_v4:DMN-8"
      title: "Biology grounding completion (Vygotsky private speech, DMN, label-as-control, self-distancing lit-pulls)"
      phase: 2
      status: deferred
      blocker_class: lit_gap
      lit_pull_status: none
      severity: medium
      owner_exq: null
      unblocks_claims: [ARC-090, MECH-380, MECH-383]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Current state: architectural-analogy anchors only (Vygotsky private speech; Lupyan/Swingley labels-alter-search; Kross/Moser third-person self-talk; DMN self-reflection/simulation literature) -- recorded as anchors, NOT a citable out-of-domain dataset (no research_anchor claim)"
        - "Per project rule feedback_biology_before_formal_definitions: each pillar that instantiates a formal developmental concept needs a biology lit-pull BEFORE its substrate is built"
        - "Schedule per-pillar: private-speech/inner-speech (MECH-380/381), label-as-perceptual-control (MECH-383), self-distancing (MECH-382) -- follow when their pillars are scheduled"
      last_updated: 2026-06-10
      completion_note: "The cluster's evidence anchors are textbook-level psychology/neuroscience supporting a strong architectural analogy, not citable mechanism evidence. This node tracks closing that grounding debt before each pillar's substrate is built; deferred (not in_progress) because no pull is active yet and the pillars themselves are upstream-blocked."
---
# Play, Private Speech, Externalised DMN -- V4 Developmental Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the 2026-06-08 externalised-DMN intake -- play as externalised
default-mode operation (ARC-090), private speech as an external cognitive-control
surface (MECH-380), the externalise-then-internalise compression ladder (MECH-381),
the distancing operator (MECH-382), labels-as-top-down-control (MECH-383), the
graded action-status vocabulary question (Q-068), and the single V3-compatible
reduced form (MECH-384) -- so V4 developmental-curriculum work slots in against a
registered spine with pinned V3 readiness gates.

This plan is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant against them. The
value is the **readiness gates** -- for each pillar, exactly which V3-era
prerequisites (claims/tracks) must land before the V4 substrate step is honest to
build. The whole cluster is `substrate_conditional` / `implementation_phase: v4`
(except MECH-384, which is the V3 reduced form), so it is correctly invisible to
the IGW proposal lane today: a V3 probe against any pillar would be vacuous.

---

## One-line framing

> The internal default-mode network -- self-reference, memory, future simulation,
> counterfactual thought, narrative construction -- is the END-STATE (ARC-014 safe
> imagination, MECH-029 reflective evaluation). This cluster asserts those
> functions first run EXTERNALLY in development: pushed outward into play objects,
> roles, movement, and spoken self-narration, then compressed inward over a
> developmental ladder. REE already owns the end-state and the bounded-play
> mechanics; what is new is play-AS-externalised-DMN and the externalise->internalise
> compression axis. This plan sequences those pillars and pins their V3 gates.

---

## The pillars (one developmental primitive, several surfaces)

| Node | Pillar | Claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| DMN-1 | V3 reduced form (self-narration trace) | MECH-384 | V3 (post-green-board, optional) | MECH-094 state already computed; surface it as a coherent trace |
| DMN-2 | graded action-status + frame vocabulary | Q-068 | V4 (first decision) | MECH-094 + MECH-061 coarse boundary live; decide if finer vocabulary is first-class |
| DMN-3 | externalised-DMN play scaffold | ARC-090 | V4 | V3 play cluster (ARC-049/050, MECH-194-199) + ARC-014/MECH-029 + object-file (OBJ-2) |
| DMN-4 | private speech as control surface | MECH-380 | V4 | INV-034 goal-maintenance + MECH-029; keep separate from ARC-077/MECH-337 content-scaffold |
| DMN-5 | externalise->internalise compression ladder | MECH-381 | V4 | INV-060/MECH-197 play-type axis + DMN-3 + DMN-4 scaffolds to compress |
| DMN-6 | distancing operator | MECH-382 | V4 (cheap V3 variant possible) | ARC-005 control plane + DMN-2 frame vocabulary + INV-061 |
| DMN-7 | labels as perceptual control | MECH-383 | V4 | ARC-005 + MECH-251/261 precision cluster + DMN-4 narration surface |
| DMN-8 | biology grounding debt | ARC-090/MECH-380/383 | cross-cutting | per-pillar lit-pulls (anchors only today) |

---

## What this plan deliberately does NOT pull into V3

- **Only MECH-384 is V3.** It is a read-only observability trace
  (`epistemic_category: substrate_coherence`, `implementation_phase: v3`) and is
  POST-GREEN-BOARD + off the critical path -- build only if it helps REE-v3 pass
  existing tests more cleanly. No other node touches V3.
- **The play cluster is the upstream blocker, not part of this roadmap.** ARC-049/050
  and MECH-194-199 are themselves substrate_blocked in V3 (no `play_frame_tag`, no
  synthetic-signal seeding, no bilateral frame). Per project memory, those claims are
  IGW-suppressed by their `substrate_conditional` category; this roadmap consumes them
  as a gate (DMN-3) and does not try to queue them.
- **No graded-vocabulary experiment.** Q-068 is explicitly `substrate_conditional`
  so `narrow_open_question` does NOT fire; it is a V4 decision awaiting the ARC-090
  narration surface, not a V3-tractable question to narrow by experiment.
- **No new substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/externalised_dmn_play_private_speech.md](../../docs/architecture/externalised_dmn_play_private_speech.md) | home doc: the cluster + V3/V4 boundary |
| docs/thoughts/2026-06-08_play_private_speech_externalised_dmn.md | original intake the cluster was reaped from |
| claims.yaml ARC-090 / MECH-380 / MECH-381 / MECH-382 / MECH-383 / Q-068 | the V4 pillar claims (substrate_conditional, v4) |
| claims.yaml MECH-384 | the single V3 reduced-form trace (substrate_coherence, v3) |
| claims.yaml ARC-049/050 + MECH-194-199 + INV-058/060 | the V3 play cluster gating DMN-3 (substrate_blocked) |
| evidence/planning/object_representation_v4_plan.md | sibling V4 roadmap; OBJ-2 token-instance permanence is the cross-plan gate for DMN-3 |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap, sibling to
  `object_representation_v4`. Nodes seeded from the 2026-06-08 externalised-DMN
  intake (ARC-090, MECH-380/381/382/383, Q-068, MECH-384). Readiness gates pinned
  per pillar. DMN-3 carries a cross_plan_link to `object_representation_v4:OBJ-2`
  (the 'this block is a house' role-substitution needs token-instance object-files).
  `generation: v4` set so the V3 closure % is unaffected. No claims.yaml edits.
  Cluster is mostly reaped -- all seven claims already registered; no new claims
  proposed.
