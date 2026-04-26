# Feldman & Friston 2010 -- Attention, uncertainty, and free-energy

## What the paper did

Feldman & Friston offered a computational reformulation of attention as inference about precision. In their account, attention is not a separate mechanism that selects channels but the natural consequence of jointly optimising a free-energy bound on surprise -- the brain must estimate both the state of the world and the precision (inverse variance) of the data that report on that state, and the cued channel in a Posner paradigm gets a higher precision estimate, hence higher gain on its prediction errors. They demonstrated through neuronal simulation that this single principle reproduces psychophysical and electrophysiological observations including biased competition, attentional capture, and speed-accuracy tradeoffs.

## Key findings relevant to MECH-269b

The paper establishes the closest available cortex-side precedent for MECH-269b per-stream V_s. Precision is set per-channel, varies dynamically with state, and modulates how strongly each channel prediction error drives downstream representations. In MECH-269b language: a stream that is poorly predicted (low V_s) is the cortical analogue of an unattended channel, and its prediction-error contribution to downstream control is correspondingly muted. The mathematical structure -- precision as a state-dependent multiplicative gain on prediction error -- is exactly what MECH-269b assumes on the cortical side.

This is tag (a) direct support for cortex-side per-channel precision gating. It supplies the framework within which V_s as a per-stream signal is computationally sensible and biologically plausible.

## How the findings translate to REE

MECH-269b assumes that V_s, computed by a verisimilitude-tracker for each latent stream, is broadcast to downstream consumers and used to weight that stream contribution to ascending PE. Feldman & Friston framework lifts directly: the V_s signal plays the role of attentional precision, and the consumers (E1 forward sensory predictor, E2 transition model, and onward to dACC adaptive control / SD-032b) play the role of the cortical hierarchies whose ascending PE messages must be precision-weighted before being integrated into higher-level beliefs.

## Limitations and caveats

Two caveats. First, the paper does not commit on whether each anatomically-distinguishable sensory stream has its own precision parameter or whether one global precision schedule modulates all streams together. MECH-269b per-stream V_s is consistent with the former interpretation but the paper allows the latter -- the per-stream specialisation is consistent but not directly tested. Second, the framework is purely cortical and attentional. The hippocampal proposer is not in scope, so the symmetric-application question -- does the same precision signal that gates cortical sensory channels also gate hippocampal anchor selection? -- is not engaged at all here. This is a measurement gap (tag d).

## Confidence reasoning

Confidence 0.70 -- supports MECH-269b at the cortical-architectural level. Source quality good (computational simulation grounded in psychophysical / electrophysiological observations). Mapping fidelity moderately high because the mathematical structure is exactly what MECH-269b assumes on the cortical side. Transfer risk modest. The clear gap is the absence of any hippocampal-proposer engagement, which is the symmetric-application novelty MECH-269b carries.
