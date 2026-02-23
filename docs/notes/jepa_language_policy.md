# REE-First Canonical Language Policy (V2 Interface)

**Claim Type:** implementation_note  
**Scope:** Documentation and user-facing terminology policy for REE-v2  
**Depends On:** IMPL-020, IMPL-022, IMPL-023  
**Status:** candidate  
**Claim ID:** IMPL-024
<a id="impl-024"></a>

---

## Purpose

For v2 and onward, canonical documentation in `REE_assembly` should be REE-first while preserving explicit translation
to JEPA interface terms where helpful.

Goal:
- keep `REE_assembly` centered on REE architectural semantics,
- keep JEPA wording available as interface translation without shifting canonical ownership,
- keep source-fidelity JEPA-first narratives in `REE_convergence`.

---

## Policy Rules

1. First mention rule:
- in `REE_assembly`, write `REE term (JEPA term)` when cross-framework translation is needed.
- Example: `E2 fast predictor (latent predictor)`.

2. Ongoing mention rule:
- in canonical architecture/spec/governance docs, default to REE terms.
- JEPA terms are interface annotations, not canonical framing.

3. User-facing rule:
- `REE_assembly` dashboards/summaries should be REE-first, with optional JEPA parenthetical translation.
- `REE_convergence` source-intake outputs may remain JEPA-first for source fidelity.

4. Contract stability rule:
- machine keys stay stable and REE-contract-compatible (`z_t`, `z_hat`, `pe_latent`, `uncertainty_latent`).
- language policy must not cause schema key churn.

---

## Canonical Quick Map

- L-space <- latent embedding
- E2 fast predictor <- latent predictor
- E1 substrate path <- context/target encoder
- L-state deviation / PE routing input <- latent prediction error
- efference/reafference-ready substrate stream <- action-conditioned prediction

---

## Out of Scope

- This policy does not assert JEPA and REE are equivalent.
- This policy does not change claim status by itself.
- This policy does not modify experiment-pack schema keys.
- This policy does not relocate source-level JEPA playbooks; those remain in `REE_convergence/sources/jepa/*`.

## Related Claims (IDs)

- IMPL-024
- IMPL-020
- IMPL-022
- IMPL-023
