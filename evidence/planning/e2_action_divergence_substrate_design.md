# E2 action-conditional divergence — substrate design memo

**Date:** 2026-05-28
**Author session:** `e2-action-divergence-design-memo-20260528T174310Z`
**Status:** plan-of-record for the option (ii) E2 fix
**Lever chosen:** B — contrastive next-state ([Srivastava et al. 2021](https://arxiv.org/abs/2112.01163) style)
**Successor session:** `/implement-substrate` on E2's `world_forward` (separate)

---

## Origin

Commissioned after the [2026-05-25 V3-EXQ-571 root-cause finding](v3_exq_571_root_cause_2026-05-25.md) and the [2026-05-28 ML+biology lit-pull](../literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md) settled the question of which architectural fix to pursue for the E2 world-forward per-candidate signal collapse. User chose option (ii) (fix E2) with lever B (contrastive next-state) per AskUserQuestion 2026-05-28T17:38Z, after I recommended it on three grounds: simplest to implement, negative-sample distribution falls out of CEM's existing K-candidate batch, and the target failure mode (K different actions collapse to the same predicted z_world) is exactly the regime where contrastive losses have the most signal.

This memo specifies what gets added to E2 and what the next experiment programme looks like. It does not edit code; the implementation belongs to a separate `/implement-substrate` session.

---

## What is broken

[`ree-v3/ree_core/predictors/e2_fast.py:176-197`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e2_fast.py):

```python
def world_forward(self, z_world, action):
    a_enc = self.world_action_encoder(action)   # Linear(action_dim, action_dim)
    z_a = torch.cat([z_world, a_enc], dim=-1)
    delta = self.world_transition(z_a)
    return z_world + delta
```

With `world_dim=32` and `action_dim=4`, the action contributes 4/36 ≈ 11% of the input dimensionality to `world_transition`. Under reconstruction-shaped training, the state-dominated solution that ignores action is the local minimum. V3-EXQ-571 measured `cand_world_pairwise_dist = 0.0000` across K=8 candidates that differ only in their first action one-hot — the action's contribution has been fitted to zero.

The biological reference (cerebellum, prefrontal counterfactual rollout, vestibular cerebellum) preserves action-specificity *at the prediction step* via dedicated structural mechanisms. The ML field has named this failure family ([Saanum, Dayan, Schulz 2024](https://arxiv.org/abs/2401.17835) PLSM diagnosis: "lack of systematic representation of action effects") and offers three independent training-objective remedies. We pick the contrastive one.

---

## The substrate change

### Loss form

For each training batch containing K rollouts that share starting state `z_world_0` but differ in first action `a_i`, add an auxiliary InfoNCE-style contrastive loss against E2's `world_forward`:

```
For each anchor i in [K]:
  positive:   (z_world_0, a_i) -> predicted z_world_1[i]
  negatives:  (z_world_0, a_j) for j != i in the same batch, mapped through
              world_forward to produce K-1 alternative predictions.

L_contrast_i = -log( exp(-||pred_i - z_world_1[i]||^2 / tau)
                    / sum_j exp(-||pred_j - z_world_1[i]||^2 / tau) )
```

The model can only minimise this loss if predictions for different actions are distinguishable in `z_world`. A model that collapses K different actions to the same predicted `z_world` is structurally precluded.

Total E2 loss becomes:

```
L_E2 = L_reconstruction + w_contrast * mean_i(L_contrast_i)
```

with `w_contrast` defaulting to a small value (suggested 0.01) and configurable for sweep.

### Why this scope

- Apply to `world_forward` only, not `predict_next_self`. `z_self` is not the collapse site; V3-EXQ-571 specifically measured `cand_world_pairwise_dist`.
- Negatives come from in-batch sibling CEM candidates — same `z_world_0`, different first action. This is structurally the case where collapse hurts, and the negatives are informative by construction (they really are different actions). No negative-sample design pass needed.
- Asymmetric (anchor-to-prediction) is sufficient. Symmetric InfoNCE doubles the cost without changing the architectural commitment.

### What does NOT change

- `world_transition` and `world_action_encoder` shapes and inits unchanged.
- `predict_next_state`, `predict_next_self`, `action_object`, `forward`, `forward_counterfactual` unchanged.
- E1, E3, hippocampal module, residue field, all downstream consumers unchanged.
- Existing rollout-loss machinery unchanged — the contrastive term is added, not substituted.

---

## Config knobs

All new flags consumed by `REEConfig.from_dims` and propagated to `E2Config`:

| Flag | Type | Default | Role |
|---|---|---|---|
| `e2_action_contrastive_enabled` | bool | `False` | Master switch. Default OFF guarantees bit-identical to pre-substrate HEAD. |
| `e2_action_contrastive_weight` | float | `0.01` | `w_contrast` in the loss form above. Subject to a small calibration sweep at validation time. |
| `e2_action_contrastive_temperature` | float | `0.1` | InfoNCE temperature `tau`. Standard literature value. |
| `e2_action_contrastive_min_batch_classes` | int | `2` | Minimum distinct first-action classes per batch required for the contrastive loss to fire. Falls through to no-op below the floor (no negatives to use). |

No defaults of existing E2 / latent / agent parameters change. Per the `implement-substrate` skill rule.

---

## MECH-094 (hypothesis tag)

The contrastive loss is a *training* signal on a forward predictor, not a content-write into residue / hippocampus / replay. It is invoked from the standard E2 training loop, which is already off the simulation path. No new MECH-094 plumbing required at the loss-computation site. If E2 is ever called with `simulation_mode=True` in a future replay-driven training context, the contrastive loss should fall through to zero — handle the same way as other regulators (`SD-035 / MECH-279 / MECH-313 / MECH-314 / MECH-319 / MECH-320` precedent): accept a `simulation_mode: bool = False` argument on the loss-compute helper and return `torch.tensor(0.0)` when `True`.

---

## Diagnostic: `cand_world_pairwise_dist`

The headline metric V3-EXQ-571 used to diagnose the collapse, and that the [lit-pull SYNTHESIS](../literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md) verdict 3 named as a methodological gap in the model-based RL literature.

Definition: for a batch of K CEM candidates sharing `z_world_0` but differing in first action `a_i`, compute the K predicted first-step `z_world` outputs via `world_forward`, then take the mean pairwise L2 distance:

```
cand_world_pairwise_dist =
  mean over (i, j), i != j: ||world_forward(z_world_0, a_i) - world_forward(z_world_0, a_j)||_2
```

Under the current substrate this is `0.0000` (V3-EXQ-571 measurement). Under a successful contrastive fix it should rise above a substrate-readiness threshold (suggested `>= 0.05` in normalised units, calibrated empirically by V3-EXQ-NEW-1).

This is the right metric to expose as a substrate-readiness diagnostic AND to land as a published novel measurement once the substrate fix is validated. It is publishable in its own right.

Implementation: a small helper `e2_fast.py:cand_world_pairwise_dist(e2, z_world_0, candidate_actions)` that takes the agent, a starting state, and a `[K, action_dim]` candidate-action batch, runs `world_forward` K times, and returns the mean pairwise distance. Called from the new substrate-readiness experiment and exposed in a diagnostics dict on training manifests when the flag is on.

---

## Acceptance criteria for V3-EXQ-NEW-1 (substrate-readiness diagnostic)

Sub-tests UC1–UC5 in the standard substrate-readiness pattern (`/queue-experiment` skill convention):

- **UC1 — Module surface.** New config flags present with correct defaults; `cand_world_pairwise_dist` helper importable; E2 loss helper accepts `simulation_mode` kwarg.
- **UC2 — Master-OFF backward-compat.** Single tick of `act_with_split_obs` and a one-step E2 training pass with `e2_action_contrastive_enabled=False` produce bit-identical outputs to pre-substrate HEAD across 3 seeds. 506/506 contracts + 7/7 preflight PASS unchanged.
- **UC3 — Per-candidate divergence rises.** With the flag ON and 200 SGD steps of synthetic batches containing K=8 candidates per `z_world_0`, `cand_world_pairwise_dist` rises from `~0.0` baseline to `>= 0.05` (threshold subject to one-shot calibration; the *direction* of change is the load-bearing claim, not the magnitude).
- **UC4 — Contrastive-task accuracy.** Held-out batch contrastive accuracy `> 50%` (random baseline `1/K = 12.5%` for K=8). Confirms the contrastive task is learnable on the substrate, not just that the loss decreases.
- **UC5 — MECH-094 simulation gate.** Loss helper called with `simulation_mode=True` returns `tensor(0.0)` and does not advance any optimiser state.

Total runtime budget: < 30 min on Mac for the substrate-readiness diagnostic. Behavioural validation (the FP-2 falsifier) is a separate queue entry.

---

## Successor experiments

In the order they get queued:

1. **V3-EXQ-NEW-1 — Substrate-readiness diagnostic** (this memo). Queued via `/queue-experiment` after `/implement-substrate` lands the change. Confirms the substrate is operative on synthetic batches; `cand_world_pairwise_dist >= 0.05` is the load-bearing PASS criterion.

2. **V3-EXQ-569a — Matched-entropy FP-2 falsifier on the fixed substrate** ([GAP-A R1 successor on `behavioral_diversity_isolation_plan.md`](behavioral_diversity_isolation_plan.md)). Same six-arm matched-entropy sweep design as V3-EXQ-569 (which was reclassified non-contributory because the bias channel structurally carried no per-candidate variance). On the fixed substrate, the R1.a/R1.b decision rule can finally fire:
   - **R1.a** (matched -> `non_contributory`): SP-CEM entropy = noise-matched entropy on the diversity metrics. Theory 1 not load-bearing on its own; attention shifts to theories 2-4.
   - **R1.b** (SP-CEM > matched noise on `trajectory_class_count`, FP-2 cleared): theory 1 confirmed; advance to Rung 2.

3. **V3-EXQ-NEW-2 — Per-candidate spread re-measurement** (optional follow-on). Re-run V3-EXQ-571 / V3-EXQ-609's per-candidate spread decomp on the fixed substrate, to confirm that `bias_fraction_*` channels (MECH-314a, MECH-320, MECH-295, SD-033a, SD-033b) actually carry per-candidate variance now that the upstream signal is preserved. This closes the diagnostic loop opened by V3-EXQ-571.

4. **Downstream MECH-292 / MECH-293 / ghost-goal / commitment-closure** unblocks: once `cand_world_pairwise_dist > 0`, every downstream consumer that reads `cand_world_summaries` recovers per-candidate signal. The plan-of-record entries for those gaps can be reviewed against the fixed substrate.

---

## What this memo does NOT do

- **Does not pick the calibration values empirically.** `w_contrast`, `tau`, and the `cand_world_pairwise_dist >= 0.05` threshold are starting points; V3-EXQ-NEW-1 calibrates them.
- **Does not pre-commit to an InfoNCE form over PLSM-style MI factorisation.** If V3-EXQ-NEW-1 FAILs (contrastive task is not learnable on REE's E2 architecture for some reason — e.g. the world_dim is too small relative to action_dim for the contrastive task to have a useful loss landscape), the fall-back is PLSM-style MI factorisation as the second lever, or architectural restructure (option D from the synthesis verdict) as the third.
- **Does not modify MECH-094, ARC-065, ARC-062, MECH-314a, MECH-320, MECH-295, SD-033a, SD-033b, or any other claim.** Those edits are governance follow-ons on the validation result.
- **Does not queue V3-EXQ-NEW-1.** Separate `/queue-experiment` session per `REE_Working/CLAUDE.md` skill discipline.

---

## Plan-of-record sequencing

| Step | Skill / session | Output | Status |
|---|---|---|---|
| 0 | this memo | `e2_action_divergence_substrate_design.md` | DONE 2026-05-28 |
| 1 | `/implement-substrate` | `e2_fast.py` contrastive loss + config knobs + `cand_world_pairwise_dist` helper + contract tests + bit-identical-OFF regression | NEXT |
| 2 | `/queue-experiment` | `V3-EXQ-NEW-1` substrate-readiness diagnostic queued | After step 1 |
| 3 | runner | V3-EXQ-NEW-1 manifest landed | After step 2 |
| 4 | `/queue-experiment` | V3-EXQ-569a matched-entropy FP-2 falsifier queued (R1.a/R1.b decision rule) | After step 3 PASS |
| 5 | runner | V3-EXQ-569a manifest landed | After step 4 |
| 6 | governance | Apply R1.a or R1.b per the decision rule; update GAP-A status | After step 5 |

Each step is a separate session to keep blast radii small and concurrency clean.

---

## What the substrate fix is NOT promising

Three honest disclaimers, mirroring the synthesis verdict's tone:

- **The contrastive task being learnable does not by itself imply behavioural diversity emerges.** Per-candidate `z_world` divergence is necessary (V3-EXQ-571 documented it being absent and downstream channels falling silent), but the V3-EXQ-569a matched-entropy falsifier is what actually tests whether downstream behaviour responds.
- **Lever B may not be the right lever** if REE's specific architecture has a feature we have not noticed. PLSM-style MI factorisation (lever A) and SWIRL-style MI maximisation (lever C) are valid fallbacks. If V3-EXQ-NEW-1 fails on the InfoNCE objective, that is a substrate finding worth its own autopsy before re-trying a different lever.
- **Option (i) (extend GAP-B one-hot bypass) is still on the table** as a tactical step if the V3-EXQ-569a FP-2 decision is needed urgently and the substrate fix is taking longer than expected. The lit-pull synthesis verdict named (i) as a workaround, not as wrong; it just commits to an architecture neither the cerebellar nor prefrontal reference needs.

---

*Author session: e2-action-divergence-design-memo-20260528T174310Z. Commissioned 2026-05-28T17:43:10Z. References: [v3_exq_571_root_cause_2026-05-25.md](v3_exq_571_root_cause_2026-05-25.md), [evidence/literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md](../literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md), [behavioral_diversity_isolation_plan.md](behavioral_diversity_isolation_plan.md).*
