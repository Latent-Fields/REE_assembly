# Young (1993) — The Evolution of Conventions

## What the paper did

H. Peyton Young modeled a society as n players drawn each period from a large finite population to play a coordination game. Each player observes a sample of recent history and chooses a best response to that sample. Occasionally, players make random errors (mutations). Young proved that as the error rate goes to zero, only certain equilibria -- the stochastically stable ones -- survive: they have positive probability in the limiting stationary distribution. He provided a graph-theoretic algorithm for computing stochastically stable states via "paths of least resistance" between equilibria, and showed that in 2x2 games the risk-dominant equilibrium is stochastically stable, and in potential games the potential-maximizing equilibrium is selected.

## Key findings

The central conceptual move is that small persistent random perturbations (errors, mutations, exploration) allow the system to escape any locally stable equilibrium, but do so with unequal resistance -- it is much easier to transit to some equilibria than others. Stochastic stability formalizes which equilibria are the most robust long-run attractors. The path-of-least-resistance calculation is a graph-theoretic algorithm on the Markov chain defined by the transition probabilities between equilibria under the error process. In potential games, this calculation simplifies: the potential-maximizing equilibrium is always stochastically stable.

## REE translation

Q-023 asks whether a multiagent REE system can be formally shown to converge to ethical attractors. Young (1993) gives the stochastic stability argument for why even noisy, boundedly rational agents converge to the right equilibrium in the long run. If REE multiagent systems can be modeled as agents sampling from interaction history and approximately best-responding, then Young's result says: given any positive exploration rate, the long-run behavior concentrates near the potential-maximizing equilibrium. If REE's potential function encodes aggregate harm cost (via ARC-034 and INV-028), the potential-maximizing equilibrium is the ethical attractor. Stochastic stability then becomes the formal certificate that the ethical attractor is *selected* under realistic noisy learning, not merely *existing* as a mathematical fixed point.

The notes in Q-023 flag that MECH-127 (counterfactual utility) may break the standard potential game framework, requiring extension to pseudo-potential games or interdependent-types frameworks. Young's result applies cleanly only if the potential game structure holds. Without it, the path-of-least-resistance calculation still applies in principle, but the stochastically stable set may not be the potential-maximizing equilibrium and may be harder to characterize.

## Limitations and honest caveats

Young's agents use adaptive sampling (bounded rationality with memory), which is stylized relative to REE's learning dynamics. The mutation process corresponds to exploration noise in REE -- a reasonable identification, but one that needs to be made precise. The framework is for finite populations and finite strategy spaces; extension to continuous strategies or large populations requires additional technical work. Most importantly, as with Monderer and Shapley, the entire apparatus is conditional on the potential game structure holding -- a condition that MECH-127 may violate.

There is also a conceptual subtlety: stochastic stability selects among Nash equilibria -- it does not guarantee that the selected Nash equilibrium is *desirable* in any ethical sense. The ethical valence of the selected attractor depends entirely on whether REE's payoff structure correctly encodes the harm penalty. If REE utility has subtle misalignments, stochastic stability will faithfully select the wrong attractor.

## Confidence reasoning

Econometrica 1993 -- a foundational result in evolutionary game theory with nearly certain proofs within its formal scope. Confidence limitation is entirely in the mapping: does REE's utility structure satisfy the potential condition? Are REE agents' learning dynamics sufficiently Markovian? Is the selected Nash equilibrium actually the ethical attractor? Overall confidence 0.72 -- the framework is exactly the right formal tool for Q-023 if the potential condition can be established.
