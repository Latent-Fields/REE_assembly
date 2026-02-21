# Experiment: claim_probe_mech_060

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-21T150649Z_claim-probe-mech-060_seed47_single_error_stream_toyenv_internal_minimal` at `2026-02-21T15:06:49Z` signatures: mech060:postcommit_channel_contamination, mech060:attribution_reliability_break, mech060:commitment_reversal_spike
- `2026-02-21T150649Z_claim-probe-mech-060_seed29_single_error_stream_toyenv_internal_minimal` at `2026-02-21T15:06:49Z` signatures: mech060:postcommit_channel_contamination, mech060:attribution_reliability_break, mech060:commitment_reversal_spike
- `2026-02-21T150649Z_claim-probe-mech-060_seed11_single_error_stream_toyenv_internal_minimal` at `2026-02-21T15:06:49Z` signatures: mech060:postcommit_channel_contamination, mech060:attribution_reliability_break, mech060:commitment_reversal_spike

Recurring signatures:
- `mech060:postcommit_channel_contamination` occurred in 12 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-060_seed47_single_error_stream_toyenv_internal_minimal`
- `mech060:attribution_reliability_break` occurred in 12 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-060_seed47_single_error_stream_toyenv_internal_minimal`
- `mech060:commitment_reversal_spike` occurred in 12 FAIL run(s); latest `2026-02-21T150649Z_claim-probe-mech-060_seed47_single_error_stream_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `mech060:postcommit_channel_contamination` (12 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-060_seed47_single_error_stream_toyenv_internal_minimal`).
- [ ] Investigate signature `mech060:attribution_reliability_break` (12 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-060_seed47_single_error_stream_toyenv_internal_minimal`).
- [ ] Investigate signature `mech060:commitment_reversal_spike` (12 FAIL run(s), latest `2026-02-21T150649Z_claim-probe-mech-060_seed47_single_error_stream_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
