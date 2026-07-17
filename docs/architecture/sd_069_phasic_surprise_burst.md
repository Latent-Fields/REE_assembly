# SD-069: control_plane.phasic_surprise_burst

**Claim ID:** SD-069
**Subject:** control_plane.phasic_surprise_burst
**Status:** IMPLEMENTED
**Registered:** 2026-07-17
**Depends on:** MECH-313 (stochastic_noise_floor, tonic), ARC-005, MECH-063
**Blocks:** MECH-063 sub-claim (ii) behavioural validation (tonic-vs-phasic dissociation)

## Problem

MECH-063 ("Control plane retains orthogonal tonic/phasic axes rather than
collapsing into one scalar", `docs/architecture/control_plane.md#mech-063`)
has two sub-claims:

1. **Orthogonal axes** -- the control plane exposes several independent axes
   (precision, delay-tolerance, interrupt/volatility, ...) rather than one
   scalar. Covered behaviourally by V3-EXQ-777
   (`ree-v3/experiments/v3_exq_777_mech063_orthogonal_control_axes_dissociation.py`).

2. **Tonic/phasic split** -- *each* axis carries BOTH a slow **tonic baseline**
   AND a fast **phasic event-burst** as independent degrees of freedom.

Sub-claim (ii) could not be tested behaviourally because the V3 substrate had
**no toggleable phasic event-triggered control lever that routes to action
selection**. A full substrate scan (2026-07-17) confirmed:

- **MECH-104 volatility-surprise spike** was DOCUMENTED but UNIMPLEMENTED as a
  substrate module -- no regulator class, no `use_*` flag. It existed only as
  prose in `ree_core/policy/noise_floor.py` and `structured_curiosity.py`, and
  was faked inside experiments by directly mutating `agent.e3._running_variance`
  (e.g. `experiments/v3_exq_062_mech104_surprise_gate.py`). That poke routes to
  the ARC-016 commit/de-commit gate (`e3_selector.py`), NOT to the softmax
  `score_bias` / `temperature` that MECH-063's tonic levers use.
- **MECH-287 InvalidationTrigger** is genuinely phasic/event-triggered but
  routes exclusively to hippocampal MECH-284 staleness / MECH-269 anchor reset
  -- never to the E3 softmax.
- **Every actual E3-softmax control input is tonic or continuous**: MECH-313
  noise_floor (tonic temperature), MECH-320 tonic_vigor (EWMA score bias),
  MECH-314 structured_curiosity, dACC anti-recency.

There was therefore a tonic lever on the softmax (MECH-313) with **no phasic
counterpart on a comparable readout**, so tonic-vs-phasic could not be
dissociated behaviourally.

## Solution

A toggleable, pure-arithmetic **phasic** regulator -- the LC-NE phasic
complement to MECH-313 `noise_floor` (tonic) on the **same E3 softmax
temperature channel**.

Module: `ree-v3/ree_core/regulators/phasic_surprise_burst.py`
(`PhasicSurpriseBurst` / `PhasicSurpriseBurstConfig`). Matches the pure-scalar
regulator pattern of `ree_core/policy/noise_floor.py` (MECH-313) and
`ree_core/regulators/broadcast_override.py` (SD-037): no `nn.Module`, no
learned parameters, no gradient flow.

**Relationship to MECH-104 (do not conflate).** This regulator reuses the
MECH-104 volatility-surprise **lit basis** (LC-NE phasic burst on
unexpected/surprising events; Aston-Jones & Cohen 2005 adaptive-gain model,
phasic mode). It does NOT implement the MECH-104 **claim**. The active,
evidenced MECH-104 claim (`control_plane.volatility_interrupt`, v3_exq_365) is
the volatility spike routing to the ARC-016 commit / de-commit gate. SD-069
routes the same surprise event to the E3 **selection** softmax temperature
instead -- the tonic/phasic axis of MECH-063, NOT the commit gate. Same
biological substrate, same source signal, different consumer.

**Data flow:**

```
<surprise source: e3._running_variance OR e3.last_instantaneous_pe>
  -> PhasicSurpriseBurst.tick(surprise)
       event iff surprise >= trigger_ratio * max(ema_baseline, trigger_floor)
       on event: inject drive in [0,1] from normalized surprise excess
       envelope = max(decayed_prev, drive); decay geometrically each tick
  -> burst_level in [0,1]  (spikes on event, decays over a few ticks)
  -> temperature_delta = temp_delta * burst_level   (default NEGATIVE = sharpen)
  -> combined_T = max(tonic_effective_T + temperature_delta, min_temperature)
  -> e3.select(candidates, combined_T)   [agent.py select_action]
```

The tonic MECH-313 lift is applied first (sustained, every tick); SD-069 adds
an **event-locked transient** on top. Both act on the effective softmax
temperature -> **comparable readouts, independently toggleable**. Default
`temp_delta` is NEGATIVE: a phasic burst transiently **sharpens** the softmax
(LC-NE phasic gain increase; "phasic mode gates committed exploitation", the
reading `noise_floor.py` already commits to). Sign and magnitude are
config-exposed; the load-bearing property for MECH-063 (ii) is that the phasic
contribution is EVENT-LOCKED and TRANSIENT, versus the tonic lift's sustained
every-tick offset.

**Config (REEConfig; all no-op defaults; bit-identical OFF):**

| Param | Default | Purpose |
|-------|---------|---------|
| `use_phasic_burst` | `False` | master switch (agent does not instantiate when False) |
| `phasic_burst_surprise_ema_decay` | `0.1` | EMA rate for the surprise baseline (~20-tick) |
| `phasic_burst_trigger_ratio` | `1.5` | event fires at >= ratio x baseline |
| `phasic_burst_trigger_floor` | `1e-6` | absolute baseline floor (no fire on ~0 noise) |
| `phasic_burst_temp_delta` | `-0.5` | temperature delta at full burst (negative = sharpen) |
| `phasic_burst_decay` | `0.5` | geometric per-tick decay of the envelope |
| `phasic_burst_min_temperature` | `0.1` | strict-positive floor on the combined temperature |
| `phasic_burst_signal_source` | `"running_variance"` | event-detector source signal; `"instantaneous_pe"` for the sharp source (see below) |

### Sharp-surprise source (2026-07-17)

The event detector's source signal is selectable so the phasic lever can fire on
**real, non-synthetic** surprise events:

- **`"running_variance"`** (default, no-op): reads the SMOOTHED `e3._running_variance`
  EMA -- the original wiring. Empirically that accumulator **decays monotonically**
  for an untrained forward model (0.475 -> 0.004) and washes out real per-tick PE
  spikes, so the lever fires **0 natural events** even with env volatility enabled
  (`CausalGridWorldV2 background_drift_enabled=True, n_drift_sources=3,
  drift_policy=random_walk`). A no-training 777-style probe on this source therefore
  self-routes `substrate_not_ready_requeue` -- it can only exercise the lever with a
  synthetic poke to `_running_variance`, which is exactly what the MECH-063 (ii) test
  must avoid.
- **`"instantaneous_pe"`**: reads a new read-only signal `e3.last_instantaneous_pe` =
  the RAW per-tick PE-MSE (`error_var` in `e3.update_running_variance`) captured
  BEFORE the running-variance EMA smoothing folds it in. Genuine surprise spikes
  survive, so the lever fires on real events. Grounded in the MECH-104 lit basis
  (Aston-Jones & Cohen 2005 phasic mode fires on **sharp/instantaneous** salience, not
  a smoothed average). The detector keeps its own EMA baseline + relative-ratio
  trigger, so a sharp single-tick input still produces a clean event.

`e3.last_instantaneous_pe` is written **unconditionally** by `update_running_variance`
(a pure additive no-op accumulator) and read **only** by the phasic-burst source branch
in `REEAgent.select_action` when `phasic_burst_signal_source == "instantaneous_pe"`, so
the default keeps existing experiments bit-identical. An invalid source string raises
`ValueError` at agent construction (no silent fallback to the smoothed source).

**Validation (untrained rollout, drift on, no synthetic poke).** Under
`"instantaneous_pe"` the phasic burst is ACTIVE across the run (burst_ticks up to
209/232 at trigger_ratio 1.3), while under `"running_variance"` it is NEVER active
(0/217) -- a clean load-bearing contrast. The regulator's `n_events` counter resets per
episode (`agent.reset -> phasic_burst.reset`), so a readiness gate must sum events
across episodes rather than read the end-of-run `get_state`. Full validation: V3-EXQ-779
(MECH-063 sub-claim ii dissociation).

**Diagnostic (telemetry probe).** `phasic_burst_level` and
`phasic_burst_temp_delta` are surfaced in `agent._last_score_bias_decomp`
(alongside `noise_floor_temp`), and a `phasic_burst` block
(`temp_delta` / `burst_level` / `present`) is added to
`agent._last_control_vector` (alongside `noise_floor_temp_lift` /
`tonic_vigor_v_t`). The tonic lift readout is kept **uncontaminated** by the
phasic transient so the dissociation is directly readable from a manifest.

**MECH-094.** `simulation_mode=True` returns the cached burst unchanged and
does NOT advance the EMA baseline, envelope, or counters (replay / DMN content
must not trigger waking phasic arousal). No memory write surface, no encoder
head -> **phased training NOT required**, and MECH-094 `hypothesis_tag` is
not applicable (nothing is written to memory).

## Architecture Context

SD-069 is the phasic sibling of MECH-313 on the E3 selection softmax. Together
they instantiate the MECH-063 tonic/phasic decomposition on one axis (the
precision/vigor axis, dopamine/LC-NE-like), making the two components
independently toggleable levers on the same effective-temperature readout.
MECH-320 `tonic_vigor` provides the alternative tonic lever on the per-candidate
`score_bias` channel; SD-069 routes to the temperature channel to pair cleanly
with MECH-313 (the noise_floor docstring already names MECH-104 as its phasic
complement).

## What This SD Enables

- **MECH-063 sub-claim (ii)** behavioural validation: a genuine tonic-vs-phasic
  dissociation experiment (777-harness pattern) where the tonic lever
  (MECH-313 noise_floor) moves a sustained/baseline readout and the phasic lever
  (SD-069) moves an event-locked transient readout, on comparable softmax
  temperature / precision readouts.

## Related Claims

MECH-063 (tonic/phasic split, the claim this SD enables), MECH-313
(stochastic_noise_floor, the tonic counterpart), MECH-104
(volatility_interrupt, shared lit basis / different consumer -- commit gate),
ARC-005 (control plane), MECH-287/288 (the other phasic event stream, routed to
hippocampal staleness).
