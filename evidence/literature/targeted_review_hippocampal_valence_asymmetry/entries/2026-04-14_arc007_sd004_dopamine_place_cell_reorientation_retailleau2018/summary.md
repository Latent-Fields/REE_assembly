# Retailleau & Morris 2018 — Spatial Rule Learning and CA1 Place Cell Reorientation Depend on Local Dopamine Release

## What they did

Retailleau and Morris recorded CA1 place cells in rats while they learned a spatial rule (attend to one of two orthogonal cue sets to find reward). After the rats learned the first rule, the experimenters introduced a set-shift (switch which cue set is reward-relevant). Crucially, they infused the D1 receptor antagonist SCH23390 locally into the hippocampus during the set-shift phase.

## Key findings

Successful rule learning was accompanied by place cell reorientation — the cells' spatial firing patterns shifted to represent the reward-relevant dimension. When dopamine D1 receptors were blocked locally, two things happened simultaneously: the place cells did not reorient (they continued representing the old, now-irrelevant dimension), and the rats failed to learn the new rule. They perseverated on the old strategy.

This is a tight causal link: local hippocampal dopamine is required for the cognitive map to reorient toward reward-relevant features, and without that reorientation, goal-directed behaviour fails.

## REE translation

This paper is perhaps the most directly relevant to the architectural question at hand. It shows that dopamine's role in the hippocampal map is not to add a valence label — it's to control which features of the spatial representation are emphasised. The map reorients to represent reward-relevant structure, and this reorientation IS what enables goal-directed navigation.

For ARC-007, this means the hippocampal terrain doesn't have a separate "wanting gradient" layer. Instead, dopaminergic modulation reshapes the terrain itself — making reward-relevant spatial features more prominent in the place cell code. The approach gradient is implicit in the representational structure: reward-associated locations have sharper, more stable, more reward-aligned representations.

For SD-004, the implication is that the action-object backbone of the hippocampal map needs to be dopamine-sensitive. When the reward structure changes (resources respawn elsewhere), dopamine should enable the map to reorient — enhancing representations of the new reward-relevant locations and letting the old ones fade. Without this, the system perseverates.

The perseveration finding is particularly interesting for REE. It suggests that without dopaminergic modulation, the hippocampal map becomes stuck — it cannot update to track changes in the reward landscape. This is analogous to the anhedonia/amotivation seen in low-dopamine states, where the cognitive map fails to reorient toward available rewards.

## Limitations

The task is a set-shifting paradigm, not a free-foraging navigation task. The place cell "reorientation" is a reference frame shift (which cue set defines the spatial code), not a change in approach gradient per se. The mapping to REE's wanting-in-terrain concept requires an inference step: if dopamine reshapes the map to represent reward-relevant features, and navigation follows the map, then the approach gradient is implicit in the map structure. This is plausible but not directly demonstrated in this paper.

## Confidence reasoning

High confidence (0.85) — strong empirical design with causal manipulation (local D1 blockade) and simultaneous electrophysiology. The finding is directly relevant to how reward information enters the hippocampal map. Main caveat is that the task is not navigation per se.
