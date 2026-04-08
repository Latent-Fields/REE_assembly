# Seymour (2019) — Pain as Precision Signal for Reinforcement Learning and Control

## What the paper does

Seymour's Neuron review recasts pain from an imprecise subjective experience into a precise, objectifiable control signal within a reinforcement learning framework. The central argument: pain's core function is motivational — directing short- and long-term behaviour away from harm — and its apparent variability across cognitive and motivational contexts is not imprecision but sophisticated computational tuning.

This is the most complete computational formalization of pain's dual nature as both a sensory and motivational signal, which is exactly the distinction SD-011 requires.

## Key claims relevant to SD-011

1. **Nociceptive sensing vs. pain**: Seymour draws an explicit distinction between nociceptive sensing (the detection process) and pain (the internal reinforcement signal used for learning). These are computationally separable: sensing provides data, pain provides the teaching signal. This maps directly onto z_harm_s (sensing: immediate, precise, action-contingent) vs. z_harm_a (pain: motivational, urgency-driving, used for behavioural control).

2. **Precision weighting**: Pain is formalized as a precision-weighted prediction error. When predicted, pain's precision is modulated — expected pain is attenuated at the sensory level. This is the forward-model cancellation mechanism: a learned model predicts nociceptive input, and the precision of the residual error is what matters. SD-011 claims exactly this for z_harm_s: E2_harm_s predicts z_harm_s_next from action, and the predicted component is cancelled.

3. **Why prediction cannot cancel the motivational signal**: The RL framework makes clear why the motivational component must remain operative regardless of prediction accuracy. If you could perfectly predict all harm, the sensory surprise would be zero — but the need to avoid the harm remains. The RL signal (the "pain" in Seymour's framework) is not the prediction error itself but the value signal derived from it. This provides the computational rationale for SD-011's asymmetry: z_harm_a (motivational urgency) is not and cannot be forward-model-cancelled.

4. **Distributed network necessity**: Pain requires a distributed brain network precisely because it serves multiple computational functions simultaneously — sensory discrimination, learning, action selection, and long-term policy update. These cannot be collapsed into a single stream without losing information.

## Translation to REE

Seymour provides the computational justification for SD-011's architectural decision. The question is: why separate z_harm into two streams at all? The answer from this framework: because the sensory-discriminative function (precise, fast, forward-predictable) and the motivational-control function (persistent, urgency-driving, not cancellable by prediction) serve different computational purposes that would be degraded by fusion.

In REE terms: z_harm_s feeds E2_harm_s for attribution (SD-003) — it must be precise and action-contingent. z_harm_a feeds E3 for commit gating (ARC-016) — it must be persistent and reflective of accumulated threat state. Fusing them (as the V3 substrate originally did with a single z_harm) forces the system to choose between precision and persistence, which is exactly why EXQ-093/094 showed bridge_r2=0.

## Limitations and caveats

Seymour does not explicitly formalize two anatomically separable streams. His "nociceptive sensing vs. pain" distinction is conceptual, operating at the computational level of Marr's hierarchy rather than the implementational level. The paper does not address the Adelta/C-fiber dual-pathway anatomy that provides SD-011's biological grounding. The mapping from "pain is an RL signal" to "there must be two latent streams in the substrate" requires inference that goes beyond the paper's explicit claims.

The paper also emphasises the integrated, unified nature of pain as a control signal — which could be read as arguing against stream separation rather than for it, if one focuses on the "precise and objectifiable" framing rather than the dual-function rationale.

## Confidence reasoning

High source quality (Neuron, Seymour is among the top computational pain researchers internationally). Mapping fidelity is moderate: the sensing/motivation distinction provides strong conceptual support for SD-011's rationale, but the paper does not formalize two separate streams and could be read either way. Transfer risk is low: this is directly about the computational architecture of pain processing.
