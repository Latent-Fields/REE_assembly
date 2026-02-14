# REE-v2 Substrate Spec (Draft)

**Claim Type:** implementation_note  
**Scope:** v2 substrate-first architecture and implementation contract  
**Depends On:** IMPL-008, IMPL-021, IMPL-022, MECH-057, MECH-058, MECH-059, MECH-060  
**Status:** candidate  
**Claim ID:** IMPL-023
<a id="impl-023"></a>

---

## Purpose

Define a concrete, buildable target for REE-v2:
- JEPA-aligned sensing + E1/E2 substrate first,
- explicit interface hooks for later control completion (hippocampal, control-plane, E3).

This document is intentionally implementation-oriented and keeps philosophy out of scope.

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

## v2 Failure Gates

The following are hard-fail conditions for v2 readiness:

- Adapter contract drift or missing required signal declaration.
- Timescale-collapse signatures (E1/E2 separation fails repeatedly).
- Uncertainty stream unavailable or uncalibrated where required by experiment profile.
- Residual/precision input completeness below configured threshold.

---

## v3 Hooks Required in v2

v2 must expose explicit hooks for later v3 modules:

- pre-commit simulation error stream placeholder,
- post-commit realized error stream placeholder,
- commitment-context trace IDs for attribution,
- rollout-candidate metadata for hippocampal/controller attachment.

These hooks are interface commitments, not full v2 behavior commitments.

---

## Repository Strategy for v2

Current recommendation:
- keep v2 spec and contract evolution in `REE_assembly`,
- use `ree-v1-minimal` for qualification and `ree-experiments-lab` for stress falsification,
- create dedicated `ree-v2` implementation repo only after interface stabilization.

Stabilization gate:
- two consecutive governance cycles with no major contract churn in adapter signals and pack schema.

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
- MECH-057
- MECH-058
- MECH-059
- MECH-060
