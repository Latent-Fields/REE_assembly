# Aberrant Salience, Information Processing, and Dopaminergic Signaling in People at Clinical High Risk for Psychosis

**Howes, Hird, Adams, Corlett & McGuire (2020) — Biological Psychiatry**
DOI: [10.1016/j.biopsych.2020.03.012](https://doi.org/10.1016/j.biopsych.2020.03.012)
*Based on articles retrieved from PubMed*

## What the paper did

Howes and colleagues synthesised evidence from neuroimaging, neurochemistry, and computational psychiatry to ask what distinguishes people at clinical high risk (CHR) of psychosis from those who subsequently transition to frank psychosis, and what distinguishes both groups from healthy controls. The review focused on three intersecting processes: striatal dopamine function, reward and salience processing, and predictive processing parameters (particularly precision and prediction error signalling). The inclusion of the CHR population is methodologically valuable: these are individuals with dysregulated processes but not yet at clinical threshold, making them a window onto the transition dynamics.

## Key findings

CHR individuals show dysregulated subcortical dopamine function -- elevated striatal dopamine synthesis and release relative to controls, though often less extreme than in frank psychosis. This dysregulation tracks with aberrant salience attribution: CHR individuals over-weight irrelevant sensory events, treating them as prediction errors requiring model update. The predictive processing framing re-describes this as a precision dysregulation: the weight given to incoming prediction errors relative to prior expectations is too high, causing the agent's world model to be destabilised by events that a well-calibrated system would dismiss. Early adverse life experiences appear to shift prior expectations in ways that lower the threshold for psychotic transition -- people with early trauma have priors that are more easily overridden by sensory evidence.

## REE translation

Q-018 asks for an RC-conflict threshold that prevents both authority spoofing and chronic over-suppression. Howes et al.'s aberrant salience model gives a vivid characterisation of the under-threshold failure mode: an agent whose RC detector fires too readily treats every mild world-model mismatch as a genuine authority signal, updating its model based on spurious inputs. This is precisely authority spoofing at the process level -- not an external attacker exploiting a low threshold, but the agent's own calibration making it susceptible to noise. The CHR-to-psychosis transition suggests that the failure does not require a catastrophic change in parameters; a modest shift in the precision weighting (slightly elevated dopamine tone) can gradually erode the stability of the world model over time. For REE, this implies that the RC threshold must be calibrated not just to the current sensory environment but to the expected density of genuine authority signals -- an environment with many legitimate authority signals requires a lower threshold (to be responsive) but that same low threshold makes the system vulnerable in adversarial or high-noise environments. The hysteresis criterion in Q-018 is directly supported: there is a range of threshold values (the CHR zone) where the system is functioning but vulnerable, and the transition to collapse is gradual rather than abrupt.

## Limitations

The paper describes biological processes (dopamine, early trauma, neural connectivity) whose mechanisms have no direct implementation counterpart in REE. The mapping from dopamine dysregulation to threshold parameter is conceptual, not quantitative -- there is no way to read off the correct RC threshold value from this review. The CHR population represents one specific clinical context; the authority spoofing scenario in Q-018 may have a different parameter structure, with external adversarial manipulation rather than endogenous dopamine dysregulation driving threshold vulnerability. The review also focuses on the low-threshold failure mode; the high-threshold failure (chronic over-suppression) is less well characterised in the psychosis literature (it corresponds more to conditions like flat affect or avolition than to the aberrant salience models covered here).

## Confidence reasoning

I rate this 0.74. The paper provides the strongest available conceptual framework for understanding threshold calibration failure in the context of Q-018, supported by convergent evidence from neuroimaging and computational psychiatry. The confidence penalty comes from the biological-to-computational gap and from the asymmetric coverage of failure modes (low-threshold/psychosis side well covered; high-threshold/over-suppression side less so).
