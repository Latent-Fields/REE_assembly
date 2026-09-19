# Simons, Garrison & Johnson (2017) -- Brain Mechanisms of Reality Monitoring

**Claim tested:** MECH-065 -- *Reality-coherence conflict lane modulates loop precision and commitment thresholds before execution lock-in.*
**Direction:** supports (lane separability) | **Confidence:** 0.71

## What the paper does

This is a synthesis, in Trends in Cognitive Sciences, of what is known about how people tell apart
information they generated themselves -- thoughts, intentions, imaginings -- from information that came
from outside. The authors pull together human neuroimaging, lesion, individual-difference and clinical
work into an emerging neurocognitive characterisation: reality monitoring has identifiable frontal
correlates, most consistently in anterior medial prefrontal cortex; competence at it varies with
anatomical individual differences, notably the presence or absence of the paracingulate sulcus; and its
failures form a continuum running from ordinary real-versus-imagined confusions in healthy cognition
through to hallucinations in mental illness. They close on rehabilitation prospects, which matters
mainly as evidence that the authors take the function to be a modifiable, targetable thing rather than
an epiphenomenon.

## Why I pulled this one for MECH-065

The other two supporting entries in this pull (Cavanagh 2011, Frank 2015) establish that a conflict
signal can raise a pre-commitment threshold. Neither of them touches the question MECH-065 actually
stands or falls on, which is whether *reality-coherence* conflict is a **distinct lane** rather than a
relabelling of generic conflict or surprise. MECH-065 states its own falsifier in exactly those terms:
the claim is refuted if the observed effect "is better explained by existing signals (S1/S3) alone."

This review is the strongest external argument I could find that internal-versus-external provenance
discrimination is its own operation. It has its own substrate, its own individual-difference profile,
its own developmental trajectory, and -- most persuasively -- its own selective breakdown pattern. A
function that can fail while the rest of cognitive control is intact is, prima facie, a separable
function. That is not proof of a separate REE lane, but it shifts the prior.

The review also tells REE what shape to give the channel. Reality-monitoring failure is *graded* and
*continuous with normal cognition*: a nonzero rate of real-versus-imagined confusion is baseline, not
pathology. So RC_conflict should be computed as a continuous provenance-attribution confidence, and the
confirming criterion for MECH-065 should be set on a *shift* in that quantity under manipulation --
never on the absence of misattribution events, which would report failure on a correctly-functioning
system. The individual-difference finding carries a second design warning: if reality-monitoring
competence has a real distribution rather than a fixed value, a REE experiment that treats RC_conflict
sensitivity as an architectural constant may charge between-seed variance to the manipulation.

## The weakness I do not want to paper over

Reality monitoring, as this literature operationalises it, is overwhelmingly a **retrospective**
source-memory judgement: was this remembered item something I saw, or something I imagined? MECH-065
needs a **prospective, pre-commit** signal that moves a threshold before an action is taken. Whether
the same machinery serves online provenance evaluation of an arriving instruction is an assumption
rather than a finding, and it is the assumption that does most of the work in this mapping. I have held
mapping fidelity at 0.66 for that reason and would not want a governance reading of this entry to
quietly forget it.

Two smaller caveats. This is a narrative review, not new data and not a quantitative meta-analysis, so
the weight of each cited effect has to be taken on the authors' summary of it. And REE's four-way carve
of RC_conflict into provenance, temporal, identity and policy components is an engineering
decomposition with no counterpart anywhere in this literature -- nothing here speaks to whether that
carve is the right one.

## Confidence reasoning

Source quality 0.78 -- authoritative authors in a strong venue, but a review. Mapping fidelity 0.66 --
limited principally by the retrospective/prospective mismatch, which is substantive. Transfer risk 0.38
-- human episodic source memory to an agent's online instruction-provenance evaluation is a real leap.
Aggregate 0.71, weighted toward mapping fidelity as the calibration guide directs for an architectural
claim. This entry is doing narrower work than its confidence might suggest: it supports lane
*separability in principle*, and nothing at all about the threshold mechanism, which the other entries
carry.
