# Thought intake: plasticity governance -- learning as a governed write, not a reflex

**Date:** 2026-05-21 (raw); intake written 2026-06-05
**Status:** intake / candidate claim cluster (NOT yet registered in claims.yaml)
**Raw thought file:** `docs/thoughts/2026-05-21_Gated_plasticity.md`
**Origin:** user convergence of two biological findings -- HuD/ELAVL4 developmental-reuse
(adult plasticity reuses the embryonic molecular "playbook" with stage-specific target
substitutions) and ACh-gated dopamine learning (a dopamine RPE only teaches when its phase
relationship to a cholinergic dip permits the write). User seed: "could these pathways
translate to primitives or invariants that help me assemble REE."
**Anchors (existing claims this lands beside):** MECH-083 (ACh as meta-level plasticity
gain: durable-write vs read-through), INV-056 (selective neoteny / substrate-specific
hardening), INV-074 (plasticity-injection crystallization), MECH-333 / MECH-334 (the
crystallization / closure side), SD-037, and the sibling raw thought
`docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md` (ACh/PV/BDNF opening side --
see memory `project_plasticity_window_neuromodulators`).

---

## 1. Core idea (one line)

**Plasticity is not the same thing as a signal: learning requires permission.** A teaching
signal (RPE, harm PE, novelty, salience, social/affective discrepancy) is a *proposal* to
alter a structure, not an update. A separate gating layer decides whether it may write,
*where*, and *how deep*.

## 2. What is new vs what REE already has

The load-bearing observation from the incorporation audit (2026-06-05): REE has the
**closure / crystallization** side of plasticity well developed but lacks an explicit,
unified **typed-write-permission transaction** model. This thought supplies that.

| Element of the thought | Already in REE? | Novelty verdict |
|---|---|---|
| ACh gates whether a teaching signal teaches | **Yes** -- MECH-083 (ACh meta-level plasticity gain, durable-write vs read-through) | Confirms; thought adds the *timing-window* phrasing and the dopamine-phase-relation grounding |
| Plasticity narrows with development; some substrates stay plastic | **Yes** -- INV-056 (selective neoteny), INV-074 / MECH-333 / MECH-334 (crystallization) | Confirms the *closing* side; thought adds the *reuse* framing (same operator, shifting target set) |
| Sleep/offline re-evaluates blocked or unresolved updates | **Partial** -- sleep substrate (SD-017, MECH-204) consolidates; "blocked plasticity event re-evaluation" is not an explicit primitive | Extension |
| **Signal-as-proposal**: a teaching signal is a candidate event with source/target/depth/timing/benefit/harm fields, evaluated by a gate before it writes | **No** -- REE has per-channel write gates (e.g. MECH-094 hypothesis tag, beta gate MECH-090) but no *unified typed plasticity-event + controller* abstraction | **NOVEL** -- the central contribution |
| **Target x depth separation**: same signal may update shallow salience yet be forbidden from touching identity invariants / ethical constraints | **Implicit only** -- write-locus claims exist (MECH-060 write-locus contamination, MECH-094) but no graded *depth ladder* | **NOVEL** |
| **Plasticity-depth ladder** (transient -> salience -> local model -> memory map -> self/other -> goal -> ethical constraint -> identity invariant), deeper = stronger gate | **No** | **NOVEL** -- directly governance-relevant |
| **Blocked-signal residue**: a write denied for safety reasons leaves a residue trace, not silence | **Partial** -- moral residue exists (residue claims, MECH-056 residue trajectory); "blocked plasticity = residue candidate" gives residue a *computational* definition | Extension / sharpening |
| **Ethics as plasticity selection**: an agent becomes what it permits itself to learn; moral architecture must supervise self-modification, not only action | **No explicit claim** -- REE's ethics is action-selection + residue centred | **NOVEL** -- a genuine bridge claim |
| Failed-experiment debugging grammar (correct-signal/wrong-gate, correct-gate/wrong-target, ...) | **No** | Useful diagnostic tooling, not a claim |

**Reconciliation with the 2026-06-01 plasticity-window note.** That note covers the
*opening* side (basal-forebrain ACh / PV / BDNF state-conditional plasticity *gain*) and is
flagged V4-or-late-V3. This 2026-05-21 thought is the more general *transaction/permission*
frame that the opening-side neuromodulators would plug into: ACh-gating here = the gate's
timing-window; BDNF / critical-period = the developmental-phase term in the depth permission.
The two should be registered as one cluster, with 2026-06-01 as the neuromodulatory-substrate
child of the 2026-05-21 governance frame. Do **not** double-register the ACh-gating idea --
MECH-083 already holds it; the cluster *cites* MECH-083, it does not restate it.

## 3. Key formulations (verbatim-faithful)

- Signal pipeline: `error/reward/salience/harm/novelty -> state gate -> target permission
  -> timing window -> depth permission -> consolidation/suppression/audit -> authorised
  learning`.
- `teaching_signal_present != learning_authorised`.
- `residue = blocked or incomplete plasticity with ethical salience`.
- Depth ladder (8 rungs): transient activation / salience weight / local transition model /
  memory-map consolidation / self-other model / goal stream / ethical constraint /
  identity invariant. Higher rung -> stronger gate + governance.
- Implementation sketch present in the raw thought: `PlasticityEvent`, `PlasticityGate.permits()`,
  `PlasticityController.process()` (dataclass-level, REE-v3-shaped) -- usable as a v4 design
  scaffold, NOT yet a substrate commitment.

## 4. Candidate claims (for future governance registration -- NOT registered here)

Naming will follow the registry's numeric convention at registration time; the thought's
mnemonic IDs are kept here only for traceability.

- **INV (signals-as-proposals)** -- RPE / harm PE / novelty / salience / social / affective
  discrepancy are candidate plasticity events, not automatic updates. *[novel; gate on V4]*
- **INV (target-depth separation)** -- a plasticity event must distinguish *target* from
  *depth*; the same signal may update shallow salience yet be forbidden from identity /
  ethical-constraint structures. *[novel]*
- **INV (developmental reuse)** -- adult adaptation reuses development-like plasticity
  operators but with stricter target permissions than childhood world-model formation.
  *[overlaps INV-056 / INV-074; register as refinement or fold in, do not duplicate]*
- **ARC (typed plasticity gating / plasticity controller)** -- learning implemented as
  typed, gated events (source, type, target, timing, confidence, valence, expected
  benefit/harm, depth, governance-required?). *[novel; the central architectural commitment]*
- **MECH (plasticity-depth ladder)** -- plasticity graded by 8 depth rungs; gating strength
  monotone in depth. *[novel]*
- **MECH (blocked-signal residue)** -- a morally salient signal denied a write records a
  residue trace rather than being discarded. *[sharpens existing residue claims]*
- **ETH / SAF (ethics-as-plasticity-selection + deep-plasticity-risk)** -- ethical cognition
  governs which experiences may alter the agent; deep plasticity (self/other model, goals,
  ethical constraints, identity invariants) is safety-critical and requires gating + audit +
  (where possible) rollback. *[novel bridge; high value for reward-hacking / prompt-injection
  / identity-drift resistance]*

Open questions worth carrying: target-class taxonomy (Q), mode-specific plasticity
permissions (Q), depth at which governance becomes mandatory (Q), expected-vs-irreducible-
uncertainty discrimination (Q), rollback for high-depth events (Q).

## 5. Affected existing claims / docs

- **MECH-083** -- this cluster is the system-level home for the ACh gating MECH-083 states
  locally; cross-link, do not restate.
- **INV-056 / INV-074 / MECH-333 / MECH-334 / SD-037** -- the crystallization/closing side;
  the depth-ladder + reuse-invariant should be filed as the *complement* (governed opening)
  so the closure work and the permission work read as one story.
- **MECH-094 (hypothesis tag write gate), MECH-090 (beta gate), MECH-060 (write-locus
  contamination)** -- existing single-channel write gates; the typed-plasticity controller
  is the abstraction these are instances of. Worth a note that the controller *generalises*
  them rather than replacing them.
- **Residue cluster (MECH-056 + moral-residue claims)** -- gains the "blocked write =
  residue" computational definition.
- Docs to touch if/when registered: `control_plane.md`, `l_space.md`,
  `entities_and_binding.md`-adjacent hippocampal docs, sleep plan
  (`evidence/planning/sleep_substrate_plan.md`), and a new
  `docs/architecture/plasticity_governance.md`.

## 6. Next steps (gated -- not started this pass)

1. **Biology-before-formal-definitions lit pull** (per memory `feedback_biology_before_formal_definitions`):
   commission a targeted review on (a) HuD/ELAVL4 developmental reuse and (b) ACh-DA phase
   gating of learning, to ground the gate + depth-ladder before any MECH is registered. The
   ACh side partly overlaps the 2026-06-01 note's Berridge/Hasselmo territory -- check for an
   existing `targeted_review_*` first.
2. **Governance triage**: decide V4 vs late-V3. The audit + memory both place this V4-leaning;
   keep it off the V3 critical path. The one V3-tractable sliver is the *blocked-signal-residue*
   sharpening, which could attach to existing residue instrumentation without a new substrate.
3. **Register as a cluster** (one governance pass) reconciled with the 2026-06-01 neuromodulator
   note, citing MECH-083 / INV-056 / INV-074 rather than duplicating them.

## 7. Cross-references

- Raw: `docs/thoughts/2026-05-21_Gated_plasticity.md`; sibling
  `docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md`.
- Memory: `project_plasticity_window_neuromodulators` (opening side, V4-late-V3),
  `feedback_biology_before_formal_definitions`.
- Claims: MECH-083, INV-056, INV-074, MECH-333, MECH-334, SD-037; write-gate instances
  MECH-094 / MECH-090 / MECH-060; residue MECH-056.
