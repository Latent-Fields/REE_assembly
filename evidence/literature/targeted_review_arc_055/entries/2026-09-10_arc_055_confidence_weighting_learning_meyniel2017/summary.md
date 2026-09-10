# Confidence weighting in probabilistic learning (Meyniel & Dehaene, 2017)

**Claim tested:** ARC-055 -- verisimilitude signal availability: V(t) and D_V must be explicitly available to E3 selection and influence E1/E2 learning updates.
**Direction:** supports (learning-update leg only) | **Confidence:** 0.72

## What the paper did

Human adults learned the transition probabilities underlying auditory or visual sequences while in an fMRI scanner. The sequences were non-stationary in a way the subjects knew about -- the transition probabilities could change at unsignalled moments -- which makes the learning problem inherently hierarchical: you must estimate both the current statistic and how much to trust it. Subjects reported their confidence trial by trial, and the whole dataset was analysed against an ideal-observer model that computes the Bayes-optimal answer to exactly that problem.

The design is worth dwelling on, because it is the reason this entry is admissible at all. A study that merely showed confidence correlating with something would be weak evidence for an architectural claim. This study instead asks whether the brain's learning rule *has the confidence-weighting form* -- whether the reliability estimate is doing computational work in setting how much a new observation revises the model.

## Key findings relevant to the claim

Three findings matter here. Subjective confidence reports tightly followed ideal-observer predictions, so the maintained reliability estimate is accurate rather than a post-hoc rationalisation. Subjects attached *distinct* confidence levels to each learned transition probability, which is what Bayes-optimal inference requires and what a single global arousal-like signal could not produce. And the likelihood of new observations and the confidence in current predictions were tracked in distinct brain areas and combined in the right inferior frontal gyrus in agreement with the confidence-weighting model, with additional signatures of a hierarchical process disentangling distinct sources of uncertainty.

## How this translates to REE

ARC-055's substantive assertion is not that verisimilitude exists but that it must be *explicit* -- an addressable signal rather than an emergent epiphenomenon -- because specific downstream consumers have to read it. This paper gives the general form of that requirement a fairly direct biological instantiation on one of the named consumers, learning update prioritisation. The reliability estimate is maintained, is separable enough to be independently reported and independently localised from the likelihood signal it is combined with, and demonstrably governs the size of the model revision. If reliability were epiphenomenal in the way ARC-055 argues it must not be, none of those three would hold.

The finding that confidence is attached per-statistic rather than as one scalar is also mildly informative about the claim's shape. ARC-055 treats V(t) and D_V as signals; the hierarchical result here is a hint that a single scalar may be under-specified for the job, which is a design question the claim's Stage 1 / Stage 2 / Stage 3 staging note already half-anticipates.

## Limitations and confidence reasoning

The honest boundary is that this paper is about a different quantity than V(t), and about only half of ARC-055's consumers. Confidence in a learned transition probability is per-estimate reliability inside a hierarchical estimation problem; V(t) is meant to be a global verisimilitude of the agent's world model and D_V a temporal-depth property of it. Those are cousins, not the same thing, and the paper contains nothing about temporal depth. More importantly, the claim's harder half -- that V and D_V are available to *E3 trajectory selection* -- is untouched. This entry should never be cited for that leg.

Source quality is high (0.88): PNAS, an ideal-observer benchmark rather than a descriptive contrast, cross-modal replication within subjects. Mapping fidelity is 0.72, reflecting a good match on the availability-and-use structure and a loose match on the identity of the quantity. Transfer risk is low (0.30) because the subjects are human and the computation is domain-general. The aggregate 0.72 is weighted toward mapping fidelity, since ARC-055 is an architectural commitment about what must be explicitly represented rather than an empirical claim about brains.
