# Understanding the Role of Equivariance in Self-supervised Learning — Wang et al. (2024)

## Relevance to Q-014

Q-014 asks whether JEPA's invariances hide ethically relevant distinctions in REE attribution contexts. The adjudication is hybridize, meaning the concern is real but not fatal -- some architectural combination might preserve what is needed. Wang et al. provide the theoretical backbone for why this concern is well-founded, and why the hybridize conclusion requires specificity about which invariances are retained and which discarded.

## The core argument

The information-theoretic framework Wang et al. develop establishes that invariant SSL methods -- including JEPA-style architectures -- achieve invariance by discarding variation. This is not a bug in the implementation; it is the mechanism. The encoder is trained to map augmented versions of the same input to the same latent representation. The discarded variation is, by construction, whatever the invariance objective treats as noise.

The problem arises when 'noise' from the perspective of the training augmentation protocol overlaps with 'signal' from the perspective of a downstream task. Wang et al. show this happens systematically for equivariant tasks -- tasks that require sensitivity to exactly the transformations the invariant model was trained to ignore. The information gap is not small: equivariant SSL methods that preserve both channels outperform invariant-only methods by margins that correlate with the degree of task-augmentation overlap.

## The ethical blind spot mechanism for REE

Q-014 is about a specific version of this problem. In REE attribution, the agent must determine the causal structure of a harm event: was the harm agent-caused or environment-caused? Did the agent's action produce the adverse outcome, or would it have occurred anyway? These distinctions can look very similar in a learned latent space if the relevant features -- the specific causal structure of the event trajectory -- are suppressed by JEPA's invariances.

Consider what JEPA's invariance is typically trained against: variations in irrelevant perceptual context, camera viewpoint, surface texture, lighting. Now consider that in a world model trained on interaction data, similar variability can exist at the level of event type: two trajectories that reach the same terminal state via different causal routes. If the world model's invariance objective treats causal-route variation as noise -- because it is not predictive of the terminal state -- then the latent representation of those two trajectories will be indistinguishable. E3's attribution step then has no signal to work with.

This is the ethical blind spot Q-014 identifies: not that JEPA is deliberately unfair, but that its invariance mechanism can structurally suppress the distinctions required for causal moral attribution.

## What hybridize requires

Wang et al.'s framework also points toward the remedy. The explaining-away synergy in equivariant SSL recovers the suppressed information by requiring the representation to simultaneously support equivariant prediction. Applied to REE: a JEPA-based E1 that is also trained with an equivariant objective over causal event-type labels would retain the attribution-relevant features. The hybridize conclusion is therefore defensible, but it requires a specific architectural addition -- not just JEPA as standardly deployed.

## Calibration note

Confidence is set at 0.70. The source quality is high and the mechanism is well-established in the visual domain. The mapping caveat is real: temporal dynamics modelling involves different information types than static image augmentation, and the specific claim that JEPA-in-REE suppresses causal attribution features has not been directly tested. The evidence supports the hypothesis as a well-grounded theoretical concern, not yet as an empirically confirmed failure in the REE-specific architectural context.
