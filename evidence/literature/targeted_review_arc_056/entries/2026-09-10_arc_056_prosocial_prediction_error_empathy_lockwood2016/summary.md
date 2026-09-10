# A dedicated channel for learning on another's behalf (Lockwood et al., 2016)

**Claim tested:** ARC-056 -- ethics-as-coherence: ethical trajectory selection as optimisation of shared temporal-depth coherence across self and represented others.
**Direction:** mixed | **Confidence:** 0.58

## What the paper did

Participants in an fMRI scanner performed a probabilistic reinforcement-learning task in which the stimuli they chose between led to rewards for themselves, for another person, or for no one. The no-one condition is the important piece of design: it isolates the other-directed component from the mere act of learning a contingency. Trial-wise computational modelling recovered separate learning parameters per condition, and trait empathy was measured independently and used as a predictor.

Three results. People did learn to obtain rewards for others, but more slowly than for themselves. A posterior portion of subgenual anterior cingulate cortex / basal forebrain signalled a prosocial prediction error conforming to classical reinforcement-learning principles, and drove learning *only* in the prosocial context. And there was substantial variability in how efficiently people learned prosocially, both behaviourally and in the selectivity of the sgACC response, which trait empathy predicted.

## Why this is filed as mixed

It supports one of ARC-056's commitments and pulls against another, and I would rather governance saw both than a net-of-signs number.

**The support.** ARC-056's LEG 2 confirming criterion is explicit that any other-regarding effect should *scale* with `beta_j` rather than being all-or-nothing -- a formula that switches on and off is a decorative formula. Here the effect is continuously graded: how well a person learns on another's behalf varies with empathy along a dimension rather than sorting people into prosocial and non-prosocial types. Against a categorical moral-circle architecture, in which others are either inside the circle or outside it, this is real evidence for the weighted-coefficient picture the claim assumes.

**The tension.** ARC-056 posits one objective in which self and other terms are summed with different weights. If the other's term were simply the self term at lower gain, one would expect the same machinery running quieter. What is found instead is a substrate that carries a prediction error largely specific to the prosocial context, plus a different learning *rate* rather than only a different final weight. A rate difference is not what a coefficient on a shared objective produces; it is what separately parameterised streams produce. That is the signature of a dedicated channel, not a common currency.

## How much this actually settles

Less than it first appears, in both directions, and the symmetry is worth stating.

The support half is on the wrong axis. Trait empathy varies across *participants* for a fixed target. ARC-056's `beta_j` must vary across *targets j* for a fixed agent -- that is what "depends on inferred similarity, relational commitment and responsibility structure" means. Gradedness between people is suggestive by analogy for gradedness between targets, but it is not the same measurement, and the claim's own criterion asks for the latter.

The tension half is also not decisive. A dedicated substrate for *computing* an other-directed term is entirely compatible with those terms being summed into one objective further downstream. Nothing in this design distinguishes "separate objectives" from "separate computation feeding one objective", and ARC-056 only commits to the latter. So this marks a live architectural question rather than closing it.

And the standing limitation across this whole directory applies again: the currency is reward, not `D_V`. ARC-056's distinctive content -- that what is optimised across self and others is shared temporal-depth coherence -- remains untested by anything available. Only the form of the objective is at issue in this entry.

## Confidence reasoning

Source quality is 0.85: PNAS, trial-wise model fitting rather than condition contrasts, a control condition that genuinely isolates the other-directed component, and an independent trait measure used as a predictor rather than a post-hoc median split. Mapping fidelity is 0.60 -- both directions of bearing land on real ARC-056 commitments, but the supporting evidence sits on the between-subject axis rather than the between-target one the claim needs. Transfer risk is 0.40 for laboratory monetary prosocial learning read as a general ethical objective. The aggregate 0.58 reflects a solid study whose two directions partly offset.
