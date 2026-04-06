# Prioritized memory access explains planning and hippocampal replay

**Mattar & Daw, 2018, Nature Neuroscience**

## What the paper does

Mattar and Daw derive a normative theory of which memories should be replayed, starting from first principles in reinforcement learning. Rather than asking "what does the hippocampus replay?" they ask "what *should* it replay, if the goal is to maximally improve future decisions?" The answer is a DYNA-like framework where replay events are prioritized by the product of two terms: *gain* (how much would updating this state's value change the agent's policy?) and *need* (how likely is the agent to visit this state soon?).

## Key findings relevant to MECH-205

The gain term is directly prediction-error-dependent: states whose values changed unexpectedly -- because reward was surprising or transitions were novel -- have high gain. This captures the core of MECH-205's surprise-gating: surprising experiences are replayed more because updating their representation yields the largest behavioural improvement. The model predicts reverse replay after unexpected reward (gain-dominated, propagating the surprise backward through the trajectory) and forward replay before runs (need-dominated, preparing for imminent states). Both patterns match empirical observations.

Critically, the model also shows that replay can *compose* novel sequences from separately experienced trajectory segments. This is not rote re-presentation -- it is generative, assembling counterfactual paths the agent never actually traversed. This maps onto MECH-205's claim that hippocampal replay generates variations rather than simply re-presenting cached episodes.

## Mapping to REE

The gain x need framework maps onto MECH-205 with a refinement: MECH-205 uses raw prediction error magnitude as the priority, while Mattar & Daw use *policy-relevant* prediction error -- surprise matters only insofar as it would change behaviour. This is a more selective criterion. One could argue REE's surprise buffer should incorporate a need-like term (is this model region relevant to the agent's current viability landscape?), which would sharpen the claim.

The compositional sequence generation maps onto MECH-205's E2 counterfactual rollouts: the hippocampus doesn't just replay what happened, it generates what *could* have happened, training the forward models on these counterfactuals. The implicit termination criterion (replay utility falls below threshold as the value function converges) maps onto MECH-205's convergence-based deprioritisation.

## Limitations

The model is designed for planning replay (awake, between decisions), not offline sleep replay. The prioritisation logic may differ during sleep, where the "need" term is undefined (no imminent behaviour). The framework assumes discrete state spaces and tabular value functions, which is a simplification relative to REE's continuous latent spaces.

## Confidence reasoning

High source quality (Nature Neuroscience, widely cited, normative derivation). Mapping fidelity moderately high -- the gain term captures surprise-gating, but the need term and policy-relevance filter are not part of MECH-205. Transfer risk low: the framework is general RL, not tied to a specific species or task. Overall confidence 0.82.
