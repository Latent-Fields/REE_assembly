# Haggard (2017) -- Sense of Agency in the Human Brain

## What the paper did

Haggard's Nature Reviews Neuroscience synthesis is the current canonical statement of the neuroscience of agency. It integrates three major strands: the comparator model (Frith, Blakemore, Wolpert), the intentional-binding paradigm (Haggard's own lab), and the cue-integration framework (Moore, Synofzik, and colleagues). The review does not report new experiments but adjudicates between these frameworks and offers a synthesis that subordinates the classical comparator model to a broader multi-cue account.

## Key findings relevant to an SD-003 successor

Three claims matter for REE. First, the sense of agency is not a single signal. Haggard argues it arises from at least three converging cues: a prospective intentional signal (motor preparation, selection, motor readiness potential), a sensorimotor comparator signal (the Frith-Wolpert forward-model residual), and a retrospective outcome signal (did what happened match what I wanted). Second, these cues are integrated following optimal cue-integration principles: the weight each cue carries depends on its reliability. Third, there is a clinical dissociation: healthy volunteers rely primarily on the comparator (predictive) while schizophrenia patients, in whom the comparator is thought to be compromised, rely more on retrospective outcome matching. This retrospective reconstruction can produce systematic misattribution -- the same mechanism that underwrites delusions of control.

The implication is that the classical Frith 2000 comparator is a real and central mechanism but is insufficient to explain the full phenomenon of agency attribution. Intentional binding effects -- the subjective compression of time between a voluntary action and its outcome -- persist even when the comparator is degraded, and can be produced by prospective cues alone.

## Translation to ARC-033 and the SD-003 successor

For the minimum viable SD-003 successor, this paper reinforces the case for starting with a single-pass comparator: z_harm_s_obs - z_harm_s_pred, driven by E2_harm_s. That is the predictive half and it is architecturally the cleanest. But Haggard warns that REE should not expect a pure comparator to reproduce the full biological agency signal. A natural next step after the comparator lands would be to add: (1) a prospective signal from commitment strength or action-selection precision, and (2) a retrospective signal from outcome-to-goal compatibility checked independently of E2_harm_s. The three would then be combined by precision-weighted cue integration. This maps naturally onto existing REE claims: MECH-094 (hypothesis tag as write gate), ARC-016 (dynamic precision from E3), and the commitment-boundary architecture.

The clinical dissociation is also worth carrying into the experiment design. If E2_harm_s is weak during early training, the REE agent should be observed reconstructing agency from outcomes after the fact -- and this should produce systematically worse attribution accuracy than the predictive mode. If the agent does not show this dissociation, the implementation of cue integration is probably incorrect (the agent is using one cue only rather than weighting).

## Limitations and caveats

Haggard 2017 is scope-broad: it is about agency for ordinary voluntary action (button presses, reaches, gestures) in healthy human observers. REE's SD-003 problem is narrower: attributing changes in harm proximity to self vs environment during navigation. The cue-integration framework scales up cleanly in principle but may be overkill for the immediate task. A minimal single-pass comparator based on Frith 2000 plus Shergill 2003 may be sufficient for the first REE validation, with Haggard's multi-cue enrichment reserved for later.

A more subtle issue is that the review does not dissect nociceptive / harm-specific agency separately from motor-sensory agency. For Haggard and the field the sense of agency is unitary and applies to movement in general. Whether the same cue-integration architecture operates on harm-proximity signals is not established. It is a plausible extrapolation -- there is no obvious reason the brain would run different architectures for different modalities of self-caused change -- but it is an extrapolation.

## Confidence reasoning

Source quality is high (Nature Reviews Neuroscience, authoritative synthesis by the leading experimentalist). Mapping fidelity is moderate because the paper is broader than REE's immediate problem and the transfer to harm-proximity attribution is an inference. Transfer risk is moderate. The paper is a mixed-direction entry: it supports the core comparator architecture (hence 'supports' for the single-pass design), but it warns that comparator alone is insufficient (hence the mixed classification). Overall confidence 0.68.

Based on article retrieved via PubMed search. DOI: https://doi.org/10.1038/nrn.2017.14
