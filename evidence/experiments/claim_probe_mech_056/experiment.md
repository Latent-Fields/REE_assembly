# Experiment: claim_probe_mech_056

## What it tests

- Core question: are observed failures in `MECH-056` caused by true latent-geometry distortion, or by
  valence-weighted hippocampal remapping that changes retrieval and path selection without damaging core geometry?
- Hypothesis under test:
  - `H_distortion`: valence pressure directly distorts latent geometry (representation quality degradation).
  - `H_competition`: valence pressure primarily changes hippocampal mapping/retrieval weighting; geometry remains
    largely intact and failures are routing/readout-driven.
- Claim linkage:
  - primary: `MECH-056`
  - secondary cross-checks: `MECH-057`, `Q-013`, `Q-014`

## Probe design (2x2 factorial)

Use matched seeds across all four conditions and identical scenario traces:

| condition_id | valence_channel | hippocampal_mapping | short label |
|---|---|---|---|
| `C1` | on | adaptive | `V+_H+` |
| `C2` | on | frozen | `V+_H-` |
| `C3` | off_or_neutral | adaptive | `V-_H+` |
| `C4` | off_or_neutral | frozen | `V-_H-` |

Minimum run policy:

- at least 3 matched seeds per condition (`12` runs minimum),
- additional seeds if variance on geometry metrics exceeds 10% between adjacent seeds.

## Required metrics (metrics.json values)

Geometry stability metrics:

- `latent_procrustes_drift` (lower is better)
- `latent_knn_overlap` (higher is better)
- `latent_trustworthiness` (higher is better)
- `latent_continuity` (higher is better)

Hippocampal mapping and retrieval metrics:

- `hippocampal_retrieval_valence_skew`
- `hippocampal_path_selection_entropy`
- `valence_conditioned_recall_error`

Downstream behavioral/control metrics:

- `policy_error_rate`
- `commitment_reversal_rate`
- `conflict_signature_rate`

## Failure modes it detects

- `mech056:latent_geometry_distortion`
  - trigger: geometry metrics degrade materially whenever valence is on, including frozen mapping (`C2` vs `C4`).
- `mech056:valence_mapping_competition`
  - trigger: geometry remains near-stable, but retrieval/path metrics shift sharply with adaptive mapping
    (`C1` vs `C2`, and `C3` vs `C4`).
- `mech056:mixed_coupling_instability`
  - trigger: both geometry degradation and mapping-skew signatures rise under valence-on adaptive mode (`C1`).
- Existing signatures still relevant for this lane:
  - `ledger_editing`
  - `domination_lock_in`
  - `explanation_policy_divergence`

## Falsification and interpretation rules

Use `C4` (`V-_H-`) as baseline.

- Distortion-dominant support:
  - `latent_procrustes_drift(C2)` increases by >= 20% vs `C4`, and
  - at least two of `{latent_knn_overlap, latent_trustworthiness, latent_continuity}` worsen by >= 10% in `C2`.
- Competition-dominant support:
  - geometry metrics in `C1` and `C2` stay within 5% of `C4`, but
  - `hippocampal_retrieval_valence_skew(C1)` or `valence_conditioned_recall_error(C1)` worsen by >= 20% vs `C2`.
- Mixed-coupling support:
  - both distortion and competition criteria are met in the same seed block.

If none of these thresholds hold, classify as `inconclusive` and increase seed count.

## Required pack fields and scenario tagging

In each run `manifest.json`, include:

- `claim_ids_tested`: must include `MECH-056`
- `evidence_direction`: `supports`, `weakens`, `mixed`, or `unknown`
- `scenario` fields that encode condition toggles:
  - `valence_channel_mode`: `on` or `off_or_neutral`
  - `hippocampal_mapping_mode`: `adaptive` or `frozen`
  - matched `seed`

Suggested run_id suffix pattern:

- `..._valence_on_mapping_adaptive_...`
- `..._valence_on_mapping_frozen_...`
- `..._valence_off_mapping_adaptive_...`
- `..._valence_off_mapping_frozen_...`

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
Recent failure runs:
- `20260226T194240_claim_probe_mech_056_ree_v1_minimal` at `2026-02-26T19:42:40Z` signatures: none
- `2026-02-22T203715Z_claim-probe-mech-056_seed47_valence_off_or_neutral_mapping_frozen_toyenv_internal_minimal` at `2026-02-22T20:37:15Z` signatures: ledger_editing, domination_lock_in
- `2026-02-22T203713Z_claim-probe-mech-056_seed11_valence_off_or_neutral_mapping_frozen_toyenv_internal_minimal` at `2026-02-22T20:37:13Z` signatures: ledger_editing, domination_lock_in

Recurring signatures:
- `ledger_editing` occurred in 35 FAIL run(s); latest `2026-02-22T203715Z_claim-probe-mech-056_seed47_valence_off_or_neutral_mapping_frozen_toyenv_internal_minimal`
- `domination_lock_in` occurred in 26 FAIL run(s); latest `2026-02-22T203715Z_claim-probe-mech-056_seed47_valence_off_or_neutral_mapping_frozen_toyenv_internal_minimal`
- `explanation_policy_divergence` occurred in 18 FAIL run(s); latest `2026-02-22T203710Z_claim-probe-mech-056_seed47_valence_on_mapping_frozen_toyenv_internal_minimal`
- `mech056:valence_mapping_competition` occurred in 3 FAIL run(s); latest `2026-02-22T203707Z_claim-probe-mech-056_seed47_valence_on_mapping_adaptive_toyenv_internal_minimal`
- `mech056:latent_geometry_distortion` occurred in 3 FAIL run(s); latest `2026-02-22T203710Z_claim-probe-mech-056_seed47_valence_on_mapping_frozen_toyenv_internal_minimal`

Suggested design TODOs:
- [ ] Investigate signature `ledger_editing` (35 FAIL run(s), latest `2026-02-22T203715Z_claim-probe-mech-056_seed47_valence_off_or_neutral_mapping_frozen_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (26 FAIL run(s), latest `2026-02-22T203715Z_claim-probe-mech-056_seed47_valence_off_or_neutral_mapping_frozen_toyenv_internal_minimal`).
- [ ] Investigate signature `explanation_policy_divergence` (18 FAIL run(s), latest `2026-02-22T203710Z_claim-probe-mech-056_seed47_valence_on_mapping_frozen_toyenv_internal_minimal`).
- [ ] Investigate signature `mech056:valence_mapping_competition` (3 FAIL run(s), latest `2026-02-22T203707Z_claim-probe-mech-056_seed47_valence_on_mapping_adaptive_toyenv_internal_minimal`).
- [ ] Investigate signature `mech056:latent_geometry_distortion` (3 FAIL run(s), latest `2026-02-22T203710Z_claim-probe-mech-056_seed47_valence_on_mapping_frozen_toyenv_internal_minimal`).
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
