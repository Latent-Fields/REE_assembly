# Carr, Jadhav & Frank (2011) -- Hippocampal replay in the awake state

## What the paper does

Carr, Jadhav, and Frank synthesise a decade of awake-SWR electrophysiology into a
dual-function framework: the hippocampus produces SWRs both during offline states
(NREM sleep, quiet wakefulness) and during active waking, and the awake SWRs split
into at least two functionally distinguishable populations. Quiescence-flanked awake
SWRs -- those occurring during reward consumption, grooming, or pauses in motion
-- are proposed to subserve consolidation (writing the trace forward into
longer-term storage). Planning-flanked awake SWRs -- those occurring just before
movement onset at a choice point -- are proposed to subserve retrieval (reading
the trace for action selection). The authors argue that these two populations
are behaviourally, temporally, and functionally segregated despite sharing the
same underlying substrate (the SWR generator).

## Relevance to MECH-261

This paper is the closest thing the literature has to a direct biological
precedent for MECH-261. The core mechanism MECH-261 posits -- that a single
substrate produces different downstream consequences depending on a mode variable
-- is exactly what Carr and colleagues document at the awake-SWR level. The SWR
substrate is shared, but whether the SWR writes to cortex (consolidation) or
gates trajectory into the planning system (retrieval) is systematically segregated
by behavioural context. For REE, the mapping is: MECH-261's internal_replay mode
corresponds to quiescence-flanked awake SWRs (consolidation-oriented, write-enabled
to cortical substrates); MECH-261's internal_planning mode corresponds to
planning-flanked awake SWRs (retrieval-oriented, write-suppressed to cortex but
write-enabled to trajectory proposal buffers).

The critical architectural point is that the *same generator* produces both, and
the downstream gating is context-conditioned. That is the MECH-261 abstraction in
miniature. It supports the design decision to implement a shared SWR-analog
mechanism in V3 with a gate variable rather than separate generators for each
mode.

## Caveats and mapping risks

Carr and colleagues frame the segregation as behavioural-context-dependent, not
mode-dependent in the salience-network sense MECH-261 invokes. Their causal arrow
runs from behavioural context -> SWR-subpopulation -> downstream effect. MECH-261
proposes that the salience network (SD-032a) is the explicit coordinator of the
mode variable. These are compatible but not equivalent: the salience-network
framing predicts that a lesion of SD-032a would abolish the SWR-subpopulation
segregation, which is a strong empirical commitment not tested in this paper.
The rodent literature has not, to my knowledge, directly tested salience-network-
dependent segregation of awake SWR subpopulations, so this is a V3-pending
prediction of MECH-261 rather than an established biological fact.

A second caveat: the paper does not posit any mode for offline_consolidation
distinct from internal_replay. MECH-261's four-mode family (external_task /
internal_planning / internal_replay / offline_consolidation) is a coarser
abstraction than the awake-SWR literature has directly validated. The
offline_consolidation mode is a legitimate extrapolation from the sleep-SWR
literature but is not this paper's focus.

## Confidence reasoning

This is the highest-confidence entry in the pull because the mapping is tight.
Source quality is high (Nature Neuroscience, Frank lab -- one of the few labs
with direct awake-SWR recording capability). Mapping fidelity is high because
the consolidation/retrieval distinction maps almost directly onto internal_replay
vs internal_planning. Transfer risk is moderate because the salience-network
coordinator hypothesis is an overlay not validated by this paper. Aggregate
confidence 0.82.
