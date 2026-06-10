# V3-EXQ-664 -- Affective Fishtank Showcase

**Status:** PASS (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** Feed fishtank_viz.html with an episode_log exposing the protoemotional
register (nociceptive cascade z_harm_s/un/a, drive, wanting, vigor, orexin override,
blocked-agency assert pole, PAG freeze, MECH-307 excite/dread).

**Affect substrate:** SD-019a (z_harm_un), MECH-320 (vigor), SD-037 (override),
MECH-279 (PAG freeze, capped at 8), MECH-353 (blocked agency, env
action-blocks), MECH-307 split-surprise (excite/dread) -- on the 524 reef stack.

**Non-degeneracy (max std across seeds):**
- z_harm_s: 0.24369  (varies)
- z_harm_un: 0.12453  (varies)
- z_harm_a: 0.22263  (varies)
- drive: 0.34733  (varies)
- z_goal: 0.00000  (FLAT)
- vigor: 0.00000  (FLAT)
- override: 0.24575  (varies)
- z_block: 0.00000  (FLAT)
- excite: 2.39818  (varies)
- dread: 0.58551  (varies)
- freeze fires (total): 44 / 378 eval steps
- blocked steps (total): 14

## Per-seed
| Seed | reward | harm | std z_harm_a | std drive | std vigor | std z_block | freeze | blocked |
|------|--------|------|--------------|-----------|-----------|-------------|--------|---------|
| 0 | -1.055 | 1.055 | 0.0381 | 0.3473 | 0.0000 | 0.0000 | 11 | 6 |
| 1 | -0.958 | 1.206 | 0.0557 | 0.0352 | 0.0000 | 0.0000 | 20 | 1 |
| 2 | -1.006 | 1.087 | 0.2226 | 0.1800 | 0.0000 | 0.0000 | 13 | 7 |

The `_episode_log.json` companion is auto-discovered by fishtank_viz.html via
`/api/fishtank/logs`. Each step carries the affect fields above; the viz renders
the nociceptive cascade, drive/wanting/vigor/orexin bars, a bipolar dread/excite
meter, an assert bar, and FROZEN / ASSERTING behaviour modes.
