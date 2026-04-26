# Lisman & Jensen 2013 -- The theta-gamma neural code

## What the paper did

Lisman and Jensen wrote what has become the canonical *Neuron* review on theta-gamma cross-frequency coupling as a coding scheme. They synthesised rodent hippocampal LFP, primate working-memory recordings, and computational modelling into a single proposal: when theta and gamma rhythms co-occur in the same region and are phase-coupled, the result is a temporally structured code in which multiple items are represented in an ordered way within a single theta cycle, with each item occupying a different gamma sub-cycle. The review's central evidence comes from CA1 place-cell sequences, in which different spatial locations are read out at different gamma phases of an ongoing theta cycle, and from working-memory load studies in which the number of gamma sub-cycles per theta cycle predicts capacity.

## Key findings relevant to MECH-294

This review is the theoretical anchor MECH-294 most directly inherits from. The core architectural commitment Lisman & Jensen articulate -- that a theta cycle is not a clock signal but a structured temporal frame organised into gamma sub-slots -- is precisely the substrate MECH-294 needs. If the brain is going to bind heterogeneous content streams (goal_latent, action_proposal, risk_estimate, state_summary) into a single phase-aligned packet, the theta-gamma multiplexing machinery is the natural candidate, and Lisman & Jensen's review establishes that this machinery exists.

The review also makes the cross-region case that matters for MECH-294: theta-gamma coupling coordinates communication between brain regions, which is what MECH-294 needs if the four content streams arrive from different sources (goal from prefrontal, action proposal from BG, risk from amygdala/insula, state summary from hippocampus). The review's framing of theta-gamma coupling as an inter-regional binding mechanism is supportive of MECH-294 in spirit even where direct evidence is missing.

## How the findings translate to REE

MECH-294 takes Lisman & Jensen's slot-coding scheme and re-types the slot contents. Where they argue that gamma sub-cycles carry homogeneous list items (different spatial locations, different items in a working-memory list), MECH-294 argues that gamma sub-cycles can also carry heterogeneous content streams -- one slot for the active goal latent, one for the proposed action, one for the risk estimate, one for the current state summary -- and that the phase-aligned theta window binds them into a coherent packet that downstream consumers can read jointly.

The translation is principled but not directly tested. Lisman & Jensen's evidence base is constructed almost entirely around homogeneous content (place sequences, list items). Whether the same gamma-sub-cycle architecture can carry semantically distinct streams without interference, and what would distinguish a multi-content joint packet from a serially read sequence of single-content packets at theta-cycle resolution, are open empirical questions the review does not address.

## Limitations and caveats

Three honest limitations. First, the review treats multi-item coding as ordered serial slots, which is a sequence-organising operation; MECH-294 needs binding-organising. These are computationally different and the review does not distinguish them. Second, the canonical examples (place cells, working-memory items) are all homogeneous content; the heterogeneous-binding case is unaddressed. Third, the review is from 2013 and predates much of the more recent work on goal-content theta sequences (Wikenheiser & Redish 2015) and constant theta cycling (Kay et al. 2020), so its synthesis is incomplete with respect to the content-type diversity MECH-294 needs to bind.

## Confidence reasoning

Confidence 0.74 -- inferential support for MECH-294. Source quality very high (canonical Neuron review). Mapping fidelity moderate because the substrate (theta-gamma multiplexing) is exactly what MECH-294 needs, but the specialisation (heterogeneous-content joint binding rather than homogeneous-list serial coding) is REE-specific and not addressed by the literature this review summarises. Transfer risk modest because the framework is general -- nothing in the review obviously precludes the heterogeneous-binding case, but nothing directly supports it either. Tag: (c) inferential support.
