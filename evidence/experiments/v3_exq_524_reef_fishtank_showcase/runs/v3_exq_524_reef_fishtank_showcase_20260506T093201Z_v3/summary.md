# V3-EXQ-524 -- Reef Fishtank Showcase

**Status:** N/A (diagnostic showcase -- not scored)
**Purpose:** Reef-aware fishtank_viz.html episode log with shelter mode, reef zone
overlay, and zone-transition labels (reef_entry / reef_exit).

**Substrate enabled:** SD-007 (reafference), SD-008 (alpha_world=0.9), SD-010
(sensory harm stream), SD-011 (affective harm stream + history), SD-012
(drive-modulated goal), SD-018 (resource proximity supervision), SD-021
(descending modulation), SD-050 (reef enrichment: n_patches=3 radius=2
hazard_food_attraction=0.7), MECH-090 (bistable beta gate).

**Grid:** 12x12 non-toroidal | **Reef cells:** ~33 (corners (2,2), (2,9), (9,2)) |
**Hazard food attraction:** 0.7 (hazards chase food -- creates flee-to-reef incentive)

**Warmup:** 60 eps | **Eval:** 5 eps | **Steps/ep:** 200

## Per-seed Metrics

| Seed | W-first10 | W-last10 | W-delta | eval reward | eval harm | n_cands |
|------|-----------|----------|---------|-------------|-----------|---------|
| 0 | -0.5443 | -1.0892 | -0.5449 | -0.0693 | 0.3964 | 32.0 |
| 1 | -0.6682 | -0.6242 | 0.0440 | -0.6328 | 0.6328 | 32.0 |
| 2 | -0.3518 | -1.0275 | -0.6756 | -0.5008 | 0.5830 | 32.0 |

The `_episode_log.json` companion file is the payload fishtank_viz.html
auto-discovers via `/api/fishtank/logs`. Each episode record carries `reef_cells`
([[x,y], ...]) and each step carries `in_reef` (bool). The viz renders teal zone
overlay, REEF ZONE / OPEN WATER indicator, and shelter mode (cyan) for agents
retreating to reef under threat.
