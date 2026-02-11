# Thoughts: Dopamine Precision Weighting

Status: processed

Processed in:
- `docs/architecture/precision_control.md` (MECH-043)

---

Related claims: ARC-005, INV-008, MECH-003, MECH-043

Dopamine‑like control signals should modulate the **precision weighting** of unsigned prediction errors, shaping learning
and commitment without becoming a scalar reward objective. Misallocation of this precision is a plausible mechanism for
hallucination‑like failures.

Possible affected components:
- Precision control (MECH-002)
- Precision scoping (MECH-003)
- Control‑plane regime tuning (ARC-005)
