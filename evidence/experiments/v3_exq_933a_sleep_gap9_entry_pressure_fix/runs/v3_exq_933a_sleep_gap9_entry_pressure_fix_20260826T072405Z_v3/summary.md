# V3-EXQ-933a -- SD-SLEEP-ENTRY-PRESSURE (GAP-9 follow-up) validation

**Status:** PASS -- label: `entry_pressure_fix_validated`
**Purpose:** diagnostic CONSUMER validation (sleep_substrate:SD-SLEEP-ENTRY-PRESSURE).

Reproduces V3-EXQ-933's exact NEED_SUB (demand 0.1, threshold
0.5) and NEED_HIGH (demand 1.0) conditions against the new
entry_pressure_crossed() mechanism (a running SUM + steps_since_sleep refractory floor,
distinct from need_crossed()'s time-invariant MEAN).

- seeds: [0, 1, 2]; life length: 120 waking steps; refractory: 2 steps
- C1 PRESSURE_SUB crosses in bounded time (Process-S fix, was 0/120 fires): True
- C2 PRESSURE_HIGH fire rate strictly < 1/step (refractory fix, was 120/120 fires): True
- C3 CEILING (lever OFF) reproduces the pre-fix baseline exactly, pressure arm inert: True

See `interpretation` for the pre-registered acceptance rule and readiness preconditions, and
`per_condition_results` for the full per-seed x arm table.
