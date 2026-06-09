# Spintronic-memristive substrates as future physical cognifold candidates

**Status:** candidate compass — POST-V5 / future physical instantiation.
**NOT on the V3 critical path. NOT queueable for V3.**

Home doc for the claims reaped from the 2026-06-06 spintronic-memristive
cognifold-substrate thought intake
([`docs/thoughts/2026-06-06_spintronic_memristive_cognifold_substrate.md`](../thoughts/2026-06-06_spintronic_memristive_cognifold_substrate.md)).

| Claim | Type | Subject |
|-------|------|---------|
| [ARC-089](#arc-089) | architectural_commitment | `cognifold.substrate_independent_primitives` |
| [MECH-374](#mech-374) | mechanism_hypothesis | `cognifold.memristive_physical_substrate_candidate` |
| [Q-066](#q-066) | open_question | `cognifold.physical_substrate_auditability_safety_scaling` |

All three are `status: candidate`, `epistemic_category: substrate_conditional`,
`implementation_phase: post_v5`, `version_relevance: post_v5`. Promote/demote is
suppressed; `narrow_open_question` does not fire on Q-066 (explicit
`substrate_conditional`).

---

## Why this lives in REE_assembly

This is **not** an implementation requirement for REE-v3. It belongs here as a
*future-substrate architecture note* because it sharpens how REE should specify
the cognifold in **substrate-independent** terms. REE is intended to be a single
cognifold — one interacting state-space, not a modular stack — so the relevant
future substrate is not merely "hardware that can run REE" but hardware that can
physically instantiate a persistent, deformable, multi-timescale action-field.

The load-bearing near-term extraction is **ARC-089**: keep the cognifold's
primitive vocabulary hardware-neutral and physically legible. The spintronic
hardware (MECH-374) is a *candidate* the primitives let us later evaluate, not a
target.

---

## The REE bridge

> Residue is not merely stored memory; it is deformation of the future action
> landscape.

Memristive media — physical substrates in which past activity alters future
state-transition behaviour — make that idea physically literal in a way von
Neumann computation does not. This is the conceptual hinge linking REE's
residue-as-latent-curvature ([ARC-013](../claims/claims.yaml)) to a physical
substrate's history-dependent conductance/state landscape.

### REE ↔ spintronic-memristive mapping (raw section 4)

| REE concept | Spintronic-memristive analogue |
|---|---|
| cognifold | single interacting state-space rather than separate modules |
| residue field | history-dependent deformation of future conductance/state landscape |
| E1 | persistent predictive substrate / slow attractor structure |
| E2 | fast transition dynamics / oscillatory propagation |
| E3 | thresholded commitment / switching between candidate and released action |
| control plane | gain, precision, and phase/coupling modulation |
| offline integration | re-driving / reconsolidating the field without action authority |

---

## ARC-089 — Substrate-independent cognifold primitives {#arc-089}

REE specifies its single cognifold in a hardware-neutral primitive vocabulary:
persistent state; history-dependent deformation; multi-timescale field dynamics;
oscillatory propagation; stochastic transition; attractor transitions;
residue-as-deformation-of-the-future-action-landscape; commitment as a real
boundary between simulated and released action; offline reintegration. Any future
physical substrate is then evaluated by whether it can *instantiate* these
dynamics, not merely *execute* modular software.

These primitives are **already owned and remain software-expressible** — the
claim adds the explicit commitment to keep them substrate-independent and
physically legible:

- residue-as-curvature / cognitive map — ARC-013
- cognifold-as-single-interacting-field with signed coupling — ARC-084
- commitment latch / real boundary between simulated and released action — MECH-090
- offline reintegration as a mathematical necessity — INV-049
- control plane supplying gain/precision/phase modulation — ARC-005

**Guardrail (raw section 8).** If a future agent tries to convert this into
REE-v3 implementation work (hardware targets, hardware-abstraction layers,
android substrate tasks), **stop and reframe**. The correct near-term extraction
is "define and preserve cognifold primitives in software-neutral terms."

---

## MECH-374 — Memristive deformation as physical analogue of residue/cognifold curvature {#mech-374}

Spintronic-memristive media — magnetic tunnel junctions, nanomagnet ensembles,
domain walls, topological spin textures, spin waves / spin-Hall nano-oscillators
— are physical substrates in which past activity alters future state-transition
behaviour. They are a candidate **post-V5 physical cognifold substrate** because
they combine, in one medium: persistent state, history-dependent deformation,
oscillatory dynamics, stochastic switching, attractor-like state-space
trajectories, and possible low-power embodied operation.

**Important non-claims (raw section 5).** This does *not* claim REE-v3 should
target spintronic hardware; does *not* claim such hardware is android-ready; does
*not* claim future REE must run on spintronics. The useful, weaker claim: *if*
REE is a single cognifold, future physical substrates should be assessed by
whether they instantiate persistent, deformable, multi-timescale action-field
dynamics rather than merely execute modular software. Should **not** be promoted
directly to an invariant.

### External anchors (for later literature intake — not citable REE evidence)

These are hardware surveys/announcements, out of REE's experimental domain. They
are preserved for a later targeted lit-pull and are **not** load-bearing for this
candidate registration:

- Shao et al., "Spintronic memristors for computing" — surveys spintronic
  devices from a memristor point of view (MTJs, nanomagnet ensembles, domain
  walls, topological spin textures, spin waves). https://arxiv.org/abs/2112.02879
- TDK spin-memristor for neuromorphic devices (industry; with CEA and Tohoku
  University) — claim that a spin-memristor can function as a basic neuromorphic
  element being developed toward practical application.
- "Memristive control of spin-Hall nano-oscillator synchronization" — relevant to
  oscillator-array control, coupling, memory, and training in one platform.
  https://arxiv.org/abs/2009.06594

---

## Q-066 — Physical-substrate auditability / stability / safety scaling {#q-066}

Can spintronic-memristive media (or any candidate physical cognifold substrate)
scale to embodied REE cognition **without** losing auditability, stability, or
the harm/safety boundaries that REE's software cognifold currently enforces — and
which ARC-089 primitives does each candidate substrate genuinely instantiate
versus merely approximate?

Sub-questions:

1. Can a physical cognifold preserve the simulated-vs-released action boundary
   (MECH-090) as a hard, auditable gate?
2. Does an analog substrate's stochastic switching threaten the stability that
   signed competitive coupling (Q-058) buys in the software cognifold?
3. How is offline reintegration without action authority (INV-049) physically
   realised and verified?

This is the genuinely-open axis: an analog deformable medium may instantiate the
dynamical primitives while making the commitment boundary, provenance/write
gating, and harm-residue firewall harder to inspect and guarantee than in
software. Parked as a post-V5 question awaiting a physical-substrate decision —
not a V3-tractable question to narrow by experiment.

---

## Phase placement

This is **post-V5 physical-instantiation work**. It should not create REE-v3
substrate tasks, experiment-queue entries, or near-term implementation
requirements, and should not distract from the REE-v3 green-board path or from
V4/V5 cognitive-architecture work. It is a **future physical substrate compass**:
the long-range bridge between REE as a software architecture and REE as a possible
future physically embodied cognifold.
