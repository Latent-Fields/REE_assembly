# Perceived Controllability Modulates the Neural Response to Pain

**Salomons TV, Johnstone T, Backonja MM, Davidson RJ (2004). Journal of Neuroscience. DOI: 10.1523/JNEUROSCI.1315-04.2004**

## What the paper did

Salomons et al. used a clever within-subjects fMRI design to ask whether the neural response to pain is determined by the stimulus alone or also by the perceived ability to control it. Sixteen healthy adults received identical thermal pain stimuli under two conditions: one where they believed they could press a button to terminate or reduce the pain, and one where they had no such option. Critically, the stimulus was identical in both conditions -- the controllability was a belief, not a physical reality. This allowed the authors to isolate the neural signature of perceived control completely orthogonal to stimulus intensity.

## Key findings relevant to Q-036

The answer was unambiguous: perceived controllability significantly reduced activation in the anterior cingulate cortex (ACC), insular cortex, and secondary somatosensory cortex (SII) -- the core affective pain circuit -- for identical stimuli. This is the cleanest possible evidence that variables beyond stimulus magnitude modulate affective harm load. Controllability is a cognitive-contextual variable that operates at the level of meaning and agency, not sensation.

Within the ACC, there was functional differentiation: the dorsal ACC integrated both stimulus intensity and controllability context (suggesting it is the locus where raw sensory information is combined with contextual/agency information), while the rostroventral ACC responded specifically to the controllability manipulation. The authors interpret the rostroventral ACC as serving a "modulatory role based on contextual information" -- which translates cleanly into a variable that weights the affective load of a harm signal beyond its sensory magnitude.

## REE translation

Q-036 asks whether temporal integration (MECH-219's hysteretic accumulator) is sufficient to make z_harm_a a genuinely distinct load state, or whether additional variables are needed. This paper answers one part of that question decisively: controllability is a real variable that modulates the affective pain circuit independently of stimulus intensity. In REE terms, the ACC/insula circuit corresponds to the z_harm_a substrate (SD-019/SD-032c area), and the controllability effect means that an agent's representation of whether it can escape or terminate a harm state modulates z_harm_a's effective magnitude. A pure temporal integrator with no controllability term would misrepresent the biological reality.

The interesting implementation question is whether controllability enters z_harm_a directly (as a weight on the accumulator) or indirectly (via a top-down prediction about harm trajectory). The dorsal ACC result (integrating both intensity and controllability) suggests a direct gating role rather than a purely downstream modulation.

## Limitations and caveats

The sample is small (n=16), healthy adults only, and the controllability manipulation is about perceived control rather than actual escape behaviour. No measurement of temporal accumulation or persistence; single-trial stimuli cannot speak to whether controllability effects scale with exposure duration. The finding is about cognitive-contextual modulation of the affective circuit; how this translates to REE's z_harm_a as a latent representation would require explicit inclusion of an agency-belief or escape-prediction signal, which is not yet specified in the substrate design.

## Confidence reasoning

Clean experimental design, direct neural measurement, high mapping fidelity to z_harm_a's substrate. Main penalty is small sample size. Confidence 0.75.
