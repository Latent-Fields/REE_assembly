# Dispatch Shortlist

Generated: `2026-02-13`
Source: `evidence/planning/experiment_proposals.v1.json`

This shortlist is the approved high-priority dispatch set for current conflict adjudication.

## Batch 1 - Experimental (ree-experiments-lab)

### EXP-0003
- `proposal_id`: `EXP-0003`
- `backlog_id`: `EVB-0003`
- `claim_id`: `MECH-056`
- `proposal_type`: `experimental`
- `target_repo`: `ree-experiments-lab`
- `suggested_experiment_type`: `trajectory_integrity`
- `objective`: Reduce uncertainty for MECH-056 via targeted experiment runs.
- `why_now`: `active_conflict`, `directional_conflict_alert`, `low_overall_confidence`, `missing_literature_evidence`
- `acceptance_checks`:
  - At least 2 additional runs with distinct seeds.
  - Experiment Pack validates against v1 schema.
  - Result links to claim_ids_tested and updates matrix direction counts.

### EXP-0005
- `proposal_id`: `EXP-0005`
- `backlog_id`: `EVB-0004`
- `claim_id`: `Q-011`
- `proposal_type`: `experimental`
- `target_repo`: `ree-experiments-lab`
- `suggested_experiment_type`: `trajectory_integrity`
- `objective`: Reduce uncertainty for Q-011 via targeted experiment runs.
- `why_now`: `active_conflict`, `directional_conflict_alert`, `low_overall_confidence`, `missing_literature_evidence`
- `acceptance_checks`:
  - At least 2 additional runs with distinct seeds.
  - Experiment Pack validates against v1 schema.
  - Result links to claim_ids_tested and updates matrix direction counts.

## Batch 2 - Literature (REE_assembly)

### LIT-0004
- `proposal_id`: `LIT-0004`
- `backlog_id`: `EVB-0003`
- `claim_id`: `MECH-056`
- `proposal_type`: `literature_review`
- `target_repo`: `REE_assembly`
- `suggested_literature_type`: `targeted_review_mech_056`
- `objective`: Improve literature grounding and confidence for MECH-056.
- `why_now`: `active_conflict`, `directional_conflict_alert`, `low_overall_confidence`, `missing_literature_evidence`
- `acceptance_checks`:
  - At least 1 structured literature entry linked to claim_ids_tested.
  - Confidence explicitly justified in confidence_rationale.
  - Direction is supports/weakens/mixed/unknown and reflected in matrix.

### LIT-0006
- `proposal_id`: `LIT-0006`
- `backlog_id`: `EVB-0004`
- `claim_id`: `Q-011`
- `proposal_type`: `literature_review`
- `target_repo`: `REE_assembly`
- `suggested_literature_type`: `targeted_review_q_011`
- `objective`: Improve literature grounding and confidence for Q-011.
- `why_now`: `active_conflict`, `directional_conflict_alert`, `low_overall_confidence`, `missing_literature_evidence`
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

