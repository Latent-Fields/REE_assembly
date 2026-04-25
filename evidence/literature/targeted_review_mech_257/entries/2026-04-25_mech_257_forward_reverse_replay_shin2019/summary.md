# Shin, Tang & Jadhav 2019 — Forward/Reverse Replay Mode Switching (MECH-257)

**Source:** Shin JD, Tang W, Jadhav SP. "Dynamics of Awake Hippocampal-Prefrontal Replay for Spatial Learning and Memory-Guided Decision Making." *Neuron* 104(6):1110–1125. DOI: 10.1016/j.neuron.2019.09.012

## What the paper did

Shin et al. recorded simultaneously from large ensembles of hippocampal CA1 neurons and dorsal mPFC neurons in rats throughout the full learning trajectory of a spatial alternation task. During pauses between behavioural runs, they tracked sharp-wave ripple-associated replay events and classified each as forward (same temporal order as experience) or reverse (reverse temporal order). The key innovation was continuous tracking of the same identifiable ensembles across sessions, allowing them to map how replay mode contributions change as a function of learning stage.

## Key findings relevant to MECH-257

The paper's central result is a learning-phase dissociation: reverse replay dominates early in learning (when the animal is assigning credit to recently-taken paths) and forward replay dominates late in learning (when the animal is prospectively planning future paths). Critically, the *same* hippocampal-prefrontal ensembles carry both replay types — the authors find opposing learning gradients for reverse and forward replay content within the same recorded populations. Hippocampal-prefrontal coordination was stronger during correct-path replay, and the coordinated replay distinguished the chosen path from alternative options, suggesting a role in memory-guided decision-making.

## Translation to MECH-257

MECH-257 claims that E2_x is a single substrate read in two modes: retrospective comparator (Mode 1, post-action residual computation) and prospective rollout-scoring (Mode 2, pre-action candidate evaluation). The Shin et al. result is the closest available single-substrate biological parallel: the same CA1 population supports both retrospective (reverse replay) and prospective (forward replay) processing, with a controller-like switch — the learning stage, which the authors interpret as reflecting a shift in behavioural policy from trial-and-error to memory-guided planning. The mode shift is not just theoretical but is reflected in opposing learning curves, implying that both modes run on shared circuit resources without mutual exclusion.

The prefrontal readout component is also relevant: MECH-257 requires a controller gating signal (MECH-094, ARC-023) to determine which mode is active. In Shin et al., the prefrontal ensemble reads out the hippocampal replay content preferentially for correct paths, which is consistent with a prefrontal arbitration role over which hippocampal mode is currently serving behaviour.

## Limitations and caveats

The paper cannot directly resolve whether the *same individual neurons* contribute to both replay modes (the opposing learning gradients are at the population level). Nor does it address sub-episode mode-switching — MECH-257 proposes moment-by-moment controller gating, whereas Shin et al. describe a learning-phase gradient. The sharpest gap is that REE's E2_x is a learned neural-network forward model trained on prediction error, not a place-cell assembly; whether the weight-sharing constraint (training for evaluator mode must not degrade comparator mode) holds in a deep learning substrate is the explicit falsifiability criterion MECH-257 sets for itself, and this paper cannot address it.

## Confidence

0.78. Strong empirical support from high-quality single-unit recording for the single-substrate-dual-mode biological architecture. Moderate mapping fidelity because the paper addresses place-cell replay, not a trained forward model, and the temporal scale of mode-switching (session-level vs moment-by-moment) differs.
