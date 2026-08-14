# V3-EXQ-929 -- GAP-9 within-life sleep-trigger validation

**Status:** PASS -- label: `within_life_trigger_validated`
**Purpose:** diagnostic substrate-readiness validation (sleep_substrate:GAP-9, v1 ceiling arm).

Before GAP-9, REE's sleep trigger was boundary-only, so a TRUE single-continuous life
(num_episodes=1) could never sleep. This run validates the within-life trigger.

- seeds: [0, 1, 2]
- life length: 120 waking steps; step ceiling: 25
- OFF cycles fired (max across seeds): 0  (target 0)
- ON cycles fired (min across seeds): 4  (target >= 1)
- ON ceiling-arm fraction (min): 1.00  (target 1.0)
- C1 OFF silent: True | C2 ON fires: True | C3 ceiling arm: True

See `interpretation` for the pre-registered acceptance rule and per-condition preconditions,
and `per_condition_results` for the full per-seed x arm table.
