# Ernst & Banks 2002 -- Humans integrate visual and haptic information in a statistically optimal fashion

## What the paper did

Ernst & Banks ran a foundational psychophysics experiment on multimodal cue integration. They asked observers to estimate the height of an object when both visual and haptic information were available, manipulating the variance (noise) in each modality independently. They demonstrated that the integrated percept is well-described by maximum-likelihood integration: each modality contribution to the integrated estimate is weighted by its inverse variance, and the resulting estimate has lower variance than either modality alone. Visual dominance in many earlier studies turned out to reflect lower visual variance, not a fixed perceptual bias -- when haptic variance was reduced and visual variance increased, haptic information dominated.

## Key findings relevant to MECH-269b

This is the canonical empirical demonstration that the human nervous system performs reliability-weighted (precision-weighted) multimodal integration. The brain demonstrably computes per-stream reliability and uses it to weight stream contributions. MECH-269b V_s formalises and extends this: the per-stream precision parameter is psychophysically demonstrable in humans for at least the sensory-modality case, and MECH-269b proposes it generalises to all the latent streams in the planning loop.

This is tag (c) strong inferential support: the per-stream precision parameter that MECH-269b proposes is empirically grounded for cue integration, and the mathematical primitive (per-stream inverse-variance weighting) is the same primitive MECH-269b applies to forward-prediction-error gating.

## How the findings translate to REE

Ernst & Banks supply the empirical foundation that MECH-269b per-stream V_s formalises. The brain demonstrably has the computational machinery to (a) estimate the variance of each modality contribution, (b) weight contributions inversely with variance, and (c) integrate the result into a single percept. MECH-269b extends this from current-sensory-estimate combination to forward-prediction-error gating -- the same mathematical primitive applied at the level of model-generated predictions weighted by per-stream reliability rather than at the level of current sensory estimates. This is a forward extrapolation but a natural one mathematically.

## Limitations and caveats

Three caveats. First, cue integration is per-modality at the perceptual level. Extending this to per-stream gating of forward-prediction errors (E1 / E2 rollouts) is a generalisation MECH-269b makes but Ernst & Banks do not directly test. The principle transfers but the setting differs. Second, the paradigm is purely cortical-perceptual and silent on hippocampal proposer dynamics. The symmetric-application claim cannot be addressed from this evidence -- tag (d) measurement gap. Third, two modalities only. The generalisation to many simultaneous streams (z_world, z_self, z_harm_s, z_harm_a, z_goal in REE) is a mathematical extension that the paper supports in principle but does not directly demonstrate.

## Confidence reasoning

Confidence 0.74 -- supports MECH-269b at the empirical-primitive level. Source quality very high (Nature, behaviourally rigorous, replicated extensively in subsequent work). Mapping fidelity moderate because the cue-integration setting is one step removed from forward-prediction gating; the principle transfers cleanly, but it is not directly tested in MECH-269b setting. Transfer risk modest because the reliability-weighting principle is broadly applicable across sensory and motor systems -- it is the strongest empirical foundation in the anchor list, but it is one mathematical step away from what MECH-269b actually claims.
