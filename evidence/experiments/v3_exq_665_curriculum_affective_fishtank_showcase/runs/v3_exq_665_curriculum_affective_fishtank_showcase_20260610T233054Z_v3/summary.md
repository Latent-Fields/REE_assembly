# V3-EXQ-665 -- Curriculum-trained Affective Fishtank Showcase

**Status:** PASS (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** Developmentally-scaffolded counterpart to V3-EXQ-664. Feeds
fishtank_viz.html with an affective episode_log from an agent trained through the
ScaffoldedSD054OnboardingScheduler curriculum + harm-pathway training.

- harm-pathway train steps (total): 2043  (harm streams TRAINED, unlike 664)
- z_goal activated at eval: True  (Stage-0 peaks per seed in metrics)
- freeze fires / blocked steps (eval): 0 / 0

## Eval channel mean / max-std (vs 664 for comparison)
- z_harm_s: mean=1.1000 max_std=0.17728 (varies)
- z_harm_un: mean=1.1150 max_std=0.18251 (varies)
- z_harm_a: mean=3.6804 max_std=0.01312 (varies)
- drive: mean=0.0075 max_std=0.00541 (varies)
- z_goal: mean=0.3740 max_std=0.02704 (varies)
- vigor: mean=0.0124 max_std=0.03933 (varies)
- override: mean=0.1577 max_std=0.08270 (varies)
- z_block: mean=0.0000 max_std=0.00000 (FLAT)
- excite: mean=0.0000 max_std=0.00000 (FLAT)
- dread: mean=0.0000 max_std=0.00000 (FLAT)

The `_episode_log.json` companion feeds fishtank_viz.html (FISHTANK_VIZ_VERSION
2026-06-10.2) via /api/fishtank/logs -- compare the suffering / wanting channels
against the raw-warmup V3-EXQ-664 run.
