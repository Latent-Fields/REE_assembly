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

## MECH-142 translation (added 2026-08-10)

MECH-142 states: "Valence-arousal axis orthogonality in the control plane is not a static geometric property but requires active cholinergic maintenance during learning; without it, axes drift toward correlation under repeated co-activation." That claim's `notes` field named this paper as its "critical addition" beyond the static-orthogonality evidence (Bush 2018, Baucom 2011 -- see the sibling entries in this same directory), but no `record.json` had ever actually been tagged to MECH-142 -- the claim existed with `evidence: []` for four and a half months despite its own notes citing a specific paper.

Re-reading the paper's own ablation with MECH-142's wording in hand, the match is closer than the original Q-017 framing captured. The paper's contrast condition is literally: global (non-gated) modulation causes "weight increases not only for the current stimulus, but also for any stimulus previously associated with the same action" -- i.e., channels that co-activate (fire together during the same rewarded action) drift toward shared, correlated weights when the gating signal is absent. That is a spiking-network instance of "axes drift toward correlation under repeated co-activation," and the gating signal that prevents it is, again literally, cholinergic. This is a tighter fit to MECH-142's own sentence than to Q-017's minimal-axis-count question, which is why `confidence` for this entry was raised from 0.65 to 0.72 and `claim_ids_tested` now includes MECH-142 alongside Q-017.

The gap that remains, and that keeps this from being a slam-dunk rather than a solid supporting result: the paper's "channels" are striatal action-selection channels (stimulus-action pairs), not REE's specific valence and arousal representations, and the species/domain transfer from striatal reinforcement learning to an artificial control plane's affective axes is inferred, not demonstrated. The mechanism-level principle (co-activation without a gating signal -> drift toward correlation; a gating signal -> preserved separation) is what MECH-142 borrows; the paper does not itself contain a valence/arousal manipulation.

## Limitations

This is a computational model, not empirical data. The channels in this model are stimulus-action pairs -- fundamentally different from REE's loops which are distinguished by error-signal type and temporal scale, and different again from MECH-142's specific valence/arousal axes. The ACh gating mechanism as implemented here is a plasticity constraint, not a real-time control-plane selector. It is an open question whether a similar gating principle applies to REE's loop-level architecture, where the channels are operating in parallel rather than competing for the same synaptic eligibility trace. The model also assumes a single striatal network; REE's tri-loop architecture involves multiple anatomically distinct striatal regions.

## Confidence reasoning

I rate this 0.72 (raised from the original 0.65, which was calibrated for Q-017 alone). The channel-orthogonality-requires-active-maintenance insight is genuinely useful for Q-017 and comes from a mechanistically grounded model; for MECH-142, the paper's own gated-vs-global ablation is structurally the same experiment MECH-142's hypothesis predicts the outcome of, which raises mapping_fidelity for that claim specifically. The confidence penalty that remains comes from the computational-only nature of the evidence and the domain transfer from striatal action-channel plasticity to REE's affective valence/arousal axes, which is inferred rather than directly tested.
