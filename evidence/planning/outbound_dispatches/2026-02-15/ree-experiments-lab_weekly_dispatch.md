# Weekly Dispatch - ree-experiments-lab

Generated: `2026-02-15T14:56:46.678173Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-experiments-lab`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`

## Proposals

| proposal_id | claim_id | priority | experiment_type | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- |
| `EXP-0014` | `MECH-056` | `high` | `trajectory_integrity` | Reduce uncertainty for MECH-056 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0017` | `MECH-058` | `high` | `jepa_anchor_ablation` | Reduce uncertainty for MECH-058 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0019` | `MECH-059` | `high` | `jepa_uncertainty_channels` | Reduce uncertainty for MECH-059 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0021` | `MECH-060` | `high` | `commit_dual_error_channels` | Reduce uncertainty for MECH-060 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0032` | `Q-017` | `high` | `control_axis_ablation` | Reduce uncertainty for Q-017 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-experiments-lab`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0014` / `MECH-056` / `trajectory_integrity`
- `EXP-0017` / `MECH-058` / `jepa_anchor_ablation`
- `EXP-0019` / `MECH-059` / `jepa_uncertainty_channels`
- `EXP-0021` / `MECH-060` / `commit_dual_error_channels`
- `EXP-0032` / `Q-017` / `control_axis_ablation`

Contract to follow exactly:
- `evidence/experiments/INTERFACE_CONTRACT.md`

Acceptance checks per proposal:
- At least 2 additional runs with distinct seeds.
- Experiment Pack validates against v1 schema.
- Result links to claim_ids_tested and updates matrix direction counts.

Output required:
- concise run table: run_id, seed, status, key metrics, evidence_direction
- list of generated run pack paths
```
