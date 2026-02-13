# Experiment Pack Backfill Report

Generated: `2026-02-13T15:04:02.264343Z`
Mode: `apply`

## Summary

- Manifest files scanned: 10
- Manifest files requiring backfill: 10
- Manifest files written: 10

## Per-Run Changes

### `2026-02-13T080000Z_claim-probe-mech-053_seed11`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/claim_probe_mech_053/runs/2026-02-13T080000Z_claim-probe-mech-053_seed11/manifest.json`
- Experiment type: `claim_probe_mech_053`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-claim-probe-mech-053-claim-probe-mech-053`
  - `env_version` = `legacy-88cea3e429e6`
  - `dynamics_hash` = `legacy-2b1769f24d21`
  - `reward_hash` = `legacy-aec1db27d2ad`
  - `observation_hash` = `legacy-500d93eb6027`
  - `config_hash` = `534b6efca7b0`
  - `tier` = `toy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities: none

### `2026-02-13T080000Z_claim-probe-mech-053_seed29`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/claim_probe_mech_053/runs/2026-02-13T080000Z_claim-probe-mech-053_seed29/manifest.json`
- Experiment type: `claim_probe_mech_053`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-claim-probe-mech-053-claim-probe-mech-053`
  - `env_version` = `legacy-88cea3e429e6`
  - `dynamics_hash` = `legacy-0f7fc03e02ab`
  - `reward_hash` = `legacy-861b64328d37`
  - `observation_hash` = `legacy-31890fed490f`
  - `config_hash` = `534b6efca7b0`
  - `tier` = `toy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities: none

### `2026-02-13T080000Z_claim-probe-mech-054_seed11`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/claim_probe_mech_054/runs/2026-02-13T080000Z_claim-probe-mech-054_seed11/manifest.json`
- Experiment type: `claim_probe_mech_054`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-claim-probe-mech-054-claim-probe-mech-054`
  - `env_version` = `legacy-88cea3e429e6`
  - `dynamics_hash` = `legacy-7db303be49f6`
  - `reward_hash` = `legacy-186bc24a1834`
  - `observation_hash` = `legacy-43d427528553`
  - `config_hash` = `71fb32781db0`
  - `tier` = `toy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities: none

### `2026-02-13T080000Z_claim-probe-mech-054_seed29`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/claim_probe_mech_054/runs/2026-02-13T080000Z_claim-probe-mech-054_seed29/manifest.json`
- Experiment type: `claim_probe_mech_054`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-claim-probe-mech-054-claim-probe-mech-054`
  - `env_version` = `legacy-88cea3e429e6`
  - `dynamics_hash` = `legacy-a0735bef010b`
  - `reward_hash` = `legacy-3c06e5bbda09`
  - `observation_hash` = `legacy-b11923f0b4f6`
  - `config_hash` = `71fb32781db0`
  - `tier` = `toy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities: none

### `2026-02-13T060000Z_dummy-pass`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/runs/2026-02-13T060000Z_dummy-pass/manifest.json`
- Experiment type: `trajectory_integrity`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-trajectory-integrity-trajectory-integrity-smoke`
  - `env_version` = `legacy-111111111111`
  - `dynamics_hash` = `legacy-9ad125027728`
  - `reward_hash` = `legacy-1bb23907f7d4`
  - `observation_hash` = `legacy-541c99fe1fc8`
  - `config_hash` = `cfg_a1`
  - `tier` = `toy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities:
  - MECH-056 run missing some dispatch metrics; leaving related capability flags false: `perceptual_sampling_channel_usage_count`, `precommit_semantic_overwrite_events`, `structural_bias_magnitude`, `structural_bias_rate`, `structural_consolidation_channel_usage_count`, `trajectory_commit_channel_usage_count`
  - MECH-056 summary lacks explicit channel escalation tokens; `mech056_summary_escalation_trace` set false

### `2026-02-13T070000Z_dummy-fail`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/runs/2026-02-13T070000Z_dummy-fail/manifest.json`
- Experiment type: `trajectory_integrity`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-trajectory-integrity-trajectory-integrity-stress`
  - `env_version` = `legacy-222222222222`
  - `dynamics_hash` = `legacy-dcc062cec124`
  - `reward_hash` = `legacy-d825b1ba8ba6`
  - `observation_hash` = `legacy-9fdcb9566db1`
  - `config_hash` = `cfg_b2`
  - `tier` = `stress`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities:
  - MECH-056 run missing some dispatch metrics; leaving related capability flags false: `perceptual_sampling_channel_usage_count`, `precommit_semantic_overwrite_events`, `structural_bias_magnitude`, `structural_bias_rate`, `structural_consolidation_channel_usage_count`, `trajectory_commit_channel_usage_count`
  - MECH-056 summary lacks explicit channel escalation tokens; `mech056_summary_escalation_trace` set false

### `exp_0003_20260213T090639857099Z`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/runs/exp_0003_20260213T090639857099Z/manifest.json`
- Experiment type: `trajectory_integrity`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-trajectory-integrity-proposal-exp-0003`
  - `env_version` = `legacy-d39241ebcad5`
  - `dynamics_hash` = `legacy-9e5225b9d59e`
  - `reward_hash` = `legacy-bfde89c696ba`
  - `observation_hash` = `legacy-12c6b1d70919`
  - `config_hash` = `legacy-f8b5a1ba8d1a`
  - `tier` = `legacy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities:
  - MECH-056 run missing some dispatch metrics; leaving related capability flags false: `perceptual_sampling_channel_usage_count`, `precommit_semantic_overwrite_events`, `structural_bias_magnitude`, `structural_bias_rate`, `structural_consolidation_channel_usage_count`, `trajectory_commit_channel_usage_count`
  - MECH-056 summary lacks explicit channel escalation tokens; `mech056_summary_escalation_trace` set false
  - scenario.config_hash missing; config_hash derived from deterministic placeholder
  - tier inferred as `legacy` because no toy/stress indicators were found

### `exp_0003_20260213T090639905363Z`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/runs/exp_0003_20260213T090639905363Z/manifest.json`
- Experiment type: `trajectory_integrity`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-trajectory-integrity-proposal-exp-0003`
  - `env_version` = `legacy-d39241ebcad5`
  - `dynamics_hash` = `legacy-862f841c0d0b`
  - `reward_hash` = `legacy-5bec971b4ede`
  - `observation_hash` = `legacy-737d87ea86d5`
  - `config_hash` = `legacy-e982853ba1da`
  - `tier` = `legacy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities:
  - MECH-056 run missing some dispatch metrics; leaving related capability flags false: `perceptual_sampling_channel_usage_count`, `precommit_semantic_overwrite_events`, `structural_bias_magnitude`, `structural_bias_rate`, `structural_consolidation_channel_usage_count`, `trajectory_commit_channel_usage_count`
  - MECH-056 summary lacks explicit channel escalation tokens; `mech056_summary_escalation_trace` set false
  - scenario.config_hash missing; config_hash derived from deterministic placeholder
  - tier inferred as `legacy` because no toy/stress indicators were found

### `exp_0005_20260213T090639951474Z`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/runs/exp_0005_20260213T090639951474Z/manifest.json`
- Experiment type: `trajectory_integrity`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-trajectory-integrity-proposal-exp-0005`
  - `env_version` = `legacy-d39241ebcad5`
  - `dynamics_hash` = `legacy-89c462941ad3`
  - `reward_hash` = `legacy-ff4a14067834`
  - `observation_hash` = `legacy-90dc507dd9c1`
  - `config_hash` = `legacy-b3bf2f523f58`
  - `tier` = `legacy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities:
  - scenario.config_hash missing; config_hash derived from deterministic placeholder
  - tier inferred as `legacy` because no toy/stress indicators were found

### `exp_0005_20260213T090639999186Z`

- Manifest: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/runs/exp_0005_20260213T090639999186Z/manifest.json`
- Experiment type: `trajectory_integrity`
- Changed fields: `environment`, `producer_capabilities`
- Environment values:
  - `env_id` = `legacy-trajectory-integrity-proposal-exp-0005`
  - `env_version` = `legacy-d39241ebcad5`
  - `dynamics_hash` = `legacy-e15b29c1c976`
  - `reward_hash` = `legacy-67a4a690b87f`
  - `observation_hash` = `legacy-ec0ad087adbc`
  - `config_hash` = `legacy-afb520116d84`
  - `tier` = `legacy`
- Producer capabilities:
  - `trajectory_integrity_channelized_bias` = `false`
  - `mech056_dispatch_metric_set` = `false`
  - `mech056_summary_escalation_trace` = `false`
- Unresolved ambiguities:
  - scenario.config_hash missing; config_hash derived from deterministic placeholder
  - tier inferred as `legacy` because no toy/stress indicators were found
