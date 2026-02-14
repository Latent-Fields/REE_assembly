# JEPA as E1/E2 Integration Contract

**Claim Type:** implementation_note  
**Scope:** Interface contract for using JEPA-family world models as REE E1/E2 substrate  
**Depends On:** IMPL-020, IMPL-021, ARC-001, ARC-002, ARC-005, ARC-015, MECH-057  
**Status:** stable  
**Claim ID:** IMPL-022
<a id="impl-022"></a>

---

## Purpose

Specify how JEPA-family models can be integrated into REE as:

- `E1` deep predictive substrate (slow, coherence-preserving latent structure),
- `E2` fast predictive substrate (short-horizon transition prediction).

This contract isolates the substrate boundary so control-completion behavior remains explicit REE scope.

---

## Integration Boundary

JEPA side provides:

- latent state encoding,
- latent future prediction,
- optional action-conditioned latent dynamics.

REE side retains ownership of:

- commitment gating (`E3`),
- control-plane arbitration and precision routing,
- responsibility attribution/efference-reafference learning,
- residue and viability constraints.

---

## Required Interface Surfaces

### Inputs into JEPA substrate

- `obs_t`: current observation slice.
- `ctx_{t-k:t}`: context window (optional memory-conditioned input).
- `a_t` (optional): candidate action token/vector for action-conditioned predictions.
- `mode_tags` (optional): REE regime hints (`deliberative`, `reactive`, `reflective`) for evaluation-only stratification.

### Outputs from JEPA substrate

- `z_t`: latent representation for current context.
- `z_hat_{t+1:t+h}`: predicted latent futures for horizon `h`.
- `pe_latent`: latent prediction deviation statistics (`L-state deviation`).
- `uncertainty_latent` (optional): calibrated uncertainty/dispersion estimate over latent predictions.

### JEPA-native signal map (adapter contract)

The adapter must map native JEPA training/runtime streams onto stable REE-facing keys:

| REE contract key | JEPA-native stream | Extraction rule | Status |
| --- | --- | --- | --- |
| `z_t` | encoder/target-encoder latent tokens | export post-normalization latent for the active context window | direct |
| `z_hat_{t+1:t+h}` | predictor output tokens | export predictor outputs aligned to masked target blocks and rollout step index | direct |
| `pe_latent.mean` | latent prediction loss | compute mean latent distance from `z_hat` to target latent (`smooth_l1`/equivalent) | direct |
| `pe_latent.p95` | latent prediction residuals | compute p95 over per-token latent residuals before global reduction | derived |
| `pe_latent.by_mask` | masked block residuals | emit per-target-mask residual mean keyed by mask id | derived |
| `uncertainty_latent.dispersion` | multi-target/multi-step latent spread | estimate dispersion across equivalent target predictions (same context, multiple masks/seeds) | derived |
| `uncertainty_latent.calibration_error` | predicted uncertainty vs realized residual | expected calibration error between uncertainty estimate and realized `pe_latent` bins | derived |
| `trace.context_mask_ids` | mask sampler outputs | emit exact context/target mask ids used for each prediction | direct |
| `trace.action_token` (if action-conditioned) | action-conditioned predictor input | emit action token/vector hash + schema id for each rollout step | direct |

Notes:

- `pe_latent` is already explicit in canonical JEPA implementations.
- `uncertainty_latent` is partially implicit in canonical JEPA and must be adapter-derived unless the producer exposes a dedicated uncertainty head.
- `precision_latent` is not guaranteed as an explicit calibrated JEPA output channel. The adapter may export internal precision proxies (for example, dispersion, ensemble disagreement, attention entropy, or action sensitivity) with provenance metadata; REE control-plane logic must compose the final confidence channel (uncertainty-derived precision).
- Machine-readable adapter declaration for experiment packs: `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`.

### JEPA↔REE control signal mapping matrix (execution contract)

This table defines ownership and gating for control-plane-relevant channels when JEPA backs E1/E2.

| REE control function | REE-facing channel | JEPA source class | JEPA extraction examples | Final transform owner | Required checks | Canonical failure signatures |
| --- | --- | --- | --- | --- | --- | --- |
| Substrate mismatch feed (`MECH-058`) | `pe_latent` | explicit/derived | `smooth_l1` residual, `p95`, `by_mask` | REE consumes; adapter exports only | `latent_residual_coverage_rate >= 0.95` | `contract:jepa_residual_stream_missing`, `mech058:timescale_separation_collapse` |
| Confidence-channel synthesis (`MECH-059`) | `confidence_channel` | derived proxy bank | `uncertainty_latent.dispersion`, ensemble disagreement, attention entropy, rollout inconsistency, action sensitivity | REE control plane only | calibration, separability, and completeness checks | `mech059:calibration_slope_break`, `mech059:uncertainty_metric_gaming_detected`, `mech059:abstention_reliability_collapse` |
| Pre-commit planning signal (`MECH-060`) | `pre_commit_error` | hybrid | `pe_latent` + hypothetical action-conditioned rollout deltas | REE control plane only | `pre_commit_error_signal_to_noise` and leakage checks | `mech060:precommit_channel_contamination` |
| Post-commit attribution signal (`MECH-060`) | `post_commit_error` | hybrid | realized residuals + reafference delta + action trace | REE attribution path | `post_commit_error_attribution_gain` and attribution reliability checks | `mech060:postcommit_channel_contamination`, `mech060:attribution_reliability_break` |
| Trajectory-first control support (`MECH-056`) | `trajectory_candidate_risk` | derived | rollout consistency + commitment reversal diagnostics | REE commitment layer | trajectory-first checks under ablation | `mech056:trajectory_order_violation` |
| Channel-isolation guard (`MECH-060`) | `cross_channel_leakage_rate` | REE diagnostic | control-plane leakage estimator across pre/post channels | REE control plane only | `cross_channel_leakage_rate <= threshold` | `mech060:cross_channel_leakage_spike` |

### Proxy bank declaration (adapter to control handoff)

When JEPA-backed control routing is enabled, the adapter should export `proxy_bank` declarations for each active
internal proxy used by REE confidence/channel logic. Each proxy entry should include:

- `proxy_id`: stable key (`uncertainty_dispersion`, `ensemble_disagreement`, `attention_entropy`, `rollout_inconsistency`, `action_sensitivity`, `other`)
- `source_stream`: source family (`uncertainty_dispersion`/`ensemble_disagreement`/`attention_entropy`/`rollout_inconsistency`/`action_sensitivity`/`other`)
- `extraction_method`: short deterministic description of how the proxy is computed
- `normalization`: scaling/bounding transform
- `window`: temporal/statistical window used
- `calibration_target`: what the proxy is calibrated against (`latent_residual`, `commitment_reversal`, `attribution_gain`, `other`)
- `provenance`: adapter-internal source pointer (module name, tensor path, or equivalent)

### Contract invariants

- Output latents must remain numerically stable under repeated rollout calls.
- Prediction deviation keys must be fixed-name numeric fields across runs.
- JEPA outputs must not directly commit actions; they are advisory inputs to REE control.
- JEPA adapters may emit proxy signals, but must not emit final control-plane decisions or commitment actions.

---

## Mapping Rules

1. `z_t` feeds REE `L-space` ingest path.
2. Multi-step `z_hat` feeds `E2` short-horizon prediction interfaces and hippocampal rollout seeding.
3. `pe_latent` feeds REE prediction-error routing (precision/eligibility inputs), not direct policy rewrite.
4. Any action-conditioned JEPA output is treated as hypothetical until E3 commitment.
5. Internal JEPA proxies are valid control inputs only after explicit REE-side calibration and attribution-safe routing.

### Signed PE and precision routing bridge

To keep substrate/control separation explicit:

- JEPA adapter emits unsigned latent deviation and uncertainty streams only.
- REE computes signed decomposition downstream (for example, harm/benefit directional channels) using claim-owned control-plane rules.
- Precision routing consumes `pe_latent` + the confidence channel (derived from calibrated proxy bank inputs such as `uncertainty_latent`) + context tags; it is not learned implicitly inside the JEPA adapter.

Practical interpretation:

- JEPA gives the mismatch stream (`what was wrong`) and can expose dispersion (`how many futures looked plausible`).
- REE converts that into a confidence channel (uncertainty-derived precision: `how strongly to trust this error for control`) with explicit, auditable transforms.

---

## Required Knobs (Config Contract)

The substrate adapter must expose, at minimum:

- `latent_dim`
- `prediction_horizon`
- `context_window`
- `action_conditioned` (bool)
- `uncertainty_head` (bool)
- `update_rate_e1_proxy` (slow path)
- `update_rate_e2_proxy` (fast path)
- `residual_export_mode` (`global_only` | `per_mask` | `per_token`)
- `uncertainty_estimator` (`none` | `dispersion` | `ensemble` | `head`)

REE-side control knobs remain out-of-scope for JEPA substrate and must be separately configured in control-plane docs.

---

## Evaluation Contract

### Required metrics (stable keys)

- `latent_prediction_error_mean`
- `latent_prediction_error_p95`
- `latent_rollout_consistency_rate`
- `latent_uncertainty_calibration_error` (if uncertainty head present)
- `action_conditioned_delta_error` (if action-conditioned enabled)
- `latent_residual_coverage_rate` (fraction of predictions with exported residual trace)
- `precision_input_completeness_rate` (fraction of steps with all required PE/uncertainty fields)

### Additional required metrics (JEPA control-proxy routing profiles)

- `proxy_bank_coverage_rate` (fraction of steps with declared proxy provenance)
- `proxy_confidence_calibration_ece` (confidence-channel calibration error from proxy-driven confidence)
- `proxy_residual_correlation_abs` (absolute correlation between confidence channel and raw residual magnitude)
- `proxy_ablation_control_delta` (control quality delta when proxy bank is disabled vs enabled)

### Required checks

- separation check: E1-proxy updates are slower than E2-proxy updates;
- no direct commitment check: substrate outputs cannot bypass E3;
- attribution readiness check: outputs contain enough trace context for reafference comparison.
- uncertainty provenance check: every uncertainty value must declare estimator type (`dispersion`/`ensemble`/`head`);
- signed-PE boundary check: adapter does not emit control-plane valence labels as if they were substrate-native.
- proxy provenance check: every active control proxy has `proxy_bank` declaration fields.
- confidence/residual separability check: confidence channel is not a direct alias of residual magnitude.
- ablation utility check: at least one declared proxy improves control/attribution behavior under matched seeds.

---

## Failure Modes and Handling

- **FM-INT-001: Latent shortcut lock-in**  
  Symptom: low training error with poor transfer under intervention shifts.  
  Handling: adversarial environment variants + counterfactual action sweeps.

- **FM-INT-002: Substrate overreach into control**  
  Symptom: adapter performs implicit action selection before E3.  
  Handling: strict interface check that adapter emits predictions only.

- **FM-INT-003: Timescale collapse**  
  Symptom: E1 and E2 update channels become indistinguishable.  
  Handling: enforce update-rate ratio thresholds and reject runs failing separation.

- **FM-INT-004: Responsibility-blind predictions**  
  Symptom: no usable attribution deltas for self-impact loops.  
  Handling: require action-conditioned traces and reafference comparison hooks in output pack.

---

## Evidence Routing

Primary claim linkage:

- `MECH-057` (control-completion requirement)
- `Q-012` (falsifiability of control necessity)

Evidence should be recorded via:

- literature: `evidence/literature/targeted_review_mech_057/**`
- experiments: `evidence/experiments/claim_evidence.v1.json`

---

## Acceptance Gate for Adoption

Adopt JEPA substrate as REE default E1/E2 backend only when all conditions hold:

- literature support for substrate adequacy remains net-positive,
- experimental runs pass interface checks and stable-key metric checks,
- no unresolved evidence that substrate bypasses REE commitment/control ownership,
- governance queue has explicit approval for adoption decision.

---

## Related Claims (IDs)

- IMPL-022
- IMPL-021
- IMPL-020
- MECH-057
- Q-012
- ARC-001
- ARC-002
- ARC-005
- ARC-015

---

## Primary Source Anchors

The following source families were used to define the signal contract:

- I-JEPA paper (predictor over masked target representations): [arXiv:2301.08243](https://arxiv.org/abs/2301.08243)
- V-JEPA/V-JEPA2 methodology (mask-denoising in latent space, L1-style latent regression, action-conditioned autoregressive world model): [arXiv:2506.09985](https://arxiv.org/abs/2506.09985)
- JEPA uncertainty extension evidence (latent variables + variance/covariance regularization in non-deterministic futures): [arXiv:2412.10925](https://arxiv.org/abs/2412.10925)
- Reference implementation streams:
  - I-JEPA training loop (`target_encoder` latent targets, predictor outputs, `smooth_l1_loss`): [facebookresearch/ijepa/src/train.py](https://github.com/facebookresearch/ijepa/blob/main/src/train.py)
  - V-JEPA2 pretraining loop (latent prediction loss over masked tokens): [facebookresearch/vjepa2/app/vjepa/train.py](https://github.com/facebookresearch/vjepa2/blob/main/app/vjepa/train.py)
  - V-JEPA2 action-conditioned loop (`jloss` teacher forcing + `sloss` autoregressive rollout): [facebookresearch/vjepa2/app/vjepa_droid/train.py](https://github.com/facebookresearch/vjepa2/blob/main/app/vjepa_droid/train.py)
