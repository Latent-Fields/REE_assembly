---
title: "SD-024: DA-Modulated RBF Center Density"
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 14
status: candidate
status_asof: 2026-07-16
status_claim: SD-024
---

# SD-024: DA-Modulated RBF Center Density

> Registered: 2026-04-14
> Claims: MECH-232, ARC-057
> Depends on: SD-004, SD-014, ARC-007
> Status: **IMPLEMENTED** 2026-07-16 (built as the DIAGNOSTIC instrument that
> resolves MECH-232; validation V3-EXQ-766 queued). Design was doc-only 2026-04-14
> -> 2026-07-15. **Live-path producer wired 2026-07-20** -- see the section
> immediately below BEFORE reading the 2026-07-16 status as complete.

## Live-Path Producer (2026-07-20) -- the 2026-07-16 landing had no writer

The 2026-07-16 implementation below is accurate about what it built, and it built
the mechanism correctly. What it did not build was a **caller**.

`ResidueField.accumulate_benefit` -- the sole write path into
`benefit_rbf_field`, and the method this whole SD modulates -- had **no caller
anywhere in `ree_core/`**. Its only two write sites (`field.py:673`, `:682`) are
inside that one method; it was invoked only from `experiments/` scripts and
`tests/contracts/`. `agent.py` called `update_valence`, `accumulate`,
`accumulate_safety` and `evaluate_safety`, never `accumulate_benefit`.

Measured on a real warmup_train loop (darwin-arm64, `curiosity_weight=0.5`) with
BOTH `benefit_terrain_enabled` and `use_da_modulated_rbf_density` True:

- `benefit_rbf_field.active_mask.sum() == 0`, `num_benefit_events == 0.0`;
- `compute_local_density` early-returns zeros on an empty active mask
  (`field.py:273`), so `compute_representational_density` returned exactly `0.0`;
- so `HippocampalModule._curiosity_bonus` computed
  `novelty = density * (1 - familiarity) = 0` and returned `0.0` on all 14432
  live calls, regardless of `curiosity_weight`;
- the `use_curiosity_familiarity` True/False ablation was **bit-identical**,
  confirming familiarity was not the binding constraint;
- hand-populating the terrain with 20 direct `accumulate_benefit` calls made both
  density and the bonus non-zero, isolating the missing producer.

**The SD-025 curiosity drive therefore contributed exactly zero to CEM trajectory
scoring in every live agent run between 2026-07-16 and 2026-07-20.**

**Why the 13 contracts did not catch it.** Every one of them calls
`rf.accumulate_benefit(...)` itself and then asserts on the resulting field. That
is a valid in-vitro validation of the allocation mechanism and it is exactly why a
missing *producer* was invisible: a test that populates the terrain itself cannot
detect that nothing else does. The new contracts
(`tests/contracts/test_sd024_benefit_terrain_live_producer.py`, 7 tests, C1-C6)
assert through the real `REEAgent` API against a real `CausalGridWorldV2` episode
loop and never call `accumulate_benefit` directly.

**The fix.** `REEAgent.update_z_goal` -- the canonical reward-contact hook, which
already carries both ingredients this SD names for the phasic DA signal -- now
calls `accumulate_benefit(z_world, benefit_magnitude=benefit_exposure,
dopamine_signal=benefit_exposure * drive_level)`, gated on
`ResidueConfig.benefit_terrain_live_producer` (default `False`) and a
consummatory threshold `benefit_live_producer_threshold` (default `0.1`).

Three things about that fix are load-bearing and should not be "simplified":

1. **A separate flag, not `benefit_terrain_enabled`.** V3-EXQ-767/767a set
   `benefit_terrain_enabled=True` and populate the terrain themselves via direct
   `rf.accumulate_benefit()` calls (767a lines 236, 238, 305). Reusing that flag
   would silently double-populate those designs on re-run. 767/767a stand as valid
   in-vitro validations of the drive mechanism; they simply never established
   live-path efficacy, and governance owns any re-reading of what they support.
2. **The block precedes `update_z_goal`'s `goal_state is None` guard.** The
   default config has `goal_state = None`. Placed after the guard, the producer
   never runs -- a second instance of the same no-producer defect, for every
   config that runs the curiosity drive without goal seeding. This was caught
   empirically: the block was first written after the guard and contracts
   C2/C4/C5 failed at 0 active centers.
3. **`dopamine_signal` uses base `drive_level`**, not `pacc.effective_drive` nor
   the SD-037 override-amplified value. Those are goal-*seeding* gains; the SD-012
   phasic reward signal this SD consumes is `benefit_magnitude * drive_level`.

**Scope.** No completed run's manifest or evidence direction was altered by this
landing. V3-EXQ-767/767a are NOT invalidated. MECH-314a
(`ree_core/policy/structured_curiosity.py`) is a separate novelty path and is
unaffected.

## Implementation Status (2026-07-16)

Implemented in `ree-v3` as a DIAGNOSTIC substrate -- the instrument that tests
MECH-232's falsifiable prediction, NOT a feature gated behind it. Modulates ONLY
the benefit terrain (`ResidueField.benefit_rbf_field`); the harm and safety RBF
fields keep single-center standard-bandwidth allocation, so the MECH-233 encoding
asymmetry is preserved structurally.

- **`RBFLayer`** (`ree_core/residue/field.py`): optional `per_center_bandwidth`
  buffer (default off -> byte-identical scalar-bandwidth reads); `add_residue_cluster()`
  allocates `n = 1 + int(da_signal * allocation_scale)` jittered centers with
  optional per-center bandwidth narrowing (floored at `0.5 * base`);
  `compute_local_density()` returns a **weight-independent** proximity-weighted
  active-center count.
- **`ResidueField`** (`field.py`): benefit field built with per-center bandwidth +
  optional `da_benefit_num_centers` capacity override when the master switch is on;
  `accumulate_benefit(..., dopamine_signal=)` routes to the cluster path when DA is
  active (MECH-094 `hypothesis_tag` gate inherited -> replay cannot expand);
  `compute_benefit_density()` wrapper.
- **`HippocampalModule`** (`ree_core/hippocampal/module.py`):
  `compute_representational_density()` read-through (the SD-025 curiosity-drive hook).
- **Config** (`ree_core/utils/config.py`, `ResidueConfig`):
  `use_da_modulated_rbf_density` (master, default `False`), `da_allocation_scale`
  (`0.0`), `da_jitter_radius` (`0.1`), `da_bandwidth_narrowing` (`0.0`),
  `da_benefit_num_centers` (`None`). **All defaults no-op -> bit-identical OFF**
  (full `pytest tests/` 1475 passed; 13 SD-024 contracts in
  `tests/contracts/test_sd024_da_modulated_rbf_density.py`).

**The MECH-232 discriminator** (against a valence-tag mechanism): `compute_local_density`
depends only on center positions + active mask + per-center bandwidth, **never on the
RBF weights**. DA-driven multi-center allocation raises density even when the summed
benefit value (`evaluate_benefit`, the weight sum) is held flat -- so approach that
follows density demonstrates approach from representational *quality* alone, not from a
positive-valence gradient. The total `intensity` is split across the cluster so the
weighted benefit value integrates to the same magnitude a single-center allocation
would (the expansion is representational, not a value inflation).

**No phased training** (no new encoder head; allocation logic + a read over an existing
field). **MECH-094**: DA expansion inherits `accumulate_benefit`'s `hypothesis_tag` gate.

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

> **SD-025 Status: IMPLEMENTED 2026-07-16** (ree-v3 `ree_core/hippocampal/curiosity.py`
> `FamiliarityTracker` + `HippocampalModule._curiosity_bonus`/`update_familiarity`).
> Config (`HippocampalConfig`): `curiosity_weight` (master, default `0.0` -> bit-identical
> OFF), `familiarity_ema_alpha` (`0.01`), `use_curiosity_familiarity` (`True`),
> `familiarity_bandwidth` (`1.0`). `_score_trajectory` subtracts
> `curiosity_weight * mean(density * (1 - familiarity))`; density is the SD-024
> weight-independent `compute_representational_density`, familiarity a proximity-weighted
> visit-count EMA raised on WAKING visits only (MECH-094; agent gates on `hypothesis_tag`).
> No phased training (read + EMA state only). 7 contracts in
> `tests/contracts/test_sd025_curiosity_drive.py`; full `pytest tests/` 1488 passed.
> **Scope:** the substrate is buildable on SD-024, but the full ARC-057 ecological
> approach-emergence claim (SD-024 x SD-025 interaction) is ENV-CONSTRAINED (the
> CausalGridWorld cannot test it faithfully -- see the ARC-057 SUBSTRATE CONSTRAINT in
> Motivation above). Validation V3-EXQ-767 is scoped to the DRIVE MECHANISM (does
> curiosity propagate into CEM selection toward higher-density regions? + the familiarity
> anti-perseveration discount), NOT the interaction claim.

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

<a id="curiosity-exploitation-polarity-mech-458"></a>
#### Polarity: an exploitation amplifier, not a diversity generator (MECH-458)

> **MECH-458 (candidate / v3_pending, registered 2026-07-17).** Source of truth:
> [`evidence/planning/curiosity_exploitation_amplifier_reframe_2026-07-17.md`](../../evidence/planning/curiosity_exploitation_amplifier_reframe_2026-07-17.md).
> Evidence anchor: V3-EXQ-767a + V3-EXQ-768a (both cloud PASS, non-degenerate) +
> the re-analysis probe `scratchpad/probe1_sd025_force_decomposition.py`.

The same "does the same computation everywhere" property that makes approach EMERGE
(ARC-057) makes this drive structurally the WRONG force for strategy-diversity
GENERATION. Two cloud PASSes decompose the drive on the identical CEM score-margin
scale (re-analysis, no new compute):

- **767a (map IS reward-shaped):** density-attraction at selection = **39.3** vs the
  familiarity-discount CEILING (after 12 forced visits) = **20.4** (1.93x), and the
  diversity term contributes **0 at the decision point** (familiarity starts at 0).
  The drive's first move is 100% exploitation; its only diversity affordance is a
  lagging, reactive "leave after you've exploited" brake -- Bellemare's proactive
  low-count bonus INVERTED.
- **768a (map is NOT reward-shaped):** SD-025-alone on a flat map = **0** directed
  behaviour. The density-attraction force is 100% parasitic on dopamine (SD-024)
  having already sculpted the map.

**Together:** curiosity pulls only toward structure reward has ALREADY built (a
rich-get-richer loop); it has no proactive pull toward unshaped / under-represented
regions -- exactly the flat-map case where it outputs zero. This under-serves the
stuck v3 mass (conversion_ceiling 0%, competence floor, monostrategy).

**Corollary (the build spec, v3_pending, blocked-on-upstream INV-088):** proactive
strategy-diversity generation requires a SEPARATE **rarity-seeking** drive (Bellemare-2016
polarity: attraction to LOW-count / under-represented strategy classes, independent of
reward-shaping) -- NOT a novelty-MAGNITUDE increase on the existing drive (768a shows
the flat-map arm reads ~0 regardless of weight; the `infant_substrate:GAP-13` lever
cannot help). It is ORDERING-GATED on INV-088 z_world differentiation: a rarity term
over an AUC-0.83 under-differentiated map chases the sparse corner, not diverse
strategies (Stachenfeld 2017; matches the monostrategy plan's differentiate-first
prediction). This hands to `ARC-065 / MECH-314` (`arc_062_rule_apprehension:GAP-H` /
`behavioral_diversity_isolation`) and adds a GENERATION face to the
`conversion_ceiling_campaign` (whose five existing faces are all SELECTION machinery).

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

> NOTE: Phase 3 is the ENV-FREE interaction spike (Test B) -- run on the SD-024 workaround in synthetic RBF/z_world space (see V3-EXQ-768). The env-enabled ECOLOGICAL test (Test C) is a separate, stronger claim deferred to V4 -- routing rationale in evidence/planning/arc_057_ecological_env_decision_2026-07-16.md.

- DA modulation + curiosity drive together
- Measure: does approach behavior emerge toward reward locations?
- Ablation: DA ON + curiosity OFF, DA OFF + curiosity ON, both OFF
- Pass criterion: combined condition shows significantly more approach
  than either alone (interaction effect, not just additive)

**Phase 4: Failure mode characterization**
- Craving test: remove reward, measure persistence of approach
- Anhedonia test: ablate DA signal, measure loss of directional preference
- Perseveration test: lock DA high, measure loss of reorientation
