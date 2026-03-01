# REE-v2 Implementation Spec

**Claim Type:** implementation_note
**Scope:** V2 architecture, subsystem boundaries, SD-001/002/003 resolution, required metrics, failure gates
**Depends On:** IMPL-008, IMPL-021, IMPL-022, IMPL-025, MECH-057, MECH-058, MECH-059, MECH-060, MECH-061, MECH-062, MECH-063
**Status:** candidate
**Claim ID:** IMPL-023
<a id="impl-023"></a>

---

## Revision History

- **Original (pre-2026-02-28):** JEPA-like representation interface spec only. Written before V1
  experimental program. No SD-001/002/003, no HippocampalModule, no CausalGridWorld.
- **Revised 2026-03-01:** Incorporates V1 experimental learning. Adds subsystem separation
  (SD-001), mutual constitution framing (SD-002), self-attribution substrate requirement
  (SD-003), CausalGridWorld environment spec, and implementation step map (Steps 2.0–2.5).
  Step 2.2 representation-interface content retained unchanged under its own section.

---

## Purpose

Define a concrete, buildable target for REE-v2, incorporating everything learned from the V1
experimental program:
- Resolve substrate debts SD-001, SD-002, SD-003 in V2 architecture
- Implement persistent-causal-footprint environment (prerequisite for SD-003 experiments)
- Lock stable representation-interface contract for sensing adapters and E1/E2 latent prediction
- Expose interface hooks for V3 control completion (hippocampal, control-plane, E3)

V2 is the phase where subsystem separation becomes clean, the representation-interface becomes
reliable, and self-attribution becomes experimentally testable — so that V3 can focus on
control completion rather than fighting substrate debt.

Boundary note:
- JEPA is external to REE and is used here as an inspiration/comparison reference only.
- REE-v2 does not require JEPA to be part of the REE architecture graph.

---

## V1 Learning Incorporated

V1 ran 14 experiments (EXQ-000 through EXQ-013). Results: 10 PASS, 4 FAIL.

**PASSes confirm:**
- MECH-059: Control plane precision separation is load-bearing
- MECH-056: Residue trajectory placement is load-bearing
- MECH-061: Commitment boundary token reclassification is load-bearing
- MECH-060/067: Write-locus contamination degrades attribution reliability
- MECH-063: Candidate count is load-bearing (n=32 meaningfully better than n=1)
- MECH-062: Residue routing weight is load-bearing (amnesic baseline degrades)

**FAILs are substrate-limited, not architecture failures:**
- MECH-058 (×2): E1/E2 timescale separation test conflated by SD-001; E2 was doing hippocampal
  work, making E2_FROZEN test "no trajectory proposal" rather than "no transition prediction"
- MECH-057 (×2): Control completion requires multi-step environment with genuine commitment
  pressure; V1 stateless hazard grid cannot surface this

**Substrate debts registered:**
- **SD-001:** E2.generate_candidates_cem() is hippocampal work inside E2. Prevents clean
  mechanistic isolation of E2 as transition model.
- **SD-002:** E1 and E2 are mutually constitutive, not orthogonal. E2 scaffolds E1's
  associative learning; E1 primes E2's predictions. MECH-058 framing incomplete.
- **SD-003:** E2 as self-attribution substrate requires clean isolatability as a pure
  transition model. V1 conflation (SD-001) and stateless environment prevent this.

**V1 saturation:** V1 has reached its qualification limit. Further V1 runs would not add
mechanistic clarity. V2 build proceeds now.

---

## V2 Subsystem Boundaries

### Module map

| Module | Role | V1→V2 change |
|--------|------|--------------|
| `LatentStack` | Multi-timescale latent (γ/β/θ/δ depths), two-pass encode | Unchanged |
| `E1DeepPredictor` | Slow LSTM world model; associative learning; long-horizon prediction; E1 prior for E2 | Unchanged; episode-boundary hidden-state semantics documented |
| `E2FastPredictor` | **Pure** fast transition model: `f(z_t, a_t) → z_{t+1}` | CEM removed; `forward_counterfactual()` added (SD-003) |
| `HippocampalModule` | **New.** Trajectory proposal by navigating residue-weighted affective terrain. CEM refinement loop. | Replaces E2.generate_candidates_cem() (SD-001) |
| `E3TrajectorySelector` | Scores trajectories: J(ζ) = F(ζ) + λ·M(ζ) + ρ·Φ_R(ζ). Selects via precision-gated softmax. | Scoring equation flagged as working hypothesis; requires experimental validation |
| `ResidueField` | Persistent ethical geometry. Accumulates harm. Weights only increase. | Unchanged; architectural note added: may become multi-module input (sensorium gate, hippocampal terrain, E1 conditioning) in V3+ |
| `REEAgent` | Wires all modules; two-timescale training loop | Updated to delegate trajectory proposal to HippocampalModule |
| `CausalGridWorld` | **New.** Grid environment with persistent agent causal footprint, contamination spread, background hazard drift | Replaces stateless V1 GridWorld (SD-003 prerequisite) |

### E2: pure transition model (SD-001 resolution)

E2 is strictly `f(z_t, a_t) → z_{t+1}`. It does not search, plan, or refine trajectories.

**Kept:**
- `predict_next_state(z, a)` — single-step transition with residual connection
- `predict_observation(z)` — observation from latent
- `predict_harm(z, a)` — harm level in [0,1]
- `rollout(z, action_sequence)` — multi-step rollout given a fixed action sequence
- `generate_candidates_random()` — random-shooting baseline for HippocampalModule

**Removed:**
- `generate_candidates_cem()` — this was hippocampal work; moved to HippocampalModule

**Added:**
- `forward_counterfactual(z, a_cf)` — counterfactual query substrate for SD-003.
  Identical in implementation to `predict_next_state` but named distinctly to flag
  its use in attribution experiments:
  ```
  z_actual = e2.predict_next_state(z, a_actual)
  z_cf     = e2.forward_counterfactual(z, a_cf)
  causal_delta = z_actual - z_cf   # agent's causal signature
  ```

### HippocampalModule (SD-001 resolution)

HippocampalModule owns trajectory proposal. It uses E2 only as a forward model.

Architecture:
1. `terrain_prior` MLP: `(z_beta, residue_at_z) → initial action distribution mean`.
   Biases proposals toward low-residue regions of the affective landscape.
2. CEM refinement loop:
   - Sample `num_candidates` action sequences from current distribution
   - Roll each through `e2.rollout()` (E2 as pure forward model)
   - Score each: `harm + 0.5 × residue`
   - Refit distribution mean/std to elite fraction (lowest-scoring)
   - Repeat for `num_cem_iterations`
3. Returns final candidate set to E3 for evaluation

Key design property: E2 is passed in as a dependency and called only for rollouts.
The search strategy, terrain weighting, and elite selection are entirely hippocampal concerns.

V3 note: The terrain_prior is a simple MLP. A more principled design would model the
hippocampus as learning a map of the affective landscape via place-cell-like representations.
This is out of scope for V2.

### E3TrajectorySelector: working hypothesis

The scoring equation J(ζ) = F(ζ) + λ·M(ζ) + ρ·Φ_R(ζ) is a **working hypothesis**, not
a settled canonical formulation. The weights (λ, ρ) are placeholder parameters pending
calibration experiments. The entire scoring function is expected to be redesigned as the
three-gate basal ganglia model and HippocampalModule architecture mature.

Known gaps in V2 E3 implementation:
- F(ζ): implemented as trajectory smoothness + final-state viability score. Actual reality
  constraint mechanism not yet specified.
- M(ζ): does not distinguish agent-caused from environment-caused harm. This requires
  SD-003 self-attribution experiments (Step 2.4).
- Φ_R(ζ): treated as scalar cost term. May become multi-module input in V3+.

### ResidueField: architectural trajectory note

The ResidueField is currently used as a cost term in E3's scoring function and as terrain
input for HippocampalModule. At scale, the residue field (or residue manifold) may be better
understood as an **input to multiple modules** rather than a penalty:

- As attentional prior for a sensorium gate (harm geometry shapes what the system notices)
- As hippocampal terrain (trajectory proposals navigate it)
- As E1 conditioning signal (associative learning weighted by harm history)

This is not a V2 implementation requirement. It is a design consideration to keep live as
the architecture is developed toward V3+.

### CausalGridWorld (SD-003 prerequisite)

The V1 GridWorld was stateless — no persistent agent causal footprint. This meant
agent-caused and environment-caused transitions were indistinguishable, making
self-attribution experiments impossible.

CausalGridWorld provides:
- **Contamination grid:** agent visits spread contamination with configurable rate.
  Contaminated cells can become additional hazards. Contamination persists across steps.
- **Footprint grid:** visit counts per cell, exposing agent's causal history.
- **Background drift:** hazards random-walk independently of the agent on a configurable
  interval, providing environment-caused transitions.
- **Transition type signal:** `info['transition_type']` on each step:
  - `"agent_caused_hazard"` — contamination-triggered harm attributable to prior agent visits
  - `"env_caused_hazard"` — background drift-triggered harm independent of agent action
  - `"resource"` — reward from resource collection
  - `"none"` — no notable transition

This makes agent-caused and environment-caused harm structurally distinct and
experimentally disambiguatable via counterfactual E2 queries.

---

## SD-002: E1/E2 Mutual Constitution (documentation, V2 scope)

E1 and E2 are not parallel systems with orthogonal outputs. They are co-constitutive:

1. **E2 scaffolds E1:** E2's transition sequence is the temporal evidence stream from which
   E1 distills associations. The association "arm-up → throwing" only becomes reliably
   learnable because E2 provides the ordered kinematic chain.

2. **E2→E1 autotrain (V3 work):** E2's forward predictions can generate synthetic temporal
   sequences that E1 learns from, without waiting for ground-truth observations. Not
   implemented in V2; flagged for V3.

3. **E1 primes E2:** E1's associative prior conditions E2's transition predictions.
   Partially implemented in V2: E1 generates a prior that REEAgent computes but does not
   yet wire into HippocampalModule. Full bidirectional loop is Step 2.2 work.

**Implication for MECH-058 results:** The E1_FROZEN and E2_FROZEN conditions in EXQ-002/006
disrupted both directions of the mutual-constitution loop, not just the targeted component.
MECH-058 FAILs should be interpreted at system level, not as evidence that E1/E2 timescale
separation is non-load-bearing. Retesting on V2 substrate (Step 2.1 parity check) with clean
E2 separation may yield different results.

---

## V2 Implementation Steps

These map to roadmap Steps 2.0–2.5 (see `docs/roadmap.md`).

### Step 2.0 — V2 Redesign ← this document
**Status:** In progress. This spec document is the primary deliverable.

Exit criteria:
- [x] GOVERNANCE_STATE.md SD-003 entry complete
- [x] Roadmap updated with Steps 2.1–2.5 refined
- [x] V2 entry criteria revised in roadmap
- [ ] This spec document complete and committed ← current task

### Step 2.1 — E2 Separation (SD-001 resolution)
**Status:** Code complete. Formal close pending parity check.

What was done:
- E2.generate_candidates_cem() removed
- HippocampalModule created as independent class
- E2.forward_counterfactual() added
- REEAgent wired to HippocampalModule
- CausalGridWorld built
- Smoke tests pass

Remaining:
- [ ] Parity check: replicate V1 PASS results (MECH-059, 056, 061, 060/067) on V2 substrate
- [ ] SD-001 formally closed in GOVERNANCE_STATE.md after parity check passes

### Step 2.2 — Representation Interface Contract
**Status:** Not started. Original spec content (below) defines scope.

Scope: sensor adapters → JEPA-like context/target latent interfaces; IMPL-022; stable
output streams; calibration metrics. E1 prior wired into HippocampalModule. Full
bidirectional E1↔E2 loop connected.

### Step 2.3 — Persistent Causal Environment
**Status:** Environment built. Baseline validation not run.

Remaining:
- [ ] Baseline experiment confirming agent-caused vs env-caused signal is empirically
      distinguishable (not just structurally present) in CausalGridWorld

### Step 2.4 — Self-Attribution Substrate
**Status:** Not started. Prerequisite: Steps 2.1 and 2.3 closed.

Scope: counterfactual E2 queries exercised experimentally; first genuine experiments
isolating agent-caused vs environment-caused harm; SD-003 closed in GOVERNANCE_STATE.md.

Success criterion: at least one genuine PASS on a self-attribution claim using
`forward_counterfactual()` against CausalGridWorld.

### Step 2.5 — V2 Qualification
**Status:** Not started. Prerequisite: all prior steps.

---

## Required Metrics (V2)

### Core representation metrics (Step 2.2)
- `latent_prediction_error_mean`
- `latent_prediction_error_p95`
- `latent_rollout_consistency_rate`
- `latent_residual_coverage_rate`
- `precision_input_completeness_rate`
- `latent_uncertainty_calibration_error` (if confidence-channel inputs present)

### Mechanism-targeted metrics
- `e1_e2_timescale_separation_ratio` (MECH-058) — expected to improve on V2 substrate
- `uncertainty_coverage_rate` (MECH-059)
- `cross_channel_leakage_rate` (MECH-060, provisional hook for V3)

### SD-003 self-attribution metrics (Step 2.4)
- `agent_caused_harm_rate` — harm events attributed to agent causal footprint
- `env_caused_harm_rate` — harm events attributed to background environment drift
- `counterfactual_delta_mean` — mean |z_actual - z_cf| across transitions
- `attribution_accuracy` — fraction of transition_type labels correctly predicted by
  counterfactual delta

### HippocampalModule metrics (Step 2.1 parity / Step 2.3+)
- `terrain_bias_score` — degree to which CEM iterates toward lower-residue regions
- `elite_harm_mean` — mean harm of elite trajectories vs random baseline

---

## Failure Gates (V2)

### Hard-fail conditions (block V2 completion)
- Adapter contract drift or missing required signal declaration
- Timescale collapse (E1/E2 separation fails repeatedly on V2 substrate)
- Uncertainty stream unavailable or uncalibrated where required
- Residual/precision input completeness below threshold
- E2 counterfactual queries produce no measurable causal delta (Step 2.4)
- CausalGridWorld agent/env distinguishability not confirmed empirically (Step 2.3)
- SD-001 parity check fails: V1 PASS experiments do not replicate on V2 substrate

### Readiness thresholds (tunable, but explicit)
- `latent_residual_coverage_rate >= 0.95`
- `precision_input_completeness_rate >= 0.95`
- `e1_e2_timescale_separation_ratio >= 1.5` in qualification lane
- `agent_caused_harm_rate` vs `env_caused_harm_rate` separable under matched seeds
- `counterfactual_delta_mean > 0` in at least one self-attribution experiment
- V1 PASS claims (MECH-059, 056, 061, 060/067, 062, 063) replicate on V2 substrate
- No unresolved adapter-contract failures across two consecutive governance cycles

---

## Acceptance Checklist (Go/No-Go for V2 Completion)

- [ ] SD-001 closed: E2 parity check passes, HippocampalModule independently testable
- [ ] SD-002 documented: e2.md updated with mutual constitution framing
- [ ] SD-003 closed: counterfactual E2 querying demonstrated experimentally
- [ ] CausalGridWorld: agent/env distinguishability confirmed empirically
- [ ] Representation interface stable across qualification and stress lanes (Step 2.2)
- [ ] All required metrics emitted in contract-compliant experiment packs
- [ ] Core V2 mechanism claims have active evidence with documented conflict handling
- [ ] Governance output recommends moving implementation focus to V3 control completion

---

## Step 2.2 Scope: Representation Interface Contract

*Content below is from the original V2 spec. Scope: Step 2.2 only.*

---

---

## Terminology Mode (v2)

V2 canonical docs in `REE_assembly` use REE-first language throughout.

JEPA is used as inspiration only — for the self-supervised latent prediction principle and
the conceptual distinction between context encoding (slow) and target prediction (fast).
JEPA terminology does not appear in V2 contracts, schemas, or metric keys. There is no
JEPA adapter layer in V2; E1, E2, and LatentStack are the native REE representation system.

---

## Step 2.2 Scope: E1/E2 Representation Interface Contract

**Note on JEPA (2026-03-01):** JEPA is used as inspiration only. REE-v2 implements its own
native E1/E2 representation system. No JEPA adapter signals, proxy bank, or EMA anchor path
from JEPA are part of the V2 contract. The REE latent stack (LatentStack, E1, E2) is the
canonical implementation, not an adapter layer over an external system.

### In scope (Step 2.2)

- Native sensor ingress: normalise environment observations to LatentStack input format
- E1/E2 representation interface contract:
  - stable latent output streams (`z_t`, `z_hat`, `pe_latent`, optional `uncertainty_latent`)
  - E1 prior wired into HippocampalModule (currently computed but not connected; Step 2.2 work)
  - E2→E1 autotrain pathway design (V3 scope; interface stub in V2)
- Stable, contract-compliant experiment pack output
- Uncertainty/calibration channels with measurable calibration

### Out of scope (Step 2.2)

- Final control-plane arbitration policy (V3)
- Full hippocampal replay/planning controller (V3)
- Full E3 commitment policy and accountability (V3)

V2 must still expose stub hooks for:
- pre-commit simulation error stream (`MECH-061`)
- post-commit realized error stream (`MECH-061`)
- commit-boundary token envelope (`HK-007`)
- trajectory candidate metadata (`HK-008`, `MECH-062`)

These become V3 primary implementation scope.

### Step 2.2 Implementation Objectives

- `OBJ-V2-001`: stable latent representation outputs under repeated runs and seed variation
- `OBJ-V2-002`: explicit uncertainty/error channels with measurable calibration
- `OBJ-V2-003`: strict experiment-pack contract compliance (manifest, metrics, summary)
- `OBJ-V2-004`: expose V3-ready hook stubs without embedding V3 policy decisions
- `OBJ-V2-005`: E1 prior wired into HippocampalModule (bidirectional E1↔E2 loop connected)

### Step 2.2 E1/E2 Interface Contract

Runtime ingress (per step):
- `obs_t`: current environment observation tensor
- `ctx_window`: ordered context frames/latent states `[z_{t-k}, ..., z_{t-1}]`
- `action_t` (optional): action taken at step t (for E2 conditioning)
- `run_tags`: mode and scenario labels for experiment pack

Runtime egress (per step):
- `z_t`: current latent state `[batch, latent_dim]` — from LatentStack.get_affordance_latent()
- `z_hat`: E1 long-horizon predictions `[batch, horizon, latent_dim]`
- `z_next_pred`: E2 fast next-state prediction `[batch, latent_dim]`
- `pe_latent`: latent prediction error from committed trajectory
  - `mean`: mean squared error over latent_dim
  - `p95`: 95th percentile across batch
- `uncertainty_latent` (optional):
  - `dispersion`: std of z across ensemble or rollout samples
  - `calibration_error`: if calibration head present

All production evidence must be exportable into contract-compliant experiment pack keys.

### Step 2.2 Configuration Contract

Required configurable parameters:

- `latent_dim`
- `e1_horizon`: E1 long-horizon prediction steps
- `e2_rollout_horizon`: E2 rollout horizon for trajectory candidates
- `e2_num_candidates`: number of CEM candidate trajectories
- `hippocampal_num_cem_iterations`: CEM iterations in HippocampalModule
- `residue_rbf_centers`: number of RBF harm centers in ResidueField
- `uncertainty_estimator`: `none | dispersion`
- `lambda_ethical`: E3 ethical cost weight (placeholder; requires calibration)
- `rho_residue`: E3 residue cost weight (placeholder; requires calibration)

Required reproducibility metadata in emitted manifests:
- scenario id/name and seed
- config hash
- environment: `env_id`, `env_version`, `grid_size`, `contamination_spread`, `env_drift_prob`
- source repo commit

### Step 2.2 Qualification Profiles

1. **E1/E2 timescale ablation** (MECH-058, retested on clean V2 substrate)
   - E1_FROZEN vs E2_FROZEN vs FULL on CausalGridWorld
   - Now interpretable cleanly: E2_FROZEN = no transition prediction; E1_FROZEN = no
     associative prior. SD-001 conflation no longer contaminates results.

2. **Uncertainty channels** (MECH-059)
   - Deterministic vs dispersion estimator
   - Verify precision-input completeness

3. **Write-locus validation** (MECH-060/067, parity check on V2)
   - Confirm V1 PASS replicates on V2 substrate
   - Pre-commit sim error vs post-commit realized error separation

4. **E1 prior integration** (new in V2)
   - With vs without E1 prior wired into HippocampalModule
   - Verify terrain_prior biases trajectory proposals toward lower-residue regions

### Step 2.2 Milestones

`M2.2-0` E1 prior wired into HippocampalModule; bidirectional loop complete
`M2.2-1` Stable representation outputs: z_t, z_hat, pe_latent present across runs
`M2.2-2` Uncertainty calibration: dispersion estimator validates against held-out outcomes
`M2.2-3` V3 hook stubs: pre/post commit placeholders exported consistently
`M2.2-4` Step 2.2 stabilization: two clean experiment cycles, no contract churn

---

## Cross-Version Hooks Required in V2

V2 must expose all `v2_required` hooks listed in `docs/architecture/hook_registry.v1.json`.

V2 should also emit stubs for `v3_planned` hooks where feasible:
- pre-commit simulation error stream placeholder
- post-commit realized error stream placeholder
- commitment-context trace IDs for attribution
- rollout-candidate metadata for hippocampal/controller attachment

Bridge coverage expectation in `v2_required` hook tier:
- commit-boundary token envelope export (`HK-007`, `MECH-061`)
- tri-loop gate arbitration trace export (`HK-008`, `MECH-062`)
- orthogonal control-axis telemetry export (`HK-009`, `MECH-063`)

These are interface commitments, not full behavior commitments for the future layers.

---

## Repository Strategy

- `REE_assembly`: canonical governance, spec, evidence matrix
- `ree-v2`: primary qualification lane for V2 experiments
- `ree-v1-minimal`: legacy baseline/reference harness for parity checks only;
  not the primary V2 qualification lane
- `ree-experiments-lab`: stress/falsification/adversarial experiments

V2 qualification lane activation: once Step 2.1 parity check passes, `ree-v2` becomes
the required lane. `ree-v1-minimal` is retired from primary qualification status.

---

## Open Questions

- What threshold values should gate V2 readiness without overfitting to current harnesses?
- How much of dual pre/post commit channeling should be stubbed vs implemented in late V2?
- What is the right uncertainty estimator for V2 given the native E1/E2 architecture?
  (The JEPA ensemble/head distinction is no longer relevant; dispersion over E2 rollouts
  is the natural candidate.)

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
- MECH-061
- MECH-062
- MECH-063
- MECH-063
