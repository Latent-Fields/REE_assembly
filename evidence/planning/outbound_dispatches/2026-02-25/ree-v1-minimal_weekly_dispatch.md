# Weekly Dispatch - ree-v1-minimal

Generated: `2026-02-25T17:56:37.301803Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-v1-minimal`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`
- Architecture epoch: `ree_hybrid_guardrails_v1`
- Epoch start (UTC): `2026-02-15T15:31:31Z`
- Epoch policy source: `evidence/planning/planning_criteria.v1.yaml`

## Proposals

| proposal_id | claim_id | priority | experiment_type | dispatch_mode | decision_deadline_utc | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-v1-minimal`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:

Contract to follow exactly:
- `evidence/experiments/INTERFACE_CONTRACT.md`

Epoch tagging requirements:
- Stamp every new run `manifest.json` with `"architecture_epoch": "ree_hybrid_guardrails_v1"`.
- Keep `timestamp_utc` aligned with the current epoch window (`>= 2026-02-15T15:31:31Z`).

Acceptance checks per proposal:
- At least 2 additional runs with distinct seeds unless stricter pair checks are specified in proposal acceptance checks.
- Experiment Pack validates against v1 schema.
- Each emitted manifest includes `architecture_epoch=ree_hybrid_guardrails_v1`.
- Result links to claim_ids_tested and updates matrix direction counts.

Output required:
- concise run table: run_id, seed, status, key metrics, evidence_direction
- list of generated run pack paths
```
