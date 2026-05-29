# SD-056: e2.action_conditional_divergence_contrastive

**Claim ID:** SD-056
**Subject:** e2.action_conditional_divergence_contrastive
**Status:** IMPLEMENTED 2026-05-29
**Registered:** 2026-05-29
**Depends on:** SD-005 (z_world / z_self split), ARC-033 (E2_harm_s forward family)
**Blocks (substrate-readiness):** V3-EXQ-569a matched-entropy FP-2 falsifier (GAP-A R1.a/R1.b decision rule); downstream `cand_world_summaries` consumers (MECH-292, MECH-293, ghost-goal, commitment-closure, MECH-314a curiosity novelty, MECH-320 tonic vigor, MECH-295 liking bridge, SD-033a lateral_pfc, SD-033b ofc).

## Problem

[`ree-v3/ree_core/predictors/e2_fast.py:176-197`](../../../ree-v3/ree_core/predictors/e2_fast.py)
implements `world_forward`:

```python
def world_forward(self, z_world, action):
    a_enc = self.world_action_encoder(action)   # Linear(action_dim, action_dim)
    z_a = torch.cat([z_world, a_enc], dim=-1)
    delta = self.world_transition(z_a)
    return z_world + delta
```

With `world_dim=32` and `action_dim=4`, action contributes 4/36 ~ 11% of the input
dimensionality. Under reconstruction-shaped training, the state-dominated solution
(action contribution fitted to zero) is the local minimum.

**V3-EXQ-571 measurement** (manifest 2026-05-16):
`cand_world_pairwise_dist = 0.0000` across K=8 candidates that differ only in
their first action one-hot. The K diverse first-action one-hots collapse to a
single z_world after one E2 world-forward step.

**Same root cause as 2026-05-17 ARC-062 GAP-B autopsy**:
"SP-CEM delivers ~5 distinct first-action classes but E2 world-forward compresses
them to 0.22% of z_world magnitude before reaching the z_world-only GatedPolicy
heads -- the heads are under-fed." GAP-B fix was scoped only to `GatedPolicy`
(first-action one-hot bypass at the head input). Every other bias channel that
reads `cand_world_summaries` (MECH-314a curiosity novelty, MECH-320 tonic vigor,
MECH-295 liking, SD-033a lateral_pfc, SD-033b ofc) consumes the same compressed
first-step z_world and is doomed by the same upstream collapse. SD-056 is the
architecturally-faithful generalisation: fix the E2 world-forward training
objective so per-action divergence is preserved at the source, restoring
per-candidate signal to every downstream channel.

**Biological reference** (cerebellum, prefrontal counterfactual rollout,
vestibular cerebellum) preserves action-specificity *at the prediction step*
via dedicated structural mechanisms; ML literature names this failure family
(PLSM diagnosis Saanum/Dayan/Schulz 2024 "lack of systematic representation
of action effects") and offers three independent training-objective remedies
(PLSM MI factorisation, contrastive next-state, SWIRL MI maximisation). The
2026-05-28 SYNTHESIS verdict and user 2026-05-28T17:38Z decision chose lever B
(contrastive next-state).

## Solution

### Loss form

For each training batch containing K rollouts that share starting state
`z_world_0` but differ in first action `a_i`, add an auxiliary InfoNCE-style
contrastive loss against E2's `world_forward`:

```
For each anchor i in [K]:
  positive:   (z_world_0, a_i) -> predicted z_world_1[i]
  negatives:  (z_world_0, a_j) for j != i in the same batch, mapped through
              world_forward to produce K-1 alternative predictions.

L_contrast_i = -log( exp(-||pred_i - z_world_1[i]||^2 / tau)
                    / sum_j exp(-||pred_j - z_world_1[i]||^2 / tau) )
```

Equivalent to cross-entropy over `logits[i,j] = -||pred_j - target_i||^2 / tau`
with label `i` -- one row per anchor, K columns per prediction.

The model can only minimise this loss if predictions for different actions are
distinguishable in `z_world`. A model that collapses K different actions to the
same predicted `z_world` is structurally precluded.

Total E2 loss becomes:

```
L_E2 = L_reconstruction + w_contrast * mean_i(L_contrast_i)
```

with `w_contrast` defaulting to `0.01` (small relative to L_recon so the
auxiliary objective doesn't dominate the reconstruction signal during early
training; subject to a small calibration sweep at validation time).

### Scope (NOT changed)

- `world_transition` and `world_action_encoder` shapes and inits unchanged.
- `predict_next_state`, `predict_next_self`, `action_object`, `forward`,
  `forward_counterfactual` unchanged.
- E1, E3, hippocampal module, residue field, all downstream consumers unchanged.
- Existing rollout-loss machinery unchanged -- the contrastive term is added,
  not substituted.
- Applies to `world_forward` only, not `predict_next_self`. `z_self` is not the
  collapse site; V3-EXQ-571 specifically measured `cand_world_pairwise_dist`
  on the z_world stream.

Negatives come from in-batch sibling CEM candidates -- same `z_world_0`,
different first action. This is structurally the case where collapse hurts,
and the negatives are informative by construction (they really are different
actions). No negative-sample design pass needed.

Asymmetric (anchor-to-prediction) is sufficient. Symmetric InfoNCE doubles the
cost without changing the architectural commitment.

### Config knobs

All new flags on `E2Config` and surfaced through `REEConfig.from_dims`:

| Flag | Type | Default | Role |
|---|---|---|---|
| `e2_action_contrastive_enabled` | bool | `False` | Master switch. Default OFF guarantees bit-identical to pre-substrate HEAD. |
| `e2_action_contrastive_weight` | float | `0.01` | `w_contrast` in the loss form above. Calibratable at validation time. |
| `e2_action_contrastive_temperature` | float | `0.1` | InfoNCE temperature `tau`. Standard literature value. |
| `e2_action_contrastive_min_batch_classes` | int | `2` | Minimum distinct first-action classes per batch required for the contrastive loss to fire. Falls through to no-op below the floor (no informative negatives). |

No defaults of existing E2 / latent / agent parameters change.

### `cand_world_pairwise_dist` diagnostic helper

Headline metric V3-EXQ-571 used to diagnose the collapse, named by the lit-pull
SYNTHESIS verdict 3 as a methodological gap in the model-based RL literature
worth publishing as a standalone novel measurement once the substrate fix is
validated.

Definition: for a batch of K CEM candidates sharing `z_world_0` but differing
in first action `a_i`, compute the K predicted first-step `z_world` outputs
via `world_forward`, then take the mean pairwise L2 distance:

```
cand_world_pairwise_dist =
  mean over (i, j), i != j: ||world_forward(z_world_0, a_i) - world_forward(z_world_0, a_j)||_2
```

Under the current substrate this is `0.0000` (V3-EXQ-571 measurement). Under
a successful contrastive fix it should rise above a substrate-readiness
threshold (suggested `>= 0.05` in normalised units, calibrated empirically
by V3-EXQ-NEW-1; the *direction* of change is the load-bearing claim, not
the magnitude).

Implementation: `E2FastPredictor.cand_world_pairwise_dist(z_world_0,
candidate_actions)` takes a starting state and a `[K, action_dim]` candidate-
action batch, runs `world_forward` K times, and returns the mean pairwise
distance. Called from V3-EXQ-NEW-1 and exposed to training manifests in
behavioural successors.

### MECH-094

The contrastive loss is a *training* signal on a forward predictor, not a
content-write into residue / hippocampus / replay. It is invoked from the
standard E2 training loop, off the simulation path. No new MECH-094 plumbing
required at the loss-computation site. If E2 is ever called with
`simulation_mode=True` in a future replay-driven training context, the loss
helper accepts a `simulation_mode: bool = False` argument and returns
`torch.tensor(0.0)` when `True` (same defensive pattern as SD-035, MECH-279,
MECH-313, MECH-314, MECH-319, MECH-320, MECH-341).

## ML/AI engineering notes (Layer 7)

- **Technique adopted**: asymmetric InfoNCE (anchor-to-prediction),
  [Srivastava et al. 2021](https://arxiv.org/abs/2112.01163) contrastive RSSM
  style.
- **Engineering problem solved**: under reconstruction-only training the
  state-dominated solution (action contribution fitted to zero) is the local
  minimum when action dimensionality is small relative to state. Diagnosed by
  [Saanum/Dayan/Schulz 2024](https://arxiv.org/abs/2401.17835) PLSM as "lack
  of systematic representation of action effects."
- **REE-specific adaptation**: negatives drawn from in-batch sibling CEM
  candidates (`z_world_0` shared, first action differs) rather than random
  negative-sampling. Cheaper and structurally relevant -- no negative-mining
  sweep needed. Asymmetric form chosen over symmetric (doubles cost without
  changing architectural commitment).
- **Biological grounding compatibility**: cerebellar internal model
  ([Tanaka et al. 2020](https://doi.org/10.3389/fnsys.2020.00019)), prefrontal
  counterfactual rollout ([Miyamoto/Rushworth/Shea 2023](https://doi.org/10.1016/j.tics.2023.04.005)),
  vestibular cerebellum corollary discharge ([Cullen 2023](https://doi.org/10.1016/j.tins.2023.01.001))
  all preserve action-specificity at the prediction step via dedicated
  structural mechanisms. The contrastive loss enforces this same property --
  actions must be discriminable in the predicted z_world.
- **Known failure mode defended against**: degenerate batch (single first-
  action class) -- `min_batch_classes` floor returns 0 loss rather than
  producing meaningless gradients on uninformative negatives.
- **Numerical**: tau=0.1 standard literature value; w_contrast=0.01 small
  relative to L_recon so auxiliary objective doesn't dominate reconstruction
  signal during early training; both calibratable via V3-EXQ-NEW-1.
- **Phased training**: NOT required at the substrate level. Unlike encoder-
  head-on-frozen-latent patterns (EXQ-166b/c/d historical), both `L_recon` and
  `L_contrast` target the same predictor weights (`world_transition` +
  `world_action_encoder`) with compatible objectives. Joint training is the
  designed-for case.

## Architecture context

SD-056 is the substrate-side resolution of the V3-EXQ-571 root-cause finding.
It generalises the ARC-062 GAP-B one-hot bypass (which was scoped only to
GatedPolicy) by fixing the predictor itself rather than bypassing it. After
SD-056 lands and V3-EXQ-NEW-1 PASSes:

- Every downstream consumer that reads `cand_world_summaries` recovers
  per-candidate signal: MECH-314a curiosity novelty, MECH-320 tonic vigor,
  MECH-295 liking bridge, SD-033a lateral_pfc, SD-033b ofc.
- The V3-EXQ-569a matched-entropy FP-2 falsifier (GAP-A R1.a/R1.b decision
  rule on `behavioral_diversity_isolation_plan.md`) becomes runnable on the
  fixed substrate. V3-EXQ-569 was reclassified non_contributory specifically
  because the bias channel structurally carried no per-candidate variance;
  on the fixed substrate the decision rule can finally fire.
- The plan-of-record entries for MECH-292 / MECH-293 / ghost-goal /
  commitment-closure gaps that consume `cand_world_summaries` can be
  reviewed against the fixed substrate.

## What this SD enables

- **V3-EXQ-NEW-1** substrate-readiness diagnostic: this SD's UC1-UC5 acceptance
  criteria (queued in the same /implement-substrate session per skill).
- **V3-EXQ-569a** matched-entropy FP-2 falsifier: GAP-A R1.a/R1.b decision rule
  applied on the fixed substrate, separate /queue-experiment session per
  plan-of-record sequencing.
- **V3-EXQ-NEW-2** (optional follow-on): re-run V3-EXQ-571 / V3-EXQ-609
  per-candidate spread decomposition on the fixed substrate to confirm
  `bias_fraction_*` channels (MECH-314a, MECH-320, MECH-295, SD-033a, SD-033b)
  actually carry per-candidate variance now that the upstream signal is
  preserved.

## What this SD does NOT promise

- **The contrastive task being learnable does not by itself imply behavioural
  diversity emerges.** Per-candidate `z_world` divergence is necessary
  (V3-EXQ-571 documented its absence and downstream channels falling silent),
  but the V3-EXQ-569a matched-entropy falsifier is what actually tests whether
  downstream behaviour responds.
- **Lever B (contrastive) may not be the right lever** if REE's specific
  architecture has a feature we have not noticed. PLSM-style MI factorisation
  (lever A) and SWIRL-style MI maximisation (lever C) are valid fallbacks. If
  V3-EXQ-NEW-1 fails on the InfoNCE objective, that is a substrate finding
  worth its own autopsy before re-trying a different lever.
- **Option (i) (extend GAP-B one-hot bypass to all bias-channel consumers of
  first-step z_world)** is still on the table as a tactical step if V3-EXQ-569a
  FP-2 decision is needed urgently and SD-056 takes longer than expected. The
  SYNTHESIS verdict named (i) as a workaround, not as wrong; it just commits to
  an architecture neither the cerebellar nor prefrontal reference needs.

## Related claims

MECH-094 (call-site scoping via simulation_mode kwarg; substrate-readiness
inherits the existing waking-only call pattern), MECH-256 (single-pass forward-
model comparator family; SD-056 sits at the world_forward training-objective
layer of this family), ARC-033 (E2_harm_s forward model; sibling per-stream
forward predictor, NOT subject to this SD -- z_world is the collapse site),
ARC-062 GAP-B (tactical first-action one-hot bypass on GatedPolicy that SD-056
generalises), MECH-309 (logical-necessity claim for behavioural diversity that
SD-056 unblocks at the substrate level), MECH-314a / MECH-320 / MECH-295 /
SD-033a / SD-033b (downstream bias-channel consumers of `cand_world_summaries`
that recover per-candidate signal once SD-056 lands), V3-EXQ-571 (the
diagnostic that surfaced the collapse), ARC-062 GAP-B autopsy 2026-05-17
(the parallel root-cause analysis).

## References

- Plan-of-record memo: [REE_assembly/evidence/planning/e2_action_divergence_substrate_design.md](../../evidence/planning/e2_action_divergence_substrate_design.md)
- Failure record: [REE_assembly/evidence/planning/v3_exq_571_root_cause_2026-05-25.md](../../evidence/planning/v3_exq_571_root_cause_2026-05-25.md)
- Lit-pull SYNTHESIS: [REE_assembly/evidence/literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md](../../evidence/literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md)
- Behavioural successor plan: [REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md](../../evidence/planning/behavioral_diversity_isolation_plan.md)
