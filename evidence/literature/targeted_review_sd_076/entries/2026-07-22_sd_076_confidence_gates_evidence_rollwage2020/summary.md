# Rollwage et al. (2020) -- Confidence drives a neural confirmation bias

## What the paper did

Participants made a perceptual discrimination, reported their confidence, and then received further evidence bearing on the same discrimination before a final judgement. MEG recorded the neural signature of evidence accumulation in the post-decisional window, and behavioural plus neural modelling separated how confirmatory and disconfirmatory evidence were integrated as a function of the confidence held in the initial choice.

## Key findings relevant to SD-076

At high confidence, post-decisional processing was sharply reorganised: confirmatory evidence was amplified, and integration of disconfirmatory evidence was abolished rather than merely reduced. Confidence acted as a gate on which evidence was allowed to influence the belief at all, which in turn suppressed changes of mind.

This is, for my purposes, the most useful paper in the SD-076 set, and it is worth being precise about why. The Sharot line of work shows an asymmetry in updating; it does not show what *drives* the asymmetry. Rollwage and colleagues show that the driver is the precision-like variable itself. Applied to SD-076, that turns a one-way drift into a loop: an inflated running-variance estimate reports high precision, high precision gates out exactly the high-error evidence that would deflate it, and the estimate inflates further. If that loop is real in REE, then waking precision drift is not a slow leak that any reasonable time constant would eventually correct -- it is self-amplifying, and a periodic external corrective is not a refinement but a requirement. That is a substantially stronger argument for MECH-204's necessity than the sleep literature makes on its own.

## How this translates to REE

SD-076 currently specifies a fixed asymmetry between the up-rate and down-rate of the running-variance EMA. This paper suggests the asymmetry should itself be a function of current precision. I am deliberately not proposing that change -- SD-076 is registered as bit-identical by default and awaiting behavioural validation as the MECH-204 Phase 7 retest, and adding a second-order coupling before the first-order effect is measured would confound the retest. But it is the obvious next question if the Phase 7 arms come back showing a weaker drift than the sign convention predicts.

## Limitations and confidence

The timescale gap is the honest caveat and I do not want to paper over it. This is a within-trial effect unfolding over hundreds of milliseconds, keyed to a specific just-made commitment. SD-076 is an across-episode drift with no commitment event to key on. Nothing here shows that trial-level gating integrates into a slow bias in a variance estimate; that is REE's inference, not the paper's finding. The other thing worth flagging is that the gating was *complete* at high confidence, not graded -- a linear two-rate EMA cannot express a hard gate, so if the biology is a threshold and REE implements a slope, REE will understate the effect precisely in the high-precision regime where it matters most.

Confidence 0.78, with mapping fidelity carrying most of the weight: this is the one retrieved source where the quantity manipulated and the quantity measured are both the confidence/precision variable SD-076 is about.

*Retrieved via PubMed. [DOI](https://doi.org/10.1038/s41467-020-16278-6)*
