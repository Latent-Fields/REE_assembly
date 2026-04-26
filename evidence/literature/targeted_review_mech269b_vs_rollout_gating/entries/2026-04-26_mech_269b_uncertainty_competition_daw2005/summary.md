# Daw, Niv & Dayan 2005 -- Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control

## What the paper did

Daw, Niv & Dayan formalised a long-standing observation in animal learning -- that goal-directed and habitual behaviours coexist and that one or the other dominates depending on training, environmental volatility, and task structure -- as Bayesian arbitration between two reinforcement-learning controllers. The prefrontal cortex hosts a model-based system that uses an internal world model to plan; the dorsolateral striatum hosts a model-free system that caches state-action values from experience. Each system maintains its own uncertainty estimate, and the system with lower uncertainty controls behaviour. The paper showed that this arbitration principle reproduces a wealth of empirical findings about when habits form, when they break down, and when deliberation takes over.

## Key findings relevant to MECH-269b

This is the closest available precedent for tag (b) symmetric application of a reliability signal across architecturally-distinct world-model systems. Daw et al. argue that a single uncertainty signal arbitrates between two computationally-distinct controllers, each with its own model of the world (model-based vs cached). MECH-269b makes a structurally analogous claim: a single V_s signal gates contributions from architecturally-distinct world-model substrates -- the hippocampal proposer (model-based, episodic, fast-learning) and the cortical forward predictors E1 / E2 (model-based, slow-learning, generalising).

This is the only paper in the anchor list that engages directly with the symmetric question MECH-269b asks: when two distinct architectures hold different opinions about a state, can a single reliability signal arbitrate between them? The principle (uncertainty as cross-architecture arbiter) maps cleanly. The implementation (cross-system action arbitration vs within-loop weighting) differs.

## How the findings translate to REE

Daw, Niv & Dayan supply the structural precedent for MECH-269b symmetric-application novelty. The principle that a single reliability signal can arbitrate between two architecturally-distinct world-model systems is established here. MECH-269b extends the principle in two ways. First, rather than arbitrating action-selection between MB and MF systems, V_s gates within-loop contribution from hippocampal proposer (the MB-analog) and cortical forward predictors (E1, E2, the MB-cortical analog). Second, the gating is per-stream rather than per-system: V_s is computed for each latent stream and applied to that stream contribution wherever it appears in the loop.

## Limitations and caveats

Three caveats. First, Daw et al. arbitrate between two distinct action-selection systems. MECH-269b proposes V_s gates contributions to a single shared planning loop from two complementary substrates within that loop. The structural analogy holds (uncertainty-as-arbiter) but the specific architecture is different. Second, the paper does not test the prediction that the same uncertainty signal driving arbitration is also computed and consumed in the hippocampus -- they treat hippocampus as a contributor to the model-based system rather than as an architecturally-distinct precision-gated module. The symmetric-cortical-vs-hippocampal precision claim is implied by the framework but not directly tested. Third, the paper is computational rather than empirical-biological, so the arbitration signal is not directly measured.

## Confidence reasoning

Confidence 0.58 -- mixed support for MECH-269b symmetric-application novelty. Source quality high (Nature Neuroscience, foundational computational paper). Mapping fidelity moderate-low: the structural analogy (uncertainty as arbiter between distinct world-model substrates) is good, but the specific architecture (cross-system action arbitration vs within-loop per-stream weighting) differs meaningfully. Transfer risk noticeable because the extension from action-arbitration to per-stream-rollout-gating is a forward step that this paper does not directly support. This is the closest precedent in the anchor list for the symmetric-application novelty, but it is genuinely a precedent rather than direct evidence -- which is why this entry is the lowest-confidence in the review and why the symmetric-application novelty remains the principal gap MECH-269b carries.
