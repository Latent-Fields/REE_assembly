# SD-037 Axis (a) Phase 1 -- Consumer-Input Distributions

- Queue id: `V3-EXQ-620b`
- Run id: `v3_exq_620b_sd037_axis_a_phase1_consumer_input_distributions_stream_on_20260601T180611Z_v3`
- Timestamp UTC: `20260601T180611Z`
- Manifest: `evidence/experiments/v3_exq_620b_sd037_axis_a_phase1_consumer_input_distributions_stream_on_20260601T180611Z_v3.json`
- Plan: [sd_037_axis_a_consumer_input_recalibration_plan.md](sd_037_axis_a_consumer_input_recalibration_plan.md)

Phase 1 substrate-readiness diagnostic. Substrate matches 483e ARM_0 OFF_OFF (PAG-engaging env via SD-036 + MECH-279, SalienceCoordinator + dACC + amygdala all enabled) but with `use_broadcast_override=False` and all four MECH-281 cascade gains 0.0. Pure baseline: this is the natural fishtank distribution every consumer-module input gate sees when the broadcast is silent.

## Phase 2 recalibration table (p70 candidates)

| Consumer-input quantity | Knob | Current default | Measured p70 (pooled) | Phase 2 candidate |
|---|---|---|---|---|
| `z_harm_a_norm` | `BLAConfig.arousal_threshold_on` | 0.40 | 0.4326 | 0.4000 |
| `cea_low_freq_magnitude` | `CeAConfig.fast_route_threshold` | 0.50 | 0.0930 | 0.0930 |
| `z_harm_a_instant_val` | `PAGFreezeGateConfig.duration_input_threshold` | 0.40 | 0.4326 | 0.4000 |
| `pag_sustained_product` | `PAGFreezeGateConfig.theta_freeze` | 2.00 | 0.8671 | 0.8671 |
| `bla_pe_magnitude` | `(BLA PE channel; informational)` | n/a | 0.3752 | (see plan Phase 2 dACC rescale rule) |
| `dacc_pe` | `DACCConfig.dacc_precision_scale (informational; rescale not threshold)` | n/a | 0.0000 | (see plan Phase 2 dACC rescale rule) |

Floor / ceiling per Phase 2 plan: floor 0.05 (theta_freeze 0.1); ceiling current default (so a high-p70 cannot raise a threshold above its current value -- Phase 2 NEVER raises a default, only lowers).

## Per-seed distributions

### Seed 42

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.3158 | 0.3328 | 0.3231 | 0.0035 | 0.3247 | 0.3281 | 0.000 |
| `cea_low_freq_magnitude` | 0.0705 | 0.0732 | 0.0718 | 0.0004 | 0.0720 | 0.0723 | 0.000 |
| `z_harm_a_instant_val` | 0.3158 | 0.3328 | 0.3231 | 0.0035 | 0.3247 | 0.3281 | 0.000 |
| `pag_sustained_product` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 0.0000 | 0.4819 | 0.4372 | 0.0693 | 0.4537 | 0.4641 | 0.024 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

### Seed 7

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.4305 | 0.4430 | 0.4342 | 0.0028 | 0.4366 | 0.4378 | 0.000 |
| `cea_low_freq_magnitude` | 0.0925 | 0.0953 | 0.0934 | 0.0007 | 0.0940 | 0.0942 | 0.000 |
| `z_harm_a_instant_val` | 0.4305 | 0.4430 | 0.4342 | 0.0028 | 0.4366 | 0.4378 | 0.000 |
| `pag_sustained_product` | 0.0000 | 2.2080 | 1.1211 | 0.7467 | 1.7292 | 2.1644 | 0.165 |
| `bla_pe_magnitude` | 0.0000 | 0.4950 | 0.3746 | 0.0298 | 0.3770 | 0.3834 | 0.005 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

### Seed 19

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.3290 | 0.3448 | 0.3317 | 0.0020 | 0.3319 | 0.3339 | 0.000 |
| `cea_low_freq_magnitude` | 0.0627 | 0.0660 | 0.0641 | 0.0004 | 0.0644 | 0.0646 | 0.000 |
| `z_harm_a_instant_val` | 0.3290 | 0.3448 | 0.3317 | 0.0020 | 0.3319 | 0.3339 | 0.000 |
| `pag_sustained_product` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 0.0000 | 0.3358 | 0.3180 | 0.0256 | 0.3229 | 0.3270 | 0.006 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

## Pooled distributions (across seeds)

| Quantity | n | min | max | mean | std | p10 | p25 | p50 | p70 | p80 | p90 | p95 | p99 | zero_frac |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 4049 | 0.3158 | 0.4430 | 0.3813 | 0.0522 | 0.3290 | 0.3310 | 0.3381 | 0.4326 | 0.4345 | 0.4375 | 0.4378 | 0.4398 | 0.000 |
| `cea_low_freq_magnitude` | 4049 | 0.0627 | 0.0953 | 0.0793 | 0.0140 | 0.0639 | 0.0643 | 0.0724 | 0.0930 | 0.0934 | 0.0941 | 0.0942 | 0.0946 | 0.000 |
| `z_harm_a_instant_val` | 4049 | 0.3158 | 0.4430 | 0.3813 | 0.0522 | 0.3290 | 0.3310 | 0.3381 | 0.4326 | 0.4345 | 0.4375 | 0.4378 | 0.4398 | 0.000 |
| `pag_sustained_product` | 4049 | 0.0000 | 2.2080 | 0.5518 | 0.7672 | 0.0000 | 0.0000 | 0.0000 | 0.8671 | 1.3100 | 1.7503 | 2.1631 | 2.1877 | 0.589 |
| `bla_pe_magnitude` | 4049 | 0.0000 | 0.4950 | 0.3582 | 0.0513 | 0.3161 | 0.3216 | 0.3712 | 0.3752 | 0.3793 | 0.4317 | 0.4494 | 0.4680 | 0.007 |
| `dacc_pe` | 4049 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

## Routing

PASS -> Phase 2 deterministic recalibration rule (read p70 from the pooled distribution; apply per-experiment overrides; queue Phase 3 verification diagnostic). FAIL with all-zero z_harm_a_norm + bla_pe (would mean even the affective stream itself is silent at baseline) -> route to axis (b) SD-029-style sustained-threat env curriculum without waiting on a p60 / p80 sweep, because static threshold lowering cannot help when the upstream signal is absent.
