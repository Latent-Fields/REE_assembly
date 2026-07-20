# SD-037 Axis (b) Phase 1b -- Consumer-Input Distributions (Sustained-Threat Curriculum)

- Queue id: `V3-EXQ-625b`
- Run id: `v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_20260601T181233Z_v3`
- Timestamp UTC: `20260601T181233Z`
- Manifest: `evidence/experiments/v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_20260601T181233Z_v3.json`
- Plan: [sd_037_axis_b_sustained_threat_curriculum_plan.md](sd_037_axis_b_sustained_threat_curriculum_plan.md)

Phase 1b substrate-readiness diagnostic. Substrate matches V3-EXQ-620 ARM_PHASE1_BASELINE verbatim (PAG-engaging env via SD-036 + MECH-279, SalienceCoordinator + dACC + amygdala enabled, broadcast OFF, all four MECH-281 cascade gains 0.0). Only delta vs 620 is the env overlay below -- SD-029 scheduled_external_hazard curriculum ON + hazard_harm 4x lift + proximity_harm_scale 2x lift.

## Env overlay (delta vs V3-EXQ-620)

| Knob | Value |
|---|---|
| `scheduled_external_hazard_enabled` | `True` |
| `scheduled_external_hazard_interval` | `20` |
| `scheduled_external_hazard_prob` | `0.7` |
| `scheduled_external_hazard_adjacent_only` | `True` |
| `hazard_harm` | `0.2` |
| `proximity_harm_scale` | `0.2` |

## Acceptance gate (plan Section 3.4)

- **C1_curriculum_firing**: True
- **C1_detail**: {'required': '3/3', 'achieved': '3/3', 'per_seed': [{'seed': 42, 'external_hazard_event_count': 10, 'ok': True}, {'seed': 7, 'external_hazard_event_count': 45, 'ok': True}, {'seed': 19, 'external_hazard_event_count': 6, 'ok': True}]}
- **C2_z_harm_a_nonzero**: True
- **C2_detail**: {'required': '>=2/3', 'achieved': '3/3', 'per_seed': [{'seed': 42, 'zero_fraction': 0.0, 'ok': True}, {'seed': 7, 'zero_fraction': 0.0, 'ok': True}, {'seed': 19, 'zero_fraction': 0.0, 'ok': True}]}
- **C3_sustained_window**: False
- **C3_detail**: {'required': '>=2/3', 'achieved': '1/3', 'per_seed': [{'seed': 42, 'n_sustained_runs': 0, 'ok': False}, {'seed': 7, 'n_sustained_runs': 1, 'ok': True}, {'seed': 19, 'n_sustained_runs': 0, 'ok': False}]}
- **acceptance_pass**: False

## Phase 2 recalibration table (p70 candidates on axis-b distributions)

| Consumer-input quantity | Knob | Current default | Measured p70 (pooled) | Phase 2 candidate |
|---|---|---|---|---|
| `z_harm_a_norm` | `BLAConfig.arousal_threshold_on` | 0.40 | 0.4343 | 0.4000 |
| `cea_low_freq_magnitude` | `CeAConfig.fast_route_threshold` | 0.50 | 0.0935 | 0.0935 |
| `z_harm_a_instant_val` | `PAGFreezeGateConfig.duration_input_threshold` | 0.40 | 0.4343 | 0.4000 |
| `pag_sustained_product` | `PAGFreezeGateConfig.theta_freeze` | 2.00 | 1.3028 | 1.3028 |
| `bla_pe_magnitude` | `(BLA PE channel; informational)` | n/a | 0.3811 | (see plan Phase 2 dACC rescale rule) |
| `dacc_pe` | `DACCConfig.dacc_precision_scale (informational; rescale not threshold)` | n/a | 0.0000 | (see plan Phase 2 dACC rescale rule) |

Floor / ceiling per Phase 2 plan: floor 0.05 (theta_freeze 0.1); ceiling current default (so a high-p70 cannot raise a threshold above its current value -- Phase 2 NEVER raises a default, only lowers).

## Per-seed sustained-window summary

| Seed | external_hazard_event_count | n_sustained_runs | total_duration | max_run_len |
|---|---|---|---|---|
| 42 | 10 | 0 | 0 | 0 |
| 7 | 45 | 1 | 1413 | 1413 |
| 19 | 6 | 0 | 0 | 0 |

Sustained-run definition: contiguous ticks where `z_harm_a_instant_val > 0.4` for at least 10 consecutive ticks (PAG `duration_input_threshold` default; biological gating per plan Section 2.3).

## Per-seed distributions

### Seed 42

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.3126 | 0.3386 | 0.3235 | 0.0041 | 0.3252 | 0.3288 | 0.000 |
| `cea_low_freq_magnitude` | 0.0697 | 0.0739 | 0.0719 | 0.0005 | 0.0719 | 0.0726 | 0.000 |
| `z_harm_a_instant_val` | 0.3126 | 0.3386 | 0.3235 | 0.0041 | 0.3252 | 0.3288 | 0.000 |
| `pag_sustained_product` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 0.0000 | 0.4780 | 0.4309 | 0.0794 | 0.4510 | 0.4636 | 0.032 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

### Seed 7

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.4309 | 0.4568 | 0.4349 | 0.0031 | 0.4369 | 0.4386 | 0.000 |
| `cea_low_freq_magnitude` | 0.0927 | 0.0977 | 0.0935 | 0.0007 | 0.0940 | 0.0943 | 0.000 |
| `z_harm_a_instant_val` | 0.4309 | 0.4568 | 0.4349 | 0.0031 | 0.4369 | 0.4386 | 0.000 |
| `pag_sustained_product` | 0.0000 | 2.2054 | 1.0907 | 0.7375 | 1.7288 | 2.1682 | 0.161 |
| `bla_pe_magnitude` | 0.0000 | 0.4987 | 0.3733 | 0.0329 | 0.3779 | 0.3858 | 0.007 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

### Seed 19

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.3293 | 0.3551 | 0.3352 | 0.0057 | 0.3359 | 0.3445 | 0.000 |
| `cea_low_freq_magnitude` | 0.0631 | 0.0699 | 0.0646 | 0.0011 | 0.0645 | 0.0661 | 0.000 |
| `z_harm_a_instant_val` | 0.3293 | 0.3551 | 0.3352 | 0.0057 | 0.3359 | 0.3445 | 0.000 |
| `pag_sustained_product` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 0.0000 | 0.3483 | 0.3049 | 0.0720 | 0.3241 | 0.3326 | 0.052 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

## Pooled distributions (across seeds)

| Quantity | n | min | max | mean | std | p10 | p25 | p50 | p70 | p80 | p90 | p95 | p99 | zero_frac |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 1916 | 0.3126 | 0.4568 | 0.4068 | 0.0473 | 0.3250 | 0.3437 | 0.4323 | 0.4343 | 0.4369 | 0.4386 | 0.4386 | 0.4459 | 0.000 |
| `cea_low_freq_magnitude` | 1916 | 0.0631 | 0.0977 | 0.0871 | 0.0109 | 0.0699 | 0.0727 | 0.0928 | 0.0935 | 0.0940 | 0.0943 | 0.0943 | 0.0958 | 0.000 |
| `z_harm_a_instant_val` | 1916 | 0.3126 | 0.4568 | 0.4068 | 0.0473 | 0.3250 | 0.3437 | 0.4323 | 0.4343 | 0.4369 | 0.4386 | 0.4386 | 0.4459 | 0.000 |
| `pag_sustained_product` | 1916 | 0.0000 | 2.2054 | 0.8044 | 0.7946 | 0.0000 | 0.0000 | 0.4412 | 1.3028 | 1.7345 | 2.1610 | 2.1713 | 2.1930 | 0.381 |
| `bla_pe_magnitude` | 1916 | 0.0000 | 0.4987 | 0.3759 | 0.0578 | 0.3327 | 0.3709 | 0.3752 | 0.3811 | 0.3881 | 0.4414 | 0.4513 | 0.4672 | 0.016 |
| `dacc_pe` | 1916 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

## Routing

PASS -> axis (b) Phase 2 deterministic recalibration rule (re-applies axis-a Phase 2 p70 rule on the new distributions; per plan Section 4.1). FAIL -> route to plan Section 5 five-row interpretation grid (curriculum mis-applied / affective-stream noise floor / PAG sustained-window failure / dACC PE deterministic-prediction / env-kwarg surface exhausted -> axis (c) heavier path).
