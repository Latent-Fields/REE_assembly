# Aston-Jones & Cohen 2005 -- An Integrative Theory of Locus Coeruleus-Norepinephrine Function: Adaptive Gain and Optimal Performance

According to PubMed ([DOI](https://doi.org/10.1146/annurev.neuro.28.061604.135709)).

## What the paper does

Aston-Jones and Cohen propose a unifying theory of LC-NE function organised around two distinct modes of LC activity. Phasic LC is the canonical burst response to task-relevant stimuli; in this mode, LC facilitates ensuing behaviours and optimises performance on the current task -- the exploitation regime. Tonic LC is a sustained elevation in baseline firing; in this mode, LC drives disengagement from the current task and a search for alternative behaviours -- the exploration regime. The transition between modes is under cortical control: the anterior cingulate and orbitofrontal cortices, which monitor task-related utility, send direct projections to LC and bias the mode. As task utility declines, ACC/OFC drive LC into the tonic-elevated mode and the system disengages.

## Why it matters for V_s invalidation

This is the most architecturally complete paper in the pull for the trigger-plus-accumulator structure MECH-284 requires. The phasic burst is the single-event broadcast invalidation trigger -- the moment the system registers a violation. The tonic level is the integrated state -- the accumulator output reflecting accumulated utility decline of the currently operative behavioural mode. When tonic LC crosses a threshold, the system disengages: this is the MECH-269 anchor reset operation, mapped onto an LC variable. The cortical inputs from ACC/OFC are the credit-assignment circuits that decide which kind of failure should drive the tonic shift -- which connects this paper to Wilson2014's OFC-as-state-label framing.

The architectural payoff is parsimony. Rather than positing separate substrates for "trigger" and "accumulator", the LC framework gives us a single circuit with two operating regimes that together implement both functions. Phasic events drive the immediate broadcast; tonic level integrates the events into a sustained state that gates behavioural switching. MECH-284 maps cleanly onto this: the accumulator output is the tonic LC level, the trigger events are phasic bursts, and MECH-269 reset is the threshold crossing.

## Refinement of MECH-272 and connection to OFC

The framework also constrains MECH-272 in a useful direction. The waking system is *anchor-dominant when phasic mode dominates* and *probe-dominant when tonic mode dominates*. The transition is graded via the LC tonic level, not threshold-discrete. This refines MECH-272's currently sketchy "anchor-dominant in waking" framing: the more accurate statement is that waking is anchor-dominant under phasic-LC regimes and probe-dominant under tonic-LC regimes, with cortical (ACC/OFC) inputs determining which regime obtains. Sleep then becomes the extreme tonic state in which probe routing dominates -- consistent with our existing MECH-272 framing but giving it a continuous biological underpinning.

The ACC/OFC -> LC projection is also load-bearing. Wilson2014's OFC-as-state-label feeds into LC's gain control. So OFC is not just the local accumulator (in the Wilson framing); it is also the source of the credit-assignment signal that converts violation events into tonic-LC integration. The OFC and LC together form the trigger-accumulator circuit, with OFC as the schema-specific credit-assignment substrate and LC as the broadcast amplification.

## Failure modes

Disrupted phasic-tonic balance produces dissociable cognitive failures. Hyper-tonic LC (chronic anxiety, hypervigilance) is *over-invalidation*: the system is constantly disengaging from current routines in search of alternatives. Hypo-tonic LC (depression, dementia, advanced PD) is *under-invalidation*: stale routines persist because the integrated state never crosses the disengagement threshold. The V3-EXQ-475 phenotype maps to the hypo-tonic pattern: phasic events register (single freeze releases occur) but the tonic integration never accumulates enough to keep the system out of the avoid-anchor.

## Confidence reasoning

Source quality high (Annu Rev Neurosci). Mapping fidelity 0.75 because the phasic-tonic structure maps cleanly to trigger-plus-accumulator. Transfer risk low (0.25). Aggregate 0.76.
