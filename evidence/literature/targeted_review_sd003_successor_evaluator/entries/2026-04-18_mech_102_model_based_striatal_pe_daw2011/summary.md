# Daw, Gershman, Seymour, Dayan, Dolan (2011). Model-based influences on humans' choices and striatal prediction errors. *Neuron*.

## What the paper does

By 2011 the model-free/model-based split in reinforcement learning had been a theoretical framework for twenty years, but behaviorally dissociating them in human experiments had proved slippery. The Daw paper introduced the two-step task -- a Markov decision problem with a first-stage choice leading probabilistically to one of two second-stage states, each with its own reward structure -- and showed that human behavior was unambiguously a mixture. Some subjects weighted model-based control (using knowledge of transition probabilities to compute expected second-stage value) more heavily; others leaned on model-free cached stimulus-response learning. The experimental design lets you read the weighting off the choice data directly.

Then they did the same analysis in the scanner. Ventral striatum, which the previous decade had treated as the canonical substrate of model-free reward prediction error, turned out to carry both signals at the same time: the model-free prediction error you would expect, and -- additionally -- a prediction error computed against a model-based value estimate that took the transition structure into account. The mixing weight in the fMRI signal correlated with the mixing weight in behavior.

## Findings and what they force

Two things follow from this that matter for our question. First, forward-model-based (model-based) evaluation in humans is not a niche strategy used only in explicit deliberation; it is continuously present and continuously feeding downstream prediction-error signals. The evaluator mode is a real mode, measurably active. Second -- and this is the subtle one -- the *comparator operation* (the prediction-error computation at outcome time) draws on outputs from *both* the forward-model-based system and the cached-value system. The substrate for the post-hoc comparison is not segregated by which source generated the expected value; ventral striatum is running one comparator over mixed expected-value inputs.

## REE mapping

For ARC-018 and MECH-033, the paper supports the general architecture that forward-model rollouts feed value estimation. For the SD-003 successor's central question -- is the evaluator substrate the same as the comparator substrate, or separate? -- the Daw result is actually informative in a way I did not fully expect going in. If the biological comparator (ventral striatum prediction error) integrates outputs from multiple evaluator systems, then a clean REE split where "the forward model used in evaluator mode is a different module from the comparator" would be going against a pattern the Daw paper demonstrates. That is, biology seems to favor a shared comparator that takes inputs from multiple forward-model sources, rather than a dedicated comparator paired one-to-one with each forward model.

For MECH-102 (violence as terminal error correction), the relevance is softer. The Daw result tells us what normal-mode evaluation looks like; terminal-error-correction behavior implies some collapse or bypass of this mixed system. That is a story worth developing later but is not directly in the paper.

## Where the mapping is imperfect

The forward model at issue in Daw is an abstract state-transition model of a cognitive task, not a harm forward model. The biological mapping runs through ventral striatum not vmPFC/OFC, and the striatal signal is a prediction error, not the pre-action value estimate per se. So the paper tells us about the comparator end of the pipeline (striatal PE) and constrains the inputs to that comparator (mixed model-based + model-free); it does not directly record the upstream forward model.

A second limit: the two-step task probes abstract state transitions, not the kind of domain-specific forward model (E2.world_forward, E2_harm_s) REE is architecting. Transferring the "shared comparator accepts mixed forward-model inputs" inference from abstract task to stream-separated REE is a real inferential step. If REE's stream separation is biologically real and simply not probed by the Daw paradigm, the mapping weakens.

## Confidence reasoning

Source quality very high -- Neuron, Daw, thousands of citations, definitional paper. Mapping fidelity good for the forward-model-based evaluator existing and feeding downstream value; moderate for the stream-separation question, where the paper's shared-comparator finding is actually mildly weakening for a strict REE split. Transfer risk moderate -- abstract task domain, not harm. Confidence 0.78.
