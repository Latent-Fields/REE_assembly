# V3-EXQ-909 -- Sleep-Refinement DV Probe (multi-firing, multi-seed)

**Status:** PASS -- label: `sleep_dv_nonnull_detected`
**Purpose:** diagnostic discrimination, successor probe to V3-EXQ-906b (observational review
Section 13-C track C). Does the sleep-refinement DV (SWS slot diversity / REM replay
diversity) register a non-null waking->sleep difference on the repertoire-diverse-but-
non-converting fishtank substrate?

- seeds: [0, 1, 2]
- total sleep-cycle firings: 45 (target >= 10)
- draws_per_cycle (structural, min across seeds): 50
- mean waking mode-entropy across just-completed segments: 1.4545 bits
- sws_slot_diversity: min=0.0000 mean=0.0002 median=0.0001 max=0.0009
- replay_diversity_index: min=0.0200 mean=0.0200 median=0.0200 max=0.0200
- fraction of firings at the -1.0 zero-draws sentinel: 0.000
- fraction of firings classified non-null (pre-registered epsilons): 1.000
- r(waking mode-entropy, sws_slot_diversity): 0.39319138053742475
- r(waking mode-entropy, replay_diversity_index): None

See `interpretation.note` for the pre-registered discrimination rule and `sleep_firing_records`
in the episode-log companion file for the full per-firing table.
