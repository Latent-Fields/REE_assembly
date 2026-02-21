# REE-v2 Repository Bootstrap Spec

**Document Type:** implementation_bootstrap  
**Scope:** New `ree-v2` repository setup for qualification-lane substrate validation  
**Depends On:** IMPL-022, IMPL-023, IMPL-025, IMPL-008, MECH-056, MECH-058, MECH-059, MECH-060  
**Status:** candidate

---

## 1. Purpose and Lane Role

`ree-v2` is the primary **qualification lane** for REE substrate claims and contract-hardening runs.

- Qualification lane owner: `ree-v2`
- Stress/falsification lane owner: `ree-experiments-lab` (unchanged)
- Transitional parity backstop: `ree-v1-minimal` until migration gates are met

This bootstrap spec defines the minimum repository surfaces needed to run claim-bearing qualification experiments that are ingestible by `REE_assembly` without schema or hook drift.

---

## 2. Source Audit Summary (Required v2 Scope)

This section is the direct audit output for:

- `docs/architecture/ree_v2_spec.md`
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `docs/architecture/hook_surface_contract.md`
- `docs/architecture/hook_registry.v1.json`
- `evidence/experiments/INTERFACE_CONTRACT.md`

### 2.1 Scope requirements extracted from source docs

1. `ree-v2` must implement JEPA-based E1/E2 substrate interfaces from `IMPL-022`:
   - inputs: `obs_t`, `ctx_{t-k:t}`, optional `a_t`
   - outputs: `z_t`, `z_hat_{t+1:t+h}`, `pe_latent`, optional `uncertainty_latent`
2. `ree-v2` must emit contract-compliant Experiment Packs:
   - required files: `manifest.json`, `metrics.json`, `summary.md`
   - optional but required when declared: `jepa_adapter_signals.v1.json`
3. `ree-v2` must expose all `v2_required` hooks from `hook_registry.v1.json` (`HK-001..HK-006`).
4. `ree-v2` must keep control completion out of scope:
   - no E3 bypass, no merged pre/post-commit learning semantics
5. v2 qualification profiles are mandatory for:
   - `jepa_anchor_ablation` (`MECH-058`)
   - `jepa_uncertainty_channels` (`MECH-059`)
   - `commit_dual_error_channels` (`MECH-060`, hook-level in v2)
   - `trajectory_integrity` (`MECH-056`, migration parity lane)
6. v2 must enforce explicit calibration and completeness signals:
   - `latent_residual_coverage_rate`
   - `precision_input_completeness_rate`
7. v2 must preserve stable schema keys and version constants (`v1` contracts).
8. v2 must define a JEPA source/provenance lock so substrate code origin is auditable and reproducible.
9. v2 must define explicit local-vs-cloud execution policy; qualification sweeps must not assume local laptop compute.

---

## 3. Minimal Repository Layout

```text
ree-v2/
  README.md
  docs/ops/
    compute_execution_policy.md
    cloud_backend_setup.md
    local_compute_options.md
  contracts/
    hook_registry.v1.json
    schemas/v1/
      manifest.schema.json
      metrics.schema.json
      jepa_adapter_signals.v1.json
    ree_assembly_contract_lock.v1.json
  third_party/
    jepa_sources.lock.v1.json
    patches/
  src/ree_v2/
    sensor_adapter/
      __init__.py
      adapter.py
    latent_substrate/
      __init__.py
      encoder.py
      target_anchor.py
      predictor.py
    signal_export/
      __init__.py
      adapter_signals.py
      metrics_export.py
    hooks/
      __init__.py
      emitter.py
      registry.py
    experiments/
      __init__.py
      profiles.py
      run_context.py
  scripts/
    validate_experiment_pack.py
    validate_hook_surfaces.py
    check_seed_determinism.py
    estimate_run_resources.py
    build_remote_job_spec.py
    submit_remote_job.py
    pull_remote_results.py
  evidence/experiments/
    INTERFACE_CONTRACT.md
    stop_criteria.v1.yaml
  .github/workflows/
    qualification-ci.yml
```

Notes:

- File names are normative for bootstrap consistency; internal module decomposition can expand later.
- `contracts/schemas/v1/*` must be pinned to `REE_assembly` hashes through `contracts/ree_assembly_contract_lock.v1.json`.
- `third_party/jepa_sources.lock.v1.json` is required before non-smoke qualification runs begin.
- `docs/ops/local_compute_options.md` must track upgrade choices for constrained local hardware users.

---

## 4. Required Interface Contracts

## 4.1 Runtime substrate contract (`IMPL-022`)

Ingress keys:

- `obs_t`
- `ctx_window` (maps to `ctx_{t-k:t}`)
- `a_t` (optional)
- `mode_tags` (optional, evaluation stratification only)

Egress keys:

- `z_t`
- `z_hat`
- `pe_latent.mean`
- `pe_latent.p95`
- `pe_latent.by_mask` (required when available)
- `uncertainty_latent.dispersion` (conditional)
- `uncertainty_latent.calibration_error` (required when uncertainty stream is enabled)
- `trace.context_mask_ids`
- `trace.action_token` (conditional for action-conditioned runs)

## 4.2 Experiment Pack contract (`experiment_pack/v1`)

Required artifacts per run:

- `manifest.json`
- `metrics.json`
- `summary.md`

Conditional artifact:

- `jepa_adapter_signals.v1.json` when `manifest.artifacts.adapter_signals_path` is declared.

Required manifest linkage fields:

- `claim_ids_tested`
- `evidence_class`
- `evidence_direction` (`supports|weakens|mixed|unknown`)
- reproducibility context in `scenario` and/or `environment` (`seed`, `config_hash`, hash set)

## 4.3 Hook surface contract (`IMPL-025`, `hook_registry/v1`)

`ree-v2` must emit the following `v2_required` hooks in qualification runs:

| hook_id | hook_name | lifecycle_phase | required key_fields | availability |
| --- | --- | --- | --- | --- |
| `HK-001` | `latent_state_export` | `post_predict` | `z_t` | always |
| `HK-002` | `latent_future_export` | `post_predict` | `z_hat` | always |
| `HK-003` | `latent_prediction_error_export` | `post_predict` | `pe_latent.mean`, `pe_latent.p95` | always |
| `HK-004` | `latent_uncertainty_export` | `post_predict` | `uncertainty_latent.dispersion` | conditional |
| `HK-005` | `context_mask_trace_export` | `post_predict` | `trace.context_mask_ids` | always |
| `HK-006` | `action_token_trace_export` | `post_predict` | `trace.action_token` | conditional |

`ree-v2` must also emit v3-planned stubs with stable IDs and placeholder payloads:

- `HK-101` (`pre_commit_simulation_error_stream`)
- `HK-102` (`post_commit_realized_error_stream`)
- `HK-103` (`commitment_trace_id_export`)
- `HK-104` (`rollout_candidate_metadata_export`)

For v2, stub hooks are allowed to be marked `planned_stub=true` with non-empty ID-bearing payload shells.

## 4.4 JEPA source acquisition and provenance contract

`ree-v2` must choose and document one JEPA source mode:

- `vendored_snapshot` (copied snapshot pinned to upstream commit)
- `submodule_pin` (git submodule pinned to commit)
- `internal_minimal_impl` (local implementation with explicit compatibility statement)

Required lock file:

- `third_party/jepa_sources.lock.v1.json`

Required lock file fields:

- `source_mode`
- `upstream_repo_url` (if external source is used)
- `upstream_commit`
- `license_id`
- `patch_set` (list of local patch IDs/files)
- `compatibility_target` (must reference `IMPL-022`)
- `last_verified_utc`

Run-level provenance requirement:

- `manifest.scenario` must include:
  - `jepa_source_mode`
  - `jepa_source_commit`
  - `jepa_patch_set_hash`

Schema note:

- these provenance fields are recorded under `manifest.scenario` to preserve `manifest.schema.json` compatibility.

---

## 5. Qualification Profiles, Metrics, and Failure Signatures

## 5.1 Required profile coverage

| Claim | Required experiment_type | Required comparison conditions |
| --- | --- | --- |
| `MECH-056` | `trajectory_integrity` | trajectory-first enabled vs ablated |
| `MECH-058` | `jepa_anchor_ablation` | `ema_anchor_on` vs `ema_anchor_off` |
| `MECH-059` | `jepa_uncertainty_channels` | `deterministic_plus_dispersion` vs `explicit_uncertainty_head` |
| `MECH-060` | `commit_dual_error_channels` | `single_error_stream` vs `pre_post_split_streams` |

Minimum seed policy per profile:

- at least 3 distinct seeds per condition in qualification lane
- at least one deterministic replay pair (same seed/config repeated) for CI determinism gate

## 5.2 Required metrics per claim

| Claim | Required stable metric keys |
| --- | --- |
| `MECH-056` | `ledger_edit_detected_count`, `explanation_policy_divergence_rate`, `domination_lock_in_events`, `commitment_reversal_rate` |
| `MECH-058` | `latent_prediction_error_mean`, `latent_prediction_error_p95`, `latent_rollout_consistency_rate`, `e1_e2_timescale_separation_ratio`, `representation_drift_rate` |
| `MECH-059` | `latent_prediction_error_mean`, `latent_uncertainty_calibration_error`, `precision_input_completeness_rate`, `uncertainty_coverage_rate` |
| `MECH-060` | `pre_commit_error_signal_to_noise`, `post_commit_error_attribution_gain`, `cross_channel_leakage_rate`, `commitment_reversal_rate` |

Global v2 readiness thresholds (from current v2 spec):

- `latent_residual_coverage_rate >= 0.95`
- `precision_input_completeness_rate >= 0.95`
- `e1_e2_timescale_separation_ratio >= 1.5` in qualification lane

Terminology standardization note (`MECH-059`):

- Use **confidence channel (uncertainty-derived precision)** for control-plane weighting semantics.
- Keep metric keys unchanged (`latent_uncertainty_calibration_error`, `uncertainty_coverage_rate`) for contract compatibility.

## 5.3 Required failure signatures (emit when triggered)

| Claim | Required signature IDs |
| --- | --- |
| `MECH-056` | `ledger_editing`, `explanation_policy_divergence`, `domination_lock_in` |
| `MECH-058` | `mech058:ema_drift_under_shift`, `mech058:latent_cluster_collapse`, `mech058:anchor_separation_collapse` |
| `MECH-059` | `mech059:calibration_slope_break`, `mech059:uncertainty_metric_gaming_detected`, `mech059:abstention_reliability_collapse` |
| `MECH-060` | `mech060:precommit_channel_contamination`, `mech060:postcommit_channel_contamination`, `mech060:attribution_reliability_break` |

Contract drift signatures from ingestion are also mandatory when applicable:

- `contract:jepa_adapter_signals_missing`
- `contract:jepa_adapter_signals_version`
- `contract:jepa_adapter_signals_invalid`

---

## 6. CI Gates (Bootstrap Mandatory)

`ree-v2` bootstrap CI must fail on any gate violation.

## 6.1 Gate A: schema/contract validation

Required checks:

1. Validate every emitted `manifest.json` against `manifest.schema.json`.
2. Validate every emitted `metrics.json` against `metrics.schema.json`.
3. Validate every declared adapter file against `jepa_adapter_signals.v1.json`.
4. Validate lock-file schema hashes in `contracts/ree_assembly_contract_lock.v1.json`.

Minimum command contract:

```bash
python3 scripts/validate_experiment_pack.py --runs-root evidence/experiments
```

## 6.2 Gate B: deterministic seed replay check

Required checks:

1. For each required profile, replay one `(condition, seed, config_hash)` pair twice.
2. Compare normalized metric vectors and required signal presence keys.
3. Fail if key sets differ or metric deltas exceed tolerance.

Bootstrap tolerance contract:

- strict equality for key sets and stream presence booleans
- numeric metric max absolute delta `<= 1e-6`

Minimum command contract:

```bash
python3 scripts/check_seed_determinism.py --profile all --max-abs-delta 1e-6
```

## 6.3 Gate C: hook surface coverage

Required checks:

1. `HK-001..HK-006` present when availability conditions are satisfied.
2. `key_fields` required by hook registry are present in emitted payloads.
3. `HK-101..HK-104` stubs emitted with stable IDs.

Minimum command contract:

```bash
python3 scripts/validate_hook_surfaces.py --registry contracts/hook_registry.v1.json
```

## 6.4 Gate D: local-vs-cloud execution policy

Baseline local machine profile for bootstrap planning:

- `Apple MacBook Air (M2, 2022)`

Local execution is allowed for:

- schema/hook validation,
- deterministic seed checks on smoke workloads,
- single-seed debug runs expected to complete quickly.

Qualification runs must be offloaded to cloud/remote compute when any trigger is true:

- estimated runtime per run `> 360` minutes (6 hours);
- estimated batch runtime `> 360` minutes (6 hours);
- seed count per condition `> 2`;
- projected memory footprint exceeds safe local budget;
- local thermal throttling or repeated OOM/fatal runtime instability is detected.

Minimum command contract:

```bash
python3 scripts/estimate_run_resources.py --profile all --machine macbook_air_m2_2022
```

The estimator must output `execution_mode=local|remote` per profile/condition.

## 6.5 Gate E: remote execution export/import contract

When `execution_mode=remote`, `ree-v2` must:

1. build provider-agnostic job specs containing:
   - `experiment_type`, `condition`, `seeds`, `config_hash`,
   - source commit + contract lock hash + JEPA source lock hash;
2. submit jobs to configured cloud backend;
3. retrieve result packs unchanged into `evidence/experiments/**/runs/**`;
4. run local pack validation before handoff to `REE_assembly`.

Minimum command contract:

```bash
python3 scripts/build_remote_job_spec.py --profile all
python3 scripts/submit_remote_job.py --job-spec-dir jobs/outgoing
python3 scripts/pull_remote_results.py --job-run-dir jobs/completed --runs-root evidence/experiments
```

If remote credentials are unavailable, CI must support `--dry-run` validation of job-spec generation.

## 6.6 Gate F: local compute options and cost visibility

`ree-v2` must keep an operator-facing local hardware options sheet:

- path: `docs/ops/local_compute_options.md`
- update cadence: at least once every 4 weeks, or immediately when blocked by repeated local capacity limits.

Required content:

1. current local baseline:
   - machine profile (`MacBook Air M2 2022`)
   - observed bottlenecks (`runtime`, `memory`, `thermal`, `disk`)
2. purchase/upgrade options in at least three tiers:
   - low-cost improvement tier
   - mid-cost workstation tier
   - high-cost local acceleration tier
3. each option entry must include:
   - estimated one-time cost (EUR band)
   - expected impact on qualification workloads
   - expected setup complexity and maintenance burden
   - recommendation status (`now`, `later`, `not_recommended`)
4. clear decision trigger thresholds:
   - when to keep using cloud offload only,
   - when local purchase is justified by runtime/cost/time tradeoff.
5. hobby-operator default policy (required baseline unless explicitly overridden):
   - default state: `hold_cloud_only`
   - promote to `upgrade_low` when local friction is increasing but rolling 3-month cloud spend remains below `EUR 80/month`
   - promote to `upgrade_mid` when either:
     - rolling 3-month cloud spend is `>= EUR 100/month`, or
     - local blocked sessions exceed `2 per week` for `3 consecutive weeks`
   - promote to `upgrade_high` only when both are true:
     - rolling 3-month cloud spend is `>= EUR 250/month` for `3 consecutive months`
     - active qualification workload regularly exceeds `10 hours/week`
   - if uncertain, remain in `hold_cloud_only` and reassess next weekly cycle

This gate is documentation-and-decision quality, not benchmark perfection.

---

## 7. Migration Bridge from `ree-v1-minimal`

## 7.1 Migration stages

1. **Stage M-1: JEPA source + compute policy bootstrap**
   - create `third_party/jepa_sources.lock.v1.json` and remote execution policy docs.
   - create initial `docs/ops/local_compute_options.md` with tiered purchase options and trigger thresholds.
   - validate local-vs-remote estimator behavior on all required profiles.
2. **Stage M0: Contract mirror**
   - copy/pin `v1` schemas and create lock file in `ree-v2`.
   - verify pack validation parity against known `ree-v1-minimal` sample packs.
3. **Stage M1: Profile parity**
   - implement `trajectory_integrity`, `jepa_anchor_ablation`, `jepa_uncertainty_channels`, `commit_dual_error_channels` runners in `ree-v2`.
   - preserve experiment_type names and metric keys to avoid ingestion churn.
4. **Stage M2: Dual-lane overlap**
   - run at least one governance cycle with both `ree-v1-minimal` and `ree-v2` qualification packs.
   - compare pass/fail, signatures, and direction deltas by claim.
5. **Stage M3: Qualification cutover**
   - switch default qualification dispatch target from `ree-v1-minimal` to `ree-v2`.
   - keep `ree-v1-minimal` as parity backstop until two consecutive clean cycles.

## 7.2 Cutover acceptance gates

- no unresolved contract drift signatures for `ree-v2` across two consecutive governance cycles
- required hooks and schema checks green in CI
- deterministic seed replay gate green for all required profiles
- local-vs-cloud gate decisions logged and remote export/import path validated
- local compute options sheet present and updated within 4 weeks
- no missing claim coverage for `MECH-056/058/059/060`

---

## 8. Risks and Open Questions (Blocking v2 Start)

Priority order is highest risk first.

1. **P0: uncertainty calibration policy remains unsettled (`Q-013`)**
   - blocker: no finalized decision on deterministic-dispersion vs explicit uncertainty-head default.
   - impact: `MECH-059` qualification outcomes may be non-comparable across runs.
2. **P0: pre/post-commit channel semantics are only stubbed in v2**
   - blocker: `MECH-060` can be qualified only at hook/instrumentation level until v3 control completion.
   - impact: attribution reliability can be measured, but causal learning-policy effects remain partial.
3. **P1: failure-signature namespace inconsistency (`MECH-056` legacy IDs vs prefixed IDs)**
   - blocker: mixed signature naming can fragment conflict tracking.
   - impact: governance reports may under-cluster recurring failures.
4. **P1: migration overlap period can create contradictory direction updates**
   - blocker: simultaneous `ree-v1-minimal` and `ree-v2` qualification outputs may diverge.
   - impact: temporary conflict inflation in `claim_evidence.v1.json`.
5. **P2: hook stub payload expectations for `HK-101..HK-104` are not yet schema-pinned**
   - blocker: planned hooks are defined in registry but payload schemas are still informal.
   - impact: future v3 integration churn risk if stub shape drifts now.
6. **P2: cloud backend operational risk (credentials, quotas, cost control)**
   - blocker: remote execution path can fail if credentials/quotas are not prepared before qualification sweeps.
   - impact: qualification schedule stalls or silently falls back to underpowered local runs.

---

## 9. Non-Goals for Bootstrap

- no refactor of existing `REE_assembly` architecture claims
- no v3 policy implementation inside `ree-v2`
- no schema-version bump beyond current `v1` contract family

---

## 10. Adjacent Lane Note: Agent-Shell Upgrade Path

This v2 bootstrap remains a substrate-qualification lane. A separate agent-shell lane (for example, an "REE-Claw"
bridge) can reuse these contracts with additional requirements:

- typed input/output routing (`OBS`/`INS`/trajectory proposal lanes),
- strict authority-store separation (`POL`/`ID`/`CAPS`) with verifier-gated privileged commits,
- explicit commit tokenization on irreversible tool actions,
- post-commit append-only attribution ledger and replay-safe offline consolidation.

This note clarifies interoperability scope; it does not expand `ree-v2` non-goals.
