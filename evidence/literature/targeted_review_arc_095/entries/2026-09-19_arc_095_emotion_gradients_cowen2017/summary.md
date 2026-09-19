# Cowen & Keltner (2017) -- Self-report captures 27 distinct categories of emotion bridged by continuous gradients

**Claim tested:** ARC-095 (affect.open_extensible_stream_taxonomy) | **Direction:** mixed | **Confidence:** 0.58

## What the paper did

Cowen and Keltner had 853 participants respond to 2,185 short emotionally evocative video clips,
using free response, category judgements and affective-dimension scales, and then asked what
structure the reported-experience space actually has. Two findings matter here. First, the space
needs 27 distinct varieties of reported emotional experience -- considerably more than the classic
basic-emotion five or six, and more than a low-dimensional valence/arousal scheme can carry. Second,
and more interesting, the categories are bridged by continuous gradients: the boundaries are fuzzy,
and the territory between categories is occupied rather than empty.

## Why I have marked this mixed rather than supporting

This is the only entry in the pull that cuts both ways for ARC-095, and the honest thing is to say
so rather than recruit it.

It supports the claim's core. If emotion space is bridged by smooth gradients rather than partitioned
at natural joints, then any register of handles carving that space is drawing convenient lines
through continuous territory. Wherever REE puts a handle boundary, it is making a modelling choice,
not discovering a joint -- and a modelling choice is exactly the sort of thing later evidence should
be allowed to move. That is ARC-095's split/merge permission, arrived at from the geometry of the
space rather than from the history of any one construct. The count reinforces it: 27 categories in
a single elicitation modality, against REE's eleven handles, suggests the register as listed is
coarse.

But it also cuts against the claim as written, and this is the part worth flagging to governance.
A data-driven method recovered a stable, reproducible structure from 2,185 stimuli. That is an
existence proof that an affect taxonomy is the kind of thing a sufficiently large empirical study
*can* settle. "Must not be frozen into a final ontology" is therefore stronger than the evidence
licenses. The defensible version is time-indexed: do not freeze *before* the substrate has generated
the evidence to carve by. That weaker claim is, I think, what ARC-095 actually wants -- its
dependence on SD-011 and its substrate_conditional status already imply it -- but the current
wording asserts something closer to permanent openness, and this paper is a reason to narrow it.

There is also a structural warning here that no amount of later splitting can repair. If the states
*between* handles are occupied, then a register implemented as mutually exclusive categorical
channels with winner-take-all assignment will systematically misrepresent those in-between states.
That is an architecture-level decision, not an ontology-level one: you can rename and split handles
forever and still have the wrong representation if assignment is categorical. Worth separating from
the taxonomy question when V5 gets built.

## Limitations, and why the confidence is the lowest in this pull

The transfer here is the weakest of the five entries and should be treated with real suspicion. This
is human self-report about reactions to video clips. It measures the structure of the emotion
*lexicon* and of reportable conscious experience -- not the structure of the underlying motivational
control signals that REE's handles are meant to name. There is no reason those must agree, and some
reason to expect they do not. REE's register includes fatigue/cost, agency and prediction-error,
which are control-theoretic quantities with no obvious self-report counterpart at all, and excludes
much of what populates the 27-category space (admiration, nostalgia, aesthetic appreciation).

The 27 figure is also method-dependent -- it reflects the stimulus set, the response format and the
dimensionality-reduction choices, and later work using other modalities recovers different counts.
Reading a target number of REE handles off this paper would be a straightforward mistake, and I want
that on the record because the number is the most quotable thing in it.

## Confidence reasoning

Source quality good (0.84): PNAS, large stimulus set, data-driven rather than confirmatory, but
capped by single-modality self-report and the known method-dependence of the count. Mapping fidelity
is low (0.58) and dominates the aggregate -- the paper measures reportable experience structure
whereas ARC-095's handles are control signals, and three of the eleven have no self-report analogue.
Transfer risk high (0.45) for the same reason. Aggregate 0.58, deliberately near the floor of the
moderate band to mark this as support-with-serious-caveats.
