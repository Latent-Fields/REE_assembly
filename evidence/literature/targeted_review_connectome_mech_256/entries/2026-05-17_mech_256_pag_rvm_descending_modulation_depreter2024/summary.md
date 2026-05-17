# De Preter & Heinricher (2024): The 'In's and Out's' of Descending Pain Modulation from the Rostral Ventromedial Medulla

*Trends in Neurosciences* 47(6), 447-460. DOI: 10.1016/j.tins.2024.04.006

## What the paper did

De Preter and Heinricher (Heinricher lab, Oregon Health & Science University) reviewed current understanding of how the rostral ventromedial medulla (RVM) -- the key output node of the descending pain-modulatory circuit -- integrates top-down and bottom-up inputs to regulate pain. The RVM receives inputs from the periaqueductal gray (PAG), which itself receives cortical signals (ACC, prefrontal, insular) encoding motivational and emotional state, as well as ascending nociceptive signals from the spinal cord. The two functionally defined RVM cell classes (ON-cells and OFF-cells) drive opposing effects: OFF-cells inhibit spinal pain transmission (their pausing at the moment of nocifensive reflex is antinociceptive); ON-cells facilitate transmission (their burst is pronociceptive). The review summarises input and output circuits for each cell type and discusses ongoing challenges in aligning functional definitions with emerging molecular/genetic cell-type identification.

## Key findings relevant to MECH-256 and SD-029

The critical finding for the nociceptive comparator question is architectural: the RVM's modulatory action is governed by *behavioural state*, not by *motor command prediction*. ON/OFF cell firing is determined by: opioid tone (mu-opioid agonists silencing ON-cells, activating OFF-cells), PAG-mediated motivational signals (stress-induced analgesia, conditioned pain modulation, expectation of harm), and ascending spinal nociceptive input. There is no evidence in this review -- or in the broader RVM literature it synthesises -- of a mechanism by which the RVM receives efference copy of motor commands and subtracts a predicted z_harm_s signal from incoming nociceptive afference. The descending control is gain control based on context, not forward-model subtraction based on a_actual.

This matters because the REE plan for GAP-4 posited that "PAG/RVM descending modulation shares the efference-copy structure." On the evidence synthesised here, that posit is not supported at the mechanistic level. The PAG/RVM implements a different but related computational operation: it modulates the *expected precision* of nociceptive signals based on motivational state (Seymour's precision-signal framing, see companion entry seymour2019 in targeted_review_sd_029). This is contextual precision-gating, not efference-copy cancellation.

## Mapping to MECH-256 and SD-029

The mapping is a clarification, not a falsification. MECH-256 claims that for any reafferent latent stream z_x with a forward model E2_x, the residual (z_x_observed - E2_x(z_x_{t-1}, a_actual)) is the agency signal. The Lalouni 2020 paper (already in the SD-029 corpus) provides behavioural evidence that self-generated pain IS attenuated ~40% relative to external pain, which is exactly what a functioning nociceptive comparator would produce. This paper adds the constraint that the PAG/RVM is NOT the anatomical substrate for that attenuation -- the behavioural result requires a different substrate, most likely: (a) corticospinal collaterals to dorsal horn interneurons providing corollary discharge at the spinal gate (the anatomical site where efference copy could gate nociceptive afference before it ascends), or (b) somatosensory cortex (S1/insula) forward-model subtraction at the cortical level.

In REE terms: E2_harm_s's comparator operation is anatomically located at the spinal cord / somatosensory cortex level. The PAG/RVM contributes a parallel layer of contextual precision-gating (which in REE would map to an expected-precision adjustment on z_harm_s's reliability, independent of the per-step efference-copy residual). Both mechanisms are active; they are not redundant.

## Caveats

The paper does not directly test whether corticospinal efference copy reaches spinal dorsal horn interneurons and gates nociception at that level -- that would require a different experimental paradigm (e.g. comparing pain thresholds with intact vs lesioned corticospinal tract). The absence of evidence for efference copy in the RVM is not evidence of its absence in the pain system generally; it is simply evidence that PAG/RVM is not where it happens.

Additionally, the molecular mismatch problem -- where functional ON/OFF cell classification does not cleanly align with molecular markers -- means the circuit is more complex than the canonical model. This complexity could in principle conceal a smaller efference-copy subpopulation within the RVM, but there is currently no evidence for this.

## Confidence reasoning

Source quality is high: *Trends in Neurosciences* with the Heinricher lab, which has defined the ON/OFF cell framework. Mapping fidelity is moderate (65%) because the paper does not directly test the efference-copy hypothesis -- it characterises the circuit as it is understood without that framing, leaving the negative inference as mine. Transfer risk is low given human imaging corroboration. Aggregate 0.74.
