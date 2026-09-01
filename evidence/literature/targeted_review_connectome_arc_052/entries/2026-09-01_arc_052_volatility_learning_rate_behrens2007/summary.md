# Learning the value of information in an uncertain world (Behrens et al., 2007)

## What the paper did

Behrens and colleagues gave healthy adults a probabilistic two-armed bandit in which the reward
contingencies were stable in one block and volatile in another, and asked a deceptively simple
question: how much should any one past outcome influence the next decision? They fitted a Bayesian
learner that infers not only the current reward probability but also the *volatility* of that
probability, and showed that human behaviour tracks the optimal learner -- subjects raised their
effective learning rate in the volatile block and lowered it in the stable block. The neural half of
the result is that anterior cingulate cortex activity at outcome time scaled with how informative
that outcome was for future prediction, and between-subject variation in that ACC signal predicted
between-subject variation in learning rate.

## Why it bears on ARC-052

ARC-052's second clause says that z_harm_a precision rises with accumulation stability -- that when
the threat state is changing rapidly, the accumulated affective estimate deserves less influence over
E3. This paper is the canonical demonstration that brains actually do this arithmetic, and that they
do it by explicitly representing volatility as a quantity in its own right rather than by any
heuristic proxy. The mapping is a dual rather than an identity: Behrens et al. express the adjustment
as a *learning rate* (how much the new observation moves the estimate), where ARC-052 expresses it as
a *precision* (how much a downstream consumer trusts the estimate). Under a Kalman-style reading
these are two faces of the same relative-precision ratio, so the finding transfers, but the transfer
is an inference and should be labelled as one.

What is genuinely useful here beyond confirmation is the ACC localisation. If ARC-052 is later wired
to a neuromodulatory or hub-level control signal (MECH-220's harm hub is the obvious candidate), this
paper says the volatility estimator is a real, separable computation with its own substrate, not
something that falls out of the encoder for free. That argues for computing the volatility term
explicitly in the substrate rather than hoping a precision head learns it implicitly from an NLL
objective.

## Limitations and what it does not license

The domain is appetitive. Nothing in this paper establishes that the same volatility-to-precision
relation holds for an aversive accumulator, and there are reasons to expect asymmetry -- Browning et
al. (2015), the companion entry in this directory, took exactly that question to an aversive task and
found the effect present but moderated by trait anxiety. The volatility manipulated here is of an
outcome probability; ARC-052's z_harm_a is an accumulated homeostatic deviation (SD-011), whose
"stability" is a different statistic and may need a different estimator. And the value being tracked
is a scalar, which sidesteps the question ARC-052 will have to answer in implementation: whether a
single precision scalar suffices for a multi-dimensional latent, or whether the precision head must
be per-dimension.

## Confidence

0.70, direction supports. The evidence is strong and the source is about as good as this literature
gets; the discount is entirely on mapping. I would not cite this paper as evidence that a precision
*head* is the right architecture -- only that the quantity such a head would carry is one the brain
demonstrably computes and uses.
