# The Differentiable Cross-Entropy Method: the direct ML precedent for SD-055

**Claim:** SD-055 — differentiable CEM selection approximation: replace the non-differentiable argmax/argsort elite-selection step in `HippocampalModule.propose_trajectories()` with a softmax-weighted candidate mean so gradient flows from task reward back through candidate selection to SD-016 `cue_action_proj`.

**Source:** Amos B, Yarats D (2020), *The Differentiable Cross-Entropy Method*, ICML 2020 (PMLR vol. 119). [arXiv:1909.12830](https://arxiv.org/abs/1909.12830). Direction: **supports** (confidence 0.82).

## What the paper does

The cross-entropy method (CEM) is an iterative, sampling-based optimizer: draw candidate solutions from a distribution, score them, keep the top-k "elite" candidates, refit the distribution to those elites, repeat. The elite-selection step is a hard top-k threshold — sort the candidates by cost and keep the best fraction. That sort/threshold is piecewise-constant and has zero (or undefined) gradient, so although CEM is widely used as an inner-loop planner in model-based RL, you cannot backpropagate through a CEM solve to learn the parameters of the objective it is optimizing.

Amos and Yarats replace the hard top-k with a **temperature-controlled smooth top-k** operation. The selection becomes a soft, differentiable weighting over candidates; a temperature parameter controls how sharp it is, and as the temperature is lowered the soft operation recovers the original hard selection in the limit. With this substitution the whole CEM solve becomes differentiable with respect to the objective's parameters. They demonstrate it on energy-based structured prediction and, more relevantly here, on fine-tuning CEM-based continuous controllers by learning a lower-dimensional embedding of action sequences end-to-end.

## How it maps to SD-055

This is the precedent SD-055 is built on, almost line for line. SD-055's `functional_restatement` identifies the same barrier: `HippocampalModule.propose_trajectories()` calls `torch.argsort()` to rank candidate trajectories by score and then indexes elite candidates by rank — "an operation with zero gradient w.r.t. scores." Because the `action_bias` from SD-016's `cue_action_proj` enters candidate generation through the E2 rollouts, and the scores derive from those rollouts, the argsort barrier prevents *any* gradient from reaching `cue_action_proj.weight`. SD-055's fix —

```
weights = softmax(-scores / T, dim=0)
ao_mean = sum_i weights[i] * ao_candidate[i]
```

— is precisely a temperature-controlled soft replacement of the elite-selection aggregate, with `T = differentiable_cem_temperature` playing the same role as DCEM's temperature: low `T` concentrates weight near the argmax (approaching the hard selection), high `T` averages broadly. DCEM establishes that this class of move (i) restores gradient flow to upstream parameters and (ii) is usable inside a planner/controller, which is exactly what SD-055 needs to argue. That is why I score the direction as `supports` with mapping fidelity 0.82.

## Limitations and why confidence is 0.82, not higher

Two gaps keep this short of a same-task confirmation. First, DCEM's smooth top-k is the more general Limited-Multi-Label (LML) projection over the elite set, whereas SD-055 uses the *simplest* member of the family — a softmax-weighted mean over **all** candidates, i.e. a temperature-controlled top-1-style aggregate. DCEM therefore validates the family and the rationale, but does not specifically certify that SD-055's dense softmax-mean preserves CEM's *elite* semantics tightly; a broad average can dilute the very selectivity CEM relies on (this is the caveat the companion Sander et al. 2023 entry develops). Second, DCEM fine-tunes a learned controller objective, whereas SD-055 deliberately keeps ARC-007's value-flat residue-terrain scoring with no new value head — so the *objective* being differentiated is not the same. The precedent is methodological, not an identical-task result. Failure modes to watch: if the score→`action_bias` path through the E2 rollouts carries near-zero usable gradient, the differentiable selection would faithfully restore a path that transmits no signal; and DCEM itself reports the soft relaxation is not uniformly better than vanilla CEM, so a null result in REE would be consistent with the literature rather than a refutation.

## Why included

It is the canonical, peer-reviewed source establishing the exact technique SD-055 implements, applied to the exact class of operation (CEM elite selection inside a planner). No other single paper maps as directly onto the claim.
