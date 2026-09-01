# Anxious individuals have difficulty learning the causal statistics of aversive environments (Browning et al., 2015)

## What the paper did

Thirty-one healthy adults, deliberately recruited to span the trait-anxiety range, played a two-armed
bandit in which each choice could deliver an electric shock of trial-varying magnitude. One 90-trial
block was stable (one shape predicted shock 75% of the time), the other volatile (the predictive
shape reversed every twenty trials, at 80/20). Pupil diameter was recorded throughout. The design is
the aversive twin of Behrens et al. (2007), and it asks the question that paper left open: does the
volatility-to-learning-rate machinery operate on threat as it does on reward, and if so, in everyone?

The answer is a qualified yes. At the group level, participants raised their learning rate in the
volatile block, and pupil dilation tracked volatility (F(1,26)=9.8, p=0.004). But the adjustment was
strongly moderated by trait anxiety: elevated anxiety predicted a *reduced* change in learning rate
between blocks (r(28)=-0.42, p=0.02), with no relationship to the mean learning rate across blocks
(r(28)=0.1, p=0.6). The effect is specifically about adapting the weighting, not about learning
speed. And the pupillary response to volatility showed the same moderation (r(26)=-0.51, p=0.005),
which the authors read as possible evidence of altered noradrenergic responsivity, since pupil
diameter is argued to index locus coeruleus activity.

## Why it bears on ARC-052

This is the most direct empirical support in the pull for ARC-052's second clause, and it is direct
in the way that matters -- the domain is harm, not reward. The finding that an accumulated aversive
estimate is down-weighted when the threat environment becomes volatile is precisely what a precision
term on z_harm_a would implement.

The pupillometry does something ARC-052 needs and Behrens et al. cannot supply: it makes the
neuromodulatory clause empirical rather than decorative. ARC-052 says serotonin and norepinephrine
*modulate the precision gains*. Browning et al. put a measurable ascending-arousal signal in the loop
and show it carries the volatility term. That is a claim about where the gain lives -- outside the
encoder, in a modulatory channel -- and it is the architectural commitment that distinguishes ARC-052
from "the harm encoder learns to be uncertain when things are unstable".

## What it also warns about, and this is the more interesting half

The individual-difference result is not a nuisance finding to be noted and dropped; it is a failure
signature for the architecture. A system can possess volatility-sensitive precision machinery and
still fail to deploy it, and in the clinical population where that failure is most visible the
neuromodulatory index is blunted alongside it. If REE wires 5-HT/NE gains onto harm precision, it
inherits a specific pathology as a reachable state: a gain channel that stops tracking volatility
produces an agent whose accumulated threat estimate stays maximally trusted in an environment that no
longer supports it. Clinically that reads as anxious rigidity, and if it appears in the substrate it
should be recognised as this rather than treated as a bug in the precision head.

## Limitations

Thirty-one participants, with the key correlations in the r=0.4-0.5 band; this is the effect-size
range where independent replication is not a formality. The noradrenergic interpretation is a proxy
inference the authors are careful to hedge -- they say outright that they cannot determine whether
the deficit reflects anxiety-related noradrenergic control without pharmacological manipulation. The
aversive-specificity claim is weaker than it first reads: a reward version showed no anxiety effect,
but the difference between tasks was not itself significant. And the volatility manipulated is of a
cue-outcome probability rather than of an accumulated homeostatic state, which is the object SD-011
actually defines z_harm_a to be.

## Confidence

0.72, direction supports. Highest mapping fidelity in this pull, discounted for sample size and for
the proxy status of pupillometry.
