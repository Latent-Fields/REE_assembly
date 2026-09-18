# Orbitofrontal reality filtering (Schnider 2013)

## What the paper does

This is Schnider's own synthesis of the research programme he built around a deceptively simple
clinical question: how does the brain decide that a memory it has just evoked refers to *now*?
The paradigm is a continuous recognition task run twice. In the second run, a stimulus that the
subject genuinely saw -- in the first run -- must nonetheless be rejected as "not yet seen in this
run". Nothing about the memory's strength, vividness or accuracy licenses the rejection; only its
relation to the present does. Patients who fail this task are the patients who confabulate and act
on their confabulations, and who are disoriented. The review's conclusion is that the brain solves
this with a phylogenetically old orbitofrontal faculty -- extinction -- together with reward-system
structures, and that failure of this filter, rather than failure of memory storage, is what produces
behaviourally enacted confabulation.

## Why it bears on MECH-037

MECH-037 posits that E1-generated content should not reach high-precision commitment unless it is
supported by hippocampal trace structure and temporal-ordering signals, and that gate failure
produces confabulation-like high-confidence commitment of ungrounded content. The second half of
that is, as near as human neuroscience gets, simply true, and this review is the best single
statement of it. There is a dissociable gate; it sits upstream of acting-upon; its failure
signature is confabulation plus disorientation; and it is not reducible to graded memory
degradation. That is real support for the architectural shape of the claim -- a licensing stage
between candidate generation and commitment, distinct from the verifier that checks content.

But the review is equally clear about something MECH-037 is not. The gating computation Schnider
describes is *extinction*: the suppression of memory traces that no longer carry current
behavioural or reward relevance. That is a relevance computation performed by posterior medial
orbitofrontal cortex and basal-forebrain reward structures. It is not a computation over trace
presence, and it is not a computation over temporal order. MECH-037 as written in
`docs/architecture/papez_circuit.md` says the gate reads "hippocampal trace presence, temporal
ordering confidence, and recency flags". The human mechanism this claim is modelled on reads
something else.

## How I would translate it

I do not think this retires the claim. I think it identifies a substitution that happened somewhere
between the thought fragment and the architecture doc: the *function* (provenance gating before
commitment) was imported faithfully, and the *implementing signal* was filled in from REE's own
hippocampal machinery because that is what REE has. The honest version of MECH-037 would carry two
candidate gating variables -- trace/ordering support, and an extinction-like relevance suppressor --
and would treat "which one licenses commitment" as the open question rather than as settled. That
also gives the claim a non-degenerate experiment, which it currently lacks: vary trace support and
relevance independently and see which one moves commitment rate.

## Limitations and confidence

This is a narrative review, so the numbers live in the primary papers, not here. The operational
construct -- a two-run continuous recognition task -- is much narrower than REE's general
provenance gate over arbitrary E1 content, and I would not want to lean on the generalisation
without the ERP papers that pin down timing and dissociation (which is why the Liverani and
Bouzerda-Wahlen entries in this directory matter). And there is a circularity to guard against: the
paper is about orbitofrontal cortex, and MECH-037 is about a Papez-like loop. Reading this as
confirmation of the Papez routing would be reading the conclusion into the evidence. I have set
confidence at 0.62 -- high source quality, moderate mapping fidelity, and a real transfer risk --
and direction to `mixed`, because the paper supports the claim's architecture while weakening its
stated mechanism.
