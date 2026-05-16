# Summary: Curiosity-driven Exploration by Self-supervised Prediction (Pathak et al., ICML 2017)

**Entry:** 2026-05-16_mech314c_curiosity_forward_model_pe_pathak2017
**Claims:** MECH-314, MECH-314c, ARC-065
**Direction:** supports | **Confidence:** 0.75

---

## What the paper did

Pathak and colleagues proposed using the prediction error of a forward model -- trained in a learned feature space derived from an inverse dynamics objective -- as an intrinsic reward signal for reinforcement learning. The key architectural insight is that the feature space should filter out environmentally uncontrollable factors: the inverse dynamics model learns to represent only those aspects of the environment that the agent can influence, so that prediction error in that space reflects genuine learning opportunity rather than environmental noise. Agents trained with this intrinsic reward alone (no extrinsic task reward) demonstrated purposeful exploration of VizDoom and Super Mario Bros, succeeding in crossing significant portions of game levels without any hand-designed reward.

## Key findings relevant to the claim

Three findings are directly REE-relevant. First, the forward-model prediction error in a *learned* feature space is a better curiosity signal than raw pixel error, because raw-pixel prediction error is dominated by visual details irrelevant to the agent's causal influence. This motivates the MECH-314c design choice of using a running-variance proxy (which tracks model uncertainty broadly) rather than raw observation prediction error. Second, an agent trained purely on curiosity intrinsic reward acquires competent navigation skills as a side effect of wanting to see new states -- the exploration drive produces world-model skill as a downstream consequence, not as a separate training objective. Third, and critically, the approach fails in stochastic environments: when part of the environment is irreducibly random (the paper mentions environments where the agent can access random stimuli), prediction error remains perpetually high in those regions, creating an attractor that captures the agent's attention without yielding any useful learning.

## REE translation

For MECH-314c, this paper establishes the computational tradition that REE's learning-progress sub-flavour joins. The REE Phase-1 implementation uses EMA of |PE_t - PE_{t-K}| (derived from e3._running_variance) as the broadcast scalar. Pathak 2017 is the direct anchor: the agent should prefer to be in states where its forward model is improving. The Phase-1 approximation (broadcast scalar vs. per-candidate learned prediction error) is an acknowledged simplification -- Phase 2 would require a forward-variance head on the E1 LSTM to produce per-candidate prediction-improvement estimates.

The stochastic environment failure is the most actionable finding for the user's central question: if REE's infant-stage environment contains any irreducibly random elements (stochastic reward delivery, random goal placement, random obstacle appearance), the MECH-314c signal will fixate on those random attractors rather than driving exploration toward learnable structure. This is a reason not just to turn up novelty_bonus_weight but to audit the environment for stochastic attractors.

## Limitations and caveats

The REE Phase-1 implementation does not include an inverse dynamics model to filter out environmentally uncontrollable factors. This means REE's curiosity signal is potentially noisier than Pathak's. The learned-feature-space requirement is partially met by REE's z_world representation, but z_world is not specifically trained to filter environmentally uncontrollable dimensions. The paper tests only two environments; large-scale cross-environment evaluation (which Burda 2018 provides) reveals the failure mode more systematically.

## Confidence reasoning

Source quality is high (ICML 2017, foundational in the field). Mapping fidelity is moderate because the Phase-1 approximation departs meaningfully from the architecture this paper tests. The core functional insight (learning-progress as curiosity, stochastic-attractor failure) transfers well; the specific implementation details do not map directly onto REE Phase 1.
