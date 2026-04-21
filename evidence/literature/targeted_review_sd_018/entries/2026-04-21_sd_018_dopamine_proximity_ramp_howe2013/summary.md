# Howe et al. 2013 -- Dopamine Ramp Signals Reward Proximity in Striatum

**Claim tested:** SD-018 (encoder.resource_proximity_supervision)
**Direction:** supports | **Confidence:** 0.78

## What the paper did

Howe, Tierney, Sandberg, Phillips and Graybiel used fast-scan cyclic voltammetry (FSCV) to measure dopamine release in the dorsal striatum and NAc as rats navigated mazes toward distant food rewards. Their central finding was that dopamine signals did not follow the standard phasic prediction-error profile (a brief spike at cue onset). Instead, dopamine gradually ramped upward as the rat moved toward the distant reward, with the ramp scaling flexibly with both the distance to the reward and the reward magnitude. These ramp signals emerged through learning and showed spatial preferences for goal locations, readily updating when reward values changed.

## Key findings relevant to SD-018

The finding is striking precisely because of what the rat's sensory environment does not do during the approach phase: **nothing changes**. The sensory scene in a maze corridor is static until the rat reaches the reward zone. A world-model system trained on sensory prediction error would therefore receive no gradient signal about reward proximity during the approach -- the sensory inputs are invariant to how far the rat still needs to travel. Yet dopamine ramps anyway, signaling proximity. This demonstrates that reward proximity encoding is a computationally separate process from sensory prediction, requiring a dedicated circuit (the mesolimbic dopamine system) that reads from motivational state and goal distance rather than from sensory prediction error.

## REE translation

SD-018 claims that z_world trained on E1 world-model prediction loss cannot encode resource proximity because the sensory scene in CausalGridWorldV2 is invariant to resource proximity until contact. The resource does not change the visual field or hazard pattern until the agent actually reaches it. Howe et al. 2013 documents the exact biological analog of this problem: the sensory scene is invariant during maze approach, yet the brain still encodes proximity via a dedicated dopaminergic ramp. In REE, the architectural solution is an auxiliary resource_proximity_head (Sigmoid regression on z_world predicting max(resource_field_view)), which provides the explicit gradient signal that sensory prediction alone cannot provide -- the structural analog of having a dedicated mesolimbic proximity circuit.

## Limitations and caveats

The biological ramp is encoded by dopamine release in striatum -- a fully separate projection system from sensory cortex. In SD-018, the implementation is an auxiliary head on z_world (a shared representation), not a separate latent. This means the REE solution is architecturally weaker than the biological precedent: the proximity signal in biology has a dedicated circuit that cannot be contaminated by sensory prediction, whereas in REE the resource_proximity_head adds gradient pressure to z_world that competes with E1 world-model gradients. A more faithful implementation might eventually require a separate z_benefit latent (analogous to how SD-011 split z_harm from z_world). SD-018 should be understood as a necessary but possibly not sufficient step toward full biological fidelity.

Additionally, subsequent work (Costa et al. 2025, included in this review set) shows ongoing debate about whether dopamine ramps reflect VTA neuron firing per se or local circuit mechanisms. This debate does not undermine the main finding (proximity is distinctly encoded in NAc dopamine) but does add uncertainty about the mechanistic chain from goal distance to dopamine signal.

## Confidence reasoning

Nature paper with strong, well-replicated behavioral phenomenon. The core finding -- that reward proximity is distinctly encoded in striatal dopamine in a way that cannot be derived from moment-to-moment sensory prediction -- maps tightly onto SD-018's motivation. Confidence 0.78 reflects high source quality and good mapping fidelity, with a moderate transfer risk for the shared-vs-separate representation caveat.
