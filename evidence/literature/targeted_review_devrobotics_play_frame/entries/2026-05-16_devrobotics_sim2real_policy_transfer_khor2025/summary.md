# Summary: Post-Convergence Sim-to-Real Policy Transfer

**Entry ID:** 2026-05-16_devrobotics_sim2real_policy_transfer_khor2025
**Claim IDs:** MECH-195, MECH-196, INV-059

## What the paper does

Khor and Weng (2025, arXiv) address the problem of which trained policy to deploy after RL convergence when multiple near-optimal policies are available. They observe that naive selection by simulated performance is a poor predictor of real-world performance (Spearman rank correlation SCC ~0.25). They propose a worst-case performance optimization approach -- formulated as a convex quadratic-constrained linear programming problem -- that improves SCC to ~0.55 without requiring the sim-real gap to be small. Theorem 1 formally establishes that policy structural robustness and absolute reward magnitude are independent.

## Key findings

The key formal result for REE is the demonstrated and proven dissociation between policy ranking (strategy structure) and absolute reward magnitude. A policy can be structurally robust (maintains high rank across dynamics perturbations) while having poorly calibrated absolute reward predictions. Conversely, a policy that achieves high reward in simulation may have that reward magnitude mediated by simulator-specific calibration that does not transfer.

The Spearman rank correlation metric provides an implementable test for calibration leak: if policy performance in the source domain (play / simulation) is predictive of performance ranking in the target domain (real) in the rank-order sense, strategy has transferred. If the correlation is weak but improves when worst-case weighting is applied, the naive correlation was being driven by calibration-mediated outliers.

## REE mapping

This maps to MECH-195 (strategy transfers, calibration re-anchors) and provides an operational metric for the DEV-NEED-011 constructive play gate. The gate should test whether E3 trajectory competence rankings in play episodes predict trajectory competence rankings in real episodes, using rank correlation rather than absolute performance correlation. If they do, strategy has transferred independently of synthetic signal magnitudes.

MECH-196's safety property (frame collapse -> immediate recalibration) has a direct analogue: the worst-case optimization approach assumes the sim-real gap could be large at any moment, so it maintains worst-case-robust policies rather than calibration-optimistic ones. The recalibration trigger in REE corresponds to the moment of transition between the synthetic domain and the real domain.

## Limitations and caveats

Preprint, not peer-reviewed. The dynamics mismatch in robotics sim-to-real is mechanistically different from REE's deliberate synthetic reward signals -- the former involves wrong physics, the latter involves authorized-synthetic learning within a frame tag. The Spearman correlation metric measures policy ranking consistency but not the specific E3 trajectory structure vs z_goal/z_harm magnitude dissociation REE requires. Direct application needs REE-specific operationalization.

## Confidence reasoning

Confidence 0.62: preprint status and moderate mapping fidelity limit confidence. The formal theorem and the SCC metric are the most directly applicable computational results for MECH-195 available in the current literature, but require adaptation.
