# Neural computations underlying arbitration between model-based and model-free learning (Lee et al., 2014)

## What the paper did

By 2014 it was well established that humans have both a deliberative model-based and a reflexive
model-free system for choosing actions. Lee, Shimojo and O'Doherty asked the question that had gone
unanswered: what decides which one is driving at any given moment? Their answer is an *arbitrator*
that allocates control in proportion to the estimated reliability of each system's predictions.
Reliability is not stipulated -- it is estimated online from the distribution of each system's
prediction errors, using a Bayesian estimate of the PE distribution summarised by an inverse
index of dispersion, with state prediction error standing in for the model-based system's competence
and reward prediction error for the model-free system's. In the fMRI data, inferior lateral
prefrontal and frontopolar cortex encoded both the reliability signals and the output of the
comparison between them, and connectivity between those regions and model-free valuation areas was
negatively modulated by the degree of model-based control -- i.e. the arbitrator appears to act by
turning the model-free pathway down rather than by turning a knob at a summing junction.

## Why it bears on ARC-052

Of the five entries in this pull, this is the one whose *architecture* most nearly matches what
ARC-052 proposes. Two parallel streams; each emits, alongside its content, an online estimate of how
much it should be trusted; the estimates are compared; downstream influence follows the comparison.
That is ARC-052's structure, in a different domain, working, with a neural correlate.

It is also the only entry that answers ARC-052's first clause in operational detail. ARC-052 asserts
that z_harm_s precision should increase with forward model accuracy -- when E2_harm_s predictions are
good, the prediction error is more informative -- but does not say how the substrate would know that.
Lee et al. give a recipe: track the dispersion of the forward model's own state prediction error and
invert it. REE already computes E2_harm_s PEs; the quantity is sitting there. That makes clause (1)
implementable without a new learned head at all, which is worth weighing against the notes' current
proposal to learn log_sigma from an NLL objective -- see the Kendall & Gal entry in this directory
for why the learned route is less innocent than it looks.

## Where the mapping strains, and what that costs

The two things being arbitrated here are two whole control systems computing the *same* quantity
(action value) by different routes. ARC-052's two streams compute *different* things --
sensory-discriminative proximity/intensity and affective-motivational accumulated deviation (SD-011)
-- and both feed one controller. "Relative reliability" is a cleaner concept when the alternatives
are redundant estimators of one quantity than when they are complementary contributors to a decision,
and ARC-052 should not assume the softmax-over-reliabilities form transfers unexamined. Relatedly,
the arbitration Lee et al. found was asymmetric and implemented as connectivity gating; ARC-052
currently assumes symmetric weighting at the point of combination. Both are defensible designs, but
this paper supports the first more than the second.

The subtler warning is in how reliability is defined. Inverse dispersion of prediction error rewards
*consistency*, not *accuracy*. A forward model that is systematically wrong in a stable way looks
maximally reliable by this measure. In a reward task that error is self-correcting; in a harm stream
it is not obviously so, and an agent that grants high influence to a confidently-wrong threat
predictor is describing a recognisable clinical picture rather than a rare edge case. If clause (1)
is implemented this way, that failure mode should be instrumented from the start.

## Confidence

0.75, direction supports. The architectural correspondence is the strongest evidence ARC-052 has;
the discount is domain transfer, not method.
