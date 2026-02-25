# Experiment Regime Coverage

Generated: `2026-02-25T19:52:33.269382Z`

## Regime Definitions

- `toy_qualification`: primary mechanism harness (typically `ree-v2` toy qualification runs).
- `synthetic_stress`: adversarial stress lane (typically `ree-experiments-lab`).
- `runtime_authority`: runtime authority/commit boundary execution lane (typically `ree-openclaw`).
- `backstop_contract`: contract emitter parity lane (typically `ree-v1-minimal`, non-authoritative).
- `literature_connectome`: external constraint lane (connectome/literature pulls).

## Summary

- active_claims: `7`
- claims_with_missing_regimes: `0`
- claims_missing_runtime_authority: `0`
- claims_missing_synthetic_stress: `0`
- claims_missing_literature_connectome: `0`

## Producer Freshness

| repo | latest_sync_utc | status | imports | report |
|---|---|---|---:|---|
| `ree-experiments-lab` | `2026-02-25T19:51:10.874283Z` | `ok` | `24` | `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260225T195113Z_handoff_sync_report.json` |
| `ree-openclaw` | `2026-02-25T19:51:10.874283Z` | `ok` | `2` | `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260225T195113Z_handoff_sync_report.json` |
| `ree-v1-minimal` | `2026-02-25T18:59:08.448087Z` | `ok` | `16` | `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260225T185910Z_handoff_sync_report.json` |
| `ree-v2` | `2026-02-25T17:15:34.582206Z` | `ok` | `943` | `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260225T171536Z_handoff_sync_report.json` |

## Claim Matrix

| claim_id | conflict_ratio | required_regimes | covered_regimes | missing_regimes | proposal_refs | nuance_gap_flags |
|---|---:|---|---|---|---|---|
| `MECH-056` | `0.618` | `runtime_authority, synthetic_stress, toy_qualification` | `backstop_contract, runtime_authority, synthetic_stress, toy_qualification` | `none` | `EXP-0016@ree-v2:trajectory_integrity:discriminative_pair` | `none` |
| `MECH-057` | `0.75` | `runtime_authority, synthetic_stress, toy_qualification` | `runtime_authority, synthetic_stress, toy_qualification` | `none` | `EXP-0025@ree-experiments-lab:claim_probe_mech_057:discriminative_pair` | `none` |
| `MECH-058` | `0.871` | `literature_connectome, synthetic_stress, toy_qualification` | `backstop_contract, literature_connectome, synthetic_stress, toy_qualification` | `none` | `none` | `high_conflict_despite_lane_coverage` |
| `MECH-059` | `0.566` | `synthetic_stress, toy_qualification` | `backstop_contract, synthetic_stress, toy_qualification` | `none` | `EXP-0020@ree-v2:jepa_uncertainty_channels:discriminative_pair` | `none` |
| `MECH-060` | `0.865` | `literature_connectome, runtime_authority, synthetic_stress, toy_qualification` | `backstop_contract, literature_connectome, runtime_authority, synthetic_stress, toy_qualification` | `none` | `none` | `high_conflict_despite_lane_coverage` |
| `MECH-061` | `0.667` | `runtime_authority, synthetic_stress, toy_qualification` | `runtime_authority, synthetic_stress, toy_qualification` | `none` | `EXP-0014@ree-v2:claim_probe_mech_061:discriminative_pair` | `none` |
| `Q-017` | `0.835` | `literature_connectome, runtime_authority, toy_qualification` | `literature_connectome, runtime_authority, synthetic_stress, toy_qualification` | `none` | `none` | `high_conflict_despite_lane_coverage` |

## Priority Gaps

- Runtime authority lane missing:
  - none
- Synthetic stress lane missing:
  - none
- Literature/connectome lane missing:
  - none
