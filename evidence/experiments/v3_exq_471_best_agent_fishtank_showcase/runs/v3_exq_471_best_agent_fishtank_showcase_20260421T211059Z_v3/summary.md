# V3-EXQ-471 -- Best-Available V3 Agent Fishtank Showcase

**Status:** N/A (diagnostic demo -- not scored)
**Purpose:** Showcase a full-stack V3 agent in fishtank_viz.html. All smoke-passed
substrate flags turned on; phased-training-required or still-under-validation
substrates left off.

**Substrate enabled:** SD-007 (reafference), SD-008 (alpha_world=0.9), SD-010
(sensory harm stream), SD-011 (affective harm stream + history), SD-012
(drive-modulated goal), SD-018 (resource proximity supervision), SD-021
(descending modulation), SD-022 (directional limb damage), SD-023 (Landmark B),
MECH-090 (bistable beta gate).

**Warmup:** 60 eps | **Eval:** 5 eps | **Steps/ep:** 200

## Per-seed Metrics

| Seed | W-first10 | W-last10 | W-delta | eval reward | eval harm | n_cands |
|------|-----------|----------|---------|-------------|-----------|---------|
| 0 | -0.2760 | -0.2170 | 0.0589 | -0.0830 | 0.3243 | 32.0 |
| 1 | -0.1083 | -0.2858 | -0.1775 | -0.2001 | 0.2847 | 32.0 |
| 2 | -0.5306 | -1.0478 | -0.5172 | -0.3716 | 0.6140 | 32.0 |

The `_episode_log.json` companion file is the payload fishtank_viz.html
auto-discovers via `/api/fishtank/logs`.
