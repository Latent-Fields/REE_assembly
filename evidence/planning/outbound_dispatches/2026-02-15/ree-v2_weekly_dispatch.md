# Weekly Dispatch - ree-v2

Generated: `2026-02-15T17:55:15.237598Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-v2`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`

## Proposals

| proposal_id | claim_id | priority | experiment_type | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- |
| `EXP-0005` | `MECH-059` | `high` | `jepa_uncertainty_channels` | Reduce uncertainty for MECH-059 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0020` | `ARC-007` | `high` | `claim_probe_arc_007` | Reduce uncertainty for ARC-007 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0021` | `ARC-018` | `high` | `claim_probe_arc_018` | Reduce uncertainty for ARC-018 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0022` | `MECH-033` | `high` | `claim_probe_mech_033` | Reduce uncertainty for MECH-033 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0023` | `Q-012` | `high` | `claim_probe_q_012` | Reduce uncertainty for Q-012 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0024` | `MECH-040` | `high` | `claim_probe_mech_040` | Reduce uncertainty for MECH-040 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0025` | `MECH-046` | `high` | `claim_probe_mech_046` | Reduce uncertainty for MECH-046 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0026` | `Q-015` | `high` | `claim_probe_q_015` | Reduce uncertainty for Q-015 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-v2`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0005` / `MECH-059` / `jepa_uncertainty_channels`
- `EXP-0020` / `ARC-007` / `claim_probe_arc_007`
- `EXP-0021` / `ARC-018` / `claim_probe_arc_018`
- `EXP-0022` / `MECH-033` / `claim_probe_mech_033`
- `EXP-0023` / `Q-012` / `claim_probe_q_012`
- `EXP-0024` / `MECH-040` / `claim_probe_mech_040`
- `EXP-0025` / `MECH-046` / `claim_probe_mech_046`
- `EXP-0026` / `Q-015` / `claim_probe_q_015`

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
