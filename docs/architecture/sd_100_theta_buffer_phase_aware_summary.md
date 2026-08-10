---
status: candidate
status_asof: 2026-08-10
status_claim: SD-100
---

# SD-100: hippocampal.theta_buffer_phase_aware_summary

**Claim ID:** SD-100
**Subject:** hippocampal.theta_buffer_phase_aware_summary
**Registered:** 2026-08-10
**Depends on:** MECH-089 (theta-cycle cross-rate batching -- this SD replaces its summary
  mechanism, does not add a new one), SD-006 (multi-rate clock -- owns `theta_buffer_size`)
**Blocks:** ARC-032 (theta-rate frontal-hippocampal goal-context communication -- gated on this
  fix per `failure_autopsy_V3-EXQ-228c_2026-08-10.md` routing), MECH-089 itself (the
  context-gated-redesign line its own `what_would_answer` has left open since EXQ-066/EXQ-122)

## Problem

`failure_autopsy_V3-EXQ-228c_2026-08-10.md` found that V3-EXQ-228c -- the first fair,
E3-tick-restricted, direct-DV test of ARC-032 -- failed both primary criteria with a **reversed**
trend: theta ACTIVE was measurably *noisier* than theta bypassed (`noise_delta_mean=-0.0671`)
and showed no persistence benefit (`persist_delta_mean=4.47e-07`). The autopsy's four-layer
diagnosis registered this as `implementation: partial` (biology-divergence gap), not a claim
falsification: `docs/architecture/approach_avoidance_symmetry.md#arc-032`'s frontal-hippocampal
theta-synchrony hypothesis (Sigurdsson et al. 2010) predicts *degradation* under a broken theta
channel, not a null/reversed result, so a null/reversed result under the AS-IMPLEMENTED channel
argues against the implementation, not the architecture.

This converges with two of MECH-089's own confirmed findings, independent of ARC-032:
EXQ-066 (batched E3 prediction error 2.28x worse than raw) and EXQ-122 (harm_auc delta=-0.135,
adverse direction) both showed static/uniform theta-averaging measurably *hurts* E3's
fine-grained discrimination. MECH-089's `what_would_answer` has named a "context-gated redesign"
as the open line since 2026-03-28 and it has not been built.

`ThetaBuffer.summary()` (`ree_core/latent/theta_buffer.py`) computes a flat, unweighted mean over
the last `theta_buffer_size` (default 10) E1 `z_world` estimates. A flat mean is **permutation
invariant** over the window: two theta cycles containing the same set of world-states in a
different order produce an identical summary. Dragoi & Buzsáki 2006 (theta-sequence compression)
and Colgin et al. 2016 (theta-gamma phase nesting) both attribute theta's functional payload
specifically to *within-cycle ordinal/phase structure*, not to a rate-coded average -- place-cell
ensembles fire in a temporally compressed replay of the upcoming/recent trajectory once per theta
cycle, and information carried at different theta phases is functionally distinct (not
interchangeable). The flat mean is a formal-definition-style stand-in ("average the theta window")
for a biologically load-bearing structural property ("where in the cycle it happened"), and per
SD-003 precedent this divergence is treated as load-bearing, not a caveat.

## Solution

### Mechanism: forward-sweep phase-weighted summary

Replace (behind a flag) the flat mean with a **fixed, non-parametric, order-sensitive** weighted
sum. This is deliberately *not* a trained encoder: the engineering problem here is "make the
aggregator order-sensitive," not "learn a representation," so a closed-form fixed kernel avoids
committing to phased P0/P1/P2 training (Step 3e) for a change whose payload is structural, not
statistical, and keeps the mechanism at REE's usual 2-3-line-transform scale rather than
importing ImageNet/LLM-scale complexity for a 10-step window (Layer 7 "do not over-engineer").

For a buffer holding `T` entries (oldest -> newest, `T <= theta_buffer_size`), assign each
position `t` (`0`-indexed) a phase within the **forward half-cycle**:

```
phase_t = pi * t / (T - 1)            # 0 (oldest) .. pi (newest); T==1 -> phase_t = pi
```

A half-cycle (`[0, pi]`), not a full `2*pi` wraparound, is deliberate: Dragoi 2006's compression
sweep runs once, forward, per cycle -- it does not wrap the oldest and newest samples back
adjacent to each other the way a literal `2*pi` phase would. Weight is a von-Mises-style kernel
centred on the read-out phase (cycle completion, i.e. "now" = the newest sample):

```
log_w_t = -kappa * cos(phase_t)       # kappa = theta_phase_concentration (config, default 4.0)
w        = softmax(log_w)             # normalises the kernel over the T positions actually present
summary  = sum_t w_t * z_world_t
```

`-cos` is strictly monotonically increasing over `[0, pi]`, so `w_t` is strictly monotonically
increasing in recency: the mechanism is a **legitimate phase-readout kernel**, not an arbitrary
recency bias, and it degrades gracefully to the current behaviour: at `kappa=0`, `log_w_t=0` for
every `t`, `softmax` returns the uniform distribution `1/T`, and the summary is mathematically
identical to the existing flat mean. The implementation nonetheless keeps the OFF path as the
original `.mean(dim=0)` call unchanged (rather than routing through `kappa=0`) so the no-op case
is **bit-identical**, not merely equivalent up to softmax's floating-point rounding.

Because weights are strictly monotonic and distinct per position, any two windows containing the
same multiset of `z_world` values in a **different order** produce a **different** summary
(unless the reordering happens to swap two positions holding numerically identical vectors) --
this is precisely the permutation-sensitivity a flat mean cannot provide by construction, and is
exercised directly by `test_theta_buffer_phase_aware_summary.py::test_reordering_changes_summary`.

### Scope: `summary()` only, not `self_summary()` or `consolidation_summary()`

`summary()` (E1 `z_world` -> E3) is the exact site the failure record and MECH-089's own
`what_would_answer` implicate. `self_summary()` (E1 `z_self` -> E2) and `consolidation_summary()`
(MECH-122 Phase-3 offline cx->hip packaging, already order-sensitive via its own linear-decay
weighting) are separate consumers with no failure record entry; extending the same treatment to
them is plausible follow-on but out of this SD's scope (`REE_Working/CLAUDE.md` Scope Discipline).

### Config

```python
# ree_core/utils/config.py, HeartbeatConfig (co-located with theta_buffer_size)
use_theta_phase_weighted_summary: bool = False   # master switch; False = bit-identical flat mean
theta_phase_concentration: float = 4.0           # von-Mises kappa; only read when the switch is True
```

Exposed through `REEConfig.from_dims(...)` as `use_theta_phase_weighted_summary` /
`theta_phase_concentration` kwargs, mirroring the existing `breath_period`-style HeartbeatConfig
exposure pattern (`from_dims` writes `config.heartbeat.<field>` directly).

### Data flow

```
E1 z_world estimate (per env step)
    -> ThetaBuffer.update()                          [unchanged]
    -> ThetaBuffer.summary()                          <- THIS SD
         OFF (default): stacked.mean(dim=0)            [bit-identical to pre-SD-100]
         ON:  softmax(-kappa*cos(phase_t)) weighted sum over the current window
    -> agent.py:5359 z_world_for_e3 = theta_buffer.summary()
    -> E3 trajectory scoring / proposal generation      [unchanged consumer, same [batch, world_dim] shape]
```

### Backward compatibility

`use_theta_phase_weighted_summary` defaults to `False`. With the default, `ThetaBuffer.summary()`
executes the exact pre-existing code path (`torch.stack(...).mean(dim=0)`) -- no new tensor ops
run, no new attributes are read on the hot path. `theta_phase_concentration` is inert whenever the
switch is off. No existing config field's default changes. `self_summary()` and
`consolidation_summary()` are untouched.

### ML/AI engineering notes (Layer 7)

Core engineering problem: make an order-invariant aggregator (mean-pooling over a fixed window)
order-*sensitive* without adding trainable parameters. The closest ML parallel is fixed sinusoidal
positional encoding (Vaswani et al. 2017) added to pooled features before mean-pooling; the
REE-specific adaptation here folds the position signal directly into the pooling *weights*
(a phase-indexed attention kernel with no learned parameters) rather than concatenating a
positional feature vector, because the consumer (E3) requires the output to stay at `world_dim`
width -- concatenation would change that shape and ripple through every E3 config that assumes
`world_dim`-wide `z_world`. No numerical-stability concerns beyond the ordinary `softmax`
guarantees (bounded, sums to 1, no gradient path since `ThetaBuffer.update()` already calls
`.detach()` on its inputs). No new trainable parameters -> no phased-training requirement
(Step 3e does not apply). No MECH-094 relevance -- this changes an aggregation function, not
simulation/replay content (Step 3f does not apply).

## Architecture Context

Sibling to `consolidation_summary()`'s existing linear-recency weighting (MECH-122, cx->hip
direction) -- both are V3 proxies for a fuller bidirectional, genuinely phase-tagged ThetaBuffer
(deferred to V4, per `consolidation_summary()`'s own docstring). This SD is the hip->cx
(`summary()`, E3-facing) counterpart getting the same order-sensitivity `consolidation_summary()`
already has, using a phase-motivated kernel rather than a plain linear ramp so the weighting has
an explicit circular/phase reading (Colgin 2016) rather than being framed as generic recency bias.

## What This SD Enables

Clears MECH-089's own `what_would_answer` context-gated-redesign line (a phase-weighted kernel is
a form of non-uniform, context-independent-but-position-sensitive gating; a fully context-gated
variant, as EXQ-066/EXQ-122's "reading (2)" speculates, remains a distinct, larger follow-on).
Unblocks a re-test of ARC-032 (`/queue-experiment` V3-EXQ-228d, recommended not queued by this
session) with theta ACTIVE now representing genuine within-cycle structure instead of a flat
average, addressing the biology-divergence gap the 228c autopsy identified rather than the
frontal-hippocampal-synchrony hypothesis itself.

## Related Claims

ARC-032, MECH-089, MECH-116 (E1 goal maintenance -- the upstream signal theta-packages),
MECH-122 (`consolidation_summary()`, the sibling cx->hip weighting).
