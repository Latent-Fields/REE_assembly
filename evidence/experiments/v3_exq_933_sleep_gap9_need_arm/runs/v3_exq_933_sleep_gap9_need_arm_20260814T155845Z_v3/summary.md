# V3-EXQ-933 -- GAP-9 MEL/need-crossing PRIMARY arm validation

**Status:** PASS -- label: `need_arm_validated`
**Purpose:** diagnostic CONSUMER validation (sleep_substrate:GAP-9 design (b), the need arm).

Validates the MEL/need-crossing PRIMARY arm the v1 ceiling-only build (V3-EXQ-929) left as a
placeholder. Controlled MEL stimulus (the ecological producer is parked -- GAP-5b/718a), driving
the need arm through the same note_step_pe -> need_crossed() -> notify_waking_step path a real
non-converging environment would.

- seeds: [0, 1, 2]; life length: 120 waking steps
- threshold: 0.5; injected MEL high/sub: 1.0/0.1
- C1 NEED_HIGH need-arm fires & carries: True
- C2 NEED_HIGH fires sooner than ceiling: True
- C3 NEED_SUB threshold-gates (need frac 0): True
- C4 CEILING reproduces v1 (all ceiling arm): True

See `interpretation` for the pre-registered acceptance rule and readiness preconditions, and
`per_condition_results` for the full per-seed x arm table.
