# Hobson & Friston 2012 -- Waking and Dreaming Consciousness: Free Energy and REM

**Claim tested: MECH-123**
**Evidence direction: supports**

## What the paper claims

Combining Hobson's protoconsciousness/activation-synthesis framework with Friston's free energy principle, the paper argues that REM sleep is when the brain takes its generative model offline for optimisation. Key claims:
- The brain's generative model (virtual reality generator) is the same architecture as Helmholtz's inference machine / Friston's predictive coding hierarchy
- During REM, aminergic suppression (noradrenaline and serotonin withdrawal) reduces the precision of sensory prediction errors -- effectively turning off bottom-up evidence
- With sensory evidence precision set to zero, the model runs as an unconstrained internal simulation
- This offline state allows the model to be optimised: pruning redundancy, reducing complexity, refining prior expectations (free energy minimisation)
- PGO waves provide stochastic perturbations that probe the model's internal structure, equivalent to random restarts in optimisation

## Mapping to MECH-123

MECH-123 claims REM resets precision priors (commitment_threshold, precision_ema_alpha) after content consolidation, and must be last because recalibrating before replay corrupts evidence weighting. The Hobson-Friston framework provides the most direct theoretical grounding for this claim.

The mapping is nearly one-to-one:
- 'Aminergic suppression reduces precision of sensory prediction errors' = REM reduces the precision weight on incoming evidence, freeing the model to revise its priors
- 'Offline optimisation prunes redundancy and reduces complexity' = hyperparameter updating: commitment_threshold and precision_ema_alpha are hyperparameters of the predictive coding hierarchy that are revised during this offline pass
- 'Generative model runs unconstrained' = the model tests its prior structure without evidence anchoring it -- equivalent to simulated annealing of prior parameters

The ordering constraint emerges from this framework: the generative model being optimised during REM is the post-NREM consolidated model (MECH-121 has loaded new schema content). If REM ran first (before NREM consolidation), the model being optimised would be the pre-consolidation model -- the precision recalibration would be applied to a model that has not yet integrated the new episodic content, corrupting evidence weighting.

## The precision mechanism

Aminergic suppression during REM is a precision-reduction operation:
- Noradrenaline modulates precision weights on sensory channels (high NA = high sensory precision = anchored to evidence)
- During REM, NA withdrawal = sensory precision set low = model is freed from evidence constraints
- This is exactly what MECH-123 requires: a state where precision parameters can be revised without being constrained by current sensory evidence

The free energy framing makes explicit what Walker-van der Helm's SFSR leaves implicit: the precision recalibration is not just about emotional affect -- it is a general Bayesian hyperparameter update that happens to have a particularly strong effect on affectively weighted memories because those carried the highest precision weights during waking.

## What the paper does not say

The paper is primarily theoretical. Empirical evidence for free-energy-minimisation as an explicit REM mechanism is limited. The paper does not name commitment_threshold or precision_ema_alpha (these are REE constructs). The specific parameters being updated are characterised at the level of 'model complexity' and 'prior expectations' without specifying the architectural instantiation.

## Evidence quality note

High-quality theoretical paper (Progress in Neurobiology, Hobson + Friston collaboration). This is the canonical statement of the free energy / predictive coding account of REM sleep. The mapping to MECH-123 is high-fidelity because REE is built on the same predictive coding / precision framework. The theoretical nature limits empirical confidence, but as the framework paper it provides the strongest mechanistic grounding for MECH-123's precision recalibration claim.
