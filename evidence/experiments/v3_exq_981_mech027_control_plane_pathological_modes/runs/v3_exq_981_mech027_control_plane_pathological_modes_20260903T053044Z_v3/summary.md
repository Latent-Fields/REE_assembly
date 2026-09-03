# V3-EXQ-981 -- MECH-027: control-plane hypervigilance signature probe

**Overall Status:** FAIL  (label: `substrate_not_ready_requeue`, 1/2 load-bearing criteria)
**Claim:** MECH-027 -- hypervigilance is a mis-tuned regime of elevated
gain/precision + shortened prediction horizon + suppressed replay, not a
separate mechanism (scoped single-signature probe; see module docstring).
**Seeds:** [11, 23, 37]

## Per-seed ambiguous-band false-alarm rate

| Seed | Baseline | Hypervigilant | Reversion | Recovered frac | precision(base) | precision(HV) |
|---|---|---|---|---|---|---|
| 11 | 0.5303 | 0.5466 | 0.5572 | -0.6465 | 1.09e+05 | 9.606e+05 |
| 23 | 0.5060 | 0.5393 | 0.5529 | -0.4086 | 1.241e+05 | 9.656e+05 |
| 37 | 0.6949 | 0.4894 | 0.5959 | 0.5182 | 1.174e+05 | 9.724e+05 |

## Readiness (P0) preconditions

- precision_channel_non_degenerate: measured=8.271 threshold=5 met=True
- horizon_channel_non_degenerate: measured=0.201 threshold=0.5 met=True
- replay_channel_non_degenerate: measured=0 threshold=0 met=True
- replay_channel_baseline_reachable: measured=0 threshold=1 met=False
- sleep_cycle_fires_during_eval: measured=25 threshold=1 met=True
- precision_scaled_commit_temperature_engaged: measured=0.7542 threshold=0.05 met=True
- precision_margin_norm_elevated_under_hv: measured=0.0001944 threshold=0.01 met=False
- commit_temperature_reduced_under_hv: measured=0.0001907 threshold=0.01 met=False
- positive_control_hazard_sensitivity: measured=-0.4307 threshold=0.05 met=False
- hazard_bin_sample_coverage: measured=10 threshold=5 met=True
- no_fatal_action_selection_errors: measured=0 threshold=0.5 met=True

## Criteria

- C1 (LOAD-BEARING) false-alarm elevation: FAIL (mean_hv=0.5251 vs 2x mean_base=1.1542, base_max=0.6949)
- C2 (LOAD-BEARING) reversion recovery: PASS (pooled_recovered_fraction=0.8377, per-seed-mean=-0.1790 [diagnostic only], vs floor 0.5)

overall_pass = READY (all P0 preconditions met) AND non_degenerate AND C1 (HV ambiguous-band false-alarm rate >= 2x baseline AND outside baseline's own across-seed range) AND C2 (>= 50% of the elevation reverts in the EVAL_REVERSION block, same agent, channels restored to baseline). Any P0 precondition unmet routes to substrate_not_ready_requeue.
