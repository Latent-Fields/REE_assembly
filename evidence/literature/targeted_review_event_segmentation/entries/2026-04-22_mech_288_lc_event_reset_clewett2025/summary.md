# Clewett, Huang & Davachi 2025 -- Locus coeruleus activation "resets" hippocampal event representations and separates adjacent memories

According to PubMed, this is the most direct evidence to date that LC activation at event boundaries drives hippocampal pattern separation. [DOI](https://doi.org/10.1016/j.neuron.2025.05.013)

## What the paper does

Combined fMRI, neuromelanin imaging, and pupillometry in healthy human adults. Subjects encoded sequences containing event boundaries (context shifts). The authors measured: (a) pupil-linked arousal at boundaries (LC surrogate), (b) BOLD activity in LC and hippocampus, (c) neuromelanin signal as a structural proxy for chronic LC activity, and (d) subsequent memory separation between adjacent events.

## Findings relevant to MECH-288 and MECH-287 coupling

Three findings convergently support the (c) coupling option from the spec's question 3. (1) Event boundaries triggered pupil-linked arousal AND LC BOLD activation -- the boundary detection is co-temporal with the broadcast trigger. (2) LC activation predicted hippocampal DG pattern separation between adjacent memories -- the broadcast is downstream of boundary detection and consequential. (3) Hyperaroused tonic LC activity DISRUPTED the transient phasic boundary-locked LC response and impaired event segmentation -- there is a phasic/tonic distinction the substrate must respect.

## Mapping to REE

The architectural recommendation is unambiguous. Implement MECH-288 as the upstream comparator (boundary detection) and MECH-287 as the downstream broadcast that fires at the moment MECH-288 emits a new segment_id. MECH-287 does NOT need its own independent comparator code -- it reads MECH-288 boundaries. This collapses an architectural ambiguity and prevents duplication.

A second design decision: add a tonic-vs-phasic guardrail. MECH-287 broadcast strength should be normalised against background activity, not absolute. If background MECH-287 trigger is saturated, phasic boundary-driven broadcasts will be lost -- exactly the failure mode Clewett 2025 documents in hyperaroused LC.

## Limitations and caveats

fMRI + pupil + neuromelanin all measure surrogates of LC activity at BOLD timescale, not direct single-unit recording. The coupling is robust at this scale but the substrate-level ms-scale coupling cannot be inferred directly. The (c) coupling option is the most parsimonious reading; (a) independent-correlated and (b) shared-stage remain logically possible but require additional architectural components without explanatory benefit.

A second caveat: the LC mapping assumes MECH-287 broadcast is implemented as an LC-analog. If MECH-287 instead becomes a hippocampal-comparator-derived broadcast (per Vinogradova/Lisman comparator stage in v_s_foundation pull verdict 5), the coupling architecture is more complex -- two coupled-stage components both reading MECH-288 boundaries.

## Confidence reasoning

0.92 -- the highest in this pull. Neuron 2025, three-modality convergent design, directly addresses the architectural question the spec poses. THE single best paper for MECH-287/288 coupling.
