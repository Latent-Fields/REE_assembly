# Powers, Mathys & Corlett (2017) -- Pavlovian conditioning-induced hallucinations result from overweighting of perceptual priors

**Claim tested:** MECH-065 -- *Reality-coherence conflict lane modulates loop precision and commitment thresholds before execution lock-in.*
**Direction:** supports (ratio account) | **Confidence:** 0.74

## What the paper did

Powers, Mathys and Corlett used a Pavlovian conditioning paradigm that induces *conditioned
hallucinations*: pair a visual cue with a tone often enough and people begin to report hearing the tone
when it is not played. The design is the elegant part. Four groups were crossed orthogonally on two
factors that usually travel together and are usually confounded -- whether a person hears voices, and
whether they have sought treatment. That crossing lets the study ask which computational signature
belongs to the symptom and which to the help-seeking.

People who hear voices were significantly more susceptible to the conditioned hallucination.
Functional neuroimaging identified a mediating circuit, and computational modelling of perception --
a hierarchical Gaussian filter -- localised the group difference to the *weighting of perceptual priors
relative to incoming sensory evidence*. The two groups' signatures dissociated: voice-hearing and
treatment-seeking did not reduce to a single axis of "more prior weighting."

## Why this matters specifically to MECH-065

MECH-065's most distinctive commitment, and the one that makes it falsifiable rather than vague, is the
ratio framing: the reality-coherence threshold should be `ratio(E1_precision, authority_signal_precision)`,
not an absolute authority-signal magnitude. The claim's own notes rest that commitment entirely on
Sterzer et al. (2016) -- a theoretical review, already pulled under Q-018. This paper is the
experimental and computational counterpart that grounding was missing.

Two things transfer. First, the substantive result: a system whose prior precision is too high relative
to its sensory likelihood precision *perceives what it expects rather than what is there*, which is the
perceptual form of exactly the authority-spoofing worry that motivated REE's RC lane. Second, and more
immediately useful, the *method*: the HGF estimates prior precision and likelihood precision as
separately identifiable parameters. That separability is what MECH-065's own dissociation arm requires
-- hold authority-signal strength fixed and vary internal precision, hold internal precision fixed and
vary authority strength, and confirm that equal movements in the *ratio* produce equal threshold shifts.
Without a fitting procedure that can recover the two terms independently, that arm cannot be run at
all, and the claim's stated falsifier ("magnitude alone predicts the shift as well as the ratio does")
cannot be evaluated.

## The gap that keeps this below 0.8

This is *perceptual inference*, not *decision commitment*. Powers et al. measure what the system
reports perceiving under a precision imbalance. MECH-065 asserts something about the threshold of
evidence required before the system locks in an action. Those are different stages of the loop, and I
can construct no argument from this paper that rules out a precision imbalance distorting perception
while leaving the commitment threshold entirely untouched. The honest position is that this entry
supports the *ratio quantity* and its measurability, and the Cavanagh/Frank entries support the
*threshold mechanism*, and nothing in this pull joins the two ends together. That join is precisely
what an experiment would have to establish.

There is also a quieter trap worth flagging for whoever designs that experiment. The ratio account only
has content when both of its terms are genuinely uncertain. If REE delivers its authority signal as a
discrete, unambiguous token -- source verified, source spoofed -- then there is no likelihood precision
to divide by, and the ratio collapses silently into the magnitude account that MECH-065's own falsifier
identifies as the refuting outcome. An experiment built that way would *look* like a clean test and
would in fact be incapable of dissociating the two hypotheses. The authority signal must arrive as
noisy, graded evidence for the test to mean anything.

Finally, the orthogonal-group result carries its own warning: susceptibility did not vary along one
axis. A REE arm that sweeps precision ratio and expects a single monotone behavioural readout may be
superimposing two different failure modes and reading the superposition as noise.

## Confidence reasoning

Source quality 0.88 -- Science, a design that separates symptom from help-seeking, modelling by the
authors of the framework, an imaging circuit alongside, and a result that has held up. Mapping fidelity
0.62 -- the perceptual-versus-commitment stage gap is real and I have not inflated the number to hide
it. Transfer risk 0.42 -- that gap again, plus a clinical sample. Aggregate 0.74, weighted toward
mapping fidelity per the calibration guide for architectural claims, which is what pulls it below where
the venue alone would put it.
