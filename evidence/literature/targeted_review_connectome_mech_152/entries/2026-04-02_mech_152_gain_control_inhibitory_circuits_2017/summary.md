# Kanashiro et al. (2017) — Attentional Modulation of Neuronal Variability in Circuit Models of Cortex

## What the paper does

Kanashiro and colleagues model how top-down attention modulates cortical processing through inhibitory circuits. They show that a single biophysical mechanism — top-down signals primarily affecting inhibitory neurons — can explain multiple correlates of attention: increased response gain, decreased noise correlations, and enhanced stimulus sensitivity. The model is validated against V4 electrophysiology data showing attention effects on neural responses.

## Relevance to MECH-152

MECH-152 claims that cue-indexed context projects to a terrain_weight signal [w_harm, w_goal] that scales E3's harm and goal scoring multiplicatively. This is a form of gain control: the context determines how strongly each evaluation channel responds. Kanashiro et al. provide the computational neuroscience foundation for this operation — demonstrating that gain control is a fundamental operation in cortical circuits, implemented through top-down modulation of inhibitory networks.

The key insight: gain control doesn't just scale magnitude; it also controls signal-to-noise ratio. If terrain_weight operates analogously, then high w_harm in a hazard-gradient context wouldn't just amplify harm signals — it would make harm evaluation more precise (lower variability). This has implications for how MECH-152 composes with ARC-016's dynamic precision.

## Mapping caveats

The mapping is functional, not mechanistic. The paper models visual attention through SOM/PV inhibitory circuit dynamics; MECH-152 uses a trained linear projection from ContextMemory to [w_harm, w_goal]. There is no inhibitory circuit analogue in REE's current architecture. The gain control principle transfers, but the implementation is vastly simpler in REE.

## Confidence reasoning

Good computational paper in eLife. Supports the gain control principle underlying MECH-152. Confidence moderated by the domain distance (visual attention vs terrain evaluation) and mechanism gap (inhibitory circuits vs linear projection).
