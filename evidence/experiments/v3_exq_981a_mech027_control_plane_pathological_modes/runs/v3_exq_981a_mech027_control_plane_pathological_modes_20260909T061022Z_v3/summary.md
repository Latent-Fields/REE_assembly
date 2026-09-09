# V3-EXQ-981a -- MECH-027 (Stage A abort)

**Overall Status:** FAIL (label `substrate_not_ready_requeue`)
**Unmet Gate A preconditions:** ['positive_control_hazard_sensitivity']
**Seeds:** [11, 23, 37]

## Gate A preconditions

- positive_control_hazard_sensitivity: measured=-0.0957542 threshold=0.05 met=False
- hazard_bin_sample_coverage: measured=70 threshold=30 met=True
- positive_control_band_pooled_coverage: measured=342 threshold=150 met=True
- replay_channel_baseline_reachable: measured=5 threshold=1 met=True
- no_fatal_action_selection_errors_stage_a: measured=0 threshold=0.5 met=True
- c1_elevation_headroom: measured=0.945931 threshold=0.2 met=True
- precision_margin_headroom: measured=0.61066 threshold=0.05 met=True

Gate A (the DV/env pairing gate) is evaluated after EVAL_BASELINE and BEFORE EVAL_HYPERVIGILANT / EVAL_REVERSION are run at all. Any unmet Gate A precondition routes to substrate_not_ready_requeue and the hypervigilance blocks are skipped.
