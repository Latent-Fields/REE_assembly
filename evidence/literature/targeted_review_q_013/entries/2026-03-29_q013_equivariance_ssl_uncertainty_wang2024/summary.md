# Understanding the Role of Equivariance in Self-supervised Learning — Wang et al. (2024)

## Relevance to Q-013

Q-013 is about whether JEPA's deterministic representation can substitute for explicit stochastic uncertainty heads in REE's precision routing. To evaluate that, we need to know what information JEPA's invariances actually preserve versus discard -- and Wang et al.'s NeurIPS 2024 paper provides the most rigorous information-theoretic answer yet available.

## What the paper shows

The authors establish a theoretical framework showing that contrastive and invariant SSL methods (the JEPA family) systematically discard information associated with data augmentations. This discarding is the mechanism by which they achieve invariance -- and it is precisely the same mechanism by which they lose information useful for downstream tasks that require sensitivity to those transformations. Color for plant classification. Orientation for geometric reasoning. Event-type distinctions for precision routing.

The key theoretical contribution is the characterisation of an explaining-away effect in equivariant SSL: when a model must simultaneously predict an equivariant label and a classification label, the equivariant task forces the model to retain features that also help classification, creating a synergy. Invariant-only methods lack this synergy; they actively suppress the relevant features to achieve invariance.

The result is expressed information-theoretically: equivariant SSL methods retain strictly more downstream-relevant information than invariant-only methods, and the margin is not small -- it corresponds to a categorical difference in what the representation can support.

## The implication for JEPA-based precision routing

For REE, the question is whether JEPA's z variable -- the component that captures what the context cannot determine -- provides enough uncertainty signal for precision routing to work. Wang et al.'s framework suggests that if the relevant distinctions for routing decisions are ones that JEPA's invariances discard, then no amount of dispersion analysis on z will recover them, because the information was never encoded.

In a temporal world model, the analogous distinctions might be: two trajectories that look similar in JEPA's invariant space but have very different harm potential. If the invariance was trained on augmentations that collapse those trajectories, z captures their shared unpredictability but not their divergent risk profiles. Precision routing that relies on z alone would weight them identically.

This does not rule out the hybridize answer -- it specifies what hybrid means. A JEPA-based E1 could work as an E2 fast transition model if the equivariant channel from Wang et al.'s framework is preserved in the part of z that feeds E3's precision router. But a purely invariant JEPA head cannot substitute for an explicit uncertainty head without information loss that matters for routing.

## Calibration note

Confidence is 0.61 -- marked mixed because the paper cuts both ways. It diagnoses the problem (invariance discards information precision routing needs) but also points toward the solution (equivariant extensions can recover it). The mapping from image-domain SSL to temporal world-model dynamics requires care; the information types are different, and the argument, while plausible, has not been validated in the temporal sequential setting REE requires.
