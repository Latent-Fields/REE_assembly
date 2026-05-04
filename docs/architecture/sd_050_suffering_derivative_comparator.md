# SD-050: relief.suffering_derivative_comparator

**Claim ID:** SD-050
**Subject:** relief.suffering_derivative_comparator
**Status:** IMPLEMENTED
**Registered:** 2026-05-04
**Depends on:** SD-011 (z_harm_a affective stream), MECH-057a (commitment-release pipeline), MECH-091 (salient-event phase-reset), MECH-094 (categorical tag write)
**Blocks:** MECH-302 (relief-completion event substrate), MECH-303 (safety-cue prediction teaching signal)

## Problem

REE's goal-completion pipeline (MECH-057a beta-gate drop + MECH-091 phase-reset + MECH-094
VALENCE_LIKING write) fires on goal-attainment events. There is no architecturally analogous
event for the end of a period of suffering: avoidance commitments accumulate during harm, but
no clean "relief completion" event closes the episode and tags what just worked. This leaves
MECH-302 untestable -- the claim that the same downstream pipeline reuses for sustained
suffering-reduction cannot be verified without a comparator that detects the crossing.

## Solution

A non-trainable rolling-window descent detector (`SufferingDerivativeComparator`) on
`z_harm_a.norm()`. On each waking tick (gated by `simulation_mode=False`), the comparator
appends the current norm to a fixed-length FIFO buffer. When:

1. The buffer is full (`window_length` ticks of data)
2. The initial (oldest) norm exceeds `min_initial_norm` (prevents false fires on a stream
   that was already quiet)
3. The drop from initial to final exceeds `drop_threshold`

the comparator returns `True` and `agent.sense()` sets `_relief_completion_event = True`.
This flag is consumed and cleared by `select_action()` in the same tick (adjacent to the
MECH-091 urgency block, opposite polarity).

On event fire (`select_action()`):
- If beta is elevated: `beta_gate.release()` + `_committed_step_idx = 0` (MECH-057a reuse)
- If `valence_liking_enabled` and `not hypothesis_tag`: `ResidueField.update_valence(z_world, VALENCE_LIKING, relief_completion_weight)` (MECH-094 reuse)

## Architecture Context

SD-050 is architecturally adjacent to MECH-091 (urgency interrupt). MECH-091 fires on an
UPWARD z_harm_a spike -- the "pain is suddenly worse, abort" signal. SD-050 fires on a
DOWNWARD z_harm_a descent -- the "sustained relief, episode over" signal. The two share the
downstream pipeline by design: both are salient events whose polarity is set at the input
(nociceptive escalation vs nociceptive de-escalation) but whose consolidation machinery is
shared (commitment release + valence write).

The comparator reads `z_harm_a` (C-fiber / affective-motivational stream, SD-011), NOT
`z_harm` (A-delta / sensory-discriminative stream). This is biologically grounded:
Navratilova 2012 shows pain relief activates VTA-DA + NAc-shell DA via the same circuit
as reward; the relief signal is carried by the affective stream, not the discriminative one.

The MECH-094 gate (`hypothesis_tag`) prevents simulation and replay content from triggering
relief-completion writes: only waking-path z_harm_a observations advance the comparator.

## Data Flow

```
CausalGridWorldV2.step() -> obs_harm_a [harm_obs_a_dim]
-> agent.sense(obs_harm_a=...) -> AffectiveHarmEncoder -> z_harm_a [1, z_harm_a_dim]
-> z_harm_a.norm() -> SufferingDerivativeComparator.tick(norm, simulation_mode=False)
-> agent._relief_completion_event (bool, set in sense(), consumed in select_action())
-> select_action():
     if relief_completion_event and beta_gate.is_elevated:
         beta_gate.release(); _committed_step_idx = 0
     if relief_completion_event and valence_liking_enabled and not hypothesis_tag:
         residue_field.update_valence(z_world, VALENCE_LIKING, relief_completion_weight)
     _relief_completion_event = False  (cleared each tick)
```

## Config Parameters

All gated by `use_suffering_derivative_comparator=False` (default, no-op):

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `use_suffering_derivative_comparator` | `False` | master switch |
| `suffering_window_length` | `5` | rolling-window FIFO depth (ticks) |
| `suffering_drop_threshold` | `0.10` | required drop from window[0] to window[-1] |
| `suffering_min_initial_norm` | `0.05` | floor on window[0] before detection is active |
| `relief_completion_weight` | `1.0` | VALENCE_LIKING write magnitude on event fire |

All parameters wired through `REEConfig.from_dims()`.

## What This SD Enables

- MECH-302: relief-completion event substrate (the comparator IS the MECH-302 substrate)
- MECH-303 teaching signal: the MECH-302 event is the signal that updates MECH-303's
  safety-cue predictive store
- Chronic-anxiety / persistent-avoidance failure mode: with comparator OFF, avoidance
  commitments accumulate without tag-and-release (no VALENCE_LIKING write on avoidance
  completion); PTSD/anxiety analog substrate

## Module and Files

- `ree_core/comparator/suffering_derivative_comparator.py` -- `SufferingDerivativeComparator` class
- `ree_core/comparator/__init__.py` -- package (shared with `TPJComparator`)
- `ree_core/utils/config.py` -- 5 config params in `REEConfig`, wired through `from_dims()`
- `ree_core/agent.py` -- import (line ~93), `__init__` instantiation (line ~328), `sense()` tick (line ~1801), `select_action()` fire handler (line ~2094), `reset()` clear (line ~1061)

## Backward Compatibility

`use_suffering_derivative_comparator=False` by default. With this default:
- `agent.suffering_comparator is None`
- `sense()` skips the comparator tick entirely
- `select_action()` skips the relief-completion block entirely
- No change to any existing experiment output

All 5 smoke tests PASS 2026-05-04 (backward compat, feature ON 10 steps, comparator logic,
flat-signal no-fire, min_initial_norm guard).

## Biological Basis

Navratilova et al. 2012 (PNAS): pain relief activates VTA dopamine and NAc-shell dopamine
via the same circuit as appetitive reward; blocked by DA antagonists and produces
conditioned place preference -- confirming shared machinery. Tanimoto 2004 (Nature):
Drosophila opponent-timing confirms relief as a positive reinforcer when paired with
appropriate temporal structure. Andreatta 2012: relief from fear -> striatum (not amygdala),
mirroring the goal-attainment vs harm-anticipation dissociation. The suffering-derivative
comparator (not a pooled DA readout) is the architecturally correct trigger per
Bromberg-Martin 2010 DA-heterogeneity qualifier: value-coding VTA-DA is the substrate, but
the REE trigger must be the derived comparator to avoid mixing salience-coding DA.

## Related Claims

MECH-302 (relief-completion event), MECH-303 (safety-cue prediction teaching signal),
SD-011 (z_harm_a affective stream source), MECH-057a (commitment-release reused),
MECH-091 (opposite-polarity urgency interrupt), MECH-094 (VALENCE_LIKING write gate)

## Validation Experiment

V3-EXQ-515 queued (4-arm substrate readiness diagnostic: OFF / ON / ON+valence / ON+no-hazards).
See experiment script `experiments/v3_exq_515_mech302_suffering_derivative_relief_completion.py`.
