---
title: "SD-093: Progress-Velocity Effort/Persistence Modulation"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 21
status: candidate
status_asof: 2026-08-03
status_claim: SD-093
---

# SD-093: Progress-Velocity Effort/Persistence Modulation

**Claim ID:** SD-093 (architectural commitment) / MECH-426 (mechanism, `goal.progress_velocity_maintenance`)
**Subject:** `goal.progress_velocity_maintenance`
**Status:** IMPLEMENTED 2026-08-02
**Registered:** 2026-08-02
**Depends on:** INV-086, INV-034, MECH-217 (all satisfied; MECH-217 confirmed IMPLEMENTED
2026-07-30 -- see `ree-v3/CLAUDE.md` "MECH-217: goal.replay_wanting_spread"), MECH-116
**Blocks:** EXP-0384 (was `blocked_substrate`; reset to `proposed` by this landing)

---

## Problem

`GoalState.goal_proximity()` (`ree_core/goal.py`) is a bounded, INSTANTANEOUS wanting signal --
`1 / (1 + MSE(z_world, z_goal))` -- read fresh every tick by `agent.py` (`_compute_persistence_appraisal`,
per-candidate liking) and `e3_selector.py` (`compute_goal_score`). Nothing anywhere differentiates it over
time. MECH-426 asserts that a rate-of-progress (velocity) signal -- the derivative of this on-path progress
estimate -- is itself a load-bearing maintenance signal, distinct from the instantaneous value: it is the
REE instantiation of Carver & Scheier's (1990) second-order "velocity" control loop, in which affect (here,
an effort/persistence modulation) is generated from the RATE of discrepancy reduction, not the discrepancy
itself.

**CRITICAL MODELLING CAVEAT (Carver & Scheier coasting), copied verbatim from the claim's own notes**:
above-reference progress produces positive affect that REDUCES effort on the current goal and licenses
redeployment -- velocity must be modelled as EFFORT-REGULATION, not same-goal reinforcement. A naive
implementation that treats positive progress-affect as a bonus increasing same-goal commitment INVERTS the
theory and mis-fires. This is the single hardest constraint on the implementation below, and the reason the
signal is wired into E3's commit-threshold EFFORT/PERSISTENCE pressure rather than into goal VALUE /
trajectory score.

MECH-217 (temporal_wanting_propagation, `goal.replay_wanting_spread`) is a distinct, already-implemented
mechanism: it BUILDS the wanting landscape via reverse replay (a training-time/offline credit-assignment
operation). MECH-426 READS a derivative of progress AT DECISION TIME to modulate commitment -- the two do
not overlap and MECH-217 being implemented does not by itself supply MECH-426's readout.

---

## Solution

**Rolling-window velocity computation (`ree_core/goal.py`, `GoalState`).** A bounded deque
(`maxlen=progress_velocity_window`, default 5) of `goal_proximity()` readings, appended once per E3 tick via
`GoalState.record_progress(z_world)`. Velocity is the simple rolling-window derivative:

```
velocity = (proximity_newest - proximity_oldest) / (window_length - 1)
```

`record_progress()` is a true no-op (history left untouched, returns `0.0`) when
`use_progress_velocity_effort_modulation` is `False` -- the master switch. `progress_velocity` exposes the
cached derivative; it is `0.0` until at least two readings have been recorded.

**Effort-modulation function (`GoalState.progress_velocity_effort_modulation`, a property):**

```
raw = -progress_velocity_effort_gain * progress_velocity
effort_modulation = clip(raw, -progress_velocity_effort_max, +progress_velocity_effort_max)
```

Sign convention, chosen to satisfy the coasting caveat and verified against `e3_selector.py`'s own commit
rule (`committed = variance < effective_threshold`, i.e. a HIGHER threshold is MORE permissive):

- **`velocity > 0`** (proximity increasing -- approaching the goal faster than the implicit zero reference
  rate) -> `effort_modulation < 0` -> when consumed, LOWERS `effective_threshold` (stricter commit bar, more
  readily kicked back into deliberation) -- licenses coasting/redeployment, matches Carver & Scheier.
- **`velocity < 0`** (proximity decreasing -- falling behind) -> `effort_modulation > 0` -> RAISES
  `effective_threshold` (more permissive, locks in and pushes through) -- boosts persistence/effort on the
  current goal.

This is deliberately the OPPOSITE of "positive progress -> bonus": a same-goal-commitment bonus on positive
velocity would invert the theory, which is exactly the failure mode the claim's notes warn against.

**Consumer wiring (`ree_core/predictors/e3_selector.py`, `E3TrajectorySelector.select()`).** Immediately
after the existing SD-011 `urgency_applied` block (both modulate the same `effective_threshold` variable,
applied multiplicatively in sequence):

```python
if goal_state is not None and goal_state.is_active():
    velocity_effort = goal_state.progress_velocity_effort_modulation
    if velocity_effort != 0.0:
        effective_threshold = effective_threshold * (1.0 + velocity_effort)
```

`goal_state` was already a parameter of `select()` (used by `compute_goal_score`), so no new plumbing was
needed at the call site. `compute_goal_score()` / `goal_proximity()` (goal VALUE / trajectory score) are
completely untouched by this flag -- verified by a byte-identical contract test.

**Recording call site (`ree_core/agent.py`, `_e3_tick`).** Once per E3 tick, on the SAME one-shot
`z_world_for_e3` (theta-buffer summary) the tick's other non-per-candidate goal appraisals already read --
NOT the per-candidate trajectory rollouts `compute_goal_score()` scores:

```python
if self.goal_state is not None and self.goal_state.is_active():
    self.goal_state.record_progress(z_world_for_e3)
```

**`with_injection()` propagation.** `GoalState.with_injection()` (MECH-188's `z_goal_inject > 0` scoring-only
wrapper) constructs a lightweight `GoalState.__new__` view that previously did not copy the drive trace or
any velocity state. `E3.select()` receives THIS wrapper whenever `z_goal_inject > 0`, so without propagating
`_progress_history` / `_progress_velocity` into it, the injected view would silently read a fresh
zero-initialised deque and `progress_velocity_effort_modulation` would always report `0.0` under that
(pre-existing, off-by-default) feature. Fixed by sharing the same deque object into the injected view
(read-only for that tick; never mutated by `select()`).

**`reset()`.** Clears `_progress_history` and `_progress_velocity` -- per-episode state, mirroring the
existing `_drive_trace` reset (a stalled-vs-progressing read from a PRIOR episode must not leak into a fresh
one's effort modulation).

### Config (`GoalConfig`, `ree_core/goal.py`)

| Param | Type | Default | Purpose |
|---|---|---|---|
| `use_progress_velocity_effort_modulation` | bool | `False` | master switch |
| `progress_velocity_window` | int | `5` | rolling-window length (clamped to >= 2) |
| `progress_velocity_effort_gain` | float | `1.0` | scales velocity into the modulation signal |
| `progress_velocity_effort_max` | float | `0.3` | symmetric saturation cap on the modulation |

All four default to a no-op: with the master switch `False`, `record_progress()` never populates the
history and `progress_velocity_effort_modulation` always returns `0.0` -- byte-identical to every existing
run.

### Backward compatibility

Verified by contract tests (`tests/contracts/test_mech426_progress_velocity.py`, 18 tests): flag-off is a
true no-op (history never populated); `goal_proximity()` / `goal_distance()` are byte-identical regardless
of the flag; an existing V3 experiment script (`v3_exq_869a_...`) runs unchanged under `--dry-run`.

### Phased training

Not applicable -- this is a hand-computed rolling-window derivative and a deterministic clip function, not a
trained head. No phased (P0/P1/P2) protocol is required.

### MECH-094

Not applicable -- `record_progress()` records the WAKING-tick `goal_proximity()` reading only (called from
`_e3_tick`, the waking `select_action` path); it is not a simulation/replay content write to any memory
store, so no `hypothesis_tag` applies.

---

## Architecture Context

Sits alongside the existing SD-011 (`z_harm_a` urgency) mechanism in `E3TrajectorySelector.select()`'s
`effective_threshold` pipeline -- both are EFFORT/PERSISTENCE modulators on the commit decision, applied
multiplicatively in sequence (sweep-threshold-reduction -> urgency -> progress-velocity). Distinct from
MECH-217 (`goal.replay_wanting_spread`, an offline/training-time credit-assignment mechanism over the same
`GoalState`) and from MECH-340/Q-053's `PersistenceAppraisal` (`ree_core/hippocampal/persistence_appraisal_compute.py`,
a SEPARATE, independently-gated `GhostGoalBank` license computation that also reads instantaneous
`goal_proximity`). MECH-426 does not modify either of those; it adds a third, independently-gated
consumption path off the same underlying `GoalState.goal_proximity()` primitive.

---

## What This SD Enables

Unblocks EXP-0384 (MECH-426's own falsifier: a 2x2 VELOCITY-ON/OFF x SPARSE/DENSE-confirmation ablation
testing whether long-horizon superordinate-goal maintenance degrades specifically in the sparse-confirmation
regime when velocity is ablated). Reset from `blocked_substrate` to `proposed` by this landing --
`/queue-experiment` can now design and queue the run.

---

## Related Claims

MECH-426, SD-093 (this doc), INV-086, INV-034, MECH-217, MECH-116, MECH-340/Q-053 (sibling consumer of
`goal_proximity`, not modified by this SD).
