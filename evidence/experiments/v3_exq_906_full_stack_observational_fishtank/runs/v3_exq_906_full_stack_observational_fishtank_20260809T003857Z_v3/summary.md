# V3-EXQ-906 -- Full-Stack Observational Fishtank Showcase

**Status:** PASS (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** current-substrate successor to V3-EXQ-665 (2026-06-10). Feeds
fishtank_viz.html with a long, richly-instrumented, minimally-hand-tuned episode_log
from an agent trained through the full onboarding curriculum with the broadest
mechanically-stable feature combination this substrate currently supports.

- harm-pathway train steps (total): 3794
- z_goal activated at eval: True
- eval steps (total): 447  across 30 eps x 600 steps/seed
- events: block=10 limb_damage=0 external_hazard=0 world_rule_shift=1
- sleep cycles fired: 3
- freeze fires (eval, motor-override relaxed): 0

## Eval channel mean / max-std
- z_harm_s: mean=0.2962 max_std=0.16199 (varies)
- z_harm_un: mean=0.5965 max_std=0.17225 (varies)
- z_harm_a: mean=3.8337 max_std=0.34385 (varies)
- drive: mean=0.0202 max_std=0.02503 (varies)
- z_goal: mean=0.2065 max_std=0.12847 (varies)
- vigor: mean=0.0000 max_std=0.00000 (FLAT)
- override: mean=0.2550 max_std=0.16734 (varies)
- z_block: mean=0.0000 max_std=0.00000 (FLAT)
- excite: mean=0.3398 max_std=0.14707 (varies)
- dread: mean=0.4041 max_std=0.35408 (varies)

The `_episode_log.json` companion feeds fishtank_viz.html (FISHTANK_VIZ_VERSION
2026-06-10.2) via /api/fishtank/logs, including an `env_config` block for the
viz's toroidal/reef badges (665's episode_log omitted this -- see driver note).
