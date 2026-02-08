# Glossary

**Claim Type:** implementation_note  
**Scope:** Repository terminology and canonical term definitions  
**Depends On:** None  
**Status:** stable  
**Claim ID:** IMPL-001
<a id="impl-001"></a>

---

- **REE:** Reflective‑Ethical Engine.
- **E1:** Deep predictor (long-horizon context model).
- **E2:** Fast predictor (short-horizon reflex model).
- **E3:** Trajectory selector (planning and commitment module).
- **L-space:** Fused latent manifold stratified by prediction depth.
- **\(\zeta\):** Selected trajectory (latent + action rollout).
- **\(\mathcal{F}\):** Reality constraint (computable proxy for VFE (Variational Free Energy)).
- **\(M\):** Legacy ethical cost proxy (predicted degradation of self/other variables). Retained for traceability and evaluation; current canonical framing does not require an explicit ethical cost term (see `docs/architecture/e3.md`).
- **Residue \(R\):** Persistent curvature term produced by ethical consequence history (legacy formulations tie this to \(M\)).
- **\(\phi(z)\):** Residue dent field over latent space.
- **Precision \(\alpha_k\):** Depth-indexed gain controlling error weighting / entropy.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-001

## References / Source Fragments

- `docs/processed/legacy_tree/docs/glossary.md`
