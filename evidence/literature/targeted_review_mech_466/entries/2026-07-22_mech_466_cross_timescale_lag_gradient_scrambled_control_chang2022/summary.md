# Information flow across the cortical timescale hierarchy (Chang, Nastase & Hasson, 2022) -- MECH-466, Q-081

## What the paper did

Listening to a story requires integrating over several concurrent timescales at once -- words
into sentences into paragraphs into a narrative -- and the standard account is a chain of cortical
areas with progressively longer temporal receptive windows. Chang et al. reasoned that if that
chain is real, it should show up as an ordered sequence of response lags between networks during
comprehension.

They measured it with inter-subject cross-correlation, which captures only stimulus-driven
coupling by correlating across participants rather than within. They found a fixed sequence on
the scale of several seconds: early auditory areas first, then language areas, then the attention
network, then the default mode network. The gradient held across eight distinct stories. It was
absent during rest, and absent for a scrambled-story stimulus. A simple computational model
reproduced it from gradual accumulation of information within the boundaries of nested linguistic
events.

## Key findings relevant to the cluster

I include this mainly for the control design, which is the cleanest worked example in this pull
of the discrimination Q-081 is built around.

The threat to the lag-gradient finding is exactly REE's Outcome B. A gradient of response lags
across a hierarchy of areas with different intrinsic timescales could be nothing but those
intrinsic timescales -- structure trivially implied by each component's own rate, requiring no
shared organisation at all. What answers that objection is the scrambled-story condition. Scrambling
preserves the low-level acoustic and lexical input statistics and destroys only the nested event
structure. The gradient disappears. So the gradient is a property of narrative construction, not
of the areas' intrinsic rates.

Translated into REE's design: the prospective run needs a structure-destroying arm alongside the
rate-matched surrogate, and the two are not substitutes. The surrogate destroys cross-stream
alignment in the *analysis*; the scrambled-equivalent arm destroys the event and commitment
landmark structure in the *system*, while leaving the streams, the configured rates and the
environmental input statistics intact. A cross-stream statistic that survives that arm was
measuring the clock. This is a stronger and more direct test than a shuffle control, because it
operates on the mechanism rather than on the data.

The second transferable point is that the model's mechanism -- accumulation within the boundaries
of *nested* events producing cross-scale lag structure -- is the same mechanism MECH-466 proposes
for REE, arrived at independently. That is worth noting and worth not over-reading.

## How this translates to REE

Cross-stream lag is named in Q-081's falsifier as one of three candidate analyses, and this paper
shows it is measurable and informative. But it also shows why a bare lag statistic is the wrong
primary readout for REE, and the reason is sharper here than in the fMRI case.

In fMRI, apparent lag is partly instrumental: the haemodynamic response function varies by region,
so some of any measured lag is filtering. REE has the analogous problem in a worse form. E1
updates every step, E2 every three, E3 every ten. A lag between them is *guaranteed by the
scheduler* with no shared organisation whatever. A cross-stream lag statistic in REE is therefore
closer to an Outcome B detector than an Outcome A one, and should be reported as a control
quantity -- something that must be present and must not explain the result -- rather than as
evidence for the claim.

Inter-subject cross-correlation itself does not transfer. It isolates stimulus-driven coupling by
correlating across brains; REE's nearest analogue is across seeds, which estimates a different
thing -- what is shared across initialisations, not what is coordinated within a run. That may be
a useful quantity in its own right, but substituting it silently would change the question.

## Limitations and caveats

Cross-stream lag is a weaker notion of shared organisation than the homologous transition motifs
Q-081 actually asks about. A fixed lag can arise from a pure feed-forward chain, which is closer
to wired coordination -- Outcome B again -- than to emergent shared organisation. Finding a lag
gradient in REE would be consistent with the streams simply being plumbed in series.

Naturalistic fMRI with all the usual caveats: slow, indirect, haemodynamically filtered signal,
and lags on the order of seconds in a modality whose sampling is on that order.

GOV-ANALOGY-1: analogy, not evidence. The cortical timescale hierarchy is not a finding about REE.

## Confidence

0.61. Source quality 0.85 -- PNAS, Hasson lab, replicated across eight stories, with two negative
controls and a generative model reproducing the effect, which is an unusually complete control
structure for naturalistic work and the reason the entry is here. Mapping fidelity 0.58: the
control *logic* transfers cleanly and the ISC *measurement* not at all. Transfer risk 0.50.

Literature confidence 0.61; experimental confidence for MECH-466 and Q-081 remains 0.0. What this
contributes is a control design, not a result about REE.
