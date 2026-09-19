# A computational and neural model of momentary subjective well-being

Rutledge, Skandali, Dayan & Dolan (2014), *PNAS* 111(33):12252-12257.
DOI [10.1073/pnas.1407535111](https://doi.org/10.1073/pnas.1407535111) - PMID 25092308 - PMC4143018.
Retrieved via PubMed.

## What the paper does

Twenty-six people played a probabilistic gambling task in an MRI scanner and were repeatedly asked
how happy they were right now. The headline result is negative and clarifying: momentary happiness
is *not* explained by current or cumulative task earnings. It is explained by a model in which
happiness is a weighted sum of recent certain rewards, the expected values of chosen gambles, and
the reward prediction errors arising from those expectations -- each weighted by an exponentially
decaying forgetting factor. The account survived a large-scale smartphone replication with 18,420
participants, and the same model terms that predicted the subjective reports also accounted for
task-dependent striatal BOLD.

So: mood is a leaky exponential integral over the prediction-error stream.

## How it bears on MECH-055 -- both ways

This is the entry that cuts hardest in both directions, and the reason it is worth the pull.

**Supporting.** MECH-055 asks whether REE's axis 1 (hedonic-stability, the mu/kappa overlays)
stays distinct from axis 3 (signed precision-weighted prediction error). Rutledge et al. establish
that the biological version of the slow channel really is a state variable in its own right, with
its own timescale and its own functional form, and that it is *not* the instantaneous outcome
signal -- current earnings do not explain it. Different variance signature, different timing
signature. That is close to a restatement of what MECH-055's CONFIRMING clause asks a distinctness
test to demonstrate.

**Weakening.** In the fitted model, happiness has no driver whatsoever beyond expectation and
prediction-error history. It is a deterministic linear filter of the signed PE stream. Perturb the
PE stream and mood moves in a fixed, predictable way -- which is structurally MECH-055's own
FALSIFIER (i). The best-supported account of hedonic tone in the human literature makes it
*derivative of* signed PE, not independent of it. If REE's mu/kappa turns out to be reconstructable
from its PE history, REE would be biologically orthodox and would still fail MECH-055 as worded.

## The part that should change the test design

The two readings above are not actually in tension; they are the same fact seen through two
different statistics, and that is the practically useful finding here.

Under a leaky-integrator relationship, the *instantaneous correlation* between the slow channel and
the fast channel is low -- which reads as distinctness -- while the slow channel is nonetheless
fully determined by the fast one, which is collapse with a lag. MECH-055's FALSIFIER (ii) is
written as "numerically redundant (correlation ~1)". That test would pass an architecture that is
completely collapsed, simply because the collapse is filtered. The right test is not correlation
against raw PE but residual variance against a *best-fitting leaky filter* of PE: fit the
Rutledge-form exponential-decay filter from REE's PE channel onto the mu/kappa trajectory, and ask
what survives. Anything that does not survive is not an independent channel, whatever its
instantaneous correlation says.

One further caution against over-reading the weakening direction: the paper shows a leaky-PE-integral
model *suffices*, not that no independent mood driver exists. Absence of an extra term in a fitted
model is weak evidence against separability. And the fact that the same quantities explain striatal
BOLD means shared neural substrate between a hedonic-tone channel and a PE channel is the biological
expectation here -- so a REE finding that mu/kappa and the PE channel share upstream state is not by
itself the collapse MECH-055 is hunting.

## Where the mapping strains

The dependent variable is a reported subjective feeling. REE's axis 1 is a softmax-temperature and
commitment-threshold regulator with no reportable content, and MECH-055's own NAMING NOTE concedes
the two constructs are not the same. What justifies the transfer is the shared formal role -- a
slowly-integrating scalar that biases action selection -- and nothing more. The exponential
forgetting constant, fitted to sub-minute sampling in a human monetary task, does not transfer to
mu/kappa moving on episode and curriculum timescales in a grid-world. Only the functional form does.

## Confidence

0.80. Source quality 0.92: primary modelling with a neural convergence test and an unusually large
independent replication, in a top venue, since treated as a standard account of momentary mood.
Mapping fidelity 0.66 for the construct mismatch. Transfer risk 0.35 -- lower than it might be
because what transfers is a functional form rather than an anatomical or pharmacological fact.
Recorded as `mixed` rather than forced into one direction, because forcing it would lose precisely
the part worth keeping.
