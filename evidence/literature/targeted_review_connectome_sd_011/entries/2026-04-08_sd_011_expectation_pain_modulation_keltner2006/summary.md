# Keltner et al. (2006) — Expectation Modulates Sensory Pain Transmission via a Distinct Affective Network

## What the study did

Keltner and colleagues at UCSF designed an elegantly balanced fMRI experiment to isolate how expectation of pain intensity modulates nociceptive processing. Subjects received thermal stimulation at two intensities (~47C and ~48C) preceded by visual cues conditioned to either intensity. In half the runs, cue-stimulus pairings were matched; in the other half, mismatched. This design allows subtraction of the expectation effect from the raw sensory effect — a cleaner decomposition than most prior work.

## Key findings relevant to SD-011

Two distinct activation patterns emerged:

1. **Sensory-nociceptive pathway**: Comparing high vs. low thermal intensity (with matched high-expectation cues) activated the ipsilateral thalamus, contralateral second somatosensory cortex (S2), and contralateral insular cortex. These are the classical nociceptive relay stations — the lateral spinothalamic pathway.

2. **Expectation-modulatory network**: Isolating the pure expectation effect (high vs. low cue, same stimulus intensity) activated the ipsilateral caudal anterior cingulate cortex (ACC), head of caudate, cerebellum, and contralateral nucleus cuneiformis (nCF). Critically, these regions constitute a distinct network from the sensory relay.

The authors propose convergence at the nucleus cuneiformis — a brainstem site where descending modulatory signals meet ascending nociceptive input. This is the anatomical point where "prediction" meets "sensation."

## Translation to REE

The finding maps onto SD-011's dual-stream architecture with a specific and important nuance. The sensory-nociceptive pathway (thalamus, S2, insula) is what gets modulated by expectation — this is z_harm_s, the stream amenable to forward-model prediction and cancellation. When you know the pain is coming and how much, the sensory transmission is attenuated. A learned forward model E2_harm_s could replicate exactly this function: predict z_harm_s_next from action, and cancel the predicted component.

The expectation-modulatory network (caudal ACC, caudate, nCF) is not the thing being cancelled — it is the thing doing the cancelling. This is closer to z_harm_a territory: the affective-motivational processing that evaluates threat urgency and drives behavioral adjustment. You do not attenuate the warning system itself; you attenuate the sensory signal it acts upon.

## Limitations and caveats

The mapping is principled but indirect. Keltner et al. were not testing dual-stream nociceptive anatomy. The insula appears in both contrasts, which complicates a clean two-pathway story — though this is consistent with the insula's known role as a hub bridging sensory and affective processing (posterior insula more sensory, anterior insula more affective; see Craig 2002, 2009). The caudal ACC activation is an expectation-driven signal, not a sustained homeostatic deviation signal as z_harm_a formally requires. The experiment uses brief thermal stimuli, not sustained threat exposure, so the "accumulation" aspect of z_harm_a is not directly tested.

## Confidence reasoning

The study earns high marks for experimental design and source quality (J Neurosci, Howard Fields' lab — one of the leading pain modulation groups). The mapping fidelity to SD-011 is moderate: it supports the principle that prediction-based cancellation applies differentially to sensory vs. affective processing, but was not designed to test the two-stream claim directly. Transfer risk is low — human fMRI with actual nociceptive stimulation is about as close to the target domain as literature evidence gets.
