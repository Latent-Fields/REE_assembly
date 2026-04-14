# Neural correlates of object identity and reward outcome in the sensory cortical-hippocampal hierarchy
**Fiorilli, Marchesi, Ruikes et al. (2024) | Cerebral Cortex | doi:10.1093/cercor/bhae002**

## What the paper did

Fiorilli and colleagues implanted rats with multi-electrode arrays targeting four regions simultaneously -- primary somatosensory barrel cortex (S1BF), secondary visual cortex (V2L), perirhinal cortex (PER), and dorsal hippocampus (CA1/CA3/DG) -- and trained them on a multisensory two-alternative forced-choice object discrimination task. Animals learned to associate two 3D LEGO objects with left/right reward ports, with trials presenting visual, tactile, or combined sensory information. This design allowed the authors to ask which region in the hierarchy encodes object identity, and which encodes other task-relevant signals such as outcome and goal location.

## Key findings relevant to SD-015

The main finding is a striking dissociation: object identity was decoded significantly above chance only from secondary visual cortex (V2L, 9.2% of recorded cells) and not from perirhinal cortex or hippocampus during the object-sampling phase. Perirhinal cortex instead encoded goal-location approach -- PER cells anticipated arrivals at reward ports and signalled unexpected trial outcomes (reward omission). Hippocampus showed amodal object representations, but only after reward delivery, not during the initial sampling phase.

The message for SD-015 is straightforward: the object identity signal lives early in the processing chain, at the sensory cortex level. By the time information reaches perirhinal cortex -- which is often assumed to be the key object-recognition structure -- it has already been transformed into motivational and outcome-expectation content. The hippocampus integrates object information only after reward feedback, forming an amodal, post-hoc representation rather than a proactive identity signal that could drive approach.

This supports the architectural choice in SD-015 to implement z_resource as a dedicated ResourceEncoder operating on raw sensory observations (world_obs[250] -> Linear(250,64) -> z_resource[32]) rather than attempting to extract object type from a downstream integrated representation like z_world. By the time information is fused into z_world, it carries spatial context, temporal history, and motivational colouring -- the object-type signal is no longer cleanly accessible.

## The REE translation and what it tells us about architecture

One way to read this paper is as a constraint on where in the processing chain you can still recover clean object identity. You can do it at sensory cortex, roughly at the stage where world_obs is generated. You cannot reliably do it from perirhinal cortex (the "standard" view), and you cannot do it from hippocampus before reward. z_resource must therefore be extracted close to the sensory input, before spatial and motivational context collapses the representation. This is consistent with SD-015's proposal that ResourceEncoder operates on raw observation features.

The perirhinal finding also has an interesting implication for E3 in REE: PER's role in encoding goal-location approach and outcome expectation looks more like the motivational weighting in E3's evaluation stage than like an object-type encoder. This suggests the architecture may naturally separate into sensory object coding (z_resource) and motivational valuation (E3/PER) -- which is precisely what SD-015 proposes.

## Limitations and caveats

This study uses fixed object locations. The animals always approached the same objects at the same positions; object identity and spatial position are confounded across sessions even if the task involves discriminating identity locally. The critical question for SD-015 -- whether the early sensory-cortex representation of object type is spatially invariant when objects respawn at random locations -- is not directly tested. The paper shows where object identity is encoded in a fixed-position task; it does not show that this encoding survives positional variation. That question is more directly addressed by DiCarlo & Cox (2007) for IT cortex, already in this review.

The task also has only two object types, so the within-region discrimination analysis is coarse. Whether V2L and upstream areas maintain robust object identity coding across many object types and environmental positions remains an open question.

## Confidence reasoning

Source quality is high: simultaneous four-region recording, large cell counts, rigorous decoding analyses, and the multisensory design provides good cross-validation. Mapping fidelity is moderate: the dissociation it reveals is directionally useful (object identity lives early, not in PER), but the fixed-position design limits inference about the spatial invariance that is central to SD-015's motivation. Confidence is 0.72 -- the paper provides useful negative evidence (PER is not where you find object identity) and constrains the architecture, but its positive claim (sensory cortex is sufficient) needs the DiCarlo/IT cortex literature to establish spatial invariance. Together these entries make a stronger combined case than either alone.
