# JEPA-First Language Policy (V2)

**Claim Type:** implementation_note  
**Scope:** Documentation and user-facing terminology policy for REE-v2  
**Depends On:** IMPL-020, IMPL-022, IMPL-023  
**Status:** candidate  
**Claim ID:** IMPL-024
<a id="impl-024"></a>

---

## Purpose

For v2, documentation and user-facing interactions should be JEPA-first while preserving explicit translation to REE
terms.

Goal:
- use JEPA vocabulary as the default substrate language,
- keep REE terminology visible inline so architecture continuity is preserved.

---

## Policy Rules

1. First mention rule:
- write `JEPA term (REE term)` on first mention in each section.
- Example: `latent predictor (E2 fast predictor)`.

2. Ongoing mention rule:
- in substrate-focused sections, default to JEPA terms.
- in control/commitment sections, default to REE terms and reference JEPA terms only when needed.

3. User-facing rule:
- dashboards and summaries should use JEPA-first labels with REE translation inline or as parenthetical text.
- Avoid REE-only jargon without translation for v2-facing interfaces.

4. Contract stability rule:
- machine keys stay stable and REE-contract-compatible (`z_t`, `z_hat`, `pe_latent`, `uncertainty_latent`).
- language policy must not cause schema key churn.

---

## Canonical Quick Map

- latent embedding -> L-space
- latent predictor -> E2 fast predictor
- context/target encoder -> E1 substrate path
- latent prediction error -> L-state deviation / PE routing input
- action-conditioned prediction -> efference/reafference-ready substrate stream

---

## Out of Scope

- This policy does not assert JEPA and REE are equivalent.
- This policy does not change claim status by itself.
- This policy does not modify experiment-pack schema keys.

## Related Claims (IDs)

- IMPL-024
- IMPL-020
- IMPL-022
- IMPL-023
