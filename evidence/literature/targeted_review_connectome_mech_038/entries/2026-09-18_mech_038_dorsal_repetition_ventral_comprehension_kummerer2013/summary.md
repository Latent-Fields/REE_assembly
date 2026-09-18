# Kummerer et al. (2013) -- Damage to ventral and dorsal language pathways in acute aphasia

**Claim tested:** MECH-038 (arcuate-like sequence-to-motor channel nudges language emergence)
**Direction:** supports | **Confidence:** 0.74

## What the paper did

One hundred patients with acute post-stroke aphasia were scanned and tested within days of onset. The authors combined
voxelwise lesion-behaviour mapping with probabilistic fibre tracking, deriving dorsal (superior longitudinal /
arcuate) and ventral (extreme capsule) tract masks from healthy controls and then measuring, per patient, how much of
each tract the lesion overlapped. The behavioural measures were repetition and comprehension.

The result is a double dissociation along the tracts. Overlap with the dorsal tract correlated negatively with
repetition and not with comprehension; overlap with the ventral tract correlated negatively with comprehension and not
with repetition. The acute timing matters more than it might seem: chronic aphasia data are contaminated by months of
reorganisation, and a tract-function correlation measured a year out is partly a correlation with how well the brain
recovered. Here that confound is largely absent.

## How this bears on MECH-038

The architecture doc for MECH-038 asserts two things that this paper tests directly: that the AF analog is a *fast
sequence-to-motor channel*, and that meaning grounding rides a separate, ventral-style route, with neither sufficient
alone. Kummerer et al. are the human lesion evidence for that division. Cut the dorsal route and the deficit is in
reproducing a *form*. Cut the ventral route and the deficit is in *understanding*. The channel MECH-038 proposes is, on
this evidence, correctly characterised as carrying sequence to articulation rather than carrying meaning.

The operational consequence for the REE build is a constraint I think matters more than the confirmation does. If the
LESION arm severs routing in a way that also degrades semantic alignment, the experiment has lesioned both streams and
the result cannot be read against MECH-038's criteria at all -- it would look like "no emergence in LESION", which the
claim lists as falsifying its nudge framing, when in fact it would only mean the manipulation was too broad. The ON and
LESION arms must differ in routing of signal form and in nothing else. This paper is what licenses saying that is
possible: the two functions really do come apart.

## Limitations and where the mapping strains

Repetition is imitation of an experimenter-supplied target. MECH-038's ON arm routes *self-generated* sequence
summaries -- hippocampal rollouts, E1 summaries -- into signalling affordances. Whether the dorsal channel carries a
self-initiated signal with the same dependence is not something a repetition task can answer, and I would not want the
REE design to assume it does without saying so.

The attribution to tracts is also an inference rather than a measurement. Stroke lesions follow vascular territories,
not white-matter bundles, so dorsal-tract overlap is correlated with damage to the temporoparietal grey matter the
tract passes through. The paper handles this as well as lesion studies can, but it cannot randomise which tract gets
hit. And the dissociation is graded: dorsal-damaged patients repeat badly, not not at all. That graded quality is
incidentally the shape MECH-038's nudge framing predicts, which is worth noting since the Schomers entry in this
directory points the other way.

Finally, and this is the boundary that limits the whole entry: these are adults with an already-acquired language
system. The paper says what the channel does once language exists. It says only indirectly whether the channel biases
language toward emerging in the first place, which is what MECH-038 actually claims. The Northam entry addresses that.

## Confidence reasoning

Source quality 0.85 -- N=100, acute timing, Brain. Mapping fidelity 0.70: the dorsal/ventral functional split transfers
cleanly onto the claim's architecture; the repetition-versus-self-generation gap and the acquired-versus-emerging gap
do not. Transfer risk 0.35, moderate and somewhat reduced by MECH-038 explicitly framing the AF as a functional analog
rather than an anatomical requirement. Aggregate 0.74.
