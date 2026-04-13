# Toward Causal Representation Learning -- Scholkopf et al. (Proceedings of the IEEE, 2021)

## The Foundational Problem

Scholkopf and colleagues begin from an observation that is simple to state but widely underappreciated in practice: a statistical model trained on observational data learns P(y|x) -- the conditional distribution, which encodes correlation. When we ask the model an interventional question -- what would happen if I set x to some value, rather than conditioning on observing x to take that value -- we are asking about P(y|do(x)), which is a different distribution. These two distributions coincide only when there are no unobserved confounders, i.e., no hidden variable that influences both x and y. In the presence of confounders, P(y|x) and P(y|do(x)) can diverge arbitrarily, and a model trained to minimize prediction error on P(y|x) will give systematically wrong answers to interventional queries.

## The SD-013 Derivation

This is the paper cited in the SD-013 claim notes as the foundational source -- not merely adjacent evidence but the theoretical basis from which the claim was constructed. The translation is direct. E2_harm_s is trained to minimize prediction error on P(z_harm_s_next | z_t, a) using trajectories collected by the behavioral agent. But when it is queried during causal_sig computation -- E2_harm_s(z_t, a_cf) -- it is being asked an interventional question: what harm would result if the agent had taken a_cf from state z_t? This is P(z_harm_s | do(a_cf)), not P(z_harm_s | a_cf, behavioral_policy). In confounded states where the behavioral policy's state-occupancy pattern correlates with harm, these diverge. The observational model answers the wrong question.

## Why i.i.d. Assumptions Break

Scholkopf et al. emphasize that standard ML relies on i.i.d. data drawn from a fixed distribution. Interventions break this assumption: when an agent executes a_cf rather than a_actual, it changes the causal chain that determines z_harm_s. The data distribution shifts. A model trained on the pre-intervention distribution will not generalize to the post-intervention distribution unless it has learned the causal structure rather than the correlational structure. The paper notes that this is not a generalization problem in the usual sense -- collecting more data from the same distribution will not solve it. The problem is that the model is learning the wrong thing, precisely because it is given the right thing for the wrong task.

## The Necessity of Interventional Data

The paper identifies the conditions under which the interventional distribution can be recovered from observational data: when the causal graph is known and satisfies the backdoor or front-door criterion, or when instrumental variables are available. In environments where these conditions do not hold -- and REE's harm-proximal state occupancy confounding is likely to violate them -- interventional data is a necessity, not an option. ARC-033's counterfactual perturbation requirement is the practical implementation of this necessity: by executing a_cf from the same confounded state, E2_harm_s receives training signal that is genuinely interventional -- drawn from P(z_harm_s | do(a_cf)) rather than from the behavioral policy's correlated distribution.

## Summary

Scholkopf et al. (2021) provide the theoretical foundation for SD-013. The distinction between observational and interventional distributions, the identification conditions under which the interventional distribution is recoverable from observational data, and the necessity of interventional samples when those conditions are unmet -- these are the three pillars of the SD-013 argument, all sourced from this paper. The claim notes cite it explicitly as the basis for the argument that ARC-033 must include explicit counterfactual perturbation steps. Of the four entries in this review, this one carries the highest confidence precisely because it is the source from which SD-013 was derived.
