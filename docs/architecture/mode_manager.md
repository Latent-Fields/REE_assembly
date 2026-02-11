# Mode Manager

**Claim Type:** mechanism_hypothesis  
**Scope:** Mode management and transitions  
**Depends On:** ARC-005, ARC-003  
**Status:** candidate  
**Claim ID:** MECH-008
<a id="mech-008"></a>

---

Source: `docs/processed/legacy_tree/mode_manager.md`

# Mode Manager — Architectural Specification (Draft)

> **Status:** Draft / architectural control document  
> **Scope:** Functional mode management and transitions (not anatomy-specific)  
> **Intended location:** `docs/architecture/mode_manager.md`

---

## Purpose

The Mode Manager formalises how REE operates in **discrete cognitive modes**, how those modes differ in control-plane parameterisation, and how transitions between modes occur.

This document does **not** introduce new cognitive content systems.  
It specifies **how existing systems (E1, E2, E3, control plane)** are reconfigured across modes.

---

## Update: Fast Priors and Pre‑Commitment

Mode management is decomposed into two control‑plane functions:

- **Amygdala Analogue (AA):** fast salience classification that proposes a distribution over modes (see MECH‑046 in
  `control_plane.md`).
- **Pre‑Commitment Mode Manager (PCM):** commits to a mode with hysteresis and switching costs, constraining E3
  trajectory search before deep evaluation (MECH‑047 below).

AA proposes; PCM commits.

---

<a id="mech-020"></a>
## Emergent Cognitive Modes (MECH-020)

Different cognitive modes (reactive, deliberative, habitual, reflective) emerge from how the control plane biases:
- which prediction horizons dominate,
- which errors are allowed to matter,
- which bindings become rigid or remain fluid,
- and which trajectories are allowed to accumulate learning.

From the outside, this can look like “choice.” From the inside, it is better understood as continuous shaping of a landscape in which some paths stabilise and others decay.

Source: `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`

---

See `modes_of_cognition.md` for the control-plane regime taxonomy (ARC-016, MECH-025..MECH-028).

---

## Core assumptions

1. Cognition operates in semi-discrete modes, not a single continuous regime.
2. Modes are persistent, with hysteresis and refractory periods.
3. Fast mode priors bias regime selection before deep trajectory evaluation.
4. Control-plane modulation parameterises modes; it does not encode content.
5. Transitions are gated, multi-signal decisions.

---

<a id="mech-047"></a>
## Pre‑Commitment Mode Manager (MECH-047)

**Claim Type:** mechanism_hypothesis  
**Scope:** Mode commitment with hysteresis and switching costs  
**Depends On:** ARC-005, MECH-046  
**Status:** candidate  
**Claim ID:** MECH-047

The pre‑commitment mode manager (PCM) stabilises a **committed mode** using hysteresis and switching costs. It consumes
AA mode priors, energy/viability state, and transition cost signals, then **commits or maintains** a regime that shapes
E3 trajectory search before deep evaluation. PCM prevents oscillatory thrashing by requiring sustained salience or
confidence to switch.

---

## Primitive modes (v1)

### M1 — Goal / Action Mode
Focused, task-positive, exploitative behaviour.

**Control profile**
- Commitment (K3): High
- Precision (K2): High
- Exploration (K4): Low
- Plasticity (K1): Moderate
- Attention (K6): Narrow

---

### M2 — Default Mode / Generative Mode
Internally oriented modelling and integration.

**Control profile**
- Commitment (K3): Low
- Precision (K2): Low
- Exploration (K4): Moderate
- Attention (K6): Broad

---

### M3 — Play / Exploration Mode
Active sampling with reduced penalty.

**Control profile**
- Commitment (K3): Low–Moderate
- Precision (K2): Moderate
- Exploration (K4): High
- Plasticity (K1): High

---

### M4 — Sleep / Offline Modes
Action suppressed; replay and consolidation dominant.

---

### M5 — Vigilance / Orienting (Transient)
Short-lived interrupt state.

---

## Transition triggers

- Resource / homeostatic
- Trajectory coherence
- Aversive / interruptive
- Completion / closure
- Contextual / social

---

## Constraints

- Hysteresis
- Refractory periods
- Feasibility gating
- Safety overrides

---

## Illustrative math sketch (non‑binding)

This is a minimal formal sketch of the AA → PCM interface. It is optional and can be implemented with discrete clocks,
spiking phase windows, or conventional schedulers.

Mode priors from AA:

\[
q^{AA}_t(m) = \mathrm{softmax}\left(\frac{\ell_t(m)}{\tau_t}\right)
\]

Entropy temperature modulated by μ/κ overlays (MECH‑048):

\[
\tau_t = \tau_0 \exp(\alpha_\kappa \kappa_t - \alpha_\mu \mu_t)
\]

Switching inertia (commitment stability):

\[
I_{t+1} = \lambda I_t + \eta_\mu \mu_t - \eta_\kappa \kappa_t
\]

PCM commits when a candidate mode exceeds the current mode by a threshold that includes inertia and transition costs.

---

## Relationship to E-levels

- E1: dominant in M2, M4
- E2: dominant in M1, M3
- E3: active in M1, M3
- Control plane: owns modes and transitions

---

## Open areas

- Attention/gain axis formalisation
- Availability gating
- Safety constraints
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-008
- MECH-020
- MECH-046
- MECH-047
- MECH-048

## References / Source Fragments

- `docs/processed/legacy_tree/mode_manager.md`
- `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`
- `docs/thoughts/2026-02-11_amygdala.md`
- `docs/thoughts/2026-02-11_some_control_plane_maths_hypotheses.md`
