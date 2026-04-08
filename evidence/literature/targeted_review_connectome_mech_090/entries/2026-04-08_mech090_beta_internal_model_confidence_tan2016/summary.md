# Tan et al. 2016 -- Post-Movement Beta and Internal Model Confidence

## What the paper did

Tan, Wade, and Brown recorded scalp EEG from 15 healthy young adults performing a visuomotor joystick task with adaptation. Subjects moved a cursor toward targets under conditions of either stable or randomly varying visual perturbations (priming phase), followed by a constant 60-degree rotation (adaptation phase) and washout. The key measure was post-movement beta synchronization (PMBS) -- the rebound of beta power over sensorimotor cortex occurring after movement termination. A Bayesian learning model was used to decompose the subjects' internal state into expected environmental uncertainty and estimation uncertainty (confidence in the forward model's predictions).

## Key findings

The central result is that PMBS amplitude negatively correlated with estimation uncertainty derived from the internal forward model. When the internal model was confident in its predictions (low estimation uncertainty), PMBS was high. When the model was uncertain -- because the environment had recently changed or perturbations were unpredictable -- PMBS was suppressed. Critically, this relationship held even when movement errors were matched between conditions, ruling out a simple error-driven account. PMBS tracked a computationally specific internal variable (model confidence) rather than motor output parameters like reaction time or movement duration, which did not differ between conditions.

The paper also showed that lower PMBS predicted greater trial-to-trial exploratory adjustment in subsequent movements. But when estimation uncertainty was included in the statistical model, the PMBS-adjustment correlation disappeared -- suggesting that PMBS drives adaptive behavior indirectly, via its reflection of internal model confidence, rather than through direct motor inhibition.

## REE translation

This paper presents a genuinely mixed picture for MECH-090. The claim states that beta oscillations gate E3-to-action-selection propagation -- not E3 internal updating. Tan et al. confirm that the behavioral consequence of beta is on output stability: high PMBS corresponds to maintaining the current motor policy (less exploration), low PMBS corresponds to policy change (more exploration). This is consistent with beta as an output gate.

However, the mechanism Tan et al. identify is not simple output gating. PMBS reflects the internal model's estimation of its own confidence -- a quintessentially internal computation. If beta merely gated output without reflecting internal state, one would expect PMBS to be independent of model confidence and driven instead by task demands on motor output. Instead, the internal model's self-evaluation is encoded in the beta signal. This means beta is at minimum a readout of internal processing, and plausibly a mediator between internal model evaluation and output policy.

For MECH-090, the question becomes: does the internal model confidence signal reflected in beta constitute "internal updating" in the sense the claim means? If MECH-090 intends that E3's model-building and trajectory evaluation continue independently while beta holds the output gate closed, then Tan et al.'s finding is consistent -- beta reflects the product of that internal computation (confidence) and uses it to modulate output. If MECH-090 intends that beta is mechanistically independent of internal processing, the finding weakens the claim: beta is clearly sensitive to internal model state.

## Limitations

The study measures cortical PMBS via scalp EEG, not beta in the basal ganglia or STN -- the primary locus of MECH-090's mechanism. PMBS is a phasic post-movement event, while MECH-090 concerns tonic beta during committed action sequences. The extrapolation from "post-movement cortical rebound reflects model confidence" to "sustained BG beta gates output during sequences while internal updating continues" requires bridging two different temporal scales, circuit levels, and functional contexts. The healthy population is an advantage over the Kuhn 2004 PD data, but the lack of direct BG recordings limits anatomical specificity.

## Confidence reasoning

Confidence is set at 0.72 with a mixed evidence direction. Source quality is high -- rigorous experimental design with computational modeling in a well-controlled adaptation paradigm. Mapping fidelity is moderate because of the cortical-vs-BG and phasic-vs-tonic discrepancies. The mixed direction reflects a genuine conceptual tension: beta's functional effect is on output policy (supporting MECH-090), but beta encodes internal model state (complicating the pure output-gate framing). This paper refines rather than refutes the claim -- it suggests that the "gate" is not a dumb switch but an information-carrying signal whose state depends on internal computation.
