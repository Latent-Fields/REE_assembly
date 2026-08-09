# V3-EXQ-906b -- Full-Stack Observational Fishtank Showcase (proximity-radius fix)

**Status:** PASS (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** bug-fix lettered iteration of V3-EXQ-906a (2026-08-09), routed by the
user-confirmed `failure_autopsy_V3-EXQ-906a_894b_2026-08-09.md`. 906a fixed 2 of 3
independent health-drain channels (contamination, direct hazard contact) but left a third,
grid-wide proximity-approach-damage channel untouched (radius ~11 cells vs the agent's
fixed radius-2 sensory window) -- this run tightens that radius to ~1.33 cells (inside the
sensory window, with a genuine "smell before harm" gap), adds a bounded safe-spawn retry so
no segment starts already inside the harm zone, and fixes three recording-core bugs
(elapsed_seconds/config/seeds) 906a's manifest was missing. See module docstring for the
full mechanism and the arithmetic behind the chosen parameter values.

- harm-pathway train steps (total): 3751
- z_goal activated at eval: True
- eval steps (total): 3909  across 8 segments x up to 500 steps/seed
  (mean realized segment length: 488.6 steps -- 906's was ~14.9, 906a's was 25.4)
- segment endings: health_depleted=2 step_cap=6
- events: block=152 limb_damage=28 external_hazard=31 world_rule_shift=15
- sleep cycles fired: 1
- freeze fires (eval, motor-override relaxed): 0
- safe-spawn retries (total across all segments): 1  (segments that exhausted 20 attempts: 0)

## Eval channel mean / max-std
- z_harm_s: mean=0.1936 max_std=0.03440 (varies)
- z_harm_un: mean=0.3840 max_std=0.06102 (varies)
- z_harm_a: mean=2.5124 max_std=1.48781 (varies)
- drive: mean=0.3396 max_std=0.20580 (varies)
- z_goal: mean=0.0244 max_std=0.07224 (varies)
- vigor: mean=0.0000 max_std=0.00000 (FLAT)
- override: mean=0.6755 max_std=0.05405 (varies)
- z_block: mean=0.1462 max_std=0.31141 (varies)
- excite: mean=14.0051 max_std=12.04164 (varies)
- dread: mean=1.0080 max_std=0.86260 (varies)

The `_episode_log.json` companion feeds fishtank_viz.html via /api/fishtank/logs, including
an `env_config` block for the viz's toroidal/reef badges, per-segment `done_cause`,
`sleep_cycle_fired_before_this_segment`, and (new in this iteration)
`spawn_safe_attempts` / `spawn_safe_exhausted` fields. **Whether this file reaches
origin/master depends on `PHASE3_SPOOL_SIDEFILES=1` being set on the hub and the pinned
worker -- see module docstring point 6. This is an infra/ops item, not something this
script can confirm or fix.**

## For a future `/failure-autopsy` (or any reader) on THIS run -- read before re-running anything

If `ecology_survivable` still reads FAIL despite the radius fix, the next things to check,
in order, are: (1) whether `total_spawn_safe_exhausted_segments` is nonzero (the grid may be
denser than estimated, or `SAFE_SPAWN_MAX_ATTEMPTS` too low for this layout), (2) the
per-segment `done_cause` breakdown in the episode_log (health_depleted vs step_limit -- a
lingering health_depleted majority despite the radius fix would point at hazard density
itself, per module docstring point 4, or a fourth drain channel not yet found), and (3) the
mean/max-std of the affect channels vs 906a's (a real behavioural shift vs an unrelated
non-degeneracy issue). The 906a-carried-forward telemetry-audit fields (residue_surprise,
footprint_at_cell, residue_stats_at_segment_start/final) remain available for tracing the
separately-registered unbounded-residue-valence finding (SD-RESIDUE-VALENCE-BOUND, pending
`/governance` ratification) without re-running anything live.
