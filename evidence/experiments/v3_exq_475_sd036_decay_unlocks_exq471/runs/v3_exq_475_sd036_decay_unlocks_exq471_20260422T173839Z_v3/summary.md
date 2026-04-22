# V3-EXQ-475 -- SD-036 GABAergic Decay Unlocks EXQ-471

**Status:** N/A (diagnostic -- not scored)
**Purpose:** Diagnostic re-run of EXQ-471 with SD-036 GABAergic cross-stream decay
regulator and MECH-279 PAG freeze-gate enabled. Hypothesis: tonic decay on
z_harm_s / z_harm_a / z_beta unlocks the EXQ-471 monostrategy lock-in by
providing a relaxation mechanism that lets the salience coordinator / dACC
bundle re-enter alternative operating modes.

**Substrate enabled (delta vs EXQ-471):** SD-036 (use_gabaergic_decay=True),
MECH-279 (use_pag_freeze_gate=True). All other EXQ-471 flags retained.

**Reference:** V3-EXQ-471 (best-available agent fishtank showcase) -- NOT a
supersede. EXQ-471 stands as the no-decay baseline; EXQ-475 is the matched
diagnostic with SD-036 ON.

**Warmup:** 60 eps | **Eval:** 5 eps | **Steps/ep:** 200

## Per-seed Metrics

| Seed | W-first10 | W-last10 | W-delta | eval reward | eval harm | n_cands | pag_commits | pag_releases | freeze_active |
|------|-----------|----------|---------|-------------|-----------|---------|-------------|--------------|---------------|
| 0 | -0.2927 | -0.2543 | 0.0384 | -0.0960 | 0.3441 | 32.0 | 71 | 6 | 1000 |
| 1 | -0.1954 | -0.3320 | -0.1366 | -0.3996 | 0.3996 | 32.0 | 70 | 5 | 1000 |
| 2 | -0.8955 | -0.1272 | 0.7684 | -0.2466 | 0.3245 | 32.0 | 64 | 5 | 1000 |

The `_episode_log.json` companion file is the payload fishtank_viz.html
auto-discovers via `/api/fishtank/logs`.
