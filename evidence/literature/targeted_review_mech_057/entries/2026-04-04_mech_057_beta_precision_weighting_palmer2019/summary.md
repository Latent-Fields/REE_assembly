# Literature Summary: 2026-04-04_mech_057_beta_precision_weighting_palmer2019

## Claims Tested

- `MECH-057a` (Committed action sequences suppress sensory precision reweighting until execution completes)

## Source

- Palmer CE, Auksztulewicz R, Ondobaka S, Kilner JM (2019).
  *Sensorimotor beta power reflects the precision-weighting afforded to sensory prediction errors.*
  NeuroImage, 200, 59-71. [DOI: 10.1016/j.neuroimage.2019.06.034](https://doi.org/10.1016/j.neuroimage.2019.06.034)
- PMID: 31226494

## What Was Studied

Palmer et al. had healthy human participants perform a visuomotor adaptation task in which the uncertainty of visual feedback was directly manipulated -- participants had to adapt their reaching movements to a rotated cursor, and the precision of the cursor feedback was varied experimentally. EEG was recorded throughout, and the Hierarchical Gaussian Filter (HGF) was used to extract latent variables: the precision-weighting of sensory prediction errors at each trial, independent of error magnitude.

The key question: does sensorimotor beta power track error, or does it track the precision (inverse uncertainty) afforded to error?

## Key Findings

Beta power correlated with the inverse uncertainty afforded to sensory prediction errors -- both before and after movement. The correlation held independently of the prediction error magnitude itself. The authors interpret this as sensorimotor beta encoding relative uncertainty within the sensorimotor system: high beta = high precision weighting = the sensory channel is trusted; low beta = low precision = sensory signals are downweighted.

This is a genuinely important distinction for MECH-057a. The earlier, simpler view was that beta suppresses movement initiation (a motor output gate). The Palmer et al. result reframes beta as a precision-weighting signal: it doesn't block the motor channel, it modulates how much sensory prediction error is allowed to revise the current state estimate. That is exactly what MECH-057a claims happens during a committed action sequence.

## Mapping to MECH-057a

MECH-057a states: "Committed action sequences suppress sensory precision reweighting until execution completes." The evidence quality note on the claim explicitly distinguishes motor output suppression (what MECH-090 claims) from sensory precision reweighting suppression (what MECH-057a claims) -- referencing this distinction as the reason MECH-090 is probably the "more correct" account of beta's role in the REE architecture, but MECH-057a's precision-suppression framing is worth preserving as an independent testable prediction.

Palmer et al. 2019 is the most direct empirical grounding for MECH-057a's specific framing. If beta encodes precision weighting rather than motor gating, then elevated beta during committed sequences would suppress sensory precision reweighting -- exactly the MECH-057a prediction. The pre-movement effect (beta elevation before the limb moves, tracking prior precision) is particularly interesting: it suggests the suppression is anticipatory and plan-level, not purely reactive.

## Caveats

The precision-beta correlation was measured in the context of voluntary reaching, not during committed action sequences in the sense REE uses the term. The "commitment" in MECH-057a refers to a qualitative transition (the agent is now executing a planned trajectory and should not be deflected by ambient sensory noise), whereas in Palmer et al. the precision modulation is trial-by-trial continuous. Whether the committed/uncommitted distinction in REE maps cleanly onto high/low precision in this paradigm is an inference, not a direct test. The paper also does not address sequence-level gating -- it is action-level within a single reaching movement.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.78`
- Rationale: Most direct empirical support for the precision-weighting interpretation of beta in sensorimotor cortex; the specific Bayesian framing aligns with the MECH-057a mechanism.
