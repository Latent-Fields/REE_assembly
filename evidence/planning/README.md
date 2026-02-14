# Evidence Planning Subsystem

This folder closes the architecture loop by converting current evidence into a machine-readable work queue.

## Generated Outputs

- `evidence_backlog.v1.json`: claims requiring new evidence and why.
- `experiment_proposals.v1.json`: concrete proposed work items for experimental/literature producers.
- `INDEX.md`: generated summary.
- `DISPATCH_*.md`: curated copy/paste dispatch bundles for active claim batches.
- `WEEKLY_HANDOFF_TEMPLATE.md`: shared producer handoff packet format for `ree-v2`, `ree-experiments-lab`, and `ree-v1-minimal`.

## Inputs

- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/conflicts.md`
- `evidence/experiments/promotion_demotion_recommendations.md`
- `evidence/decisions/decision_log.v1.jsonl`

## Configuration

- `planning_criteria.v1.yaml`: thresholds and repo-routing hints.

## Generation

```bash
python3 evidence/experiments/scripts/build_experiment_indexes.py
```

The planning files are regenerated on each run.

## Governance Cycle Helper

Run non-decision maintenance steps and generate a discussion agenda:

```bash
python3 evidence/planning/scripts/run_governance_cycle.py
```

Generated agenda outputs:

- `governance_agenda.v1.json`
- `GOVERNANCE_AGENDA.md`

Strict thought gate mode:

```bash
python3 evidence/planning/scripts/run_governance_cycle.py --strict-thoughts
```
