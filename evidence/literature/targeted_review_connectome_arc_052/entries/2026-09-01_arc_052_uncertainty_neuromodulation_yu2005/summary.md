# Uncertainty, neuromodulation, and attention (Yu & Dayan, 2005)

## What the paper did

Yu and Dayan asked what a Bayesian observer needs in order to behave sensibly when both its
observations and its context are unreliable, and answered that it needs at least two distinct
uncertainty quantities. *Expected* uncertainty is the known unreliability of a predictive cue within
a stable context -- you have learned that this signal is only 70% trustworthy. *Unexpected*
uncertainty is the possibility that the context itself has changed, so that everything you have
learned may no longer apply. They proposed that acetylcholine carries the first and norepinephrine
the second, and showed the assignment is consistent with a large body of physiological,
pharmacological and behavioural data, working the argument through a class of attentional cueing
tasks in which the two modulators are predicted to interact in a "part-antagonistic,
part-synergistic" way.

## Why it bears on ARC-052

ARC-052's final sentence -- that neuromodulatory inputs modulate the precision gains -- is doing more
architectural work than its brevity suggests, and this paper is where the justification for it lives.
The claim is not merely that precision exists but that its *gain* is set from outside the encoder.
Yu and Dayan give the computational reason that factorisation is right rather than arbitrary: the
uncertainty that matters is a property of the context, shared across streams, and a single stream
cannot recover it from its own statistics. An encoder that estimates only its own output variance is
blind to the question "has the world just changed underneath all of my estimates?".

The more useful contribution, though, is one ARC-052 has not yet taken up. ARC-052 states two
precision clauses that it treats as a matched pair: z_harm_s precision rises with forward-model
accuracy, z_harm_a precision rises with accumulation stability. Read through this framework those are
not the same kind of quantity. Forward-model accuracy is expected uncertainty -- a learned,
within-context reliability. Accumulation volatility is much closer to unexpected uncertainty -- an
inference that the threat regime has shifted. If that reading is right, routing both through one
shared precision-gain pathway would collapse two quantities the neuromodulatory literature says are
separately represented, and would be a design error visible only in exactly the regime ARC-052 cares
about most: a rapidly changing threat environment.

## Limitations, stated plainly

This is a theory paper. It synthesises other people's measurements into an assignment; it does not
test that assignment. Twenty years on, the ACh/NE story has been productively complicated rather than
overturned, but a REE claim leaning on it is leaning on a framework, not a result. More pointedly for
ARC-052: the modulators here are acetylcholine and norepinephrine, whereas ARC-052 names serotonin
and norepinephrine. Only the NE half is shared. I searched for a comparable formalisation assigning
serotonin a precision-gain role and did not find one that would survive this directory's standards,
so the serotonergic half of ARC-052's neuromodulatory clause should be recorded as currently
ungrounded rather than quietly carried along by this citation. That is worth stating explicitly
because REE already has a SerotoninModule, and the presence of an implementation is not evidence for
the claim it was built to serve.

## Confidence

0.65, direction supports. Strong for the architectural point (gains are external to the encoder),
weak for the specific modulator assignment ARC-052 makes.
