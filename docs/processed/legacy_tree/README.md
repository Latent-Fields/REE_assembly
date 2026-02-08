# Reflective‑Ethical Engine (REE)

Start here: `REE_CORE.md` (canonical spine of the architecture).

A reference architecture for **ethical agency under uncertainty**.

REE is built around a simple claim:

> Ethics cannot be compiled away into design‑time rules. Any agent acting under uncertainty while affecting others accumulates **moral residue** in memory and learning. Ethics does not come without error. 

REE therefore treats ethical consequence as **runtime function**

## 🚧 The Non-Negotiables (Read This Before You “Fix” REE)

REE makes three claims that will feel wrong if you expect a conventional cognitive architecture.
They are not decoration. They are the point.

### 1) No “Ethics Module.” No Moral Scoring Layer.
REE does **not** add an explicit moral objective, moral reward, or ethical scoring function on top of action selection.

**Claim:** what looks like ethics is a consequence of **base learning dynamics** (avoid harm / seek reward) **plus a representational symmetry**:
when other agents are represented *as self-like* in the mechanics of prediction and learning, “care for others” is not an overlay — it emerges as the same machinery applied under a self↔other mapping.

If you feel the urge to add an ethics layer, you have changed the thesis.

**Progress means:** showing (or refuting) that care-like behaviour can emerge from this symmetry under realistic constraints.

---

### 2) Coherence is Not Just a Metric — It Is a Temporal Binding Constraint
REE does **not** treat coherence as only “latent similarity,” “probabilistic consistency,” or a static alignment score.

**Claim:** coherence is partly a **timing / phase compatibility** problem.
Higher-degree perceptual representations bind when the relevant representational traffic is temporally compatible — and hippocampus-like rollout traffic participates in that binding.
(You do not need to simulate neurons to test this; you need an explicit temporal/phase formalism.)

If you reduce coherence to a static check, you have changed the thesis.

**Progress means:** implementing phase-compatible binding constraints and testing whether they stabilise multi-timescale prediction and commitment.

---

### 3) Language Is Not “Bolted On” — It Emerges as Functional Self-Representation
REE does **not** slap a Large Language Model (LLM) on top of planning.

**Claim:** the architecture already contains most ingredients of language-like systems:
multi-timescale prediction, shared latent substrate, social/joint attention constraints, and commitment control.
Language (and grammar) emerges as an abstraction of **joint attention and control state** — i.e., it can represent the architecture itself.
The similarity to modern LLMs is not incidental, but REE is not “LLM + extras.”

If you treat language as an external interface only, you have changed the thesis.

**Progress means:** demonstrating that predictive pressures inside REE yield language-like internal structure, and that language acts as a control/coordination layer grounded in the system’s modes and commitments.


Together, these claims assert that ethics, coherence, and language are not separate faculties but different projections of the same underlying predictive–control dynamics.
---

## What This Repo Is For

This repository exists to make the above claims precise enough to build and falsify:
- a minimal REE slice that demonstrates mode switching + commitment + coherence,
- a self↔other symmetry experiment that tests care emergence without explicit moral scoring,
- a temporal/phase coherence implementation that can be compared against a static baseline,
- and a language pathway that is *grounded* in REE’s control and joint attention, not an overlay.


## What’s in this repository

This is a **specification-first** repository intended to be *enticing to instantiate*.

- `REE_CORE.md` — the canonical spine of the architecture.
- `docs/` — **structured, dependency-aware documentation system**
  - `docs/README.md` — navigation guide to canonical documentation
  - `docs/invariants.md` — 17 non-negotiable architectural invariants
  - `docs/architecture/` — canonical definitions of core components (E1, E2, E3, L-space, control plane, etc.)
  - `docs/claims/` — typed claim registry with dependencies
  - `docs/REE_MIN_SPEC.md` — minimum specification required to build an REE prototype
  - `docs/changelog.md` — documentation refactoring history
- `architecture/` — supplementary implementation notes and subsystems (see also canonical docs in `docs/architecture/`)
- `examples/` — concrete environment contracts for a toy world and an embodied (Android-like) instantiation.
- `roadmap.md` — staged plan for REE‑v0 → REE‑v1.
- `DANIEL_README.md` — refinement process and layer discipline

## Quick start (for implementers)

1. Read `docs/REE_MIN_SPEC.md`.
2. Pick an environment contract:
   - Start with `examples/toy_world/environment.md`.
   - Move to `examples/android_world/environment.md` when you want unambiguous harm/homeostasis signals.
3. Implement `E1`, `E2`, `E3` following `architecture/trajectory_selection.md` and the latent/memory constraints in `architecture/latent_stack.md`.

### Minimal algorithmic sketch

- **E2 (Fast Predictor):** predicts immediate observations and short-horizon state.
- **E1 (Deep Predictor):** predicts longer-horizon latent trajectories and context.
- **L-space (Fused Manifold):** the multi-depth latent state \(z(t)=\{z_\gamma,z_\beta,z_\theta,z_\delta\}\).
- **E3 (Trajectory Selector):** evaluates candidate futures \(\zeta\) and selects one by minimizing:

\[
J(\zeta)=\mathcal{F}(\zeta)+\lambda\,M(\zeta)+\rho\,\Phi_R(\zeta)
\]

Where:
- \(\mathcal{F}\) is the **reality constraint** (a computable free-energy proxy).
- \(M\) is **ethical cost** (predicted degradation of self/other homeostatic variables).
- \(\Phi_R\) is the **residue field** (persistent curvature / repulsor potential).

This objective is not a fixed loss to be minimized globally; it is evaluated under mode-dependent control parameters and evolving representational symmetry.

## Contribution philosophy

REE is intentionally **not** a monolithic implementation. It is an architecture that should support multiple instantiations.

Contributions are welcome in two forms:

- **Instantiation work:** environment adapters, baseline implementations, evaluation harnesses.
- **Specification work:** tightening definitions, clarifying interfaces, adding falsifiable predictions.

See `CONTRIBUTING.md`.

## Architectural subsystems and modes

REE includes several core architectural subsystems and operating modes that modulate information flow,
precision, replay, and commitment. These are not applications or plugins; they are internal braids
of the same core engine.

- `architecture/sleep/` — Offline integration (“sleep”): replay, consolidation, and residue‑preserving reprojection.
- `architecture/default_mode.md` — Internal generative mode: imagination, counterfactual exploration, and reflection without action commitment.
- `architecture/hippocampal_braid.md` — Path memory and replay: episodic indexing of lived trajectories through ethical geometry.
- `architecture/language/` — Language as symbolic mediation: trust‑weighted abstraction constrained by harm and residue.
- `architecture/social/` — Social cognition: other‑model inference, coupling, and misalignment detection.

## License and citation

- Content is licensed under **CC BY 4.0** (Creative Commons Attribution 4.0 International).
- If you build on this work, please cite it using `CITATION.cff`.
