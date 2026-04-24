# Foster & Wilson 2006 -- Reverse Replay of Spatial Sequences at Reward in the Awake State

**Claim tested:** ARC-028 (HippocampalModule completion signal -> BetaGate wiring)
**Direction:** supports | **Confidence:** 0.72

## What the paper did

Foster and Wilson used tetrode recordings of hippocampal place cells in rats running a linear track for reward. Their key finding was that during awake rest periods immediately after the rat reached the reward location, place cells replayed the sequence of positions traversed -- but in *reverse* temporal order. The entire recent trajectory was re-represented in compressed form, running backward from reward location to start. This awake reverse replay was distinct from the sleep replay known at the time, and its reversed structure was interpreted as consistent with reinforcement learning models where value is propagated backward from outcome to preceding states.

## Key findings relevant to ARC-028

The most direct implication for ARC-028 is the *triggering condition*: reverse replay fires at the reward location, during the awake state, at the moment the trajectory terminates successfully. This is the biological instantiation of "trajectory completion triggers hippocampal evaluation." The concurrent timing with reward receipt means the replay co-occurs with phasic dopamine signals at the reward site -- establishing the link between completion, dopamine, and hippocampal evaluation that ARC-028's wiring depends on.

The reversed structure has a secondary significance: it is consistent with a credit-assignment mechanism (RL-style TD backup), where the hippocampus propagates the terminal reward signal backward to preceding states. In REE terms, this would correspond to the HippocampalModule evaluating which steps of the trajectory actually contributed to goal arrival -- relevant to how the completion signal is computed, not just transmitted.

## REE translation

ARC-028 requires that trajectory completion (goal arrival) produces a signal from HippocampalModule that, via the subiculum -> NAc -> VP -> VTA pathway (Lisman & Grace 2005), releases dopamine that suppresses BG beta oscillations (BetaGate release). Foster & Wilson 2006 is evidence for the upstream half of this chain: goal arrival triggers coordinated hippocampal activity (reverse replay) that is temporally co-registered with peak dopamine release at reward. The co-occurrence of reverse replay and dopamine at the endpoint is the biological coupling mechanism that ARC-028 instantiates architecturally. In the waking state, this is a prediction-error-driven mechanism: a larger PE at the endpoint (unexpected reward, or reward after long approach) corresponds to a larger dopamine signal and more reliable BetaGate release.

## Limitations and caveats

The paper does not directly measure dopamine concurrent with the reverse replay -- the connection to dopamine is inferred from reward timing and parallel work on phasic dopamine at reward. Foster & Wilson's focus is on place cell sequence structure, not on the gate-release mechanism. The paper also uses a simple linear track; whether the reverse-replay trigger generalises to more complex spatial environments (like CausalGridWorldV2 with obstacles, hazards, and resource fields) is an assumption rather than a demonstrated finding.

The 'reverse' structure of the replay is not directly modeled in REE's HippocampalModule. REE's CEM produces forward-simulated trajectories; there is no backward-replay analogue in the current architecture. This may represent a missing credit-assignment mechanism that could improve goal-path evaluation in V4.

## Confidence reasoning

High source quality (Nature). Moderate mapping fidelity because the paper establishes endpoint-triggered replay rather than directly showing the dopamine-beta gate chain. The inference from "replay at reward" to "dopamine-mediated BetaGate release" is supported but requires joining with other evidence (Lisman & Grace 2005, Brittain et al. 2014). Confidence 0.72.
