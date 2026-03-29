# Von Holst and Mittelstaedt (1950): Das Reafferenzprinzip (The Reafference Principle)

**Claim tested:** MECH-101 -- z_world encoding requires reafference context to correctly attribute external vs. self-caused change

## What the paper did

Von Holst and Mittelstaedt published a theoretical and experimental account of how the nervous system distinguishes sensory signals caused by the animal's own movement from those caused by the external environment. Working with insects and fish, they documented a range of behavioral phenomena -- flies that can no longer stabilize their flight when their head is glued in place; fish that spiral when their tail-fin feedback is inverted -- and proposed a unified explanatory framework. The key concept is the Efferenzkopie (efference copy): when the motor system generates a command, it sends a copy of that command to the sensory processing system. This copy is used to generate an expectation of what sensory signals will arrive as a consequence of the movement (the expected reafference). The actual sensory signal is compared with this expectation; the matching part -- the predicted reafference -- is cancelled, and only the unmatched residual (the exafference -- environmentally-caused signals) passes through to higher-level processing.

## Key findings relevant to MECH-101

The reafference principle establishes the computational problem MECH-101 addresses: z_world must not respond to sensory change caused by the agent's own locomotion (reafference) but must respond to changes caused by the environment (exafference). Without this distinction, z_world conflates the agent's movement through the world with things changing in the world -- a confusion that would make causal attribution (who caused this harm?) impossible. Von Holst's framework says: use the motor command (efference copy) to predict the expected sensory consequence, then subtract it. The residual is attributed to external events. MECH-101's ReafferencePredictor implements this computationally.

## REE translation

The REE ReafferencePredictor takes (z_world_raw_prev, a_t) and predicts the locomotion-caused component of delta_z_world_raw. This is the efference copy computation: a_t is the motor command, and the prediction is the expected reafference. Subtracting this from the actual delta_z_world_raw leaves the exafferent component -- changes in the world not caused by locomotion. MECH-101's specific contribution beyond the basic von Holst principle is the claim that z_world_raw_prev is required in addition to a_t, because the reafference in a local-view grid is scene-content-dependent: the new cells that enter the field of view depend on what is adjacent in the world, not just on the direction of movement. This is an extension of the reafference principle to the case where the expected reafference is a function of both motor command and current scene state.

## Limitations and caveats

Von Holst's original formulation assumes the efference copy (motor command alone) is sufficient to predict the expected reafference. This is appropriate for the cases he studied (fly visual stabilization, where the optic flow pattern depends mainly on heading direction). MECH-101 extends this by requiring scene-state input (z_world_raw_prev) for accurate prediction, which is a non-trivial extension. The von Holst principle motivates the architecture -- there should be a reafference prediction and cancellation step -- but does not directly support the specific scene-context requirement. That requirement is grounded in the grid-world geometry (local view, new cell content on locomotion) and supported by the experimental failure (EXQ-027, R2=0.027 with z_self alone) and fix (EXQ-021 PASS with z_world_raw_prev). Von Holst 1950 is also a pre-computational era paper with no quantitative neural data; it is a theoretical framework, not a mechanistic characterization.

## Confidence reasoning

Confidence is 0.75. The reafference principle is the foundational concept behind MECH-101 and maps cleanly at the level of the core computation (predict self-caused change, subtract it, what remains is external). The confidence is not higher because the specific scene-context extension is not in the original principle -- it is a MECH-101 addition -- and the paper provides theoretical framing rather than experimental measurement. Together with Cullen 2019 (which provides the neural mechanistic evidence that scene context is required in MSTd) and the REE experimental evidence, this paper anchors the theoretical foundation of MECH-101.
