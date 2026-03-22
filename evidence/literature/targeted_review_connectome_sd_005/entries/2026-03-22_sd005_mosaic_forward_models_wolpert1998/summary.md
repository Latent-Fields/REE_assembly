# Literature Summary: 2026-03-22_sd005_mosaic_forward_models_wolpert1998

## Claims Tested

- `SD-005`

## Source

- Wolpert DM, Kawato M (1998). *Multiple paired forward and inverse models for motor control*. Neural Networks, 11(7-8): 1317-1329.
- DOI: `10.1016/S0893-6080(98)00066-5`
- URL: `https://www.sciencedirect.com/science/article/pii/S0893608098000665`

## Source Wording

Motor control is decomposed into a MOSAIC (MOdular Selection And Identification for Control) architecture of multiple paired forward and inverse models. Each forward model receives an efference copy of the current motor command and predicts the sensory consequences of self-generated movement. This forward prediction is used to cancel the reafferent signal -- the sensory input caused by the agent's own movement. What remains after cancellation is the exafferent signal: sensory change attributable to the external world, not to the agent's own action. The forward model is trained on self-motion prediction error and does not update on externally caused sensory change. A gating network selects among modules based on contextual state estimates.

## REE Translation

**SD-005 (z_self/z_world split)**: The MOSAIC forward model is the established biological/computational antecedent of z_self. It encodes the predicted sensory consequences of self-generated action -- an efference copy stream that tracks what the body did and what sensory outcome that should produce. Critically, it does not encode world state: it updates only on self-motion prediction error. The residual exafferent signal -- sensory input that the forward model cannot account for by self-action -- is the antecedent of z_world: the channel encoding changes in the environment not caused by the agent.

In REE architecture: E2 operating on z_self (motor-sensory prediction, proprioceptive stream) and E3/hippocampus operating on z_world (exteroceptive residue, harm/goal attribution) mirrors the forward-model/exafferent-residual decomposition. The biological machinery for this split already exists at the cerebellar-parietal level; SD-005 proposes that the same factorisation should be reflected at the conceptual-sensorium (z_gamma) level in V3.

This also bears on MECH-069 (incommensurable error signals): forward-model prediction error (z_self domain) and exafferent-residual error (z_world domain) are structurally distinct -- the forward model cannot be trained on exafferent signals without corrupting the self-model, and vice versa. This is not a design preference but a functional necessity.

## Caveat

MOSAIC is a model of low-level sensorimotor control (reaching, tool use, limb dynamics). The z_self/z_world split in SD-005 operates at the level of z_gamma -- a higher-order conceptual sensorium, not raw sensory streams. Extrapolating from cerebellar efference copy to latent-space separation at the planning level involves a meaningful abstraction. The source supports the functional principle (self-caused vs world-caused signal factorisation) but does not directly evidence a high-level latent split. The 1998 MOSAIC paper proposes the modular architecture; more recent neuroimaging work (Imamizu et al. 2003, Nat Neurosci) provides evidence for the neural substrate, but that is a separate citation.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.80`
