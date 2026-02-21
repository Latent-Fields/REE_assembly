# Weekly Dispatch - ree-openclaw

Generated: `2026-02-21T13:01:54.607462Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-openclaw`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`
- Architecture epoch: `ree_hybrid_guardrails_v1`
- Epoch start (UTC): `2026-02-15T15:31:31Z`
- Epoch policy source: `evidence/planning/planning_criteria.v1.yaml`

## Proposals

| proposal_id | claim_id | priority | experiment_type | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-openclaw`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:

Contract to follow exactly:
- `evidence/experiments/INTERFACE_CONTRACT.md`

Epoch tagging requirements:
- Stamp every new run `manifest.json` with `"architecture_epoch": "ree_hybrid_guardrails_v1"`.
- Keep `timestamp_utc` aligned with the current epoch window (`>= 2026-02-15T15:31:31Z`).

Acceptance checks per proposal:
- At least 2 additional runs with distinct seeds.
- Experiment Pack validates against v1 schema.
- Each emitted manifest includes `architecture_epoch=ree_hybrid_guardrails_v1`.
- Result links to claim_ids_tested and updates matrix direction counts.

Output required:
- concise run table: run_id, seed, status, key metrics, evidence_direction
- list of generated run pack paths
```
