# Kilteni, Engeler, Ehrsson (2020): Efference Copy Is Necessary for the Attenuation of Self-Generated Touch

*iScience* 23(2), 100843. DOI: 10.1016/j.isci.2020.100843

## What the paper did

This is the cleanest causal dissociation in the sensory-attenuation literature of whether the *copy of the motor command* (efference copy) or the *prediction of the sensory consequence* is what drives attenuation. Kilteni and colleagues had 40 healthy adults perform a force-discrimination task on the left index finger in three conditions: active (the participant voluntarily pressed a sensor with the right index finger, triggering a test tap on the relaxed left finger), passive (the right finger fell freely onto the sensor under gravity, producing the same tactile contact with no voluntary motor command), and no-movement (externally triggered tap). Point-of-subjective-equality values were extracted from psychometric curves.

## Key findings

Attenuation occurred only in the active condition. The PSE shift between active and no-movement was approximately 0.21 N (~10% attenuation, p < 0.001). The passive condition produced no measurable attenuation (p = 0.799; Bayes factor = 0.20 in favour of the null). The direct active-vs-passive contrast was highly significant (p < 0.001). The temporal predictability of the tactile event was matched across active and passive conditions -- the only thing that differed was the presence of a voluntary motor command. Attenuation cannot therefore be explained by prediction of the sensory consequence alone; a copy of the motor command is required.

## Mapping to SD-029

SD-029 asks whether self-caused harm can be detected by a single-pass comparator of the form `residual = z_harm_s_observed - E2_harm_s(z_harm_s_{t-1}, a_actual)`. The architecture depends on the action token `a_actual` entering the forward model. Kilteni 2020 is the cleanest evidence that in biology, the reference against which observed reafference is compared is built from a copy of the motor command -- not from a separate predictor that only has access to sensory context. If SD-029 instead tried to detect self-caused harm from `z_harm_s_{t-1}` alone without conditioning on `a_actual`, the architecture would be the analogue of Kilteni's passive condition, and by this evidence it should fail.

The Kilteni result also informs C2 calibration. Attenuation in healthy adults is approximately 10%, not binary cancellation. SD-029's C2 criterion specifies "partial attenuation (Shergill partial-attenuation pattern, not a binary gate)" -- the Kilteni magnitude is consistent with that framing. A V3-EXQ-433a-style criterion that demanded full cancellation would be inconsistent with the biological baseline.

## Caveats

The modality gap is the main risk. Kilteni tested tactile force-matching on the finger; SD-029 operates on a nociceptive reafferent stream. The efference-copy logic is argued to be modality-general in the broader literature (descending pain modulation via PAG/RVM has analogous forward-model structure), but Kilteni themselves did not test nociception. For direct nociceptive-transfer evidence one must read Lalouni 2020 Pain and Lalouni 2025 Eur J Pain in this same pull. Kilteni should be read as mechanism evidence for the comparator architecture that SD-029 instantiates, not as nociceptive-stream transfer evidence.

A second caveat: Kilteni's design does not speak to the event-conditioned readout (C3). The attenuation was computed as a mean PSE shift across trials, not conditioned on approach-to-hazard events specifically. C3 will need additional grounding from ERP studies where the peri-event SEP attenuation profile is time-locked.

## Confidence reasoning

Source quality is high: peer-reviewed Cell-press journal, pre-registered OSF protocol, a Bayes-factor-quantified null for the passive-control contrast (which many sensory-attenuation papers omit). Mapping fidelity is moderate -- the comparator architecture maps cleanly, but the modality is tactile, not nociceptive. Transfer risk is moderate for the same reason. Aggregate confidence 0.78: stronger than a correlational study, weaker than a direct nociceptive-stream experiment would be. The paper supports the single-pass architecture of SD-029 but does not by itself discharge the nociceptive mapping risk flagged in the SD-011 design doc.
