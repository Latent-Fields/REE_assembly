# Hagewoud et al. 2010 — Sleep Deprivation Shifts Learning Strategy from Hippocampal to Striatal

**Source:** Hagewoud R, Havekes R, Tiba PA, et al. "Coping with sleep deprivation: shifts in regional brain activity and learning strategy." *Sleep* 33(11):1465-73, 2010. DOI: [10.1093/sleep/33.11.1465](https://doi.org/10.1093/sleep/33.11.1465)

**Claims evidenced:** MECH-120

---

## What the paper did

Hagewoud and colleagues used a symmetrical maze that can be solved by either a hippocampus-dependent spatial strategy (using allocentric map-based navigation) or a striatum-dependent response strategy (using egocentric stimulus-response associations). Crucially, the maze is designed so that both strategies produce identical performance during standard training -- the strategies can only be distinguished on probe trials using different start positions. A subset of mice were subjected to 5-hour post-training sleep deprivation each day.

CREB phosphorylation (a marker of memory consolidation activity) was measured in both hippocampus and dorsal striatum at the end of training, providing a molecular readout of which system was engaged.

## Key findings relevant to REE

Sleep-deprived mice performed comparably to controls during training -- they learned the task. But on probe trials using novel start positions, sleep-deprived animals failed, revealing that they had learned a response strategy (same turns from the familiar start position) rather than a spatial map (navigate to the goal location regardless of start). Controls used the spatial strategy. The CREB shift was dramatic: sleep-deprived mice showed training-induced CREB phosphorylation in the dorsal striatum rather than the hippocampus.

The second finding clinches the flexibility interpretation: sleep-deprived mice showed significantly impaired reversal learning the next day. Having locked into the striatal response strategy, they could not adapt when the rewarded location changed. Controls, operating on a hippocampal spatial map, updated more readily.

## Translation to REE

This paper provides the most direct behavioural evidence for the claim that sleep absence produces monostrategy convergence. The mechanism is exactly as MECH-120 predicts: without the SWS synaptic downscaling phase, the Hebbian-strengthened response engrams in the striatum accumulate unchecked during training. The hippocampal spatial strategy -- requiring a more distributed and metabolically expensive map representation -- cannot compete when the striatal habit trace has monopolised the synapse budget. MECH-120's 'attractor flattening' is precisely what preserves access to the flexible map-based alternative.

The reversal deficit is the REE equivalent of an agent that learned one viability-map trajectory and cannot reroute when the path is blocked. In the CausalGridWorld context, this would manifest as persistent navigation toward a previously-rewarded cell that is now hazardous -- the agent's action selection has been captured by the dominant historical trajectory.

What makes this paper particularly important for REE is that the monostrategy convergence occurs in a benign environment (no harm, just reward), ruling out the MECH-124 fear-conditioning pathway. This is the neutral-environment Hebbian lock-in variant -- the second failure mode that the existing claims do not capture -- driven purely by the absence of MECH-120's downscaling.

## Limitations and caveats

The study uses mice, not zebrafish, requiring a species transfer. More importantly, the hippocampus-striatum competition in rodents is between two anatomically and functionally distinct systems. In REE, the analog may be a single-substrate attractor dominance effect within the HippocampalModule/E3 complex -- one trajectory monopolising the viability map rather than two systems competing. The mapping is functional rather than anatomical. The sleep deprivation is also post-training (consolidation window), whereas MECH-120 is about the ongoing online-to-offline phase cycle. Finally, the reversal deficit could reflect active interference from the consolidated striatal trace rather than loss of flexibility per se -- a distinction REE would need to model separately.

## Confidence reasoning

Confidence 0.82 -- strong for the functional claim that absent sleep causes monostrategy convergence. The mechanistic readout (CREB shift) and the reversal paradigm are clean. Docked for the rodent-to-REE two-step transfer and the anatomical translation issue.
