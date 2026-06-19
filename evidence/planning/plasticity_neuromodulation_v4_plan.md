---
closure_plan:
  id: plasticity_neuromodulation_v4
  generation: v4
  title: "Plasticity-window neuromodulators (V4 OPENING-side roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-17
  scope_claims: [INV-074, MECH-333, MECH-334, ARC-075, MECH-313, MECH-104, MECH-203, SD-037, MECH-205]
  sibling_plans: [object_representation_v4, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. REE owns the CLOSURE side of
    developmental plasticity (INV-074 crystallization necessity, MECH-334 EWC
    write-protect, the MECH-333 closure half) but NOT the OPENING side: there is
    no basal-forebrain ACh-analog gating encoder learning rates, no
    state-conditional plasticity-gain scalar, no PV-interneuron window-closure
    clock, no BDNF-analog duration knob. This plan sequences that opening-side
    cluster. V4 has no experiments yet, so every node carries owner_exq: null and
    the drift checker stays dormant. The value is the readiness_gate per node:
    exactly which V3-era prerequisites (claims/tracks) must land before the V4
    substrate step is honest to build. generation: v4 keeps these nodes OUT of
    the V3 closure percentage. A node graduates to closure-tracked by gaining an
    owner_exq once its first V4 experiment is queued. Hard separation rule
    (from the source framing note): do NOT conflate the opening-side plasticity
    GAIN signal with the content signals MECH-313 (LC-NE tonic noise floor),
    MECH-104 (phasic volatility interrupt), MECH-203 (5-HT state), or SD-037
    (orexin broadcast). Those gate CHOICE / AFFECT, not learning rate.
  nodes:
    - id: "plasticity_neuromodulation_v4:PLW-1"
      title: "Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate"
      phase: 1
      status: blocked
      blocker_class: decision_gate
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [INV-074, MECH-333]
      depends_on: []
      cross_plan_link: []
      blocking_on: "The decision-to-build entry gate is UN-CLEARED (un-passed, not un-built). Two conjunctive conditions must hold before any opening-side substrate (PLW-2 onward) is honest to commission: (1) a CONCRETE V3 problem the opening side would unblock, AND (2) the V3-conservative form (scheduler-driven flag toggling, e.g. the goal-pipeline ARM_D writer-freeze) demonstrably INSUFFICIENT for that problem. As of 2026-06-14 neither is demonstrated -- there is no V3 failure that the existing scheduler-driven InfantCurriculumScheduler phase transitions cannot carry. An ARM_D PASS does NOT clear this gate; it only confirms scheduler-driven toggling is sufficient for the V3 goal-pipeline question (the opposite conclusion). The gate is a TRIGGER condition, not a substrate dependency -- it clears when a concrete V3 problem arises that defeats the conservative form, not by building anything."
      readiness_gate:
        - "CLOSURE side already built: INV-074 (crystallization necessity, universal invariant), MECH-334 (EWC residue write-protect, Kirkpatrick 2017 anchor), MECH-333 closure half -- landed 2026-05-17 in ree-v3/ree_core/policy/gated_policy.py (GatedPolicy.crystallize) + residue/field.py (ResidueField.snapshot_ewc_anchor)"
        - "OPENING side is the gap this plan opens: no ACh-analog plasticity-gain gate, no state-conditional plasticity scalar, no PV-analog closure clock, no BDNF-analog duration knob"
        - "ENTRY GATE before any opening-side substrate is commissioned (from the 2026-06-01 framing note): there must be a concrete V3 problem the opening side unblocks AND the V3-conservative form (scheduler-driven flag toggling, e.g. the goal-pipeline ARM_D writer-freeze) must be demonstrably insufficient for it. An ARM_D PASS does NOT authorise this work."
      last_updated: 2026-06-14
      completion_note: "FRAMING DELIVERABLE COMPLETE; DECISION-TO-BUILD GATE UN-CLEARED (status open->blocked, blocker_class decision_gate, 2026-06-14, IGW PLW-1 reconcile). The asymmetry IS the spine of this plan -- REE has the lock (closure: INV-074/MECH-333/MECH-334) but not the key (opening: ACh/PV/BDNF gain gates) -- and that framing is now durably recorded across this plan doc + the canonical thought note (docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md) + INV-074/MECH-333 governance notes. This node, however, ALSO tracks the decision-to-build entry gate, which is explicitly un-passed (see blocking_on). NOT flipped to done: done would read as 'gate passed / PLW-2+ authorised', which is false. NOT deferred: the generator drops deferred/done entirely, and this is a load-bearing gate worth keeping VISIBLE. blocked + decision_gate (mirrors object_reasoning_abstraction_v4:OBJ-ABS-1's visible-blocked treatment) keeps it out of the ready '(plan reconcile)' lane while the gate stays surfaced as blocked. No claims.yaml edit (framing already lives in plan + thought note; INV-074/MECH-333 carry their own governance notes). Source: docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md."
    - id: "plasticity_neuromodulation_v4:PLW-2"
      title: "Biology grounding lit-pull (Hensch / Bear-Singer / Froemke / Kilgard / Sale)"
      phase: 1
      status: done
      lit_pull_status: done
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-398", "ARC-093"]
      depends_on: ["plasticity_neuromodulation_v4:PLW-1"]
      cross_plan_link: []
      readiness_gate:
        - "Project rule feedback_biology_before_formal_definitions: commission this /lit-pull BEFORE registering any ACh/PV/BDNF substrate claim; the opening-side claims have NO biology lit-pull today"
        - "Anchors named in the framing note: Hensch 2005 (PV/GABA critical-period closure), Bear & Singer 1986 (ACh+NE pairing abolishes plasticity), Froemke 2015 + Kilgard & Merzenich 1998 (nucleus basalis -> cortical remapping), Sale 2007 (GABA reduction reopens CP), Lehmann & Lowel 2008 + Trachtenberg 2015 (windows shift in gain, not binary)"
        - "Do NOT pull pre-emptively: gate the pull on PLW-1's decision-to-build passing first"
      last_updated: 2026-06-17
      completion_note: "DONE 2026-06-17 (/lit-pull, user-directed per the 2026-06-16 V4 tractability audit -- this was the only generation:v4 plan with lit_pull_status:none). Five literature_evidence/v1 entries written under evidence/literature/targeted_review_plasticity_neuromodulation_v4/ grounding the OPENING-side cluster: Kilgard & Merzenich 1998 (Science, NB activity ENABLES adult cortical remapping -> MECH-398 gate exists+necessary, conf 0.80 supports); Froemke/Merzenich/Schreiner 2007 (Nature, cholinergic disinhibition = a TRANSIENT self-rebalancing plasticity window -> MECH-398 mechanism + ARC-093 state-conditional gain, conf 0.78 supports); Bear & Singer 1986 (Nature, combined ACh+NE lesion abolishes OD plasticity, either alone ineffective -> MECH-398 multiplicative ACh x LC-NE composition + the content/gain hard-separation rule, conf 0.79 supports); Hensch 2005 (Nat Rev Neurosci, PV-interneuron maturation sets CP timing + area-specific timings -> MECH-399 closure clock + Q-072 layer-specificity, conf 0.80 supports); Sale 2007 (Nat Neurosci, enrichment reopens adult window via GABA-down/BDNF-up/PNN-down, benzodiazepine rescue -> ARC-093 re-openable continuous gain + MECH-400 duration knob, conf 0.76 MIXED -- weakens binary-irreversible closure). Index rebuilt (1728 lit entries). NOTE the PLW-2 readiness_gate's 'gate the pull on PLW-1 passing first' was OVERRIDDEN by explicit user direction: the grounding pull registers NOTHING by itself (proposal-first, per-child approval) and closing grounding debt before any substrate-claim registration is exactly what feedback_biology_before_formal_definitions requires, independent of PLW-1's decision-to-build status. PLW-1 (decision-to-build gate) remains BLOCKED/un-cleared; the proposed claims stay candidate/v4/substrate_conditional off the V3 closure path regardless. INV-074/MECH-333 already carry strong CLOSURE-side anchors (Fagiolini & Hensch 2000, Kirkpatrick 2017); the OPENING-side ACh-gain mechanism was the ungrounded half -- now grounded. Candidate-claim harvest (MECH-398/ARC-093/MECH-399/MECH-400/Q-072, each with an explicit falsifier) returned proposal-first for per-child user approval before any claims.yaml registration."
    - id: "plasticity_neuromodulation_v4:PLW-3"
      title: "PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate"
      phase: 2
      status: blocked
      blocker_class: v3_substrate
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-398"]
      depends_on: ["plasticity_neuromodulation_v4:PLW-2"]
      cross_plan_link: []
      blocking_on: "MECH-333 open-phase mechanism is planned-but-unbuilt (epistemic_category substrate_conditional 2026-06-10; only the plastic-channel-injection option landed, the F-gradient-attenuation core never exercised -- V3-EXQ-610a..610e all non_contributory). The ACh gate is the state-conditional generalisation of MECH-333's open phase; building it before MECH-333's core exists is premature."
      readiness_gate:
        - "MECH-333 open-phase core (pre-window F-gradient attenuation / PV-analog competitive gating) must land first -- the ACh gate makes that gating STATE-CONDITIONAL rather than scheduler-driven"
        - "Driver inputs must exist as readable scalars: MECH-205 surprise EMA (novelty), SD-032a salience coordinator current_mode (attention focus), drive_level + sustained z_harm_a (arousal) -- all live in V3"
        - "Bear & Singer 1986 pairing: the natural composition is ACh-gate x LC-NE-gate multiplicative; LC-NE lives at MECH-313 (tonic) + MECH-104 (phasic), so the gate reuses existing content signals as INPUTS without collapsing into them"
      last_updated: 2026-06-10
      completion_note: "Scalar in [0,1] multiplying encoder learning rates and residue write magnitudes; distinct from the CHOICE-noise (MECH-313) and AFFECT-broadcast (SD-037) signals. Prose-only today -- proposed as a new claim, not registered here."
    - id: "plasticity_neuromodulation_v4:PLW-4"
      title: "PILLAR B -- state-conditional plasticity-gain architectural commitment"
      phase: 2
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-3, SENT-13]
        requires_welfare_review: false
        forbidden_combinations: [negative_valence_with_replay_without_integration]
        note: "State-conditional plasticity gated high during negative-valence states = trauma-imprinting analog; a combination concern, not harmful alone."
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: ["ARC-093"]
      depends_on: ["plasticity_neuromodulation_v4:PLW-3"]
      cross_plan_link: []
      blocking_on: "Depends on PLW-3 (the ACh gate is the first concrete instance of the scalar this ARC-level claim generalises). No architectural commitment is honest before at least one gate instance exists."
      readiness_gate:
        - "ARC-075 (infant-curriculum plasticity-magnitude asymmetry, candidate, implementation_phase v3) names the architectural need; this node extends it from scheduler-driven phase magnitudes to STATE-driven gain"
        - "Open layer-specificity question must be decided: one global plasticity scalar vs per-substrate scalars (encoder / residue / hippocampal / E2-forward). Biology (Hensch 2005) says layer-specific -- visual/auditory/somatosensory CPs differ in timing"
        - "Must NOT re-derive content signals: the commitment is that plasticity GAIN is separately gated from the content carried by LC-NE/5-HT/orexin (MECH-313/MECH-104/MECH-203/SD-037)"
      last_updated: 2026-06-10
      completion_note: "ARC-level commitment that cortical encoder learning rates and residue write rates are multiplicatively gated by a state-conditional plasticity scalar. Likely an extension of ARC-075 rather than a wholly new ARC -- the layer-specificity decision is the open fork."
    - id: "plasticity_neuromodulation_v4:PLW-5"
      title: "PILLAR C -- PV-interneuron inhibitory-maturation window-closure clock"
      phase: 3
      status: deferred
      blocker_class: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-399"]
      depends_on: ["plasticity_neuromodulation_v4:PLW-3"]
      cross_plan_link: []
      readiness_gate:
        - "Biology-faithful refinement of MECH-333 closure / MECH-334: a time-since-onset accumulator that monotonically lowers the plasticity-gain CEILING, replacing the current binary phase transition (on_phase3_entry crystallize)"
        - "Hensch 2005 + Deidda 2015 anchors (PV/GABA E-I maturation as the causal closure gate) -- already partially cited under MECH-333"
        - "Only worth building after PLW-3/PLW-4 give a continuous gain scalar to put a ceiling on; against a binary flag (MECH-334 today) a continuous clock is redundant"
      last_updated: 2026-06-10
      completion_note: "Deferred behind the gain gate: a closure CLOCK needs a continuous gain variable to clamp. Today's MECH-333/MECH-334 closure is a binary phase transition that the clock would only matter against once gain is continuous."
    - id: "plasticity_neuromodulation_v4:PLW-6"
      title: "PILLAR D -- BDNF-analog trophic window-duration knob (lowest priority)"
      phase: 3
      status: deferred
      blocker_class: deferred
      severity: low
      owner_exq: null
      unblocks_claims: ["MECH-400"]
      depends_on: ["plasticity_neuromodulation_v4:PLW-5"]
      cross_plan_link: []
      readiness_gate:
        - "The duration knob sits ON TOP of the gain knob (PLW-3) and the closure clock (PLW-5); both must exist first"
        - "Huang 1999 anchor (BDNF precociously opens AND closes the CP) -- already cited under MECH-333"
        - "Lowest priority of the cluster; only build if window-duration tuning becomes a measured bottleneck"
      last_updated: 2026-06-10
      completion_note: "Explicitly the lowest-priority pillar in the source sketch: a duration multiplier on top of the gain + closure machinery. Deferred until the gain/closure pillars are validated."
    - id: "plasticity_neuromodulation_v4:PLW-7"
      title: "Layer-specificity adjudication (one global scalar vs per-substrate gates)"
      phase: 2
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: ["Q-072"]
      depends_on: ["plasticity_neuromodulation_v4:PLW-4"]
      cross_plan_link: []
      readiness_gate:
        - "Open question: does plasticity-gain modulate identically across encoder / residue / hippocampal / E2-forward layers, or per-substrate?"
        - "Biology says layer-specific (distinct cortical-area CP timings); REE must decide between one global ACh scalar and per-substrate scalars -- this gates how PLW-3/PLW-4 are parameterised"
        - "Answer_state claim (a question, not an assertion); resolution may be derivational (work through the substrate dependency graph) before any experiment"
      last_updated: 2026-06-10
      completion_note: "The pivotal design fork for the whole cluster: a single global gain scalar is V3-tractable if scoped to ONE substrate; a full per-substrate layer-specific cluster is the V4-budget version. Registered as an open question, not an assertion."
---
# Plasticity-window neuromodulators -- V4 OPENING-side Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the OPENING side of developmental plasticity -- the
basal-forebrain ACh-analog plasticity-gain gate, the state-conditional
plasticity-gain commitment, the PV-interneuron closure clock, and the
BDNF-analog duration knob -- so that if this cluster is ever commissioned it
slots against a registered spine instead of re-deriving the framing. REE already
owns the CLOSURE side (INV-074 / MECH-334 / MECH-333 closure half); this plan is
the missing key to the lock REE already built.

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant. The value is the
**readiness gates** -- for each pillar, exactly which V3-era prerequisites
(claims/tracks) must land before the V4 substrate step is honest to build.

---

## One-line framing

> ACh is essentially a per-stimulus gating signal for which inputs cortex should
> incorporate into long-term representations: without it (nucleus basalis lesion)
> animals still perceive and act, but their cortical representations stop
> updating. REE has built the mechanism that CLOSES the plasticity window
> (crystallization / EWC write-protect) but has nothing that OPENS and gain-gates
> it. This plan sequences that opening-side cluster and pins each pillar's V3
> readiness gate.

---

## The pillars (opening-side cluster)

| Pillar | Node | Claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| (framing) opening-vs-closure | PLW-1 | INV-074 / MECH-333 | V4 (entry gate) | closure side built; decision-to-build gate: V3-conservative flag-toggle demonstrably insufficient |
| (grounding) biology lit-pull | PLW-2 | NEWCLAIM (ACh, state-gain) | cross-cutting | /lit-pull Hensch / Bear-Singer / Froemke / Kilgard / Sale -- gated on PLW-1 |
| A -- ACh-analog gain gate | PLW-3 | MECH-398 | V4 (gated on MECH-333) | MECH-333 open-phase core + readable drivers (MECH-205 / SD-032a / drive) |
| B -- state-conditional gain | PLW-4 | ARC-093 | V4 | extends ARC-075; layer-specificity decided |
| C -- PV closure clock | PLW-5 | MECH-399 | V4 (deferred) | continuous gain scalar exists to clamp (PLW-3) |
| D -- BDNF duration knob | PLW-6 | MECH-400 | V4 (deferred, low) | gain knob + closure clock both exist |
| (fork) layer-specificity | PLW-7 | Q-072 | V4 (open question) | decide global-vs-per-substrate before parameterising A/B |

---

## What this plan deliberately does NOT pull into V3

- **It does NOT conflate the plasticity-GAIN signal with the content signals.**
  MECH-313 (LC-NE tonic noise floor) and MECH-104 (phasic volatility interrupt)
  gate action-selection CHOICE; MECH-203 (5-HT) gates STATE; SD-037 (orexin)
  gates AFFECT broadcast. The opening-side gate multiplies LEARNING RATES. Those
  content signals are INPUTS to the gate (Bear & Singer's ACh+NE pairing), never
  the gate itself. Do not collapse them.
- **It does NOT authorise V4 substrate work from an ARM_D PASS.** The
  goal-pipeline ARM_D writer-freeze is the V3-conservative approximation
  (scheduler-driven flag toggling). An ARM_D PASS means "scheduler-driven
  toggling is sufficient for the V3 goal-pipeline question" -- it does NOT mean
  REE needs a full ACh / plasticity-window system. The two are separate claims at
  separate phases.
- **No substrate code, no experiments, no claim registrations.** Per the source
  framing note's own Status header, this cluster stays unregistered in
  `claims.yaml` until commissioned. This plan registers the ROADMAP only; the
  proposed claims are returned as candidates for the orchestrator, not written
  into the registry here.

---

## Source artefacts

| Artefact | Role |
|---|---|
| docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md | PRIMARY -- the opening-side framing note (canonical paragraph; deliberately unregistered) |
| docs/architecture/critical_period_crystallization.md | INV-074 / MECH-334 closure-side design doc (Nikishin 2023 / Kirkpatrick 2017 synthesis) |
| claims.yaml INV-074 / MECH-333 / MECH-334 / ARC-075 | closure side + the open-phase mechanism (MECH-333 substrate_conditional, unbuilt core) |
| claims.yaml MECH-313 / MECH-104 / MECH-203 / SD-037 | the CONTENT signals this cluster must stay distinct from |
| claims.yaml MECH-205 / SD-032a | candidate driver inputs (surprise EMA novelty; salience-coordinator attention) |
| evidence/planning/goal_pipeline_developmental_window_diagnostic_memo_2026-06-01.md | the ARM_D V3-conservative-form relationship |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap (sibling to
  object_representation_v4). Nodes seeded from the 2026-06-01 framing note and the
  INV-074 / MECH-333 / MECH-334 / ARC-075 closure cluster. Readiness gates pinned
  per pillar. `generation: v4` set so the V3 closure % is unaffected. No
  claims.yaml edits. Four substrate pillars (ACh gain gate, state-conditional
  gain, PV closure clock, BDNF duration knob) plus the layer-specificity open
  question returned as proposed_claims for the orchestrator to assign IDs. The
  decision-to-build gate (PLW-1) and biology grounding (PLW-2) front-load the
  honesty checks before any substrate is registered.
- **2026-06-14** -- IGW PLW-1 reconcile (interactive). PLW-1 was surfaced as a
  ready "(plan reconcile)" item (IGW-20260614-151). It is NOT a flip-to-done: the
  node bundles the opening-vs-closure asymmetry FRAMING (complete -- recorded here
  + in the 2026-06-01 thought note + INV-074/MECH-333 governance notes) with the
  decision-to-build ENTRY GATE, which is explicitly UN-CLEARED (no concrete V3
  problem yet defeats the scheduler-driven conservative form; an ARM_D PASS would
  confirm the conservative form is sufficient, not insufficient). User-confirmed
  disposition: status `open` -> `blocked`, `blocker_class: decision_gate`, with an
  explicit `blocking_on` recording the un-passed gate condition. Chosen over
  `done` (would falsely imply the gate passed / PLW-2+ authorised) and over
  `deferred` (the generator drops deferred/done, hiding a load-bearing gate);
  `blocked` keeps the gate VISIBLE while removing it from the ready plan lane
  (mirrors object_reasoning_abstraction_v4:OBJ-ABS-1). PROMOTES NOTHING; no
  claims.yaml edit (INV-074 stays `substrate_ceiling` on biology per the
  2026-06-13 V3-EXQ-655 STOP; MECH-333 stays candidate/substrate_conditional).
  Node + frontmatter `last_updated` -> 2026-06-14. The gate clears only when a
  concrete V3 problem arises that the conservative form cannot carry -- a future
  trigger, not a build step.
- **2026-06-17** -- PLW-2 biology grounding lit-pull COMPLETE (`/lit-pull`,
  user-directed: the 2026-06-16 V4 tractability audit found this was the only
  `generation:v4` plan with `lit_pull_status: none`). Five literature_evidence/v1
  entries written under `evidence/literature/targeted_review_plasticity_neuromodulation_v4/`
  -- Kilgard & Merzenich 1998, Froemke/Merzenich/Schreiner 2007, Bear & Singer
  1986, Hensch 2005, Sale 2007 -- grounding the opening-side ACh-gain / state-
  conditional-gain / PV-closure-clock / BDNF-duration cluster. PLW-2 status
  `open` -> `done`, `lit_pull_status` `none` -> `done`. The PLW-2 readiness_gate's
  "gate the pull on PLW-1 passing first" line was OVERRIDDEN by explicit user
  direction: the grounding pull registers nothing by itself (proposal-first,
  per-child approval) and `feedback_biology_before_formal_definitions` requires
  the biology to PRECEDE any substrate-claim registration regardless of PLW-1's
  decision-to-build status. PLW-1 stays BLOCKED/un-cleared; the proposed claims
  (MECH-398 / ARC-093 / MECH-399 / MECH-400 / Q-072, each with an explicit
  falsifier) stay candidate/v4/substrate_conditional off the V3 closure path and
  were returned proposal-first for per-child user approval. PROMOTES NOTHING;
  no V3 closure-% change (generation:v4). Index rebuilt (1728 literature
  entries). Node + frontmatter `last_updated` -> 2026-06-17.
