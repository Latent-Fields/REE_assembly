# Bursztyn et al. (2006) -- Neural Correlates of Internal-Model Loading

## What the paper did

Bursztyn and colleagues, working in the Kawato lab, ran an event-related fMRI experiment to identify the neural correlates of internal model recruitment. Subjects practiced manipulating an object with unusual dynamics (resistive, assistive, or null force field), and then performed three conditions in the scanner: (1) grasping and moving the trained object, (2) moving in free space without the object, and (3) applying isometric force to the object without moving it. The key contrast was between conditions requiring versus not requiring recruitment of the learned internal model. Crucially, the model had to be loaded during a preparation period (between cue and go signal), allowing isolation of the recruitment process from movement execution.

## Key findings relevant to ARC-033

The conjunction of contrasts (primary task vs both controls) revealed significant activation in ipsilateral cerebellum and contralateral plus supplementary motor areas. The ipsilateral cerebellum is notable because cerebellar internal models for the ipsilateral hand would normally be expected to be contralateral; the ipsilateral activation may reflect the recruitment of a recently learned, not yet fully lateralised model. The result establishes that the brain maintains distinct internal models for different objects and selectively loads the appropriate model in preparation for action.

This is part of a broader research programme (Wolpert, Kawato, Flanagan) showing that the brain operates a modular mosaic of internal models -- each a forward model mapping action to predicted sensory consequence for a specific context or domain. The modular architecture allows different forward models to make predictions simultaneously during action preparation, with the most activated one selected for execution.

## Translation to ARC-033

ARC-033 proposes that SD-003 counterfactual attribution requires E2_harm_s: a dedicated forward model operating on the harm stream z_harm_s, predicting how harm proximity changes as a function of action. This is architecturally separate from E2.world_forward (which predicts z_world). The biological evidence here provides existence proof that the brain maintains multiple concurrent domain-specific forward models and selectively recruits them. If this modular organisation applies to harm prediction -- and there is good reason to think the brain maintains dedicated threat-anticipation models given the evolutionary importance of harm avoidance -- then E2_harm_s is architecturally well-motivated.

The forward model framework is also relevant to the counterfactual operation. ARC-033's counterfactual attribution computes E2_harm_s(z_harm_s, a_cf) -- the predicted harm under counterfactual action. This is exactly the kind of prospective model-based reasoning that Kawato's programme describes: using an internal model to simulate future states under hypothetical actions without executing them. The preparation-period fMRI activation in this experiment (model loading before movement) is the biological correlate of exactly this anticipatory forward modelling.

## Limitations and caveats

The domain transfer is the primary caveat. Kawato's internal models are sensorimotor dynamics models for limb and tool manipulation. A harm proximity forward model is conceptually similar (action -> predicted sensory consequence) but operates in a very different feature space. There is no direct evidence that the brain maintains a dedicated harm proximity forward model of the kind E2_harm_s implements. The modular architecture is well-supported biologically; whether harm proximity specifically is handled by its own forward model is inferred rather than demonstrated.

Additionally, EXQ-095b found persistent failure (R2=0) for the harm forward model in V3 due to signal sparsity in harm_obs_s. This suggests the biological forward model analogy, while structurally valid, does not guarantee easy learnability in the REE training regime.

## Confidence reasoning

High-quality source from a prominent lab, published in Current Biology. The modular forward model architecture is well-established in biological motor control. The transfer to a harm-specific forward model is the main inferential leap, which is plausible but not established. Overall confidence 0.65.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1016/j.cub.2006.10.051
