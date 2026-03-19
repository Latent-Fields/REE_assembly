# Evidence Conflict Report

Generated: `2026-03-19T22:13:03.482052Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-007` | directional | 2 | 1 | 0.667 | `20260319T090529Z_v3_exq_042_hippocampal_terrain_training_v3` | 3 |
| `ARC-016` | directional | 4 | 5 | 0.889 | `20260319T075521Z_v3_exq_041_full_pipeline_smoke_test_v3` | 9 |
| `ARC-024` | directional, mixed_evidence | 2 | 2 | 1 | `20260319T060720Z_v3_exq_039_training_progression_v3` | 10 |
| `MECH-071` | directional, mixed_evidence | 4 | 1 | 0.4 | `20260319T075521Z_v3_exq_041_full_pipeline_smoke_test_v3` | 12 |
| `MECH-093` | directional, source_disagreement | 1 | 1 | 1 | `20260319T061623Z_v3_exq_038_arc016_precision_sweep_v3` | 2 |
| `MECH-098` | directional, source_disagreement, mixed_evidence | 4 | 4 | 1 | `20260318T180316Z_v3_exq_027_sd003_v3_reafference_v3` | 10 |
| `MECH-099` | directional, source_disagreement, mixed_evidence | 3 | 1 | 0.5 | `20260317T232006Z_v3_exq_017_combined_lateral_reafference_v3` | 5 |
| `MECH-102` | directional, mixed_evidence | 1 | 2 | 0.667 | `20260319T104327Z_v3_exq_043_sd003_trajectory_attribution_v3` | 4 |
| `SD-003` | directional, mixed_evidence | 5 | 8 | 0.769 | `20260319T104327Z_v3_exq_043_sd003_trajectory_attribution_v3` | 30 |
| `SD-005` | directional, mixed_evidence | 3 | 1 | 0.5 | `20260319T070357Z_v3_exq_040_z_separation_alpha09_v3` | 6 |
| `SD-007` | directional, mixed_evidence | 2 | 3 | 0.8 | `20260318T201740Z_v3_exq_029_sd003_proxy_gradient_world_v3` | 7 |
| `SD-008` | directional | 1 | 3 | 0.5 | `20260319T070357Z_v3_exq_040_z_separation_alpha09_v3` | 4 |

## Conflict Details

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=1, conflict_ratio=0.667, overall_confidence=0.69
- Recent entries:
  - `2026-03-08T11:46:44.792784+00:00` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
  - `2026-03-16T06:19:08.594368+00:00` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-03-19T09:05:29Z` `experimental` `claim_probe_sd_004` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:path_memory_ablation` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-016
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=5, conflict_ratio=0.889, overall_confidence=0.724
- Recent entries:
  - `2026-03-18T17:34:19Z` `experimental` `claim_probe_arc_016` direction=`supports` confidence=0.75
  - `2026-03-18T20:17:24Z` `experimental` `claim_probe_arc_016` direction=`supports` confidence=0.75
  - `2026-03-18T20:18:53Z` `experimental` `claim_probe_arc_016` direction=`supports` confidence=0.75
  - `2026-03-19T06:16:23Z` `experimental` `claim_probe_arc_016` direction=`weakens` confidence=0.75
  - `2026-03-19T07:55:21Z` `experimental` `claim_probe_mech_089` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:precision_regime_probe` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-024
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.509
- Recent entries:
  - `2026-03-19T05:49:38Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T05:49:52Z` `experimental` `claim_probe_mech_102` direction=`supports` confidence=0.75
  - `2026-03-19T05:50:00Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-19T06:06:18Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T06:07:20Z` `experimental` `claim_probe_mech_071` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-071
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.779
- Recent entries:
  - `2026-03-18T20:25:55Z` `experimental` `claim_probe_arc_025` direction=`supports` confidence=0.75
  - `2026-03-19T05:49:38Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T06:06:18Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T06:07:20Z` `experimental` `claim_probe_mech_071` direction=`mixed` confidence=0.5
  - `2026-03-19T07:55:21Z` `experimental` `claim_probe_mech_089` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:causal_attribution_calibration` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-093
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.742
- Recent entries:
  - `2026-03-16T12:00:00Z` `literature` `targeted_review_connectome_mech_093` direction=`supports` confidence=0.72
  - `2026-03-19T06:16:23Z` `experimental` `claim_probe_arc_016` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-098
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.825
- Recent entries:
  - `2026-03-17T23:20:06Z` `experimental` `claim_probe_mech_099` direction=`weakens` confidence=0.75
  - `2026-03-18T02:58:20Z` `experimental` `claim_probe_sd_008` direction=`weakens` confidence=0.75
  - `2026-03-18T02:59:09Z` `experimental` `claim_probe_sd_007` direction=`mixed` confidence=0.5
  - `2026-03-18T18:03:01Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
  - `2026-03-18T18:03:16Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-099
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.849
- Recent entries:
  - `2026-03-17T21:00:00Z` `literature` `targeted_review_reafference_streams` direction=`supports` confidence=0.82
  - `2026-03-17T21:00:00Z` `literature` `targeted_review_reafference_streams` direction=`supports` confidence=0.88
  - `2026-03-17T21:00:00Z` `literature` `targeted_review_reafference_streams` direction=`supports` confidence=0.86
  - `2026-03-17T23:17:48Z` `experimental` `claim_probe_mech_099` direction=`mixed` confidence=0.5
  - `2026-03-17T23:20:06Z` `experimental` `claim_probe_mech_099` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-102
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=1, weakens=2, conflict_ratio=0.667, overall_confidence=0.618
- Recent entries:
  - `2026-03-18T20:19:10Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-19T05:49:52Z` `experimental` `claim_probe_mech_102` direction=`supports` confidence=0.75
  - `2026-03-19T05:50:00Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-19T10:43:27Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-003
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=5, weakens=8, conflict_ratio=0.769, overall_confidence=0.614
- Recent entries:
  - `2026-03-19T05:49:52Z` `experimental` `claim_probe_mech_102` direction=`supports` confidence=0.75
  - `2026-03-19T05:50:00Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-19T06:06:18Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T06:06:43Z` `experimental` `claim_probe_mech_069` direction=`supports` confidence=0.75
  - `2026-03-19T10:43:27Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-005
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.74
- Recent entries:
  - `2026-03-17T05:37:22Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-17T20:41:44Z` `experimental` `claim_probe_mech_095` direction=`mixed` confidence=0.5
  - `2026-03-17T22:51:09Z` `experimental` `claim_probe_sd_005` direction=`weakens` confidence=0.75
  - `2026-03-18T17:34:29Z` `experimental` `claim_probe_mech_071` direction=`supports` confidence=0.75
  - `2026-03-19T07:03:57Z` `experimental` `claim_probe_sd_005` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-007
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=2, weakens=3, conflict_ratio=0.8, overall_confidence=0.605
- Recent entries:
  - `2026-03-17T23:20:06Z` `experimental` `claim_probe_mech_099` direction=`weakens` confidence=0.75
  - `2026-03-18T02:59:09Z` `experimental` `claim_probe_sd_007` direction=`mixed` confidence=0.5
  - `2026-03-18T18:03:01Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
  - `2026-03-18T18:03:16Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-18T20:17:40Z` `experimental` `claim_probe_sd_003` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-008
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=3, conflict_ratio=0.5, overall_confidence=0.699
- Recent entries:
  - `2026-03-18T02:58:20Z` `experimental` `claim_probe_sd_008` direction=`weakens` confidence=0.75
  - `2026-03-18T03:16:43Z` `experimental` `claim_probe_sd_003` direction=`weakens` confidence=0.75
  - `2026-03-18T03:17:37Z` `experimental` `claim_probe_sd_003` direction=`weakens` confidence=0.75
  - `2026-03-19T07:03:57Z` `experimental` `claim_probe_sd_005` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
