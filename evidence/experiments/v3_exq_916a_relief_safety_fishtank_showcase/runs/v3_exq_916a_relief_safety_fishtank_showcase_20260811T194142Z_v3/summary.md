# V3-EXQ-916a -- Relief/Safety Fishtank Showcase (residue_wanting writer fix)

**Status:** PASS (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** Follow-on to V3-EXQ-664. Feeds fishtank_viz.html with an episode_log that
additionally exposes MECH-302 (relief-completion), MECH-304 (cue-specific safety) and
MECH-303 (contextual safety terrain) -- real, validated substrate that no prior Fishtank
driver ever enabled (each sits behind its own default-False REEConfig flag).

**Affect substrate (inherited from 664):** SD-019a (z_harm_un), MECH-320 (vigor), SD-037
(override), MECH-279 (PAG freeze, capped at 8), MECH-353 (blocked agency,
env action-blocks), MECH-307 split-surprise (excite/dread) -- on the 524 reef stack.

**Relief/safety substrate (NEW this experiment):** MECH-302 (suffering-derivative
comparator -> relief_event), MECH-304 (conditioned safety store -> safety_cue_signal),
MECH-303 (contextual safety terrain -> safety_terrain_read).

**Non-degeneracy (max std across seeds):**
- z_harm_s: 0.20780  (varies)
- z_harm_un: 0.15134  (varies)
- z_harm_a: 0.66521  (varies)
- drive: 0.36466  (varies)
- z_goal: 0.07800  (varies)
- vigor: 0.00000  (FLAT)
- override: 0.24222  (varies)
- z_block: 0.00000  (FLAT)
- excite: 6.57770  (varies)
- dread: 0.76207  (varies)
- safety_cue_signal: 0.42916  (varies)
- safety_terrain_read: 0.00000  (FLAT)
- residue_wanting: 0.56797  (varies)
- freeze fires (total): 176 / 1013 eval steps
- blocked steps (total): 30
- relief fires (total, MECH-302): 60 / 1013 eval steps

## Per-seed
| Seed | reward | harm | std z_harm_a | std drive | std vigor | std z_block | freeze | blocked | relief |
|------|--------|------|--------------|-----------|-----------|-------------|--------|---------|--------|
| 0 | -0.756 | 0.918 | 0.6652 | 0.3515 | 0.0000 | 0.0000 | 79 | 15 | 58 |
| 1 | -1.013 | 1.093 | 0.4631 | 0.3647 | 0.0000 | 0.0000 | 31 | 7 | 0 |
| 2 | -0.889 | 1.132 | 0.1156 | 0.1908 | 0.0000 | 0.0000 | 66 | 8 | 2 |

The `_episode_log.json` companion is auto-discovered by fishtank_viz.html via
`/api/fishtank/logs`. Each step carries the 664 affect fields plus relief_event /
safety_cue_signal / safety_terrain_read; the viz renders the nociceptive cascade,
drive/wanting/vigor/orexin bars, a bipolar dread/excite meter, an assert bar, FROZEN /
ASSERTING behaviour modes, and (new) relief/safety bars with graceful degradation for
older logs that predate this telemetry.
