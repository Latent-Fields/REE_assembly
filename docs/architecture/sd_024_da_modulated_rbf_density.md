# SD-024: DA-Modulated RBF Center Density

> Registered: 2026-04-14
> Claims: MECH-232, ARC-057
> Depends on: SD-004, SD-014, ARC-007
> Status: candidate (design doc only, not yet implemented)

## Motivation

ARC-057 proposes that approach behavior emerges from DA-mediated representational
expansion + curiosity drive, without an explicit wanting gradient. The substrate
constraint (see `hippocampal_valence_asymmetry.md`) is that this mechanism
requires an informationally rich environment where expansion captures genuinely
additional information -- which the CausalGridWorld cannot provide.

**The workaround:** fake the information-space expansion inside the hippocampal
module itself. Instead of the environment being richer at reward locations, the
hippocampal RBF layer allocates more representational capacity there. The curiosity
drive sees more internal structure at those locations and follows it -- producing
approach behavior even in a sparse grid world.

This is more biologically faithful than it appears. In the real brain, dopamine
enhances LTP and sharpens place fields. The brain allocates more representational
resources to reward locations regardless of whether the environment "justifies" it.
A rat in a perfectly uniform corridor still gets sharper place fields near the reward
end (Retailleau & Morris 2018).

## Current Architecture

The RBFLayer (`ree_core/residue/field.py`) has:
- **32 centers** (num_basis_functions), allocated by cyclic FIFO
- **Fixed bandwidth** (1.0) -- all centers have uniform Gaussian width
- **No adaptive resolution** -- center allocation is purely sequential
- **4-component valence_vecs** (SD-014) per center: wanting, liking,
  harm_discriminative, surprise

The hippocampal module (`ree_core/hippocampal/module.py`) navigates action-object
space via CEM, scoring trajectories against the residue field. The terrain_prior
network initializes search from [z_world, e1_prior, residue_val, benefit_val].

The existing "dopamine-analog" is `hippocampal.compute_completion_signal()` which
maps trajectory quality to a float in [0.5, 1.0) -- currently used only by the
BetaGate for commitment coupling (ARC-028).

## Proposed Mechanism

### 1. DA-Modulated Center Allocation

When a reward encounter occurs (benefit_exposure > threshold), the DA signal
modulates how many RBF centers are allocated to that region of z_world:

```
# Current: single center per event, FIFO
self.centers[self.next_center_idx] = z_world
self.next_center_idx = (self.next_center_idx + 1) % num_centers

# Proposed: DA-modulated allocation count
n_centers = 1 + int(dopamine_signal * da_allocation_scale)
for i in range(n_centers):
    # Allocate multiple centers in a local neighborhood
    jitter = torch.randn_like(z_world) * da_jitter_radius
    self.centers[self.next_center_idx] = z_world + jitter
    self.next_center_idx = (self.next_center_idx + 1) % num_centers
```

This creates a cluster of closely-spaced centers near reward locations --
higher representational density in those z_world neighborhoods. Harm events
continue to allocate single centers (no DA modulation).

**Key parameters:**
- `da_allocation_scale`: how many extra centers per unit DA signal (default: 2)
- `da_jitter_radius`: spread of the center cluster in z_world (default: 0.1)
- `num_centers` may need increasing from 32 to accommodate expansion (64 or 128)

### 2. DA-Modulated Bandwidth (Optional, Independent)

Narrower bandwidth at DA-modulated centers creates finer spatial discrimination:

```
# Per-center adaptive bandwidth
self.center_bandwidth[idx] = base_bandwidth * (1.0 - dopamine_signal * bandwidth_narrowing)
# DA=0: bandwidth=1.0 (standard), DA=1: bandwidth=0.5 (sharper)
```

This is orthogonal to center density: density gives more centers, bandwidth makes
each center more spatially precise. Both increase the representational resolution
at reward locations. Can be tested independently.

### 3. Curiosity Drive (SD-025)

The curiosity drive biases exploration toward regions of higher representational
density. It operates on the hippocampal map's internal state, not on the
environment directly:

```
# Representational density at current z_world
density = rbf_layer.compute_local_density(z_world)
# = count of active centers within bandwidth radius, weighted by proximity

# Novelty = density-weighted unexplored structure
novelty = density * (1.0 - familiarity)
# familiarity = visit count or EMA of time spent at this z_world region

# Curiosity bonus added to trajectory scoring
curiosity_score = curiosity_weight * novelty
```

The curiosity drive does the same computation everywhere -- but regions with more
centers (DA-expanded) have higher density, so they score higher on novelty *even
if the agent has visited before*, because there are more centers to distinguish
between. The agent keeps finding "new" structure in the expanded region.

### 4. DA Signal Source

The dopamine signal for center allocation should come from the reward encounter
itself (phasic DA), not from E3 precision (which is tonic/sustained):

```
# At benefit contact:
dopamine_signal = benefit_magnitude * drive_level  # SD-012 modulation
residue_field.accumulate_benefit(z_world, benefit_val, dopamine_signal=dopamine_signal)
```

This means:
- Higher drive (hungry agent) -> more DA -> more centers allocated at reward
- Higher benefit (richer reward) -> more DA -> more centers allocated
- Zero drive (sated agent) -> no extra centers -> expansion decays via FIFO

The FIFO decay is critical: old centers get overwritten as new events occur. If the
agent stops encountering reward at a location, the expanded cluster gradually gets
overwritten by centers from other events. The expansion is maintained only as long
as the reward contingency holds -- wanting-as-maintenance.

## Why This Works in a Grid World

The environment doesn't need to contain more information at reward locations. The
hippocampal module creates more internal states at those locations. The curiosity
drive operates on the hippocampal map's internal structure, not on the environment.

From the curiosity drive's perspective, a region with 8 closely-spaced RBF centers
is genuinely more complex than a region with 1 center -- there are more
representational boundaries to explore, more fine-grained distinctions to make.
The fact that these distinctions don't correspond to environmental features is
irrelevant to the mechanism. The agent approaches because its own map is richer
there.

## Informative Failure Modes

### Craving / Addiction Model

If DA-driven over-allocation produces approach toward locations where reward has
been depleted (resource consumed, not yet respawned), that is a model of craving.
The mechanism produces approach even when there is nothing to gain -- because the
representational expansion persists after the reward is gone.

The FIFO decay rate controls the timescale of craving: slow decay = persistent
craving; fast decay = quick extinction. DA magnitude controls intensity.

### Anhedonia Model

If DA signal is suppressed (e.g., ablated or set to 0), no representational
expansion occurs. The curiosity drive treats all locations equally. The agent
wanders without directional preference -- not because it cannot detect reward,
but because its map is uniformly flat. This maps to the motivational deficit
in anhedonia: the reward is there, the agent can perceive it, but the map
doesn't draw it toward it.

### Perseveration

If DA signal is locked high (no decay, no modulation), all visited locations
get expanded and the agent cannot prioritize. The map becomes uniformly dense
and the curiosity drive loses its directional signal. This maps to the
Retailleau & Morris 2018 D1 blockade finding: the map cannot reorient.

## Interaction with Existing Architecture

- **Residue field (harm side)**: unchanged. Harm centers are allocated at
  standard density with standard bandwidth. The asymmetry is preserved.
- **SD-014 valence_vecs**: DA-allocated centers inherit valence vectors from
  the parent event. The wanting component of expanded centers carries the
  reward signal.
- **MECH-094 hypothesis_tag**: DA modulation of center allocation MUST be
  gated by hypothesis_tag. Replay/simulation events do not trigger real DA
  expansion. Only post-commit realized outcomes modulate center density.
- **CEM trajectory scoring**: the curiosity bonus is added to the existing
  terrain_score. High-density regions score better, biasing CEM toward
  trajectories that pass through DA-expanded terrain.
- **ARC-016 precision**: E3 precision (running_variance) is separate from
  RBF spatial precision. E3 precision governs commitment; RBF density
  governs representational richness. These are independent.

## Parameters and Defaults

| Parameter | Default | Meaning |
|-----------|---------|---------|
| `da_allocation_scale` | 2 | extra centers per unit DA (0 = disabled) |
| `da_jitter_radius` | 0.1 | z_world spread of center cluster |
| `num_centers` | 64 | increased from 32 to accommodate expansion |
| `bandwidth_narrowing` | 0.0 | DA-driven bandwidth reduction (0 = disabled) |
| `curiosity_weight` | 0.1 | CEM scoring bonus for representational density |
| `familiarity_ema_alpha` | 0.01 | visit-count EMA decay for novelty computation |

All DA modulation defaults to 0 or no-effect values for backward compatibility.
Existing experiments are unaffected unless DA parameters are explicitly set.

## Test Plan

**Phase 1: Center density alone (no curiosity drive)**
- Enable DA-modulated center allocation at reward contacts
- Measure: center spatial distribution (should cluster at reward locations)
- Measure: does CEM trajectory scoring naturally favor denser regions?
- Baseline: uniform allocation (da_allocation_scale=0)

**Phase 2: Curiosity drive alone (no DA modulation)**
- Enable curiosity bonus in CEM scoring
- Measure: does the agent preferentially explore regions with more centers?
- This tests the drive mechanism independent of the DA expansion

**Phase 3: Combined (ARC-057 test)**
- DA modulation + curiosity drive together
- Measure: does approach behavior emerge toward reward locations?
- Ablation: DA ON + curiosity OFF, DA OFF + curiosity ON, both OFF
- Pass criterion: combined condition shows significantly more approach
  than either alone (interaction effect, not just additive)

**Phase 4: Failure mode characterization**
- Craving test: remove reward, measure persistence of approach
- Anhedonia test: ablate DA signal, measure loss of directional preference
- Perseveration test: lock DA high, measure loss of reorientation
