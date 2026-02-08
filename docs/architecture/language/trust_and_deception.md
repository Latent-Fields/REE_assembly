# Trust And Deception

**Claim Type:** mechanism_hypothesis  
**Scope:** Trust and deception  
**Depends On:** ARC-009, ARC-010  
**Status:** candidate  
**Claim ID:** MECH-015
<a id="mech-015"></a>

---

Source: `docs/processed/legacy_tree/architecture/language/trust_and_deception.md`

> **Elaborates Section 5 (Social Extension: Language) of `REE_CORE.md`.**

# Trust, Reliability, and Deception

Because language conditions priors, REE must treat symbolic input as:
- informative but not authoritative.

### Trust-weighting
The receiver maintains an estimate of sender reliability:
- consistency with observed outcomes,
- alignment with harm signals,
- history of calibration (confidence vs accuracy).

Symbolic updates are weighted by this reliability estimate.

### Deception risks
Language introduces attack surfaces:
- false harm claims,
- false commitments,
- ideological framing,
- reputational laundering.

REE predicts robust systems will:
- cross-check language against embodied harm and world-model prediction,
- penalise repeated miscalibration via reduced trust-weight.
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-015

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/language/trust_and_deception.md`
