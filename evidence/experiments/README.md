# Experimental Evidence Subsystem

This folder is the ingestion boundary between implementation experiments (e.g., `ree-v1-minimal`) and REE architecture docs.

## Purpose

- Store machine-readable experiment artefacts in a stable, versioned format.
- Generate indexes that make PASS/FAIL trends visible at a glance.
- Turn repeated failures into concrete design TODOs so experiments drive architecture updates.
- Merge experiment evidence with literature evidence for claim-level confidence and conflict tracking.
- Surface human-in-the-loop promotion/demotion decisions (never auto-apply status changes).

## Folder Layout

- `INTERFACE_CONTRACT.md`: strict format contract for producers.
- `CROSS_REPO_SYNC_POLICY.md`: lockstep policy across producer repos.
- `stop_criteria.v1.yaml`: versioned stop/fail criteria used by ingestion.
- `decision_criteria.v1.yaml`: versioned decision thresholds for promotion/demotion recommendations.
- `schemas/v1/`: JSON schema references for pack files.
- `claim_evidence.v1.json`: generated claim-to-evidence matrix (do not hand edit).
- `conflicts.md`: generated conflict report across evidence sources (do not hand edit).
- `promotion_demotion_recommendations.md`: generated human decision queue (do not hand edit).
- `../decisions/decision_log.v1.jsonl`: persistent append-only human decisions.
- `../decisions/decision_state.v1.json`: generated latest decision state by claim.
- `../planning/evidence_backlog.v1.json`: generated evidence gaps and priorities.
- `../planning/experiment_proposals.v1.json`: generated proposals for experimental/literature work.
- `<experiment_type>/experiment.md`: experiment template with required sections.
- `<experiment_type>/runs/<run_id>/`: immutable run packs.
- `scripts/build_experiment_indexes.py`: ingestion + index generator.
- `INDEX.md`: generated top-level index (do not hand edit).
- `TODOs.md`: generated failure-driven TODO queue (do not hand edit).

## Experiment Pack (required files)

Each run directory must include:

- `manifest.json`
- `metrics.json`
- `summary.md`
- optional `jepa_adapter_signals.v1.json` (required if `manifest.artifacts.adapter_signals_path` is declared)
- optional `traces/`
- optional `media/`

See `INTERFACE_CONTRACT.md` for field-level requirements.
For claim-level evidence mapping, include `claim_ids_tested`, `evidence_class`, and `evidence_direction` in
`manifest.json`.

For JEPA-backed runs, attach adapter signal coverage via `jepa_adapter_signals.v1.json` and
`manifest.artifacts.adapter_signals_path`. Ingestion validates this contract and marks invalid files as FAIL.

`evidence_class` values from experiment packs are treated as experimental classes (`exp:*`) in the
claim-evidence matrix.

## Experiment Template (required per type)

Each experiment type keeps `experiment.md` with these sections:

- `## What it tests`
- `## Failure modes it detects`
- `## Design implications`

`Design implications` is auto-updated by the ingestion script between markers:

- `<!-- AUTO-DESIGN-IMPLICATIONS:START -->`
- `<!-- AUTO-DESIGN-IMPLICATIONS:END -->`

## Ingestion

From repository root:

```bash
python3 evidence/experiments/scripts/build_experiment_indexes.py
```

Outputs regenerated on each run:

- `evidence/experiments/INDEX.md`
- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/conflicts.md`
- `evidence/experiments/promotion_demotion_recommendations.md`
- `evidence/experiments/<experiment_type>/INDEX.md`
- `evidence/experiments/<experiment_type>/experiment.md` (auto section only)
- `evidence/experiments/TODOs.md`
- `evidence/literature/INDEX.md`
- `evidence/decisions/decision_state.v1.json`
- `evidence/planning/evidence_backlog.v1.json`
- `evidence/planning/experiment_proposals.v1.json`

To persist decision outcomes across regenerations, append to:

- `evidence/decisions/decision_log.v1.jsonl`
- with helper: `python3 evidence/experiments/scripts/record_decision.py ...`

## Adding a New Experiment Type

1. Create `evidence/experiments/<experiment_type>/experiment.md` with the required sections.
2. Add run packs under `evidence/experiments/<experiment_type>/runs/<run_id>/`.
3. Add stop rules for that experiment type in `stop_criteria.v1.yaml`.
4. Run the ingestion script.
5. Review generated indexes and TODO queue.

## Stop Criteria Notes

`stop_criteria.v1.yaml` is intentionally JSON-compatible YAML so it can be parsed with Python standard library only.
