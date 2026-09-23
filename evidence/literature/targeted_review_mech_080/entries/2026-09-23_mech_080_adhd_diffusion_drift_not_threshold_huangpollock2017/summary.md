# Drift, not boundary, in ADHD (Huang-Pollock et al., 2017)

## What the paper did

Ninety-seven children with ADHD and thirty-nine controls, aged eight to ten, performed
go/no-go tasks at several event rates. The authors -- who include Ratcliff and McKoon, who
built the diffusion model -- decomposed the reaction-time and accuracy data into the model's
separate parameters: drift rate (how fast and cleanly evidence accumulates), boundary
separation (how much evidence is required before committing), starting point (prior bias),
and non-decision time.

ADHD children failed more inhibitions at fast event rates. The decomposition put that on a
*reduced drift rate* toward the no-go decision, together with an increased starting point.
Not on a lowered boundary.

## Why this is the sharpest challenge to MECH-080

MECH-080's arm 1 is explicit: ADHD is truncation-biased, the BG urgency threshold is too low,
and the consequence is premature commitment. That is a statement about a *threshold*. The
diffusion model exists precisely to separate a threshold account from an accumulation-quality
account of the same surface behaviour, because the two are behaviourally confusable -- both
produce fast, error-prone responding -- and this study ran that separation with adequate
power on the target population. The answer was accumulation quality.

The consequence for MECH-080 is not merely that one arm has the wrong label. It is that arm 1
may fall inside the claim's own exclusion clause. MECH-080 states that a failure is
uninformative if all effects reduce to lost competence. Drift rate *is* competence -- it is
the rate at which the system extracts decision-relevant signal from its input. If ADHD's
prematurity is a drift phenomenon, then a REE experiment that shortens `rollout_horizon`,
observes premature harmful commits, and reads that as an ADHD analog has not modelled ADHD.
It has modelled a competence reduction and given it a clinical name. Given what is already
known about V3's conversion ceiling, that is the most likely thing such an experiment would
in fact produce.

## The limit of the challenge

I do not want to over-read this, and the limit is a real one. A go/no-go task has no forward
rollout in it at all. The boundary parameter the authors did *not* find a difference in is an
analog of REE's E3 commit threshold, not of `config.e2.rollout_horizon` -- REE keeps those
in different places, and this paper cannot speak to rollout depth because its task never
requires any. So the paper does not show that rollout truncation is the wrong parameter for
ADHD. It shows that the prior question -- is ADHD's premature commitment a threshold
phenomenon at all -- has an answer, and the answer is unfavourable to the assumption arm 1
rests on. The increased starting point is worth holding onto as well: prematurity here is
jointly produced by bias and poor accumulation, a two-parameter story that no single
truncation set-point reproduces.

The paediatric sample is the other limit. Eight-to-ten-year-olds with ADHD to a REE agent is
a long transfer, and I have priced it at 0.40.

## Confidence

0.70, `weakens`. This is the entry I would put in front of governance first if MECH-080 is
ever proposed for promotion, because it converts a vague worry about the competence confound
into a specific, measured, well-powered finding about the exact disorder in arm 1. Mapping
fidelity at 0.60 is the honest discount for the single-step task; it is not enough to change
the direction.
