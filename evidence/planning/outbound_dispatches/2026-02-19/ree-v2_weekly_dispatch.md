# Weekly Dispatch - ree-v2

Generated: `2026-02-19T07:51:19.921131Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-v2`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`

## Proposals

| proposal_id | claim_id | priority | experiment_type | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- |
| `EXP-0017` | `ARC-018` | `high` | `claim_probe_arc_018` | Reduce uncertainty for ARC-018 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0018` | `Q-007` | `high` | `claim_probe_q_007` | Reduce uncertainty for Q-007 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0019` | `MECH-033` | `high` | `claim_probe_mech_033` | Reduce uncertainty for MECH-033 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0020` | `ARC-007` | `high` | `claim_probe_arc_007` | Reduce uncertainty for ARC-007 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0021` | `MECH-059` | `high` | `jepa_uncertainty_channels` | Reduce uncertainty for MECH-059 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0022` | `Q-018` | `low` | `claim_probe_q_018` | Reduce uncertainty for Q-018 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-v2`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0017` / `ARC-018` / `claim_probe_arc_018`
- `EXP-0018` / `Q-007` / `claim_probe_q_007`
- `EXP-0019` / `MECH-033` / `claim_probe_mech_033`
- `EXP-0020` / `ARC-007` / `claim_probe_arc_007`
- `EXP-0021` / `MECH-059` / `jepa_uncertainty_channels`
- `EXP-0022` / `Q-018` / `claim_probe_q_018`

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
