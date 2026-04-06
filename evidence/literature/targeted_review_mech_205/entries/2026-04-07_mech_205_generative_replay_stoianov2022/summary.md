# The hippocampal formation as a hierarchical generative model supporting generative replay and continual learning

**Stoianov, Maisto & Pezzulo, 2022, Progress in Neurobiology**

## What the paper does

Stoianov et al. propose a computational model of the hippocampal formation as a three-level hierarchical generative model: the first level encodes individual experience items, the second organises these into sequential patterns, and the third clusters sequences into spatial maps. The model is implemented as a hierarchical variational autoencoder and tested on simulated rodent navigation trajectories.

## Key findings relevant to MECH-205

The central contribution is formalising *generative replay* as "the offline resampling of fictive sequences from the generative model." This is not rote re-presentation of stored episodes -- it is sampling from the learned distribution, which can produce novel sequences with the same statistical structure as experienced trajectories but not identical to any specific experience. The model demonstrates that this generative replay supports continual learning without catastrophic forgetting: by regularly resampling from learned maps during offline periods, old memories are maintained while new ones are integrated.

The hierarchical structure is particularly relevant: the three levels (items -> sequences -> maps) parallel REE's representational hierarchy (z_gamma events -> trajectories in E2 rollouts -> viability map in the hippocampal module). Generative replay at the sequence level produces variations on experienced trajectories -- exactly what MECH-205 claims happens when the hippocampus generates counterfactual variations during offline phases.

## Mapping to REE

The generative replay mechanism maps directly onto MECH-205's claim that replay produces counterfactual variations via E2 rollouts. The key insight is that the hippocampus is not a tape recorder -- it is a generative model that can sample new sequences from its learned distribution. In REE terms, this means the hippocampal module can generate "what if" trajectories for E1/E2 to train on, expanding the training set beyond direct experience.

However, Stoianov et al. do not model *prioritisation*. Their generative replay samples from the learned distribution without any surprise-gating or prediction-error-based scheduling. MECH-205 claims that replay is both generative AND surprise-prioritised; this paper provides strong theoretical grounding for the first half but is silent on the second.

## Limitations

The model is tested on simulated spatial navigation only. The generative mechanism may not straightforwardly extend to affective or harm-related content, which is central to MECH-205's connection to the residue field and viability map consolidation. The uniform sampling (no prioritisation) is a significant gap relative to MECH-205's surprise buffer.

## Confidence reasoning

Strong theoretical framework in a good venue. High mapping fidelity for the generative aspect; absent mapping for the surprise-gating aspect. Overall confidence 0.75.
