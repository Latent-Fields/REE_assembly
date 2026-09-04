# SD-WAYPOINT-FIELD: environment.waypoint_proximity_field

**Claim ID:** SD-WAYPOINT-FIELD
**Subject:** environment.waypoint_proximity_field
**Status:** IMPLEMENTED
**Registered:** 2026-09-04
**Implemented:** 2026-09-04 (ree-v3 `ree_core/environment/causal_grid_world.py`)
**Depends on:** SD-005 (world observation split), SD-094 (waypoint-arrival detection)
**Blocks:** INV-086 (`goal_maintenance_feedback_necessity`), MECH-428 (EXP-0390), and
every navigation-dependent DV in `subgoal_mode` (goal maintenance, subgoal seeding,
sequence-completion rate)
**Provenance:** `chip-20260902-waypoint-proximity-field-observable`, campaign C3 item 2 of
`evidence/planning/science_wave_campaign_plan_20260904.md`

---

## Problem

In `subgoal_mode` the sub-goal waypoints reach the agent through exactly one channel:
entity-type index 6 of the 5x5x7 local view (`causal_grid_world.py`, the `local_view`
block of `_get_observation_dict`). The local view has radius 2. **A waypoint more than
two cells from the agent is therefore not observable at all** -- not faintly, not
noisily: it is absent from the observation vector.

The consequence was measured directly, not inferred. V3-EXQ-977 (INV-086
`goal_maintenance_feedback_necessity`) was adjudicated `blocked_substrate` on 2026-09-02
by session `fable-queue-refill-20260902` after one-tick probes (`probe_nav_977.py`;
results in the EXP-0705 `blocked_note`). Configuration: `subgoal_mode=True`, 3 waypoints,
`waypoint_visit_reward=0`, 12x12 grid, 400 steps, seeds 42/43/44. Result: **the agent's
own policy visited 0 / 0 / 1 waypoints and completed 0 sequences** -- statistically
indistinguishable from a random walk.

This is a substrate ceiling, not a negative scientific result. Any DV defined over
goal-directed navigation is pinned at chance regardless of what the mechanism under test
does, so such an experiment cannot discriminate its hypotheses in either direction. The
existing corpus shows the workaround pressure: of the 27 `subgoal_mode` drivers, 883/884
**script the walk** rather than let the policy navigate, and the 460-series completion
figures rely on a Chebyshev tolerance band roughly 25% of the grid wide.

A second, subtler reason a grid-sourced fix would not work: the waypoint's *grid marker*
is erased on first transit unless `subgoal_arrival_position_check=True` (the SD-094
defect). Any observable read off `self.grid` inherits that bug.

## Solution

An env-level, **default-OFF**, 25-dimension field view carrying a monotone proximity
gradient around the **pending** waypoint, following the established field-view pattern of
the hazard / resource / SD-023 landmark / SD-065 safety-cue channels.

```
self.waypoints[self._next_waypoint_idx]      (source: the substrate's own pending target)
    -> 1 / (1 + waypoint_field_decay * d)    (reciprocal Manhattan decay, torus-aware)
    -> 5x5 patch centred on the agent        (25 dims, appended LAST to world_state)
    -> SplitEncoder / z_world                (absorbed automatically via env.world_obs_dim)
```

**Constructor parameters** (`CausalGridWorld` / `CausalGridWorldV2`):

| Param | Type | Default | Purpose |
|---|---|---|---|
| `waypoint_proximity_field_enabled` | bool | `False` | master switch |
| `waypoint_field_decay` | float | `0.25` | gradient steepness; must be `> 0` |

**Kernel.** `f(cell) = 1 / (1 + decay * d(cell, target))`, with `d` the Manhattan
distance -- the same reciprocal decay `_compute_proximity_fields()` already uses for the
hazard field. Because there is a single source, the field self-normalises: exactly `1.0`
on the target cell, no per-episode rescaling, and values comparable across episodes and
across seeds. At the default decay on a 12x12 grid the dynamic range is `1.0` (d=0) down
to `0.154` (d=22, the diagonal) -- discriminable in float32 across the whole grid, which
is the property the exponential kernels (reef, landmark) do not have at long range.

**Directionality.** The gradient is the point. The 5x5 patch is strictly monotone toward
the target from anywhere on the grid, so a policy can hill-climb it without ever having
the waypoint inside its local view. This is what converts a navigation DV from
random-walk-pinned to reachable.

**Torus awareness.** When `self.toroidal`, each axis uses the shortest wrap-around
distance (`min(dd, size - dd)`). The existing `_compute_proximity_fields()` uses plain
Manhattan, which on a wrapped world points the agent the long way round; the new channel
deliberately does not repeat that. Pinned by contract C8.

**Computed on demand, not cached.** Reef and landmark fields are cached grid arrays
because their sources are static per episode. The waypoint source *moves*: the pending
index advances mid-`step()` and `_respawn_waypoints()` relocates the whole set. A cached
grid would be exactly one tick stale precisely when the target changes -- so the 25-cell
patch is computed directly in `_get_observation_dict()` from `self.waypoints`. This also
costs 25 distance evaluations per tick instead of `size^2`.

**Sourced from `self.waypoints`, never from `self.grid`** -- deliberately, so the SD-094
marker-erasure defect cannot propagate into the new channel.

**Preconditions (loud, not silent).** `ValueError` on each of: the flag without
`use_proxy_fields` (the channel rides `world_state`, which only carries field views in
proxy mode); the flag without `subgoal_mode` (`self.waypoints` is never populated, so the
channel would be identically zero and the experiment would silently measure nothing);
`waypoint_field_decay <= 0` (a constant kernel is not a gradient).

**Placement.** Appended **last** in `world_parts`, after the SD-065 arm, with the matching
`+25` last in `world_obs_dim`. This is load-bearing: `latent/stack.py`
(`HAZARD_INDICES`, `CONTAMINATION_SLICE = slice(175,200)`,
`RESOURCE_FIELD_SLICE = slice(225,250)`) and `latent/zworld_p0.py`
(`RESOURCE_FIELD_SLICE`) are **prefix** slice constants pinned by
`test_sd018_resource_field_head.py::test_c4_slice_constants_agree_with_env_layout`.
Inserting anywhere before index 250 would break them; appending last does not.

**Consumption requires no agent-side change.** Drivers already size the encoder from the
env (`REEConfig.from_dims(world_obs_dim=env.world_obs_dim, ...)`), so growing
`world_obs_dim` by 25 is absorbed automatically and `z_world` encodes the new channel.

## Backward compatibility

Bit-identical when off, on all three axes:

- **No channel.** `world_obs_dim` is unchanged (250 in proxy mode) and
  `waypoint_proximity_field_view` is absent from the obs dict (the mech090
  absent-when-disabled precedent, matching SD-065).
- **No RNG.** The field is a pure read of `self.waypoints`; enabling it draws zero env
  RNG, so a trajectory is bit-identical to a control differing only by the flag
  (contract C7).
- **No prefix movement.** With the flag ON, `world_state[:250]` is byte-for-byte the OFF
  `world_state` (contract C3).

Setting `waypoint_field_decay` alone, with the master switch off, changes nothing.

**Env-only; NOT surfaced through `REEConfig.from_dims`** -- the same convention as SD-065
and SD-023, and the reason no `config.py` change is owed here. `EnvironmentConfig` carries
no env observable knobs at all; drivers pass them to the `CausalGridWorld(...)`
constructor directly and only `env.world_obs_dim` flows into `from_dims`.

## Observability

Always-present info-dict sentinels (inert when disabled):
`waypoint_proximity_field_enabled`, `waypoint_field_at_agent` (the patch-centre value),
`waypoint_field_target_idx` (the pending index the field is pointing at, `-1` when none).

One behaviour worth stating for driver authors: **the at-agent value never reads `1.0` in
normal play.** Arrival and re-targeting happen within the same tick, so the observation
returned by the arrival step already points at the *next* waypoint. A DV that expects the
field to saturate on arrival is mis-specified; use `transition_type` /
`waypoint_field_target_idx` for arrival, and the field for approach.

## Phased training

Not applicable. This SD adds no encoder head and no loss -- it is an environment
observable only. No P0/P1/P2 phasing is required by this change (a consumer that adds a
head on top of it would inherit the usual requirement).

## MECH-094

Not applicable. The channel is a live exteroceptive observation computed from the current
environment state. It writes nothing to memory and generates no simulated or replayed
content, so the `hypothesis_tag=True` requirement does not arise.

## ML/AI engineering notes

The engineering problem is **reward-free goal reachability under partial observability** --
a target outside the observation window makes the goal-directed policy unlearnable, and
no amount of mechanism work downstream compensates. The standard remedies are potential-
based shaping (Ng et al.), goal-conditioned observation augmentation (UVFA / HER), and
distance-to-goal features.

What was adopted, and what deliberately was not:

- **Adopted: a goal-distance *observation*, not a shaping *reward*.** Potential-based
  shaping would alter the reward signal and therefore contaminate every valence /
  commitment / residue DV that reads it -- exactly the streams the blocked experiments
  measure. Making the distance an observable leaves the reward channel untouched and
  keeps the mechanism under test the only thing that varies.
- **Adopted: a monotone, bounded kernel.** `1/(1+kd)` is bounded in `(0, 1]`, so it needs
  no normalisation pass and cannot destabilise encoder input scale as the source moves --
  the numerical failure mode an unbounded or max-normalised moving-source field would
  have.
- **Not adopted: a learned goal embedding or an attention read-out.** The SD is an
  observability fix; importing representational machinery here would be
  architecture-by-analogy and would confound the very DVs the fix is meant to free.

The biological grounding is compatible and is the ordinary one for this channel family:
allocentric distance-to-goal gradients are a standard spatial-navigation affordance, and
the channel sits alongside the existing hazard / resource / landmark gradient views rather
than introducing a new modality.

## Contract coverage

`ree-v3/tests/contracts/test_waypoint_proximity_field.py` -- 19 tests, C1-C8:

| # | Contract |
|---|---|
| C1 | off by default, inert sentinels, no channel, `world_obs_dim` unchanged, tuning knob alone is a no-op |
| C2 | preconditions raise (`use_proxy_fields`, `subgoal_mode`, `decay > 0`); master flag alone is legal |
| C3 | `+25` exactly; view is the trailing 25 dims; ON prefix == OFF `world_state` |
| C4 | kernel equals `1/(1+decay*d)` cell-by-cell; exactly `1.0` on the target; out-of-bounds cells stay `0.0` |
| C5 | **directionality**: patch monotone toward the target; at-agent value strictly rises along an approach route (exact series `0.5, 4/7, 2/3, 0.8` at decay 0.25); a target far outside the 5x5 local view is still discriminable where the local view is identical |
| C6 | field re-points when the pending index advances; all-zero with no pending waypoint; `reset()` tags track the new episode, `reset_to()` clears them |
| C7 | RNG isolation over 60 steps against a flag-only control |
| C8 | toroidal: a target across the seam reads near, not far |

## What this SD enables

- **INV-086** (`goal_maintenance_feedback_necessity`) -- V3-EXQ-977's retest becomes
  meaningful: the OFF-arm floor is no longer random walk, so a goal-maintenance effect has
  somewhere to show up.
- **MECH-428** (EXP-0390) and any completion-rate DV.
- Removes the standing need for `subgoal_mode` drivers to script the walk or widen the
  tolerance band, i.e. lets sequence completion be a *measured* behaviour rather than a
  constructed one.

## Validation

Deferred at implementation time, and stated here rather than silently omitted: the
`substrate_queue.json` entry and the validation experiment could not be written on
2026-09-04 because `/governance` session `governance-20260904-1347` held an exact-file
pause on `REE_assembly/evidence/planning/substrate_queue.json`,
`REE_assembly/docs/claims/claims.yaml` and `ree-v3/experiment_queue.json`. See
`evidence/planning/c3_deferred_writes_20260904.md` for the drafted entry and the
validation-experiment specification, to be applied once the pause lifts.

Validation shape (per `/implement-substrate` Step 8, acceptance criteria taken from the
V3-EXQ-977 failure record): `experiment_purpose: diagnostic`; arms
`waypoint_proximity_field_enabled` ON vs OFF at matched seeds; DV = waypoints visited and
sequences completed by the agent's **own** policy (no scripted walk); OFF-arm expectation
is the measured 0/0/1 visits and 0 completions; the ON arm must exceed the random-walk
floor. The bar must be pre-registered inside the DV's measured range.

## Related claims

INV-086, MECH-428, SD-094 (arrival detection -- the reason this field reads
`self.waypoints` rather than `self.grid`), SD-023 (landmark gradient views -- the pattern
followed), SD-065 (safety-cue channel -- the default-OFF additive-channel template),
SD-018 (`RESOURCE_FIELD_SLICE` prefix constants -- the reason the channel is appended
last), SD-005 (world observation split).
