---
nav_exclude: true
---

# SD-054: Reef Enrichment Substrate (CausalGridWorldV2 extension)

**Status: IMPLEMENTED 2026-05-04**
**Renamed: 2026-05-08 (was SD-050; collided with the canonical Suffering-Derivative Comparator entry in claims.yaml)**
**Gap ID:** SD-054-reef-enrichment
**Depends on:** none (pure environment substrate)

---

## Problem

Agents trained in CausalGridWorldV2 with a single resource attractor and uniformly-drifting
hazards consistently collapse to a monomodal policy: a single fixed route between corner-adjacent
forage targets. The route is locally optimal under the existing hazard model, but it produces
an environment-event distribution dominated by agent-initiated transitions and a near-zero
rate of independent environment-initiated harm contacts.

This blocks SD-029 (self-attribution comparator) at the measurement level. SD-029's C2 / C3
acceptance criteria require balanced agent-vs-environment event distributions to dissociate
"I caused this" from "the world caused this." A monomodal policy structurally cannot generate
the harm-event types SD-029 needs to measure: there are not enough environment-initiated
contacts in the data stream, and the agent's own contacts are stereotyped to a single route
shape. Every iteration of SD-029 (V3-EXQ-433/433a/433b/470) reclassified `non_contributory`
for this reason rather than for an architectural failure of the comparator itself.

The substrate fix is to enrich the environment so monomodal exploitation is no longer locally
optimal. SD-054 introduces two competing behavioural attractors -- safety-seeking and
foraging -- that together create a two-mode strategy space the agent cannot collapse into
a single fixed route.

---

## Design

### Principle: behavioural partitioning by competing attractors

The biological analog is coral-reef refugia: in marine systems, predator-free patches with
distinct microhabitat structure force fish into context-dependent strategy selection
(shelter-seeking near the reef vs. foraging in open water). Single-template exploitation
breaks down because each strategy is locally optimal in only part of the environment.

In CausalGridWorldV2 this becomes:

| Attractor | Implementation | Effect |
|---|---|---|
| Safety (reef) | Hazard-free cells with a static scent gradient | Pulls a stressed agent toward corner-adjacent shelter |
| Foraging | Existing food spawning + new food-attracted hazard drift | Increases hazard density along agent-food paths |

The two attractors are spatially anti-correlated (reef patches occupy corners; food spawns
elsewhere) so a fixed route cannot satisfy both simultaneously.

### Reef safe zones

Up to six corner-adjacent patch centres are available:
```
(2, 2), (2, sz-3), (sz-3, 2), (sz-3, sz-3),    # four corners
(2, sz//2), (sz-3, sz//2)                      # two mid-edges
```
The first `n_reef_patches` are used. A patch consists of all interior cells within Manhattan
radius `reef_patch_radius` of the centre. Cells in a patch are added to `self._reef_cells`.

**Hazard exclusion.** Reef cells are removed from the spawn pool at reset, so hazards and food
never start inside a reef patch. During `_drift_hazards()`, no hazard may step into a reef
cell -- both toroidal and bounded branches enforce `(nx, ny) not in self._reef_cells`. A
defensive guard in the step harm-resolution path zeroes `harm_signal` if a hazard somehow
ends up colocated with the agent in a reef cell.

**Reef scent gradient.** A static `(sz, sz)` field is precomputed at reset:
```python
field[i, j] = sum_over_reef_cells(exp(-manhattan_distance / reef_scent_sigma))
field /= field.max()
```
The agent sees a 5x5 local view of this field appended to `world_state` whenever
`reef_enabled=True`. The gradient gives the agent a continuous distance-to-shelter signal,
analogous to how SD-023 landmark-B fields give a distance-to-resource signal.

### Food-attracted hazard drift

During `_drift_hazards()`, with probability `hazard_food_attraction` per drifting hazard,
candidate move directions are sorted by Manhattan distance to the nearest food cell rather
than randomly shuffled. The hazard then takes the first valid direction in that ordering.
This is not a single biased step -- it is a deterministic preference for food-ward moves
whenever the gate fires.

The effect is that foraging paths become actively more dangerous over time as hazards
accumulate near food spawns. With reef-zone safety on the same map, the agent must trade
off between "stay in shelter" (no food, no harm) and "go forage" (food, but rising harm
density along the path).

`hazard_food_attraction=0.0` (default) leaves the legacy uniform random walk bit-identical
on every drift step.

### What does NOT change

`harm_obs` is unchanged -- reef cells are not nociceptive signals; they affect the world
observation only.

`harm_obs_dim` stays 51. Only `world_obs_dim` grows: 250 -> 275 when `reef_enabled=True`
(+25 from the 5x5 reef field view). With multi-resource heterogeneity (SD-049) or landmarks
(SD-023) also enabled, the dimensions stack additively.

No encoder changes. SplitEncoder receives the new channels via the larger `world_obs_dim`
exactly as it does for SD-023 landmark fields.

---

## Implementation

### File: `ree_core/environment/causal_grid_world.py`

New `__init__` params (all default to disabled / no-op for backward compatibility):
```python
reef_enabled: bool = False,
n_reef_patches: int = 3,
reef_patch_radius: int = 2,
reef_scent_sigma: float = 2.5,
hazard_food_attraction: float = 0.0,
```

New state and helpers:
- `self._reef_cells: Set[Tuple[int, int]]` (populated by `_place_reef_patches`)
- `self._reef_field: np.ndarray[(sz, sz)]` (static scent gradient, recomputed at reset)
- `_place_reef_patches(available)` -- builds `_reef_cells`, computes the scent field, and
  removes reef cells from the spawn pool

`reset()` calls `_place_reef_patches(available)` before placing hazards / food, so reef cells
are excluded from `available` for the duration of the episode.

`world_obs_dim` property: returns `previous_dim + 25` when `reef_enabled=True`.

`_get_observation_dict()`: 5x5 reef field view extracted from the agent's local window and
appended to `world_state`; obs_dict key `"reef_field_view"` [25] added.

`_drift_hazards()`: food-attraction sort gate before the candidate-direction loop; reef-cell
exclusion in both bounded and toroidal hazard-step branches.

Step harm path: defensive zero of `harm_signal` if `(new_x, new_y) in self._reef_cells`.

### Config

Reef params are CausalGridWorldV2 constructor params -- not in `REEConfig.from_dims()`.
Experiments using the reef substrate must set `world_obs_dim=275` explicitly when
constructing `REEConfig` (or `world_obs_dim=300` when SD-023 landmarks are also on, etc.).

### No agent changes

This is a pure environment extension. No changes to `LatentStack`, `ResidueField`, `BetaGate`,
or any agent-side module. No new training target. No phased-training implications.

### Backward compatibility

`reef_enabled=False` and `hazard_food_attraction=0.0` are defaults. With the flag off:
- `_reef_cells` is empty, `_reef_field` is zeros (or never instantiated)
- `world_obs_dim` returns the legacy 250 (or 300 / 275 + landmarks / 250 + N x 25 for SD-049,
  unchanged from before SD-054)
- `_drift_hazards` behaves bit-identically to the pre-SD-054 random walk -- no extra RNG
  draws when `hazard_food_attraction=0.0`

All existing experiments are unaffected. The bit-identical-OFF property was verified at
substrate-readiness time (V3-EXQ-521).

---

## Why this enables SD-029 measurement

Without SD-054:
- Single attractor (food). Optimal policy is a fixed corner-to-corner shuttle.
- Hazards drift uniformly. Agent-initiated contacts dominate; environment-initiated contacts
  are rare and stereotyped.
- C2 / C3 require contrastive event distributions: "agent caused this harm" vs. "world caused
  this harm". The substrate cannot produce enough variance in the environment-initiated
  category for the comparator to fit.

With SD-054:
- Two attractors with anti-correlated locations. Fixed routes cannot exploit both.
- Hazard drift is biased toward food, so the agent-vs-environment causal landscape is
  non-stationary along forage paths.
- Behaviour partitions into reef-occupancy phases (low-harm, no food) and foraging phases
  (food, rising harm density). Each phase produces a different agent-vs-environment ratio
  in the harm event stream -- the contrast SD-029 needs.

This is why SD-054 is documented as a substrate prerequisite for SD-029, not as a solution
to SD-029. SD-054 produces the data; SD-029 / MECH-256 / MECH-269 still need to do the
attribution work on top of it.

---

## ML/AI engineering notes

No ML/AI engineering concerns. SD-054 is a pure environment extension -- no encoder, no
training target, no new learning component. The z_world encoder (SplitEncoder) receives
the new channels automatically via `world_obs_dim`. No phased training. No gradient flow.
No MECH-094 interaction (env observation stream, not replay content).

The only calibration choice is `reef_scent_sigma` (default 2.5). Larger sigma flattens the
gradient and reduces the safety-cue informativeness; smaller sigma sharpens it and risks
overfitting policy to scent-direct paths. The default matches SD-023 landmark-B sigma so
the two gradient signals are comparable in scale.

---

## Validation

### V3-EXQ-521 -- substrate readiness diagnostic (PASS, 2026-05-04)

7 / 7 acceptance criteria:
- ARM_0 (`reef_enabled=False`): `world_obs_dim=250`, `len(_reef_cells)=0`
- ARM_1 / ARM_2 (`reef_enabled=True`): `world_obs_dim=275`, `len(_reef_cells)=33`
  (12x12 grid, 3 patches at radius 2)
- 0 reef-cell violations across 30 episodes x 200 steps x 3 seeds in ARM_1 / ARM_2
  (no hazard ever entered a reef cell; spawn pool exclusion verified)
- ARM_2 mean food-distance 2.057 vs ARM_0 baseline 3.790 (-46%) -- food-attraction bias
  measurably pulls hazards along forage paths
- Behaviour-distribution entropy not collapsed: ARM_2 = 4.049 >= 0.7 x baseline 4.557 = 3.190
- Agent reef-visits = 1987 across the diagnostic in ARM_1 (reef is reachable and visited
  under uniform exploration)

### V3-EXQ-522 -- monostrategy-breaking behavioural diversity (PASS, 2026-05-05)

Confirmed that agents trained under `reef_enabled=True, hazard_food_attraction=0.7` produce
materially more diverse behaviour distributions than the `reef_enabled=False` baseline:
non-trivial reef-occupancy fraction, periodic reef <-> forage transitions, zone-transition
counts in the tens per episode rather than ~0. ARM_1_reef_food was selected as the canonical
config for downstream experiments (see V3-EXQ-524 fishtank showcase).

---

## Related claims

- **SD-054** -- this SD (env behavioural-diversity substrate)
- **SD-029** -- self-attribution comparator (primary beneficiary; SD-054 unblocks C2 / C3
  measurement, does not implement the comparator itself)
- **MECH-256** -- SD-029 successor mechanism; consumes the same enriched event stream
- **MECH-269** -- regional verisimilitude V_s monostrategy diagnostic; the current
  SD-029 retest blocker is V_s, with SD-054 already in place
- **SD-023** -- environmental gradient texture (parallel substrate enrichment pattern;
  SD-054 reuses the static-field-with-5x5-view design from SD-023 landmarks)
- **SD-049** -- multi-resource heterogeneity (parallel env enrichment; world_obs_dim stacks
  additively with SD-054)

---

## Naming history

The original CLAUDE.md entry (2026-05-04) labelled this substrate SD-050. The canonical
SD-050 in `claims.yaml` is the Suffering-Derivative Comparator. The collision was resolved
on 2026-05-08:
- ree-v3/CLAUDE.md SD-050 reef block renamed to SD-054 (with an inline note)
- 17 experiment scripts swept from `SD-050` to `SD-054` in docstrings, comments, and one
  banner print string (cosmetic only -- the indexer keys on manifest `claim_ids_tested`,
  not stdout or script source)
- SD-051 (Conditioned Safety Store), SD-052 (Contextual Passive Safety Terrain), and
  SD-054 (this entry) registered as proper `claims.yaml` design_decision entries on the
  same date
- SD-053 was left informally reserved for a sustained-drive claim per
  `docs/architecture/sustained_drive_anticipatory_wanting.md`
