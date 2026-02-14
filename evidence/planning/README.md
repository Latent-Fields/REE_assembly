# Evidence Planning Subsystem

This folder closes the architecture loop by converting current evidence into a machine-readable work queue.

## Generated Outputs

- `evidence_backlog.v1.json`: claims requiring new evidence and why.
- `experiment_proposals.v1.json`: concrete proposed work items for experimental/literature producers.
- `INDEX.md`: generated summary.
- `structure_review/latest/INDEX.md`: latest human-readable structure review dossier index.
- `structure_review/latest/structure_review_report.v1.json`: latest dossier generation report.
- `DISPATCH_*.md`: curated copy/paste dispatch bundles for active claim batches.
- `WEEKLY_HANDOFF_TEMPLATE.md`: shared producer handoff packet format for `ree-v2`, `ree-experiments-lab`, and `ree-v1-minimal`.
- `HOBBY_OPERATOR_PLAYBOOK.md`: weekly structured workflow and buy/hold compute decision policy for spare-time operation.
- `LOCAL_CADENCE_AUTOMATION.md`: local scheduler runbook for weekly handoff pull/ingest and outbound dispatch emission.

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

This also generates structure review dossiers from the architecture gap register:

- `evidence/planning/structure_review/<YYYY-MM-DD>/<CLAIM_ID>/DOSSIER.md`
- `evidence/planning/structure_review/<YYYY-MM-DD>/<CLAIM_ID>/dossier.v1.json`
- `evidence/planning/structure_review/latest/INDEX.md`

Run dossier generation directly:

```bash
python3 evidence/planning/scripts/build_structure_review_dossiers.py
```

Strict thought gate mode:

```bash
python3 evidence/planning/scripts/run_governance_cycle.py --strict-thoughts
```

## Cadence Automation Scripts

- Pull/import handoffs:
  - `python3 evidence/planning/scripts/sync_weekly_handoffs.py --day MONDAY`
- Emit weekly dispatch bundles:
  - `python3 evidence/planning/scripts/emit_weekly_dispatches.py`
- Run ree-v2 cutover readiness (adjudicated divergence mode):
  - `python3 evidence/planning/scripts/check_ree_v2_cutover_readiness.py`
  - add `--apply-cutover` to flip `experimental_default_repo` to `ree-v2` only when all gates pass

See:

- `evidence/planning/LOCAL_CADENCE_AUTOMATION.md`
