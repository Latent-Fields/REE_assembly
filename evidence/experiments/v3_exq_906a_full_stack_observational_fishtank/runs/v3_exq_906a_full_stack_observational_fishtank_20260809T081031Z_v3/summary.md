# V3-EXQ-906a -- Full-Stack Observational Fishtank Showcase (survivable, continuous)

**Status:** FAIL (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** bug-fix lettered iteration of V3-EXQ-906 (2026-08-09). 906's episodes died at
an average of ~15 realized steps (contamination-death bug, SD-094 trap #2) against a
configured-but-unreachable 600-step budget (env hard-caps at 500). This run fixes the
root cause (contamination_spread=0.0), corrects the budget to the real 500-step cap, and
restructures the eval phase as ONE continuous multi-segment observation of the SAME agent
(only the first segment fully resets it) instead of 30 successive fresh resets -- see
module docstring "CONTINUITY REDESIGN". Terminal cause (health_depleted / step_limit) and
a per-segment sleep-mode marker are now recorded into the episode_log for fishtank_viz.html.

- harm-pathway train steps (total): 3939
- z_goal activated at eval: True
- eval steps (total): 203  across 8 segments x up to 500 steps/seed
  (mean realized segment length: 25.4 steps -- 906's was ~14.9)
- segment endings: health_depleted=8 step_cap=0
- events: block=8 limb_damage=0 external_hazard=1 world_rule_shift=0
- sleep cycles fired: 0
- freeze fires (eval, motor-override relaxed): 0

## Eval channel mean / max-std
- z_harm_s: mean=0.2323 max_std=0.05076 (varies)
- z_harm_un: mean=0.4628 max_std=0.07181 (varies)
- z_harm_a: mean=3.5640 max_std=0.23410 (varies)
- drive: mean=0.0217 max_std=0.01632 (varies)
- z_goal: mean=0.3099 max_std=0.09027 (varies)
- vigor: mean=0.0000 max_std=0.00000 (FLAT)
- override: mean=0.5655 max_std=0.12070 (varies)
- z_block: mean=0.0000 max_std=0.00000 (FLAT)
- excite: mean=0.0400 max_std=0.03266 (varies)
- dread: mean=0.5431 max_std=0.21143 (varies)

The `_episode_log.json` companion feeds fishtank_viz.html (FISHTANK_VIZ_VERSION
2026-06-10.2 as of 906; may be bumped alongside a viz-side sleep-marker rendering
change, tracked separately) via /api/fishtank/logs, including an `env_config` block for
the viz's toroidal/reef badges, plus per-segment `done_cause` and
`sleep_cycle_fired_before_this_segment` fields new in this iteration.

## For a future `/failure-autopsy` (or any reader) on THIS run -- read before re-running anything

The survivability fix made a genuine substrate finding newly OBSERVABLE that no prior
fishtank run ever lived long enough to expose: sustained continuous exposure drives
`z_world_norm` and the residue-derived `excite`/`dread` channels far outside their
smoke-scale range (see module docstring point 6, "TELEMETRY AUDIT", for the full
mechanism -- an unclamped `RBFLayer.update_valence()` `+=` in `ree_core/residue/field.py`
fed every step by MECH-307 split-surprise writes onto a small, repeatedly-revisited set
of RBF centers). **Do not re-run this experiment live to check whether that is still
true or to quantify it further** -- this run's own `_episode_log.json` already carries
everything needed: per-step `residue_surprise` / `residue_write_fired` / `footprint_at_cell`
(the write-rate and revisit-rate driving it), per-segment-boundary
`residue_stats_at_segment_start` (`total_residue` / `active_centers` / `mean_weight` /
cumulative surprise-write count / `coverage_pct`), and per-seed
`residue_total_residue_final` / `residue_active_centers_final` /
`residue_surprise_write_count_final` in this manifest's own metrics -- a before/after
trajectory across the whole run is directly reconstructable from what is already recorded.
This is the SD-094 "recording gap" principle applied one level up: recording the raw
mechanism, not just its downstream symptom, is what makes a future diagnosis possible
without a multi-hour re-run. If this driver's survivability numbers, seed variance, or
the residue trajectory look worth a dedicated `/failure-autopsy` target, that target can
be built entirely from this manifest + episode_log.
