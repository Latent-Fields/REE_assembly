# Evidence Conflict Report

Generated: `2026-02-15T21:38:13.992121Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-003` | directional | 3 | 4 | 0.857 | `2026-02-15T213603Z_claim-probe-arc-003_seed1001_single_error_stream_toyenv_internal_minimal` | 7 |
| `ARC-007` | directional | 6 | 4 | 0.8 | `2026-02-15T213601Z_claim-probe-arc-007_seed1001_trajectory_first_enabled_toyenv_internal_minimal` | 10 |
| `ARC-018` | directional | 5 | 4 | 0.889 | `2026-02-15T213637Z_claim-probe-arc-018_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 9 |
| `MECH-033` | directional | 5 | 4 | 0.889 | `2026-02-15T213638Z_claim-probe-mech-033_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 9 |
| `MECH-040` | directional | 4 | 4 | 1 | `2026-02-15T213634Z_claim-probe-mech-040_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 8 |
| `MECH-046` | directional | 4 | 4 | 1 | `2026-02-15T213635Z_claim-probe-mech-046_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 8 |
| `MECH-056` | directional, source_disagreement | 11 | 22 | 0.667 | `exp_0004_20260215T211117389757Z` | 33 |
| `MECH-057` | directional | 4 | 5 | 0.889 | `2026-02-15T213702Z_claim-probe-mech-057_seed1003_trajectory_first_enabled_toyenv_internal_minimal` | 9 |
| `MECH-058` | directional, mixed_evidence | 22 | 14 | 0.778 | `2026-02-15_mech058_connectome_byol_asymmetry_analysis_2022` | 37 |
| `MECH-059` | directional, mixed_evidence | 14 | 1 | 0.133 | `2026-02-15T213803Z_claim-probe-mech-059_seed1008_deterministic_plus_dispersion_toyenv_internal_minimal` | 41 |
| `MECH-060` | directional, mixed_evidence | 22 | 14 | 0.778 | `2026-02-15_mech060_connectome_vjepa2_dual_loss_channels_arxiv2025` | 37 |
| `MECH-061` | directional | 3 | 4 | 0.857 | `2026-02-15T213606Z_claim-probe-mech-061_seed1001_single_error_stream_toyenv_internal_minimal` | 7 |
| `Q-001` | directional | 6 | 4 | 0.8 | `2026-02-15T213641Z_claim-probe-q-001_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-002` | directional | 6 | 4 | 0.8 | `2026-02-15T213642Z_claim-probe-q-002_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-003` | directional | 6 | 4 | 0.8 | `2026-02-15T213643Z_claim-probe-q-003_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-004` | directional | 6 | 4 | 0.8 | `2026-02-15T213644Z_claim-probe-q-004_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-005` | directional | 6 | 4 | 0.8 | `2026-02-15T213645Z_claim-probe-q-005_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-006` | directional | 6 | 4 | 0.8 | `2026-02-15T213645Z_claim-probe-q-006_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-007` | directional | 6 | 4 | 0.8 | `2026-02-15T213646Z_claim-probe-q-007_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-008` | directional | 6 | 4 | 0.8 | `2026-02-15T213647Z_claim-probe-q-008_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-009` | directional | 6 | 4 | 0.8 | `2026-02-15T213648Z_claim-probe-q-009_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-010` | directional | 6 | 4 | 0.8 | `2026-02-15T213649Z_claim-probe-q-010_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 11 |
| `Q-012` | directional | 4 | 4 | 1 | `2026-02-15T213633Z_claim-probe-q-012_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 8 |
| `Q-013` | directional | 6 | 4 | 0.8 | `2026-02-15T213639Z_claim-probe-q-013_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 10 |
| `Q-014` | directional | 6 | 4 | 0.8 | `2026-02-15T213640Z_claim-probe-q-014_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 10 |
| `Q-015` | directional | 4 | 4 | 1 | `2026-02-15T213636Z_claim-probe-q-015_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 8 |
| `Q-017` | directional, mixed_evidence | 22 | 16 | 0.842 | `2026-02-15_q017_connectome_neuromod_degeneracy_neuron2012` | 39 |

## Conflict Details

### ARC-003
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=4, conflict_ratio=0.857, overall_confidence=0.665
- Recent entries:
  - `2026-02-15T18:09:24.416725Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
  - `2026-02-15T18:09:24.496279Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:13Z` `experimental` `claim_probe_arc_003` direction=`weakens` confidence=0.75
  - `2026-02-15T21:10:33Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:03Z` `experimental` `claim_probe_arc_003` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (4)
  - `mech060:attribution_reliability_break` (4)
  - `mech060:commitment_reversal_spike` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.647
- Recent entries:
  - `2026-02-15T18:10:23Z` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:57.175710Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:57.233345Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:31Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:01Z` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.664
- Recent entries:
  - `2026-02-15T18:05:21Z` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:17Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:37Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:08Z` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:37Z` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.662
- Recent entries:
  - `2026-02-15T18:05:22Z` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:18Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:38Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:09Z` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:38Z` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-040
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.637
- Recent entries:
  - `2026-02-15T18:05:26Z` `experimental` `claim_probe_mech_040` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:14Z` `experimental` `claim_probe_mech_040` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:34Z` `experimental` `claim_probe_mech_040` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:05Z` `experimental` `claim_probe_mech_040` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:34Z` `experimental` `claim_probe_mech_040` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-046
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.627
- Recent entries:
  - `2026-02-15T18:05:28Z` `experimental` `claim_probe_mech_046` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:15Z` `experimental` `claim_probe_mech_046` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:35Z` `experimental` `claim_probe_mech_046` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:06Z` `experimental` `claim_probe_mech_046` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:35Z` `experimental` `claim_probe_mech_046` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-056
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=11, weakens=22, conflict_ratio=0.667, overall_confidence=0.749
- Recent entries:
  - `2026-02-15T18:07:10.784771Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.843991Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:57.289360Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:57.348626Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T21:11:17.389757Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (20)
  - `stop:ledger_edit_detected_count>0` (20)
  - `domination_lock_in` (16)
  - `stop:domination_lock_in_events>0` (16)
  - `explanation_policy_divergence` (12)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-057
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=5, conflict_ratio=0.889, overall_confidence=0.712
- Recent entries:
  - `2026-02-15T20:52:30Z` `experimental` `claim_probe_mech_057` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:50Z` `experimental` `claim_probe_mech_057` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:21Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:50Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:02Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=22, weakens=14, conflict_ratio=0.778, overall_confidence=0.709
- Recent entries:
  - `2026-02-15T21:11:17.270833Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T21:28:00Z` `literature` `targeted_review_connectome_mech_058` direction=`supports` confidence=0.78
  - `2026-02-15T21:29:00Z` `literature` `targeted_review_connectome_mech_058` direction=`supports` confidence=0.75
  - `2026-02-15T21:30:00Z` `literature` `targeted_review_connectome_mech_058` direction=`mixed` confidence=0.69
  - `2026-02-15T21:31:00Z` `literature` `targeted_review_connectome_mech_058` direction=`supports` confidence=0.71
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (12)
  - `mech058:ema_drift_under_shift` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=14, weakens=1, conflict_ratio=0.133, overall_confidence=0.766
- Recent entries:
  - `2026-02-15T21:37:16Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:37:28Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:37:39Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:37:51Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:38:03Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (18)
  - `mech059:abstention_reliability_collapse` (18)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=22, weakens=14, conflict_ratio=0.778, overall_confidence=0.7
- Recent entries:
  - `2026-02-15T21:11:17.331544Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T21:24:00Z` `literature` `targeted_review_connectome_mech_060` direction=`supports` confidence=0.73
  - `2026-02-15T21:25:00Z` `literature` `targeted_review_connectome_mech_060` direction=`supports` confidence=0.79
  - `2026-02-15T21:26:00Z` `literature` `targeted_review_connectome_mech_060` direction=`supports` confidence=0.76
  - `2026-02-15T21:27:00Z` `literature` `targeted_review_connectome_mech_060` direction=`mixed` confidence=0.64
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (12)
  - `mech060:attribution_reliability_break` (12)
  - `mech060:commitment_reversal_spike` (12)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-061
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=4, conflict_ratio=0.857, overall_confidence=0.654
- Recent entries:
  - `2026-02-15T18:09:24.550177Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
  - `2026-02-15T18:09:24.601905Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:15Z` `experimental` `claim_probe_mech_061` direction=`weakens` confidence=0.75
  - `2026-02-15T21:10:36Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:06Z` `experimental` `claim_probe_mech_061` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (4)
  - `mech060:attribution_reliability_break` (4)
  - `mech060:commitment_reversal_spike` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-001
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:42:59.843878Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:21Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:42Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:13Z` `experimental` `claim_probe_q_001` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:41Z` `experimental` `claim_probe_q_001` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-002
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:42:59.948094Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:22Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:43Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:13Z` `experimental` `claim_probe_q_002` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:42Z` `experimental` `claim_probe_q_002` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-003
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.057101Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:23Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:43Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:14Z` `experimental` `claim_probe_q_003` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:43Z` `experimental` `claim_probe_q_003` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-004
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.162877Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:24Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:44Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:15Z` `experimental` `claim_probe_q_004` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:44Z` `experimental` `claim_probe_q_004` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-005
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.275478Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:25Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:45Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:16Z` `experimental` `claim_probe_q_005` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:45Z` `experimental` `claim_probe_q_005` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-006
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.393190Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:26Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:46Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:17Z` `experimental` `claim_probe_q_006` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:45Z` `experimental` `claim_probe_q_006` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-007
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.506072Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:26Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:47Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:18Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:46Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-008
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.620452Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:27Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:48Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:18Z` `experimental` `claim_probe_q_008` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:47Z` `experimental` `claim_probe_q_008` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-009
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.738488Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:28Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:48Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:19Z` `experimental` `claim_probe_q_009` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:48Z` `experimental` `claim_probe_q_009` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-010
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.576
- Recent entries:
  - `2026-02-15T18:43:00.851513Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:29Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:49Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:20Z` `experimental` `claim_probe_q_010` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:49Z` `experimental` `claim_probe_q_010` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-012
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.66
- Recent entries:
  - `2026-02-15T18:05:24Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:12Z` `experimental` `claim_probe_q_012` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:32Z` `experimental` `claim_probe_q_012` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:02Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:33Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-013
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.634
- Recent entries:
  - `2026-02-15T18:10:25Z` `experimental` `claim_probe_q_013` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:20Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:39Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:10Z` `experimental` `claim_probe_q_013` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:39Z` `experimental` `claim_probe_q_013` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-014
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.634
- Recent entries:
  - `2026-02-15T18:10:27Z` `experimental` `claim_probe_q_014` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:21Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:41Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:12Z` `experimental` `claim_probe_q_014` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:40Z` `experimental` `claim_probe_q_014` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-015
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.616
- Recent entries:
  - `2026-02-15T18:05:29Z` `experimental` `claim_probe_q_015` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:16Z` `experimental` `claim_probe_q_015` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:36Z` `experimental` `claim_probe_q_015` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:07Z` `experimental` `claim_probe_q_015` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:36Z` `experimental` `claim_probe_q_015` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-017
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=22, weakens=16, conflict_ratio=0.842, overall_confidence=0.711
- Recent entries:
  - `2026-02-15T21:11:17.186174Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T21:20:00Z` `literature` `targeted_review_connectome_q_017` direction=`supports` confidence=0.78
  - `2026-02-15T21:21:00Z` `literature` `targeted_review_connectome_q_017` direction=`supports` confidence=0.8
  - `2026-02-15T21:22:00Z` `literature` `targeted_review_connectome_q_017` direction=`supports` confidence=0.74
  - `2026-02-15T21:23:00Z` `literature` `targeted_review_connectome_q_017` direction=`mixed` confidence=0.72
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (12)
  - `q017:control_axis_entropy_collapse` (12)
  - `q017:control_axis_policy_loss_spike` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
