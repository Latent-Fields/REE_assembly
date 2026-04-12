---
nav_exclude: true
---

# Efficiency and Dimensionality Hypothesis: E1/E2/E3 Multi-Stack vs Single-Stack

**Status:** Working hypothesis — Phase 2 ablations pending
**Date:** 2026-03-19
**Related claims:** SD-004, SD-005, MECH-069, MECH-070, ARC-021

---

## 1. The Question

Does the E1/E2/E3 multi-stack architecture achieve equivalent or better reasoning capability at lower effective latent dimensionality than a single unified-latent stack? And if so, why?

This matters practically: if the answer is yes, multi-stack systems can solve harder planning problems with fewer total parameters, and their internal representations should be more interpretable (lower intrinsic dimensionality per module). If the answer is no — or only conditionally yes — we need to understand the conditions.

---

## 2. The Theoretical Case For Multi-Stack Efficiency

### 2.1 Gradient Specialization Reduces Interference

In a single-stack model trained to minimize a joint loss over sensory prediction error, motor-sensory error, and harm/goal error, gradient directions for each signal conflict in shared parameter space. The network requires additional capacity (higher ambient dimensionality) to simultaneously satisfy all three error signals without destructive interference.

REE's multi-stack routes each error channel to its own module with its own optimizer:
- **E1** (Adam 1e-4) — sensory prediction error only
- **E2** (separate optimizer) — motor-sensory error (z_self domain)
- **E3** (separate optimizer) — harm/goal error (z_world domain)

Each module trains on a cleaner signal, theoretically converging to a lower-dimensional attractor for its specific task. A single 64-dim unified latent trained on all three signals simultaneously is predicted to require more effective dimensions to disentangle what three 32-dim specialized modules separate structurally.

**Prediction:** PCA 90%-variance threshold on multi-stack latents < PCA threshold on equivalent unified latent, at matched parameter count.

### 2.2 Action-Object Compression (SD-004, EXQ-003)

CEM-based planning in raw z_world (32-dim) requires exponentially more candidates to cover the search space than planning in the action-object space O (16-dim). SD-004 implements a learned compression from z_world-level effects to 16-dim action objects, enabling hippocampal navigation to use a much smaller search space.

EXQ-003 (PASS, 2026-03-xx): terrain-guided planning in O-space achieves **6× survival improvement** over random trajectory selection in z_world. This is direct empirical evidence that the dimensionality reduction in the planning space — not just the architecture — is doing work.

This benefit is structural and does not require functional z_self/z_world separation (SD-005) to hold. It is the strongest current piece of evidence for the efficiency hypothesis.

### 2.3 Timescale Factoring

E1 operates with prediction_horizon=20, trained on slow world-model updates (LSTM). E2 operates with rollout_horizon=30, producing fast motor-sensory predictions. E3 evaluates harm over committed trajectory windows.

In a flat single-stack, all three timescales must be represented within the same forward pass and parameter space. The network cannot cheaply ignore long-horizon context when doing fast motor-sensory computation, or ignore low-level sensory dynamics when doing high-level harm evaluation. Timescale separation requires additional capacity in a flat model.

Multi-stack factoring means each module only processes the temporal abstraction appropriate to its function. **Prediction:** multi-stack requires fewer total parameters to reach comparable performance on tasks with mixed-timescale demands.

### 2.4 Attribution Clarity (SD-003)

Counterfactual self-attribution — `E2(z, a_actual) − E2(z, a_cf)` — requires that z_self contains primarily proprioceptive/motor-sensory content and z_world contains exteroceptive/harm-relevant content. If z is a unified 64-dim latent mixing both, the subtraction produces a vector that conflates self-caused effects with ambient world dynamics, requiring a higher-dimensional probe to recover clean attribution signal.

This is why the V2 SD-003 experiments (EXQ-027) failed with z_gamma: the unified latent could not support clean attribution without SD-005 (z_self/z_world split).

---

## 3. Counterevidence and Costs

### 3.1 Structural Separation ≠ Functional Separation (SD-008)

The most important caveat: having separate modules and separate latent dimensions does not automatically produce functionally specialized representations.

**SD-008 finding:** In v3, alpha_world=0.3 in LatentStack.encode() creates a ~3-step EMA that suppresses z_world's response to events to ~30% of its nominal amplitude. Despite the z_self/z_world split being architecturally correct, z_world is functionally unresponsive to harm events — making it no better than a stale running average.

**Implication:** Multi-stack has a configuration cost. A misconfigured multi-stack can be strictly worse than a flat baseline that at least responds to all signals uniformly. The efficiency gains are only realized when modules are correctly tuned.

EXQ-023 (alpha_world=0.9) is queued to fix SD-008. Until it passes, functional efficiency claims are premature.

### 3.2 Negative world_selectivity_margin (EXQ-001)

EXQ-001 (FAIL): world_selectivity_margin = −0.1252. z_world currently responds more strongly to body/proprioceptive events than to world/exteroceptive events — the opposite of its intended role.

This means the current v3 multi-stack is not yet achieving the representation separation that the efficiency hypothesis requires. EXQ-001 must be rerun after SD-008 and SD-009 fixes before the Phase 2 ablation comparison is valid.

### 3.3 Engineering Overhead

Multi-stack requires N separate optimizers, N separate loss functions, explicit routing of error signals, and careful hyperparameter tuning per module. A single-stack model with a joint loss is simpler to train and debug. For tasks where all three error signals are weak or correlated, the separation provides no benefit and adds complexity.

---

## 4. Existing Evidence Summary

| Experiment | Claim | Status | Relevance to Efficiency Hypothesis |
|------------|-------|--------|-------------------------------------|
| **EXQ-003** | SD-004 action objects | **PASS** | 6× survival gain — direct evidence for O-space compression efficiency |
| **EXQ-001** | SD-005 z-split selectivity | **FAIL** | world_selectivity_margin<0 — functional separation not yet achieved |
| **EXQ-011** | MECH-095 TPJ proxy | **FAIL** (marginal) | z_self still contaminated — specialization cost not yet offset |
| **EXQ-023** | SD-008 alpha_world=0.9 | **Queued** | Gate for all functional efficiency claims |
| V2 EXQ-023 | MECH-058 E1/E2 timescale | **FAIL** | Timescale separation not demonstrable in V2; V3 split latent may resolve this |

**Current verdict:** The planning-space compression benefit (SD-004) is confirmed. The latent specialization benefit (SD-005) is architecturally present but not yet functionally realized. The full efficiency hypothesis is **plausible but unconfirmed**, blocked on SD-008.

---

## 5. Open Questions for Phase 2 Ablations

1. **Unified latent ablation:** Does a z_gamma=64 unified latent (single optimizer, same E1/E2/E3 structure) match or exceed multi-stack performance on CausalGridWorld? At what parameter count?

2. **E1-only baseline:** What is the floor? How much of multi-stack performance comes from E2/E3 planning vs E1 associative prior?

3. **E1+E2 without E3:** Does E3 harm evaluation add measurable efficiency beyond E2 rollouts? Or is CEM in O-space sufficient?

4. **Effective dimensionality measurement:** What is the intrinsic dimensionality (PCA 90% threshold) of z_self, z_world, and O separately vs a unified z_gamma of the same total size?

5. **Training efficiency:** Does multi-stack converge to equivalent performance in fewer episodes? (Per-module credit assignment should help.)

---

## 6. Conditions Under Which Multi-Stack Efficiency Holds

Based on the theoretical analysis and current evidence, multi-stack efficiency over single-stack is predicted to hold when:

1. The task has **multiple incommensurable error signals** (sensory, motor-sensory, harm) — ARC-021 / MECH-069
2. The task requires **planning over extended horizons** (rollout_horizon > prediction_horizon) — MECH-070
3. The planning search space benefits from **structured compression** (action objects) — SD-004
4. The error channels have **different timescales** that need to be factored
5. **Module hyperparameters are correctly tuned** — especially alpha_world ≥ 0.9 (SD-008)

If any of 1–4 do not hold (e.g. a simple reactive task with a single reward signal), single-stack with a unified latent may be equally or more efficient due to lower engineering overhead.

---

## 7. Next Steps

**Immediate:**
- Wait for EXQ-023 (SD-008 alpha_world=0.9) result
- If PASS: rerun EXQ-001; confirm world_selectivity_margin > 0
- If EXQ-001 rerun PASS: proceed to Phase 2 ablations

**Phase 2 ablation experiments to write (after EXQ-023 PASS):**
- `v3_exq_NNN_unified_latent_ablation.py` — full multi-stack vs z_gamma=64 unified latent
- `v3_exq_NNN_e1_only_baseline.py` — E1 LSTM + greedy vs full multi-stack
- `v3_exq_NNN_e1_e2_no_e3.py` — E1+E2 rollouts only vs full multi-stack

**Phase 3 (future):** DreamerV3-style RSSM external baseline, parameter-matched, same CausalGridWorld evaluation. Register as `V3-EXQ-EXT-001`.
