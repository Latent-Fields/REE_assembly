> **This overview is subordinate to `REE_CORE.md` (the canonical specification).**

# REE overview

**Claim Type:** implementation_note  
**Scope:** High-level REE summary and design commitments  
**Depends On:** INV-001, INV-002, INV-003, ARC-001, ARC-002, ARC-003, ARC-004, ARC-007, ARC-018  
**Status:** legacy  
**Claim ID:** IMPL-004
<a id="impl-004"></a>

REE (Reflective‑Ethical Engine) is a specification for agents that must act under uncertainty while affecting others.

REE’s distinguishing requirement is **moral continuity**:

- An agent cannot discharge ethical responsibility by optimizing it to zero.
- Even “correct” choices generate **moral residue**—persistent geometric cost that shapes future policy selection.

REE is organized into five computational components:

1. **E1 (Deep Predictor):** long-horizon, recurrent context model.
2. **E2 (Fast Predictor):** short-horizon, reflex model.
3. **L-space (Fused Manifold):** multi-depth latent state stratified by prediction horizon.
4. **E3 (Trajectory Selector):** selects a coherent future trajectory \(\zeta\) by minimizing reality cost plus ethical cost plus residue curvature. (Legacy phrasing; current canonical framing does not require an explicit ethical cost term — see `docs/architecture/e3.md`.)
5. **Hippocampal Systems:** explicit multi-step rollouts and path memory.

Explicit multi-step rollouts are hippocampal; E1/E2 supply constraints and short-horizon predictions.
Terminology: rollout = explicit hippocampal multi-step sequence; forward prediction = E2 local transition kernel.

## Design commitments

- Multi-modal sensing is preferred: no single modality is perfectly faithful.
- The agent must have explicit **self sensing**, **damage/harm sensing**, and **homeostatic sensing**.
- “Otherness” is detected via **structural similarity** without interoceptive closure: others are loosely coupled but homologous models.
- Harm to others is representable because the self-model is reused for other-model prediction.

## Non-goals

- REE is not a moral rule engine.
- REE is not “reward maximization with constraints.”
- REE does not assume ethical cost can be eliminated.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-004
- INV-001
- INV-002
- INV-003
- ARC-001
- ARC-002
- ARC-003
- ARC-004

## References / Source Fragments

- `docs/processed/legacy_tree/docs/REE_overview.md`
