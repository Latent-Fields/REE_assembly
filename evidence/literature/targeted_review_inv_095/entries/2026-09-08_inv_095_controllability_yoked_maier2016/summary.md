# Maier & Seligman (2016) -- the yoked control, and what a distribution-matched contrast can show

## What the paper did

This is the fiftieth-anniversary reassessment of learned helplessness by the two people who defined
the paradigm. The original 1967 account held that animals exposed to inescapable shock *learn* that
outcomes are independent of their responses, and that this learned expectation produces later
passivity. The 2016 paper reports that the neuroscience inverted this. Passivity is "the default,
unlearned response to prolonged aversive events," mediated by serotonergic activity in the dorsal
raphe nucleus. What is actually learned is the opposite: animals "overcome this passivity by
learning control, with the activity of the medial prefrontal cortex." The mPFC detects
controllability and inhibits the default dorsal raphe response.

The methodological backbone throughout is the yoked design. One animal can terminate the shock by
its own action; a second receives physically identical shock -- same intensity, same duration, same
timing -- delivered independently of anything it does. The aversive input distribution is matched by
construction. Only the informational relationship differs.

## Key findings relevant to the claim

INV-095's falsifier asks what happens when REE's harm/residue signal is replaced by
distribution-matched random noise. The yoked control is the biological precedent for that
experimental move, and the reason to have confidence that it is the discriminating manipulation
rather than a merely convenient one. Fifty years of this literature rests on the observation that
matching the distribution of aversive input and varying only its informativeness produces large,
persistent, circuit-level behavioural divergence.

For REE the lesson is directly about experimental design. It would be much easier to ablate the harm
signal -- zero it, or remove the pathway -- and observe degradation. But such a result is weak,
because it cannot distinguish a signal that is load-bearing from a signal whose mere presence
happens to be load-bearing (an input scaling issue, a normalisation artefact, a distributional shift
that any zeroed channel would produce). The distribution-matched substitute controls for all of
that. It is the difference between showing that the channel matters and showing that what the
channel *says* matters, which is the distinction the axiom's own language turns on: information
versus noise.

## How this translates to REE

Concretely: the successor to V3-EXQ-533 should replace `z_harm_a`/`z_harm_s`/`ResidueField` output
with a substitute matched on the empirical distribution of the intact signal -- same marginal
statistics, same scale, same sparsity -- and decorrelated from actual hazard. If E3 hazard-avoidance
trajectory selection and RBF-driven repair/avoidance pull degrade under that substitution relative
to intact, the axiom's named architectural consequence is confirmed on the substrate. If they do
not, the signal is decorative in the sense the claim's falsifying observation specifies.

The yoked literature also warns about what the comparison group must be. A distribution-matched
noise arm and an intact arm are not sufficient on their own; the informative comparison in the
rodent work is always three-way, including the no-stress control, because that is what reveals
whether the effect is impairment under noise or enhancement under signal.

## Limitations and confidence reasoning

The mapping boundary is real and the 2016 reframing widens it. The variable manipulated in yoked
designs is action-outcome contingency: the shock a yoked animal receives is uncontrollable, but it
still veridically signals tissue threat. A REE noise substitute would be uninformative about the
threat *itself*. These are corruptions of different relations -- the signal's relation to action
versus its relation to the world. And because the paper relocates the behavioural difference into a
control-detection circuit (mPFC) rather than into aversive-signal processing, the gap is wider than
it looks: the yoked effect may be telling us about control detection specifically, not about harm
signals being informative in general.

That is worth carrying into the REE experiment as a live confound. A noise-substitution result could
in principle be driven by the agent losing a learnable control relation rather than by the harm
signal ceasing to be about hazard, and the design should separate them -- for instance by including
an arm where the harm signal is intact but decorrelated from the agent's own action while remaining
correlated with world hazard.

Two smaller caveats. Yoked designs equate distributions but cannot fully equate perceived
predictability, a long-standing criticism. And rodent shock-escape is a narrow readout relative to
REE's "commitment-relevant behaviour," which spans trajectory selection and repair/avoidance pull.

Confidence 0.73. Source quality 0.88 -- Psychological Review, fifty years of converging behavioural
and circuit evidence, authored by the paradigm's originators and notable for reporting a result that
overturns their own earlier theory, which is a mark in its favour. Mapping fidelity 0.70 is the
limiting term, for the contingency-versus-integrity reason above. The entry's main value is
methodological rather than evidential: it is the existence proof that a distribution-matched control
is constructible and discriminating.
