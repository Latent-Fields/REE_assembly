# Dispatch Shortlist

Generated: `2026-02-13`
Source: `evidence/planning/experiment_proposals.v1.json`

This shortlist reflects current high-priority proposals.

## Batch 1 - Experimental

### EXP-0001
- `proposal_id`: `EXP-0001`
- `backlog_id`: `EVB-0001`
- `claim_id`: `MECH-056`
- `proposal_type`: `experimental`
- `target_repo`: `ree-experiments-lab`
- `suggested_experiment_type`: `trajectory_integrity`
- `objective`: Reduce uncertainty for MECH-056 via targeted experiment runs.
- `why_now`: `active_conflict`, `directional_conflict_alert`
- `routing_rationale`:
  - missing required capabilities on default repo:
    - `trajectory_integrity_channelized_bias`
    - `mech056_dispatch_metric_set`
    - `mech056_summary_escalation_trace`
  - capability gate fallback to `ree-experiments-lab`
- `acceptance_checks`:
  - At least 2 additional runs with distinct seeds.
  - Experiment Pack validates against v1 schema.
  - Result links to claim_ids_tested and updates matrix direction counts.
  - Required metric keys are present in metrics.json for each run:
    - `trajectory_commit_channel_usage_count`
    - `perceptual_sampling_channel_usage_count`
    - `structural_consolidation_channel_usage_count`
    - `precommit_semantic_overwrite_events`
    - `structural_bias_magnitude`
    - `structural_bias_rate`
  - `precommit_semantic_overwrite_events` remains zero on PASS runs.
  - Summary states whether non-primary channels were activated and why.
  - `manifest.json` includes `producer_capabilities` with required capability flags set true.

### EXP-0003
- `proposal_id`: `EXP-0003`
- `backlog_id`: `EVB-0002`
- `claim_id`: `Q-011`
- `proposal_type`: `experimental`
- `target_repo`: `ree-experiments-lab`
- `suggested_experiment_type`: `trajectory_integrity`
- `objective`: Reduce uncertainty for Q-011 via targeted experiment runs.
- `why_now`: `active_conflict`, `directional_conflict_alert`
- `acceptance_checks`:
  - At least 2 additional runs with distinct seeds.
  - Experiment Pack validates against v1 schema.
  - Result links to claim_ids_tested and updates matrix direction counts.

## Batch 2 - Literature (REE_assembly)

### LIT-0002
- `proposal_id`: `LIT-0002`
- `backlog_id`: `EVB-0001`
- `claim_id`: `MECH-056`
- `proposal_type`: `literature_review`
- `target_repo`: `REE_assembly`
- `suggested_literature_type`: `targeted_review_mech_056`
- `objective`: Improve literature grounding and confidence for MECH-056.
- `why_now`: `active_conflict`, `directional_conflict_alert`
- `acceptance_checks`:
  - At least 1 structured literature entry linked to claim_ids_tested.
  - Confidence explicitly justified in confidence_rationale.
  - Direction is supports/weakens/mixed/unknown and reflected in matrix.

### LIT-0004
- `proposal_id`: `LIT-0004`
- `backlog_id`: `EVB-0002`
- `claim_id`: `Q-011`
- `proposal_type`: `literature_review`
- `target_repo`: `REE_assembly`
- `suggested_literature_type`: `targeted_review_q_011`
- `objective`: Improve literature grounding and confidence for Q-011.
- `why_now`: `active_conflict`, `directional_conflict_alert`
- `acceptance_checks`:
  - At least 1 structured literature entry linked to claim_ids_tested.
  - Confidence explicitly justified in confidence_rationale.
  - Direction is supports/weakens/mixed/unknown and reflected in matrix.

## Completion Signals

- Experimental packs appear under `evidence/experiments/<experiment_type>/runs/<run_id>/`.
- Literature records appear under `evidence/literature/<literature_type>/entries/<entry_id>/`.
- After ingestion run, conflict ratio for `MECH-056` and `Q-011` should update in:
  - `evidence/experiments/conflicts.md`
  - `evidence/experiments/claim_evidence.v1.json`
