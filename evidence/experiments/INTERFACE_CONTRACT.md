# Experiment Pack Interface Contract (v1)

This contract defines what REE experiment substrates must emit for ingestion by `REE_assembly`.

## Required Directory Shape

```text
evidence/experiments/<experiment_type>/runs/<run_id>/
  manifest.json
  metrics.json
  summary.md
  jepa_adapter_signals.v1.json   # optional legacy adapter file; required only when declared
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
  - optional `adapter_signals_path` (legacy adapter runs only)
  - optional `traces_dir`, `media_dir`

Optional but recommended:

- `scenario`: object (`name`, `seed`, `config_hash`, etc.)
- `stop_criteria_version`: string, e.g. `"stop_criteria/v1"`
- `architecture_epoch`: string, e.g. `"ree_hybrid_guardrails_v1"` for epoch-aware applicability tracking
- `claim_ids_tested`: string array of REE claim IDs, e.g. `["MECH-056", "Q-011"]`
- `evidence_class`: string, e.g. `"simulation"`, `"behavioral"`, `"control_theory"`
  - `"synthetic_harness"` (added 2026-09-23, GFLAG-0287): a design-validation result from a synthetic toy world with no REE substrate. Linked to a claim for provenance only; never scored. Such manifests live outside `evidence/experiments/` (currently `evidence/planning/convergence_signal_synthetic_assay_runs/`) so no ingestion path reads them.
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

## File: `jepa_adapter_signals.v1.json` (legacy adapter runs only)

If `manifest.artifacts.adapter_signals_path` is set, this file is required and ingestion validates it.
This is a historical bridge contract for old external-model adapter evidence. It is not the
active REE-native evidence path for V3 revalidation, and it should not be used to validate
MECH-058, MECH-059, or MECH-060.

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

Legacy control-proxy extension fields (historical only, not recommended for current work):

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

Epoch note:

- Producers should stamp `manifest.architecture_epoch` for all new runs aligned to the current REE architecture epoch.

## Stability Guarantees for Producers

- `schema_version` values are versioned and immutable.
- New major changes require new schema versions.
- `v1` ingestion assumes JSON-compatible UTF-8 files.

## Tolerated non-`experiment_pack/v1` packs (allow-list) and stranded-run recovery

**Every `<experiment_type>/runs/<run_id>/manifest.json` MUST carry
`schema_version: "experiment_pack/v1"`, except the 12 packs listed here.** The list is
mirrored verbatim in `evidence/experiments/scripts/recover_stranded_run.py` (`ALLOWLIST`),
and `evidence/experiments/scripts/test_recover_stranded_run.py` asserts the live corpus
against it, so the set cannot grow silently. `recover_stranded_run.py --scan` runs the same
check by hand (exit 3 on a finding).

**Any new pack outside `experiment_pack/v1` is a defect.** In particular, do NOT recover a
stranded run by copying its flat manifest into `runs/<run_id>/manifest.json` ("path 3" in
`evidence/planning/pack_third_writer_path_staged_20260808.md`). Use the tool, which calls the
same `runpack_for_flat` / `build_runpack_docs` the Phase-3 hub writer and `governance.sh` use,
so the pack is byte-identical to a hub materialisation:

```bash
/opt/local/bin/python3 evidence/experiments/scripts/recover_stranded_run.py --dry-run evidence/experiments/<run_id>.json
/opt/local/bin/python3 evidence/experiments/scripts/recover_stranded_run.py evidence/experiments/<run_id>.json
```

It refuses to overwrite an existing pack (a pack is not a pure function of its flat sibling
once `/governance` or `/failure-autopsy` has written to it; use `sync_v3_results.py --heal`
for that) and refuses dry-run smokes and non-V3 flats. Adding an entry to the allow-list is a
reviewed decision recorded with its landing commit, in BOTH the script and this section --
never a way to make the test pass.

Approved by the user 2026-09-16 (options A + C of the planning doc above; option B,
regenerating the path-3 packs, was explicitly NOT chosen because two of them carry hand-curated
corrections). The indexer already tolerates both categories: it reads `status`/`outcome`
and `claim_ids_tested`/`claim_ids`, and every listed run is present in `claim_evidence.v1.json`.
The path-3 packs lack a `metrics.json` sibling, so they get no metric display, stop-criteria
evaluation or duplicate fingerprinting -- a completeness gap, not an evidence loss.

### Path 3 -- verbatim copies of the flat manifest (7; `manifest.json` only)

| `<experiment_type>/runs/<run_id>` | Added by |
|---|---|
| `v3_exq_614_mech341_p3_behavioural_falsifier_3arm/runs/v3_exq_614_mech341_p3_behavioural_falsifier_3arm_20260529T191318Z_v3` | `39664fc7658` 2026-07-30 (admitted `superseded`; hand-curated) |
| `v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260611T224744Z_v3` | `1a4ad27d9ee` 2026-07-20 |
| `v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T005615Z_v3` | `37f1af866f3` 2026-07-30 |
| `v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T010234Z_v3` | `1a4ad27d9ee` 2026-07-20 |
| `v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T033246Z_v3` | `1a4ad27d9ee` 2026-07-20 (arm-degeneracy assertion later hand-corrected, `eabe9c453b`) |
| `v3_exq_707c_arc110_loop_segregation_c2_release_repair/runs/v3_exq_707c_arc110_loop_segregation_c2_release_repair_20260722T041239Z_v3` | `37f1af866f3` 2026-07-30 |
| `v3_exq_899_arc030_mech307_g0_readiness/runs/v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3` | `7141d4c9190` 2026-08-09 (the 7th; landed after the 2026-08-08 count of 6) |

### Pre-schema legacy packs (5; predate the `experiment_pack/v1` projection)

| `<experiment_type>/runs/<run_id>` | Note |
|---|---|
| `v3_exq_241a_sd011_second_source_validation/runs/v3_exq_241a_sd011_second_source_validation_20260408T190019Z_v3` | 2026-04-08, no `schema_version` |
| `v3_exq_241b_sd011_second_source_info_gain/runs/v3_exq_241b_sd011_second_source_info_gain_20260408T231939Z_v3` | 2026-04-08, no `schema_version` |
| `v3_exq_247_sd011_sd012_integration/runs/v3_exq_247_sd011_sd012_integration_20260406T080943Z_v3` | 2026-04-06, no `schema_version` |
| `v3_exq_247_sd011_sd012_integration/runs/v3_exq_247_sd011_sd012_integration_20260407T105051Z_v3` | 2026-04-07, no `schema_version` |
| `v3_exq_628_mech319_simulation_mode_rule_gate_replay_falsifier_evidence/runs/v3_exq_628_mech319_simulation_mode_rule_gate_replay_falsifier_evidence_v3_20260602T191625Z` | 2026-06-02, `schema_version: "v1"`, mis-ordered run_id |

### Synthetic-assay manifests are NOT packs (decided 2026-09-16)

`REE_assembly/scripts/convergence_signal_synthetic_assay_00N.py` (a separate writer found
2026-09-16, post-dating the 2026-08-08 investigation) emits synthetic measurement manifests --
not V3 substrate runs: `claim_ids: []`, `status: synthetic_*_run_only`, no `architecture_epoch`,
no flat sibling. Six of them had been banked on 2026-09-09 under
`evidence/experiments/convergence_signal_synthetic_assay_00N/runs/20260909_seed*/` and were
allow-listed here on 2026-09-16 pending a decision. **Decision (user, 2026-09-16,
`chip-20260916-synthetic-assay-pack-writer`): keep them out of `runs/` entirely.** They now bank
under `evidence/planning/convergence_signal_synthetic_assay_runs/assay_00N/<run>/manifest.json`
(the six existing files moved there, the six stub `INDEX.md`/`experiment.md` dirs removed), each
writer takes `--bank` for that path and refuses an `--out-json` inside an
`evidence/experiments/**/runs/` tree, and the allow-list category is gone. Any evidence attachment
to MECH-558/MECH-559 (open `GFLAG-0287`) is a `/governance` decision that must not route through
`runs/`, which claim scoring reads.
