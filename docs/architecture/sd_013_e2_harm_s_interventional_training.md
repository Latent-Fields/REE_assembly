# SD-013: E2_harm_s Interventional Training

**Claim ID:** SD-013  
**Subject:** self_attribution.e2_harm_s_interventional_training  
**Status:** IMPLEMENTED 2026-04-10  
**Registered:** 2026-03-28  
**Depends on:** SD-003, SD-011, ARC-033  
**Blocks:** SD-003 z_harm_s counterfactual attribution pipeline (causal_sig validity)

---

## Problem

A forward model trained on observational trajectories learns the correlational distribution
`P(z_harm_s_next | z_t, a)`, not the interventional distribution `P(z_harm_s_next | do(a))`
(Scholkopf et al. 2021). These diverge in confounded states: environments where agent
presence correlates with ambient harm independently of the agent's causal contribution.

In such states, `E2_harm_s` trained purely observationally encodes the correlation, not
the causal mechanism. Consequence: `causal_sig = E2(z_t, a_actual) - E2(z_t, a_cf)`
will underestimate the agent's causal contribution (both terms are biased upward in
confounded states, compressing the difference).

The forward model must be trained to produce **divergent** outputs for different actions,
not merely accurate outputs for the observed action. Without this, the model may learn
action-invariant harm representations that produce near-zero counterfactual gaps.

---

## Solution

Add a **contrastive interventional loss** to E2HarmSForward training. For each training
step, sample a counterfactual action `a_cf != a_actual` from the action space. Compute:

```
z_pred_actual = E2HarmSForward(z_harm_s_t, a_actual)   [standard MSE target]
z_pred_cf     = E2HarmSForward(z_harm_s_t, a_cf)        [counterfactual]
```

Add a margin loss that pushes the two predictions apart:

```
interventional_loss = max(0, margin - ||z_pred_actual - z_pred_cf||_2)
```

This has zero gradient when the predictions are already `>= margin` apart, and positive
gradient when they are too similar. Combined with the standard reconstruction loss, the
model learns both accuracy (fit observed transitions) and action-sensitivity (different
actions produce different harm predictions).

### Config params (E2HarmSConfig)

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `use_interventional` | bool | `False` | master switch |
| `interventional_fraction` | float | `0.3` | fraction of batches adding contrastive loss |
| `interventional_margin` | float | `0.1` | L2 separation margin |

### New method: `E2HarmSForward.compute_interventional_loss()`

```
compute_interventional_loss(z_harm_s, a_actual, a_cf) -> Tensor
```

Computes the margin loss for one training step. `a_cf` must be a different one-hot action.
The caller is responsible for providing `a_cf != a_actual` and for applying stop-gradient
on encoder inputs (same phased training discipline as the standard forward model).

---

## Architecture Context

SD-013 is a **training procedure extension** to ARC-033 (E2HarmSForward), not a new
module. The architecture is unchanged; only the loss function gains an additional term.

E2HarmSForward (ARC-033) already provides `counterfactual_forward(z_harm_s, a_cf)` for
the SD-003 attribution pipeline. SD-013 ensures the underlying model is properly trained
to make that counterfactual meaningful.

The phased training protocol from ARC-033 still applies:
- P0: HarmEncoder warmup (z_harm_s learns to represent sensory harm)
- P1: E2HarmSForward trains on frozen z_harm_s -- standard MSE + interventional margin
- P2: Evaluation (harm_forward_r2 + causal_sig_gap)

---

## What This SD Enables

- SD-003 causal_sig is meaningful: `E2(a_actual) - E2(a_cf)` reflects genuine causal
  sensitivity, not noisy near-zero compression artifacts.
- Discriminative pair experiments: INTERVENTIONAL vs OBSERVATIONAL conditions can measure
  whether action-sensitivity of E2 output translates to better causal attribution.

---

## Related Claims

- SD-003 (self_attribution.counterfactual_e2_pipeline)
- ARC-033 (harm_stream.sensory_discriminative_forward_model)
- SD-011 (harm_stream.dual_nociceptive_streams)
- MECH-071 (E2 harm calibration asymmetry)

---

## ML/AI Engineering Notes

**Engineering problem:** Training a forward model to be action-sensitive, not just accurate.

**Technique adopted:** Contrastive margin loss (Hadsell et al. 2006; SimCLR-style
contrastive divergence). The REE adaptation differs from standard contrastive learning:
we push apart predictions for *different actions from the same state*, not different
augmentations of the same sample. The biological grounding (Scholkopf 2021 causal
identifiability) motivates why action-sensitivity is required, not just accuracy.

**Known failure mode:** If `interventional_margin` is set too high, the model may ignore
the reconstruction objective and learn action-dependent but inaccurate representations.
Mitigation: keep margin small (0.1 << typical z_harm_s scale) so reconstruction still
dominates. The contrastive term acts as a regulariser, not the primary signal.

**Backward compatibility:** All new params default to no-op (False / 0.0). Existing
experiments using E2HarmSForward are unaffected.
