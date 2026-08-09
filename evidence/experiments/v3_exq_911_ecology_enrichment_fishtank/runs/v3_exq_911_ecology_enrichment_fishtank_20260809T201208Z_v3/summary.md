# V3-EXQ-911 -- Ecology Enrichment for Discrete-Resource Acquisition

**Status:** PASS (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** Section 9 item 3 of the 906b observational review
(observational_review_V3-EXQ-906b_2026-08-09.md), explicitly LOWER PRIORITY than tracks
A/C/906c. Section 2b of that review found 906b's "food-seeking" was overwhelmingly ambient
proximity/reef-gradient exploitation, not discrete-resource navigation (mean distance to
nearest resource ~6.2 cells regardless of whether the agent was receiving benefit). This run
re-tunes the resource side of the ecology (hazard side unchanged from 906b) so a future
food-seeking metric on this ecology would measure real navigation instead of gradient-sitting.

## What changed vs 906b (resource side only)
- `resource_field_decay`: 0.5 -> 3.0 (root-cause fix -- see module docstring for the
  Monte-Carlo grid-search that chose this value, mirroring 906b's own hazard-field methodology)
- `proximity_benefit_scale`: 0.03 -> 0.01 (sharper ambient-vs-discrete contrast)
- `resource_respawn_on_consume`: False -> True (SD-012, already-GA mechanism -- lets
  consumption recur through a segment instead of the resource pool depleting)

## Confound-reduction result (the direct falsifier for this run's purpose)
- mean distance to nearest resource, ALL steps: 4.25
  (906b baseline: 6.23)
- mean distance to nearest resource, `benefit_approach` steps: 1.29
  (906b baseline: 6.02; n=68
  vs sample floor 20; PASS threshold <= 3.0)
- genuine `resource` consumption events: 20
  (906b baseline, fixed non-respawning pool: 11; reported
  only, NOT load-bearing -- see module docstring point 3)
- mean distance at consume events (trivially ~0 by construction, reported only):
  0.05

## Ecology-survivability sanity check (unchanged gate from 906b/906c)
- harm-pathway train steps (total): 3735
- eval steps (total): 4000  across 8 segments x up to 500 steps/seed
  (mean realized segment length: 500.0 steps -- unchanged gate from 906b)
- segment endings: health_depleted=0 step_cap=8
- sleep cycles fired: 1
- freeze fires (eval, motor-override relaxed): 0

The `_episode_log.json` companion feeds fishtank_viz.html via /api/fishtank/logs, same schema
as 906b/906c.
