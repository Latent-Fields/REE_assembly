# Craig 2009 — Anterior Insula as Interoceptive Hub (SD-032c)

**Source:** Craig ADB. "How do you feel -- now? The anterior insula and human awareness." *Nature Reviews Neuroscience* 10(1):59–70. DOI: 10.1038/nrn2555

## What the paper did

Craig synthesises a broad literature across functional imaging, lesion studies, microstimulation, and single-unit recordings to argue that the anterior insular cortex (AIC) is the primary cortical site of interoceptive re-representation: it receives lamina-I spinal and brainstem afferents coding the physiological state of the body (pain, temperature, itch, cardiac activity, pulmonary stretch, gastrointestinal tone, etc.) and integrates these into a unified subjective feeling of the body's current condition. A particular anatomical claim is that von Economo neurons (VENs) in layer 5 of the AIC provide fast projection capacity to anterior cingulate and other targets, enabling rapid broadcast of interoceptive salience signals.

## Key findings relevant to SD-032c

Craig establishes three properties that directly ground SD-032c. First, the AIC integrates harm-valenced afferents (pain, visceral discomfort) with homeostatic drive signals (hunger, thirst, fatigue) into a unified interoceptive representation — this is precisely the input specification of SD-032c's AICAnalog: z_harm_a + drive_level → aic_salience. Second, the AIC has efferent projections to ACC and motor cortex, enabling salience signals to trigger behavioural mode changes — the biological substrate for SD-032c's switch trigger to SalienceCoordinator (SD-032a). Third, Craig proposes that AIC activity scales with the subjective *urgency* of a body state: extreme or changing interoceptive conditions produce strong AIC responses, while stable states produce weaker ones — supporting the threshold-gated architecture of SD-032c.

## Translation to SD-032c

SD-032c's AICAnalog module receives z_harm_a and drive_level, computes a salience, and fires a network-switch trigger when salience exceeds a threshold. Craig's paper provides the canonical biological grounding for each of these elements: AIC receives both harm signals (pain pathways) and homeostatic drive signals (via hypothalamo-insular connections), computes an integrated interoceptive signal, and projects it to ACC and frontal regions for behavioural control. The drive_level dependence in SD-032c — the key testable claim that the same z_harm_a triggers different behaviour depending on metabolic state — is consistent with Craig's framing of interoceptive re-representation as inherently context-sensitive (a moderate pain signal feels more urgent when combined with hunger and fatigue).

## Limitations and caveats

Craig's paper focuses on phenomenological awareness and subjective feeling rather than on the urgency-interrupt / network-switch function. The mode-switching circuitry requires Menon & Uddin 2010 for its network-level articulation. Craig also does not directly characterise drive-level modulation of harm-salience (the key SD-032c testable specification) — that dependence is asserted as plausible from the integration story but is not experimentally demonstrated in this review. Mapping fidelity to the SD-032c *interrupt* architecture (threshold-gated, event-driven) versus a continuous interoceptive representation (Craig's model) is the main gap.

## Confidence

0.73. Canonical, high-citation Nat Rev Neurosci review establishing the interoceptive hub role of AIC. Core biological grounding for SD-032c's input specification. Mapping fidelity moderate because Craig's emphasis is on awareness rather than urgency interrupt; drive-level modulation is implicit rather than demonstrated.
