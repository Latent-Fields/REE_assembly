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
- `producer_capabilities`: object map of capability flag -> boolean, used for capability-gated dispatch routing.
- `environment`: object for environment qualification and drift tracking.
  Recommended keys:
  - `env_id`: stable environment identifier
  - `env_version`: semantic/commit environment version
  - `dynamics_hash`: hash of transition/dynamics definition
  - `reward_hash`: hash of reward/harm shaping definition
  - `observation_hash`: hash of observation/sensor interface definition
  - `config_hash`: hash of environment config bundle
  - `tier`: e.g. `"toy"`, `"stress"`, `"ablation"`

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

## Claim-Specific Dispatch Extension: `MECH-056`

When a dispatched run includes `MECH-056` in `claim_ids_tested`, producers (including `ree-v1-minimal`) should emit these
additional metrics by default:

- `trajectory_commit_channel_usage_count`
- `perceptual_sampling_channel_usage_count`
- `structural_consolidation_channel_usage_count`
- `precommit_semantic_overwrite_events`
- `structural_bias_magnitude`
- `structural_bias_rate`

Expected summary additions for `MECH-056` runs:

- Channel escalation order observed (`trajectory_commit -> perceptual_sampling -> structural_consolidation` when triggered).
- Trigger rationale for each non-primary channel activation.

Expected capability flags for `MECH-056` producer qualification:

- `trajectory_integrity_channelized_bias`
- `mech056_dispatch_metric_set`
- `mech056_summary_escalation_trace`

Environment dispatch expectation for `MECH-056` (high-priority adjudication):

- Include at least `toy` and `stress` tiers across the run set.
- Keep environment hashes stable within a series so drift analysis compares like-for-like runs.

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
