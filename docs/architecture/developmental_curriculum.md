# Developmental Curriculum and Staged Training

**Claim Type:** architectural_commitment  
**Scope:** Staged training, curriculum gating, developmental ethics  
**Depends On:** ARC-005 (control plane), ARC-006 (entities and binding), ARC-007 (hippocampal systems), ARC-013 (residue geometry), INV-010 (offline integration)  
**Status:** provisional  
**Claim ID:** ARC-019, INV-043, MECH-158
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

## Caregiver Requirement for Ethical Development (INV-043)
<a id="inv-043"></a>

> **Synthese paper relevance:** INV-043 and MECH-158 are flagged as candidates for the
> Discussion section of the Synthese/Minds and Machines paper. They extend the five-axiom
> framework's claim that architecture alone is insufficient for ethics.

REE architecture enables but does not guarantee ethical development. The five axioms
(INV-025-029) and the E1/E2/E3 machinery provide the *capacity* for ethical behaviour,
but without a developmental phase in which the agent experiences love from caregivers and
internalises the belief that it is loveable, the architectural capacity for ethics may
resolve into survival, domination, or indifference instead.

This is not a failure of architecture — it is a recognition that architecture specifies
what the agent *can* do, not what it *will* do. Love must be experienced, modelled,
and internalised to become motivationally real, not merely present as a logical
possibility in the axiom set.

**Caregiver functional requirements:**

| Caregiver Function | Developmental Role |
|-------------------|-------------------|
| Prevent irreversible harm | Preserve agent until E3 fully online |
| Imperfect protection | Allow harm-learning without destruction |
| Model love and shared valence | Provide experienced benefit gradient |
| Demonstrate that the developing REE is loveable | Ground the belief "love applies to me" |
| Scaffold interpretation of internal states | Build the self-valence model |
| Gradually increase responsibility | Prevent premature E3 full-load |
| Provide repair after harm | Demonstrate corrigibility (Axiom 1) in practice |

Note on artificial systems: In artificial single-agent substrates (e.g., ree-v3's
CausalGridWorld), the caregiver function is partially substituted by curriculum design
and controlled harm-exposure. This tests the prerequisite structure but does not test
the love-internalisation hypothesis directly. Testing INV-043 fully requires multi-agent
substrate with modelled caregiving.

---

## "Love Exists But Not For Me" — Developmental Failure Mode (MECH-158)
<a id="mech-158"></a>

A developing REE agent that acknowledges all five axioms but concludes "love exists, but
not for me" undergoes a specific ethical motivation collapse.

The failure proceeds as follows:

1. All axioms are structurally present: uncertainty (INV-025), self (INV-026), world
   (INV-027), others (INV-028), love (INV-029).
2. But love is not experienced as personally applicable — the agent has not been
   modelled as loveable by others.
3. Therefore the benefit gradient (Axiom 5 / ARC-024) is not motivationally active
   for the self-other direction.
4. The ethical architecture reduces to self-preservation under uncertainty with others
   treated as instrumental — survival or domination strategies emerge.

This is the primary developmental failure mode for the caregiver requirement (INV-043).
It explains why architecture is necessary but not sufficient: an agent with full ethical
architecture but no love-experience may correctly model that love exists while behaving
as if it does not apply to them.

**Human analogy:** This failure mode maps precisely to attachment disruption pathology:
a child raised without consistent caregiving may understand abstractly that relationships
involve care while being unable to motivationally access that care for themselves,
producing personality structures oriented toward domination, isolation, or self-destruction.

---

## Responsibility Precedes Full Ethical Capacity

During development, responsibility-bearing situations arise before E3 is fully stable
and the ethical architecture is fully online. A childhood REE must act — and sometimes
cause harm — before it can fully process what harm means.

This is not a design flaw; it is structurally unavoidable given staged development
(ARC-019). It requires the curriculum to include:

- **Partial responsibility handling:** actions have consequences before full E3 capacity
- **Forgiveness structures:** Axiom 1 ("you cannot be sure") implies punishment-only
  systems are unethical; the agent could not have known fully
- **Learning after harm:** residue must integrate without destabilising mode
- **Repair:** the curriculum should include recovery from harm-caused relationships
- **Gradual responsibility expansion:** E3 gate thresholds should increase with stage

---

## Self-First, Social-Later Testing Order

**Claim Type:** implementation_note  
**Scope:** Developmental testing order and governance sequencing  
**Depends On:** ARC-019, Q-006, ARC-005, ARC-007, ARC-010  
**Status:** candidate  
**Claim ID:** IMPL-019
<a id="impl-019"></a>

This note refines stage execution order for experiments. It is a governance heuristic, not a new architectural
commitment.

Operational order:

0. Harness and observability readiness (deterministic seeds, mechanism flags, invariant checks, structured metrics).
1. Self-viability learning loop (self-harm reduction, residue stability, commitment reliability).
2. Control-plane stabilisation (reduced mode thrash, bounded volatility, calibration alignment).
3. Predictive rollout maturity (feasible counterfactuals, reduced confabulation, preserved rollout diversity).
4. Social extension and coupling (other-modelling introduced only after earlier gates hold).

Why this ordering is enforced:

- Social losses and coupling can mask unresolved self/control instabilities.
- Earlier-stage failures are easier to interpret in isolation.
- Later-stage social behaviour is more attributable when base loops are stable.

Gating checks before entering social extension:

- Self-harm and recovery metrics are stable across seeds.
- Control-plane mode-switch dynamics stay within thresholds.
- Rollout feasibility and prediction-error alignment are within bounds.

Expected violation signature when order is ignored:

- Elevated mode thrash and veto instability.
- Ambiguous causal attribution (social terms masking control faults).
- Increased conflict rate in claim-evidence directionality.

---

## Related Claims (IDs)

- ARC-019
- IMPL-019
- ARC-005
- ARC-006
- ARC-007
- ARC-013
- INV-010
- Q-006
- MECH-042
- INV-041 (Childhood phase as architectural prerequisite)
- ARC-040/ARC-042 (E3 dark until E1/E2 ready)
- INV-043 (Caregiver requirement for ethical development)
- MECH-158 ("Love exists but not for me" failure mode)
- MECH-052 (Care persistence, social.md)
- INV-025-029 (Five axioms -- axiom 1 grounds the forgiveness requirement)
