# V3-EXQ-906c -- Full-Stack Observational Fishtank: Appetitive-Sequence + Coupling Instrumentation

**Status:** PASS (diagnostic telemetry showcase -- not scored against any claim)
**Purpose:** Section 9 item 1 of the 906b observational review
(observational_review_V3-EXQ-906b_2026-08-09.md). Same ecology as 906b, unchanged (no
`supersedes`) -- this run adds two things: (1) manifest-level aggregation for the
residue_wanting/liking/surprise channels `_read_affect` now surfaces per-step (landed by a
sibling chip before this script was authored), and (2) six affect->behaviour lagged/
contemporaneous coupling metrics as first-class manifest fields, the same ones the review
computed post-hoc by re-reading 906b's raw episode log.

- harm-pathway train steps (total): 3898
- z_goal activated at eval: True
- eval steps (total): 3793  across 8 segments x up to 500 steps/seed
  (mean realized segment length: 474.1 steps -- unchanged gate from 906b)
- segment endings: health_depleted=1 step_cap=7
- sleep cycles fired: 1
- freeze fires (eval, motor-override relaxed): 0

## New: appetitive-channel aggregation
- residue_wanting: mean=0.0000 std=0.0000 (n=3793)
- liking: mean=19.8812 std=10.4847 (n=3793)
- surprise (VALENCE_SURPRISE read-back): mean=5.1537 std=4.5009 (n=3793)

## New: affect->behaviour coupling metrics (Section 4/12b, now first-class)
- dread(t) -> harm in t+1..t+3: r=0.1053 (n=3785)
- z_goal(t) -> approach at t+1: r=0.0692 (n=3785)
- z_goal(t) -> benefit in t+1..t+3: r=-0.0480 (n=3785)
- dread <-> z_harm_a (contemporaneous): r=-0.1753 (n=3793)
- excite <-> benefit signal (contemporaneous, **UNRELIABLE -- see interpretation.preconditions, SD-RESIDUE-VALENCE-BOUND not yet landed**): r=-0.0131 (n=3793)
- surprise-spike (p90=0.04) -> mode-change @ t+1: 17.1% (spike, n=123) vs 12.0% (no spike, n=3662)
- surprise-spike (p90) -> moved @ t+1: 45.5% (spike) vs 20.8% (no spike)

The `_episode_log.json` companion feeds fishtank_viz.html via /api/fishtank/logs, same as
906b -- unchanged episode_log schema, now also carrying residue_wanting/liking/surprise per
step (inherited from the sibling telemetry chip, not from this driver).
