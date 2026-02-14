# REE-v2 Substrate Spec

**Claim Type:** implementation_note  
**Scope:** v2 substrate-first architecture and implementation contract  
**Depends On:** IMPL-008, IMPL-021, IMPL-022, IMPL-025, MECH-057, MECH-058, MECH-059, MECH-060  
**Status:** candidate  
**Claim ID:** IMPL-023
<a id="impl-023"></a>

---

## Purpose

Define a concrete, buildable target for REE-v2:
- JEPA-aligned sensing + E1/E2 substrate first,
- explicit interface hooks for later control completion (hippocampal, control-plane, E3).

This document is intentionally implementation-oriented and keeps philosophy out of scope.

v2 is the phase where substrate behavior becomes reliable enough that v3 can focus on control completion rather than
fighting unstable representation plumbing.

---

## Terminology Mode (v2)

v2 uses JEPA-first language with inline REE translation for user-facing docs and interactions.

- First mention format: `JEPA term (REE term)`.
- Substrate sections default to JEPA wording.
- Control/commitment sections default to REE wording.
- Contract keys remain stable REE ingestion keys (no schema churn from terminology changes).

Reference policy:
- `docs/notes/jepa_language_policy.md#impl-024`

---

## v2 Architectural Boundary

## In scope (v2)

- Sensory adapter contract from environment observations to latent substrate inputs.
- JEPA-aligned latent representation/prediction substrate for E1/E2.
- Stable output streams for:
  - latent state (`z_t`),
  - predicted latent futures (`z_hat`),
  - latent prediction error (`pe_latent`),
  - latent uncertainty/dispersion (`uncertainty_latent` when available).
- Experiment Pack + adapter-signal contract compliance.

## Out of scope (v2)

- Final control-plane arbitration policy.
- Final hippocampal replay/planning controller.
- Final E3 commitment policy and full responsibility accounting.

These become v3 primary implementation scope.

---

## Implementation Objectives

- `OBJ-V2-001`: stable latent substrate outputs under repeated runs and seed variation.
- `OBJ-V2-002`: explicit uncertainty/error channels with measurable calibration.
- `OBJ-V2-003`: strict experiment-pack and adapter-signal contract compliance.
- `OBJ-V2-004`: expose v3-ready hooks without embedding v3 policy decisions.

---

## Reference Module Layout

v2 should be implemented as the following modules (names are descriptive, not mandatory file names):

1. `sensor_adapter` (JEPA context/target adapter, REE sensory ingress)
- normalize observation streams,
- build context/target slices,
- emit adapter metadata hashes for reproducibility.

2. `latent_substrate` (JEPA substrate core, REE E1/E2 substrate path)
- context encoder,
- target encoder (slow anchor / EMA path),
- latent predictor (fast transition path).

3. `latent_signal_exporter` (contract output layer)
- emit stable keys: `z_t`, `z_hat`, `pe_latent`, optional `uncertainty_latent`,
- emit trace metadata required by adapter-signal schema.

4. `pack_emitter` (evidence boundary)
- write `manifest.json`, `metrics.json`, `summary.md`,
- write `jepa_adapter_signals.v1.json` when adapter path is declared.

5. `hook_surface_adapter` (forward-compatibility interface)
- emit placeholders for pre-commit and post-commit channels,
- emit trajectory candidate IDs and attribution trace IDs.

---

## Required Interfaces

v2 must implement `IMPL-022` surfaces with stable keys:

- Inputs:
  - `obs_t`
  - `ctx_{t-k:t}`
  - optional `a_t`
- Outputs:
  - `z_t`
  - `z_hat_{t+1:t+h}`
  - `pe_latent`
  - optional `uncertainty_latent`

Adapter-signal declaration:
- `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`

Experiment pack declaration:
- `evidence/experiments/INTERFACE_CONTRACT.md`

Hook contract declaration:
- `docs/architecture/hook_surface_contract.md#impl-025`
- `docs/architecture/hook_registry.v1.json`

---

## Interface Detail (Proposed Shape)

Runtime ingress record (conceptual):
- `obs_t`: current observation payload
- `ctx_window`: ordered context frames/states
- `action_token` (optional)
- `run_tags`: mode and scenario tags

Runtime egress record (conceptual):
- `z_t`: current latent state tensor/vector
- `z_hat`: predicted latent futures by horizon step
- `pe_latent`:
  - `mean`
  - `p95`
  - optional `by_mask`
- `uncertainty_latent` (optional):
  - `dispersion`
  - optional `calibration_error`

All production evidence must be exportable into current stable schema keys.

---

## Configuration Contract (v2)

Required configurable parameters:

- `latent_dim`
- `context_window`
- `prediction_horizon`
- `action_conditioned` (bool)
- `uncertainty_estimator` (`none|dispersion|ensemble|head`)
- `ema_decay` (for target-anchor path)
- `update_rate_e1_proxy`
- `update_rate_e2_proxy`
- `residual_export_mode` (`global_only|per_mask|per_token`)

Required reproducibility metadata in emitted manifests:

- scenario id/name and seed,
- config hash,
- environment hash set (`env_id`, `env_version`, `dynamics_hash`, `reward_hash`, `observation_hash`),
- source repo commit.

---

## v2 Required Metrics

Minimum stable metrics across runs:

- `latent_prediction_error_mean`
- `latent_prediction_error_p95`
- `latent_rollout_consistency_rate`
- `latent_residual_coverage_rate`
- `precision_input_completeness_rate`
- `latent_uncertainty_calibration_error` (if uncertainty stream present)

Mechanism-targeted metrics:

- `e1_e2_timescale_separation_ratio` (`MECH-058`)
- `uncertainty_coverage_rate` (`MECH-059`)
- `cross_channel_leakage_rate` (`MECH-060`, provisional hook for v3)

---

## Qualification Profiles (Required)

v2 must maintain explicit experiment profiles for:

1. `jepa_anchor_ablation` (`MECH-058`)
- compare anchor-on vs anchor-off conditions,
- verify timescale separation and drift suppression.

2. `jepa_uncertainty_channels` (`MECH-059`)
- compare deterministic+dispersion vs explicit uncertainty head,
- verify calibration and precision-input completeness.

3. `commit_dual_error_channels` (`MECH-060`, hook-level in v2)
- compare single-stream vs pre/post split-stream instrumentation,
- verify leakage and attribution-readiness signals.

Each profile must run in:
- qualification lane (`ree-v2`; transitional fallback `ree-v1-minimal` until `ree-v2` is online),
- stress lane (`ree-experiments-lab`).

---

## v2 Failure Gates

The following are hard-fail conditions for v2 readiness:

- Adapter contract drift or missing required signal declaration.
- Timescale-collapse signatures (E1/E2 separation fails repeatedly).
- Uncertainty stream unavailable or uncalibrated where required by experiment profile.
- Residual/precision input completeness below configured threshold.

Initial readiness thresholds (tunable, but explicit):

- `latent_residual_coverage_rate >= 0.95`
- `precision_input_completeness_rate >= 0.95`
- `e1_e2_timescale_separation_ratio >= 1.5` in qualification lane
- no unresolved adapter-contract failures across two consecutive governance cycles
- stress-lane conflict ratio for core v2 claims trending downward across two consecutive cycles

---

## Milestones

`M0` Contract-hardening baseline
- adapter-signal and experiment-pack validation green in both producer repos.

`M1` Stable substrate training/inference loop
- all required interface outputs present,
- core metrics emitted with stable names.

`M2` Uncertainty and calibration lane
- uncertainty estimator variants compared and documented,
- calibration metrics incorporated into promotion/demotion flow.

`M3` v3-hook export
- pre/post channel placeholders and attribution trace IDs exported consistently.

`M4` v2 stabilization gate
- two clean governance cycles with no major contract churn,
- decision to spin dedicated `ree-v2` implementation repo.

---

## Cross-Version Hooks Required in v2

v2 must adopt the cross-version hook framework (`IMPL-025`) and expose all `v2_required` hooks listed in:

- `docs/architecture/hook_registry.v1.json`

v2 should also emit stubs for `v3_planned` hooks where feasible:

- pre-commit simulation error stream placeholder,
- post-commit realized error stream placeholder,
- commitment-context trace IDs for attribution,
- rollout-candidate metadata for hippocampal/controller attachment.

These hooks are interface commitments, not full behavior commitments for the future layers.

---

## Acceptance Checklist (Go/No-Go for v2 Completion)

- All v2 required interfaces implemented and exported.
- All required metrics emitted in contract-compliant packs.
- No unresolved contract-drift failures.
- Core v2 mechanism claims (`MECH-058/059/060`) have active evidence with documented conflict handling.
- Governance output recommends moving implementation focus to v3 control completion.

---

## Repository Strategy for v2

Current recommendation:
- keep v2 spec and contract evolution in `REE_assembly`,
- use `ree-v2` as the primary qualification lane for v2 profiles,
- use `ree-experiments-lab` for stress falsification,
- keep `ree-v1-minimal` as a legacy baseline/reference harness, not the primary v2 qualification lane.

Stabilization gate:
- two consecutive governance cycles with no major contract churn in adapter signals and pack schema.

Suggested `ree-v2` bootstrap timing:
- bootstrap now from this spec + current contracts,
- promote `ree-v2` to required qualification lane once core profiles are runnable,
- retire `ree-v1-minimal` from primary qualification status after parity checks pass.

---

## Open Questions

- Which uncertainty estimator class (`dispersion`, `ensemble`, `head`) should be default in v2?
- What threshold values should gate v2 readiness without overfitting to current harnesses?
- How much of dual pre/post commit channeling should be stubbed vs implemented in late v2?

## Related Claims (IDs)

- IMPL-023
- IMPL-008
- IMPL-021
- IMPL-022
- IMPL-025
- MECH-057
- MECH-058
- MECH-059
- MECH-060
