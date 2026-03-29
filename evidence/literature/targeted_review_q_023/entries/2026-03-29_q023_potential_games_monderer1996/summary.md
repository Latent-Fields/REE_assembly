# Monderer & Shapley (1996) — Potential Games

## What the paper did

Monderer and Shapley introduced and characterized potential games -- a class of strategic-form games where the incentive structure for every player can be captured by a single global "potential function." They defined four types of potential (exact, weighted, ordinal, generalized ordinal), characterized each by necessary and sufficient conditions, and proved the central convergence result: finite games with an ordinal potential function have the Finite Improvement Property (FIP), meaning every sequence of unilateral better-reply moves terminates at a pure Nash equilibrium. They also proved equivalence between exact potential games and congestion games, and showed that fictitious play converges in any potential game.

## Key findings

The key theorem is that the potential function is strictly increasing along every improvement path, so improvement paths in finite games are necessarily finite and terminate at equilibria. The practical implication is that distributed, selfish best-response learning -- with no coordination, no communication, and minimal rationality requirements -- will converge to stable equilibria in any potential game. For ordinal potential games, the potential function need only track the sign of payoff differences (not the magnitude), making the condition easier to satisfy than exact potential while still guaranteeing FIP.

## REE translation

Q-023 asks whether a REE multiagent system converges to ethical attractors. Monderer and Shapley's framework is the mathematical gateway. If we can show that the joint payoff structure of REE agents -- incorporating ARC-034's other-cost-aversion, INV-028's harm internalization, and MECH-127's counterfactual utility -- constitutes an ordinal potential game, then convergence to Nash equilibria follows immediately from FIP. The ethical attractor is then the potential-maximizing Nash equilibrium, which under REE's harm-penalizing potential function would correspond to the joint strategy minimizing aggregate harm cost.

The Q-023 notes flag that MECH-127 (counterfactual utility) "may break standard framework, extending to pseudo-potential games or interdependent-types framework." Monderer and Shapley's paper provides the precise formal criterion against which to check this: does the counterfactual utility structure preserve the ordinal potential condition? If yes, FIP applies. If not, we need a generalized potential or an alternative convergence argument. This is not a resolved question -- it is the core open formal problem that Q-023 is asking.

## Limitations and honest caveats

The potential game framework is for finite strategy spaces; REE agents' action spaces are in general continuous (or high-dimensional discrete). Extension to continuous action spaces requires differentiability conditions not covered by this paper. More importantly, convergence to a Nash equilibrium is not the same as convergence to an *ethical* attractor: Nash equilibria include outcomes that are equilibria for the wrong reasons (coordination on mutual defection, for instance). The ethical valence of the Nash equilibrium depends on what the potential function rewards -- and building the right potential function into REE's utility structure is itself an unsolved design problem. Monderer and Shapley give you the convergence machinery; they do not guarantee that what you converge to is good.

## Confidence reasoning

This is a foundational mathematical paper with essentially certain results within its scope. The confidence limitation comes entirely from the mapping gap: whether REE's utility structure satisfies the ordinal potential condition, especially given MECH-127's counterfactual term. Overall confidence 0.75 -- the framework is directly applicable if the potential condition holds, and provides the exact mathematical criterion for Q-023 to resolve.
