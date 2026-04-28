# Yu, Chen & Shan 2021 — DMS direct-pathway depression permits habit formation

## What the paper did

Yu et al. asked a precise mechanistic question: when habits form, does the dorsomedial
striatum (DMS) play any role beyond simply ceding control to the dorsolateral striatum
(DLS)? Using mouse instrumental conditioning, ex vivo electrophysiology, and chemogenetic
manipulation, they measured plasticity in the two MSN subtypes (direct-pathway striatonigral
and indirect-pathway striatopallidal) of the DMS during habit acquisition. They then tested
whether reversing the observed plasticity disrupted habit formation versus expression.

The key finding: postsynaptic depression at excitatory synapses on DMS direct-pathway
MSNs forms during habit learning. Chemogenetically rescuing this depression -- restoring
direct-pathway excitability to its pre-habit state -- compromised the acquisition of
habitual action but did not affect the expression of habits already formed.

## Key findings relevant to Q-019

For Q-019, this is interesting in a specific way. The three-gate architecture treats
DMS (associative loop) and DLS (sensorimotor loop) as parallel and distinct. Yu et al.
show that during habit formation, the two loops coordinate -- the DMS's direct pathway
must depress for the DLS's habit machinery to take hold. So it is not that DMS simply
disengages and DLS takes over; DMS actively reduces its drive in a specific pathway-
selective way.

This refines the segregation premise: the three loops are anatomically distinct
(supported by Ambrosi & Lerner 2022 in this targeted_review), but they coordinate during
behavioural transitions through specific synaptic mechanisms. Q-019's note about the
"automaticity gradient" -- tasks migrating from sensorium gating to sensorimotor loop
when post-commit metrics improve -- gets a concrete mechanism from this paper. The
migration is mediated by direct-pathway depression in the donor loop.

The acquisition-vs-expression dissociation is also notable. The DMS direct pathway
matters for forming habits, not for running them. This temporal asymmetry is not
currently in Q-019's formulation but probably should be -- the three-gate architecture
needs to distinguish learning-time coordination from execution-time gating.

## How this maps to REE

REE-V3's planned automaticity gradient (post-commit improvement triggering migration
from BG sensorium gate to sensorimotor loop) would benefit from this evidence. The
paper suggests that the migration is not just routing-level but plasticity-level: the
donor loop's direct pathway must depress to permit the recipient loop to take over.

For MECH-090 (BG beta gating motor execution) and MECH-061 (commitment boundary), this
adds a useful constraint -- the boundary between thought-loop control and action-loop
control is plasticity-mediated, not purely gating-mediated. That suggests REE's
implementation might want a slow-changing channel that opens up the action loop when
the thought loop's drive on it depresses.

## Limitations and caveats

The paper studies mouse habit formation in instrumental conditioning. It does not
address the sensorium loop, the limbic loop's contribution, or the thought loop's
relationship to either. So Q-019 gets supporting evidence for the DMS-DLS coordination
story but not for the full three-gate model.

The transfer to humans is moderate-risk: mouse and primate striatal architecture differ
in detail (e.g., anterior caudate functional specialisation), and the timescales of
habit formation differ across species. Mouse studies of striatal plasticity have a
mixed track record of replicating in primates.

## Confidence reasoning

I rate this 0.70. Source quality is high (Cerebral Cortex, modern causal methods,
ex vivo physiology + chemogenetic rescue). Mapping fidelity is moderate -- the paper
supports the segregation+coordination version of Q-019 but is a single mechanistic
study. Transfer risk is moderate. The main reason I do not rate this higher is that
the paper studies dorsal striatum only and does not directly address the three-loop
architecture as a whole.

According to PubMed: [10.1093/cercor/bhab031](https://doi.org/10.1093/cercor/bhab031)
