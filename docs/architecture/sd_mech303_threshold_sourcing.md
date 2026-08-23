---
title: "SD-MECH303-THRESHOLD-SOURCING: safety_prediction.contextual_passive_substrate.dedicated_proximity_gate"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 22
---

# SD-MECH303-THRESHOLD-SOURCING: safety_prediction.contextual_passive_substrate.dedicated_proximity_gate

**Claim ID:** SD-MECH303-THRESHOLD-SOURCING
**Subject:** mech303.contextual_safety_gate.dedicated_proximity_signal
**Status:** IMPLEMENTED
**Registered:** 2026-08-14
**Depends on:** SD-011 (affective-harm dual-stream encoder), SD-052 (MECH-303 contextual passive substrate), MECH-303
**Blocks:** MECH-303 live-gate usability; the owed behavioural retest (`pending_retest_after_substrate: true` on MECH-303)

## Problem

MECH-303's contextual passive safety substrate (SD-052) accumulates a safety terrain
each waking step where "harm is absent" in the current spatial context. Its gate in
`agent.py` `sense()` decided "harm absent" by reading `z_harm_a.norm() <
contextual_safety_harm_threshold`.

`z_harm_a` is a **shared** affective-harm signal, and SD-022 re-sources it. When a driver
sets `limb_damage_enabled=True`, `z_harm_a` becomes a body-damage integral --
deliberately **decoupled from the agent's current location** (SD-022's own stated design
intent: "an agent in a safe location with accumulated limb damage should have high
z_harm_a and near-zero z_harm_s"). That is exactly the wrong construct for MECH-303,
whose entire claim is about **current spatial context**.

**V3-EXQ-917** (harm-threshold calibration battery, 2 sourcing modes x 5 hazard densities
x 10 seeds x 18 swept thresholds) measured the consequence directly:

| sourcing mode | `limb_damage_enabled` | safe-vs-unsafe AUC |
|---|---|---|
| `damage_sourced` (SD-022) | True | <= 0.52 (chance) at every threshold 0.02-0.80 |
| `proximity_ema_sourced` (legacy default) | False | 0.84-0.97 (tau~0.6: reach 0.85, AUC 0.969) |

Under the damage-sourced signal the gate cannot discriminate safe from hazardous contexts
at **any** reachable threshold. The two consumers want opposite things from one boolean
(SD-022 wants body/context DECOUPLED; MECH-303 wants body/context COUPLED), so a single
`z_harm_a` structurally cannot serve both -- this is an architectural seam defect, not a
threshold-calibration problem. Biologically (Melzack & Casey 1968; Craig 2002/2003;
Rainville 1997), damage-sourcing is a reactive, sensory-discriminative nociceptive signal,
while MECH-303's contextual safety learning (Kreutzmann 2020, Meyer 2019, Laing 2022) is
anticipatory and affective-motivational -- gating the latter on the former is a
mechanistic mismatch.

**Routing decision (2026-08-12, user-adjudicated in /governance):** implement option (a) --
a DEDICATED proximity-anticipatory signal for MECH-303's gate, decoupled from SD-022's
damage-sourcing -- NOT option (b), a threshold retune of the shared damage-sourced signal.
Option (b) was rejected because damage-sourcing is load-bearing for SD-022's own
body-damage-tracking purpose and for every other `z_harm_a` consumer; re-sourcing the
shared signal would fix this gate by breaking theirs. A SECOND harm signal is the correct
shape, consistent with SD-011's dual-stream separation.

## Solution

Add a dedicated anticipatory hazard-proximity signal that MECH-303's gate consumes,
leaving every existing `z_harm_a` consumer untouched. No new encoder, no learned
parameters, no phased training -- the signal is a deterministic environment EMA.

**Environment (`ree_core/environment/causal_grid_world.py`).** The proximity machinery
already exists: `hazard_at_agent = clip(hazard_field[cell], 0, 1)` is a proximity-field
readout (each hazard contributes `1/(1+dist*decay)`, so being NEAR a hazard elevates it
before contact), computed every step regardless of `limb_damage_enabled`. A new **separate
scalar EMA** `self._safety_proximity_ema` (tau~20, `safety_proximity_ema_alpha=0.05`) is
updated from that same readout **before** the Q-080 effort injection, so it stays a pure
hazard-proximity signal decoupled from both SD-022 (body damage) and Q-080 (effort). It is
emitted as `obs_dict["safety_proximity_harm"]` (scalar in [0,1]) only when
`safety_proximity_signal_enabled=True` (absent-when-disabled, mech090 precedent; OFF path
bit-identical).

**Config (`ree_core/utils/config.py`, REEConfig + from_dims).**
- `contextual_safety_gate_source: str = "z_harm_a"` -- selector. `"proximity_signal"` opts in.
- `contextual_safety_proximity_threshold: float = 0.25` -- "harm absent" gate for the
  dedicated signal. Sits between safe (~0.0) and dense-hazard (~0.8) contexts. AUC is
  scale-invariant so discrimination holds regardless; a driver in an unusual hazard regime
  should still calibrate this to its own observed distribution.
- Existing `contextual_safety_harm_threshold` (0.05) is untouched -- it remains the gate
  for the default `z_harm_a` source.

**Agent (`ree_core/agent.py` `sense()`).** New `obs_safety_proximity: Optional[float] =
None` kwarg (the `mech090_readiness_outcome` forwarding pattern). The MECH-303 accumulate
gate now selects its signal by `contextual_safety_gate_source`:
- `"z_harm_a"` (default): `z_harm_a.norm() < contextual_safety_harm_threshold` -- unchanged.
- `"proximity_signal"`: `obs_safety_proximity < contextual_safety_proximity_threshold`. If
  the env did not surface the signal (`obs_safety_proximity is None`), the gate does NOT
  fire -- **no silent fallback to z_harm_a**, which would reintroduce the mismatch.

### Data flow

```
causal_grid_world.step():
  hazard_at_agent (proximity field @ cell, always computed)
    -> self._safety_proximity_ema  (dedicated scalar EMA, updated pre-effort-injection)
    -> obs_dict["safety_proximity_harm"]  (scalar; only when safety_proximity_signal_enabled)

driver forwards obs_dict["safety_proximity_harm"] -> agent.sense(obs_safety_proximity=...)

agent.sense() MECH-303 gate:
  gate_source == "proximity_signal"  ->  fire iff obs_safety_proximity < proximity_threshold
  gate_source == "z_harm_a" (default) ->  fire iff z_harm_a.norm() < harm_threshold  (unchanged)
  -> residue_field.accumulate_safety(z_world, ...)   [existing hypothesis_tag waking-path guard retained]
```

### Backward compatibility

With `safety_proximity_signal_enabled=False` and `contextual_safety_gate_source="z_harm_a"`
(both defaults), the environment output is bit-identical (channel absent) and the gate
reads `z_harm_a` exactly as before. The new `sense()` kwarg defaults `None`. Every existing
experiment runs unchanged.

### Smoke validation (2026-08-14)

- (a) `from_dims` wires both new fields; defaults `gate_source="z_harm_a"`,
  `proximity_threshold=0.25`; existing `harm_threshold=0.05` unchanged.
- (b) env channel absent when disabled; mean signal safe(nh=0)=0.0000 vs unsafe(nh=8)=0.8734.
- (c) end-to-end agent gate under proximity sourcing: `accumulate_safety` fires 150/150 in
  a safe context (nh=0) and 6/150 in a dense-hazard context (nh=8) -- a clean dissociation;
  the default `z_harm_a` path runs unchanged.

## Driver sourcing audit (deliverable required by the queue entry)

Of the 21 driver scripts in `ree-v3/experiments/` that set
`use_contextual_safety_terrain=True`, exactly **3** set `limb_damage_enabled=True`
(damage-sourced z_harm_a): `v3_exq_520` (positive-control readiness diagnostic, overrides
threshold to 999), `v3_exq_763` (MECH-304 conditioned-inhibition falsifier), `v3_exq_764`
(MECH-303 behavioural falsifier, calibrated threshold 0.55 + test-time freeze). The other
**18** run under the framework default `limb_damage_enabled=False` (proximity_ema). No
reviewed, scored damage-sourced run has exercised MECH-303's live gate and reported it
working. **Any future driver enabling MECH-303's live gate should set
`contextual_safety_gate_source="proximity_signal"` + `safety_proximity_signal_enabled=True`
rather than inheriting whatever `limb_damage_enabled` the rest of its config happens to set
for SD-022's unrelated purposes.**

## Architecture Context

This is the shared-signal analogue of CLAUDE.md's coupled-code remedy (a2): SD-022
(producer) and MECH-303 (consumer) each pass their own validation while being mutually
incompatible at the interface between them. The fix decouples them by giving MECH-303 its
own signal, exactly as SD-011's dual-stream design (sensory-discriminative vs
affective-motivational) separates the two pain components rather than forcing one signal to
serve both. It does NOT touch the SD-022 damage-sourcing path, the dACC-saturation consumer
(`agent.py` MECH-268/SD-034, which legitimately wants the z_harm_a harm-present binary), or
the terrain-release consumer.

## What This SD Enables

- A reachable + discriminating live gate for MECH-303's contextual safety accumulation,
  clearing the safe-vs-unsafe AUC (target 0.84-0.97) the damage-sourced signal cannot.
- The owed MECH-303 behavioural retest (`pending_retest_after_substrate: true`): once a
  driver sources the gate from the dedicated signal, the background-vigilance-lowering
  behavioural falsifier can finally be run through a gate that fires informatively.

## MECH-094 / phased-training notes

- **MECH-094:** not newly implicated. The `accumulate_safety` call retains its existing
  `hypothesis_tag` waking-path guard; the proximity signal is a waking env observable, never
  written to memory during simulation/replay.
- **Phased training:** NOT required. No encoder head, no learned parameters -- the signal is
  a deterministic environment EMA.

## Related Claims

MECH-303 (contextual passive safety substrate; this SD sources its gate), SD-052 (the
substrate this refines), SD-011 (dual-stream separation this follows), SD-022 (the
damage-sourcing this decouples from, untouched), MECH-304 (sister cue-specific safety
claim). Validation experiment: see `ree-v3/CLAUDE.md` entry.
