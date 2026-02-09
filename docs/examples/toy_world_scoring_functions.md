# Toy World Scoring Functions

**Claim Type:** implementation_note  
**Scope:** Toy world scoring functions  
**Depends On:** IMPL-003  
**Status:** stable  
**Claim ID:** IMPL-012
<a id="impl-012"></a>

---

Source: `docs/processed/legacy_tree/examples/toy_world/scoring_functions.md`

# Toy world scoring functions

Current canonical framing does not require an explicit ethical cost term. The \(M\) function below is retained as a legacy evaluation proxy.

## Reality cost \(\mathcal{F}\)

Use a proxy for VFE (Variational Free Energy): prediction errors plus complexity.

- exteroceptive prediction loss
- interoceptive / homeostatic prediction loss
- Kullback–Leibler divergence (complexity) between posterior and prior over latents

## Legacy ethical cost \(M\)

Compute from predicted degradation:

- `degrade_self` over hippocampal rollout horizon
- `degrade_other` over hippocampal rollout horizon, weighted by coupling \(\kappa\)

Optionally include counterfactual regret:

- `avoidable_harm = degrade(chosen) - degrade(best_feasible_alternative)`

## Residue update

Increase \(\phi(z)\) along the executed latent path proportional to realized ethical degradation proxy (legacy \(M\)).
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-012
- IMPL-003

## References / Source Fragments

- `docs/processed/legacy_tree/examples/toy_world/scoring_functions.md`
