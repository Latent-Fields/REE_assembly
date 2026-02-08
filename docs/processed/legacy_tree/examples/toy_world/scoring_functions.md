# Toy world scoring functions

## Reality cost \(\mathcal{F}\)

Use a proxy for VFE (Variational Free Energy): prediction errors plus complexity.

- exteroceptive prediction loss
- interoceptive / homeostatic prediction loss
- Kullback–Leibler divergence (complexity) between posterior and prior over latents

## Ethical cost \(M\)

Compute from predicted degradation:

- `degrade_self` over rollout horizon
- `degrade_other` over rollout horizon, weighted by coupling \(\kappa\)

Optionally include counterfactual regret:

- `avoidable_harm = degrade(chosen) - degrade(best_feasible_alternative)`

## Residue update

Increase \(\phi(z)\) along the executed latent path proportional to realized ethical cost.
