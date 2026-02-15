# Dispatch: High-Priority Literature Queue (2026-02-15)

Generated: `2026-02-15T14:54:52.234233Z`

## Scope

- Target repo: `REE_assembly`
- Proposal count: `9`
- Objective: complete one focused literature cycle for all high-priority claim conflicts.

## Proposal Queue

| proposal_id | claim_id | suggested_literature_type | objective |
|---|---|---|---|
| `LIT-0005` | `ARC-018` | `targeted_review_v3_hippocampal_rollout` | Improve literature grounding and confidence for ARC-018. |
| `LIT-0008` | `MECH-033` | `targeted_review_v3_hippocampal_rollout` | Improve literature grounding and confidence for MECH-033. |
| `LIT-0010` | `MECH-040` | `targeted_review_mech_063` | Improve literature grounding and confidence for MECH-040. |
| `LIT-0015` | `MECH-056` | `targeted_review_v3_hippocampal_rollout` | Improve literature grounding and confidence for MECH-056. |
| `LIT-0018` | `MECH-058` | `targeted_review_mech_058` | Improve literature grounding and confidence for MECH-058. |
| `LIT-0020` | `MECH-059` | `targeted_review_v3_jepa_mapping_limits` | Improve literature grounding and confidence for MECH-059. |
| `LIT-0022` | `MECH-060` | `targeted_review_v3_prefrontal_control` | Improve literature grounding and confidence for MECH-060. |
| `LIT-0027` | `Q-011` | `targeted_review_q_011` | Improve literature grounding and confidence for Q-011. |
| `LIT-0033` | `Q-017` | `targeted_review_mech_063` | Improve literature grounding and confidence for Q-017. |

## Acceptance Checks

- At least 1 structured literature entry linked to `claim_ids_tested` for each proposal.
- Confidence explicitly justified in `confidence_rationale`.
- `evidence_direction` in `{supports, weakens, mixed, unknown}` and reflected in matrix after ingestion.

## Copy/Paste Execution Prompt

```md
You are Codex operating in `REE_assembly`.

Goal: execute all high-priority literature proposals below in one cycle.

Required proposals:
- `LIT-0005` / `ARC-018` / `targeted_review_v3_hippocampal_rollout`
- `LIT-0008` / `MECH-033` / `targeted_review_v3_hippocampal_rollout`
- `LIT-0010` / `MECH-040` / `targeted_review_mech_063`
- `LIT-0015` / `MECH-056` / `targeted_review_v3_hippocampal_rollout`
- `LIT-0018` / `MECH-058` / `targeted_review_mech_058`
- `LIT-0020` / `MECH-059` / `targeted_review_v3_jepa_mapping_limits`
- `LIT-0022` / `MECH-060` / `targeted_review_v3_prefrontal_control`
- `LIT-0027` / `Q-011` / `targeted_review_q_011`
- `LIT-0033` / `Q-017` / `targeted_review_mech_063`

Contract to follow exactly:
- `evidence/literature/INTERFACE_CONTRACT.md`
- `evidence/literature/schemas/v1/literature_evidence.schema.json`

Then run:
- `python3 evidence/experiments/scripts/build_experiment_indexes.py`
- `python3 evidence/planning/scripts/run_governance_cycle.py`

Output required:
- table of new literature entries (`literature_type`, `entry_id`, `claim_ids_tested`, `evidence_direction`, `confidence`)
- updated proposal/backlog deltas for the affected claims
```
