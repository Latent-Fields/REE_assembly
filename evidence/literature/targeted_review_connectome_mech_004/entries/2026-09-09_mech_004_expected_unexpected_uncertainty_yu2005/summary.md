# Yu & Dayan (2005), "Uncertainty, neuromodulation, and attention"

**Claim tested:** MECH-004 (control-plane signal-to-knob wiring map)
**Direction:** supports | **Confidence:** 0.82

## What the paper did

Yu and Dayan begin from a normative question rather than an empirical one: if an animal must
infer the state of a world that is both noisy and non-stationary, what does it need to
represent? Their answer is that one uncertainty term will not do. There is the uncertainty you
expect -- a cue you already know to be only 80% valid, noise whose statistics you have learned
and can price in. And there is the uncertainty you do not expect -- the moment the cue's
validity itself changes because the context has shifted underneath you. They formalise this in
a hierarchical generative model where expected uncertainty is estimated *within* an assumed
context and unexpected uncertainty is the signal that the assumed context is no longer the
right one. They then argue, on the strength of pharmacological, lesion and behavioural evidence
from attentional cueing paradigms, that acetylcholine carries the first quantity and
norepinephrine the second.

## What it says about MECH-004

The signal map's K6 and K8 are, more or less, this paper's two quantities: K6 is glossed
"expected uncertainty / channel-specific gain (acetylcholine-like)" and K8 "unexpected
uncertainty / volatility sensitivity (noradrenaline-like)". So the first thing to say honestly
is that this entry is partly archaeology -- it documents where an REE design commitment came
from at least as much as it independently tests it. I do not think that makes it worthless, but
it does mean the entry should not be read as convergent confirmation from an unrelated
direction.

What it *does* contribute, beyond provenance, is an argument for why the non-collapse matters
that is stronger than a preference for parsimony's opposite. MECH-004 asserts throughout --
most explicitly in INV-022, heterogeneous trust allocation -- that precision must not degenerate
into a single scalar confidence number. Yu and Dayan give the functional reason: with one term
you cannot distinguish "this channel is noisy, weight it down" from "my model of the situation
is wrong, rebuild it". In the map's own vocabulary that is exactly the difference between
turning K2 down and escalating K5, and a system that has collapsed the two uncertainties has no
principled way to choose between them. It also supports the signal-side split in S4, where
safety *baseline* (tonic) and safety *volatility* (phasic) are treated as separate encodings
routing to different knobs. That is the same structural move one level upstream.

## Limitations and caveats

The mapping reaches the knobs, not the map. Yu and Dayan have nothing to say about MECH-004's
signal classes, about routing specificity, or about the parts of the control plane doing the
most distinctive work -- commitment depth (K3), the hard veto (K10), the stream/loop/global
precision decomposition. Five of the ten knobs and all six signal classes are untouched by this
paper. An entry that let this stand as evidence for "the wiring map" would be overclaiming by
some distance.

Two further cautions. First, the two uncertainties are *coupled* in the source model, not
independent: unexpected uncertainty is definitionally what forces re-estimation of the context
under which expected uncertainty was computed. A control plane exposing K6 and K8 as two freely
settable scalars can therefore be driven into configurations the source account does not
license, and would not notice. Second, this is a normative model with a fit, not a measurement.
It says what an optimal system should compute and assigns the computations to two
neuromodulators by argument; the assignment has been contested since, particularly for ACh's
role outside cue-validity settings.

## Confidence reasoning

0.82. Mapping fidelity is the highest in this pull (0.88) because the correspondence is close to
verbatim rather than analogical -- but that is also precisely the circularity risk, and I have
capped the aggregate below 0.9 for it. Source quality 0.85 reflects a formally careful,
heavily-cited paper in a top venue, discounted because it is theory plus fit rather than new
measurement. Transfer risk is low (0.25): what is being carried across into REE is a
computational decomposition, and those travel across substrate far better than the anatomical
claims in the other entries in this directory.
