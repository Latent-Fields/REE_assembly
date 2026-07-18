---
status: candidate
status_asof: 2026-07-18
status_claim: SD-070
---

# SD-070: latent.zworld_p0_anticollapse_recipe

**Claim ID:** SD-070
**Subject:** latent.zworld_p0_anticollapse_recipe
**Registered:** 2026-07-18
**Depends on:** SD-005 (split encoder), SD-018 (resource proximity head)
**Blocks:** V3-EXQ-783, SD-031 / E2WorldForward P1, and any consumer requiring a trained
z_world encoder (`substrate_queue.json:971`, `ree_core/predictors/e2_world.py:42-54`)

## Problem

The P0 the substrate prescribed for training the z_world encoder -- SD-009 event-contrastive
CE plus SD-018 resource-proximity MSE, applied online at batch=1 -- does not produce a
trained encoder. It **collapses** z_world.

Measured 2026-07-18 on this substrate (world_dim=128, seed 42, 40 eval episodes,
CausalGridWorldV2 at the x724 `ENV_KWARGS` rung, harness
`ree-v3/experiments/v3_exq_783_zworld_granularity_training_crossing.py`):

| configuration | participation ratio | contrast ratio |
|---|---|---|
| untrained | 9.21 | 0.1222 |
| SD-009 + SD-018, lr 1e-4 | **1.06** | 0.0726 |
| SD-009 only (w_018 = 0) | 1.14 | 0.0930 |
| SD-018 only, gentlest (lr 1e-5, w 0.05) | 5.76 | 0.1088 |

A participation ratio of ~1 means z_world has collapsed onto a single effective dimension:
no discriminative geometry at all. Any downstream comparator built on it is vacuous -- the
MECH-353 / V3-EXQ-642 lesson restated. This is what made V3-EXQ-783 unrunnable: its
`D*_TRAINED` arms would have produced a collapsed representation whose (necessarily low)
contrast ratio says "the training recipe destroyed the manifold", not "the dim=32 ceiling
holds", and reading it as an (a1)/(a2) verdict would be exactly the trivial-prediction
signature its readiness assert exists to catch.

### Three measured faults

**1. The SD-009 target is unlearnable from the channel it is wired to.**
`agent.compute_event_contrastive_loss` classifies `transition_type` from z_world alone. But
`transition_type` is a property of the **transition** (t-1 -> t), while z_world is a
**static single-frame** encoding. Probing the label with an identical MLP-128 from each
channel (n=721 steps, held-out macro-recall minus its own chance baseline):

| channel | 3-class map (shipped) | 6-class repaired map |
|---|---|---|
| `world_obs` — what z_world sees | **-0.014** | **-0.060** |
| `body_obs` — what z_self sees | +0.121 | +0.144 |
| world delta (`w_t - w_prev`) | +0.167 | +0.329 |
| **body delta (`b_t - b_prev`)** | **+0.240** | **+0.427** |

The world channel is **at or below chance**. The information lives in the deltas, and mostly
in the *body* delta -- which SD-005's split encoder deliberately routes to z_self, so z_world
structurally cannot see it. This is a wiring fault, not a labelling one: a repaired 6-class
map giving `hazard_approach` and `resource` their own classes (rather than folding both into
class 0, as `agent._EVENT_LABEL_MAP` does) **still sits at chance from `world_obs`**. Class
rebalancing cannot recover information that is not present.

This finding concerns SD-009's own validity and is recorded separately for governance in
[`evidence/planning/sd009_event_contrastive_channel_mismatch_2026-07-18.md`](../../evidence/planning/sd009_event_contrastive_channel_mismatch_2026-07-18.md).
**SD-070 does not adjudicate SD-009.** It routes around it.

**2. Nothing penalises collapse.** Predicting a near-constant class (the shipped map is
~95% class-0 saturated here: measured `c0=0.952, c1=0.046, c2=0.002`) and regressing one
scalar are both served perfectly by a 1-D representation. Variance in any other direction
only adds noise to those two heads, so gradient descent removes it.

The collapse is **not** the multiplicative precision gate, which was the obvious suspect
(`z_world = z_pregate * sigmoid(world_precision_logit)` is a single learnable vector that
could multiplicatively zero 127 of 128 dimensions). Measured across the full P0, the gate's
sigmoid moves only 0.4966-0.5074 and the final layer stays full-rank (singular-value
PR ~55). The encoder's **function** collapses while its weights look healthy --
`PR_pre` 8.6 -> 2.3, `PR_post` 8.7 -> 1.05.

**3. The loop is online at batch=1**, which makes any variance or covariance statistic
undefined -- there is no batch to compute one over.

## Solution

`ree-v3/ree_core/latent/zworld_p0.py`. Four components, each answering one fault:

```
  static scene-structure grounding targets   -> fault 1 (a target the channel determines)
+ class-balanced CE                          -> residual imbalance in those targets
+ VICReg variance/covariance penalty         -> fault 2 (explicit anti-collapse)
+ optional world_obs reconstruction          -> fault 2, structurally: one scalar can be
                                                served by a 1-D code, 275 outputs cannot
+ mini-batching over a rollout buffer        -> fault 3
```

### Grounding targets

Derived from `world_obs` **alone** by `scene_structure_targets()` -- no environment
introspection, so the recipe cannot leak privileged state and has no dependency on env
internals:

- `hazard_present`, `resource_present` — binary, from the 5x5x7 one-hot local view
- `hazard_distance`, `resource_distance` — bucketed Chebyshev distance to the nearest such
  cell, saturating to the last bucket when absent (an absent hazard is *information*, not a
  missing label)

These are decodable, unlike the SD-009 target. Probed from raw `world_obs`: 0.961 / 0.965 /
0.943 / 0.948 balanced accuracy against chance 0.5 / 0.5 / 0.333 / 0.333. They are also the
distinctions SD-009 was reaching for -- harm-relevance in the world channel -- expressed as
targets the observation actually determines, and they are *static single-frame* properties,
which is the right target class for a single-frame encoder.

### Anti-collapse

`variance_covariance_penalty()` returns the two VICReg terms separately, because they do
different jobs and their useful scales differ by more than an order of magnitude:

- **variance term** — `mean(relu(gamma - std_j))`, a floor under every dimension's spread
- **covariance term** — off-diagonal covariance, normalised by dim

The covariance term is the **participation-ratio lever**. The variance hinge alone cannot
raise PR: perfectly correlated dimensions at unit std still occupy one effective dimension
(pinned by contract `test_c4_variance_term_alone_cannot_detect_correlation`). This is why
`covariance_weight` defaults to 50 rather than to VICReg's published ratio, which was
measured here to be far too weak (w_cov=0.04 -> PR 1.80; w_cov=50 -> PR 4.02, same sweep).

### Data flow

```
world_obs -> [buffer] -> world_encoder -> * sigmoid(world_precision_logit) -> z_world_path
                                                    |
              +-------------------+-----------------+----------------+
              |                   |                 |                |
        grounding heads      SD-018 prox head   recon head    var/cov penalty
        (trainer-owned)      (substrate)        (trainer)     (no head)
```

Trains exactly `split_encoder.world_encoder` + `world_precision_logit` -- precisely the
parameter set V3-EXQ-783's weight-delta readiness check watches. Top-down conditioning and
the `alpha_world` temporal smoothing are applied at `sense()` time and carry no P0 gradient,
so they are deliberately outside this path.

### Backward compatibility

**Bit-identical OFF by construction, not by flag.** SD-070 adds no field to
`LatentStackConfig`, no head to `SplitEncoder`, and no method to `REEAgent`. It operates on
an existing `LatentStack` from the outside, and the auxiliary heads belong to the trainer
rather than to the substrate. Nothing runs unless an experiment explicitly constructs a
`ZWorldP0Trainer`, so no existing experiment can change behaviour and **there is no flag
that can be left in the wrong state**. Pinned by contracts C6.

The trainer also must not silently train z_self -- if it did, every downstream self-stream
result run after a P0 would be confounded. Pinned by
`test_c5_trains_world_path_and_leaves_self_path_untouched`.

## Validation

Shipped module at config defaults, world_dim=128, 3 seeds
(`scratchpad/validate_sd070.py`, reproducible from the harness config):

| seed | untrained PR -> trained PR | CR | hazard-presence bal_acc (chance 0.50) |
|---|---|---|---|
| 42 | 9.21 -> 5.19 | 0.122 -> 0.215 | 0.899 |
| 43 | 6.63 -> 5.41 | 0.134 -> 0.251 | 0.786 |
| 44 | 8.56 -> 4.64 | 0.156 -> 0.249 | 0.751 |

Against the V3-EXQ-783 anti-collapse gate, computed exactly as that harness computes it
(mean trained PR / mean dim-matched untrained PR, then the absolute floor):

- `retained_fraction` = 5.079 / 8.132 = **0.625** (needs >= 0.50) — **PASS**
- trained PR absolute = **5.079** (needs >= 2.0) — **PASS**
- contrast ratio raised on **3/3** seeds, mean 0.137 -> 0.238, clearing the untrained
  0.13-0.15 band
- world-path tensors changed 4/4 on every trained arm (readiness check 2 passes)

**Discriminative, not vacuously un-collapsed.** An anti-collapse gate can be satisfied by a
regulariser that holds PR up while the encoder learns nothing, so the trainer always reports
held-out balanced accuracy per grounding head against its own chance baseline. Measured lift
+0.23 to +0.47 across all four heads on all three seeds. A caller reporting PR without these
accuracies cannot distinguish a differentiated representation from a merely un-collapsed one.

Contracts: `ree-v3/tests/contracts/test_sd070_zworld_p0.py`, 31 tests. Full suite 1590 passed.

## Architecture Context

SD-070 is a **training recipe**, not a new latent field or module in the agent loop. It sits
between SD-005 (which defines the split encoder it trains) and SD-031 / E2WorldForward
(which requires a trained z_world before its P1 can mean anything). It supersedes the P0
prescription named in `substrate_queue.json:971` and `e2_world.py:42-54` -- those name
"SD-009 + SD-018" as the P0; fault 1 above shows the SD-009 half cannot work as wired.

Phased training is unchanged and still mandatory: **P0** (this recipe) -> **P1**
(E2WorldForward on stop-gradient z_world, encoder optimiser NOT stepped) -> **P2**
(measurement). Joint training collapses downstream heads (EXQ-166b/c/d).

MECH-094: **not applicable.** This trains an encoder on live observations and writes nothing
to memory during any non-waking state, so no `hypothesis_tag` obligation arises.

## ML/AI engineering notes

VICReg (Bardes, Ponce & LeCun 2022) supplies the variance-hinge + off-diagonal-covariance
form. It is borrowed as **engineering counsel** for a measured failure mode -- representation
collapse under a low-information objective -- and carries no architectural authority here.
Two REE-specific deviations from the standard version, both forced by measurement:

1. **No invariance term / no augmentation pairs.** Standard VICReg is a joint-embedding
   method whose variance and covariance terms regularise an invariance objective over two
   augmented views. There are no augmented views here; the terms are applied directly to a
   supervised objective purely for their anti-collapse property.
2. **Covariance weight ~1000x the published ratio.** Measured, not assumed (see above).

Scale discipline per the REE norm: the encoder remains the existing 2-layer MLP, and every
auxiliary head is a single `nn.Linear`. No capacity was added.

## What This SD Enables

- **V3-EXQ-783** becomes runnable: its `D*_TRAINED` arms now produce a non-collapsed,
  discriminative encoder, so the crossing can actually separate (a1) untrained-encoder from
  (a2) the world_dim=32 granularity ceiling.
- **SD-031 / E2WorldForward P1** gets the trained encoder its design requires instead of the
  vacuous zero comparator a random encoder gives.

## Scope limits

- Measured only at world_dim=128 and 32, on CausalGridWorldV2 at the x724 `ENV_KWARGS` rung,
  under the exploratory epsilon-mixed policy. Behaviour under other rungs is untested.
- The grounding targets are specific to the 5x5x7 local-view layout; an environment with a
  different observation encoding needs its own target derivation.
- Three seeds. Adequate for effects this size (PR 1.06 -> 5.08) but thin for anything finer.
- **Bears on INV-088's ANTECEDENT only.** No bearing on the INV-088 coupling leg
  (V3-EXQ-744a's WEAKENS reading stands), none on MECH-459 / return-scale, and none on
  either leg of the live GOV-FANOUT-1 discrimination (V3-EXQ-780 vs V3-EXQ-781).

## Related Claims

SD-005, SD-009 (routed around; see the governance artifact), SD-018, SD-031, MECH-100,
MECH-353, Q-002, INV-088 (antecedent only).
