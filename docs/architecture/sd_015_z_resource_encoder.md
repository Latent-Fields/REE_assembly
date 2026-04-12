---
nav_exclude: true
---

# SD-015: Dedicated z_resource Encoder for Goal-Directed Navigation

**Claim ID:** SD-015  
**Subject:** goal_representation.z_resource_encoder  
**Status:** IMPLEMENTED 2026-04-10  
**Registered:** (pre-existing)  
**Depends on:** SD-012, MECH-112, SD-005  
**Blocks:** MECH-112 validation experiments (z_resource seeding for goal-directed navigation)

---

## Problem

EXQ-085f/085g/085l/085o established that seeding z_goal from z_world at resource contact
does not produce a goal representation that guides navigation toward resources.

Root cause: z_world at contact encodes the full scene (agent position, hazards, resource
positions) rather than isolating resource-specific features. Resources respawn at random
locations after collection, so z_world at the contact moment has no predictive value for
future resource locations.

The SD-018 resource_proximity_head is a scalar head on z_world — also position-confounded.
Neither gives the goal system what it needs: "what kind of resource to seek," not "where
the resource was."

---

## Solution

A dedicated `ResourceEncoder(world_obs -> z_resource)` extracts object-type features
from raw world_obs, independent of z_world encoding. z_goal is seeded from z_resource
(not z_world) when `use_resource_encoder=True`.

### Architecture

```
world_obs -> Linear(world_obs_dim, 64) -> ReLU -> Linear(64, z_resource_dim) -> z_resource
z_resource -> Linear(z_resource_dim, 1) -> Sigmoid -> resource_prox_pred_r  [aux supervision]
```

ResourceEncoder is entirely separate from SplitEncoder's z_world path — no shared weights,
no shared gradients. z_resource is supervised by `benefit_exposure` (same signal as SD-018)
but through its own encoder parameters.

### Config params (LatentStackConfig)

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `use_resource_encoder` | bool | `False` | master switch |
| `z_resource_dim` | int | `32` | matches GoalConfig.goal_dim for direct seeding |

### New agent method: `compute_resource_encoder_loss()`

```
compute_resource_encoder_loss(resource_proximity_target, latent_state) -> loss
```

MSE between `resource_prox_pred_r` and `max(resource_field_view)`. Backpropagates
through ResourceEncoder only — not through z_world.

### Goal seeding change (agent.update_z_goal())

When `use_resource_encoder=True` and `z_resource` is available: seed z_goal from
`z_resource` instead of `z_world`. Falls back to `z_world` if not enabled.

---

## Architecture Context

Parallel to SD-011 harm stream separation: just as z_harm_s was separated from z_world to
enable forward prediction (ARC-033), z_resource is separated from z_world to enable
goal seeding that generalises across resource locations.

SD-015 resolves the MECH-112 bottleneck: E3 receives z_goal that encodes "what the resource
was" (object-type) rather than "where it was" (position-confounded z_world).

---

## What This SD Enables

- MECH-112 validation experiments (z_goal seeded from z_resource → navigation lift)
- SD-015 queue entry (substrate_queue.json) unblocked once MECH-112 resolves
- benefit_ratio > 0.5 experiments now have a structurally correct seeding pathway

---

## Biological Grounding

Ventral visual stream (IT cortex): encodes object identity independent of spatial position
(DiCarlo & Cox 2007 — untangled representation). Hippocampal place cells bind context
(where) with object identity (what). Goal-directed approach requires a "what-to-seek" signal,
not a "where-it-was" signal.

---

## Phased Training (recommended)

P0: Train ResourceEncoder on benefit_exposure supervision (compute_resource_encoder_loss).
P1: Enable goal seeding from z_resource (update_z_goal uses z_resource).
P2: Measure goal_resource_r_enc and benefit_ratio.

---

## Related Claims

- SD-015 (goal_representation.z_resource_encoder)
- MECH-112 (drive.goal_state_attractor)
- SD-012 (goal.homeostatic_drive_modulation)
- SD-018 (encoder.resource_proximity_supervision — scalar head on z_world, distinct)
- ARC-030 (benefit_eval_head)
