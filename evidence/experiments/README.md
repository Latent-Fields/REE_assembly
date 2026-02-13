# Experimental Evidence Subsystem

This folder is the ingestion boundary between implementation experiments (e.g., `ree-v1-minimal`) and REE architecture docs.

## Purpose

- Store machine-readable experiment artefacts in a stable, versioned format.
- Generate indexes that make PASS/FAIL trends visible at a glance.
- Turn repeated failures into concrete design TODOs so experiments drive architecture updates.

## Folder Layout

- `INTERFACE_CONTRACT.md`: strict format contract for producers.
- `stop_criteria.v1.yaml`: versioned stop/fail criteria used by ingestion.
- `schemas/v1/`: JSON schema references for pack files.
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
- optional `traces/`
- optional `media/`

See `INTERFACE_CONTRACT.md` for field-level requirements.

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
- `evidence/experiments/<experiment_type>/INDEX.md`
- `evidence/experiments/<experiment_type>/experiment.md` (auto section only)
- `evidence/experiments/TODOs.md`

## Adding a New Experiment Type

1. Create `evidence/experiments/<experiment_type>/experiment.md` with the required sections.
2. Add run packs under `evidence/experiments/<experiment_type>/runs/<run_id>/`.
3. Add stop rules for that experiment type in `stop_criteria.v1.yaml`.
4. Run the ingestion script.
5. Review generated indexes and TODO queue.

## Stop Criteria Notes

`stop_criteria.v1.yaml` is intentionally JSON-compatible YAML so it can be parsed with Python standard library only.
