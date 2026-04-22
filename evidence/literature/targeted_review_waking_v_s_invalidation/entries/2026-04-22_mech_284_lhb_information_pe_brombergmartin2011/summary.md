# Bromberg-Martin & Hikosaka 2011 -- Lateral Habenula Neurons Signal Errors in the Prediction of Reward Information

According to PubMed ([DOI](https://doi.org/10.1038/nn.2902)).

## What the paper does

Bromberg-Martin and Hikosaka asked whether the lateral habenula encodes only reward prediction errors -- the canonical Matsumoto2007 result -- or whether some LHb neurons also encode prediction errors about *information itself*. They recorded LHb units while macaques chose between cues that varied in how informative they were about upcoming reward, independent of the reward magnitude. A subpopulation of neurons responded selectively when reward information was unexpectedly cued, delivered, or denied -- the same shape as the value-PE response, but tracking information rather than value. Strikingly, these signals evaluated information sources more reliably than the monkey's actual choices did.

## Why it matters for V_s invalidation

This is the most architecturally on-target paper in the LHb literature for our purposes. The conceptual leap from "predicted reward did not arrive" (Matsumoto2007) to "predicted information did not arrive" (this paper) is exactly the leap V_s asks the brain to make. V_s is not a value signal; it is a regional schema-fit signal that asks, of the currently anchored model, whether the world is still providing the kind of structure that model assumes. An information-PE substrate -- a circuit that fires when the world fails to provide the information the agent expected this region to provide -- has the right computational shape for that.

The mapping has a real boundary. Bromberg-Martin used cues that predicted *reward information*, so the underlying PE is still tied to a reward outcome at the end of the trial. V_s is concerned with hippocampal-anchor information about regional dynamics, where the "outcome" is whether the predicted dynamics unfolded, not whether reward arrived. Whether the same LHb information-PE subpopulation also fires to anchor-mismatch in a no-reward navigation task is unknown to me. A V3 experiment that varied schema match independent of reward could test this directly.

## Architectural readings beyond MECH-284

This paper also gives MECH-272 (state-gated routing -- waking is anchor-dominant, sleep is probe-dominant) a possible refinement. If LHb information-PE is the signal that says "this anchor is no longer providing useful information", then MECH-272 should be re-stated: waking is anchor-dominant *until information-PE crosses threshold*, after which the system switches transiently into a probe-dominant re-anchoring window. That is a stronger architectural claim than the original MECH-272 and one a V3 experiment could test directly.

## Clinical resonance

If LHb has separable reward-PE and information-PE subpopulations, then the clinical failure modes might dissociate. Depression's blunted reward-PE could leave information-PE intact (people with depression still notice when their model of the world has failed, even when they cannot mobilise toward goals). OCD's perseveration could be the inverse: reward-PE intact, information-PE blunted, so the agent never registers that the compulsive routine has stopped being informative about safety. This is speculative but it is the kind of dissociation an information-PE substrate would predict.

## Confidence reasoning

Source quality very high. Mapping fidelity 0.72 -- the construct is closer to V_s than Matsumoto2007 but still tied to reward outcomes. Transfer risk 0.30. Aggregate 0.74. This paper does more architectural work for V_s than any other in the LHb cluster.
