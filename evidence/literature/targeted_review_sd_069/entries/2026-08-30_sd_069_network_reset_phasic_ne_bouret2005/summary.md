# Bouret & Sara 2005 -- the account that puts SD-069's polarity in question

## Why this entry is here

Every other SD-069 entry in this pull supports some part of the claim. This one is included because a
literature pull that only confirms the design it was written from is not evidence, it is decoration.
SD-069 inherits its functional interpretation from Aston-Jones and Cohen's adaptive-gain theory. That
theory has a standing rival of comparable stature, and the rival predicts the opposite sign on the
one parameter SD-069 ships a default for.

## What the paper argues

Bouret and Sara propose *network reset*: phasic activation of locus coeruleus neurons by salient
events provokes or facilitates dynamic reorganisation of target networks, interrupting ongoing
activity and reconfiguring circuits into new functional arrangements that permit rapid behavioural
adaptation. The framing is borrowed from invertebrate neuromodulation, and the supporting material is
primate and rodent LC electrophysiology. It is a theoretical synthesis, not a measurement.

## The polarity problem

SD-069 defaults `phasic_burst_temp_delta` to **-0.5** -- the burst *sharpens* the selection softmax.
The claim's confirming criterion pins the sign explicitly: the phasic signature is
`dR_phasic < -TRANSIENT_MARGIN`, and V3-EXQ-779a scores it that way.

Read through network reset, the expected signature is the other one. If the phasic burst releases the
current configuration so that a different action can win, the softmax should transiently *broaden* --
entropy up, not down -- for exactly as long as the reset lasts. That is a transient on the same
channel with the same timing and the opposite sign.

I do not think this falsifies anything. The two accounts are not cleanly exclusive, and both predict
an event-locked transient, which is the part SD-069 structurally depends on. Nor does "network
reconfiguration" translate uniquely into a temperature sign -- that step is my interpretation and the
review does not take it. What this entry does is mark the negative default as an *inherited design
decision* rather than an established fact. Given that the burst magnitude and sign are a single
config parameter, the cheap and obvious response is to ablate the sign rather than assume it: run the
779-family harness with `+0.5` alongside `-0.5` and let the entropy readout say which direction the
substrate actually supports.

## A second, sharper implication

Network reset casts the phasic burst as an *interrupt on ongoing commitment* -- functionally much
closer to the ARC-016 commit/de-commit gate than to a selection-temperature nudge. SD-069's title
goes out of its way to say it routes to the selection softmax and *not* to the ARC-016 gate that
carries the MECH-104 volatility_interrupt claim, which is a sensible separation of concerns for claim
hygiene. But if the phasic lever turns out to produce no measurable transient on pre-commit softmax
entropy while the same surprise signal does move the commit gate, that outcome is anticipated by this
account and not by adaptive gain. It would mean the routing decision, not the lever, was the error --
a much more informative failure than a null.

## Limitations

A 2005 theoretical review, roughly twenty years older than the rest of this pull, synthesising others'
electrophysiology rather than reporting data. Mapping fidelity is scored at 0.52 because the entry's
whole value lies in flagging an assumption, and the inferential step from circuit reconfiguration to
softmax temperature sign is mine, not the authors'. It should be read as a reason to test the sign,
never as evidence that the sign is wrong.

## Confidence

0.58, filed as `mixed`: supports SD-069's timing architecture (event-triggered, transient), contests
its polarity default.
