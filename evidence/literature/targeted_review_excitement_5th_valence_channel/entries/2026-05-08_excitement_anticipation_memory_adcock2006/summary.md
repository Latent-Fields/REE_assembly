# Reward-motivated learning: mesolimbic activation precedes memory formation (Adcock et al. 2006)

## What the paper did

Adcock, Thangavel, Whitfield-Gabrieli, Knutson, and Gabrieli (Neuron 2006) ran an event-related fMRI study where subjects viewed scenes after MID-style cues signalling either high or low monetary reward for memorising the scene. Subjects were then tested for scene recognition 24 hours later. The contrast of interest was anticipation-period mesolimbic activation (VTA, NAcc, hippocampus) on trials whose subsequent memory differed.

## Key findings relevant to the SD-014 question

The headline finding is that anticipatory NAcc and VTA activation, *before* the to-be-remembered scene appeared, predicted whether that scene would be remembered 24 hours later. High-reward cues that produced high anticipatory mesolimbic activation led to better subsequent memory. Within-subject, hippocampus-VTA functional connectivity at encoding correlated with long-term memory for the subsequent scene. The interpretation: dopamine release in the hippocampus during the anticipatory period — driven by the reward cue — promotes memory formation for whatever follows.

This is the load-bearing finding for the REE-specific reason to register VALENCE_EXCITEMENT. Existing REE channels do not predict subsequent memory consolidation. VALENCE_WANTING is a directional attractor that updates on contact, not on cue. VALENCE_LIKING writes at goal receipt. VALENCE_SURPRISE is a reactive PE record. None of them write at the *anticipatory-positive-cue* moment when, per Adcock 2006, dopaminergic drive of hippocampal memory formation is happening. A VALENCE_EXCITEMENT channel that writes during anticipation would be the natural input to MECH-205's surprise-gated replay write path: locations carrying high excitement at cue would get prioritised replay during subsequent sleep cycles.

## How this maps to REE

This connects directly to EXQ-538's sleep ablation hypothesis. The argument I made in the EXQ-538 design: sleep-dependent schema consolidation is the missing ingredient for SD-049 Phase 2 identity discrimination. Adcock 2006 strengthens that argument by adding a specific mechanism: anticipatory mesolimbic activation at encoding *causally* drives subsequent memory. If REE writes VALENCE_EXCITEMENT during anticipation, sleep replay (via MECH-285 SleepReplaySampler) can use it to prioritise which locations get re-experienced offline. That's a concrete functional payoff for the 5th channel that is not available from any existing channel.

## Limitations and caveats

Healthy adult humans; 24-hour recognition; declarative memory of visual scenes. REE's memory substrate is structurally different (residue field, RBF nodes, ContextMemory slots, hippocampal anchors). The principle translates — anticipatory positive arousal at encoding promotes consolidation — but the specific write site must be designed in REE. The Adcock effect is also graded, not binary, so VALENCE_EXCITEMENT should be a continuous-valued channel like the others, not a flag.

## Confidence reasoning

0.82. Strong source, direct functional consequence of NAcc anticipation, and the specific functional payoff (memory consolidation) is exactly what EXQ-538 is designed to test. This is the most architecturally consequential entry in the pull because it ties VALENCE_EXCITEMENT to a concrete pipeline (sleep replay prioritisation) rather than just describing the construct.

Source: PubMed via PMID 16675403. [DOI](https://doi.org/10.1016/j.neuron.2006.03.036).
