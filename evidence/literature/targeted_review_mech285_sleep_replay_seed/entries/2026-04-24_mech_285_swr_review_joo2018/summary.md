# Joo & Frank 2018 -- single SWRs serve both retrieval and consolidation

## What the paper did

A Nature Reviews Neuroscience synthesis of the sharp-wave-ripple literature up to mid-2018. The review surveys what is known about SWR content, the cognitive functions SWRs are thought to support, and how different SWR types (distinguishable by representational content, behavioural state, and physiological features) map onto distinct computations. The central thesis: a single SWR can simultaneously support retrieval for immediate behavioural use and consolidation for offline schema update, rather than being exclusively slotted into one role.

## Key findings relevant to MECH-285

Two organising claims matter for MECH-285. First, SWR content is multi-modal: replay events differ in whether they encode past, current, or potential-future representations, and these content classes correspond to different downstream functions. Second, priority signals for SWR selection are heterogeneous: reward-modulation (Michon 2019 / McNamara 2014 arm), need-for-planning (Gillespie 2021 decision arm), novelty and consolidation drivers (less well-characterised) each appear to shape different SWR populations. The single-weight-per-anchor architecture implicit in early normative accounts is probably too thin.

## Translation to REE

MECH-285 is a proposal for one specific priority signal: accumulated V_s staleness, consumed by the sleep-phase schema-revision sampler (MECH-275 and MECH-273 consumers). Joo & Frank's multi-mode framing clarifies the architectural scope. MECH-285 should be a priority on the consolidation-SWR subset -- not a global replay-scheduling bias, and not a modulator of retrieval-SWRs. Retrieval-SWRs (the "SWR as decision support" arm, where current task demand dominates) are almost certainly priority-weighted by different signals; Mattar & Daw's need term fits retrieval better than staleness. The implementation recommendation: MECH-285 writes its priority tag in a way that the sleep consumer can read specifically, without bleeding into waking decision-support channels.

This multi-mode reading also bears on the dissociation question. Joo & Frank describe priority signals as heterogeneous and plausibly non-overlapping across SWR subtypes. MECH-285's posit that staleness is dissociable from salience fits naturally if the two signals target different SWR populations -- salience preferentially drives retrieval-SWRs (for immediate decision use of emotionally-tagged memories), staleness preferentially drives consolidation-SWRs (for offline schema update). Dissociation then emerges from the substrate, not from some external arbitration mechanism.

## Limitations and caveats

A review, not primary data. The multi-mode framing is a synthesis of heterogeneous studies and is still an active research question -- the specific claim that retrieval and consolidation SWRs are cleanly separable may not survive future data. The review also does not engage with V_s residuals or any analogue of the epistemic-staleness signal MECH-285 posits; the translation is inferential. As a consumer-scoping constraint on the MECH-285 architecture, it is useful; as a direct test, it is weak.

## Confidence reasoning

High-quality review, leading authors. Mapping fidelity moderate -- the paper shapes the MECH-285 implementation scope rather than testing its predictions. Transfer risk low. Aggregate confidence 0.78.
