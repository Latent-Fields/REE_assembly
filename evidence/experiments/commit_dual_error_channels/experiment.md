# Experiment: commit_dual_error_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z` at `2026-02-14T18:53:25.221110Z` signatures: mech060:precommit_channel_contamination, mech060:postcommit_channel_contamination, mech060:attribution_reliability_break
- `bridge_v2_mech_060_cross_channel_contamination_stress_s60021_20260214t185325220131z` at `2026-02-14T18:53:25.220388Z` signatures: mech060:precommit_channel_contamination, mech060:postcommit_channel_contamination, mech060:attribution_reliability_break
- `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t184853457259z` at `2026-02-14T18:48:53.457429Z` signatures: mech060:precommit_channel_contamination, mech060:postcommit_channel_contamination, mech060:attribution_reliability_break

Recurring signatures:
- `mech060:precommit_channel_contamination` occurred in 10 FAIL run(s); latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`
- `mech060:postcommit_channel_contamination` occurred in 10 FAIL run(s); latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`
- `mech060:attribution_reliability_break` occurred in 8 FAIL run(s); latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`
- `threshold:pre_commit_error_signal_to_noise` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`
- `threshold:post_commit_error_attribution_gain` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`
- `threshold:cross_channel_leakage_rate` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`
- `threshold:commitment_reversal_rate` occurred in 2 FAIL run(s); latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`

Suggested design TODOs:
- [ ] Investigate signature `mech060:precommit_channel_contamination` (10 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `mech060:postcommit_channel_contamination` (10 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `mech060:attribution_reliability_break` (8 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `threshold:pre_commit_error_signal_to_noise` (2 FAIL run(s), latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`).
- [ ] Investigate signature `threshold:post_commit_error_attribution_gain` (2 FAIL run(s), latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`).
- [ ] Investigate signature `threshold:cross_channel_leakage_rate` (2 FAIL run(s), latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
