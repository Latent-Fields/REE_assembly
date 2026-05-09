# Hong, Fallon, Friston & Harris 2018 — Rapid Eye Movements in Sleep Furnish a Unique Probe Into Consciousness

**Source:** Hong CC-H, Fallon JH, Friston KJ, Harris JC. *Frontiers in Psychology* 9:2087 (2018). [DOI](https://doi.org/10.3389/fpsyg.2018.02087). PMID 30429814. According to PubMed.

## What the paper did

This paper extends the Hobson-Hong-Friston 2014 framework with a more empirical anchor: REMs themselves (the rapid eye movements that name REM sleep) are temporally precise, fMRI-identifiable events that mark moments of internalised active inference during the REM state. The neural correlates — REM-locked multisensory-motor integration plus activation in retrosplenial cortex, supplementary eye field, and cholinergic basal nucleus — are read as the brain "scanning" its self-generated visual constructs in the absence of sensory afferents. The paper proposes REMs as a probe of active inference at the moments when the brain is isolated from the sensorium.

## Why it matters for MECH-204

This paper does not directly tackle the F1-vs-F3 architectural question, but it strengthens the broader Hobson-Friston framework that the previous lit-pull entry (Hobson, Hong & Friston 2014) leans on. The temporally precise REM events are the operational mechanism by which the generative-model refinement happens during REM. If those refinement operations produce updated model parameters that waking inference then reads in the normal course, the F1 architecture is sufficient — the consumer side does not need a separate broadcast channel.

The paper is most useful as **second-line corroboration** of the Hobson-Friston 2014 reading, with one important methodological add: REMs are identifiable in fMRI, which means the architectural commitment is empirically tractable. If the architecture were F3 (post-REM broadcast read by waking decision circuits), one would predict REM-locked fMRI activity in waking-decision circuits (dlPFC, BG) that is mechanistically separate from generative-model parameter updates. The paper does not present such evidence; the activations are in retrosplenial / SEF / basal-nucleus circuits more naturally read as part of the model-refinement loop than as broadcast channels.

## Mapping to REE

For REE's MECH-204 SR-3, this paper supports the F1 architecture indirectly. The REM-phase active-inference loop — the temporally precise REMs marking model-refinement operations — IS the substrate that REE's `_persistent_zero_point` EMA-tracks across cycles. The waking consumer side, per the paper's framework, is just normal waking inference running on the refined model parameters; no separate broadcast read is needed.

If V3-EXQ-541b's step-size sweep finds that F1 + step-tuning clears C3, this paper is part of the literature backing the F1-only Phase 7 closure decision (i.e. Phase 7 / Option B becomes architecturally redundant in V3). If 541b fails C3 across the defensible step band, the absence of F3-supporting evidence in this paper is informative — it suggests F3 may be the wrong direction and the right move would be a different architectural lever entirely (e.g. faster recalibration cadence via SD-006 phase 2 async, or F2-equivalent integration deeper into the WRITEBACK phase).

## Caveats

(1) The paper is more about REMs as methodological probes than about the F1-vs-F3 architectural distinction REE is asking. The F1-supporting reading is inherited from the broader Hobson-Friston framework rather than stated explicitly. (2) Lower confidence than the 2014 paper because the 2018 paper's main contribution is methodological (REMs as fMRI markers) rather than the architectural question REE is asking. (3) The empirical fMRI evidence cited is for REM-LOCKED activity DURING REM; the paper does not directly empirically address what waking circuits read AFTER REM, which is the F1-vs-F3 dichotomy.

## Confidence reasoning

0.68 supports for the F1-sufficient reading of MECH-204. Source quality 0.78 (Frontiers Psychology peer-review; Friston co-author). Mapping fidelity 0.65 (paper's main contribution is methodological; F1-support is inferred from the framework rather than stated). Transfer risk 0.30 (REMs-as-active-inference-probes transfers cleanly to REE; the F1 inference is one architectural step removed). The paper functions as second-line corroboration of the Hobson-Friston 2014 reading rather than primary evidence on its own.
