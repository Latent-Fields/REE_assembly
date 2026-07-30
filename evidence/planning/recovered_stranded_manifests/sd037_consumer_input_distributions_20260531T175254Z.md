# SD-037 Axis (a) Phase 1 -- Consumer-Input Distributions

- Queue id: `V3-EXQ-620`
- Run id: `v3_exq_620_sd037_axis_a_phase1_consumer_input_distributions_20260531T175254Z_v3`
- Timestamp UTC: `20260531T175254Z`
- Manifest: `evidence/experiments/v3_exq_620_sd037_axis_a_phase1_consumer_input_distributions_20260531T175254Z_v3.json`
- Plan: [sd_037_axis_a_consumer_input_recalibration_plan.md](sd_037_axis_a_consumer_input_recalibration_plan.md)

Phase 1 substrate-readiness diagnostic. Substrate matches 483e ARM_0 OFF_OFF (PAG-engaging env via SD-036 + MECH-279, SalienceCoordinator + dACC + amygdala all enabled) but with `use_broadcast_override=False` and all four MECH-281 cascade gains 0.0. Pure baseline: this is the natural fishtank distribution every consumer-module input gate sees when the broadcast is silent.

## Phase 2 recalibration table (p70 candidates)

| Consumer-input quantity | Knob | Current default | Measured p70 (pooled) | Phase 2 candidate |
|---|---|---|---|---|
| `z_harm_a_norm` | `BLAConfig.arousal_threshold_on` | 0.40 | 0.0000 | 0.0500 |
| `cea_low_freq_magnitude` | `CeAConfig.fast_route_threshold` | 0.50 | 0.0000 | 0.0500 |
| `z_harm_a_instant_val` | `PAGFreezeGateConfig.duration_input_threshold` | 0.40 | 0.0000 | 0.0500 |
| `pag_sustained_product` | `PAGFreezeGateConfig.theta_freeze` | 2.00 | 0.0000 | 0.1000 |
| `bla_pe_magnitude` | `(BLA PE channel; informational)` | n/a | 0.0000 | (see plan Phase 2 dACC rescale rule) |
| `dacc_pe` | `DACCConfig.dacc_precision_scale (informational; rescale not threshold)` | n/a | 0.0000 | (see plan Phase 2 dACC rescale rule) |

Floor / ceiling per Phase 2 plan: floor 0.05 (theta_freeze 0.1); ceiling current default (so a high-p70 cannot raise a threshold above its current value -- Phase 2 NEVER raises a default, only lowers).

## Per-seed distributions

### Seed 42

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `cea_low_freq_magnitude` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `z_harm_a_instant_val` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `pag_sustained_product` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

### Seed 7

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `cea_low_freq_magnitude` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `z_harm_a_instant_val` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `pag_sustained_product` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

### Seed 19

| Quantity | min | max | mean | std | p70 | p90 | zero_frac |
|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `cea_low_freq_magnitude` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `z_harm_a_instant_val` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `pag_sustained_product` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `dacc_pe` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

## Pooled distributions (across seeds)

| Quantity | n | min | max | mean | std | p10 | p25 | p50 | p70 | p80 | p90 | p95 | p99 | zero_frac |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `z_harm_a_norm` | 2939 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `cea_low_freq_magnitude` | 2939 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `z_harm_a_instant_val` | 2939 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `pag_sustained_product` | 2939 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `bla_pe_magnitude` | 2939 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |
| `dacc_pe` | 2939 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.000 |

## Routing

PASS -> Phase 2 deterministic recalibration rule (read p70 from the pooled distribution; apply per-experiment overrides; queue Phase 3 verification diagnostic). FAIL with all-zero z_harm_a_norm + bla_pe (would mean even the affective stream itself is silent at baseline) -> route to axis (b) SD-029-style sustained-threat env curriculum without waiting on a p60 / p80 sweep, because static threshold lowering cannot help when the upstream signal is absent.
