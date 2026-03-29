# Cullen (2019): The neural encoding of self-generated and externally applied movement

**Claim tested:** MECH-101 -- z_world encoding requires reafference context to correctly attribute external vs. self-caused change

## What the paper did

Cullen's 2019 review synthesized research on how the nervous system distinguishes sensory signals caused by the animal's own movement (reafference) from those caused by external events (exafference). The review covers multiple sensory systems -- vestibular nuclei, cerebellum, and visual cortex (including MSTd) -- and traces the efference copy pathways by which forward models predict the sensory consequences of self-generated movement so they can be subtracted. The paper is particularly relevant to the visual system: Cullen reviews how MSTd uses an internal model of the current motor command (efference copy) combined with information about the visual scene to predict what optic flow pattern will result from the impending movement, and then uses that prediction to suppress the expected reafference, leaving the neural response selective for unexpected (externally-caused) visual motion.

## Key findings relevant to MECH-101

The finding that bears most directly on MECH-101 is that visual reafference cancellation in MSTd is scene-content-dependent. The predicted optic flow pattern depends not only on the body movement (heading direction, velocity) but on the 3D layout of the visual scene: the same head rotation produces different optic flow patterns depending on the depth structure of the environment. This means the forward model that generates the predicted reafference must have access to the current visual scene state, not just the motor command. Without scene context, the predicted reafference would be systematically wrong whenever the visual scene contains anything other than a flat fronto-parallel surface. Cullen's review documents that MSTd neurons indeed receive this combined signal -- motor command plus scene-conditioned visual prediction -- to produce accurate reafference cancellation.

## REE translation

MECH-101 makes precisely this claim for the ReafferencePredictor: it must receive z_world_raw_prev (the current scene state) in addition to the action to predict the z_world change caused by locomotion. The failure mode (MECH-101 notes.yaml, EXQ-027: R2=0.027 with z_self input alone) is the direct computational analog of what would happen if MSTd only received body-state input: the newly-revealed cell content entering the field of view cannot be predicted from body position alone, just as scene-content-dependent optic flow cannot be predicted from heading direction alone. The fix (z_world_raw_prev as input) is the computational analog of providing MSTd with the visual scene state for accurate reafference prediction.

## Limitations and caveats

The biological context (MSTd, continuous 3D visual motion, head rotation) is substantially richer than the REE grid-world context (local-view grid, discrete steps, cell content revealed/concealed by movement). The biological reafference cancellation operates on continuous visual streams with depth-structured optic flow; the REE implementation operates on discrete latent state transitions. The principle -- scene state is required for accurate reafference prediction -- generalizes cleanly across these contexts, but the implementation details do not map directly. A second caveat: Cullen's MSTd review focuses on the vestibular-visual interaction for self-motion perception, which is a somewhat different problem from the REE use case (world encoder attribution of agent-caused vs. external world changes for moral attribution purposes). The reafference principle is the same, but the downstream use of the cancelled signal differs between the biological and REE contexts.

## Confidence reasoning

Confidence is 0.80 -- this is the most direct single paper for MECH-101. The principle-level mapping is tight: scene-content-dependent reafference prediction is exactly what the ReafferencePredictor requires, and the failure mode when scene context is absent (uninformative prediction, R2=0.027) is exactly what Cullen's framework predicts would happen. The moderate caveats reflect the 3D-visual vs. discrete-grid implementation gap and the different downstream use of the cancelled signal. This paper, together with the REE experimental evidence (EXQ-021 PASS confirming z_world_raw_prev fixes the predictor), provides strong grounding for MECH-101.
