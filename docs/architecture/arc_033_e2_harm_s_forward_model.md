# ARC-033: E2_harm_s Sensory-Discriminative Harm Forward Model

**Claim ID:** ARC-033
**Subject:** harm_stream.sensory_discriminative_forward_model
**Status:** IMPLEMENTED
**Registered:** 2026-03-24
**Implemented:** 2026-04-09
**Depends on:** SD-010, SD-011, ARC-027
**Blocks:** SD-003 counterfactual harm attribution pipeline

## Problem

SD-003 self-attribution requires counterfactual harm queries: "what harm would have
occurred if I had taken a different action?" The original SD-003 design used a
HarmBridge projector (z_world -> z_harm) to compute counterfactuals. This is
architecturally infeasible:

- EXQ-093/094 confirmed bridge_r2=0: z_world perp z_harm by construction (SD-010)
- SD-010 deliberately separates the harm stream from the world stream; HarmBridge has
  nothing to learn because the streams share no information by design
- EXQ-094 confirmed training E3 on bridge noise produced 100x regression in harm_var

Additionally, the original single z_harm stream conflated two functionally distinct
nociceptive signals. SD-011 (EXQ-178b PASS) confirmed dual-stream separation into:
- z_harm_s: sensory-discriminative (Adelta-pathway analog) -- immediate proximity,
  forward-predictable from action
- z_harm_a: affective-motivational (C-fiber analog) -- accumulated homeostatic
  deviation, NOT counterfactually modeled

The z_harm_s stream supports a learnable forward model because hazard proximity
has predictable action-conditional structure: moving away from a hazard
reduces proximity in a deterministic, action-dependent way.

## Solution

E2HarmSForward: a dedicated learnable forward model f(z_harm_s_t, a_t) -> z_harm_s_{t+1}.
Analogous to E2FastPredictor.world_forward() but operating on the sensory-discriminative
harm stream. Implemented as ResidualHarmForward in ree_core/latent/stack.py (2026-04-09:
also wrapped in dedicated module ree_core/predictors/e2_harm_s.py).

Key architectural decision: **residual delta** rather than direct next-state prediction.
Identity collapse affects direct predictors on autocorrelated signals (r~0.9 for z_harm_s).
Predicting the delta forces the network to learn change structure (approach increases
proximity, retreat decreases it) rather than outputting the identity mapping.

EXQ-166e PASS confirmed the harm-delta architecture (delta_r2=0.641, causal_gap_approach=0.005).
EXQ-195 confirmed harm_forward_r2=0.914 -- the forward model component works. The
attribution_gap failure in EXQ-195 was classified non-contributory (SD-003 pipeline
wiring incomplete, not ARC-033 failure).

### Redesigned SD-003 Pipeline (post-SD-011)

```
z_harm_s_cf = E2HarmSForward(z_harm_s_t, a_cf)
causal_sig  = E3.harm_eval_z_harm(z_harm_s_actual) - E3.harm_eval_z_harm(z_harm_s_cf)
```

This operates entirely within the harm stream. No cross-stream bridge required.

## Architecture Context

E2HarmSForward is NOT part of the E2FastPredictor. It is a separate module that:
- Takes z_harm_s (from HarmEncoder/SD-010) as input
- Takes action_onehot as input (same encoding as E2.world_forward)
- Predicts z_harm_s_{t+1} via residual delta

Training protocol (phased):
- P0: HarmEncoder warmup (z_harm_s encoder trains on proximity supervision)
- P1: E2HarmSForward trains on frozen z_harm_s targets (stop-gradient on z_harm_s inputs)
- P2: Evaluation

Stop-gradient on z_harm_s during forward model training prevents the HarmEncoder from
drifting to make predictions trivially easy (representation collapse). The harm stream
is low-variance compared to z_world -- small learning rate (5e-4) recommended.

## What This Enables

SD-003 full counterfactual harm attribution pipeline:
- z_harm_s_cf = E2HarmSForward(z_harm_s, a_cf) for any counterfactual action a_cf
- causal_sig = E3(z_harm_s_actual) - E3(z_harm_s_cf)
- This gives E3 a mechanism to distinguish agent-caused harm from environment-caused harm

Note: z_harm_a (affective-motivational, SD-011) does NOT need a forward model. It feeds
E3 commit gating directly as motivational urgency (not used in counterfactuals).

## Module Location

```python
# Primary implementation (residual delta architecture):
from ree_core.latent.stack import ResidualHarmForward

# Dedicated wrapper with config (ARC-033):
from ree_core.predictors.e2_harm_s import E2HarmSForward, E2HarmSConfig

# Deprecated (identity collapse):
# from ree_core.latent.stack import HarmForwardModel  -- do not use
```

Configuration in config.py: E2HarmSConfig (standalone) or via
LatentStackConfig.use_e2_harm_s_forward (disabled by default, backward compatible).

## ML Engineering Notes

- Stop-gradient on z_harm_s inputs to forward model during training (prevent encoder drift)
- Small learning rate (5e-4, cf. E2 self forward model 3e-4)
- Residual delta architecture (not direct next-state) -- see ResidualHarmForward docstring
- Phased training required: P0 encoder, P1 forward model, P2 eval
- MECH-094: not applicable (waking forward model, not replay content)
- Identity collapse risk: mitigated by residual delta + stop-gradient

## Biological Grounding

Keltner et al. (2006, J Neurosci): predictability suppresses sensory-discriminative
pain activity (S1/S2). The brain models expected nociceptive consequences of voluntary
movement and cancels predicted input -- the efference copy mechanism applied to the
spinothalamic nociceptive pathway. This cancellation is NOT available for the affective
stream (ACC/insula integrates homeostatic context beyond single actions).

The existence of predictive cancellation in S1/S2 but not ACC provides direct biological
evidence that the sensory-discriminative stream (z_harm_s) supports a forward model while
the affective stream (z_harm_a) does not. E2HarmSForward is the REE implementation of
this predictive nociceptive mechanism.

## Validation Experiment

V3-EXQ-264: ARC-033 E2_harm_s forward model validation (queued 2026-04-09)
- Two conditions: E2_harm_s enabled vs disabled
- Metrics: forward_r2, z_harm_s_pred_norm, harm_s_cf_gap
- 3 seeds, phased training (P0 100ep + P1 50ep)

## Related Claims

- SD-003: self_attribution.counterfactual_e2_pipeline (unblocked by ARC-033)
- SD-010: harm_stream.nociceptive_separation (prerequisite)
- SD-011: harm_stream.dual_nociceptive_streams (prerequisite -- z_harm_s stream)
- ARC-027: harm_stream.parallel_thalamic_pathway (prerequisite)
- MECH-112: approach_avoidance.go_channel (downstream -- benefit-side counterpart)
- ARC-030: approach_avoidance.symmetric_evaluation (downstream)
