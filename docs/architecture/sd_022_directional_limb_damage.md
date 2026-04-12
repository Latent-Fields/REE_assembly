---
nav_exclude: true
---

# SD-022: Directional Limb Damage (Body Extension)

**Status: IMPLEMENTED 2026-04-09**
**Gap ID:** SD-022-limb-damage
**Depends on:** SD-011

---

## Problem

harm_obs and harm_obs_a were not causally independent. harm_obs_a was a 50-dim EMA of
the same hazard/resource proximity fields as harm_obs -- just with a slower time constant
(alpha=0.05 vs alpha=0.1). EXQ-241b confirmed the ceiling: r2_s_to_a = 0.996 across all
seeds even with the harm_history extension. This is a structural impossibility, not a
calibration failure: both signals derive from the same world-state source.

The A-delta/C-fiber distinction requires harm_obs_a to derive from a BODY STATE causally
independent of current world proximity. C-fibers carry tissue damage state, not
instantaneous proximity. An agent in a safe location with accumulated tissue damage should
have high z_harm_a and near-zero z_harm_s -- a dissociation CausalGridWorldV2 could not
produce with the EMA design.

---

## Implementation

### CausalGridWorldV2

Four directional limbs [N=0, E=1, S=2, W=3], each with independent damage state:

**Damage accumulation (per step, when moving in direction d into hazard):**
```
damage[d] = min(1.0, damage[d] + damage_increment * harm_signal_mag)
```

**Healing (per step, all limbs):**
```
damage *= (1.0 - heal_rate)   # heal_rate=0.002 -> ~500 steps to clear
```

**Movement failure:**
```
P(fail) = damage[d] * failure_prob_scale   # default 0.3
```
On failure: agent position reverted to prev_x, prev_y (step cost still applied).

**Episode reset:** damage reset to zeros on env.reset().

### harm_obs_a re-sourcing

When `limb_damage_enabled=True`, harm_obs_a is derived from damage state (7 dims):
```
[damage[N], damage[E], damage[S], damage[W], max(damage), mean(damage), residual_pain]
```
where `residual_pain = sum(damage) * residual_pain_scale`.

This replaces the 50-dim EMA proximity source. harm_obs_a_dim changes from 50 to 7.

### body_state extension

When `limb_damage_enabled=True` and `use_proxy_fields=True`, body_state grows from
12 to 17 dims:
- [12]: damage[N]
- [13]: damage[E]
- [14]: damage[S]
- [15]: damage[W]
- [16]: residual_pain = sum(damage) * residual_pain_scale

### Config

New `CausalGridWorldV2.__init__` params:
- `limb_damage_enabled: bool = False` -- backward compat default
- `damage_increment: float = 0.15`
- `residual_pain_scale: float = 0.5`
- `failure_prob_scale: float = 0.3`
- `heal_rate: float = 0.002`
- `residual_pain_threshold: float = 0.05`

New `REEConfig.from_dims()` params:
- `limb_damage_enabled: bool = False`
- `damage_increment: float = 0.15`
- `failure_prob_scale: float = 0.3`
- `heal_rate: float = 0.002`

When `limb_damage_enabled=True`: config sets `harm_obs_a_dim=7` in LatentStackConfig.
body_obs_dim is read directly from `env.body_obs_dim` (which returns 17 when enabled).

---

## The Dissociation This Enables

| Condition | Agent location | Limb state | Expected |
|-----------|---------------|------------|----------|
| A (damage residue) | Safe area | damage[d] = 0.8 | z_harm_a high, z_harm_s near zero |
| B (fresh hazard) | Hazard adjacent | damage[d] = 0.0 | z_harm_s high, z_harm_a near zero |

r2_s_to_a should drop from 0.996 to well below 0.5.

---

## Validation

**V3-EXQ-318**: SD-022 limb damage stream separation validation (3 seeds, 2 conditions).
PASS criterion: r2_s_to_a < 0.5 AND harm_obs_a_variance > 0.001 in LIMB_DAMAGE condition.

---

## Biological Basis

C-fiber / paleospinothalamic tract (medial pain system) carries tissue damage state --
accumulated unpleasantness and homeostatic deviation -- distinct from the A-delta lateral
system which carries precise instantaneous nociception (proximity, location, intensity).

Persistent z_harm_a with no current world threat models: hypervigilance, chronic pain,
PTSD (body-state residue persists after the threat is gone).

---

## Files Modified

- `ree-v3/ree_core/environment/causal_grid_world.py` -- limb damage state, step(), _get_observation_dict()
- `ree-v3/ree_core/utils/config.py` -- REEConfig.from_dims() params + harm_obs_a_dim override
- `ree-v3/CLAUDE.md` -- SD-022 implementation entry
- `REE_assembly/docs/claims/claims.yaml` -- SD-022 implementation_note
- `REE_assembly/docs/architecture/sd_022_directional_limb_damage.md` -- this file

---

## Related Claims

SD-011 (dual nociceptive streams), ARC-030 (Go/NoGo symmetry), MECH-112 (wanting/harm
balance), Q-034 (threshold), ARC-052 (precision outputs), SD-023 (world gradient texture).
