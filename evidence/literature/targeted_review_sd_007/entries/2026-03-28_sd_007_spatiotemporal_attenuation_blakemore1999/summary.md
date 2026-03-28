# Blakemore, Frith & Wolpert 1999 — Spatio-temporal prediction modulates the perception of self-produced stimuli

Based on articles retrieved from PubMed (DOI: [10.1162/089892999563607](https://doi.org/10.1162/089892999563607)).

## What the paper did

This is the companion behavioural study to the 1998 fMRI paper by the same group. Using a robotic setup, Blakemore and colleagues parametrically manipulated the correspondence between the participant's action and the resulting tactile stimulus. Two manipulations: (1) temporal delay — they introduced varying delays between the movement of the left hand controlling the robot and the tactile outcome on the right hand; (2) spatial perturbation — they rotated the direction of the tactile movement relative to the direction of the controlling hand movement by varying degrees. Participants rated the ticklishness and intensity of the resulting tactile sensation.

## Key findings

Both manipulations degraded the attenuation in a parametric, graded fashion. Increasing delay increased perceived ticklishness — self-produced stimuli became progressively more ticklish (i.e., less attenuated) as the delay grew. Similarly, increasing spatial mismatch increased perceived intensity. The proposed interpretation is explicit: the attenuation is proportional to the error between the sensory feedback predicted by the internal forward model and the actual sensory feedback. Perfect correspondence (zero delay, zero spatial rotation) produces maximum attenuation; increasing mismatch is experienced as an increasing prediction error that reduces the cancellation.

## REE mapping

This paper provides two specific insights for SD-007 that the 1998 paper could not. First, temporal correspondence is required: the predictor output must be computed from a state that is appropriately aligned in time with the incoming sensory signal. This maps to the SD-007 choice to use z_world_raw_prev (the previous timestep's world state) rather than a more temporally displaced state — the predictor is trained to anticipate the next-step change, not a delayed one.

Second, and more directly relevant to the input selection decision, spatial correspondence is required: the cancellation requires predicting the direction of the sensory change caused by movement, not just whether movement occurred. A predictor that only received z_self_prev (body state) would not have access to the directional content of what will change in the world — it could know that the agent moved but not which cells will enter the agent's view. Z_world_raw_prev, by contrast, contains the spatial layout of world content adjacent to the agent's current position, which is exactly what determines the direction and content of the visual change during locomotion.

The paper's formal interpretation — attenuation is proportional to prediction error — also maps onto a desirable property for SD-007: a well-trained ReafferencePredictor should produce near-zero residual after subtraction during normal locomotion, and larger residuals when unexpected world events coincide with movement.

## Limitations and caveats

Human tactile psychophysics with a robotic paradigm. The spatial correspondence manipulation in the tactile domain (rotating the direction of finger stroke) has a somewhat forced analogy to the visual domain (entering different cell content than expected). In the gridworld, the spatial aspect of the prediction is about which cell content enters view given the current world layout and the action — this is a richer spatial problem than a simple 2D direction rotation. Additionally, the parametric delay function found here (monotonic increase in perceived ticklishness with delay) would need to be separately established for visual reafference correction to directly constrain SD-007.

## Confidence reasoning

Confidence is 0.70. Good source quality (J Cogn Neurosci, behavioural, robust effects). Mapping fidelity is moderate-to-good: the paper provides specific support for two design choices in SD-007 (temporal alignment and the spatial/content information in the input). Transfer risk is the same as for Blakemore 1998 — tactile to visual gridworld. The key insight (that cancellation degrades gracefully with prediction error, and that spatial correspondence matters) is a meaningful additional constraint on SD-007's predictor design beyond what the 1998 paper provides.
