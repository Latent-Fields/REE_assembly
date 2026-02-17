# Weekly Dispatch - ree-experiments-lab

Generated: `2026-02-17T22:53:49.229420Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-experiments-lab`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`

## Proposals

| proposal_id | claim_id | priority | experiment_type | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- |
| `EXP-0001` | `MECH-057` | `high` | `claim_probe_mech_057` | Reduce uncertainty for MECH-057 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0002` | `MECH-056` | `high` | `trajectory_integrity` | Reduce uncertainty for MECH-056 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0003` | `Q-013` | `high` | `claim_probe_q_013` | Reduce uncertainty for Q-013 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0004` | `Q-014` | `high` | `claim_probe_q_014` | Reduce uncertainty for Q-014 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0005` | `ARC-003` | `high` | `claim_probe_arc_003` | Reduce uncertainty for ARC-003 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0006` | `Q-008` | `high` | `claim_probe_q_008` | Reduce uncertainty for Q-008 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0007` | `Q-009` | `high` | `claim_probe_q_009` | Reduce uncertainty for Q-009 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0008` | `Q-012` | `high` | `claim_probe_q_012` | Reduce uncertainty for Q-012 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-experiments-lab`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0001` / `MECH-057` / `claim_probe_mech_057`
- `EXP-0002` / `MECH-056` / `trajectory_integrity`
- `EXP-0003` / `Q-013` / `claim_probe_q_013`
- `EXP-0004` / `Q-014` / `claim_probe_q_014`
- `EXP-0005` / `ARC-003` / `claim_probe_arc_003`
- `EXP-0006` / `Q-008` / `claim_probe_q_008`
- `EXP-0007` / `Q-009` / `claim_probe_q_009`
- `EXP-0008` / `Q-012` / `claim_probe_q_012`

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
