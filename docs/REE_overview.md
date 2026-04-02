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

REE begins from five irreducible commitments — things that cannot be abandoned without thought itself becoming incoherent. They are not design choices. They are articles of faith.

| Layer | Axiom | Claim |
|-------|-------|-------|
| 0 | You cannot be sure | INV-025 |
| 1 | I am | INV-026 |
| 2 | Others exist | INV-028 |
| 3 | We share the world | INV-027 |
| 4 | Love exists | INV-029 |

From these axioms, ethics follows necessarily (Layer 5 — derived, not imposed). REE (Layer 6) is the decision system that *implements* that ethics under uncertainty. It is not the source of ethics. The ethics is given by what the axioms jointly require.

**The derived ethical objectives (INV-042):** preserve minds; preserve future options; reduce unnecessary suffering; increase shared joy; maintain corrigibility; maintain truth-seeking; maintain the ability to love and be loved; maintain the shared world; maintain the possibility of future minds and future love.

**Compressed statement:**

> We are uncertain minds, together in a shared world, capable of love — therefore we must act carefully, kindly, and responsibly so that minds and love may continue.

The full conceptual stack (ARC-043) from epistemic ground through the learning loop:

```
Layer 0 — Epistemic ground:   You cannot be sure        (INV-025)
Layer 1 — Existence:           I am                      (INV-026)
Layer 2 — Other minds:         Others exist              (INV-028)
Layer 3 — Shared world:        We share the universe     (INV-027)
Layer 4 — Love:                Love exists and I love    (INV-029)
Layer 5 — Ethics:              Derived from Layers 0-4   (INV-042)
Layer 6 — REE:                 Decision system implementing ethics under uncertainty
Layer 7 — Actions:             Committed outputs
Layer 8 — Consequences:        What actually happens
Layer 9 — Learning / Residue:  Updated world model and residue field
                                    ↑_____________________________________|
```

REE is Layer 6 — the machinery, not the ethics. Layers 7-9 close the loop back to Layer 6 through learning. Layers 0-4 are not updated by experience; they are the ground that makes experience interpretable at all.

See `docs/architecture/five_axioms_foundations.md` for the full derivation.

---

## What REE Is

**REE (Reflective-Ethical Engine)** is a specification for agents that must act under uncertainty while affecting others.

REE's distinguishing requirement is **moral continuity**:

- An agent cannot discharge ethical responsibility by optimizing it to zero.
- Even "correct" choices generate **moral residue** — persistent geometric cost that shapes future policy selection.
- Ethics is not a rule-set added on top. It is a structural consequence of what the axioms jointly require of any agent that acts in a shared world.

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
- INV-025, INV-026, INV-027, INV-028, INV-029 (five axioms)
- INV-042 (derived ethical objectives)
- ARC-043 (conceptual stack)
- ARC-001 (E1), ARC-002 (E2), ARC-003 (E3), ARC-004 (L-space), ARC-005 (control plane)
- ARC-007 (hippocampal systems), ARC-010 (social cognition)
- INV-001 (no explicit ethics module), INV-015 (ethics from constraint)
- INV-043 (caregiver requirement), MECH-154 (E1 as associative manifold)
