# Literature Evidence Interface Contract (v1)

This contract defines the academic-literature artefact format ingested into REE claim evidence.

## Required Directory Shape

```text
evidence/literature/<literature_type>/entries/<entry_id>/
  record.json
  summary.md
```

## File: `record.json`

Required fields:

- `schema_version`: string, must be `"literature_evidence/v1"`.
- `literature_type`: string, must match `<literature_type>` directory.
- `entry_id`: string, must match `<entry_id>` directory.
- `timestamp_utc`: RFC3339 UTC timestamp.
- `claim_ids_tested`: string array of claim IDs.
- `source`: object with required:
  - `title`
  - `authors` (string array)
  - `year` (integer)
  - optional `venue`, `doi`, `url`
- `evidence_class`: string class token (ingestion prefixes with `lit:` in the matrix).
- `evidence_direction`: one of `supports`, `weakens`, `mixed`, `unknown`.
- `confidence`: number in `[0, 1]`.
- `confidence_rationale`: short string describing how confidence was assigned.
- `summary_path`: path to summary file (usually `summary.md`).

Optional fields:

- `failure_signatures`: string array for explicit contradiction signatures.
- `tags`: string array.

## Confidence Guidance

Use confidence as an explicit quality estimate for the extracted claim linkage.

- `0.8-1.0`: strong direct evidence with low ambiguity.
- `0.5-0.79`: moderate support with caveats or indirect mapping.
- `<0.5`: weak/ambiguous mapping or conflicting literature.

## Integration Notes

- Literature entries are merged with experiment entries into `evidence/experiments/claim_evidence.v1.json`.
- Runs/records without `claim_ids_tested` are indexed under `unlinked_runs`.
