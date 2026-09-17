# Functional connectivity of default mode network components: correlation, anticorrelation, and causality (Uddin et al., 2009)

## What the paper did

Uddin and colleagues took the anticorrelation phenomenon a step past Fox et al. and asked two further
questions of it. First, does the negative relationship have a direction? Using Granger causality on
resting-state data they report that ventromedial prefrontal cortex and posterior cingulate cortex
exert greater influence on their anticorrelated networks than those networks exert back. Second, is
the default mode network homogeneous in this respect? It is not -- vmPFC and PCC show distinct
competitive interactions with different task-related systems.

## Why this is, formally, the best fit for ARC-084

ARC-084 does not claim merely that competition exists between fields. It claims something quite
specific about representational form: that inter-field coupling is a *typed, signed edge* --
`{source, target, sign, gain, precision, gate, timescale, write_authority}`. Fox et al. gives the
sign. What it cannot give, because correlation is symmetric, is source, target or gain.

This paper gives all three. The competitive relationship has a direction. The two directions differ
in magnitude. And -- the finding I find most interesting for REE -- the identity of the competitive
partner depends on which node you start from, not merely on which network. That is an edge-level
property, not a field-level one. If competition between systems were an undifferentiated emergent
consequence of selection dynamics, there is no obvious reason it should be directed, asymmetric in
gain, and node-specific all at once. Those are the signatures of a structured coupling parameter.

## Where I think the finding bites back

The heterogeneity result is a double-edged one for ARC-084, and I would rather surface that than let
it pass as unqualified support. ARC-084 frames the signed edge as a relationship between *fields* --
the cognifold's units. But if vmPFC and PCC, both sitting inside what we would call one field, have
different competitive partners, then the field is not the unit over which competitive structure is
organised. The typed-signed-edge formalism survives that observation comfortably. The specifically
*cognifold*, inter-field framing does not survive it as comfortably. A V4 design taking this
seriously might need edges below field granularity, which is a larger commitment than the claim
currently makes.

## The methodological discount

Granger causality applied to BOLD is the weakest method in this pull, and the weakness is
well-understood rather than speculative: regional differences in haemodynamic response latency can
produce apparent directed influence where none exists neurally. A region that simply has a faster
vascular response will look like it drives a slower one. Since the directedness and the asymmetric
gain are exactly what makes this entry valuable to ARC-084, that confound attacks the load-bearing
part rather than a peripheral one. Source quality is therefore set at 0.72, distinctly below Fox et
al., and overall confidence held at 0.55 despite the better mapping fidelity.

## Confidence

0.55. The unusual shape of this assessment is worth noting for whoever reads it in governance:
mapping fidelity (0.65) is the highest in the ARC-084 set while source quality (0.72) is the lowest.
This is the right paper for the claim, measured with the least trustworthy instrument. That is a
different epistemic situation from a strong measurement of a loosely related thing, and it argues for
a specific follow-up -- a directed-coupling result from electrophysiology or a lesion/stimulation
design, where directionality is not inferred from haemodynamic timing -- rather than for more fMRI.
