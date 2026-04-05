# Feldman & Friston (2010): Attention, uncertainty, and free-energy

**Entry ID:** 2026-04-06_mech_123_precision_weighting_feldman2010
**Claim:** MECH-123 (REM recalibrates precision priors after content consolidation)
**Evidence direction:** supports | Confidence: 0.78

---

## What the paper argues

Feldman and Friston propose that attention is best understood as the brain's mechanism for inferring the precision -- the inverse variance -- of sensory prediction errors during hierarchical perception. This is not a peripheral claim about attentional gating but a foundational one about the architecture of inference itself: precision encodes the expected reliability of each signal channel, and this encoding is instantiated as the synaptic gain of the units reporting prediction errors at each level of the hierarchy.

The key computational claim for MECH-123 is what the paper implies about miscalibration. In their Posner cueing simulations, invalid cues cause the system to assign low precision to prediction errors from the target location. The physical stimuli are identical. The inference fails because the credibility weights -- not the evidence -- are wrong. This is not random noise but systematic distortion: incorrectly assigned precision weights produce biased inference in a predictable direction, amplifying signals from the expected channel and attenuating signals from the actual target.

## The mechanism and its implications

Precision is encoded as synaptic gain on prediction-error units. When the gain is high, prediction errors from that channel drive strong updates to internal representations; when low, the same errors produce weak updates. The framework demonstrates that biased competition, attentional capture, and speed-accuracy trade-offs all fall out naturally from this precision-as-gain architecture. Crucially, the paper shows that errors do not need to be small or ambiguous to be ignored: an error signal with correct content but wrong precision weight will not update inference effectively. The inference problem is being solved with the wrong parameters.

## Relevance to MECH-123's failure mode

MECH-123 describes a failure mode in which precision priors are not recalibrated between episodes: the agent enters each new episode with precision parameters tuned to the prior episode's statistics. Feldman and Friston establish why this is computationally costly. Precision is not a calibration refinement that operates after inference; it is the parameter that determines which evidence is treated as signal and which as noise. Stale precision priors from episode N mean that every prediction error encountered in episode N+1 is weighted by N's reliability estimates. In a contextually new episode, this systematically distorts the integration of early evidence -- the evidence that is most important for establishing which schemas and priors apply. The distortion is not random: it reflects N's statistics imposed on N+1's context.

## What this paper does and does not establish

Feldman and Friston establish the mechanism at the level of a single inference episode -- they do not study cross-episode precision transfer, and they do not discuss sleep. The connection to REM as the recalibration mechanism requires additional support (Hobson and Friston 2012 provides this, in targeted_review_sleep_phase_mechanisms). What this paper establishes is the foundational claim: precision is the controlling gate on evidence integration, not a downstream refinement, and wrong precision weights produce systematic inference distortions regardless of evidence quality. This is the precondition that makes MECH-123's failure mode consequential rather than merely inconvenient.

## Caveats

The mapping to MECH-123 is inferential in one step: the paper demonstrates that precision miscalibration within a single episode causes systematic inference errors; the claim that precision must be reset across episodes by a specific sleep mechanism requires the additional premise that precision parameters do not self-correct within the episode. This additional premise is biologically plausible (aminergic tone, which mediates precision, does not reset within a waking episode) but is not established by this paper alone. The specific REE parameters (precision_ema_alpha, commitment_threshold) have no named equivalents in this work.
