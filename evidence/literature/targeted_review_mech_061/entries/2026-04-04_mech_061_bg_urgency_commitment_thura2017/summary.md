# Literature Summary: 2026-04-04_mech_061_bg_urgency_commitment_thura2017

## Claims Tested

- `MECH-061`

## Source

- Thura D, Cisek P (2017), *The Basal Ganglia Do Not Select Reach Targets but Control the Urgency of Commitment*.
- Neuron 95(5):1160-1170.e5
- DOI: `10.1016/j.neuron.2017.07.039`
- PMID: 28823728

## Mapping to REE

What Thura and Cisek found in macaque motor cortex and GPi is, if you squint slightly, almost exactly what MECH-061 requires: a neural structure that does not carry content about *what* action to execute but instead carries information about *when* deliberation ends. The basal ganglia here are not selecting the target -- premotor and motor cortex do that -- but they are controlling the urgency with which the cortex commits to whatever it has been building toward. GPi output rises monotonically across the deliberation period and modulates the gain of cortical target-selection signals. In REE's framing, that urgency crossing a threshold is the functional equivalent of the commit-boundary token: it is the moment at which error signals change meaning.

The implication for MECH-061 is concrete. Before the urgency threshold is crossed, cortical signals are weighting competing options, running implicit simulations of counterfactual actions, and computing prediction errors over expected trajectories -- exactly the pre-commit regime where E2's simulation errors are the operative learning signal. After the GPi urgency signal crosses its implicit threshold, the system switches from weighing evidence to executing the committed action, and any subsequent errors are realized-outcome errors, not predictive ones. The commit-boundary token in MECH-061 discretises what in biology appears to be a continuous dynamics-driven transition; the paper shows that the BG are where that control surface lives, not the cortical deliberation machinery itself.

What the paper does not give us is an explicit error-routing mechanism. The urgency model is about timing of commitment, not about what happens to learning signals after commitment occurs. The inference that urgency threshold crossing reclassifies error routing requires an additional step that REE supplies architecturally but that this paper does not directly test. This is the main source of mapping risk.

## Caveats and Mapping Limits

- The urgency signal is graded and continuous; MECH-061's boundary token is discrete. The discretization step is REE's architectural contribution, not the paper's.
- Results are from motor reaching decisions in macaque, not higher-level cognitive or harm-attribution decisions.
- The paper does not address learning-signal reclassification or dual-channel error routing.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.71`
- Rationale: strong empirical grounding for BG-mediated commitment timing as a distinct functional event, directly relevant to MECH-061's boundary concept; confidence discounted for lack of explicit error-routing evidence and motor-to-cognitive transfer risk.
