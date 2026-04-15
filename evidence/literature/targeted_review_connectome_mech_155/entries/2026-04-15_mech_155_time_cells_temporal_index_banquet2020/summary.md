# Banquet et al. 2020 -- Time as the Fourth Dimension in the Hippocampus

**Source:** Banquet JP, Gaussier P, Cuperlier N, Hok V, Save E, Poucet B, Quoy M, Wiener SI. *Progress in Neurobiology* 199:101920, 2020. DOI: 10.1016/j.pneurobio.2020.101920

**Claim tested:** MECH-155 (spatial navigation machinery is a specific instance of general associative indexing operating over different latent domains)

---

## What the paper did

Banquet and colleagues synthesised the experimental and computational literature on hippocampal temporal processing, arguing that the hippocampus encodes time as a fourth dimension using the same indexing principles it applies to physical space. The review covers three related phenomena: (1) time cells -- neurons that fire selectively at specific elapsed times during delay periods, tiling the temporal axis as place cells tile spatial paths; (2) online sequence coding -- ordered neuronal assemblies active during sequential experience, with temporal structure carried by theta-phase precession; and (3) offline sequence replay -- during sleep and quiescent states, the same assemblies reactivate in forward and reverse order for consolidation. The authors propose computational models (feedforward and recurrent) that account for the scalar properties of temporal coding and show mechanistic continuity with spatial navigation models.

## Key findings relevant to MECH-155

The central empirical claim is that hippocampal time cells tile elapsed time with the same tiling property that place cells apply to physical extent -- the same substrate, extended to a temporal dimension. Phase precession under theta oscillations encodes the sequence of upcoming states (positions or times) within each theta cycle, providing the common mechanism for both spatial path planning and temporal sequence encoding. Offline replay (during sleep and sharp-wave ripples) reactivates these sequences in both forward and reverse order, showing that the indexed representation is traversable in either direction -- a property required for planning rollout. The review also covers working memory ordering: the hippocampal sequence-encoding mechanism maintains item order in working memory tasks by assigning each item to a temporal index, providing an explicit link from the spatial navigation substrate to the working-memory-ordering sub-claim of MECH-155.

## REE translation

MECH-155 lists working memory ordering as one of the cognitive operations sharing the same associative indexing substrate as spatial navigation. Banquet et al. 2020 is the most direct evidence for this sub-claim available in the rodent single-unit literature. If time cells tile elapsed time using the same phase-precession and theta-sequence machinery as place cells tile spatial paths, then working memory ordering is not a separate cognitive module -- it is the same indexing mechanism applied to a temporal rather than spatial dimension. For the REE E1 architecture, this matters because sequential working memory (holding the order of a planned action sequence, maintaining the order of items in a presented list) would naturally emerge from the same substrate that enables spatial navigation, without requiring a separate implementation. The replay mechanism is also directly relevant: offline replay of temporal sequences is exactly what REE's consolidation-during-sleep architecture (INV-049) requires from the indexed substrate.

## Limitations and caveats

The review synthesises primarily rodent electrophysiology. Human evidence is included (EEG and iEEG correlates of episodic memory and replay) but is less mechanistically resolved. The temporal dimension is a specific extension of the spatial substrate -- the review argues for time as a fourth dimension of space, not for the full generalisation to arbitrary abstract domains (conceptual traversal, planning rollout over non-temporal abstract state spaces) that MECH-155 invokes. The step from spatial+temporal indexing to full abstract-domain indexing remains an inference from the broader literature rather than a finding of this review. The computational models are also somewhat independent from the single-unit experimental data, and the specific mechanisms proposed (plateau potentials, ramping cells in lateral entorhinal cortex) have not been resolved to the level of individual circuit components.

## Confidence reasoning

This review directly addresses the working-memory-ordering and sequential-planning dimensions of MECH-155 and provides the best mechanistic account of how the spatial indexing substrate extends to the temporal domain. Progress in Neurobiology has good standing for mechanistic reviews, and the author list includes established rodent electrophysiology groups. Mapping fidelity is moderate because the temporal extension is only one of the several domain extensions MECH-155 invokes, and the review explicitly frames time as a fourth *spatial* dimension rather than as an example of fully abstract domain generalisation. Confidence 0.68 reflects genuine support for the temporal/sequential-ordering sub-claim, moderated by the gap between temporal generalisation and full abstract generalisation.
