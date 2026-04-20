# Macaque PCC electrophysiology of default-mode processing (Hayden, Smith & Platt 2009)

## What the paper did

Hayden and colleagues recorded single-unit activity from posterior cingulate cortex (CGp) in two macaques performing simple visual attention tasks in which their behaviour varied from vigilant to inattentive. They measured firing rates during task-engaged periods, between trials, and during cued rest periods, and correlated firing-rate levels with behavioural performance. Control recordings in lateral intraparietal cortex -- an attention-network area -- provided a specificity check.

## Key findings relevant to SD-032d

CGp neurons reliably suppressed their firing during task performance and returned to a higher baseline between trials. Higher firing predicted upcoming errors and slower responses, linking the firing-rate level to behavioural performance on the next trial rather than merely correlating with gross task state. During cued rest periods -- when monkeys were explicitly liberated from exteroceptive vigilance -- firing also rose. These patterns were not observed in the lateral intraparietal recordings, so the effect is PCC-specific rather than a general property of cortical firing during attention fluctuations.

## How this translates to REE

SD-032d's PCC-analog emits a stability scalar in [0, 1] that modulates the SD-032a coordinator's switch threshold. Stability is a function of recent task success, fatigue (drive_level), and steps-since-offline-phase. Hayden 2009 is the primate electrophysiological counterpart: CGp firing tracks task engagement (and its failures), rises during disengagement, and predicts behavioural performance. The ree-v3 success-outcome EMA, updated via `agent.note_task_outcome`, is the computational analogue of the paper's engagement signal. The offline-recency counter, reset by `enter_offline_mode`, corresponds to CGp's elevated firing during cued rest.

The prediction for V3-EXQ-447 is specific: pcc_stability should covary with recent task-success history in a way that is (a) monotone, (b) detectable through ablation of the success-EMA input, and (c) predictive of subsequent coordinator behaviour. If the experiment shows stability scalar decoupled from task history, the ree-v3 arithmetic fails to capture the Hayden 2009 signature.

## Limitations and caveats

Two macaques is a small-n single-unit study, standard for the field but not high n. The mapping from macaque CGp single-neuron firing to ree-v3's scalar arithmetic is a substantial abstraction. Note also that the causal direction differs slightly: in Hayden 2009, CGp firing is a *state signal* whose level predicts upcoming performance; in ree-v3, task outcome *updates* the success EMA which *then* shapes future stability. These are complementary framings of the same engagement-tracking role but not identical -- a ree-v3 failure mode could look biologically plausible at the statistical level while missing the moment-to-moment predictive role that CGp firing plays in Hayden 2009. A more demanding test would measure whether pcc_stability decreases immediately prior to errors, matching the CGp firing-rate-predicts-error finding. Current V3-EXQ-447 design tests monotonicity against inputs rather than predictive power, so this prediction is beyond the current validation.

## Confidence reasoning

Strong source (PNAS, Platt lab, directly targeted question). Mapping fidelity is reasonably high: the key regularity (PCC activity inversely related to engagement) maps cleanly onto pcc_stability's EMA arithmetic. Transfer risk is moderate -- single-unit-to-scalar is a big abstraction step. Confidence 0.80 -- strong primate electrophysiology grounding for PCC-analog's engagement-tracking role, with a noted gap around the "predicts errors" aspect that ree-v3 does not yet operationalise.
