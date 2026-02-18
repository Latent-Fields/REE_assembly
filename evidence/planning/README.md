# Evidence Planning Subsystem

This folder closes the architecture loop by converting current evidence into a machine-readable work queue.

## Generated Outputs

- `evidence_backlog.v1.json`: claims requiring new evidence and why.
- `experiment_proposals.v1.json`: concrete proposed work items for experimental/literature producers.
- `INDEX.md`: generated summary.
- `structure_review/latest/INDEX.md`: latest active structure review dossier index (compatibility alias).
- `structure_review/latest/ACTIVE_INDEX.md`: latest active dossiers (current governance-relevant set).
- `structure_review/latest/ARCHIVE_INDEX.md`: historical/archived dossiers (prior cycles and non-active).
- `structure_review/latest/structure_review_report.v1.json`: latest dossier generation report.
- `connectome_literature_pull.v1.json`: connectome-oriented literature pull queue for structure-pressure claims.
- `CONNECTOME_LITERATURE_PULL.md`: human-readable connectome pull brief + copy/paste execution prompt.
- `connectome_pull_state.v1.json`: persistent completion/reopen state for connectome pull claims.
- `ADJUDICATION_CASCADE_PATCH_QUEUE.md`: generated architecture/doc patch queue after adjudication-cascade application.
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
- `planning_criteria.v1.yaml#model_adjudication`: JEPA-vs-REE conflict outcomes, cascade policy, temporary override mode, and anti-lock-in gate.

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

This now includes markdown task-inbox sync by default:

- `evidence/planning/task_inbox.md` (`- [ ]` open, `- [x]` done)
- synced into `evidence/planning/manual_carryover_items.v1.json` before agenda generation
- completed `- [x]` lines are pruned from inbox on sync (override with `--no-prune-completed`)

Generated agenda outputs:

- `governance_agenda.v1.json`
- `GOVERNANCE_AGENDA.md`
- `GOVERNANCE_AGENDA.md` now begins Discussion Checkpoints with an `Autonomy Triage` table (`AUTO`, `AUTO_WITH_APPROVAL`, `HUMAN_ONLY`).

This also runs adjudication-cascade application by default for `decision_status=applied`:

- `evidence/planning/scripts/apply_adjudication_cascade.py`
- output state: `evidence/decisions/adjudication_cascade_state.v1.json`
- output queue: `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`

This also generates structure review dossiers from the architecture gap register:

- `evidence/planning/structure_review/<YYYY-MM-DD>/<CLAIM_ID>/DOSSIER.md`
- `evidence/planning/structure_review/<YYYY-MM-DD>/<CLAIM_ID>/dossier.v1.json`
- `evidence/planning/structure_review/latest/INDEX.md`
- `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`
- `evidence/planning/structure_review/latest/ARCHIVE_INDEX.md`

It also generates connectome literature pull planning outputs:

- `evidence/planning/connectome_literature_pull.v1.json`
- `evidence/planning/CONNECTOME_LITERATURE_PULL.md`

Run dossier generation directly:

```bash
python3 evidence/planning/scripts/build_structure_review_dossiers.py
```

Run connectome pull queue generation directly:

```bash
python3 evidence/planning/scripts/build_connectome_literature_pull.py
```

Run adjudication-cascade directly:

```bash
python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses applied
```

Strict thought gate mode:

```bash
python3 evidence/planning/scripts/run_governance_cycle.py --strict-thoughts
```

## Cadence Automation Scripts

- Pull/import handoffs:
  - `python3 evidence/planning/scripts/sync_weekly_handoffs.py --day MONDAY`
  - full cross-repo sync on demand: `python3 evidence/planning/scripts/sync_weekly_handoffs.py --full-run --run-ingestion`
- Emit weekly dispatch bundles:
  - `python3 evidence/planning/scripts/emit_weekly_dispatches.py`
- Apply adjudication cascade from applied decisions:
  - `python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses applied`
- Run ree-v2 cutover readiness (adjudicated divergence mode):
  - `python3 evidence/planning/scripts/check_ree_v2_cutover_readiness.py`
  - add `--apply-cutover` to flip `experimental_default_repo` to `ree-v2` only when all gates pass

See:

- `evidence/planning/LOCAL_CADENCE_AUTOMATION.md`

## Manual Carryover Queue

To ensure unfinished governance items persist across weekly/full-run agenda regeneration, track them in:

- `evidence/planning/manual_carryover_items.v1.json`

`run_governance_cycle.py` automatically merges all items with `status != done` into the generated agenda under
`manual_carryover`.

Quick capture commands:

- add a task:
  - `python3 evidence/planning/scripts/capture_carryover_item.py add --summary "Your task here" --priority high`
- list open tasks:
  - `python3 evidence/planning/scripts/capture_carryover_item.py list --open-only`
- mark done:
  - `python3 evidence/planning/scripts/capture_carryover_item.py done --item-id MCI-0002`

Checklist inbox sync command:

- dry-run:
  - `python3 evidence/planning/scripts/sync_task_inbox.py --dry-run`
- write mode:
  - `python3 evidence/planning/scripts/sync_task_inbox.py`
