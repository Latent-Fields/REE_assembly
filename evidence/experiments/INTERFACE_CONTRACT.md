# Experiment Pack Interface Contract (v1)

This contract defines what `ree-v1-minimal` must emit for ingestion by `REE_assembly`.

## Required Directory Shape

```text
evidence/experiments/<experiment_type>/runs/<run_id>/
  manifest.json
  metrics.json
  summary.md
  traces/               # optional
  media/                # optional
```

## File: `manifest.json`

Required fields:

- `schema_version`: string, must be `"experiment_pack/v1"`.
- `experiment_type`: string, must match `<experiment_type>` directory.
- `run_id`: string, must match `<run_id>` directory.
- `status`: `"PASS"` or `"FAIL"`.
- `timestamp_utc`: RFC3339 UTC timestamp.
- `source_repo`: object with required `name`, `commit`; optional `branch`.
- `runner`: object with required `name`, `version`.
- `artifacts`: object with required:
  - `metrics_path` (usually `"metrics.json"`)
  - `summary_path` (usually `"summary.md"`)
  - optional `traces_dir`, `media_dir`

Optional but recommended:

- `scenario`: object (`name`, `seed`, `config_hash`, etc.)
- `stop_criteria_version`: string, e.g. `"stop_criteria/v1"`
- `claim_ids_tested`: string array of REE claim IDs, e.g. `["MECH-056", "Q-011"]`
- `evidence_class`: string, e.g. `"simulation"`, `"behavioral"`, `"control_theory"`
- `evidence_direction`: one of `"supports"`, `"weakens"`, `"mixed"`, `"unknown"`
- `failure_signatures`: string array, stable signature IDs

## File: `metrics.json`

Required shape:

- `schema_version`: string, must be `"experiment_pack_metrics/v1"`
- `values`: object
  - keys: stable metric IDs (snake_case)
  - values: numbers only (`int`/`float`)

Rules:

- No strings/booleans/null in `values`.
- Keep metric keys stable across runs for delta computation.
- Add new metrics additively; avoid renaming existing keys.

## File: `summary.md`

Human-readable run summary. Should include:

- scenario/config
- notable outcomes
- interpretation notes

No strict schema, but file must exist.

## Stop Criteria Interaction

Ingestion computes FAIL from both:

- `manifest.status`
- threshold checks in `stop_criteria.v1.yaml`

If either indicates failure, run is indexed as FAIL.

## Claim-Evidence Matrix Population

Ingestion generates `claim_evidence.v1.json` by reading run-level linkage fields:

- `claim_ids_tested` (required for claim linkage)
- `evidence_class`
- `evidence_direction` (if omitted, ingestion infers direction from PASS/FAIL)

Runs without `claim_ids_tested` are still indexed but tracked under `unlinked_runs` in the matrix.

## Stability Guarantees for Producers

- `schema_version` values are versioned and immutable.
- New major changes require new schema versions.
- `v1` ingestion assumes JSON-compatible UTF-8 files.
