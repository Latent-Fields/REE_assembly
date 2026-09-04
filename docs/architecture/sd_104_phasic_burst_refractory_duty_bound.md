# SD-104: phasic.burst_refractory_duty_bound

**Claim ID:** SD-104
**Subject:** control_plane.phasic_burst_refractory_duty_bound
**Status:** IMPLEMENTED
**Registered:** 2026-09-04
**Depends on:** SD-069, SD-075, MECH-063
**Blocks:** V3-EXQ-963b (MECH-063 sub-claim ii retest), SD-069 validation

Leg (a) of substrate_queue entry `sd_phasic_burst_decay_and_warmup_headroom`
(priority 1, severity `degrading`), created by governance `governance-20260903T2013`
from the confirmed autopsy
`REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-963a_2026-09-02.md`.
Leg (b) is [SD-105](sd_105_selection_entropy_headroom_floor.md); the two are
coupled and the autopsy's re-derive brake requires BOTH before any further
963-lineage letter.

## Problem

SD-069 `PhasicSurpriseBurst` re-arms its envelope with `max(decayed, drive)` on
every firing tick. On a **warmed** agent (SD-074 `probe_warmup`) with
`signal_source="instantaneous_pe"`, `trigger_ratio=1.2`, `decay=0.5`, the raw
per-tick PE clears `trigger_ratio * EMA` on most ticks, so a fresh event lands
before the previous one has decayed and the envelope never returns to zero.

Measured, V3-EXQ-963a vs V3-EXQ-779a (identical burst config, colder agent):

| seed | 963a T0P1 | 963a T1P1 | 779a T0P1 | 779a T1P1 |
|---|---|---|---|---|
| 11 | 0.546 | 0.496 | 0.083 | 0.132 |
| 17 | 0.647 | **0.847** | 0.085 | 0.076 |
| 23 | 0.390 | **0.884** | 0.012 | 0.007 |
| 29 | 0.513 | 0.480 | 0.072 | 0.079 |
| 37 | 0.466 | 0.501 | 0.136 | 0.105 |

Seed 23 T1P1 fired on 1489 of 1684 selections. A "transient" occupying up to
88% of ticks is a quasi-sustained regime: the MECH-063 (ii) tonic-vs-phasic
dissociation has no separable transient left to measure, which is why C2's
dominance clause failed by 5-13x and why the single quiescent-tick shortfall
existed at all.

**This is regulator behaviour, not sampling.** Raising `MAX_ENV_STEPS_PER_CELL`
cannot reach it, and the autopsy's re-derive brake explicitly REFUSES a
963-lineage successor that tries.

## Solution

Two coupled knobs on `PhasicSurpriseBurstConfig`, both no-op by default so
SD-069/SD-075 behaviour is bit-identical.

| Param | Type | Default | Purpose |
|---|---|---|---|
| `phasic_burst_refractory_ticks` | int | `0` | after an event fires, suppress further firing for this many subsequent waking ticks; the envelope keeps decaying throughout (carry-mode decay) |
| `phasic_burst_extinction_level` | float | `0.0` | envelope level strictly below which the burst snaps to exactly `0.0` |

Module: `ree-v3/ree_core/regulators/phasic_surprise_burst.py` (extends SD-069
and SD-075 in the same file, following the SD-075 precedent).

### The guarantee

Together the realised burst-active duty cycle is bounded **by construction** --
the property the autopsy asked to be ASSERTED rather than hoped for:

```
A     = 1 + floor( ln(extinction_level) / ln(1 - decay) )     # decay < 1; else 1
duty <= min(1.0, A / (refractory_ticks + 1))
```

`A` is the most consecutive active ticks one event can produce (the injection
drive is capped at 1.0); at most one event can fire per `refractory_ticks + 1`
ticks; overlaps only shrink the union. `get_state()` reports
`burst_duty_cycle_bound`, `realised_burst_duty_cycle`,
`max_active_ticks_per_event` and `burst_duty_cycle_within_bound`, so a manifest
records the guarantee instead of a later reader re-deriving it.

**Neither knob alone suffices.** A refractory without extinction leaves a
geometrically-decaying tail that never reaches zero, so "active" depends on the
consumer's own floor (963a's driver used `EVENT_LEVEL_FLOOR = 0.05` and could
not know whether the regulator agreed) and the bound is unprovable. Extinction
without a refractory still permits re-arming on the very next tick.

### The refractory counter is LIFETIME and CARRIES across `reset()`

Found by the build's own smoke test, not by reasoning: with the counter cleared
per episode, a refractory of 29 and extinction 0.05 (bound 0.167) produced a
realised duty cycle of **0.311** over 61 lifetime ticks of short episodes. Every
episode boundary re-armed immediate firing, so the realised duty cycle was again
a function of episode LENGTH -- the exact V3-EXQ-779b confound SD-075 exists to
close, reappearing on a new axis -- and the lifetime bound was false.

The envelope itself IS still cleared at `reset()`, so no in-flight burst leaks
across an episode boundary; only the refractory owed does. Biologically this is
the faithful reading: LC refractoriness is a property of the neurons, not of the
behavioural episode.

### Deliberately NOT built

A duty-cycle **target** with a controller that tunes the refractory to hit it.
The closed-form bound is a hard ceiling, which is what an assertion needs; a
controller would make the realised duty cycle a function of the surprise stream
again -- the exact property that made 963a unmeasurable.

## Architecture Context

Pure-arithmetic regulator, no `nn.Module`, no learned parameters, no gradient
flow (same category as MECH-313 `noise_floor`, SD-037 `broadcast_override`,
SD-069 itself). **Phased training does not apply.** **MECH-094**: the existing
`simulation_mode` contract is extended to the new counters -- replay/DMN content
advances no SD-104 counter and consumes no refractory tick.

Suggested operating point for a warmed agent at `decay=0.5`,
`EVENT_LEVEL_FLOOR=0.05`: `extinction_level=0.05`, `refractory_ticks=29`
(A = 5, bound = 0.167). Measured on a broad heavy-firing surprise stream (1000
ticks, uniform(0,10)): realised duty **0.788** with the knobs at defaults versus
**0.109** ON -- the OFF configuration reproduces the 963a regime (0.390-0.884)
and the ON configuration lands inside 779a's healthy band (0.007-0.136).

A caution for anyone writing a probe here, because it cost this build a red
contract: a CONSTANT spike stream is the wrong adversary. Its EMA converges to
the spike, so `trigger_ratio * ema` overtakes the spike and firing stops on the
TRIGGER test within ~30 ticks (measured duty 0.016) -- the refractory is never
exercised at all.

## What This SD Enables

- V3-EXQ-963b: the MECH-063 (ii) tonic/phasic dissociation retest, admissible
  only once the burst is shown to decay on a warmed agent.
- SD-069's own validation (its transient claim is untestable while the
  transient is quasi-sustained).

## Related Claims

MECH-063 (sub-claim ii), SD-069, SD-075, SD-074, MECH-313, MECH-104 (shared lit
basis, different consumer), [SD-105](sd_105_selection_entropy_headroom_floor.md).

## Contracts

`ree-v3/tests/contracts/test_sd104_sd105_burst_decay_and_entropy_headroom.py`
(A1-A11). A6 is the positive control: it fails if the OFF configuration stops
reproducing the 963a regime, so the suite cannot pass on a regulator that simply
never fires.
