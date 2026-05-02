# Gherman & Philiastides 2018 -- VMPFC encodes early confidence in perceptual decisions

## What the paper did

Gherman and Philiastides ran a simultaneous EEG-fMRI study with participants performing a classic motion-direction discrimination task and rating their confidence on each trial. The methodological combination is the interesting part: single-trial multivariate discriminant analysis on the EEG to identify a confidence-related component in the moment-to-moment neural data, then fMRI co-localisation to find which brain regions tracked the trial-to-trial variability in that EEG signal. The question they asked was where in the brain a perceptual confidence signal first appears, and how early.

## Key findings

The EEG analysis identified a stimulus-independent component encoding confidence that emerged **before** the participant's overt choice and confidence report. Trial-to-trial variability in this early confidence signal mapped uniquely to ventromedial prefrontal cortex activity in the fMRI, with functional coupling to other frontal cortical regions associated with perceptual decision-making and metacognition. The architectural reading is that VMPFC holds an early, explicit confidence representation arising from decision dynamics, and this representation precedes (and likely informs) explicit metacognitive evaluation.

## How this maps to REE

Q-038 asks whether D_V (temporal-depth verisimilitude) is explicitly represented as a dedicated signal or emerges from distributed dynamics without local representation. Confidence is the closest in-domain cousin of D_V. Both are scalar 'trust this signal' quantities, both could in principle be implemented either way, both belong to the broader family of meta-signals that ARC-055 requires to be explicitly available to E3.

Gherman's result is direct empirical evidence that the brain implements at least one member of this family -- perceptual confidence -- as an early, localised, explicit representation. By computational analogy, this raises the prior probability that D_V is implemented similarly (Q-038 option A). The functional coupling pattern Gherman reports (VMPFC -> frontal cortex) is also architecturally suggestive: a localised confidence/precision signal feeds the broader decision system. REE's E3 could index a localised D_V signal through an analogous architecture, with a dedicated read-out region rather than ensemble decoding.

This paper sits alongside Guan 2024 as one of two anchors for option A in Q-038's evidentiary picture. Guan provides behavioural evidence that abstract temporal structure exists; Gherman provides neural evidence that at least one related precision/uncertainty signal is localised and explicit. Together they make option A biologically plausible without closing the question.

## Limitations and caveats

The most important caveat is internal to the paper: showing that VMPFC *carries* a confidence signal early does not show that confidence is *computed* in VMPFC. The signal could be a localised read-out of upstream distributed dynamics -- which is, awkwardly, exactly the architectural pattern Q-038 is trying to discriminate between. So this paper supports 'option A is biologically plausible' more strongly than it supports 'option A is the correct architectural choice for D_V'. Confidence is also not D_V. The two signals have different computational content and may be implemented by different mechanisms. The mapping is by architectural analogy, not direct measurement.

A methodological point: simultaneous EEG-fMRI is one of the most demanding combinations in human cognitive neuroscience, with significant artefact-removal and signal-coupling challenges. The Gherman/Philiastides pipeline is well-validated, but the inferential chain from 'EEG component decodes confidence' to 'this component co-varies trial-by-trial with VMPFC BOLD' to 'VMPFC holds an early confidence representation' has multiple steps and assumptions.

## Confidence reasoning

I am holding this at 0.70. The methodology is high-quality, the journal is top-tier, and the architectural lesson is real. Mapping fidelity is moderate because confidence is not D_V; transfer risk is moderate because the leap from a perceptual confidence signal to REE's coupling-stability quantity is substantial. The paper anchors one side of Q-038 but does not resolve it.

Source: According to PubMed, [DOI: 10.7554/eLife.38293](https://doi.org/10.7554/eLife.38293).
