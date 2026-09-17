# The human brain is intrinsically organized into dynamic, anticorrelated functional networks (Fox et al., 2005)

## What the paper did

Fox and colleagues examined spontaneous BOLD fluctuations in the resting human brain and found that
the cortex organises into two diametrically opposed, widely distributed networks. Within each network
regions correlate positively; between the networks they anticorrelate. One network is made of regions
that routinely activate during tasks, the other of regions that routinely deactivate. None of this
required a task -- the organisation is there in the resting brain.

## Why this is the most important entry in the ARC-084 pull

ARC-084 sets itself a demanding non-degeneracy precondition, and it is right to. The claim is not that
competition exists in REE; V3 already has competition in three places -- basal ganglia winner-take-all
(MECH-090), symmetric Go/NoGo (ARC-030), top-k selection into E3 (MECH-254). The claim is that
competition is a *first-class generative coupling mode* at the field level, carrying its own
parameters, and not a redescription of what those local softmaxes already do. A test is vacuous unless
it can separate those two hypotheses.

This paper offers the cleanest separation I found anywhere in the literature, and it comes from an
unexpected direction: the resting state. At rest there is no decision being taken, no action being
selected, no softmax running. If inter-field competition were simply what local selection competition
looks like from a distance, the resting architecture would have no particular reason to be organised
around a negative sign. It is organised around one anyway. That is a genuine argument that the sign is
structural rather than derivative, and it is the sort of argument ARC-084 needs and cannot obtain from
the local-competition literature it currently cites.

## The limitation that has to be stated first, not last

Fox et al. regressed out the global signal. Murphy and colleagues (2009, *NeuroImage*, PMID 18976716)
subsequently showed mathematically that after global signal regression, the correlation values to a
seed voxel must sum to a negative value, and concluded that global signal regression was most likely
the cause of the observed anticorrelations. Fox and colleagues replied (2009, *J Neurophysiol*, PMID
19339462) that the global signal is genuinely global rather than residing preferentially in the
anticorrelated systems, and that anticorrelated characteristics exist before global regression,
suggesting a biological basis.

I cannot adjudicate that here, and I do not think this pull should pretend to. What I can say is that
the single most load-bearing observation for ARC-084's non-degeneracy has a live methodological
challenge attached to it, and that a governance decision which promotes ARC-084 on the strength of
this entry would be resting a V4 architectural commitment on a contested imaging result. That is the
main reason confidence sits at 0.55 rather than higher.

## The second limitation: one field out of eight

ARC-084 specifies an edge as `{source, target, sign, gain, precision, gate, timescale,
write_authority}`. What this paper delivers is the sign. Correlation-based connectivity is
undirected, so it does not even deliver source and target. Nothing here speaks to gain, precision,
gating, timescale or write authority as independently manipulable parameters -- and the claim's
substance lies in their independent manipulability. An architecture built on this evidence alone would
be considerably more specified than the evidence supporting it, which is a familiar way for a
coherence-map claim to acquire unearned confidence.

## Keeping the claim's own cautions

Two boundaries ARC-084 explicitly asks for, both easy to violate when reading this paper into REE.
This is not synaptic inhibition -- it is a statistical relationship between regional haemodynamic
time-series, several levels of description above any inhibitory synapse. And an anticorrelated edge
here is not pathological, harmful or ethically negative: it is the healthy resting organisation of a
normal brain. Any V4 operationalisation that reads "competitive edge" as "inhibition" or as "penalty"
is testing something other than what this evidence supports.
