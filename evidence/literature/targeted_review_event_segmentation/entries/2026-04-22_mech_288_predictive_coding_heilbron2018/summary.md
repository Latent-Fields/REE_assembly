# Heilbron & Chait 2018 -- Great Expectations: Is there evidence for predictive coding in auditory cortex?

According to PubMed, this is a critical evaluation of the predictive-coding framework with implications for what PE-related architectural commitments are biology-tested vs over-specified. [DOI](https://doi.org/10.1016/j.neuroscience.2017.07.061)

## What the paper does

Heilbron and Chait identify five key assumptions of predictive coding theory and audit each against animal, human, and modelling evidence in auditory cortex. The five: (1) responses shaped by expectations, (2) hierarchical organisation of expectations, (3) anticipatory predictions revealed by unexpected omission, (4) separate error and prediction neurons, (5) specific oscillatory signatures (gamma for error, alpha-beta for predictions).

## Findings relevant to MECH-288

Strong support for (1), (2), (3) -- the architectural commitments MECH-288 most relies on. Hierarchical PE responses are well-attested. Unexpected omission generates a clean PE signal -- this is direct evidence that PE-spike at change-points (MECH-288 trigger criterion (a)) is biologically real. WEAK or contradictory evidence for (4), (5).

## Mapping to REE

Two takeaways for substrate design. (1) MECH-288 trigger criterion (a) PE-spike has solid biological grounding for hierarchical PE responses. The substrate can use PE-threshold safely as one trigger criterion. (2) The substrate should NOT architect a separate "error neuron" / "prediction neuron" division because biology has not validated this. A single PE signal computed from forward-model output minus actual is biologically sufficient. This is a negative architectural recommendation: do not over-engineer the PE comparator into separate prediction/error modules.

## Limitations and caveats

Auditory-cortex review; not directly about event segmentation. The transferable lesson is methodological -- which PE-related architectural commitments are biology-tested vs over-specified. Treat this paper as a sanity check on what to commit to in the substrate.

## Confidence reasoning

0.65 mixed. Useful for algorithm guidance (Q4) and as a calibration on what PE-account commitments are empirically justified. Lower mapping fidelity because the paper is about auditory cortex not event segmentation per se. Mixed direction because it supports some architectural choices and weakens others.
