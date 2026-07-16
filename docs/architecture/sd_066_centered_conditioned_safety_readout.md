---
title: "SD-066: common-mode-invariant (centered) conditioned-safety readout"
nav_exclude: true
status: candidate/v3_pending
status_asof: 2026-07-16
status_claim: SD-066
---

# SD-066: common-mode-invariant (centered) conditioned-safety readout

**Claim ID:** SD-066
**Subject:** safety_prediction.common_mode_invariant_conditioned_safety_readout
**Registered:** 2026-07-15
**Status:** IMPLEMENTED (2026-07-15)
**Depends on:** SD-051 (ConditionedSafetyStore), SD-065 (safety cue channel), SD-008 (z_world differentiation -- the deficit this works around)
**Blocks:** MECH-304 promote-to-active behavioural falsifier (V3-EXQ-763)

## Problem

The MECH-304 behavioural promote-to-active gate (SD-051 `ConditionedSafetyStore`
+ SD-065 cue channel) hits a **substrate ceiling** that the representation-level
V3-EXQ-759 (rank/AUC) sidestepped but the behavioural gate cannot. Diagnosed
2026-07-15 (session infallible-perlman-a4f3fe) by driving the full teaching->test
loop on the SD-065 substrate:

- The store's release gate is `sigmoid(gain * cosine(z_world, prototype)) >
  safety_store_threshold`. With `gain=4`, `threshold=0.5` this is **cosine > 0**.
- Under **z_world under-differentiation (SD-008)** the untrained z_world encoder
  maps *every* input into a narrow ~0.99-cosine cone: measured
  `cos(cue, nocue) = 0.9884` and `cos(two different contexts) = 0.9950` -- i.e.
  ANY two z_world sit at cosine ~0.99. So once the prototype is non-empty the gate
  fires **unconditionally**, for cue-present AND cue-absent alike.
- The cue *is* a real, consistent signal (`cos(cue,nocue)` is reliably BELOW
  `cos(ctx,ctx)` -- the right sign) but only ~**0.006 in cosine**, below the
  absolute-threshold gate's resolution, and **more encoder warmup does not help**
  (nothing supervises the encoder to differentiate the passive cue). Behaviourally:
  arm A (store on, cue) and arm C (store on, NO cue at test) both release at 1.00,
  `sig(cue) = 0.981 ~ sig(nocue) = 0.982` -- the cue makes no marginal difference.

This is the SD-051 doc's V4-deferred "the V3 EMA prototype conflates any z_world
co-occurring with relief ... may generalise the safety prediction too broadly",
now confirmed at the behavioural level. The rank-based 759 AUC exploited the
0.006 signal (scale/common-mode invariant); the behavioural absolute-cosine gate
cannot.

## Solution

An **opt-in, non-parametric, common-mode-invariant readout** on the existing
`ConditionedSafetyStore` -- NOT the V4 trainable-contrastive-head build, which is
still deferred. The store maintains a slow EMA `baseline` of z_world (the shared
common-mode direction) and does BOTH prototype accumulation and querying on the
**centered residual** `z_world - baseline`:

- **Baseline** (`_baseline`): EMA over every waking `update()` tick at rate
  `baseline_alpha` (default 0.02). First tick seeds it; `sim_mode` ticks do not
  advance it (MECH-094). This is the common-mode estimate to subtract off.
- **Accumulation:** on a MECH-302 relief `event_fired` tick the prototype
  EMA-updates from `normalize(z_world - baseline)` -- the cue-carrying residual --
  instead of `normalize(z_world)`.
- **Query:** `cosine(z_world - baseline, prototype)` -> `sigmoid(gain * cos)`.

Because the common-mode is subtracted from both sides, the residual (which carries
the cue) dominates the cosine, so the gate can resolve cue-present from cue-absent.

Entirely internal to the store: `update()` already runs every tick from
`agent.sense()`, so the baseline EMA advances there with **no agent.py wiring
change**. `centered=False` (default) is **bit-identical** to the pre-SD-066 store
(a byte-for-byte reference re-implementation reproduces every `update()` return --
contract C1).

### Config (env/agent config, surfaced through REEConfig.from_dims)

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `safety_store_centered` | `False` | opt in to the centered readout (raw cosine when False) |
| `safety_store_baseline_alpha` | `0.02` | EMA rate for the common-mode baseline |

## Validation (failure-record -> success metric)

The failure record is the spike above: raw store `A(cue)` release == `C(nocue)`
release (both 1.00), `sig(cue) ~ sig(nocue)`. A "working" readout must make the
release CUE-SPECIFIC. With `safety_store_centered=True` on the identical
teaching->test loop (real store, via `from_dims`):

| seed | A(cue) release / sig | C(nocue) release / sig | A - C |
|------|----------------------|------------------------|-------|
| 0    | 1.00 / 0.934         | 0.00 / 0.484           | +1.00 |
| 1    | 1.00 / 0.704         | 0.00 / 0.173           | +1.00 |
| 3    | 1.00 / 0.939         | 0.03 / 0.469           | +0.97 |

Cue-present separates cleanly above the 0.5 gate; cue-absent stays below. The
ceiling is lifted. Formal end-to-end validation is V3-EXQ-763 (MECH-304
promote-to-active behavioural falsifier), queued against `safety_store_centered=True`.

## Backward Compatibility

`safety_store_centered=False` by default: `_baseline` is never touched, the
accumulation/query arithmetic is byte-identical to the pre-SD-066 store. Contract
suite `tests/contracts/test_sd066_centered_safety_readout.py` (5 contracts: raw
bit-identical + never-touches-baseline / baseline lifecycle + reset / common-mode
separation / sim_mode gate / config default) + full `pytest tests/` regression.

## Related Claims

SD-051 (the store this extends), SD-065 (the cue channel it resolves), MECH-304
(the behavioural gate it unblocks), SD-008 (the z_world under-differentiation this
works around -- a proper fix would differentiate z_world so the raw cosine spreads),
MECH-303 (sister contextual-safety pathway, the V3-EXQ-763 DV2 sparing control).

## What This SD Enables / does NOT claim

Enables the behavioural cue-specific conditioned-inhibition test (V3-EXQ-763) that
gates MECH-304 provisional->active. It is a **readout workaround for the SD-008
z_world common-mode**, not a representation fix: it does not improve z_world
differentiation itself, and it does not replace the V4 trainable-contrastive store
(still the sharper long-term answer where stable non-safety features co-occur with
relief). PROMOTES NOTHING on its own; a V3-EXQ-763 PASS is what moves MECH-304.
