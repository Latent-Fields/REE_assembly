# Experiment Dispatch Briefs

Generated: `2026-02-13T19:12:52.846560Z`

Human-readable briefs for high-priority experimental proposals, including routing and capability-gate context.

## EXP-0001 — MECH-056

- Target repo: `ree-v1-minimal`
- Experiment type: `trajectory_integrity`
- Objective: Reduce uncertainty for MECH-056 via targeted experiment runs.
- What it tests:
  - Whether policy execution preserves trajectory ledger integrity under replay, intervention, and post-commit updates.
  - Whether explanation traces remain aligned with selected policy outcomes.
- Failure modes:
  - ledger editing
  - domination/lock-in dynamics
  - explanation-policy divergence
- Required metric keys:
  - `trajectory_commit_channel_usage_count`
  - `perceptual_sampling_channel_usage_count`
  - `structural_consolidation_channel_usage_count`
  - `precommit_semantic_overwrite_events`
  - `structural_bias_magnitude`
  - `structural_bias_rate`
  - `environment_shortcut_leakage_events`
  - `environment_unobservable_critical_state_rate`
  - `environment_controllability_score`
  - `environment_transition_consistency_rate`
- Required environment fields:
  - `env_id`
  - `env_version`
  - `dynamics_hash`
  - `reward_hash`
  - `observation_hash`
  - `config_hash`
  - `tier`
- Required environment tiers across run set:
  - `toy`
  - `stress`
- Summary must include:
  - channel escalation order observed (trajectory_commit -> perceptual_sampling -> structural_consolidation when triggered)
  - explicit trigger rationale for each non-primary channel activation
- Required producer capabilities:
  - `trajectory_integrity_channelized_bias`
  - `mech056_dispatch_metric_set`
  - `mech056_summary_escalation_trace`
- Latest observed run context: `exp_0005_20260213T090639999186Z` status=`FAIL` timestamp=`2026-02-13T09:06:39.999186Z` source_repo=`ree-experiments-lab`
- Experiment profile: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/experiment.md`

## EXP-0003 — MECH-057

- Target repo: `ree-v1-minimal`
- Experiment type: `claim_probe_mech_057`
- Objective: Reduce uncertainty for MECH-057 via targeted experiment runs.
- Required metric keys:
  - `environment_shortcut_leakage_events`
  - `environment_unobservable_critical_state_rate`
- Required environment fields:
  - `env_id`
  - `env_version`
  - `dynamics_hash`
  - `reward_hash`
  - `observation_hash`
  - `config_hash`
  - `tier`
- Required environment tiers across run set:
  - `toy`
  - `stress`
- Experiment profile: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/claim_probe_mech_057/experiment.md`

## EXP-0004 — Q-011

- Target repo: `ree-experiments-lab`
- Experiment type: `trajectory_integrity`
- Objective: Reduce uncertainty for Q-011 via targeted experiment runs.
- Routing rationale:
  - conflict_ratio=0.8 >= 0.7, using exploratory repo
- What it tests:
  - Whether policy execution preserves trajectory ledger integrity under replay, intervention, and post-commit updates.
  - Whether explanation traces remain aligned with selected policy outcomes.
- Failure modes:
  - ledger editing
  - domination/lock-in dynamics
  - explanation-policy divergence
- Required metric keys:
  - `environment_shortcut_leakage_events`
  - `environment_unobservable_critical_state_rate`
  - `environment_controllability_score`
  - `environment_transition_consistency_rate`
- Required environment fields:
  - `env_id`
  - `env_version`
  - `dynamics_hash`
  - `reward_hash`
  - `observation_hash`
  - `config_hash`
  - `tier`
- Required environment tiers across run set:
  - `toy`
  - `stress`
- Latest observed run context: `exp_0005_20260213T090639999186Z` status=`FAIL` timestamp=`2026-02-13T09:06:39.999186Z` source_repo=`ree-experiments-lab`
- Experiment profile: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/trajectory_integrity/experiment.md`

## EXP-0006 — Q-012

- Target repo: `ree-v1-minimal`
- Experiment type: `claim_probe_q_012`
- Objective: Reduce uncertainty for Q-012 via targeted experiment runs.
- Required metric keys:
  - `environment_shortcut_leakage_events`
  - `environment_unobservable_critical_state_rate`
- Required environment fields:
  - `env_id`
  - `env_version`
  - `dynamics_hash`
  - `reward_hash`
  - `observation_hash`
  - `config_hash`
  - `tier`
- Required environment tiers across run set:
  - `toy`
  - `stress`
- Experiment profile: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/claim_probe_q_012/experiment.md`
