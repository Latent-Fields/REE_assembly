# Daw, O'Doherty, Dayan, Seymour & Dolan 2006 — Cortical substrates for exploratory decisions in humans

[DOI](https://doi.org/10.1038/nature04766) · PMID 16778890 · *Nature* 441(7095):876–9

## What the paper did

A four-armed bandit fMRI task in healthy adult humans. Each subject's choices were modelled with a Kalman-filter reinforcement-learning model that classifies each trial as exploratory or exploitative based on the relationship between the chosen arm's expected value and the maximum-expected-value alternative. Frontopolar cortex (BA10) and intraparietal sulcus showed preferentially elevated BOLD during the exploratory trials. Striatum and ventromedial prefrontal cortex showed preferentially elevated BOLD during exploitative trials. The dissociation is robust and survives standard confounds for value, reaction time, and uncertainty.

## Why this matters for ARC-065

This is the load-bearing R3 paper (cluster-vs-extend question). The brain has anatomically and functionally distinct substrates for exploration and exploitation; they are not the same circuit running at different gain. REE has substantial substrate already in place for the *exploitation* side: E3 score-aggregation, SD-033a lateral PFC + SD-033b OFC PFC bias channels, dACC adaptive control (SD-032b), MECH-295 drive→liking→approach bridge. None of these substrates are candidates for the exploration-side analog. The frontopolar BOLD signature in Daw 2006 has no current REE analog.

This argues for the R3 PROMOTE-TO-CLUSTER verdict: ARC-065 is a separate architectural pathway, not an extension of an existing wanting / value-bias / multi-level-wanting cluster. ARC-051 multi-level wanting hierarchy could in principle absorb a curiosity sub-MECH, but Daw 2006 shows the substrate is anatomically separate from value-coding regions, which is exactly the property a separate architectural slot is designed to capture.

## Limitations and confidence

fMRI cannot resolve the cellular or projection-level architecture of the frontopolar exploration signal. The paper does not directly test the structured-vs-noise (R1) decomposition; it identifies *where* exploratory decisions are processed, not *what* generates the decision variability. The follow-up Wilson 2014 work (PMID 25347535, same Cohen lab) decomposes exploration into directed and random components but cannot say whether they share or differ in substrate. Confidence aggregate 0.82 reflects the foundational venue and clean dissociation, with a moderate transfer risk because the bandit task differs from REE's continuous-state foraging.

## Failure signature it would falsify

An REE substrate that has only the exploitation-side machinery (no separate diversity-generation pathway) should fail to produce frontopolar-equivalent activation timing during exploration phases — and consequently should fail to dissociate exploration from exploitation in any behavioural readout that depends on the timing of the explore→exploit transition.
