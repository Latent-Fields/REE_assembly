# Thought Insertion as a Self-Disturbance: An Integration of Predictive Coding and Phenomenological Approaches

**Sterzer, Mishara, Voss & Heinz (2016) — Frontiers in Human Neuroscience**
DOI: [10.3389/fnhum.2016.00502](https://doi.org/10.3389/fnhum.2016.00502)
*Based on articles retrieved from PubMed*

## What the paper did

Sterzer and colleagues took on one of the harder problems in computational psychiatry: thought insertion, the first-rank symptom of schizophrenia in which a patient experiences thoughts that feel like they come from someone else. Existing predictive coding accounts had handled hallucinations and delusions but had not coherently addressed thought insertion. The paper integrated early 20th-century phenomenological accounts from the Heidelberg School (Gruhle, Mayer-Gross, Beringer) -- who first named thought insertion as an 'Ichstorung' (disturbance of the self-boundary) -- with the modern precision-weighted prediction error framework to propose a mechanism.

## Key findings

The proposed mechanism hinges on a precision imbalance between two levels of the predictive hierarchy: the precision of context-dependent top-down predictions (how confident the agent is in its own thought-generating process) versus the precision of the resulting internal signals (how strongly those thoughts register as prediction errors). When top-down precision is reduced relative to internal signal precision, the agent's own thoughts are experienced as arriving from 'nowhere' -- they carry aberrant salience. The individual then attempts to attribute this unexpected internal signal to some external cause, resulting in thought insertion. This is mechanistically analogous to the aberrant salience of external stimuli (the Howes 2020 model), but applied to internal rather than external events.

## REE translation

The thought-insertion mechanism is the computational inverse of authority spoofing, and both describe the same underlying calibration failure: the RC threshold (or precision-ratio threshold) is wrong. In thought insertion, internally generated signals are treated as if they came from an external authority. In authority spoofing, externally generated signals are given too much authority over the internal world model. Both failures arise from the same miscalibration -- the ratio of the agent's confidence in its own model to its weighting of incoming signals. For Q-018, the precision-ratio framing is the key insight: the RC threshold should not be a simple signal-strength cutoff but a ratio comparing the confidence of the incoming authority signal to the agent's current world-model confidence. A threshold expressed as a precision ratio is harder to spoof than an absolute threshold, because an adversary would need to both inflate the authority signal's apparent precision and reduce the agent's confidence in its own model simultaneously. The thought-insertion literature also suggests that the failure is continuous (not catastrophic) -- patients experience a spectrum from mild depersonalisation to frank thought insertion, suggesting the hysteresis zone in Q-018 has a gradual slope rather than a sharp edge.

## Limitations

The predictive coding account of thought insertion is a theoretical proposal, not an established mechanism with empirical support at the level of specific circuit computations. The phenomenological descriptions from the Heidelberg School are conceptually rich but not operationalised in ways that translate directly to REE parameters. The precision-ratio mechanism proposed here is compatible with but not uniquely implied by the phenomenological data. REE's RC conflict involves E1 world-model prediction error, which is a different computation from the internal/external attribution computation involved in thought insertion -- the structural similarity is genuine but the mechanisms may diverge at implementation level.

## Confidence reasoning

I rate this 0.70. The paper provides a theoretically well-grounded account of a clinical failure mode that maps directly onto Q-018's authority-spoofing concern, and the precision-ratio framing offers a concrete direction for calibration design. The confidence penalty comes from the theoretical-only nature of the evidence and the partial mapping between thought-insertion phenomenology and REE's RC conflict mechanism.
