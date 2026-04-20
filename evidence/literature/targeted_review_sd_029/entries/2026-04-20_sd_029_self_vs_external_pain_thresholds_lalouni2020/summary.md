# Lalouni et al. (2021): Predicting pain: differential pain thresholds during self-induced, externally induced, and imagined self-induced pressure pain

*Pain* 162(5), 1539-1544. DOI: 10.1097/j.pain.0000000000002151

## What the paper did

Lalouni and colleagues (including Kilteni and Ehrsson from the sensory-attenuation lab) tested whether the efference-copy / forward-model mechanism that attenuates self-generated tactile input also operates on nociceptive input. Forty healthy adults received pressure-pain stimulation at the quadriceps via algometer (50 kPa/s ramp) in three within-subject conditions: self-induced (participant squeezed the device against their own thigh), externally induced (experimenter applied identical stimulus), and imagined self-induced (experimenter applied while participant imagined they were applying it themselves). Pressure-pain thresholds were the primary outcome.

## Key findings

Pain thresholds differed significantly across all three conditions. Mean thresholds were 729.6 kPa (self-induced) versus 521.5 kPa (externally induced) -- a 40% attenuation of nociceptive sensitivity when the subject was the causal agent. The imagery condition sat in between at 618.9 kPa. All pairwise contrasts reached significance (self vs other p < 0.001; imagery vs other p < 0.001; self vs imagery p = 0.004). The effect was robust to trial order.

This is the first clean within-subject demonstration that the efference-copy mechanism previously established for tactile reafference (Blakemore 1998, Shergill 2003, Kilteni 2020) also gates nociceptive reafference. The imagery result further suggests that even an internally generated motor prediction -- without actual movement -- is sufficient to engage some of the attenuation machinery, though less fully than an actual motor command.

## Mapping to SD-029

This is the direct nociceptive-transfer evidence the SD-011 design document explicitly flagged as the open mapping risk. The SD-029 functional restatement notes that "the canonical comparator literature evidences the mechanism on sensorimotor / tactile / force streams. Extension to nociceptive streams is plausible but not directly demonstrated in the four canonical papers." Lalouni 2020 closes that gap. The comparator architecture that SD-029 instantiates is not speculative when applied to z_harm_s; the biological system demonstrably uses efference-copy-driven forward prediction to attenuate reafferent nociception.

The magnitude matters for C2 calibration. The 40% threshold shift in healthy adults is a graded attenuation, not a binary gate. This is the Shergill-partial-attenuation pattern that SD-029 C2 specifies explicitly, and is the reason V3-EXQ-433a's failure to find attenuation should not be read as falsification of SD-029 -- a biologically correct attenuation would be partial, not near-total. If the V3 experiment was implicitly assuming near-complete cancellation, the criterion itself needs recalibrating before interpretation.

## Caveats

Two worth flagging. First, pressure-pain-threshold psychophysics in a static algometer paradigm is only loosely analogous to a V3 agent approaching a hazard tile over multiple steps. The high-level efference-copy logic transfers; the specific temporal dynamics (build-up phase, movement velocity, hazard distance) do not have direct equivalents. Second, the imagery-condition result -- non-zero attenuation without actual movement -- complicates SD-029's strict reliance on a_actual as the conditioning signal. If biology uses the intended rather than the executed motor plan in some regimes, then z_goal or a motor-plan latent might partially substitute for a_actual in the forward model. SD-029 does not currently specify this; it could be a useful boundary condition to note when the comparator under-attenuates.

## Confidence reasoning

Source quality is high: *Pain* is the highest-impact journal in the nociception literature, the design is within-subject with appropriate mixed-effects analysis, and the team has deep provenance in the sensory-attenuation field. Mapping fidelity is high because the stream tested is nociceptive, exactly SD-029's domain. Transfer risk is moderate but lower than for tactile-only studies. Aggregate 0.80 -- this is the strongest direct biological grounding for SD-029's nociceptive transfer. Combined with Kilteni 2020 on the efference-copy necessity, these two papers carry most of SD-029's mechanistic support.
