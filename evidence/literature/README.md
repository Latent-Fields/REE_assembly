# Literature Evidence Subsystem

This folder stores structured academic-literature evidence that can be merged with experimental evidence in
`evidence/experiments/claim_evidence.v1.json`.

## Purpose

- Keep literature-derived evidence separate from experiment-run evidence.
- Attach explicit confidence values to literature claims.
- Feed the same conflict and promotion/demotion decision pipeline used for experiments.

## Folder Layout

- `INTERFACE_CONTRACT.md`: producer contract for literature evidence records.
- `schemas/v1/literature_evidence.schema.json`: reference schema for `record.json`.
- `<literature_type>/entries/<entry_id>/record.json`: machine-readable evidence record.
- `<literature_type>/entries/<entry_id>/summary.md`: human summary.
- `INDEX.md`: generated index (do not hand edit).

## Ingestion

Literature evidence is ingested by:

```bash
python3 evidence/experiments/scripts/build_experiment_indexes.py
```

The script scans `evidence/literature/**/entries/**/record.json`.
