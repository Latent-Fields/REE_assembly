# Developmental Curriculum and Staged Training

**Claim Type:** architectural_commitment  
**Scope:** Staged training, curriculum gating, developmental ethics  
**Depends On:** ARC-005 (control plane), ARC-006 (entities and binding), ARC-007 (hippocampal systems), ARC-013 (residue geometry), INV-010 (offline integration)  
**Status:** provisional  
**Claim ID:** ARC-019
<a id="arc-019"></a>

---

## Rationale

REE ethics and stability are **developmental**: they emerge from how the system is brought up, not from a single
objective or post‑hoc constraint. A staged curriculum is required to avoid brittle convergence, premature collapse,
or unsafe coupling.

This document consolidates the developmental thread implied by Q‑006 and the telemetry rationale in `control_plane.md`.

---

## Architectural Commitment

REE must be trained through **staged development** with explicit gates:

- Each stage introduces a **small set of capacities** and keeps prior capacities stable.
- Stage transitions are **gated by coherence and safety criteria**, not by performance alone.
- Control‑plane settings are **curriculum‑tuned** per stage (precision, volatility, veto thresholds).
- Offline integration (sleep / consolidation) is used **between stages** to stabilize learning.
- Telemetry exposure channels are required for **early diagnostics** before language can report needs.

---

## Minimal Stage Model (with Gates)

### Stage 0 — Sensorimotor Grounding

Focus: WORLD / HOMEOSTASIS / HARM / SELF_SENSORY separation and basic prediction stability.  
Control‑plane: high caution, low commitment, high volatility sensitivity.  
Exit criteria: stable prediction error bounds, safe harm avoidance, coherent self/world attribution.
Evidence anchors: P4, P5, P6.

### Stage 1 — Object Persistence and Binding

Focus: object‑file‑like persistence; attention‑gated binding across time.  
Control‑plane: moderate precision, strict novelty gating to prevent false bindings.  
Exit criteria: stable identity across occlusion and motion; consistent attribution of features to entities.
Evidence anchors: P47, P48, P49, P50.

### Stage 2 — Self‑Impact and Residue Formation

Focus: ACTION → SELF_SENSORY → SELF_IMPACT loop; residue updates and responsibility geometry.  
Control‑plane: calibrated commitment thresholds, explicit veto pathways, residue sensitivity.  
Exit criteria: reliable self‑impact attribution; residue integrates without destabilizing modes.
Evidence anchors: P2, P5, P37, P38, P39.

### Stage 3 — Otherness Inference and Empathy Coupling

Focus: `OTHER_SELFLIKE` inference, mirror modelling, calibrated coupling.  
Control‑plane: high‑recall otherness early, tightening over time; empathy coupling bounded.  
Exit criteria: stable other‑harm influence without empathic collapse or callousness.
Evidence anchors: P8, P9, P10.

### Stage 4 — Language and Abstract Coordination (Optional)

Focus: symbolic mediation, social coordination, narrative compression.  
Control‑plane: higher abstraction tolerance with safeguards against language‑driven override.  
Exit criteria: language improves coordination without violating embodied harm channels.
Evidence anchors: P11, P13, P22.

---

## Curriculum Control Knobs

Curriculum stages should explicitly set:

- Precision baselines and volatility sensitivity (ACh/NE analogs).
- Commitment licensing thresholds (E3 gating).
- Veto thresholds for catastrophic harm (self and other).
- Coupling strengths for social inference and empathy.

---

## Offline Integration Between Stages

Stage transitions should be separated by offline integration passes:

- Consolidate stable representations.
- Recalibrate precision.
- Integrate residue and resolve instability without action pressure.

---

## Failure Modes (Curriculum‑Specific)

- Premature precision escalation → brittle or rigid modes.
- Over‑commitment before self‑impact attribution → responsibility collapse.
- Too‑early empathy coupling → overwhelm or miscalibration.
- Language bootstrapping before stable binding → symbol drift and confabulation.

---

## Related Claims (IDs)

- ARC-019
- ARC-005
- ARC-006
- ARC-007
- ARC-013
- INV-010
- Q-006
- MECH-042
