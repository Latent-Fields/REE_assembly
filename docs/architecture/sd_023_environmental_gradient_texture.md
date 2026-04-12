---
nav_exclude: true
---

# SD-023: Environmental Gradient Texture (World Extension)

**Status: IMPLEMENTED 2026-04-09**
**Gap ID:** SD-023-env-gradient-texture
**Depends on:** SD-014

---

## Problem

z_world can only encode features that exist in world_obs. CausalGridWorldV2 currently emits two
proximity fields (hazard, resource), making z_world approximately a two-scalar encoding regardless
of encoder expressiveness. This creates a ceiling on all world-model claims:

- **MECH-216 (E1 predictive wanting):** E1 has no leading-indicator signal to predict. At approach
  positions, z_world already contains the resource proximity signal. E1 learns "resource_prox is
  high" not "pattern X predicts upcoming resource contact." EXQ-263a likely produces artifactual
  salience for this reason, not because MECH-216 is wrong.

- **ARC-017 (typed stream separation) / MECH-096 (multimodal fusion):** These claims require z_world
  to encode distinct features for different world content. With only two undifferentiated proximity
  channels the claims are structurally untestable.

- **E1 world model quality generally:** E1's LSTM should build a model of temporal dynamics. With
  two proximity fields as input there are almost no independent dynamics to model.

Root diagnosis note from 2026-04-09: "There are few signals in the world from which to develop
models of what is going on too." -- This is the SD-023 problem.

---

## Design

### Principle: all objects emit, each type distinctively

Every placed object has its own gradient channel in world_obs. This is biologically grounded:
in natural environments all objects have a detectable presence (olfactory, acoustic, visual
texture). Making objects emit creates continuous world texture rather than sparse point sources.

### Object types and gradient channels

Two new landmark types extend world_obs:

| Channel block | Source | Dims | Rationale |
|---|---|---|---|
| hazard_field_view | hazard proximity (existing) | 25 | |
| resource_field_view | resource proximity (existing) | 25 | |
| landmark_a_field_view | Landmark A proximity | 25 | Navigation anchor, no harm/benefit |
| landmark_b_field_view | Landmark B proximity | 25 | Predictive cue -- biased near resources |

world_obs_dim: 250 -> 300 (50 new dims, 2 new 5x5 field channels).

**Landmark A ("pillar"):** Navigation anchor, placed randomly. Strong short-range Gaussian gradient
(sigma=1.5, scale=1.0). No harm, no benefit.

**Landmark B ("trace"):** Predictive resource cue, placed with bias near resource locations
(prob=0.7 within radius 2 of a resource). Weaker medium-range gradient (sigma=2.5, scale=0.6).
This creates the predictive co-occurrence structure for MECH-216: E1 can learn that high
landmark_B field predicts upcoming resource contact because landmark B tends to be near resources.

### Gradient field computation

```python
def _compute_landmark_field(self, positions, sigma, scale):
    field = np.zeros((self.size, self.size), dtype=np.float32)
    two_sigma2 = 2.0 * sigma * sigma
    for lx, ly in positions:
        for x in range(self.size):
            for y in range(self.size):
                d2 = float((x - lx)**2 + (y - ly)**2)
                field[x, y] += scale * float(np.exp(-d2 / two_sigma2))
    return field
```

Fields are static within an episode (landmarks do not move). Recomputed at episode start.
Agent's 5x5 view window extracted identically to existing hazard/resource fields.

### harm_obs stays unchanged

Landmark fields do NOT feed into harm_obs (they are not nociceptive signals).
harm_obs_dim stays 51. Only world_obs grows (250 -> 300 when landmarks enabled).

---

## Implementation

### File: `ree_core/environment/causal_grid_world.py`

New `__init__` params (all default to 0/disabled for backward compatibility):
```python
n_landmarks_a: int = 0,
n_landmarks_b: int = 0,
landmark_a_sigma: float = 1.5,
landmark_a_scale: float = 1.0,
landmark_b_sigma: float = 2.5,
landmark_b_scale: float = 0.6,
landmark_b_resource_bias: float = 0.7,
```

New helper methods:
- `_place_random_landmarks(n, available)` -- random placement from interior cells
- `_place_biased_near_resources(n, bias_prob, radius, available)` -- biased near resources
- `_compute_landmark_field(positions, sigma, scale)` -- Gaussian gradient field

`reset()` additions:
```python
self.landmark_a_positions = self._place_random_landmarks(n_landmarks_a, _interior)
self.landmark_b_positions = self._place_biased_near_resources(
    n_landmarks_b, landmark_b_resource_bias, radius=2, available=_interior)
self._landmark_a_field = self._compute_landmark_field(
    self.landmark_a_positions, landmark_a_sigma, landmark_a_scale)
self._landmark_b_field = self._compute_landmark_field(
    self.landmark_b_positions, landmark_b_sigma, landmark_b_scale)
```

`world_obs_dim` property: returns 300 (not 250) when landmarks enabled.

`_get_observation_dict()`: 5x5 field views extracted and appended to world_parts;
obs_dict keys "landmark_a_field_view" [25] and "landmark_b_field_view" [25] added.

### Config

Landmark params are CausalGridWorldV2 constructor params -- NOT in REEConfig.from_dims().
Experiments that use landmarks must set world_obs_dim=300 explicitly when constructing REEConfig.

### No encoder changes

SplitEncoder (z_world pathway) takes world_obs_dim as a parameter. Extending world_obs from 250
to 300 automatically exposes landmark gradient channels to z_world encoder. No structural changes
to LatentStack, AffectiveHarmEncoder, or E3.

### Backward compatibility

n_landmarks_a=0, n_landmarks_b=0 by default. world_obs_dim stays 250. All existing experiments
unaffected. Landmarks are gradient-only -- no new grid entity type.

---

## Why This Enables MECH-216

Without SD-023:
- Landmark B does not exist
- The only world feature correlated with resource proximity is resource proximity itself
- E1's schema readout learns a redundant function -- "resource_prox is high" != prediction

With SD-023:
- Landmark B fields are elevated for ~2-3 cells around each resource, even outside resource
  proximity radius
- E1's LSTM can learn: "high landmark_B field in recent context predicts upcoming resource contact"
- schema_salience should rise when landmark_B is nearby, BEFORE resource proximity rises
- This is genuinely predictive wanting -- anticipatory, not reactive

---

## ML/AI Engineering Notes

No ML/AI engineering concerns identified. This is a pure environment extension -- no new encoder,
no new training target, no new learning component. The z_world encoder (SplitEncoder) automatically
receives the new channels via world_obs_dim=300. No phased training required.

---

## Validation

Experiment: EXQ-263b (MECH-216 retest with Landmark B as predictive cue).

Acceptance criteria:
- LANDMARK_ENABLED shows salience_at_landmark_b > salience in LANDMARK_ABLATED
- landmark_prox_correlation > resource_prox_correlation in LANDMARK_ENABLED condition

---

## Related Claims

- SD-023: environment.gradient_texture (this SD)
- MECH-216: e1_predictive_wanting (primary beneficiary)
- ARC-017: stream tags (untestable without world texture)
- MECH-096: multimodal exteroceptive fusion (needs distinct world channels)
- MECH-103: multimodal fusion (landmark channels act as additional modalities)
