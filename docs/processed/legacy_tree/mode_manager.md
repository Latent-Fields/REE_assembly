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

## Core assumptions

1. Cognition operates in semi-discrete modes, not a single continuous regime.
2. Modes are persistent, with hysteresis and refractory periods.
3. Control-plane modulation parameterises modes; it does not encode content.
4. Transitions are gated, multi-signal decisions.

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
