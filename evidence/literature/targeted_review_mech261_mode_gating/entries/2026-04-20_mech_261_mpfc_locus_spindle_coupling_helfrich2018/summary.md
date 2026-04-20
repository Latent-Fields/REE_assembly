# Helfrich et al. 2018 — Medial frontal cortex is the anatomical locus of the SO-spindle gate

## What the paper did

Helfrich and colleagues collected structural MRI (atrophy maps) and overnight high-density EEG with polysomnography in a cohort of healthy younger and older adults. The behavioural measure was overnight consolidation of word-pair associative memory. They used directional cross-frequency coupling to quantify whether the cortical slow oscillation "drives" the timing of sleep spindles, and they regressed the coupling quality against regional atrophy maps. Atrophy specifically within medial frontal cortex (MFC) predicted temporal dispersion of the SO-spindle coupling and predicted overnight forgetting; atrophy in other regions (non-medial frontal, parietal, occipital) did not.

## Why this matters for MECH-261

Maingret 2016 shows that in rodents the coupling gates writes *to* mPFC. Helfrich shows that in humans the coupling is *computed by* MFC — and when the locus atrophies, the gate disperses. This is the converse-direction evidence. MECH-261's abstraction uses a central coordinator (SalienceCoordinator, the SD-032a implementation) to issue per-mode gate weights, but the biological fact Helfrich pin down is that the gate-issuing substrate is anatomically localised: remove MFC tissue and the gate's temporal precision disperses as a function of how much tissue is missing. The MECH-261 design already names SD-033a (lateral-PFC-analog) as the primary target of the write in SWS; this result says the locus-of-selection and the target may be overlapping or adjacent cortical substrates, not physically distant nodes.

This changes the implementation direction subtly: if SD-033a is the target of the write in SWS and also the seat of the gate that decides whether the write lands, then a future V4 implementation of MECH-261 that tries to separate "gate computer" from "gate consumer" into distinct substrates would diverge from the biology. A single-substrate implementation in which SD-033a both produces the gate signal and is the target of the gated write is closer to the Helfrich anatomy. This is worth noting in the SD-033 design doc when the V4 staged implementation of MECH-261 is taken up.

## Limitations

Correlational — Helfrich cannot produce a causal dispersion by ablating MFC. The regional specificity (MFC but not other cortices) is strong evidence that MFC is specifically involved, but does not distinguish between MFC as the generator of the coupling, MFC as a recipient whose feedback sharpens the coupling, or MFC as a cortically-disinhibiting substrate whose damage allows other regions to interfere. Scalp EEG also measures a reduced projection of the underlying thalamocortical circuit activity, so the exact MFC substructure is not resolved.

The aging context may also carry confounds: age brings systemic changes in spindle density, slow-wave amplitude, and memory encoding itself; the paper controls for these but cannot exclude residual variance.

## Confidence reasoning

Source quality high (Neuron, good regional controls, cross-modal MRI + EEG + behaviour design). Mapping fidelity solid on the "gate has an anatomical locus" axis, weaker on "locus is specifically SD-033a's homologue" — Helfrich's MFC ROI includes some medial prefrontal territory that maps more naturally onto REE's PCC/pACC subdivisions than onto the lateral-PFC SD-033a. Transfer risk 0.30. Overall 0.73.
