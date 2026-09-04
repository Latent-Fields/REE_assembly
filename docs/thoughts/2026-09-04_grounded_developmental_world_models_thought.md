# Grounding development in organismic constraints before abstract world models

**Date:** 2026-09-04  
**Status:** Research-bounded thought intake  
**Scope:** Developmental learning, grounded world models, self/world distinction, affordances, intrinsic information seeking  
**Source:** Pezzulo et al. (2026), [*Grounded world models in biological organisms and future artificial intelligence*](https://arxiv.org/abs/2607.13560) (perspective article; July 2026).

## Core proposition

A developmental REE should not begin by treating the world as an unstructured external object that must first be fully inferred. It begins as an organism with a body, needs, vulnerabilities, action capacities, and consequences. Those constraints make some distinctions meaningful before the agent has a rich world model: safe/unsafe, controllable/uncontrollable, sustaining/depleting, self-generated/external, approach/avoid, familiar/novel.

World structure is then discovered through active engagement from this organismic foothold. In this sense, the developmental order is:

```
viability and action → sensorimotor regularities → affordances and controllability
→ objects/places/episodes → other agents and their trajectories
→ abstract schemas, language, and social norms
```

This is not a claim that each level is fully completed before the next begins. They overlap. It is a claim about dependency: later representations should remain answerable to earlier organism-world relations.

## What the source adds

Pezzulo et al. synthesise evidence and theory around grounded world models in biological organisms. Their central contrast is between biological learning—continuous, active, embodied, intrinsically motivated, and regulated by interoceptive/allostatic needs—and conventional artificial intelligence training, which is often passive, externally curated, and only later coupled to action.

This is a perspective, not direct evidence for a single implementation. Its particular value is that it names a coherent set of design pressures that can be checked against REE: active sensing, exploration, affordances, allostasis/interoception, self-versus-world discrimination, and the gradual addition of social models and intentions.

## Connection to current REE development

REE already has unusually strong ingredients for this framing: a self that must persist, valenced consequences, an environment that supports harm and benefit, developmental staging, and emerging questions around observation → z_world → E1/E2 rollout. The source does not say that the current latent interface is wrong. It provides a red-team criterion for it:

> Does the representation preserve distinctions that are actionable for this organism before it preserves distinctions that are merely descriptive to an observer?

A successful z_world should therefore not be judged only by reconstruction or generic rollout accuracy. It should preserve the variables that allow the agent to decide whether a state is dangerous, beneficial, controllable, self-caused, informative, or relevant to another agent.

## Proposed developmental invariants

The following are candidates for protected representational invariants across expansion of the world model:

- bodily/organismic condition and threats to continuation;
- action availability and expected controllability;
- outcome valence and uncertainty;
- self-generated versus externally generated change;
- spatial and temporal relation to resources, obstacles, and agents;
- evidence that another entity has an independently evolving trajectory.

These are not necessarily literal latent dimensions. They are preservation requirements: if a compression or abstraction destroys all access to one of them, it should be treated as a possible developmental regression.

## Testable consequences

1. A staged agent grounded first in survival, controllability, and affordances should transfer more robustly to new world layouts than an equally sized agent trained directly on abstract task labels.
2. Representations that retain controllability and self/world information should support safer exploration under novelty than representations optimised only for next-observation prediction.
3. Social attribution should become more accurate when the system first learns that some observed changes are external and some are self-caused, before it is asked to infer intentions.
4. Developmental learning should show an identifiable transition: agent models become useful only once the environment contains independent trajectories whose behaviour cannot be compressed as static affordances.

## Near-term REE use

For V3, this is chiefly an evaluation and interface-design thought, not a request to enlarge the organism immediately. The current directional resource-field work is directly relevant: whether z_world preserves resources in an action-relevant form is a concrete test of groundedness.

For later social environments, the thought suggests a curriculum rather than an additional ethics module:

1. learn self-preservation and controllability;
2. learn objects/resources and reversible action consequences;
3. encounter independent agents whose trajectories must be modelled;
4. learn that actions can alter another agent's prospects;
5. develop cooperative or reparative policies under shared vulnerability.

The ethical dimension is thereby tested as an emergent property of world/self/other modelling under the axiom set, rather than supplied as disembodied instruction.

## Candidate downstream fan-out

- **Evaluation requirement:** add action-relevant information-retention probes to z_world and E1/E2 validation, starting with resource direction, controllability, and self-caused change.
- **Candidate claim:** developmental curriculum should be ordered by the appearance of new environmental regularities and action consequences, not merely by task difficulty.
- **Experiment seed:** compare an affordance/controllability-supervised z_world with a reconstruction-matched baseline on out-of-layout generalisation and harm avoidance.
- **Social design note:** introduce independent agent trajectories only after the agent can distinguish self-caused from externally caused events.
