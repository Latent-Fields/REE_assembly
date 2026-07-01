---
title: "DR-13: z_self temporal depth (dedicated self-recurrence + E1-feedback anchor)"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 6
---

# DR-13: z_self temporal depth -- dedicated self-recurrence anchored by E1 feedback

**Claim ID:** (DR-13 audit item; v4_spec.md V4-2) -- owner node `self_model_v4:SELF-1`
**Unblocks:** the whole self_model_v4 cutover -- DR-10 (SELF-3, z_self in E3 viability),
DR-11 (SELF-5, z_self-domain goals), DR-12 already-built (SELF-4), and the INV-064
(SELF-7) maturational-stability gate. MECH-215 (self-model prerequisite for agentive
prediction) is the load-bearing scope claim.
**Subject:** latent_stack.self_recurrence (z_self temporal self-model)
**Status:** IMPLEMENTED 2026-07-01
**Generation:** v4 (off the V3 critical path; promotes nothing in V3; excluded from the V3 closure %)
**Depends on:** SD-005 (z_self/z_world split, implemented) -- z_self exists today as the
single-MLP + EMA body latent this SD upgrades.
**Blocks (until built):** SELF-3 (DR-10) and SELF-5 (DR-11) were blocked on exactly this
substrate build (see the 2026-07-01 IGW-165 reconcile of `self_model_v4:SELF-3`).

---

## Problem

DR-13 from `docs/architecture/v4_spec.md` V4-2: *"z_self temporal depth. Current z_self is
single hidden layer + EMA; needs recurrence or E1 feedback for a temporal self-model."*

V3 today: in `LatentStack.encode()`, `z_self = self_encoder(body_obs)` (an instantaneous
2-layer MLP over the body observation, post top-down + precision) is then temporally
smoothed by a **fixed-alpha EMA** against the previous z_self
(`z_self = alpha_self * z_self + (1 - alpha_self) * prev.z_self`, `alpha_self = 0.3`). A
fixed-decay EMA is a memoryless low-pass filter: it cannot *selectively* retain or gate
self-state, so z_self is an instantaneous body snapshot, not a stateful subject. Every
later self-model step needs a stable, inspectable, lesionable subject to attach to:

- **DR-10 (SELF-3)** needs "a stable z_self as the subject of viability planning" -- an
  instantaneous snapshot scores capacity/affect/damage at the current instant only, not as
  a *state*.
- **DR-11 (SELF-5)** self-state goals presuppose a scorable, persistent self.
- **INV-064 (SELF-7)** the maturational-stability gate can only assert self-stability if
  the self is a perturbation-isolable object whose stability can be measured.

## Solution

A **no-op-default HYBRID lever** in `LatentStack.encode()` that, when
`use_self_recurrence` is on, **replaces the z_self EMA step ONLY** (z_world / z_beta /
z_theta / z_delta smoothing untouched) with:

1. **A dedicated gated self-recurrence** -- `SelfRecurrenceCell`
   (`ree_core/latent/self_recurrence.py`), a `GRUCell(self_dim -> self_dim)` whose hidden
   state is the previous stateful z_self and whose input is the current instantaneous
   encoded z_self. The gate lets the self-state selectively retain history a fixed-alpha
   EMA cannot. It is explicit / inspectable / **lesionable** (swap -> identity, or flag
   off) / **perturbation-isolated** (only z_self flows through the cell, so an experiment
   can perturb the self subject without touching z_world -- verified: a +5.0 perturbation
   of `prev.z_self` changes the stateful z_self and leaks 0.0 into z_world).

2. **An E1 generative-feedback anchor** -- the recurrent output is blended toward E1's
   generative prediction of z_self:
   ```
   h = SelfRecurrenceCell(z_self_instant, prev.z_self)
   z_self = (1 - c) * h + c * self_e1_anchor        # if anchor present and c > 0
          = h                                        # otherwise (pure recurrence)
   ```
   with `c = self_recurrence_e1_coupling`. This keeps the self-latent consistent with the
   E-stream generative account of the body rather than drifting into a parallel
   self-model. `c` is **the recorded residual sub-question** (ARC-081 notes 2026-06-14):
   `c = 0` is pure recurrence (Option A, maximal stability-isolation), `c = 1` is pure
   E1-feedback (Option B), the **light default `c = 0.15`** is the hybrid leaning to
   recurrence.

### The E1 anchor source (v1 scope decision)

The anchor is the **E1 predicted-next z_self**, cached at the E1 tick and consumed on the
next `encode()`. `_e1_tick` already runs the E1 forward (`predictions [batch, horizon,
total_dim]`) but discarded `predictions`; when `use_self_recurrence` is on the agent caches
`split_prediction(predictions[:, 0, :])[0].detach()` as `self._e1_predicted_next_z_self`,
and `sense()` threads it into `encode(self_e1_anchor=...)` -- exactly the
`volatility_signal` plumbing precedent. **Side-effect-free**: no extra E1 forward, no LSTM
hidden-state mutation. First tick has no cache -> anchor `None` -> pure recurrence that one
step. This mirrors the DR-12 v1 "caller/agent-supplied signal, ecological auto-source
deferred" decision and keeps DR-13 a lever on existing machinery.

### Config (all no-op default; bit-identical OFF)

| Param | Type | Default | Purpose | Class |
|-------|------|---------|---------|-------|
| `use_self_recurrence` | bool | `False` | master switch (DR-13) | LatentStackConfig (+ `from_dims`) |
| `self_recurrence_e1_coupling` | float | `0.15` | E1-anchor blend weight (the residual tunable) | LatentStackConfig |

With `use_self_recurrence=False`, `self_recurrence` is **not instantiated** (mirrors
`reafference_predictor`), so the OFF path draws no new parameters and runs the verbatim
legacy EMA -> bit-identical.

### Diagnostics (LatentState.self_recurrence_diag)

Plain-float dict `{active, state_departure (||stateful z_self - instantaneous z_self||,
batch-mean), e1_coupling, anchor_present}`. `None` when OFF. `state_departure` is the DR-13
non-vacuity readout -- how much temporal state the stateful z_self carries beyond the
instantaneous encode; a validation experiment's "buys nothing" off-ramp fires if it stays
~0 (the recurrence collapsed to the instantaneous snapshot).

## Phased training

The `GRUCell` is a new trainable element in the z_self recognition path; it trains via the
**existing** E1/E2 z_self prediction losses -- v1 adds **no new loss** (the anchor is an
inference-time blend, detached). Standard joint-collapse awareness applies (a recurrence
can collapse to identity or drift); the E1 anchor defends against drift, and the validation
falsifier pre-registers the collapse/inert off-ramp. Experiments that train the recurrence
should follow the usual P0 encoder-warmup -> P1 frozen-encoder phasing.

## MECH-094

N/A -- this is the waking perception path (`encode`/`sense`/`_e1_tick`), not
replay/simulation. No `hypothesis_tag` write surface is added.

## What this enables / the falsifier

**FALSIFIER (V4-EXQ, queued separately):** ON vs OFF; if the dedicated self-recurrence does
NOT make z_self carry temporal/self-model state beyond the EMA snapshot (state_departure
~0, or lesioning the recurrent hidden state leaves the stateful z_self unchanged), DR-13
buys nothing over the EMA and the recurrence is inert. Pre-registers a non-vacuity gate
(state_departure > floor on a majority of divergent seeds; else
`substrate_not_ready_requeue`) and an inert/collapse off-ramp. PASS = the stateful z_self
is a genuine, perturbation-isolable subject the DR-10/DR-11/INV-064 steps can attach to.

## Architecture context

- **SD-005** split encoder produces the instantaneous z_self this SD upgrades; the EMA it
  replaces is the SD-008 `alpha_self` smoothing (z_world's `alpha_world` EMA is untouched).
- **E1** (`E1DeepPredictor`) is the generative account of `[z_self, z_world]`; DR-13 uses
  its z_self prediction as the anchor, so the self-model stays E-stream-native.
- **DR-12 (SELF-4)** wires E2-forward-PE -> E3 confidence and stays E-stream-native; it
  does not depend on a stateful z_self. DR-13 is the substrate half; together with DR-10
  (SELF-3) they unblock MECH-215.
- **INV-064 (SELF-7)** maturational-stability gate: the dedicated recurrence is what makes
  the self a stability-isolable subject the gate can test.

## ML/AI engineering parallel (Layer 7)

Two moves, both engineering counsel only (the architecture is set by the SD + biological
grounding, not derived from ML):
- **Gated recurrent cell for temporal integration.** A GRU is the standard fix for a
  fixed-decay integrator that cannot selectively retain (the EMA); its gates solve
  vanishing/over-smoothing at low dimension. REE adaptation: minimal single cell at
  self_dim (no extra hidden dim), per the REE small-MLP convention.
- **Posterior<->prior consistency (RSSM / world-models).** Anchoring a recurrent latent to
  a generative prior to prevent drift is the world-model KL-to-prior idea; DR-13 uses a
  **hard inference-time blend** (coupling `c`) rather than a KL/ELBO term, grounded
  neuroscientifically (the self-model must track the E-stream body account). Hazards
  defended: collapse-to-identity (falsifier off-ramp) and runaway/drift (the E1 anchor).

## Related claims

ARC-081 (self-as-object pillar / architectural_commitment -- the DR-13 mechanism was
resolved on its notes 2026-06-14; stays candidate/v4), MECH-215 (unblocked half; stays
candidate/v4), SD-005 (the split z_self this upgrades), DR-10/SELF-3 (z_self-in-E3, the
sibling half of the MECH-215 unblock, was blocked on this build), DR-12/SELF-4 (E2-PE ->
E3, already built), INV-064/SELF-7 (maturational-stability gate), MECH-094 (N/A -- waking
path, no replay write surface).
