# Leech & Sharp 2013 — The role of the posterior cingulate cortex in cognition and disease

**Source:** *Brain*, [10.1093/brain/awt162](https://doi.org/10.1093/brain/awt162). Via PubMed (PMID 23869106).

## What the paper does

Leech and Sharp synthesise the PCC literature -- anatomy, physiology, healthy-subject fMRI, and clinical (especially traumatic-brain-injury) data -- and propose a new functional model: "Arousal, Balance, and Breadth of Attention." They argue PCC is heterogeneous (dorsal vs ventral subdivisions have distinct functions), is central to the default mode network, and that its activity varies systematically with arousal state, with the balance between internally-directed and externally-directed attention, and with the breadth of attentional focus. Crucially, they propose dorsal PCC tunes whole-brain *metastability* -- how stable network activity is over time -- and that this tuning is how PCC shapes attentional focus.

## Key findings relevant to the claim

- **PCC is part of the DMN and shows strong task-related deactivation** during externally-focused attention. Reactivation correlates with autobiographical memory, future simulation, and mind-wandering.
- **Dorsal/ventral PCC dissociation**: different patterns of activation across task types, different connectivity profiles, different clinical vulnerability. PCC is not a unitary region.
- **Arousal modulates PCC response**. Activity varies with sleep, anaesthesia, and attentional lapses; PCC is one of the first regions to deactivate as arousal falls.
- **Metastability framing**: the ABB model proposes dorsal PCC adjusts how rigidly or flexibly the brain's network activity transitions between states. Rigid metastability -> over-focused, inflexible; loose metastability -> unstable, distractible. PCC damage (especially in TBI) produces exactly these attentional dysregulations.
- **PCC is clinically protected against stroke** (good vascular supply), so focal lesion data is sparse; most clinical evidence is from TBI, Alzheimer's (early amyloid deposition and hypometabolism), and psychiatric conditions.

## How this maps onto REE (the translation)

In the cingulate-substrate cluster, the PCC-analog is the module responsible for **mode-switching between external action and internal cognition** -- the control-plane coordinator that decides when the agent is in task-execution mode vs planning/replay/simulation mode. For ree-v3 this is distinct from (but adjacent to) the roles already mapped:

- **AIC-analog (urgency interrupt)**: triggers immediate state change on salient events
- **dACC-analog (adaptive control / value integration)**: computes policy-update magnitude during ongoing action
- **aMCC-analog (effort / credit assignment)**: assigns credit to costly actions
- **PCC-analog (metastability / mode coordination)**: tunes how rigid or flexible the current mode is, and coordinates transitions between external/task and internal/DMN modes

ree-v3 has pieces: commit-state boundary (partial mode distinction), INV-049 sleep (offline phase), MECH-092 micro-quiescence replay (within-session replay), MECH-094 hypothesis tag (write-gate across modes). What it lacks is a coordinator that selects between these based on current arousal / urgency / attentional demand. The PCC-analog is that coordinator.

A concrete architectural implication: ree-v3 should have an explicit *mode* variable (at minimum: external_task, internal_replay, internal_planning, offline_consolidation) and a transition function that tunes the stability of the current mode. The PCC-analog writes this stability parameter. High stability = committed to current mode, resist transitions; low stability = easily transitioning. The other cingulate modules (AIC, ACC, MCC) can then write *into* this state via the PCC-analog rather than directly forcing mode transitions.

This is the region of the new SD cluster with the weakest computational specification in the biology -- Leech & Sharp's model is a proposal, not settled consensus, and translating "tunes network metastability" into a ree-v3 operation is non-trivial. A conservative extraction would be: "PCC-analog handles the external-vs-internal attention partition and coordinates offline phases with task phases." That's enough to justify the claim and leaves implementation details for downstream design work.

## Limitations and caveats

PCC function is contested. The "default mode" framing is consensus; the specific computational role is not. Leech & Sharp's metastability model is a synthesising proposal but other accounts emphasise autobiographical memory (Buckner line), or topological integration (Margulies line). For ree-v3 the metastability framing is useful but should not be treated as settled.

Clinical data dominates the PCC literature because of lesion rarity in healthy populations. This tilts findings toward what happens when PCC fails (TBI, Alzheimer's attention) rather than toward what it does when it works. The normal-function inferences are therefore somewhat indirect.

Transfer risk is moderate-to-high. "Tunes whole-brain metastability" does not have a clean ree-v3 operational translation. The simpler extraction (external-vs-internal attention coordinator) is safer but less informative. Adopting the full ABB model for ree-v3 is probably over-commitment.

## Confidence reasoning

0.72 -- the lowest in the pull. PCC is the least-tight anatomical-to-functional mapping in the cingulate subdivisions, and the specific computational role is genuinely contested. Source quality is good (*Brain* review, well-regarded authors) but the ABB model is a proposal, not a consensus. Mapping fidelity is moderate -- the role exists and matters for ree-v3, but the operational specification is coarse. Transfer risk is moderate-to-high. Included because without a PCC-analog the cingulate substrate cluster would miss the external/internal attention dimension -- but the specific implementation for ree-v3 should stay conservative.
