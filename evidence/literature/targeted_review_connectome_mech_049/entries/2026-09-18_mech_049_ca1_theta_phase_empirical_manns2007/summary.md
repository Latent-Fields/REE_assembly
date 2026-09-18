# Manns, Zilli, Ong, Hasselmo & Eichenbaum (2007) -- the empirical test, and what it cannot settle

## What the paper did

Hasselmo, Bodelon & Wyble (2002) predicted that if theta rhythm schedules encoding and retrieval into
separate phases, then the preferred theta phase of CA1 spiking should differ depending on whether the animal
is encoding or retrieving. This paper went and looked. CA1 pyramidal cells were recorded in rats performing
two recognition memory tasks -- an odour-cued delayed nonmatch-to-sample task and an object recognition task
based on spontaneous novelty preference -- and spike times were referenced to the concurrent theta LFP.

The prediction held. In the test period of both tasks, the preferred theta phase differed between moments
when the rat inspected repeated (match) items and non-repeated (nonmatch) items. A specific prediction, made
in advance by a published model, confirmed in the predicted direction, in two paradigms. That is a real
success and I do not want to undersell it.

## The part that matters more for REE

The same paper contains a second result that I think is the more important one, and it cuts the other way.

The authors extended the 2002 model to cover the mean phase of CA1 spiking across stimuli inducing *varying
levels* of retrieval relative to encoding -- a continuum running from novel nonmatch stimuli with no
retrieval, through to highly familiar repeated stimuli with extensive retrieval. The modelling showed that
the experimentally observed phase differences are consistent with *different levels of CA3 synaptic input*
to CA1.

Read that carefully, because it reframes the first result. Mean preferred phase is behaving as a continuous
readout of the encode/retrieve *mixture*. It is not reporting which of two regimes the system is in; it is
reporting the blend ratio. A system that smoothly interpolates between encoding and retrieving, never doing
either exclusively, produces exactly the phase difference that was observed.

## Why this is the falsifier-design entry

MECH-049 asserts temporal *compartmentalisation* -- separation sufficient to preserve independence between
fast proposal and slow evaluation, and sufficient to keep ethical constraint from being smoothed into the
optimisation gradient. The obvious way to test that is to ask whether the stages occupy different phases.
That is precisely the instrument Manns et al. applied, and it returned a clean significant result.

But the paper's own model shows that a continuously blended architecture emits the same signature. So the
instrument cannot discriminate. A mean-phase difference is what compartmentalisation produces *and* what
blending produces, and no amount of statistical power on that measure will separate them.

This has a direct consequence for how REE should build a MECH-049 falsifier, and it is the main thing I
would carry out of this pull. Do not operationalise the claim as "are the stages temporally offset?" Any
architecture that smoothly interpolates between proposing and evaluating will pass, including one in which
harm evaluation has been entirely absorbed into the selector and is merely phase-lagged relative to it --
which is the failure MECH-049 exists to prevent. The claim asserts *independence*, so the instrument must
measure independence: whether harm evaluation's output is statistically decoupled from the selector's
gradient, or whether loading one stage degrades the other in the manner shared machinery would predict.
Offset is cheap. Independence is the claim.

There is a structural echo here of the trap recorded in the MECH-039 pull, where a one-hot state instrument
could not represent a state *between* modes and so could not detect graded co-movement. This is the mirror
image: a graded instrument cannot detect whether the underlying states are *discrete*, and so reports
separation for a system that has none. In both cases the instrument's representational form, not its
sensitivity, is what determines whether the claim is testable by it.

## Limitations

Encoding and retrieval are inferred rather than manipulated. A repeated item is assumed retrieval-dominant
and a novel one encoding-dominant, but familiarity covaries with attention, sampling duration, running
speed, and reward expectation, any of which could produce a phase difference with no encode/retrieve
separation involved. The abstract reports neither sample size nor effect magnitude.

And the obvious one: these are rats doing recognition memory. There is no operation anywhere in this dataset
that resembles harm evaluation or veto. The entry evidences the substrate premise of MECH-049 -- that
neural systems do use phase to schedule competing operations -- and is entirely silent on the claim's
ethical limb.

## Confidence

0.50, direction mixed. Both halves are solid, which is why it sits in the middle rather than being scored
down. The a-priori prediction was confirmed, and that is genuine support for the phase-separation framework.
The confirmation is of a mean-phase shift that the authors' own model attributes to graded input level, and
that is genuine evidence against the compartmentalisation reading the claim needs. Its value to REE is
mostly methodological: it tells us the cheap instrument does not work.
