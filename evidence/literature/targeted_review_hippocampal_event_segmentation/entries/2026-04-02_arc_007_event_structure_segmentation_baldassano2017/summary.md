# Baldassano et al. (2017) — Hippocampal Event Boundaries: The Neural Substrate of ARC-007 Segmentation

**Claims tested:** ARC-007, MECH-022
**Evidence direction:** supports | **Confidence:** 0.76

---

## What the paper did

Baldassano and colleagues tackled a fundamental question: how does the brain parse continuous experience into discrete episodes? Participants watched the first episode of BBC Sherlock in an fMRI scanner, then later freely recalled the narrative. The researchers applied a Hidden Markov Model to the fMRI data across brain regions, fitting the model to identify where in time the brain spontaneously transitions between distinct neural states — the boundaries between events.

The results revealed a nested hierarchy of event structure. Early sensory regions (auditory cortex, early visual cortex) showed frequent, fine-grained boundaries matching fast perceptual transitions. High-order regions — in particular the posterior medial cortex (PMC), angular gyrus, and critically the hippocampus — showed sparse, coarse-grained boundaries corresponding to major narrative context shifts. The hierarchical structure matched the nested event structure that behavioral event segmentation theory (Zacks et al.) predicts. Crucially, the degree of hippocampal activity at major event boundaries predicted the subsequent strength of pattern reinstatement during free recall — the hippocampus marks boundaries, and the more strongly it marks them, the better the episode is subsequently remembered.

## Key findings for ARC-007

ARC-007 specifies that hippocampal trajectory traces are segmented into events at three types of boundaries: action commitment points, sharp changes in prediction error or precision, and contextual/motivational shifts. Baldassano et al. provide direct neural evidence that:

1. The hippocampus is specifically active at **event boundaries** in continuous experience — not during the middle of events, but at the transitions.
2. The hippocampal boundary response operates at **coarse contextual timescales** — not every prediction error or sensory change, but the major structural transitions that reorganize the meaning of the unfolding situation.
3. Hippocampal boundary activity **predicts subsequent episodic retrieval** — the hippocampus is not passively marking boundaries, it is actively encoding the transition point as a segmentation anchor for later recall.

These three properties match ARC-007's specification precisely. In REE, the segmentation at commitment points and contextual shifts is the mechanism by which continuous trajectory experience is carved into episodic units for storage. The Baldassano result confirms this architecture: hippocampus marks boundaries, stores the pattern, and uses the boundary as a retrieval anchor.

## REE translation and MECH-022

For MECH-022 (hippocampal systems as hypothesis injectors), each event boundary in ARC-007's architecture is a hypothesis injection event: at the boundary, the hippocampus transitions from one stored trajectory segment to the next, injecting the incoming trajectory hypothesis into E1/E3 processing. The Baldassano finding that high-level regions (PMC, HPC) mark coarse contextual boundaries while sensory regions mark fine-grained ones is consistent with REE's multi-timescale architecture: E1 is sensitive to fine prediction errors (short timescale), while hippocampal-mediated hypothesis injection operates at coarser contextual timescales (commitment-level transitions).

The link from boundary activity to recall also confirms MECH-022's design principle: the injection event is load-bearing for memory formation, not epiphenomenal. Disrupting hippocampal event boundary encoding should selectively impair episodic retrieval while preserving within-event processing.

## Limitations

The experiment uses passive narrative viewing — watching a TV programme — not active goal-directed behavior with commitment decisions. ARC-007's segmentation is primarily defined at action commitment points; the mapping from narrative event boundaries to action commitment boundaries requires the assumption that commitment points are a functional subset of event boundaries generally. This is principled but untested in REE's specific context. The paper does not identify the mechanism of boundary detection (what drives the HMM state transitions in the hippocampus) — this remains an open question that prediction error accounts (Brunec & Moscovitch) and schema-based accounts are addressing separately.
