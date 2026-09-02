---
title: "SD-018: Resource Proximity Supervision (+ directional-field amend)"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 18
status: implemented
status_asof: 2026-09-02
status_claim: SD-018
---

# SD-018: encoder.resource_proximity_supervision

**Claim ID:** SD-018
**Subject:** encoder.resource_proximity_supervision (amend: encoder.resource_field_supervision)
**Status:** IMPLEMENTED (scalar head 2026-04-07; directional-field amend 2026-09-02, validation owed)
**Registered:** 2026-04-06 (entry); this doc written 2026-09-02 (the entry carried `design_doc: null`)
**Depends on:** SD-005 (split encoder), SD-009 (event-contrastive supervision, the harm-side analog)
**Blocks:** SD-015 z_resource pipeline, ARC-030 benefit terrain, MECH-117 wanting/liking approach,
the EXQ-085h..o goal-directed cluster; since 2026-08-25 also MECH-457 / ARC-065 / INV-088 via the
observation-interface gate (`conversion_ceiling_root`, H-observation-interface).

## Problem

z_world is trained only on the E1 world-model prediction loss, which is invariant to resource
saliency: a resource does not change the sensory scene unless contacted. EXQ-085m (2026-04-06)
measured `benefit_eval_r2 = -0.004` -- z_world orthogonal to resource proximity -- so the whole
benefit/goal pathway (benefit_eval_head, goal_proximity, z_goal seeding, drive modulation)
operated on noise.

**The 2026-08-25 sharpening (V3-EXQ-948, confirmed, red-teamed).** With the scalar head from the
original SD-018 already active in the shared x734/737/808/948 base config, a PPO reader of
z_world alone forages 0.5 res/ep against the 1.0 D3 competence floor, while the same reader given
z_world + the full 25-dim agent-centred `resource_field_view` clears the floor on 3/3 seeds
(2.23 res/ep). That field is `world_obs[225:250]` -- it is already inside z_world's own input.
A scalar `max(resource_field_view)` target supervises magnitude only; it cannot tell a policy
which way to move. Foraging needs the directional gradient, which z_world discards.

## Solution

### Original (2026-04-07): scalar proximity head
`SplitEncoder.resource_proximity_head = Linear(world_dim, 1) + Sigmoid`, MSE against
`max(resource_field_view)`, backprop into the world encoder. Config
`LatentStackConfig.use_resource_proximity_head` (False) / `resource_proximity_weight` (0.5).
Agent loss `REEAgent.compute_resource_proximity_loss`. P0 leg `ZWorldP0Config.proximity_weight`.

### Amend (2026-09-02): directional resource-field head
Generalise the target from 1 to 25 dims -- shape (a) of the two the 948 autopsy admitted; shape
(b), routing the raw field as an explicit side-channel past z_world to every consumer, is the
fallback if (a)'s validation nulls (it has a large blast radius on every `world_dim` consumer and
bypasses the interface that E1/E2 rollouts must carry direction through).

| Param | Type | Default | Where |
|---|---|---|---|
| `use_resource_field_head` | bool | False | LatentStackConfig (+ both `from_dims` sites) |
| `resource_field_weight` | float | 0.5 | LatentStackConfig -- online P1 loss weight |
| `resource_field_dim` | int | 25 | LatentStackConfig |
| `resource_field_weight` | float | 0.0 | ZWorldP0Config -- P0 leg, off by default |

- `SplitEncoder.resource_field_head = Linear(world_dim, 25) + Sigmoid` (field is max-normalised,
  values in [0,1]); `SplitEncoder.RESOURCE_FIELD_SLICE = slice(225, 250)`, mirrored by
  `zworld_p0.RESOURCE_FIELD_SLICE`, both contract-pinned to the `CausalGridWorldV2`
  `use_proxy_fields=True` layout.
- `LatentState.resource_field_pred` [batch, 25], None when off.
- `REEAgent.compute_resource_field_loss(resource_field_target, latent_state)` -> MSE; zero-with-grad
  when off; ValueError on a width mismatch. Pass the LatentState returned by `sense()` (not the
  detached `_current_latent`), exactly as for the scalar loss.
- `ZWorldP0Trainer`: the target is `world_obs[RESOURCE_FIELD_SLICE]` from the buffered
  observations themselves (no `observe()` change); the leg runs only when the stack has the head,
  `resource_field_weight > 0`, and the buffered obs is wide enough; stats gain
  `used_resource_field_head` and a held-out `resource_field_holdout` {mse, mean_predictor_mse, r2}.

Data flow: `world_obs[225:250]` (target) -> `resource_field_head(z_world)` -> MSE -> backprop into
`world_encoder`. Nothing downstream reads the prediction; the effect is on z_world itself.

Backward compatibility: bit-identical OFF (same-seed `sense()` hash and state-dict keys identical
to HEAD before the amend). Phased training required (P0 warmup with the leg on, P1 detached heads).
MECH-094: N/A. ML note: auxiliary-task supervision; the hazard is a 25-dim target dominating P0 and
collapsing z_world onto the field -- mitigated by P0's VICReg variance/covariance terms and the
reconstruction head; report participation ratio + held-out accuracies.

## Failure record (what "working" must look like)
- EXQ-085m: `benefit_eval_r2 = -0.004` (pre-SD-018 baseline).
- EXQ-257: the scalar head's r2>0.5 validation, confounded by z_goal seeding collapse on 2/3
  seeds (seed 3: r2 = 0.998); autopsied 2026-08-08 as precondition_unmet.
- **V3-EXQ-948 (the amend's motivating FAIL target):** `ppo_ree_latent` 0.5 res/ep vs 1.0 floor;
  `ppo_latent_plus_localfield` 2.23, 3/3 seeds. A working amend must let a z_world-only reader
  clear the 1.0 floor on a strict seed majority.

## Validation (owed; design for /queue-experiment)
948-shape diagnostic: shared P0 warmup (`ZWorldP0Config.resource_field_weight > 0` on the ON
arm), arms = field head OFF vs ON (scalar head on in both, matching the x734 family base config),
PPO reader of z_world alone; DV res/ep against the 1.0 D3 floor on a strict seed majority; held-out
linear decode of `resource_field_view` from z_world (r2) as the mechanism check; claim read-across
INV-088 + MECH-457; `experiment_purpose: diagnostic`. If it nulls, build shape (b).

## Related
V3-EXQ-948 / V3-EXQ-813, `failure_autopsy_V3-EXQ-948_2026-08-25`, GFLAG-0114,
`cross_plan_root_cause_synthesis_20260902.md`, SD-009, SD-015, SD-070 (P0 recipe), INV-088,
MECH-457, ARC-065. Contracts: `ree-v3/tests/contracts/test_sd018_resource_field_head.py`.
