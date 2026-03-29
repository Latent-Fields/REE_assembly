# SafeDreamer: Safe Reinforcement Learning with World Models — Huang et al. (2024)

## Relevance to Q-012

There is a version of the Q-012 debate that could remain entirely theoretical: perhaps latent world models are in principle unsafe without explicit constraints, but this failure is hypothetical or only emerges at scales we do not yet deploy. SafeDreamer removes that escape route. Using DreamerV3 -- one of the architectures most directly implicated in Q-012 -- the paper demonstrates empirically that world-model-based agents fail safety criteria when no explicit constraint is added, and that the remedy requires a structurally separate objective pathway.

## What the paper shows

The authors take DreamerV3 and evaluate it on Safety-Gymnasium, a benchmark suite for constrained RL. Standard DreamerV3 without safety modification "often fails to achieve zero-cost performance in complex scenarios, especially vision-only tasks." The failure is attributed to two related causes: model inaccuracies in the world model (imagined rollouts diverge from reality) and insufficient sample efficiency, which together mean the agent cannot reliably distinguish safe from unsafe imagined trajectories.

The SafeDreamer fix integrates Lagrangian-based constraint optimisation into the planning process: the agent plans in imagination using the world model's latent space but must now satisfy a cost constraint as well as maximise reward. With this addition, the system achieves near-zero safety cost across tasks that vanilla DreamerV3 fails.

The key architectural insight is that the safety signal cannot simply be folded into the reward. The Lagrangian formulation maintains it as a structurally separate term that cannot be traded off against reward by adjusting the reward scale.

## The REE parallel

REE's response to the same failure mode takes a different form but is motivated by the same observation. Rather than adding a Lagrangian penalty at optimisation time, REE builds a dedicated harm-signal pathway (z_harm, E3 evaluation) that is architecturally separate from the world-model and prediction-error channels. The logic is the same: harm cannot be reliably encoded in the reward signal because capable optimisers will find ways to trade off reward components, but a separate channel with its own gradient cannot be absorbed in that way.

There is a meaningful difference worth tracking. Lagrangian constraints are a mathematical technique applied to a unified optimiser; REE's harm stream is a distinct architectural module with its own forward model and training signal. It is not obvious that these are equivalent at scale. A sufficiently capable planner might in principle find policies that satisfy the Lagrangian constraint in the learned world model while violating it in the real environment -- which is precisely the imagined-rollout problem that SafeDreamer's authors acknowledge as a limitation.

## Calibration note

Confidence is 0.80 -- the highest assigned across Q-012 entries -- because this paper directly tests DreamerV3 in the relevant failure mode and provides a constructive existence proof: the failure is real, and structural addition is required to fix it. The main caveat is scope: Safety-Gymnasium costs are engineering constraints (collisions, velocity limits), not ethical harm in the REE sense. The transfer from 'safety cost' to 'harm' as REE defines it involves a conceptual gap that the paper does not bridge. The analogy is sound but should not be read as validation of REE's specific harm architecture.
