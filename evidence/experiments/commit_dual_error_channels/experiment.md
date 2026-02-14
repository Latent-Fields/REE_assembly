# Experiment: commit_dual_error_channels

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z` at `2026-02-13T23:14:15.722633Z` signatures: mech060:precommit_channel_contamination, mech060:postcommit_channel_contamination, mech060:attribution_reliability_break
- `mech_060_memory_patch_cross_talk_s60011_20260213t231415722024z` at `2026-02-13T23:14:15.722141Z` signatures: mech060:precommit_channel_contamination, mech060:postcommit_channel_contamination, mech060:attribution_reliability_break
- `mech_060_leakage_prompt_injection_s60012_20260213t231415721523z` at `2026-02-13T23:14:15.721605Z` signatures: mech060:precommit_channel_contamination, mech060:postcommit_channel_contamination

Recurring signatures:
- `mech060:precommit_channel_contamination` occurred in 4 FAIL run(s); latest `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z`
- `mech060:postcommit_channel_contamination` occurred in 4 FAIL run(s); latest `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z`
- `mech060:attribution_reliability_break` occurred in 2 FAIL run(s); latest `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z`

Suggested design TODOs:
- [ ] Investigate signature `mech060:precommit_channel_contamination` (4 FAIL run(s), latest `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z`).
- [ ] Investigate signature `mech060:postcommit_channel_contamination` (4 FAIL run(s), latest `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z`).
- [ ] Investigate signature `mech060:attribution_reliability_break` (2 FAIL run(s), latest `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
