# Thoughts: Other-Harm Gating (Veto vs Ranking)

Status: processed

Processed in:
- `docs/architecture/social.md` (MECH-036)

---

Related claims: MECH-031, MECH-036, ARC-005, INV-005

Other-harm should trigger a **hard veto** only under high-certainty, catastrophic, or irreversible outcomes. In most
tradeoff-heavy or ambiguous contexts (e.g., necessary harm for a larger good), other-harm should influence **ranking**
instead. Control-plane coupling parameters (`lambda_empathy`, `v_other_veto`) modulate the threshold.

## Possible affected components

- Social empathy coupling (MECH-031)
- Control-plane gating thresholds (ARC-005)
