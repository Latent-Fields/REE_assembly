# Hosaka et al. 2016 -- Beta Suppression and Action Sequence Updating in Primate SMA

## What the paper did

Hosaka and colleagues recorded local field potentials from the supplementary motor area (SMA) and pre-supplementary motor area (pre-SMA) of two Japanese macaques performing a bimanual sequential motor task. The task required two-element movement sequences that changed across blocks. Within each block, the first three trials were visually guided (cues present) and the next three were memory-guided (cues absent). The key comparison was between "updating" trials (first trial of a new block, when the animal must learn a new sequence) and "maintenance" trials (subsequent trials, when the animal executes an already-known sequence). Time-frequency analysis decomposed the LFP signal into beta (10-40 Hz) and high-gamma (40-200 Hz) bands using wavelet transformation.

## Key findings

The central finding is a clean dissociation between beta and high-gamma during updating versus maintenance. During updating trials, beta power was phasically suppressed from cue onset while high-gamma power increased reciprocally. During maintenance trials, beta power remained tonically elevated through the early delay period, and high-gamma did not show the same increase. The authors interpret beta suppression as creating a "volatile" neural state that permits the reorganization of cell assemblies encoding the action sequence -- a necessary precondition for learning the new plan.

The most striking finding is the error analysis: when beta suppression occurred inappropriately during maintenance trials -- when the existing plan should have been preserved -- the animals made erroneous sequence selections. This demonstrates that premature volatility (beta suppression) destabilizes existing representations, and that elevated beta is functionally necessary to protect stable motor plans from disruption.

## REE translation

This paper is the most challenging of the three for MECH-090, and it warrants careful parsing. MECH-090 claims that beta oscillations gate E3-to-action-selection propagation but NOT E3 internal updating. The claim's architecture is that during a committed action sequence, beta is elevated, E3 continues its internal heartbeat (model updating, trajectory evaluation), but E3's updated state does not propagate to the action selector until beta drops.

Hosaka et al. show something importantly different: in the SMA, elevated beta does not merely prevent output propagation -- it prevents internal plan revision. The cell assemblies encoding the action sequence are actively protected by beta from reorganization. Beta suppression is required for the internal cognitive operation of learning a new sequence, not just for executing it. The error data make this especially pointed: inappropriate beta suppression during maintenance causes the internal representation itself to become unstable, leading to wrong actions. If the internal plan were independently maintained (as MECH-090 implies for E3), then beta dynamics should not affect the quality of the internal representation -- only its propagation to output.

However, one must be cautious about the circuit locus. MECH-090 locates its gating mechanism in the STN and striatum -- basal ganglia structures. Hosaka et al. record from the SMA, a cortical motor planning region. It is entirely possible that beta serves different functions at different levels of the motor hierarchy: BG beta may gate output propagation (as MECH-090 claims), while cortical beta in the SMA gates internal plan stability. The two are not necessarily the same mechanism. Moreover, the "updating" that Hosaka et al. measure is block-level learning of a new sequence -- a wholesale replacement of the action plan. MECH-090's "internal updating" refers to ongoing model refinement within a committed sequence (E3's heartbeat). These may be different kinds of updating with different beta sensitivities.

## Limitations

The primate SMA data cannot be directly equated with human BG beta dynamics. The sample is small (two macaques). The task structure (block-level sequence changes) does not match the within-sequence updating that MECH-090 describes. The beta band used (10-40 Hz) is broader than the typical 13-30 Hz range for beta, which may include alpha-band dynamics in the lower range.

## Confidence reasoning

Confidence is set at 0.75 with a mixed evidence direction. The paper provides the strongest available evidence that beta can gate internal plan stability, not just motor output -- a direct challenge to MECH-090's specificity claim. But the challenge is bounded by the cortical (not BG) recording site and the block-level (not within-sequence) updating being measured. The finding that elevated beta protects internal representations is important for refining MECH-090: the claim may need to distinguish between types of internal updating (ongoing model refinement vs. wholesale plan replacement) and between circuit levels (BG output gating vs. cortical representation stability). Source quality is high; mapping fidelity is moderate due to the locus and timescale differences; transfer risk is moderate.
