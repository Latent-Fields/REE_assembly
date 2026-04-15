# Counterfactual credit assignment: disentangling what the agent did from what the world did

**Source:** Mesnard et al. (2021), ICML 2021. arXiv: 2011.09464

## The problem

Reinforcement learning faces a fundamental attribution problem: when an agent receives a reward (or punishment), how much of it was due to the agent's own action versus factors outside its control? A good policy should be reinforced when it genuinely caused a good outcome, not when it was merely present during a lucky run of environmental events. The same logic applies to harm avoidance: an agent should not be burdened with residue from harm it did not cause. This is exactly the problem MECH-072 addresses from the REE side. Mesnard et al. address it from the computational RL side.

## The approach

The key insight is counterfactual conditioning. Rather than asking "what reward followed this action?" (which conflates agent and environment contributions), ask "what would the future trajectory have looked like from this state without this action?" The difference between the actual outcome and the counterfactual is the agent's causal contribution.

Mesnard et al. formalise this as a hindsight baseline: a value function conditioned on future trajectory information that excludes information about the agent's actions. By learning to extract the environmentally-determined component of future returns from trajectory data -- while explicitly constraining out action information to avoid bias -- the method isolates the action's causal effect on the outcome. The resulting policy gradient estimators have provably lower variance than standard baselines.

## Why this matters for MECH-072

MECH-072 proposes a discriminator gate on residue accumulation: harm residue should accumulate only when the harm was foreseeable and agent-caused. The core operation MECH-072 requires is a decomposition of the harm signal into agent-caused and environmentally-caused components. Mesnard et al. provide the theoretical framework for this decomposition: it is counterfactual conditioning, and it can be done with provably low variance.

The specific implementation in REE is different -- rather than a trajectory-based hindsight baseline, REE uses the E2 forward model to compute z_world_delta (the world-state change attributable to the agent's action) and a learned discriminator on (z_world_delta, is_agent_caused) pairs. But the theoretical principle is identical: partition the outcome signal by conditioning on a counterfactual that removes the agent's contribution.

The EXQ-213 result -- 0.0 false attribution rate with gating vs 0.478 without -- can be understood as an empirical demonstration of exactly what Mesnard et al. prove theoretically: counterfactual partitioning dramatically reduces credit misassignment.

## What remains open

Mesnard et al. work with generic reward signals; MECH-072 applies gating specifically to the harm residue channel. Whether harm signals have distinct learning dynamics (e.g., asymmetric learning rates for aversive outcomes, interactions with the commitment boundary) that require modifications to the generic counterfactual framework is not addressed by this paper. Additionally, Mesnard et al. require that hindsight information exclude action data to avoid bias; in REE, the discriminator receives both z_world_delta and is_agent_caused, which means the gate is explicitly conditioned on action information. Whether this introduces bias under certain conditions is worth examining.
