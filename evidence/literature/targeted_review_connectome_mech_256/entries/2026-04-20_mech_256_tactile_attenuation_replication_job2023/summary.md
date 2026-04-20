# Job and Kilteni (2023) -- Action Attenuates Predicted Touch

## What the paper did

Job and Kilteni ran three pre-registered psychophysical experiments to settle a live dispute in the sensory-attenuation literature. The classical account, due to Blakemore and colleagues in the late 1990s, is that self-generated touch is perceived as less intense than physically identical externally-generated touch because the forward model predicts and subtracts the expected sensory consequence. A recent set of papers challenged this account, proposing instead a perceptual-enhancement framework in which action predicts and sharpens touch, and reattributing the apparent attenuation to the double-tactile stimulation inherent in the classical paradigm (both hands touching each other at once).

The Karolinska group designed three experiments to adjudicate the dispute. They manipulated whether the active (voluntarily moving) hand actually contacted the passive hand, and they compared conditions with and without predictive cues. Their preregistered prediction was that attenuation would survive the manipulation while the enhancement account would not.

That is what they found. Across all three experiments, self-generated touch on the passive hand was perceived as less intense than externally-generated touch of identical physical magnitude, and the effect held whether or not the active hand also received simultaneous tactile input. The apparent enhancement effects in the recent literature reduced to an artefact of the reference condition chosen, not a real perceptual gain. The authors conclude that action attenuates predicted touch -- the original forward-model-comparator account is correct.

## Why this matters for MECH-256 and SD-029

MECH-256 asserts that self-attribution on any reafferent latent stream is implemented by a forward-model comparator producing a residual. SD-029 is the V3-active instantiation on z_harm_s with a specific pass criterion (C2): self-caused harm events should show partial attenuation relative to externally-caused harm events of identical physical intensity. V3-EXQ-433a failed this criterion -- attenuation_ratio came out at 0.95 to 1.14, essentially no attenuation, when the Shergill 2003 precedent suggested partial attenuation in the 0.3 to 0.7 range.

The question this lit pull was asked to answer is: can the biological prediction be doubted, or does the V3 failure have to be diagnosed inside the substrate? Job and Kilteni are decisive on this: the prediction is robust. Partial attenuation of self-generated sensory consequences is a stable, pre-registered, replicated finding. It is not an artefact of outdated methodology or of the Blakemore paradigm specifically. Three carefully controlled experiments published in 2023 confirm it. The biological constraint MECH-256 places on SD-029 is well-grounded.

This means V3-EXQ-433a's C2 failure has to be diagnosed in the REE implementation. Candidates, in order of likelihood based on prior V3 lessons:

1. E2_harm_s is not a well-fit forward model on the reafferent harm stream. If forward_r2 on the self-caused condition is low, the comparator has nothing to subtract cleanly. Check forward_r2 per condition before interpreting the attenuation ratio.
2. The externally-caused condition is contaminated by residual self-caused components, or the self-caused condition includes uncontrolled external variance. A clean contrast requires the conditions to differ only in agency, not in other harm-relevant variables.
3. The z_harm_s stream is not actually reafferent in the relevant sense. If z_harm_s has not picked up the sensory signature of the agent's action, then there is nothing for the forward model to predict and nothing to attenuate.

## Caveats

The paradigm is tactile pressure, not nociception. Transferring the effect from somatosensation to the harm stream still requires the assumption that the forward model is modality-general within the broader somatosensory-nociceptive family. This is plausible -- nociception is processed by overlapping circuits and attenuation of self-caused pain is documented clinically -- but not directly shown by this paper.

The measure is perceptual intensity judgment, not explicit agency attribution. MECH-256's residual is supposed to drive attribution, not just attenuation. Job and Kilteni close the attenuation half of the inferential chain robustly; the attribution half rests on other papers (Frith 2000, Haggard 2017 in the sd003_successor_comparator directory).

The effect varies between individuals. A single attenuation ratio as a pass-fail threshold may be miscalibrated to the variance in the underlying biology. REE validation of SD-029 C2 should expect variability and design criteria around distributional rather than point estimates.

## Confidence reasoning

Confidence 0.82. Source quality 0.85: pre-registered, three experiments, eLife, state-of-the-art controls, directly resolves a literature dispute -- one of the strongest entries in the MECH-256 evidence base. Mapping fidelity 0.8: tests the core self-vs-external attenuation prediction more directly than most papers in this space. Transfer risk 0.35: somatosensory-to-nociceptive is the main hazard, moderated by the biological overlap of the two modalities.

This entry gives MECH-256 and SD-029 the clearest modern psychophysical validation. It does not rescue V3-EXQ-433a; it forecloses the easy escape route of blaming the biological prediction and redirects the diagnostic work to the REE substrate.
