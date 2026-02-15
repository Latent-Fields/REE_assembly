# Experiment: commit_dual_error_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-15T140029Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal` at `2026-02-15T14:00:29Z` signatures: mech060:postcommit_channel_contamination, mech060:attribution_reliability_break, mech060:commitment_reversal_spike
- `2026-02-15T135835Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal` at `2026-02-15T13:58:35Z` signatures: mech060:postcommit_channel_contamination, mech060:attribution_reliability_break, mech060:commitment_reversal_spike
- `exp_0019_20260215T095129231597Z` at `2026-02-15T09:51:29.231597Z` signatures: none

Recurring signatures:
- `mech060:postcommit_channel_contamination` occurred in 12 FAIL run(s); latest `2026-02-15T140029Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal`
- `mech060:precommit_channel_contamination` occurred in 10 FAIL run(s); latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`
- `mech060:attribution_reliability_break` occurred in 10 FAIL run(s); latest `2026-02-15T140029Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal`
- `threshold:pre_commit_error_signal_to_noise` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`
- `threshold:post_commit_error_attribution_gain` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`
- `threshold:cross_channel_leakage_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`
- `threshold:commitment_reversal_rate` occurred in 5 FAIL run(s); latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`
- `mech060:commitment_reversal_spike` occurred in 2 FAIL run(s); latest `2026-02-15T140029Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `mech060:postcommit_channel_contamination` (12 FAIL run(s), latest `2026-02-15T140029Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal`).
- [ ] Investigate signature `mech060:precommit_channel_contamination` (10 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `mech060:attribution_reliability_break` (10 FAIL run(s), latest `2026-02-15T140029Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal`).
- [ ] Investigate signature `threshold:pre_commit_error_signal_to_noise` (5 FAIL run(s), latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`).
- [ ] Investigate signature `threshold:post_commit_error_attribution_gain` (5 FAIL run(s), latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`).
- [ ] Investigate signature `threshold:cross_channel_leakage_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
