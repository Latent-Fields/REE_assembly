---
status: candidate/v3_pending
status_asof: 2026-09-05
status_claim: SD-105
---

# SD-105: control_plane.selection_entropy_headroom_floor

**Claim ID:** SD-105
**Subject:** control_plane.selection_entropy_headroom_floor
**Registered:** 2026-09-04
**Depends on:** SD-074, MECH-313
**Blocks:** V3-EXQ-963b (MECH-063 sub-claim ii retest), and any readout of E3
selection entropy taken on a warmed agent

Leg (b) of substrate_queue entry `sd_phasic_burst_decay_and_warmup_headroom`
(priority 1, severity `degrading`), from the confirmed autopsy
`REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-963a_2026-09-02.md`.
Leg (a) is [SD-104](sd_104_phasic_burst_refractory_duty_bound.md).

## Problem

The SD-074 `probe_warmup` exists to bring the agent to a non-degenerate E3
action-value landscape before telemetry is collected. It succeeds -- and in
succeeding it produces a **confident** policy, which has almost no selection
entropy left to move.

T0P0 (tonic OFF, phasic OFF) `S_sustained_entropy`, against the R5 band
(0.02, 0.98):

| seed | 963a | 779a |
|---|---|---|
| 11 | 0.0611 | 0.2979 |
| 17 | **0.0195** | 0.5108 |
| 23 | 0.1530 | 0.6095 |
| 29 | 0.1154 | 0.2784 |
| 37 | 0.0771 | 0.1523 |

A 3-26x collapse on **every** seed. The R5 headroom gate is pinned at its 0.02
floor reproducibly; seed 17 is the tail of a systematic collapse, not a fluke.

Worse than the gate failing: the phasic lever SHARPENS (`temp_delta` negative by
default), so a baseline sitting at 0.0195 leaves ~2% of the readout's range for
the manipulation to move into. A null measured there says nothing about the
mechanism -- it says the readout had nowhere to go. That is the
**anti-conservative** direction `experiments/_lib/entropy_headroom.py` already
warns about: floor/ceiling compression biases a difference-of-arms readout
toward zero, which is fatal exactly when the adjudication rests on a null.

## The choice the autopsy left open, and why this branch

The autopsy required: *"either the warmup must leave headroom or R5's band must
be re-derived for warmed agents; state which and why."* **This SD takes the
first branch.** Re-deriving the band is REJECTED, for two reasons.

1. **It would let the gate pass while the condition it detects is untouched.**
   R5 is not an arbitrary threshold; it is the assertion that the DV has dynamic
   range. Lowering `E_SAT_LOW` to admit 0.0195 converts an artifact into a
   citable result -- the warning `experiments/_lib/precondition_gate.py` already
   carries, and the same failure the `dv-dynamic-range-precondition-class`
   harness gate (ree-v3 `8e133d26ed`) was built to catch from the other end. A
   criterion whose bar sits outside the DV's achievable range is not a weaker
   criterion; it is an unmeasurable one.
2. **The collapse is a property of any sufficiently trained policy**, not of one
   warmup recipe. Repairing it inside `probe_warmup` would be a per-experiment
   band-aid the next lineage rediscovers the first time it warms an agent by
   some other route. The headroom belongs where the temperature is set.

## Solution

New module `ree-v3/ree_core/regulators/selection_entropy_floor.py`
(`SelectionEntropyFloor`). A **one-sided integral controller in
log-temperature** -- a tonic behavioural-variability set-point.

| Param | Type | Default | Purpose |
|---|---|---|---|
| `use_selection_entropy_floor` | bool | `False` | master switch |
| `selection_entropy_floor_target` | float | `0.15` | target normalized entropy H/ln(K); inside the R5 band and inside 779a's healthy 0.152-0.610 |
| `selection_entropy_floor_gain` | float | `0.5` | integral gain per tick on the entropy error |
| `selection_entropy_floor_max_temperature_ratio` | float | `8.0` | hard cap on the multiplier |
| `selection_entropy_floor_ema_decay` | float | `0.2` | smoothing on the realised-entropy estimate |
| `selection_entropy_floor_deadband` | float | `0.05` | one-sided band above target; no chatter |

Mechanism, per waking tick:

1. Read the realised normalized entropy `H(p)/ln(K)` of the **previous** tick's
   E3 pre-commit distribution (`e3.last_precommit_probs`). Previous, because
   this temperature is an INPUT to the current tick's softmax -- one tick of
   lag, deliberately slow.
2. `h_ema = (1 - a) * h_ema + a * h_t`.
3. `h_ema < target` -> `log_mult += gain * (target - h_ema)`;
   `h_ema > target + deadband` -> `log_mult -= gain * (h_ema - target - deadband)`;
   otherwise unchanged. Clamp `log_mult` to `[0, ln(max_temperature_ratio)]`.
4. Emit `multiplier = exp(log_mult) >= 1.0`.

### Data flow

```
temperature -> MECH-313 noise_floor -> [SD-105 multiplier] -> SD-069 phasic delta -> e3.select()
```

Applied on the **tonic** side, before the phasic delta, so the phasic
contribution stays an ADDITIVE delta in absolute temperature units on top of a
lifted baseline (rescaling it would compress the event-locked transient the
MECH-063 (ii) readout is measuring). Because the floor is enabled identically in
every arm of a tonic contrast, both arms lift together: `dS_tonic` is preserved
rather than compressed, which is the point.

`noise_floor_temp` in the control vector deliberately keeps reporting the
**pre-multiplier** tonic value, so the MECH-313 readout stays uncontaminated;
the multiplier is reported separately as `_last_control_vector["entropy_floor"]`
(`temp_mult`, `temp_lift`, `observed_entropy`, `entropy_ema`, `headroom_met`,
`saturated`, `present`).

### Two properties that are load-bearing, not incidental

**One-sidedness.** The multiplier never falls below 1.0: the floor can only ADD
exploration, never remove it. A controller allowed below 1.0 would be a general
entropy REGULATOR -- it would clamp the readout from both sides, destroying
exactly the dynamic range this exists to protect, and would silently cancel a
tonic manipulation trying to raise entropy.

**The cap reports rather than hides.** When the scores are so peaked the target
is unreachable, the controller saturates and says so (`saturated`). A consumer
finding `headroom_met` False with `saturated` True has learned something real --
the policy is too confident for this readout at this budget -- and should
declare the cell UNINFORMATIVE rather than reporting the compressed number as a
measurement.

### The EMA and integrator SURVIVE `reset()`

This is the opposite of SD-069's default, and deliberate: a set-point that
re-converges from cold at every episode boundary measures episode LENGTH rather
than the policy's confidence, so a seed with short episodes would get a
systematically different lift from a seed with long ones -- the V3-EXQ-779b
confound on a new axis. `get_state()` carries `continuity_note:
"ema_and_integrator_survive_reset"` because a reader is entitled to be
surprised. Use a fresh instance for a fresh lifetime.

## Architecture Context

Pure-arithmetic regulator, no `nn.Module`, no learned parameters, no gradient
flow (same category as MECH-313 `noise_floor` and SD-069). **Phased training
does not apply.** **MECH-094**: `simulation_mode=True` returns the cached
multiplier and advances neither the EMA, the integrator, nor any counter --
replay/DMN content must not move the waking exploration set-point.

Relationship to MECH-313: `noise_floor` adds a state-INDEPENDENT constant
temperature lift; SD-105 is the state-DEPENDENT form that holds realised
variability at a floor however peaked the scores have become. Biological
reading: preserved behavioural/motor variability in the trained animal, a tonic
set-point rather than a constant offset.

## What This SD Enables

- V3-EXQ-963b: an R5 headroom gate that a warmed agent can actually clear, with
  the bar declared inside the DV's achievable range
  (`dv-dynamic-range-precondition-class`).
- Any future readout of E3 selection entropy taken after a warmup.

## Related Claims

MECH-063 (sub-claim ii), MECH-313, SD-069, SD-074, SD-075,
[SD-104](sd_104_phasic_burst_refractory_duty_bound.md).

## Contracts

`ree-v3/tests/contracts/test_sd104_sd105_burst_decay_and_entropy_headroom.py`
(B1-B10).
