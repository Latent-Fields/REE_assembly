# Directional frequency asymmetry: the coherence problem is real, but it is cross-frequency

**Claim tested:** ARC-053 (Temporal Coherence Loop) · **Direction:** mixed · **Confidence:** 0.66

## What the paper did

Bastos and colleagues took electrocorticographic recordings from macaque V1 and V4 and fitted dynamic causal models built on a canonical microcircuit -- a neural mass model with laminar-specific pyramidal populations, so that the model's forward and backward connections correspond to real anatomical projections rather than to abstract arrows. Model comparison then asked which spectral profile each direction of influence actually carried. The answer was an asymmetry: forward connections were mediated predominantly by gamma-band frequencies, backward connections by alpha/beta. This is now one of the most-cited empirical anchors for predictive-coding accounts of cortical hierarchy, where error ascends and prediction descends.

## Why this is the most useful of the three ARC-053 entries, and also the most awkward

ARC-053 says that V(t) requires ascending and descending signals to "meet in the same phase channel at the right moment", and that without a coherence mechanism "predictions and inputs miss each other in time". Notice that this claim only has content if the two streams are genuinely separable things that *can* miss each other. If ascending and descending traffic were carried in one undifferentiated channel, there would be nothing to co-register and the TCL would be decorative.

This paper establishes the premise. Ascending and descending influences are carried in distinct, rhythmically organised, dynamically regulated channels. The co-registration problem ARC-053 posits is real, and that is a genuine and non-trivial support for the *necessity* of the loop.

But it complicates the claim's phrasing in a way I do not want to paper over. The two channels are at *different frequencies*. Gamma up, alpha/beta down. So whatever the TCL does, it cannot be aligning two signals within a single band -- it must be performing a cross-frequency operation, most plausibly something in the phase-amplitude coupling family, where the descending beta phase gates the window in which ascending gamma is admitted. That is a coherent and well-precedented mechanism, and it is arguably a *better* story than the one ARC-053 currently tells, because it explains gating (TCL function 3) and integration-window modulation (function 4) with one primitive. But it is not what the claim says, and "the same phase channel" is under-specified against this anatomy.

I have therefore recorded this as **mixed**: it supports the loop's necessity and sharpens what the loop must be, while requiring the claim's own wording to be tightened before it is falsifiable. That reading is consistent with the non-degeneracy precondition already recorded in ARC-053's `what_would_answer` field -- the claim is not yet statable in falsifiable form, and this paper tells us something specific about *why* and about what a statable version would have to commit to.

## Limitations

The directional asymmetry here is an inference from Bayesian model comparison, so it inherits the assumptions of the canonical microcircuit model. A different generative model could in principle fit the same ECoG data without the laminar-frequency mapping. In practice the finding has held up across species and methods since 2015, which is why I have not discounted it heavily, but the DCM dependency is worth stating.

More importantly for the claim: this paper does not test a coherence-maintaining loop at all. It characterises the structure of the problem. It says nothing about whether any structure solves it, or about whether solving it is a precondition for anything resembling a verisimilitude readout.

## Confidence reasoning

Mapping fidelity is the highest of the three ARC-053 entries at 0.72, because unlike the pulvinar and olivary papers this one is directly about the ascending/descending distinction the claim turns on. It is held below 0.8 because it bears on the claim's *form* rather than its *truth*. Source quality 0.80 for primate ECoG plus a principled generative model, with the DCM caveat. Transfer risk 0.35. The aggregate lands at 0.66, and the most valuable thing in this entry is not the number but the specification finding: **ARC-053 needs a cross-frequency formulation of "phase channel" before a P_i term can be built against it.**
