# Summary: Stachenfeld, Botvinick & Gershman (2017) — "The hippocampus as a predictive map"

**Entry ID:** 2026-03-29_mech_033_predictive_map_stachenfeld2017
**Claim tested:** MECH-033 (E2 forward-prediction kernels seed hippocampal rollouts)
**Evidence direction:** supports | **Confidence:** 0.72

---

## What the paper did

Stachenfeld, Botvinick and Gershman proposed a formal computational account of hippocampal place cells grounded in reinforcement learning theory. Their central argument is that place cells do not represent current position but rather encode a *successor representation* (SR): a discounted sum of future expected state occupancies under the agent's current policy. Mathematically, the SR M(s, s') gives the expected discounted future time spent in state s' given that the agent is currently in state s. The authors fit this model to rodent place-field data, showing that the SR framework predicts observed asymmetries in place-field geometry, the broadening of fields near goal locations, and the formation of "splitter" cells at decision points. They further proposed that the hippocampus computes the SR while the striatum stores the reward vector, together implementing model-free value estimation that nonetheless benefits from a rich predictive geometry.

## Key findings

The core empirical observation is that hippocampal place fields systematically skew in the direction of travel and expand near reward locations -- exactly as the SR predicts. A uniform spatial representation (pure position coding) would not produce these asymmetries. The SR representation also explains remapping phenomena: when reward locations change, place fields shift in ways that are consistent with updating the forward-predictive map rather than the raw position map. Decision-point neurons in the rodent hippocampus, which fire differently depending on the upcoming choice rather than the current position, emerge naturally from the SR because the prediction of future states must branch at choice points.

## REE translation

If hippocampal representations *are* successor representations, then the hippocampal map already encodes multi-step forward predictions. This is the representational substrate that MECH-033 requires: the hippocampal rollout does not start from scratch at each decision point -- it starts from a geometry that has been shaped by anticipated future transitions. In REE terms, E2 is the fast forward transition model f(z_t, a_t) -> z_{t+1}. The SR can be expressed as an iterated application of the transition matrix. E2's one-step kernel outputs are precisely the building blocks from which the SR geometry is assembled. If E2 provides the transition kernel, and the hippocampus stores SR-structured predictions derived from applying that kernel repeatedly, then E2 is -- in a very natural sense -- seeding the hippocampal rollout structure.

The paper offers a mechanistic bridge that MECH-033 needs: it is not that E2 fires a one-time initialization signal into the hippocampus at the moment of planning, but rather that the hippocampal map's geometry is continuously shaped by E2-type predictions integrated over prior experience. The forward sweep at a decision point is then a read-out of an already-structured predictive map, not a computation performed de novo.

## Limitations and caveats

The paper is a computational model, not a direct mechanistic demonstration. It shows that hippocampal place fields are *consistent with* SR encoding; it does not show that a cerebellar-analogue fast predictor (E2) is the computational mechanism that builds or initializes that encoding. The SR framework is also policy-dependent: the map encodes predictions under the agent's *current* policy. REE's claim is about E2 seeding rollouts that are used for policy *evaluation*, which is a different computational context -- the hippocampus would need to query the E2 kernel under counterfactual actions, not just the current policy. This is a non-trivial extension that the paper does not address.

The rodent-to-architecture transfer also deserves scrutiny. The rodent experiments use open-field foraging with stable reward locations, a setting very different from the multi-step goal-directed planning with harm-avoidance that MECH-033 operates in. Whether the SR structure survives in abstract conceptual spaces (z_world in REE) rather than Euclidean spatial environments remains an open empirical question.

## Confidence reasoning

The source quality is high: Nature Neuroscience publication with a rigorous formal treatment and multiple empirical convergences. The mapping fidelity is moderate: the SR framework is the closest neuroscience analog to E2-seeded hippocampal rollouts, but the gap between "hippocampus encodes SR-structured predictions" and "E2 kernels initialize hippocampal trajectory rollouts" is real and non-trivial. The paper supports the plausibility of MECH-033 but does not test the seeding mechanism directly. Overall confidence 0.72 reflects a strong theoretical ally with significant translation distance.
