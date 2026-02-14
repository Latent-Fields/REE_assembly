# Weekly Dispatch - ree-v2

Generated: `2026-02-14T19:22:12.639234Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-v2`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`

## Proposals

| proposal_id | claim_id | priority | experiment_type | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- |
| `EXP-0001` | `ARC-003` | `high` | `claim_probe_arc_003` | Reduce uncertainty for ARC-003 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0002` | `ARC-005` | `high` | `claim_probe_arc_005` | Reduce uncertainty for ARC-005 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0003` | `ARC-007` | `high` | `claim_probe_arc_007` | Reduce uncertainty for ARC-007 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0004` | `ARC-018` | `high` | `claim_probe_arc_018` | Reduce uncertainty for ARC-018 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0006` | `IMPL-022` | `high` | `claim_probe_impl_022` | Reduce uncertainty for IMPL-022 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0007` | `MECH-033` | `high` | `claim_probe_mech_033` | Reduce uncertainty for MECH-033 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0009` | `MECH-046` | `high` | `claim_probe_mech_046` | Reduce uncertainty for MECH-046 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0010` | `MECH-053` | `high` | `claim_probe_mech_053` | Reduce uncertainty for MECH-053 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-v2`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0001` / `ARC-003` / `claim_probe_arc_003`
- `EXP-0002` / `ARC-005` / `claim_probe_arc_005`
- `EXP-0003` / `ARC-007` / `claim_probe_arc_007`
- `EXP-0004` / `ARC-018` / `claim_probe_arc_018`
- `EXP-0006` / `IMPL-022` / `claim_probe_impl_022`
- `EXP-0007` / `MECH-033` / `claim_probe_mech_033`
- `EXP-0009` / `MECH-046` / `claim_probe_mech_046`
- `EXP-0010` / `MECH-053` / `claim_probe_mech_053`

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
