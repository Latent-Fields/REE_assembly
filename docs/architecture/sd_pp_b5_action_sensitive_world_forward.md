---
title: "SD-PP-B5: Action-Sensitive world_forward + Action-Sensitivity Readiness Gate"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 11
status: IMPLEMENTED
status_asof: 2026-09-22
status_claim: SD-PP-B5
---

# SD-PP-B5: Action-Sensitive world_forward + Action-Sensitivity Readiness Gate

**Claim ID:** SD-PP-B5-z-world-per-step-displacement-range
**Subject:** predictors.e2_fast.world_forward_action_sensitivity
**Status:** IMPLEMENTED (2026-09-22; validation experiment pending)
**Registered:** 2026-09-22
**Depends on:** SD-005 (self/world latent split), SD-013 (interventional training, IMPLEMENTED
2026-04-10), SD-031 (E2_world comparator, IMPLEMENTED 2026-06-06)
**Blocks:** MECH-573 (readability gate), MECH-574 (novel-target arm), INV-063; widens MECH-572
**Build authorisation:** USER DECISION 2026-09-22T19:01:39Z at the `failure_autopsy_V3-EXQ-1073`
Step 8 gate -- "Confirm, but escalate B5 to a build now".

## Problem

`E2FastPredictor.world_forward` -- the head every consolidation experiment on the z_world stream
actually trains -- **does not read its action**. Measured on V3-EXQ-1073, seeds 42/123/456, after
3600 recon-only P0 steps reaching `conv_rel_drop` 0.997-0.999:

| Readout | Seed 42 | Seed 123 | Seed 456 | Needed |
|---|---|---|---|---|
| skill vs identity predictor (MECH-573) | -0.071 | +0.227 | -0.007 | > 0 on >= 2/3 |
| inverted-action battery MSE / original | 0.760 | 0.901 | 0.881 | > 1 for a contradiction |
| cond-3 waking PE / converged residual (G9) | 0.745 | 0.677 | 0.674 | > 2.0 |
| early surprise fraction (G4b) | 0.033 | -- | -- | >= 0.5 |

The inverted-action-map battery is **easier** than the rule the head was trained on, on all three
seeds. An action-map inversion is therefore not a contradiction, and no anti-self-sealing or
reopening test can be posed on this head at all -- which is what blocked V3-EXQ-1073's condition 3
(`confidently_wrong_condition_unposeable_on_this_head`).

The mechanism is structural, not a training-budget shortfall. `world_forward` is a residual head
(`z + delta`, `e2_fast.py:129-137`) whose action enters through a single `world_action_encoder`
linear layer. On CausalGridWorldV2 a one-cell move compresses to `identity_predictor_mse ~1e-5`, so
driving `delta -> 0` scores well against the reconstruction objective and the action encoder
receives almost no gradient. The head converges to copy-the-input and the convergence metric
(`conv_rel_drop`, normalised by the RANDOM-INIT battery) cannot see it.

## Solution

Two pieces. Neither changes any default.

### 1. Action-sensitivity readiness gate (instrument)

`experiments/_lib/action_sensitivity_gate.py` -- a reusable helper so any consolidation experiment
can assert *from measured output* that its head reads its action, BEFORE posing a contradiction.

This gate was pre-specified and never built: SD-031's own Validation Experiment P1 requires an
"Identity-collapse check: r2 on action-shuffled control must drop substantially" (2026-04-18).
`_identity_predictor_mse` currently exists only as copy-pasted private functions in
`v3_exq_1063` and `v3_exq_1073`; this promotes it to shared code.

Surface: `identity_predictor_mse()`, `skill_vs_identity()`, `action_sensitivity_ratio()`,
`readiness_verdict()`.

**This is a NEGATIVE INSTRUMENT** (CLAUDE.md "Negative instruments"): it authorises *starting* a
consolidation experiment on the strength of a negative ("no action-blindness found"). A broken
search would destroy its numerator and denominator together and read as "ready". It therefore
carries all three remedies, strongest first:

1. an explicit `cannot_determine` **category** in the verdict dataclass -- structural, so it
   survives refactoring and propagates into `--json`, rather than a print an edit can drop;
2. a known-baseline **canary** pinning V3-EXQ-1073's measured values, the only remedy of the three
   that catches a *partially* broken gate;
3. a printed pre-filter **denominator** (battery size, distinct-action count).

### 2. Action-margin loss on `world_forward` (remedy)

Port SD-013's contrastive interventional loss to `E2FastPredictor`:

```
loss_margin = max(0, margin - ||world_forward(z, a_actual) - world_forward(z, a_cf)||_2)
```

Zero gradient once the two predictions are already `>= margin` apart; positive gradient when the
head is action-invariant. Added to the P0 reconstruction objective at
`world_interventional_fraction` of steps.

**Why the margin form and not SD-056's InfoNCE form.** SD-056 already provides an
action-divergence auxiliary on this exact head (`world_forward_contrastive_loss`,
`e2_fast.py:279`). V3-EXQ-1073 deliberately omits it, citing it as "a CONFIRMED P0 destabiliser
(V3-EXQ-701b ablation, carried by 798a)". An always-on InfoNCE term competes with the
reconstruction objective throughout training; the margin loss goes silent the moment the head is
separated enough, so it cannot dominate. This is the same reasoning SD-013 applied on `e2_harm_s`
and SD-031 named for this head in 2026-04 ("Margin loss forcing ||E2_world(z_world, a_i) -
E2_world(z_world, a_j)|| >= margin for a_i != a_j is the standard extension").

**Why not just use `E2WorldForward`.** `e2_world.py:319` already has this loss, but
`E2WorldForward.__init__` hard-asserts `world_dim >= 128` (SD-031's carry-forward guard) and
V3-EXQ-1073 runs `WORLD_DIM = 16`. It is not constructible at this operating point.

### Config params (E2Config) -- all no-op

| Param | Type | Default | Purpose |
|---|---|---|---|
| `use_world_interventional` | bool | `False` | master switch |
| `world_interventional_fraction` | float | `0.3` | fraction of P0 steps adding the term |
| `world_interventional_margin` | float | `0.1` | L2 separation margin |

Threaded through all THREE config sites (dataclass field, `from_dims()` signature, post-`cls()`
re-apply). `from_dims` silently swallows unknown kwargs -- MECH-307 shipped with only the first
site and 84 drivers ran the feature OFF believing it on.

## Architecture Context

A training-procedure extension to the existing `E2FastPredictor.world_forward`, not a new module
-- the same relationship SD-013 has to ARC-033. The head, its callers and the SD-003/SD-031
attribution pipeline are unchanged.

Phased training (unchanged from SD-013 / SD-031):
- **P0** z_world encoder warmup.
- **P1** `world_forward` trains on frozen z_world (`.detach()`), standard MSE + margin term.
- **P2** evaluation; the readiness gate runs here and at P1 exit.

**MECH-094:** not applicable -- waking forward model, not replay content.

## What This Enables

- **MECH-573** becomes runnable: its CONFIRMING needs skill-vs-identity on the same frozen battery
  in the same no-grad evaluation, which is the gate's contract.
- **MECH-574** becomes posable: its novel-target arm presupposes a head that can be contradicted.
- **INV-063** inherits both.
- **MECH-572** is already runnable without B5 (readable-seed step-scale ladder); B5 widens the
  readable region rather than unblocking it.

## Validation

Ablation pair at matched budget, feature ON vs OFF, seeds 42/123/456, on the V3-EXQ-1073 operating
point. Acceptance criteria are V3-EXQ-1073's own failure numbers:

- `action_sensitivity_ratio > 1.0` on >= 2/3 seeds (measured 0.760/0.901/0.881 OFF);
- `skill_vs_identity > 0` on >= 2/3 seeds (measured -0.071/+0.227/-0.007 OFF);
- `conv_rel_drop` not materially degraded against the OFF arm -- the remedy must not buy
  action-sensitivity by destroying reconstruction (the 701b failure mode).

If the gate still fails with the margin loss ON, the remaining route is the encoder/displacement
one (SD-018-amend resource-field supervision, SD-009 event-contrastive, SD-106 world-encoder skip)
and it is registered as its own substrate entry rather than built here -- per the user's scope
decision 2026-09-22.

## Related Claims

- MECH-572, MECH-573, MECH-574, INV-063 (unblocked / widened)
- SD-013 (reference implementation, `e2_harm_s`), SD-031 (reference implementation, `e2_world`;
  named this remedy for this head), SD-056 (the InfoNCE form deliberately not used)
- SD-PP-1..4 (precision-provenance substrate, waiting on this)
