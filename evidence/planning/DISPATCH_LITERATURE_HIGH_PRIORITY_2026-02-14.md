# Dispatch: High-Priority Literature Queue (REE_assembly)

Generated: `2026-02-14`  
Target repo: `REE_assembly`  
Purpose: clear the current high-priority literature backlog driving conflict-heavy governance items.

## Work Queue (High Priority)

| proposal_id | claim_id | suggested_literature_type | objective | why_now |
| --- | --- | --- | --- | --- |
| `LIT-0005` | `ARC-018` | `targeted_review_v3_hippocampal_rollout` | Improve literature grounding and confidence for ARC-018. | active_conflict, directional_conflict_alert, missing_experimental_evidence |
| `LIT-0008` | `MECH-033` | `targeted_review_v3_hippocampal_rollout` | Improve literature grounding and confidence for MECH-033. | active_conflict, directional_conflict_alert, missing_experimental_evidence |
| `LIT-0013` | `MECH-056` | `targeted_review_v3_hippocampal_rollout` | Improve literature grounding and confidence for MECH-056. | active_conflict, directional_conflict_alert |
| `LIT-0016` | `MECH-058` | `targeted_review_mech_058` | Improve literature grounding and confidence for MECH-058. | active_conflict, directional_conflict_alert |
| `LIT-0018` | `MECH-059` | `targeted_review_v3_jepa_mapping_limits` | Improve literature grounding and confidence for MECH-059. | active_conflict, directional_conflict_alert |
| `LIT-0020` | `MECH-060` | `targeted_review_v3_prefrontal_control` | Improve literature grounding and confidence for MECH-060. | active_conflict, directional_conflict_alert |
| `LIT-0022` | `Q-011` | `targeted_review_q_011` | Improve literature grounding and confidence for Q-011. | active_conflict, directional_conflict_alert, low_overall_confidence |

## Acceptance Checks (Per Proposal)

- At least 1 structured literature entry linked to `claim_ids_tested`.
- Confidence explicitly justified in `confidence_rationale`.
- Direction is one of `supports|weakens|mixed|unknown` and is reflected in matrix.

## Copy/Paste Prompt

```md
You are Codex operating in `REE_assembly`.

Goal: execute the current high-priority literature evidence queue and emit contract-valid literature entries.

Scope:
- repo: `REE_assembly`
- modify only literature evidence records/summaries and generated indexes/planning outputs
- no unrelated architecture refactors

Literature contract (must follow):
- `evidence/literature/INTERFACE_CONTRACT.md`
- `evidence/literature/schemas/v1/literature_evidence.schema.json`

Required proposals to execute now:
- `LIT-0005` / `ARC-018` / `targeted_review_v3_hippocampal_rollout`
- `LIT-0008` / `MECH-033` / `targeted_review_v3_hippocampal_rollout`
- `LIT-0013` / `MECH-056` / `targeted_review_v3_hippocampal_rollout`
- `LIT-0016` / `MECH-058` / `targeted_review_mech_058`
- `LIT-0018` / `MECH-059` / `targeted_review_v3_jepa_mapping_limits`
- `LIT-0020` / `MECH-060` / `targeted_review_v3_prefrontal_control`
- `LIT-0022` / `Q-011` / `targeted_review_q_011`

Execution requirements:
1. Add at least one new entry per proposal under:
   - `evidence/literature/<literature_type>/entries/<entry_id>/record.json`
   - `evidence/literature/<literature_type>/entries/<entry_id>/summary.md`
2. Prefer primary sources (peer-reviewed journals/conference papers/canonical preprints).
3. Include concrete mapping caveats in each summary.
4. Do not duplicate an existing DOI + claim linkage unless the rationale is materially different.

After adding entries run:
- `python3 evidence/experiments/scripts/build_experiment_indexes.py`
- `python3 evidence/planning/scripts/run_governance_cycle.py`
- `python3 evidence/planning/scripts/emit_weekly_dispatches.py`

Output required:
1. Proposal completion table (proposal_id, entry_id, source, evidence_direction, confidence).
2. Validation summary (schema/ingestion PASS/FAIL).
3. Claim impact summary for `ARC-018`, `MECH-033`, `MECH-056`, `MECH-058`, `MECH-059`, `MECH-060`, `Q-011`:
   - updated direction counts
   - updated confidence
   - whether conflict_ratio improved.
4. Any remaining blockers for next governance cycle.
```
