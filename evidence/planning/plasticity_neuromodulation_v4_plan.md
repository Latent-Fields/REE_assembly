---
closure_plan:
  id: plasticity_neuromodulation_v4
  generation: v4
  title: "Plasticity-window neuromodulators (V4 OPENING-side roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-10
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
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [INV-074, MECH-333]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "CLOSURE side already built: INV-074 (crystallization necessity, universal invariant), MECH-334 (EWC residue write-protect, Kirkpatrick 2017 anchor), MECH-333 closure half -- landed 2026-05-17 in ree-v3/ree_core/policy/gated_policy.py (GatedPolicy.crystallize) + residue/field.py (ResidueField.snapshot_ewc_anchor)"
        - "OPENING side is the gap this plan opens: no ACh-analog plasticity-gain gate, no state-conditional plasticity scalar, no PV-analog closure clock, no BDNF-analog duration knob"
        - "ENTRY GATE before any opening-side substrate is commissioned (from the 2026-06-01 framing note): there must be a concrete V3 problem the opening side unblocks AND the V3-conservative form (scheduler-driven flag toggling, e.g. the goal-pipeline ARM_D writer-freeze) must be demonstrably insufficient for it. An ARM_D PASS does NOT authorise this work."
      last_updated: 2026-06-10
      completion_note: "The asymmetry is the spine of this plan: REE has the lock but not the key. This node tracks the decision-to-build gate, not a substrate. Source: docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md."
    - id: "plasticity_neuromodulation_v4:PLW-2"
      title: "Biology grounding lit-pull (Hensch / Bear-Singer / Froemke / Kilgard / Sale)"
      phase: 1
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:ach_analog_plasticity_gate", "NEWCLAIM:state_conditional_plasticity_gain"]
      depends_on: ["plasticity_neuromodulation_v4:PLW-1"]
      cross_plan_link: []
      readiness_gate:
        - "Project rule feedback_biology_before_formal_definitions: commission this /lit-pull BEFORE registering any ACh/PV/BDNF substrate claim; the opening-side claims have NO biology lit-pull today"
        - "Anchors named in the framing note: Hensch 2005 (PV/GABA critical-period closure), Bear & Singer 1986 (ACh+NE pairing abolishes plasticity), Froemke 2015 + Kilgard & Merzenich 1998 (nucleus basalis -> cortical remapping), Sale 2007 (GABA reduction reopens CP), Lehmann & Lowel 2008 + Trachtenberg 2015 (windows shift in gain, not binary)"
        - "Do NOT pull pre-emptively: gate the pull on PLW-1's decision-to-build passing first"
      last_updated: 2026-06-10
      completion_note: "INV-074/MECH-333 already carry strong closure-side anchors (Fagiolini & Hensch 2000, Kirkpatrick 2017). The opening-side ACh-gain mechanism is the ungrounded half. This node closes that grounding debt before substrate registration."
    - id: "plasticity_neuromodulation_v4:PLW-3"
      title: "PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:ach_analog_plasticity_gate"]
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
      severity: high
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:state_conditional_plasticity_gain"]
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
      severity: medium
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:pv_analog_closure_clock"]
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
      severity: low
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:bdnf_analog_duration_knob"]
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
      unblocks_claims: ["NEWCLAIM:plasticity_gain_layer_specificity_question"]
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
| A -- ACh-analog gain gate | PLW-3 | NEWCLAIM:ach_analog_plasticity_gate | V4 (gated on MECH-333) | MECH-333 open-phase core + readable drivers (MECH-205 / SD-032a / drive) |
| B -- state-conditional gain | PLW-4 | NEWCLAIM:state_conditional_plasticity_gain | V4 | extends ARC-075; layer-specificity decided |
| C -- PV closure clock | PLW-5 | NEWCLAIM:pv_analog_closure_clock | V4 (deferred) | continuous gain scalar exists to clamp (PLW-3) |
| D -- BDNF duration knob | PLW-6 | NEWCLAIM:bdnf_analog_duration_knob | V4 (deferred, low) | gain knob + closure clock both exist |
| (fork) layer-specificity | PLW-7 | NEWCLAIM:plasticity_gain_layer_specificity_question | V4 (open question) | decide global-vs-per-substrate before parameterising A/B |

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
