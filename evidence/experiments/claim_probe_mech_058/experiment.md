# Experiment: claim_probe_mech_058

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `2026-02-17T225311Z_claim-probe-mech-058_seed89_ema_anchor_off_toyenv_internal_minimal` at `2026-02-17T22:53:11Z` signatures: mech058:anchor_separation_collapse
- `2026-02-17T225311Z_claim-probe-mech-058_seed71_ema_anchor_off_toyenv_internal_minimal` at `2026-02-17T22:53:11Z` signatures: mech058:anchor_separation_collapse
- `2026-02-17T225311Z_claim-probe-mech-058_seed53_ema_anchor_off_toyenv_internal_minimal` at `2026-02-17T22:53:11Z` signatures: mech058:anchor_separation_collapse

Recurring signatures:
- `mech058:anchor_separation_collapse` occurred in 6 FAIL run(s); latest `2026-02-17T225311Z_claim-probe-mech-058_seed89_ema_anchor_off_toyenv_internal_minimal`
- `mech058:ema_drift_under_shift` occurred in 1 FAIL run(s); latest `2026-02-17T225244Z_claim-probe-mech-058_seed29_ema_anchor_off_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `mech058:anchor_separation_collapse` (6 FAIL run(s), latest `2026-02-17T225311Z_claim-probe-mech-058_seed89_ema_anchor_off_toyenv_internal_minimal`).
- [ ] Investigate signature `mech058:ema_drift_under_shift` (1 FAIL run(s), latest `2026-02-17T225244Z_claim-probe-mech-058_seed29_ema_anchor_off_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
