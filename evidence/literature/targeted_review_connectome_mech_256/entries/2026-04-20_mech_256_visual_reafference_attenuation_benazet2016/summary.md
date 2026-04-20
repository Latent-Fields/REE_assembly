# Benazet et al. (2016) -- Visual Reafferent Attenuation in Parietal Cortex

## What the paper did

Benazet and colleagues recorded EEG while participants performed voluntary reaching movements. In one condition the visual feedback of the hand was shown in real time; in another, the same feedback was presented with a 150 ms delay. The delay manipulation breaks the match between the forward model's prediction of what the hand should look like and what is actually seen, without changing the motor command or the stimulus modality.

They found that the N1 component of the visual evoked potential over parietal cortex was significantly smaller when the visual feedback was presented in real time. The interpretation, standard in the forward-model literature, is that when the prediction matches the input, cortical processing is attenuated; when the prediction fails, the attenuation is lost and the response recovers.

## Why this matters for MECH-256

MECH-256 claims that self-attribution on any reafferent latent stream is implemented by a forward-model comparator. The claim is stream-agnostic: the same computational structure should operate on motor-proprioceptive, visual, auditory, somatosensory, and nociceptive reafference, differing only in the forward model's target variable and the substrate instantiating it.

Most of the foundational evidence for the comparator framework comes from the somatosensory and auditory channels (Blakemore 1998 on self-tickling, Shergill 2003 on force matching, the Ford and Mathalon line on auditory N1 attenuation during speech). Benazet et al. extend the same effect to vision during reaching. This matters for MECH-256 because cross-modal universality is the biological argument for the claim's stream-agnostic framing. The more streams show the effect, the less plausible it is that the comparator is a modality-specific accident and the more plausible it is that it is a general computational principle instantiated wherever a reafferent signal needs to be interpreted.

For REE specifically, this is indirect support for committing to per-stream E2_x forward models (ARC-033 for E2_harm_s; SD-030 for E2_self; SD-031 for E2_world). The visual case shows that the forward-model-plus-comparator architecture is realised in parietal cortex for visual reafference, complementing the cerebellar realisation for proprioceptive reafference and the songbird HVC realisation for auditory reafference. Different substrate, same computational structure. That is the pattern MECH-256 predicts.

## Caveats

The paper does not measure agency attribution directly. It measures evoked response amplitude. The inferential chain -- smaller N1 implies smaller residual implies self-attribution -- is standard in the predictive-processing literature but has two steps of theoretical commitment. For the EXQ-433a C2 question (attenuation ratio), this paper does not give a number that maps directly to REE's C2 criterion, because the N1 amplitude is not in the same units as z_harm_s prediction error.

The single 150 ms delay value means the study shows only that attenuation fails when prediction is broken. It does not show the dose-response relationship between prediction quality and attenuation magnitude that would let us constrain the expected ratio more tightly.

Sample size is modest and the effect is at the group-average level. Individual-participant reliability of the effect is not the primary focus. Any quantitative transfer to a computational model should treat the attenuation magnitude reported here as suggestive rather than decisive.

## Confidence reasoning

Confidence 0.7. Source quality 0.7: a solid EEG study in Journal of Neurophysiology, well-designed but with modest sample and a single delay level. Mapping fidelity 0.7: the paper tests forward-model prediction against a sensory stream but measures evoked-response amplitude rather than attribution directly. Transfer risk 0.45: extrapolating from fast visual reafference during reaching to slow nociceptive attribution in a grid-world agent is a multi-step inference.

The paper's contribution to MECH-256 is breadth rather than depth: it adds one more stream to the cross-modal list, strengthening the substrate-agnostic case, without adding precision to the quantitative attenuation prediction. For the quantitative side, Job and Kilteni 2023 (this same lit pull) is the stronger source.
