# Seymour (2019): Pain: A Precision Signal for Reinforcement Learning and Control

*Neuron* 101(6), 1029-1041. DOI: 10.1016/j.neuron.2019.01.055

## What the paper did

Seymour (Cambridge Computational and Biological Learning Lab) presented a theoretical review arguing that pain is best understood not as imprecise sensory nociception but as a precision-weighted prediction-error signal that serves two computational functions: (a) a teaching signal for reinforcement learning (driving avoidance behaviour and updating harm expectations), and (b) a near-term control signal for immediate protective responses. He derives this from an active-inference / free-energy framework: the brain maintains a prior expectation of harm; deviations from expected harm constitute prediction errors that are weighted by their precision (reliability). Descending modulation (including PAG/opioid mechanisms) shapes the precision assigned to nociceptive signals, adjusting how much they update behaviour. Key empirical anchors include anticipatory pain modulation, conditioned pain modulation, opioid analgesia, catastrophising, and the role of the pregenual ACC and PAG in descending control.

## Key findings relevant to SD-029

The paper provides the computational-level motivation for treating harm signals as prediction errors, which is precisely what SD-029's residual (z_harm_s_observed - E2_harm_s(z_harm_s_{t-1}, a_actual)) instantiates. At Marr's computational level, Seymour and SD-029 agree: the harm stream encodes prediction error, and that prediction error drives both learning and immediate action selection. The paper also provides a framework for why attenuation of self-generated pain is computationally rational: if the agent predicts a nociceptive consequence from its own action (forward model predicts z_harm_s change), the residual is smaller than for an unexpected external harm, which is exactly SD-029's operating principle.

However, Seymour frames the precision-weighting at the level of behavioural priors (what harm is expected *in this context*, learned over trials), not at the level of per-step motor-efference-copy prediction (what harm does *this specific action* predict). These are distinct timescales: SD-029 is sub-second (per-step forward-model prediction from a_actual); Seymour's framework is over-trial (contextual prior over expected harm level). Both are prediction-error mechanisms but they operate at different granularities.

## Mapping to SD-029 and MECH-256

The paper supports the *computational rationale* for SD-029 without directly evidencing the per-step efference-copy mechanism. MECH-256 proposes that the comparator operates on a per-step basis with a_actual as the conditioning signal; Seymour's framework is agnostic about this -- his precision-signal machinery would work equally with (a) an efference-copy forward model or (b) a context-level prior, and he does not distinguish between them at the implementation level.

The companion De Preter & Heinricher (2024) entry in this corpus (targeted_review_connectome_mech_256) shows that the PAG/RVM implements Seymour's precision-weighting layer (contextual motivational-state gating of nociceptive gain) rather than the MECH-256 efference-copy layer. This means both mechanisms are active in the biological system: the MECH-256 per-step comparator (most likely implemented in spinal cord / somatosensory cortex) and the Seymour/PAG contextual precision-prior layer. They are not competing; they are parallel.

## Caveats

This is a single-author theoretical review, not an empirical study. The mapping from Seymour's computational framework to the specific MECH-256 implementation (per-step forward model on z_harm_s) is by analogy and requires the additional assumption that the short-timescale efference-copy comparator is the mechanism producing the Lalouni 2020 behavioural result. That assumption is supported by Kilteni 2020 (force discrimination efference-copy necessity, in the MECH-256 corpus) but not directly by Seymour.

The keywords on the Seymour paper (active inference, active sensing, free energy, pregenual ACC) locate it firmly in the contextual/descending modulation literature rather than the efference-copy literature. This is not contradictory -- it is simply a different part of the pain modulation system.

## Confidence reasoning

Source quality is high: *Neuron* (impact factor >14), highly cited theoretical review. Mapping fidelity is moderate (55%) because the paper operates at a higher computational level than the specific per-step efference-copy claim in SD-029, and the convergence is at Marr level 2 (algorithm) rather than level 3 (implementation). Transfer risk is low. Aggregate 0.61 -- this paper motivates the computational framing without directly validating the implementation.
