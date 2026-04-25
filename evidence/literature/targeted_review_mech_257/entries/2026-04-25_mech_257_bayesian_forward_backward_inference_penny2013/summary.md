# Penny, Zeidman & Burgess 2013 — Bayesian Forward-Backward Inference (MECH-257)

**Source:** Penny WD, Zeidman P, Burgess N. "Forward and backward inference in spatial cognition." *PLoS Computational Biology* 9(12):e1003383. DOI: 10.1371/journal.pcbi.1003383

## What the paper did

Penny et al. develop a unified probabilistic model of spatial cognition in which a single generative model supports all major computations via two inference directions: forward inference (computing likely future states given current position and action) and backward inference (computing optimal control signals given a desired future state). They map these abstract inference operations onto hippocampal electrophysiological phenomena: theta sequences are interpreted as forward inference over decision-point options; theta flickering as model selection between competing environmental hypotheses; and remote replay (preplay and awake replay) as backward inference to compute routes and motor control signals.

## Key findings relevant to MECH-257

The theoretical centrepiece is the demonstration that forward and backward inference can both be implemented over a *single shared generative model* — one set of transition probabilities and one emission model — without requiring architectural duplication. This is the computational proof-of-concept for MECH-257's core claim that E2_x need not split into E2_x_comparator and E2_x_evaluator; a single substrate can service both modes. Penny et al. further show that the *direction* of inference (forward vs backward) can be controlled by a single algorithmic switch — which maps naturally onto the MECH-257 claim that a controller signal (commitment boundary state, heartbeat phase) arbitrates between modes.

The biological mapping is also useful: theta sequences during active navigation correspond to evaluator mode (scanning ahead over candidate actions), while replay events correspond to comparator-like retrospective processing (the reverse replay interpretation) or future-path optimisation (forward replay). Together these cover both ends of what MECH-257 proposes as Mode 1 and Mode 2.

## Translation to MECH-257

MECH-257's falsifiability criterion is: *if training E2_x for both evaluator and comparator modes simultaneously degrades performance in at least one mode relative to a mode-split baseline, MECH-257 is refuted*. Penny et al. show that in a linear-Gaussian state-space model, the two inference directions share parameters without mutual degradation — providing theoretical grounding that the single-substrate architecture is sound in principle. The gap is that a deep neural network trained by gradient descent may suffer from conflicting gradient updates across the two modes (a form of catastrophic interference), which the linear-Gaussian model cannot predict.

## Limitations and caveats

This is a theoretical modelling paper; no wet-lab experiments were conducted. The linear-Gaussian framework is analytically tractable but may not capture the non-linear dynamics of E2_x. Transfer risk is moderate: the claim maps well at the level of computational structure but the implementation substrate (learned weights vs Bayesian filtering) is materially different. The biological mappings (theta = forward inference, replay = backward inference) remain interpretive rather than directly tested.

## Confidence

0.72. High conceptual mapping fidelity for the single-substrate-dual-inference claim. Confidence tempered by the paper's theoretical (not empirical) nature and the architectural gap between linear-Gaussian models and deep networks.
