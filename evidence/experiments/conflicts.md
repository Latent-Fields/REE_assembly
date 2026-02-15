# Evidence Conflict Report

Generated: `2026-02-15T18:46:45.789785Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-003` | directional | 2 | 2 | 1 | `exp_0006_20260215T180924496279Z` | 4 |
| `ARC-007` | directional | 3 | 3 | 1 | `2026-02-15T181023Z_claim-probe-arc-007_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 6 |
| `ARC-018` | directional | 3 | 2 | 0.8 | `2026-02-15T180521Z_claim-probe-arc-018_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 5 |
| `MECH-033` | directional | 3 | 2 | 0.8 | `2026-02-15T180522Z_claim-probe-mech-033_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 5 |
| `MECH-040` | directional | 2 | 2 | 1 | `2026-02-15T180526Z_claim-probe-mech-040_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 4 |
| `MECH-046` | directional | 2 | 2 | 1 | `2026-02-15T180528Z_claim-probe-mech-046_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 4 |
| `MECH-056` | directional, source_disagreement | 8 | 22 | 0.533 | `exp_0004_20260215T180710843991Z` | 30 |
| `MECH-057` | directional | 2 | 2 | 1 | `2026-02-15T181028Z_claim-probe-mech-057_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 4 |
| `MECH-058` | directional | 16 | 14 | 0.933 | `exp_0002_20260215T180710622375Z` | 30 |
| `MECH-059` | directional, mixed_evidence | 14 | 1 | 0.133 | `2026-02-15T180517Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion_toyenv_internal_minimal` | 31 |
| `MECH-060` | directional | 16 | 14 | 0.933 | `exp_0003_20260215T180710733435Z` | 30 |
| `MECH-061` | directional | 2 | 2 | 1 | `exp_0007_20260215T180924601905Z` | 4 |
| `Q-001` | directional | 4 | 2 | 0.667 | `exp_0015_20260215T184259843878Z` | 7 |
| `Q-002` | directional | 4 | 2 | 0.667 | `exp_0016_20260215T184259948094Z` | 7 |
| `Q-003` | directional | 4 | 2 | 0.667 | `exp_0017_20260215T184300057101Z` | 7 |
| `Q-004` | directional | 4 | 2 | 0.667 | `exp_0018_20260215T184300162877Z` | 7 |
| `Q-005` | directional | 4 | 2 | 0.667 | `exp_0019_20260215T184300275478Z` | 7 |
| `Q-006` | directional | 4 | 2 | 0.667 | `exp_0020_20260215T184300393190Z` | 7 |
| `Q-007` | directional | 4 | 2 | 0.667 | `exp_0021_20260215T184300506072Z` | 7 |
| `Q-008` | directional | 4 | 2 | 0.667 | `exp_0022_20260215T184300620452Z` | 7 |
| `Q-009` | directional | 4 | 2 | 0.667 | `exp_0023_20260215T184300738488Z` | 7 |
| `Q-010` | directional | 4 | 2 | 0.667 | `exp_0024_20260215T184300851513Z` | 7 |
| `Q-012` | directional | 2 | 2 | 1 | `2026-02-15T180524Z_claim-probe-q-012_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 4 |
| `Q-013` | directional | 4 | 2 | 0.667 | `2026-02-15T181025Z_claim-probe-q-013_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 6 |
| `Q-014` | directional | 4 | 2 | 0.667 | `2026-02-15T181027Z_claim-probe-q-014_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 6 |
| `Q-015` | directional | 2 | 2 | 1 | `2026-02-15T180529Z_claim-probe-q-015_seed29_trajectory_first_enabled_toyenv_internal_minimal` | 4 |
| `Q-017` | directional, source_disagreement | 16 | 16 | 1 | `exp_0001_20260215T180710518955Z` | 32 |

## Conflict Details

### ARC-003
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.597
- Recent entries:
  - `2026-02-15T17:52:24Z` `experimental` `claim_probe_arc_003` direction=`weakens` confidence=0.75
  - `2026-02-15T17:52:25Z` `experimental` `claim_probe_arc_003` direction=`weakens` confidence=0.75
  - `2026-02-15T18:09:24.416725Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
  - `2026-02-15T18:09:24.496279Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (2)
  - `mech060:attribution_reliability_break` (2)
  - `mech060:commitment_reversal_spike` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=3, conflict_ratio=1, overall_confidence=0.58
- Recent entries:
  - `2026-02-15T17:52:44Z` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
  - `2026-02-15T18:05:18Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T18:05:19Z` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:22Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:23Z` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (3)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=2, conflict_ratio=0.8, overall_confidence=0.639
- Recent entries:
  - `2026-02-15T16:00:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-15T17:52:17Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:18Z` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
  - `2026-02-15T18:05:20Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
  - `2026-02-15T18:05:21Z` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=2, conflict_ratio=0.8, overall_confidence=0.637
- Recent entries:
  - `2026-02-15T16:01:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-15T17:52:19Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:20Z` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
  - `2026-02-15T18:05:22Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-02-15T18:05:22Z` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-040
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.607
- Recent entries:
  - `2026-02-15T17:52:29Z` `experimental` `claim_probe_mech_040` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:30Z` `experimental` `claim_probe_mech_040` direction=`weakens` confidence=0.75
  - `2026-02-15T18:05:25Z` `experimental` `claim_probe_mech_040` direction=`supports` confidence=0.75
  - `2026-02-15T18:05:26Z` `experimental` `claim_probe_mech_040` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-046
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.597
- Recent entries:
  - `2026-02-15T17:52:31Z` `experimental` `claim_probe_mech_046` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:32Z` `experimental` `claim_probe_mech_046` direction=`weakens` confidence=0.75
  - `2026-02-15T18:05:27Z` `experimental` `claim_probe_mech_046` direction=`supports` confidence=0.75
  - `2026-02-15T18:05:28Z` `experimental` `claim_probe_mech_046` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-056
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=8, weakens=22, conflict_ratio=0.533, overall_confidence=0.761
- Recent entries:
  - `2026-02-15T17:39:01Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:01Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T17:48:50Z` `experimental` `claim_probe_mech_056` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.784771Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.843991Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
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
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.662
- Recent entries:
  - `2026-02-15T17:52:21Z` `experimental` `claim_probe_mech_057` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:22Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:27Z` `experimental` `claim_probe_mech_057` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:28Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional
- Evidence breakdown: supports=16, weakens=14, conflict_ratio=0.933, overall_confidence=0.707
- Recent entries:
  - `2026-02-15T17:39:00Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T17:48:51Z` `experimental` `claim_probe_mech_058` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.571305Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.622375Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (12)
  - `mech058:ema_drift_under_shift` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=14, weakens=1, conflict_ratio=0.133, overall_confidence=0.767
- Recent entries:
  - `2026-02-15T17:48:52Z` `experimental` `claim_probe_mech_059` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:15Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T17:52:16Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T18:05:16Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T18:05:17Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (10)
  - `mech059:abstention_reliability_collapse` (10)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional
- Evidence breakdown: supports=16, weakens=14, conflict_ratio=0.933, overall_confidence=0.692
- Recent entries:
  - `2026-02-15T17:39:00Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T17:48:53Z` `experimental` `claim_probe_mech_060` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.676519Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.733435Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
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
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.586
- Recent entries:
  - `2026-02-15T17:52:34Z` `experimental` `claim_probe_mech_061` direction=`weakens` confidence=0.75
  - `2026-02-15T17:52:35Z` `experimental` `claim_probe_mech_061` direction=`weakens` confidence=0.75
  - `2026-02-15T18:09:24.550177Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
  - `2026-02-15T18:09:24.601905Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (2)
  - `mech060:attribution_reliability_break` (2)
  - `mech060:commitment_reversal_spike` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-001
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:47Z` `experimental` `claim_probe_q_001` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:05Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:06Z` `experimental` `claim_probe_q_001` direction=`weakens` confidence=0.75
  - `2026-02-15T18:42:59.779424Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
  - `2026-02-15T18:42:59.843878Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-002
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:49Z` `experimental` `claim_probe_q_002` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:07Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:07Z` `experimental` `claim_probe_q_002` direction=`weakens` confidence=0.75
  - `2026-02-15T18:42:59.895000Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
  - `2026-02-15T18:42:59.948094Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-003
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:50Z` `experimental` `claim_probe_q_003` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:08Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:09Z` `experimental` `claim_probe_q_003` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.001999Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.057101Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-004
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:52Z` `experimental` `claim_probe_q_004` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:10Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:11Z` `experimental` `claim_probe_q_004` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.110262Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.162877Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-005
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:54Z` `experimental` `claim_probe_q_005` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:12Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:13Z` `experimental` `claim_probe_q_005` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.217352Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.275478Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-006
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:55Z` `experimental` `claim_probe_q_006` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:13Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:14Z` `experimental` `claim_probe_q_006` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.334859Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.393190Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-007
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:57Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:15Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:16Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.447687Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.506072Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-008
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:52:59Z` `experimental` `claim_probe_q_008` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:17Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:18Z` `experimental` `claim_probe_q_008` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.563567Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.620452Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-009
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:53:00Z` `experimental` `claim_probe_q_009` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:18Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:19Z` `experimental` `claim_probe_q_009` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.683082Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.738488Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-010
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.621
- Recent entries:
  - `2026-02-15T17:53:02Z` `experimental` `claim_probe_q_010` direction=`weakens` confidence=0.75
  - `2026-02-15T18:10:20Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:21Z` `experimental` `claim_probe_q_010` direction=`weakens` confidence=0.75
  - `2026-02-15T18:43:00.795784Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
  - `2026-02-15T18:43:00.851513Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-012
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.634
- Recent entries:
  - `2026-02-15T17:52:23Z` `experimental` `claim_probe_q_012` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:23Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
  - `2026-02-15T18:05:23Z` `experimental` `claim_probe_q_012` direction=`supports` confidence=0.75
  - `2026-02-15T18:05:24Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-013
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.67
- Recent entries:
  - `2026-02-15T17:52:39Z` `experimental` `claim_probe_q_013` direction=`weakens` confidence=0.75
  - `2026-02-15T18:09:24.657062Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
  - `2026-02-15T18:09:24.711353Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:24Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:25Z` `experimental` `claim_probe_q_013` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-014
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.67
- Recent entries:
  - `2026-02-15T17:52:40Z` `experimental` `claim_probe_q_014` direction=`weakens` confidence=0.75
  - `2026-02-15T18:09:24.769428Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
  - `2026-02-15T18:09:24.822843Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:26Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
  - `2026-02-15T18:10:27Z` `experimental` `claim_probe_q_014` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-015
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.586
- Recent entries:
  - `2026-02-15T17:52:41Z` `experimental` `claim_probe_q_015` direction=`supports` confidence=0.75
  - `2026-02-15T17:52:42Z` `experimental` `claim_probe_q_015` direction=`weakens` confidence=0.75
  - `2026-02-15T18:05:28Z` `experimental` `claim_probe_q_015` direction=`supports` confidence=0.75
  - `2026-02-15T18:05:29Z` `experimental` `claim_probe_q_015` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (2)
  - `domination_lock_in` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-017
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=16, weakens=16, conflict_ratio=1, overall_confidence=0.72
- Recent entries:
  - `2026-02-15T17:39:00Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T17:48:55Z` `experimental` `claim_probe_q_017` direction=`supports` confidence=0.75
  - `2026-02-15T18:06:29.490159Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T18:07:10.436413Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.518955Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (12)
  - `q017:control_axis_entropy_collapse` (12)
  - `q017:control_axis_policy_loss_spike` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
