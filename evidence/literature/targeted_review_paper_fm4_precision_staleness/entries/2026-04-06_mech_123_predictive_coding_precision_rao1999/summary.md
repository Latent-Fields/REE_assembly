# Rao & Ballard (1999): Predictive coding in the visual cortex

**Entry ID:** 2026-04-06_mech_123_predictive_coding_precision_rao1999
**Claim:** MECH-123 (REM recalibrates precision priors after content consolidation)
**Evidence direction:** supports | Confidence: 0.68

---

## What the paper argues

Rao and Ballard propose that the visual cortex implements hierarchical predictive coding: feedback connections from higher to lower cortical areas carry top-down predictions, while feedforward connections carry the residual errors between those predictions and the actual lower-level activations. The model accounts for a range of extra-classical receptive field effects (end-stopping, non-classical surround suppression) as natural consequences of this architecture.

The critical formalism for MECH-123 is their explicit treatment of precision weights. Both the top-down prediction and the bottom-up error signal are weighted by the inverse of their respective noise variances before entering the update equations. This is formally equivalent to a Kalman filter: the precision of each source determines how much authority it is granted in resolving conflicts between expectation and observation. High-precision priors (low top-down noise variance) suppress prediction errors; high-precision likelihoods (low bottom-up noise variance) drive strong updates from incoming evidence.

## The structural implication for cross-episode staleness

The Rao-Ballard architecture makes explicit that the relative authority of top-down expectations versus bottom-up sensory evidence is not fixed but parameterized by noise variance estimates. These estimates must reflect the actual reliability of each source in the current context to produce accurate inference. When noise variance estimates are mismatched to the current context -- when the system believes its predictions are more reliable than they are, or less reliable -- inference is systematically biased in a predictable direction.

This is the foundational structural claim that MECH-123's failure mode 4 builds on. If precision parameters (noise variance estimates) are calibrated to episode N's context and applied unchanged to episode N+1, the system enters N+1 with the wrong authority ratio between expectation and evidence. The top-down channel may be granted too much authority (if N was a familiar, predictable context and N+1 is genuinely novel) or too little (the reverse). Either way, the first prediction errors arriving in N+1 -- the most important ones for re-establishing contextual inference -- are weighted incorrectly.

## Why this is not merely a small calibration error

The Rao-Ballard formalism clarifies why the failure accumulates. Precision weights operate before inference, not after it. They determine which error signals are treated as signal and which as noise from the outset. Early prediction errors in N+1, weighted with N's precision parameters, do not merely produce slightly incorrect updates; they shape the context estimate that determines how all subsequent errors will be weighted. If the first evidence in N+1 is under-weighted because N's precision parameters grant too much authority to prior expectations, the system fails to update its context estimate. Later evidence then encounters the same stale precision parameters -- the miscalibration is self-reinforcing, not self-correcting.

## Caveats and scope

Rao and Ballard are studying within-episode visual inference. The cross-episode staleness problem and the sleep recalibration mechanism are not discussed. Their noise variance parameters (Sigma_td, Sigma_bu) encode static properties of the generative model learned over development, not the dynamic within-session precision parameters that MECH-123 claims REM recalibrates. The transfer from visual feedforward/feedback dynamics to REE's precision_ema_alpha, commitment_threshold, and harm_weight parameters requires bridging through Friston's free-energy framework (which unifies Rao-Ballard predictive coding with Bayesian inference under uncertainty).

This paper is best understood as providing the structural foundation for why precision miscalibration is computationally consequential -- a prerequisite for MECH-123's failure mode argument -- rather than as direct evidence for the sleep-dependent recalibration claim.
