# Nassar et al. 2012 -- what actually triggers a phasic burst

## What the paper did

Human participants made predictions about noisy streams punctuated by occasional change points,
while pupil diameter was recorded and behaviour was fitted with a normative model of belief
updating. Two pupillary quantities came apart. *Transient* pupil changes tracked detected
instabilities in the stream -- the model's assessment that something had shifted. *Sustained* pupil
size indexed confidence in recent observations, and captured individual differences in how stable
subjects expected the world to be. Both forecast how new information would shape subsequent
judgments. Then the authors did the thing that makes this paper load-bearing rather than merely
suggestive: they induced pupil changes independently of the task and of luminance, and this
systematically modified how much new data shifted existing beliefs.

## Why this is a trigger-side entry

Most of the SD-069 literature is about what a phasic burst *does*. This one is about what sets it
off, which is the part of SD-069 that was quietly rewritten on 2026-07-17 and deserves its own
grounding. The regulator fires when surprise exceeds `trigger_ratio x max(ema, floor)` -- a
*relative* predicate, comparing instantaneous surprise against its own running baseline rather than
against a fixed threshold. Nassar and colleagues show that this is the right shape: the phasic
arousal system's natural trigger is instability detected against an expectation, not error magnitude
in absolute terms.

It also independently vindicates the signal-source amendment. The claim's implementation note
records that the default smoothed `e3._running_variance` decays monotonically for an untrained
forward model and fired zero natural events even under environmental volatility, which is why
`phasic_burst_signal_source="instantaneous_pe"` had to be added. That amendment was made on
engineering grounds -- the lever had to fire without a synthetic poke. This paper says the same thing
from the biology: it is the *transient*, sharp component that carries event structure, while the
sustained component encodes something else entirely (confidence, expected uncertainty). Smoothing
the signal destroys precisely the quantity the phasic system reads.

## Where the mapping is approximate

The transient quantity here is change-point probability under a generative model -- a normative
Bayesian term. SD-069's predicate is a raw per-tick PE-MSE compared to its own EMA. These agree on
stationary-then-shifted streams and diverge on streams that are high-variance but stationary, where
the cheap approximation will fire and the normative quantity will not. That is a real
false-positive mode and it is worth knowing about before reading a burst rate as evidence of
genuine surprise.

The second gap is the target. What the causal manipulation demonstrated is an effect on *learning
rate* -- how much new data shifts belief. SD-069 routes to the action-selection softmax instead.
Adjacent, and both are downstream of the same arousal transient, but not the same mechanism, and
this paper cannot tell us that a burst wired to selection will do anything at all. That is SD-069's
own falsifier (2): the lever fires but writes to a channel with no readout authority.

There is also a partial asymmetry in the correspondence. Sustained pupil here indexes *confidence* --
a meaningful, adaptive quantity. MECH-313's tonic noise floor is a fixed constant with no confidence
semantics whatsoever. So the phasic half of the analogy is considerably tighter than the tonic half,
and any claim that REE implements "the" tonic/phasic split should be qualified accordingly.

## Confidence

0.77. Nature Neuroscience, model-based, and -- unusually for pupillometry -- includes a causal arm
rather than resting on correlation. Discounted for the normative-versus-raw surprise mismatch and
for the learning-rate-versus-selection target mismatch, both of which are stated in the record's
mapping caveat rather than absorbed into the score silently.
