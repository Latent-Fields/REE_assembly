# Stokes et al 2013 — Dynamic Coding for Cognitive Control in Prefrontal Cortex

**Source:** Neuron 78(2):364-375, 2013. DOI: [10.1016/j.neuron.2013.01.039](https://doi.org/10.1016/j.neuron.2013.01.039)

## What the paper did

Stokes et al recorded from 627 neurons in lateral PFC (BA 8, 9/46, 45) of two macaques performing a delayed paired-associate recognition task. Each trial opened with an instruction cue specifying which of three choice stimuli would be the target for that trial. The researchers applied time-resolved multivariate pattern analysis — cross-temporal classification, multidimensional scaling, and a velocity metric through neural state space — to track how the population response evolved from cue onset through the delay period and into the choice stimulus epoch. The key manipulation was whether population coding was time-stable (generalising across temporal windows) or time-specific (unique to each processing epoch).

## Key findings

Three results bear directly on MECH-262. First, following the instruction cue, the lateral PFC population underwent rapid state transitions before settling into a **stable low-activity state during the delay period that was differentially tuned to the current rule**. The rule identity (which stimulus would be the target) could be decoded from this quiescent state even as overall firing rates returned to baseline. Second, the stable delay-state code was **orthogonal to both the physical cue representation and any anticipated target representation** — cross-temporal decoding from the cue epoch failed entirely to generalise into the delay period, confirming that delay activity was not passive persistence of the input but a reconfigured network state. Third, when a fixed "neutral" stimulus was presented during the delay, it evoked systematically different population responses depending on the current rule — the **same physical input drove different population trajectories depending on which rule was active**. This is stimulus abstraction in action: the rule, not the stimulus, determines the network state.

## REE translation

These findings provide direct biological grounding for MECH-262 signatures 1 and 2. Signature 1 (stimulus-abstracted format): the neutral-stimulus result is close to a direct demonstration — identical sensory input drives different population trajectories depending on which rule is currently held. Signature 2 (distractor-resistant persistence): the stable low-activity delay state survives subsequent stimulus presentations, exactly the persistence-under-interference that MECH-262 requires. The postcue state in the REE lateral-PFC-analog (SD-033a) should behave analogously: it should represent the current task rule in a format that (a) generalises across the specific stimuli associated with that rule, and (b) persists across distractor/replay events without being overwritten.

The proposed mechanism — short-term synaptic plasticity configuring the network's response properties — is also informative for implementation. MECH-262 signature 3 (training-dependent emergence) is partially addressed: monkeys required at least six training sessions with each stimulus set before performance asymptoted, consistent with slow consolidation writes to the lateral-PFC substrate. The paper does not test across-session learning curves directly, but the task architecture presupposes training-dependent associations.

## Limitations and caveats

The study examines a relatively short delay (400-800 ms inter-stimulus intervals) rather than the multi-episode persistence MECH-262 requires in V3 (across internal_replay events and micro-quiescence cycles). Whether the short-term synaptic plasticity mechanism that stabilises the rule state in the natural setting survives REE's longer timescales is untested. Additionally, Stokes et al did not explicitly test distractor resistance as a probe of rule maintenance — the "distractor" stimuli in this task are choice stimuli for other rules, not independent interference events. The MECH-262 claim that rule representations persist "without being overwritten" by internal_replay events (MECH-261's write-suppression gate) is a more stringent requirement than what this study demonstrates.

## Confidence

0.80. The source is high quality and the mapping to MECH-262 signatures 1 and 2 is direct. Confidence is slightly reduced below 0.85 because the key neurophysiological mechanism (short-term synaptic plasticity as the persistence substrate) is not yet implemented in REE, and because the timescale of tested persistence is shorter than what V3 requires.
