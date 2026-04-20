# Crapse and Sommer (2008) -- Corollary Discharge Across the Animal Kingdom

## What the paper does

Crapse and Sommer survey the neurophysiological evidence for corollary discharge (CD) circuits across species and modalities. A corollary discharge is a copy of a motor command routed to sensory structures, where it modulates processing of incoming sensory signals. The function is to disambiguate self-caused from externally-caused sensory input.

The review organises CD by sensory-ambiguity class and by taxonomic breadth. Electrosensory CD in weakly electric fish (the ELL circuit): electric organ discharge commands are copied to the cerebellum-like electrosensory lobe, where they subtract predicted self-caused electrical input from the sensory stream. Auditory CD in crickets: the singing command gates auditory processing so the animal is not deafened by its own chirp. Songbird CD: HVC projects to the auditory cortex during vocalisation, attenuating responses to self-produced song. Primate oculomotor CD: superior colliculus sends a copy of saccade commands via mediodorsal thalamus to frontal eye fields and parietal cortex, supporting spatial updating across saccades. Primate somatosensory CD: copies of limb movement commands attenuate somatosensory cortex responses to self-caused skin stimulation.

The authors propose a functional taxonomy: lower-order CD that supports online motor-sensory cancellation, and higher-order CD that supports perceptual stability, monitoring of internal state, and spatial updating.

## What matters for MECH-256

MECH-256 is stream-agnostic by design. The claim is that self-attribution on any reafferent latent stream is implemented by the same comparator structure: predicted from a forward model, compared to observed, residual is the agency signal. The REE substrate commitments follow downstream: SD-029 realises this on the sensory-discriminative harm stream, SD-030 on the motor-proprioceptive stream, SD-031 on the world-causal stream.

Crapse and Sommer provide the biological grounding for the substrate-agnostic aspect. They document that efference copy plus comparator is instantiated across anatomically distinct circuits in animals separated by hundreds of millions of years of evolution: a cerebellum-like structure in fish, HVC in songbirds, superior colliculus and MD thalamus in primates. The same computational principle is solved in radically different anatomy. This is precisely the universality claim MECH-256 depends on. It is what lets REE commit to E2_x forward models as a general architectural pattern rather than a cerebellum-specific device.

The review also supports the single-pass-comparator framing MECH-256 endorses over the two-pass counterfactual framing SD-003 originally implemented. In every CD circuit Crapse and Sommer describe, the computation is one forward prediction compared to one observation. There is no parallel rollout of the counterfactual action. The counterfactual branch, whatever its appeal as a computational idealisation, is not what the neurobiology actually does.

## Caveats

The review's coverage is strong for fast, phasic sensorimotor streams and weaker for slower, integrative, affective streams. The evidence for an efference-copy-driven comparator on the nociceptive stream specifically is not a primary focus. Descending pain modulation via PAG and RVM is an adjacent literature that would need to be brought in to ground the z_harm_s case thoroughly.

The framing is classical (efference copy, subtraction) rather than hierarchical-predictive (precision-weighted prediction error). The two vocabularies are compatible but not identical, and the mapping to REE's latent-stream comparator may require some translation between them.

The paper predates the modern sense-of-agency literature by enough that the agency-attribution claim it supports is primarily computational rather than phenomenological. For the agency-phenomenology side, Haggard 2017 (already in the sd003_successor_comparator directory) is the better companion.

## Confidence reasoning

Confidence 0.82. Source quality very high (NRN 2008, heavily cited, comprehensive). Mapping fidelity high because the cross-species, cross-modality universality of the efference-copy-plus-comparator structure is exactly the biological grounding MECH-256's substrate-agnostic framing requires. Transfer risk moderate because the nociceptive-stream application is not directly covered and must be inferred.

This entry is best read alongside Welniarz 2021 (same lit pull) and Haggard 2017 (in the sd003_successor_comparator directory): Crapse and Sommer give the cross-species argument, Welniarz gives the unifying motor-plus-agency framing, Haggard ties the comparator structure to cue-integration and precision weighting.
