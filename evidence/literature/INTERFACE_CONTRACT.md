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
  - optional `venue`
  - optional **stable external identifiers**: `doi`, `pmid`, `pmc`, `arxiv_id`, `isbn`, `url`.
    Record every identifier you actually resolved -- for a biomedical source `pmid` is the primary
    verification handle and should be present. Any of these may be `null`, which means "checked,
    none exists"; that is more informative than omitting the key.
  - optional **in-publication locators**: `volume`, `issue` (string or integer), `pages` (string).

  `source` is closed (`additionalProperties: false`). Two things deliberately do NOT go in it:
  - a **denormalised rendering** of fields already declared separately -- do not add a formatted
    `citation` string or a merged `volume_pages`; put the parts in `venue`/`volume`/`issue`/`pages`.
  - **prose** -- provenance notes, metadata corrections, retrieval caveats, code/data availability.
    These belong in the entry's `summary.md`, which is the dominant corpus convention.

  `pmcid` is a deprecated spelling of `pmc`, still accepted so existing entries validate. Use `pmc`.
- `evidence_class`: string class token (ingestion prefixes with `lit:` in the matrix).
- `evidence_direction`: one of `supports`, `weakens`, `mixed`, `unknown`.
- `confidence`: number in `[0, 1]`.
- `confidence_rationale`: short string describing how confidence was assigned.
- `summary_path`: path to summary file (usually `summary.md`).

Optional fields:

- `failure_signatures`: string array for explicit contradiction signatures.
- `tags`: string array.
- `mapping`: object for source-to-REE translation details:
  - `source_claim_statement`: short source-faithful statement of what the paper actually claims.
  - `ree_translation`: REE framing of that source claim.
  - `mapping_caveat`: explicit boundary/risk in the translation.
  - optional `source_context`: short task/species/modality context note.
- `confidence_components`: object for confidence decomposition:
  - `source_quality`: number in `[0, 1]` (method quality / source reliability).
  - `mapping_fidelity`: number in `[0, 1]` (how faithful REE translation is to source wording).
  - `transfer_risk`: number in `[0, 1]` (risk that domain transfer to REE is invalid).
  - optional `notes`: short calibration note.

## Confidence Guidance

Use confidence as an explicit quality estimate for the extracted claim linkage.

- `0.8-1.0`: strong direct evidence with low ambiguity.
- `0.5-0.79`: moderate support with caveats or indirect mapping.
- `<0.5`: weak/ambiguous mapping or conflicting literature.

When `confidence_components` is present, `confidence` should reflect a reasoned aggregate of these components and
the rationale should explain the aggregation choice.

## Connectome Pull Guidance

For connectome/effective-connectivity pulls:

- preserve source wording in `mapping.source_claim_statement`,
- provide REE interpretation in `mapping.ree_translation`,
- keep explicit transfer limits in `mapping.mapping_caveat`,
- include `confidence_components` to separate source quality from mapping confidence.

## Integration Notes

- Literature entries are merged with experiment entries into `evidence/experiments/claim_evidence.v1.json`.
- Runs/records without `claim_ids_tested` are indexed under `unlinked_runs`.
