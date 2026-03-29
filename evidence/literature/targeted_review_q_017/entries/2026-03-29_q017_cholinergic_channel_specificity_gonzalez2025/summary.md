# Cholinergic modulation enables scalable action selection learning in a computational model of the striatum

**Gonzalez-Redondo, Garrido, Hellgren Kotaleski, Grillner & Ros (2025) — Scientific Reports**
DOI: [10.1038/s41598-025-18776-3](https://doi.org/10.1038/s41598-025-18776-3)
*Based on articles retrieved from PubMed*

## What the paper did

Gonzalez-Redondo and colleagues built a biologically-constrained spiking neural network model of the striatum to address the structural credit assignment problem: how does the striatum reinforce the specific stimulus-action association that produced a reward, rather than strengthening all recently active synapses indiscriminately? The proposed solution was cholinergic gating: acetylcholine released by tonically active interneurons creates phasic pauses that restrict plasticity to brief windows immediately following action execution, ensuring that only the relevant synapses are eligible for modification.

## Key findings

The ACh-gated three-factor learning rule (requiring presynaptic activity, postsynaptic depolarisation, and phasic dopamine, all within a cholinergically-gated window) suppressed cross-channel interference and enabled increasingly competitive performance relative to standard Q-learning as task complexity grew (more distractors, contingency reversals). Distinct roles emerged for the two pathways: D1 (direct pathway) neurons maintained stimulus-specific responses, while D2 (indirect pathway) neurons were recruited to suppress outdated associations during policy updating. The channel specificity result is the most structurally important: without ACh gating, plasticity bled across channels and performance degraded; with it, channels remained orthogonal even in complex environments.

## REE translation

Q-017 asks what the minimal set of orthogonal control axes is and whether it remains minimal under real operating conditions. The cross-channel interference finding from this paper gives one concrete failure mode: without active gating, channels that start orthogonal will become correlated over time as their error signals mix. In REE, the three cortico-striatal loops are designed to carry incommensurable error signals (sensorium, planning, harm -- per MECH-069). If there is no mechanism analogous to ACh gating that keeps these channels informationally isolated, their error signals will gradually couple during learning, collapsing the independence that Q-017 requires. The implication for REE's control-plane architecture is that axis minimality is not a static property -- it requires active maintenance. The minimal orthogonal set is minimal at initialisation, but staying minimal requires a channel-segregation mechanism operating during both learning and online inference.

## Limitations

This is a computational model, not empirical data. The channels in this model are stimulus-action pairs -- fundamentally different from REE's loops which are distinguished by error-signal type and temporal scale. The ACh gating mechanism as implemented here is a plasticity constraint, not a real-time control-plane selector. It is an open question whether a similar gating principle applies to REE's loop-level architecture, where the channels are operating in parallel rather than competing for the same synaptic eligibility trace. The model also assumes a single striatal network; REE's tri-loop architecture involves multiple anatomically distinct striatal regions.

## Confidence reasoning

I rate this 0.65. The channel-orthogonality-requires-active-maintenance insight is genuinely useful for Q-017 and comes from a mechanistically grounded model. The confidence penalty comes from the computational-only nature of the evidence and the inferential gap between plasticity-level channel specificity and representation-level axis independence in REE's control plane.
