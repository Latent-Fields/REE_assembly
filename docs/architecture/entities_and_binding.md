# Entities and Binding

**Claim Type:** architectural_commitment  
**Scope:** Entity representation; sparse, persistent, bindable structures  
**Depends On:** [L-space](l_space.md), INV-002 (coherence includes temporal binding)  
**Status:** provisional  
**Claim ID:** ARC-006
<a id="arc-006"></a>

---

## Role in REE

Entities in the Reflective Ethical Engine (REE) are sparse, persistent, bindable structures that emerge within the latent stack.

They are **not** forced symbols or pre-defined ontological categories.  
They are **not** denied either.

Entities are emergent but real variables that:
- maintain coherence across time
- support error ownership and attribution
- enable structured prediction and binding

---

## Architectural Commitment

From DANIEL_README.md Layer 3:

> **Entities as emergent but real variables**
> - Sparse, persistent, bindable structures
> - Not forced symbols, but not denied either
> - Error ownership is entity-linked

---

## Relationship to L-space

Entities emerge within the latent stack as coherent structures that:
- persist across multiple time steps
- bind features and predictions
- support phase-compatible temporal alignment (per INV-002)

## Design Constraints (Evidence‑Informed)

Evidence anchors: P47–P50.

- **Binding is attention‑gated.** Feature binding should depend on precision/attention state rather than a purely
  feedforward merge.
- **Entity persistence requires object‑specific buffers.** “Object‑file‑like” persistence is a **minimal mechanism**
  for tracking entities across time.
- **Relational binding is first‑class.** Binding should support arbitrary relations across space and time, not just
  feature conjunction.
- **Binding is distributed.** Hippocampal systems may participate early in relational binding/comparison rather than
  only in long‑term storage.

<a id="mech-050"></a>
## Functional Locality Without Column Geometry (MECH-050)

**Claim Type:** mechanism_hypothesis  
**Scope:** Functional locality and bounded update regions support attribution without anatomical columns  
**Depends On:** ARC-006, ARC-004  
**Status:** candidate  
**Claim ID:** MECH-050

REE should implement **functional locality** in its representational microcircuits: modular recurrent substructures,
limited lateral spillover, sparse routing constraints, and bounded update regions. This supports error attribution and
corrigibility without requiring anatomical column geometry. Columnar spatial bundling in biology is treated as a
metabolic or developmental optimisation, not a computational primitive.

<a id="mech-044"></a>
## Hippocampal Relational Binding (MECH-044)

**Claim Type:** mechanism_hypothesis  
**Scope:** Hippocampal participation in relational binding and comparison  
**Depends On:** ARC-006, ARC-007, ARC-004  
**Status:** provisional  
**Claim ID:** MECH-044

Hippocampal systems should contribute to **relational binding and comparison**, not only long‑term storage. This
supports early detection of relations and binding consistency across time and context.

---

<a id="mech-045"></a>
## Object‑File‑Like Persistence (MECH-045)

**Claim Type:** mechanism_hypothesis  
**Scope:** Minimal persistence buffer for entity continuity across time  
**Depends On:** ARC-006, ARC-004, INV-002  
**Status:** provisional  
**Claim ID:** MECH-045

Entities should be tracked via **object‑file‑like buffers** that bind features across time and motion, providing a
minimal persistence mechanism without requiring symbolic labels. These buffers are attention‑gated and update with
precision‑weighted continuity constraints.

---

## Error Ownership

Prediction errors in REE are not global.  
They are attributed to specific entities or entity-like structures.

This enables:
- targeted model updates
- localized precision control
- structured learning without global collapse

---

## Status Note

This document represents a provisional architectural commitment extracted from DANIEL_README.md.

Further elaboration is needed to specify:
- entity emergence mechanisms
- binding constraints and timing
- interaction with precision control
- relationship to social cognition (self/other modeling)

---

## Cross-References

- Latent stack: [l_space.md](l_space.md)
- Coherence and temporal binding: [../invariants.md](../invariants.md) INV-002
- Layer 3 commitments: [../../DANIEL_README.md](../../DANIEL_README.md)

---

## Open Questions

<a id="q-001"></a>
### Q-001: What mechanisms produce entity emergence and binding?

Open items from preserved sources include entity emergence mechanisms; binding constraints and timing; interaction with precision control; and relationship to social cognition (self/other modeling).

## Related Claims (IDs)

- ARC-006
- ARC-004
- INV-002
- Q-001
- ARC-007
- MECH-044
- MECH-045
- MECH-050

## References / Source Fragments

- `docs/processed/legacy_tree/docs/architecture/entities_and_binding.md`
- `docs/processed/legacy_tree/DANIEL_README.md`
- `docs/thoughts/2026-02-11_columns.md`
