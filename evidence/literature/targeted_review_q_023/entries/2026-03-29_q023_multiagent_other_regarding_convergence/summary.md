# Leonardos et al. (2022) — Global Convergence of Multi-Agent Policy Gradient in Markov Potential Games

## What the paper did

Leonardos, Overman, Panageas, and Piliouras extended the potential game convergence result from normal-form games to Markov games. They defined Markov Potential Games (MPGs) as Markov games possessing a state-dependent potential function: whenever an agent changes its policy while others hold theirs fixed, the change in that agent's value function equals the change in the potential function's value. They then proved the first global convergence result for independent policy gradient -- each agent updates only its own policy, with no coordination or communication -- converging to a Nash equilibrium policy in O(1/epsilon^2) iterations.

## Key findings

The central result is that despite the sequential, state-dependent structure of a Markov game (as opposed to the static, one-shot structure of normal-form games), the potential game convergence property extends under the MPG definition. Each agent running gradient ascent on its own value function, independently, collectively converges to a Nash policy. Crucially, this is a *global* convergence result, not just a local one -- the system does not get stuck in suboptimal equilibria. The proof adapts the gradient dominance property from single-agent MDPs to the multi-agent setting.

A notable subtlety flagged by the authors: MPGs do not decompose into per-state potential games in general. A Markov game where every state is a potential game is not necessarily a MPG, and conversely MPGs can have state-games that are zero-sum. The MPG condition is a joint property of policies and value functions over the full sequential structure.

## REE translation

For Q-023, Leonardos et al. provide the sequential generalization of Monderer and Shapley that REE needs. REE agents operate in a Markov decision process (states, transitions, multi-step rollouts) -- not a static one-shot game. The relevant formal question is whether REE's joint utility structure satisfies the MPG condition: does there exist a state-dependent potential function such that each agent's value change from a unilateral policy change equals the potential change? If yes, global convergence of independent policy gradient to Nash policies follows.

The ethical attractor interpretation: if REE's potential function is the negative of aggregate harm (consistent with ARC-034's other-cost-aversion), then the Nash policy that maximizes the potential is the joint harm-minimizing policy. Leonardos et al.'s convergence result then certifies that REE agents, running independent RL, converge globally to the joint policy that minimizes aggregate harm -- i.e., to the ethical attractor.

Q-023's notes flag that MECH-127 (counterfactual utility) "may break standard framework, extending to pseudo-potential games or interdependent-types framework." Leonardos et al.'s result already handles the sequential structure; the remaining question is whether MECH-127's counterfactual terms are compatible with the MPG potential condition. This is a specific, tractable mathematical question -- one that Q-023 should ultimately resolve.

## Limitations and honest caveats

The convergence proof is for tabular settings with known rewards and transitions. REE agents use neural network function approximation and learn rewards from experience -- extending the convergence guarantees to this setting requires additional regularity conditions that are not established here. The O(1/epsilon^2) sample complexity assumes direct policy parameterization; neural network policies in REE's continuous action space may have very different convergence profiles.

More fundamentally, MECH-127's counterfactual utility -- payoff depends on what would have happened without the agent's action -- may not be expressible as a standard policy-conditioned value function, which is what the MPG potential is defined over. If counterfactual utility introduces non-Markovian dependencies, the MPG framework needs extension. The paper does not address pseudo-potential or approximate-MPG cases, which may be where REE actually lives.

## Confidence reasoning

ICLR 2022 with a novel and important formal result. Source quality is high. The mapping requires two additional conditions (MPG structure holds for REE's utility, and the Nash policy is the ethical attractor) that are unproven. Transfer risk is elevated for the function approximation extension. Overall confidence 0.70 -- the framework is precisely the right tool if the MPG condition can be verified for REE, and the paper gives us the exact mathematical criterion to check.
