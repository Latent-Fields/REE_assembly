# SD-037 Axis (b) Phase 1b -- C3 Dynamic-Crossings Redesign + MECH-341

- Queue id: `V3-EXQ-625c`
- Run id: `v3_exq_625c_sd037_axis_b_phase1b_dynamic_crossings_mech341_20260602T072226Z_v3`
- Timestamp UTC: `20260602T072226Z`
- Supersedes: `V3-EXQ-625b`
- Manifest: `evidence/experiments/v3_exq_625c_sd037_axis_b_phase1b_dynamic_crossings_mech341_20260602T072226Z_v3.json`
- Plan: [sd_037_axis_b_sustained_threat_curriculum_plan.md](sd_037_axis_b_sustained_threat_curriculum_plan.md)
- Autopsy: [failure_autopsy_V3-EXQ-625b_2026-06-02.md](failure_autopsy_V3-EXQ-625b_2026-06-02.md)

Sharper C3 (dynamic-crossings: >=1 above->below AND >=1 below->above per seed) on the SD-037 axis-b env overlay, with MECH-341 on-policy E3 score-diversity enabled. The scaffolded_sd054_onboarding amend does NOT feed this warmup_train measurement path; MECH-341 is the applicable on-policy diversity lever (validated V3-EXQ-611b).

## Env overlay (delta vs V3-EXQ-620; identical to 625b)

| Knob | Value |
|---|---|
| `scheduled_external_hazard_enabled` | `True` |
| `scheduled_external_hazard_interval` | `20` |
| `scheduled_external_hazard_prob` | `0.7` |
| `scheduled_external_hazard_adjacent_only` | `True` |
| `hazard_harm` | `0.2` |
| `proximity_harm_scale` | `0.2` |

## Acceptance gate (C1 AND C2 AND C3-dynamic-crossings)

- **C1_curriculum_firing**: True
- **C1_detail**: {'required': '3/3', 'achieved': '3/3', 'per_seed': [{'seed': 42, 'external_hazard_event_count': 6, 'ok': True}, {'seed': 7, 'external_hazard_event_count': 22, 'ok': True}, {'seed': 19, 'external_hazard_event_count': 14, 'ok': True}]}
- **C2_z_harm_a_nonzero**: True
- **C2_detail**: {'required': '>=2/3', 'achieved': '3/3', 'per_seed': [{'seed': 42, 'zero_fraction': 0.0, 'ok': True}, {'seed': 7, 'zero_fraction': 0.0, 'ok': True}, {'seed': 19, 'zero_fraction': 0.0, 'ok': True}]}
- **C3_dynamic_crossings**: False
- **C3_detail**: {'required': '>=2/3 seeds with >=1 above->below AND >=1 below->above', 'achieved': '0/3', 'per_seed': [{'seed': 42, 'n_above_to_below': 0, 'n_below_to_above': 0, 'n_total_transitions': 0, 'ok': False}, {'seed': 7, 'n_above_to_below': 0, 'n_below_to_above': 0, 'n_total_transitions': 0, 'ok': False}, {'seed': 19, 'n_above_to_below': 0, 'n_below_to_above': 0, 'n_total_transitions': 0, 'ok': False}]}
- **legacy_sustained_window_pass**: False
- **legacy_sustained_detail**: {'note': 'reported for comparison only -- NOT part of acceptance_pass', 'achieved': '1/3', 'per_seed': [{'seed': 42, 'n_sustained_runs': 0, 'max_sustained_run_length': 0, 'ok': False}, {'seed': 7, 'n_sustained_runs': 1, 'max_sustained_run_length': 922, 'ok': True}, {'seed': 19, 'n_sustained_runs': 0, 'max_sustained_run_length': 0, 'ok': False}]}
- **acceptance_pass**: False

## Per-seed dynamic-crossings (NEW gating C3) + legacy sustained-window (diagnostic only)

| Seed | n_distinct_actions | ext_hazard_events | above->below | below->above | crossings_pass | legacy n_runs | legacy max_run |
|---|---|---|---|---|---|---|---|
| 42 | 4 | 6 | 0 | 0 | False | 0 | 0 |
| 7 | 3 | 22 | 0 | 0 | False | 1 | 922 |
| 19 | 4 | 14 | 0 | 0 | False | 0 | 0 |

C3 (gating): per seed, n_above_to_below >= 1 AND n_below_to_above >= 1 at z_harm_a > 0.4; PASS on >= 2/3 seeds. Legacy sustained-window (>= 10 consecutive ticks above 0.4) is reported for comparison only -- a single near-full-eval run is the catatonic-lock literal-pass signature the new C3 correctly excludes.

## Pooled distributions (across seeds)

| Quantity | n | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 1647 | 0.3161 | 0.4538 | 0.3893 | 0.0529 | 0.4340 | 0.4386 | 0.000 |
| `cea_low_freq_magnitude` | 1647 | 0.0624 | 0.0980 | 0.0817 | 0.0138 | 0.0934 | 0.0943 | 0.000 |
| `z_harm_a_instant_val` | 1647 | 0.3161 | 0.4538 | 0.3893 | 0.0529 | 0.4340 | 0.4386 | 0.000 |
| `pag_sustained_product` | 1647 | 0.0000 | 2.2410 | 0.6143 | 0.7728 | 0.8772 | 1.7544 | 0.524 |
| `bla_pe_magnitude` | 1647 | 0.0000 | 0.5051 | 0.3611 | 0.0637 | 0.3752 | 0.4392 | 0.018 |
| `dacc_pe` | 1647 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
