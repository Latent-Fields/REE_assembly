# Wolff et al. (2022) -- Intrinsic Neural Timescales: Temporal Integration and Segregation

## What the paper did

This is a *Trends in Cognitive Sciences* review pulling together the intrinsic-neural-timescale (INT) literature across resting-state fMRI, EEG and MEG, and across several species. Its organising claim is that INTs -- operationally, the decay of the autocorrelation function of ongoing neural activity -- form a hierarchy: short in unimodal sensory regions, long in transmodal association regions. The review's contribution beyond cataloguing that gradient is functional. Wolff and colleagues argue that where a region sits on this gradient determines whether it *integrates* incoming input into an extended temporal whole or *segregates* it into discrete events, and they connect this to the temporal structure of perception and, more speculatively, of conscious experience.

## What it says about MECH-021

MECH-021 says the subjective now is a control surface across temporal horizons. Strip the control language for a moment and there is a prior question: does the brain have a *now* with a width at all, or is that an artefact of how we talk? This review is the most direct empirical answer I found. The width is measurable, it is regionally graded, it replicates across recording modalities and species, and -- this is the part that matters for REE -- the width is functionally consequential rather than epiphenomenal. Regions with long INTs integrate; regions with short INTs segregate. That is very close to what REE asserts when it distinguishes `ThetaBuffer.summary()` from the instantaneous `z_world`.

It also supplies the corollary readout in MECH-021 with a plausible target. The claim proposes, as a secondary measurement, that commit decisions should be better predicted (AUC) by the buffer summary than by the instantaneous latent. Wolff et al. make that a reasonable expectation rather than a shot in the dark: if commitment is a transmodal, long-INT operation, the integrated vector should carry the decision-relevant signal.

## Limitations and caveats

Two reservations, one of which I think is serious.

The minor one: this is a review, not a primary result. It aggregates, and aggregation launders methodological heterogeneity. INTs estimated from BOLD autocorrelation and from MEG are not obviously the same quantity, and the field has not fully settled what the autocorrelation decay *is* -- a genuine integration window, or a summary statistic of recurrent noise that correlates with one.

The serious one is the perception/action gap. Everything here concerns how input streams are parsed. MECH-021 is a claim about *commitment* -- whether E3's selection is computed over the window or over the current sample. To get from this review to MECH-021 you must assume the window that binds perception is also the window that gates action, and that assumption is doing real work while being neither tested nor asserted by the authors. I have kept mapping fidelity at 0.55 for exactly this reason.

There is a third point worth flagging because it cuts against REE's experimental design rather than against the claim: the review reports that intrinsic timescales are not fixed structural constants but vary with task and state. REE's discriminative pair holds `theta_buffer_size` fixed per arm (1 versus 10). If the biological window is set adaptively, then the REE manipulation tests something narrower than the claim's full content -- it tests whether a *fixed wide* window beats a *fixed narrow* one, not whether a *well-set* window beats a badly-set one. That is a real limitation of the planned falsifier, and it is sharpened by the Cellier et al. entry in this same pull.

## Confidence reasoning

0.60. Source quality 0.78 -- strong venue and a competent synthesis, but review-level and resting on a measure whose interpretation is still contested. Mapping fidelity 0.55, limited by the perception-to-action inference. Transfer risk 0.40, the same graded-integration abstraction as the Chaudhuri entry, which travels reasonably well. The net is moderate support for MECH-021's framing of a widthed now, with essentially nothing said about the harm-restraint clause the claim lives or dies on.
