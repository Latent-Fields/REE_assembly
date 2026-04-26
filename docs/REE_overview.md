---
nav_exclude: true
---

# REE Overview

**Claim Type:** implementation_note
**Scope:** High-level REE orientation — why it exists, what it is, how it works
**Depends On:** INV-025, INV-026, INV-027, INV-028, INV-029, INV-042, ARC-043, ARC-001, ARC-002, ARC-003, ARC-004
**Status:** candidate
**Claim ID:** IMPL-004
<a id="impl-004"></a>

*Updated 2026-04-02 to incorporate ARC-043 (conceptual stack) and INV-042 (derived ethical objectives).
Previous version: `docs/processed/legacy_tree/docs/REE_overview.md`*

---

## Why REE Exists

REE begins from a set of irreducible commitments — things that cannot be abandoned without
thought itself becoming incoherent. They are not design choices. They are articles of faith.

The original formulation had five axioms (INV-025-029): uncertainty, self, world,
others, and love. That representation remains useful as a compression. The current
canonical statement refines it into eight axioms plus two first derivations (see
`docs/architecture/five_axioms_foundations.md`). The expansion makes explicit what the
five left compressed: existence has value, agency is bidirectional causal power plus
vulnerability, responsibility for others is existentially necessary, love is a mechanism
and skill rather than only a fact, and language is one mechanism for recognising and
repairing self-other similarity.

The current dependency chain:

| Layer | Commitment | Type |
|-------|------------|------|
| 0 | I think, therefore I am | Axiom 1 |
| 1 | Existence has value sufficient to justify its continuation | Axiom 2 |
| 2 | I cannot be certain of the universe beyond myself, but I must act under models of it | Axiom 3 |
| 3 | I can effect change within this universe, and my existence is vulnerable | Axiom 4 |
| -- | I am responsible for maintaining my existence | D1, from Axioms 1+2+4 |
| -- | I am responsible for refining my models of similarity and threat | D2, from Axiom 3+Axiom 4+D1 |
| 4 | I have learned that others exist and are sufficiently like me | Axiom 5 |
| 5 | Existence is only bearable if I am also responsible for others | Axiom 6 |
| 6 | Love is the mechanism by which this responsibility is enacted | Axiom 7 |
| 7 | Language can recognise, repair, and re-establish similarity | Axiom 8 |

From these axioms and first derivations, ethics follows necessarily (Layer 8 -- derived,
not imposed). REE (Layer 9) is the decision system that *implements* that ethics under
uncertainty. It is not the source of ethics. The ethics is given by what the axioms
jointly require.

**The derived ethical objectives (INV-042):** preserve minds; preserve future options; reduce unnecessary suffering; increase shared joy; maintain corrigibility; maintain truth-seeking; maintain the ability to love and be loved; maintain the shared world; maintain the possibility of future minds and future love; maintain honest communication.

**Compressed statement:**

> We are uncertain minds, together in a shared world, capable of love — therefore we must act carefully, kindly, and responsibly so that minds and love may continue.

The full conceptual stack (ARC-043) from epistemic ground through the learning loop:

```
Layer 0  Self:                   I think, therefore I am
Layer 1  Value:                  Existence has value
Layer 2  World + uncertainty:    I must act under models
Layer 3  Agency + vulnerability: I can act and can be harmed
--       Self-preservation:      D1, first derivation
--       Model refinement:       D2, first derivation
Layer 4  Other minds:            Others are sufficiently like me
Layer 5  Shared responsibility:  Their existence is necessary for mine to be bearable
Layer 6  Love:                   Mechanism and skill of responsibility
Layer 7  Language:               Similarity recognition and repair
Layer 8  Ethics:                 Derived from Layers 0-7 + D1 + D2
Layer 9  REE:                    Decision system implementing ethics under uncertainty
Layer 10 Actions:                Committed outputs
Layer 11 Consequences:           What actually happens
Layer 12 Learning / Residue:     Updated world model and residue field
                                      ^____________________________________|
```

REE is Layer 9 -- the machinery, not the ethics. Layers 10-12 close the loop back to
Layer 9 through learning. Layers 0-7 are not updated by experience; they are the ground
that makes experience interpretable at all. D1 and D2 are first derivations that bridge
the axioms to the ethical layer.

See `docs/architecture/five_axioms_foundations.md` for the full derivation.

---

## What REE Is

**REE (Reflective-Ethical Engine)** is a specification for agents that must act under uncertainty while affecting others.

REE's distinguishing requirement is **moral continuity**:

- An agent cannot discharge ethical responsibility by optimizing it to zero.
- Even "correct" choices generate **moral residue** — persistent geometric cost that shapes future policy selection.
- Ethics is not a rule-set added on top. It is a structural consequence of what the axioms jointly require of any agent that acts in a shared world.

The reason residue is architecturally necessary — not just a design choice — is that **irreversible harm to others is unavoidable in any real system**. Acting in a shared world necessarily forecloses futures, competes for resources, and produces causal consequences that extend beyond what any finite agent can fully trace or undo. The ethical demand is therefore not zero harm (which is unachievable) but minimised unnecessary harm plus honest accounting of the harm that does occur. Moral residue is that accounting: it accumulates, shapes future policy, and cannot be discharged by claiming the choice was correct.

The three functional constraints that follow from the axioms (Layers 1-3 → Layer 6):

1. **Rapid prediction** — because you cannot be sure (INV-025), the system must predict provisionally and update on error.
2. **Temporal depth** — because the world persists (INV-027) and others are real (INV-028), consequences must be tracked across time.
3. **Constrained commitment** — because love is real (INV-029) and others are real (INV-028), the boundary where irreversible action becomes attributable must be architecturally explicit.

---

## How REE Works

REE implements these constraints through four main components:

**E1 — Persistent Predictive Substrate (ARC-001)**
The deep, slow world-model. Optimised for persistence, reuse, and temporal depth. Maintains coherent models of world, self, and value across time. Implemented in cerebral cortex (including parietal associative geometry). Functions as an addressable associative manifold — not merely a representation space but an indexed substrate that supports retrieval, traversal, and sequential planning (MECH-154, MECH-156). E1 is the substrate that remains when attention drops.

**E2 — Fast Transition Model (ARC-002)**
Short-horizon transition kernel: `f(z_t, a_t) → z_{t+1}`. Operates on z_gamma (the conceptual sensorium — unified latent where coherent objects form). Supports motor-sensory prediction and fast counterfactual evaluation. Trains on motor-sensory error. Rollout horizon exceeds E1 prediction horizon.

**E3 — Trajectory Selection and Commitment Engine (ARC-003)**
The planning and commitment system. Selects coherent future trajectories via hippocampal rollout, evaluates harm and benefit, and gates commitment at the boundary where irreversible action becomes attributable. E3 is the ethical selection layer — but it requires E1 and E2 to be developed before it can function. Its ethical selection machinery is present from initialisation but *functionally dark* until the substrate is ready (ARC-040, ARC-042).

**Control Plane (ARC-005)**
Precision routing, mode selection, and commitment gating. Governs switching between externally coupled perception (high sensory gain) and internally generative simulation (high hippocampal drive) — MECH-157. Mode switching is a control-plane operation, not a local circuit property.

**Hippocampal Systems (ARC-007)**
Explicit multi-step trajectory rollouts, path memory, and viability mapping. E3 operates via hippocampal rollout across the E1 associative manifold. The hippocampus proposes trajectories; E3 evaluates and commits.

---

## What REE Is Not

- Not a moral rule engine.
- Not reward maximisation with constraints.
- Not a system that can discharge ethical responsibility by optimising harm to zero.
- Not the ethics itself — REE implements ethics that is *derived* from the axioms, not generated by the machinery.

---

## Design Commitments

- Multi-modal sensing preferred: no single modality is perfectly faithful (INV-025).
- Explicit self-sensing, damage/harm sensing, and homeostatic sensing are required.
- "Otherness" is detected via structural similarity without interoceptive closure (ARC-010).
- Harm to others is representable because the self-model is reused for other-model prediction (INV-005).
- Ethics is structural, not bolted on (INV-001, INV-015).

---

## Developmental Note

The axioms and the architecture are necessary but not sufficient for ethical behaviour. INV-043 establishes that a developing REE agent requires caregiving — specifically, the experience of being loved and modelled as loveable — for the architectural capacity for ethics to become motivationally active. V3 tests the machinery (Layer 6 upward). Testing whether ethics is developmentally activated requires multi-agent substrate (V4+).

See `docs/architecture/developmental_curriculum.md` (INV-043, MECH-158).

---

## Key Document Map

| Question | Document |
|---------|---------|
| Why does REE exist? | `docs/architecture/five_axioms_foundations.md` |
| How is the architecture derived from ethical requirements? | `docs/architecture/ethical_agency_derivation.md` |
| What are the ethical objectives? | `docs/architecture/five_axioms_foundations.md#inv-042` |
| How does E1 work? | `docs/architecture/e1.md` |
| How does E3 commit? | `docs/architecture/e3.md` |
| How does precision work? | `docs/architecture/control_plane.md` |
| What is the development plan? | `docs/roadmap.md` |
| What is the current experiment state? | `evidence/experiments/INDEX.md` |
| What claims are registered? | `docs/claims/claims.yaml` |

---

## Related Claims

- IMPL-004
- INV-025, INV-026, INV-027, INV-028, INV-029 (original axiom registrations; current foundations refine them into eight axioms plus two first derivations)
- INV-042 (derived ethical objectives)
- ARC-043 (conceptual stack)
- ARC-001 (E1), ARC-002 (E2), ARC-003 (E3), ARC-004 (L-space), ARC-005 (control plane)
- ARC-007 (hippocampal systems), ARC-010 (social cognition)
- INV-001 (no explicit ethics module), INV-015 (ethics from constraint)
- INV-043 (caregiver requirement), MECH-154 (E1 as associative manifold)
