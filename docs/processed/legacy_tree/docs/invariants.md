# REE Architectural Invariants

**Claim Type:** invariant  
**Scope:** Core architectural commitments that define REE identity  
**Depends On:** None (axiomatic)  
**Status:** stable

---

## Purpose

This document lists the **non-negotiable architectural invariants** of the Reflective-Ethical Engine (REE).

An implementation is **not REE-compliant** if it violates any of these invariants.

These invariants define what REE *is*. Changing one invalidates large parts of the project.

---

## Core Thesis Invariants

<a id="inv-001"></a>
### INV-001: No Explicit Ethics Module

**Subject:** ethics.emergence  
**Polarity:** denies  
**Claim:** REE does **not** add an explicit moral objective, moral reward, or ethical scoring function on top of action selection.

What looks like ethics is a consequence of **base learning dynamics** (avoid harm / seek reward) **plus a representational symmetry**: when other agents are represented *as self-like* in the mechanics of prediction and learning, "care for others" is not an overlay — it emerges as the same machinery applied under a self↔other mapping.

**Source:** [README.md](../README.md) §1, [REE_CORE.md](../REE_CORE.md) §5

**Violation:** Adding an ethics layer changes the thesis.

---

<a id="inv-002"></a>
### INV-002: Coherence Includes Temporal Binding

**Subject:** coherence.definition  
**Polarity:** asserts  
**Claim:** Coherence is **not** only "latent similarity," "probabilistic consistency," or a static alignment score.

Coherence is partly a **timing / phase compatibility** problem. Higher-degree perceptual representations bind when the relevant representational traffic is temporally compatible — and hippocampus-like rollout traffic participates in that binding.

**Source:** [README.md](../README.md) §2

**Violation:** Reducing coherence to a static check changes the thesis.

---

<a id="inv-003"></a>
### INV-003: Language Is Functional Self-Representation

**Subject:** language.emergence  
**Polarity:** asserts  
**Claim:** REE does **not** slap a Large Language Model (LLM) on top of planning.

The architecture already contains most ingredients of language-like systems: multi-timescale prediction, shared latent substrate, social/joint attention constraints, and commitment control. Language (and grammar) emerges as an abstraction of **joint attention and control state** — i.e., it can represent the architecture itself.

**Source:** [README.md](../README.md) §3

**Violation:** Treating language as an external interface only changes the thesis.

---

## Architectural Invariants

<a id="inv-004"></a>
### INV-004: Ethical Cost Is Persistent

**Subject:** ethics.persistence  
**Polarity:** asserts  
**Claim:** Ethical cost is **persistent**, not resettable.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-005"></a>
### INV-005: Harm Via Mirror Modeling

**Subject:** ethics.mechanism  
**Polarity:** asserts  
**Claim:** Harm to others contributes to ethical cost via **mirror modelling**, not symbolic rules.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-006"></a>
### INV-006: Residue Cannot Be Erased

**Subject:** residue.persistence  
**Polarity:** denies  
**Claim:** Moral residue **cannot be erased**, only integrated and contextualised.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-007"></a>
### INV-007: Language Cannot Override Harm

**Subject:** language.constraint  
**Polarity:** denies  
**Claim:** Language **cannot override embodied harm sensing**.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-008"></a>
### INV-008: Precision Is Routed and Depth-Specific

**Subject:** precision.routing  
**Polarity:** asserts  
**Claim:** Precision is **routed and depth-specific**, not global.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-009"></a>
### INV-009: Attention Via Precision Modulation

**Subject:** attention.mechanism  
**Polarity:** asserts  
**Claim:** Attention is realised through **precision modulation**, not symbolic control or content injection.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-010"></a>
### INV-010: Offline Integration Required

**Subject:** sleep.necessity  
**Polarity:** asserts  
**Claim:** Offline integration exists and is required for long-term viability.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-011"></a>
### INV-011: Imagination Without Belief Update

**Subject:** default_mode.safety  
**Polarity:** asserts  
**Claim:** Imagination and counterfactual simulation must be possible **without belief update**.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-012"></a>
### INV-012: Commitment Gates Responsibility

**Subject:** commitment.epistemology  
**Polarity:** asserts  
**Claim:** Belief and responsibility arise only through **commitment to action**, not mere prediction.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

## Layer 1 Invariants (from DANIEL_README.md)

<a id="inv-013"></a>
### INV-013: Cognition Is Predictive, Iterative, Multi-Timescale

**Subject:** cognition.structure  
**Polarity:** asserts  
**Claim:** Cognition is predictive, iterative, and multi-timescale.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-014"></a>
### INV-014: Separation of Representation and Regulation

**Subject:** architecture.separation  
**Polarity:** asserts  
**Claim:** There is a strict separation between representation (content) and regulation (control).

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-015"></a>
### INV-015: Ethics Emerges from Constraint

**Subject:** ethics.emergence_mechanism  
**Polarity:** asserts  
**Claim:** Ethics emerges from constraint, not optimisation. This includes constraints on learning dynamics plus self-other representational symmetry.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-016"></a>
### INV-016: Stability Over Performance

**Subject:** design.priority  
**Polarity:** asserts  
**Claim:** Stability, not maximal performance, is the primary viability criterion.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-017"></a>
### INV-017: Runaway Is Control Failure

**Subject:** failure.classification  
**Polarity:** asserts  
**Claim:** Runaway behaviour is a control failure, not a representational one.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

## Interpretation

These invariants collectively assert that:

1. **Ethics, coherence, and language are not separate faculties** but different projections of the same underlying predictive–control dynamics.

2. **REE is constraint-complete**: any instantiation must satisfy these constraints to remain ethically coherent as capability scales.

3. **Violations are architectural failures**, not parameter tuning issues.

---

## Cross-References

- Core architecture: [../REE_CORE.md](../REE_CORE.md)
- Refinement process: [../DANIEL_README.md](../DANIEL_README.md)
- Claim registry: [claims/claims.yaml](claims/claims.yaml)

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- INV-001
- INV-002
- INV-003
- INV-004
- INV-005
- INV-006
- INV-007
- INV-008
- INV-009
- INV-010
- INV-011
- INV-012
- INV-013
- INV-014
- INV-015
- INV-016
- INV-017

## References / Source Fragments

- `docs/processed/legacy_tree/docs/invariants.md`
- `docs/processed/legacy_tree/README.md`
- `docs/processed/legacy_tree/REE_CORE.md`
- `docs/processed/legacy_tree/DANIEL_README.md`
