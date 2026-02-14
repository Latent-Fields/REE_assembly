# Experiment Pack Interface Contract (v1)

This contract defines what `ree-v1-minimal` must emit for ingestion by `REE_assembly`.

## Required Directory Shape

```text
evidence/experiments/<experiment_type>/runs/<run_id>/
  manifest.json
  metrics.json
  summary.md
  jepa_adapter_signals.v1.json   # optional; required when adapter_signals_path is declared
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
  - optional `adapter_signals_path` (usually `"jepa_adapter_signals.v1.json"`)
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

## File: `jepa_adapter_signals.v1.json` (optional, JEPA-backed runs)

If `manifest.artifacts.adapter_signals_path` is set, this file is required and ingestion validates it.

Schema:

- `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`

Required core fields:

- `schema_version`: `"jepa_adapter_signals/v1"`
- `experiment_type`, `run_id` (must match manifest)
- `adapter.name`, `adapter.version`
- `stream_presence`
  - must include `z_t=true`, `z_hat=true`, `pe_latent=true`, `trace_context_mask_ids=true`
  - includes booleans for `uncertainty_latent`, `trace_action_token`
- `pe_latent_fields`: must contain at least `mean` and `p95`
- `uncertainty_estimator`: one of `none|dispersion|ensemble|head`
- `signal_metrics` with at minimum:
  - `latent_prediction_error_mean`
  - `latent_prediction_error_p95`
  - `latent_residual_coverage_rate` (0..1)
  - `precision_input_completeness_rate` (0..1)
  - plus `latent_uncertainty_calibration_error` if `uncertainty_latent=true`

Optional JEPA control-proxy extension fields (recommended for `MECH-059` / `MECH-060` work):

- `proxy_bank`: array of proxy declarations used by REE control routing. Each item should include:
  - `proxy_id`
  - `source_stream` (`uncertainty_dispersion|ensemble_disagreement|attention_entropy|rollout_inconsistency|action_sensitivity|other`)
  - `extraction_method`
  - `normalization`
  - `window`
  - `calibration_target` (`latent_residual|commitment_reversal|attribution_gain|other`)
  - `provenance`
- `signal_metrics` optional additions:
  - `proxy_bank_coverage_rate` (0..1)
  - `proxy_confidence_calibration_ece` (>=0)
  - `proxy_residual_correlation_abs` (0..1)
  - `proxy_ablation_control_delta` (signed delta; positive indicates control utility gain)

Conditional validation:

- if `proxy_bank` is present and non-empty, `signal_metrics` must include:
  - `proxy_bank_coverage_rate`
  - `proxy_confidence_calibration_ece`
  - `proxy_residual_correlation_abs`

Validation behavior:

- Missing/invalid adapter file is marked as run failure in generated indexes.
- Failure signature is added as `contract:jepa_adapter_signals_*`.

## Stop Criteria Interaction

Ingestion computes FAIL from both:

- `manifest.status`
- threshold checks in `stop_criteria.v1.yaml`

If either indicates failure, run is indexed as FAIL.

## Claim-Evidence Matrix Population

Ingestion generates `claim_evidence.v1.json` by reading run-level linkage fields and merging with literature records:

- `claim_ids_tested` (required for claim linkage)
- `evidence_class`
- `evidence_direction` (if omitted, ingestion infers direction from PASS/FAIL)

Experimental classes are represented as `exp:*` in the matrix.
Literature records are represented as `lit:*` classes from `evidence/literature`.
The matrix includes confidence channels:

- `experimental_confidence`
- `literature_confidence`
- `overall_confidence`

Runs without `claim_ids_tested` are still indexed but tracked under `unlinked_runs` in the matrix.

## Stability Guarantees for Producers

- `schema_version` values are versioned and immutable.
- New major changes require new schema versions.
- `v1` ingestion assumes JSON-compatible UTF-8 files.
