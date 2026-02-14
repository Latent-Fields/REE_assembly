# Weekly Dispatch - ree-v1-minimal

Generated: `2026-02-14T18:40:06.372124Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-v1-minimal`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`

## Proposals

| proposal_id | claim_id | priority | experiment_type | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-v1-minimal`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:

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
