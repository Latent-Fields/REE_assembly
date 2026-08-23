---
title: "SD-065: environment.conditioned_safety_cue_channel"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 19
status: candidate/v3_pending
status_asof: 2026-07-15
status_claim: SD-065
---

# SD-065: environment.conditioned_safety_cue_channel

**Claim ID:** SD-065
**Subject:** environment.conditioned_safety_cue_channel
**Registered:** 2026-07-14
**Status:** IMPLEMENTED (2026-07-14)
**Depends on:** SD-005 (split body/world observation), ARC-024 (proxy-gradient fields), SD-022 (limb_damage + scheduled-injection curriculum, the relief generator), SD-051 / MECH-304 (the ConditionedSafetyStore consumer), MECH-302 (relief-completion teaching signal)
**Blocks:** MECH-304 promote-to-active behavioural falsifier (classical conditioned inhibition; V3-EXQ-763)

## Problem

SD-051 built the `ConditionedSafetyStore` (agent-side) and MECH-304's release
mechanism is fully wired in `agent.py` (`sense()` -> `store.update(z_world,
event_fired=relief)`; `select_action()` -> `beta_gate.release()` when
`_conditioned_safety_signal > safety_store_threshold` and the gate is elevated).
But the store has **no controllable observable cue to key on**. The MECH-302
relief-completion event is an internal derivative (z_harm_a norm descent via
`suffering_derivative_comparator.py`) with **no distinct observable stimulus
attached**. The environment (`causal_grid_world.py`) has no safety-cue field:
threat IS the hazard US, and the SD-023 landmark_a/b + SD-049 dual_cue fields are
resource-predictive, not safety, and not bindable to relief.

Consequently the representation-level isolation test V3-EXQ-759 (which promoted
MECH-304 candidate->provisional) had to **synthesize the Pavlovian pairing
off-substrate** (region-partitioned z_world fed through `store.update(event_fired=
True)`) and score a scale-free `predict()` AUC. That evidence is
necessary-not-sufficient. The **promote-to-active** gate is the pre-registered
BEHAVIOURAL falsifier in claims.yaml (`MECH-304 functional_restatement`,
"Falsifiable:"): classical conditioned inhibition (a learned safety cue suppresses
avoidance commitment even when presented **concurrently** with a threat cue) plus a
dissociation (MECH-304 ablation abolishes cue-specific safety while sparing MECH-303
contextual safety). A behavioural test cannot fake the pairing -- it needs a real,
controllable, observable safety cue in the environment.

This mirrors the sibling MECH-302 517-family `substrate_ceiling` (V3-EXQ-517/517a/
517b FAILed: `causal_grid_world` + a trained avoidance policy filtered out the needed
trajectories), fixed by the SD-022 scheduled-injection env extension
(`scheduled_limb_damage_*`). MECH-304 needs the analogous extension for a SAFETY CUE.

## Solution

A controllable, observable **conditioned-safety cue channel** in `CausalGridWorld`,
built to the SD-022 / SD-023 precedent (env-only kwargs, defaults inert,
bit-identical OFF).

### The cue is ambient, not a spatial gradient

The store keys on the full `z_world = encode(world_state)`. For a clean
conditioned-inhibition demonstration the cue must be (a) **reliably present in
z_world** at every relief tick regardless of agent position, and (b)
**reproducible** at test so the learned prototype recognises it. A
spatially-localised gradient (landmark-style) would make the cue's z_world
contribution depend on agent position -- a navigation confound. So the cue is an
**ambient uniform field**: when active, a 25-dim (5x5) view filled with
`safety_cue_scale` (clipped [0,1]); when inactive, zeros. This is the faithful
analog of a Pavlovian tone/light CS (present ambiently, not a location) and matches
the discriminative-pair conditioned-inhibition protocol (Andreatta 2012; Ng &
Sangha 2023). The channel is emitted into `world_state` (feeds the z_world encoder)
and surfaced in `obs_dict["safety_cue_field_view"]`.

### Two activation paths

1. **Env-owned relief pairing (teaching).** `safety_cue_on_relief=True` auto-activates
   the cue whenever body-damage is elevated -- `sum(limb_damage) >
   safety_cue_heal_floor` -- i.e. across the damage->heal window that generates the
   real MECH-302 relief descent. Crucially, the `ConditionedSafetyStore` still writes
   its prototype **only** on the real `event_fired` tick (the MECH-302
   relief-completion event fired inside that window); the env only guarantees the cue
   is observable across the window. **The pairing is real, not synthesized.** Requires
   `limb_damage_enabled=True` (ValueError precondition, mirrors SD-022's
   `scheduled_limb_damage` guard). Even though the cue is also present at the
   damage-spike tick (high z_harm_a, no relief), the store does not write there
   (`event_fired=False`), so the prototype captures only the relief-tick z_world.

2. **Test-phase manual API (test).** `set_safety_cue(active)` sets a tri-state manual
   override (`None` = follow the schedule; `True`/`False` = force). It takes precedence
   over the relief-pairing path, letting an experiment present {threat + safety cue}
   **concurrently** in a single tick (threat = the existing hazard field; both ride
   `world_state` simultaneously) while an avoidance commitment is active.

### Config parameters (all env-only; not surfaced through REEConfig.from_dims)

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `safety_cue_enabled` | `False` | master switch (emits the 25-dim channel; grows world_obs_dim by 25) |
| `safety_cue_scale` | `1.0` | uniform value emitted when active (clipped [0,1]) |
| `safety_cue_on_relief` | `False` | auto-activate the cue across the damage->heal (MECH-302 relief) window |
| `safety_cue_heal_floor` | `0.05` | total-limb-damage floor above which the relief window is active |

Preconditions (loud-not-silent, mirroring SD-022):
- `safety_cue_enabled=True` requires `use_proxy_fields=True` (the channel only exists in proxy mode).
- `safety_cue_on_relief=True` requires `limb_damage_enabled=True` (no relief window without body damage).

### Data flow

```
CausalGridWorld.step()
  -> compute _safety_cue_active (manual override > relief-window > inactive)
  -> _safety_cue_field = safety_cue_scale (uniform) if active else 0
CausalGridWorld._get_observation_dict()
  -> world_state gains a 25-dim safety_cue view (when safety_cue_enabled + use_proxy_fields)
  -> obs_dict["safety_cue_field_view"] (absent when disabled)
agent.sense() -> LatentStack.encode() -> z_world (now carries the cue component)
  -> ConditionedSafetyStore.update(z_world, event_fired=_relief_completion_event)   [SD-051]
agent.select_action()
  -> if _conditioned_safety_signal > safety_store_threshold and beta_gate.is_elevated:
         beta_gate.release()    # conditioned inhibition of avoidance commitment
```

## Architecture Context

SD-065 is the environmental affordance that makes SD-051 / MECH-304 behaviourally
testable. It is to MECH-304 what SD-022's `scheduled_limb_damage` is to MECH-302: a
curriculum-level env extension that supplies the controllable antecedent the
mechanism needs, without changing the agent substrate. It does **not** add an entity
type (NUM_ENTITY_TYPES stays 7; the 5x5x7 local_view width is fleet-invariant) --
it is a field-view channel, so no arm-reuse fingerprint or obs width shifts for any
experiment that does not enable it.

## What This SD Enables

- MECH-304 promote-to-active behavioural falsifier V3-EXQ-763: crossing
  `use_conditioned_safety_store` {ON, OFF} x cue condition, teaching by pairing the
  cue with relief, test by presenting the cue concurrently with a threat under an
  active (harness-induced) avoidance commitment.
- DV1 conditioned inhibition (cue lowers avoidance-commitment release rate, ON arm only).
- DV2 dissociation (store OFF abolishes DV1 while `use_contextual_safety_terrain`
  MECH-303 contextual safety stays intact).

## Backward Compatibility

`safety_cue_enabled=False` by default. With this default: no channel emitted,
`world_obs_dim` unchanged, no RNG draws, no state change -- **bit-identical OFF**.
Verified by the contract suite (`tests/contracts/test_scheduled_safety_cue_curriculum.py`)
and the full `pytest tests/` + `tests/preflight/` regression run.

## Related Claims

MECH-304 (the behavioural claim this channel makes testable), SD-051 (the
ConditionedSafetyStore consumer), MECH-302 / SD-050 (relief teaching signal),
MECH-303 (sister contextual-safety pathway, the DV2 sparing control), SD-022
(build-pattern precedent + the relief generator).

## Validation Experiment

V3-EXQ-763 (MECH-304 promote-to-active behavioural falsifier, queued 2026-07-14).
See `experiments/v3_exq_763_mech304_conditioned_inhibition_behavioural_falsifier.py`.
