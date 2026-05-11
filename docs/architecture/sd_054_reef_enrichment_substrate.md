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

## Design hypothesis vs. observed outcome

**Design hypothesis (what SD-054 was supposed to enable).** Without SD-054 the only attractor
is food, and the optimal policy is a fixed corner-to-corner shuttle. With SD-054 the
environment carries two anti-correlated attractors (reef safety, food); a policy that
discriminates threat-context from safe-context can occupy both, producing a contrastive
agent-vs-environment harm-event distribution -- the data SD-029 / MECH-256 need for C2 / C3
calibration.

**What the substrate actually delivered.** Under a hand-coded reef-aware avoidance heuristic
(EXQ-522 ARM_1: "if hazard within 2 cells and reef available -> flee to reef; else -> forage")
the substrate produces ~50/50 reef/forage occupancy, ~49 zone transitions per episode, and a
materially different position-entropy profile from the reef_disabled baseline. This is the
substrate-ceiling demonstration: **given a discriminative policy**, SD-054 carries the
intended behaviour into the data stream.

**What the substrate did not deliver.** Under trained REE policy (the same E3 + E1 + LatentStack
substrate that EXQ-522's heuristic replaces), every SD-029 retest on SD-054 substrate has
returned `non_contributory` for the same reason:

| Run | Outcome | Direction | Diagnosis |
|---|---|---|---|
| EXQ-523 | n/a | non_contributory | Undertrained: r2=0.57 < 0.9 graduation gate |
| EXQ-523a | INCONCLUSIVE_UNDERTRAINED | non_contributory | Same |
| EXQ-523b (x2) | INCONCLUSIVE_UNDERTRAINED | non_contributory | Same |
| EXQ-433e | FAIL | non_contributory | Insufficient agent-caused trials |
| EXQ-433f | FAIL | non_contributory | C0 trials-sufficient gate FAILed in 3/4 seeds (agent_caused_trials: 15/7/20/3 vs target 20). Same monomodal V_s monostrategy substrate-ceiling pattern as 433/433d |

The trained agent does not adopt a discriminative reef-vs-forage policy. It stays monomodal
under gradient descent on a single-policy parameterisation, even with the reef substrate
present. The behavioural-diversity ceiling that the heuristic in EXQ-522 reaches is not
reached by the trained policy. The contrastive harm-event distribution SD-029 needs is
therefore not produced under current REE training.

**Diagnosis (registered as MECH-309).** The gap between EXQ-522 (heuristic, diverse) and
EXQ-433e/f / 523-series (trained, monomodal) is the size of an absent rule-apprehension
capacity at the policy layer. Bayesian / gradient-style updaters revise weights over a
hypothesis space they do not invent; without a non-Bayesian rule-creator that proposes
discriminative policy modes ("near-hazard -> reef regime; else -> forage regime"), the
trainer collapses to the smoothest single policy that is good-enough across the whole
state space. Monomodal collapse on this substrate is the equilibrium output of the
present architecture, not a failure of training. EXQ-522's hand-coded heuristic externalises
the missing apprehension layer; this is why it works where the trained agent does not.

**What this means for SD-054.** The SD is necessary substrate for behavioural diversity --
the heuristic-policy upper bound proves the environment can carry the split. It is not
sufficient under current REE training. The proximate next-stage blocker is the
rule-apprehension layer (registered as ARC-062 / ARC-063), with MECH-269 V_s monostrategy
as a representational precondition. SD-054 substrate-readiness is delivered (V3-EXQ-521,
V3-EXQ-522 PASS); SD-054's **purpose claim** -- that the substrate unblocks SD-029
measurement under trained policy -- is not. The latter is recorded as v3_pending until
the rule-apprehension layer (weak reading first; strong reading deferred to V4) is built
and re-tested.

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

### V3-EXQ-522 -- substrate-ceiling demonstration via heuristic policy (PASS, 2026-05-05)

**Important framing.** EXQ-522 used a hand-coded reef-aware avoidance heuristic
([v3_exq_522_reef_monostrategy_break.py:65](../../ree-v3/experiments/v3_exq_522_reef_monostrategy_break.py))
as the policy under test, not a trained REE agent. The heuristic is:
```
if hazard within FLEE_THRESHOLD cells AND reef cells available:
    move toward nearest reef cell
else:
    move toward nearest food
```
Under this heuristic, ARM_1 (`reef_enabled=True, hazard_food_attraction=0.7`) produces
~50/50 reef/forage occupancy, ~49 zone transitions per episode, and a materially different
position-entropy profile from ARM_0 (`reef_enabled=False`). This demonstrates that **the
substrate can carry diverse behaviour given a discriminative policy** -- it is the substrate
ceiling. ARM_1_reef_food was selected as the canonical reef config for downstream experiments
(see V3-EXQ-524 fishtank showcase).

EXQ-522 is silent on whether trained REE agents reach this ceiling. They do not (see below).

### Trained-agent retests on SD-054 substrate (FAIL / non_contributory)

V3-EXQ-433e, V3-EXQ-433f, V3-EXQ-523, V3-EXQ-523a, V3-EXQ-523b: all trained-agent SD-029
retests on the reef substrate (often combined with hazard_food_attraction>0) returned
`non_contributory` for the same diagnostic reason -- monomodal V_s monostrategy substrate-
ceiling pattern; insufficient agent-caused trials for C2 / C3 calibration. The substrate
was present and validated; the trained policy did not exploit the structural opportunity
the substrate offered.

This is the empirical foundation for MECH-309 (monomodal-collapse-as-equilibrium-without-
rule-apprehender). The substrate is necessary; the rule-apprehension layer (ARC-062 weak
reading, ARC-063 strong reading) is the next-stage architectural commitment that needs to
land before SD-054's purpose-claim can be re-tested.

---

## Related claims

- **SD-054** -- this SD (env behavioural-diversity substrate; substrate-readiness PASS,
  purpose-claim v3_pending under trained policy)
- **MECH-309** -- monomodal-collapse-as-equilibrium-without-rule-apprehender; the diagnosis
  that explains the EXQ-433e/f and 523-series non_contributory pattern
- **ARC-062** -- rule-apprehension architectural slot, weak reading (gated-policy
  architecture; V3 first pass)
- **ARC-063** -- rule-apprehension architectural slot, strong reading (distributed
  CandidateRule field with tolerance-gated availability and evidence-trace records;
  implementation_phase=v4 deferred flag)
- **SD-029** -- self-attribution comparator (primary downstream beneficiary; SD-054 +
  rule-apprehension layer together are the prerequisites for SD-029 C2 / C3 measurement,
  not SD-054 alone)
- **MECH-256** -- SD-029 successor mechanism; consumes the same enriched event stream
- **MECH-269** -- regional verisimilitude V_s monostrategy diagnostic; representational
  precondition for ARC-062 / ARC-063 (you cannot apprehend a rule about a region you
  cannot represent as discriminably different from another region)
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

---

## Bipartite layout extension (2026-05-11)

**Status: IMPLEMENTED 2026-05-11**

The legacy SD-054 corner-placement is a weak geometric expression of the
behavioural-diversity claim: reef patches sit in fixed corners, but the
agent, hazards, and food spawn at uniformly-random positions in the
remaining cells. Per-episode reef-vs-food geometry is randomised, and the
mean optimal policy across episodes converges to a single direction-following
template ("head toward nearest food") that works regardless of the specific
reef-vs-food layout. The claim that "two competing attractors create a
two-mode strategy space" is true under a discriminative policy (V3-EXQ-522
heuristic, PASS) but the legacy geometry does not create the structural
pressure that a trained REE policy would need to discover the discrimination
on its own.

The bipartite-layout extension is the sharper geometric expression of the
same claim. It does not change SD-054's semantics, dependencies, or
v3_pending status. It is a substrate-refinement that creates the
structural condition under which a well-trained ARC-062 substrate would
produce per-candidate first-action argmax diversity at typical training
probe states.

### Motivation

The 2026-05-11 diagnose-errors session on V3-EXQ-543b (TASK_CLAIMS
`diagnose-v3-exq-543c-2026-05-11T0635Z`) ran a direct numerical probe
against the legacy SD-054 substrate and recorded:

- 8 CEM candidates from `agent.generate_trajectories(latent, e1_prior, ticks)`
  at init all share `argmax(first_action)` = 3
- Continuous first-action vectors differ by ~1e-4 max across candidates
- `world_states[1]` (first POST-action predicted z_world per candidate)
  differs by ~1.2e-5 max across candidates; grows to ~2.8e-3 by t=30
- The ARC-062 head's input (per-candidate z_world summary) is therefore
  near-constant in K, gated_score_bias varies by ~4e-7 across K, TV
  distance vs bypass-uniform is ~9e-8 -- below the V3-EXQ-543b inert-gating
  threshold of 0.05

The diagnosis: the substrate-readiness premise of V3-EXQ-543b was violated
upstream of the ARC-062 head, by the CEM proposer producing near-degenerate
candidate batches. The legacy SD-054 substrate does not exert geometric
pressure that would force a trained CEM proposer to emit diverse
first-action argmaxes. See
`evidence/planning/arc_062_rule_apprehension_plan.md` decision-log entry
2026-05-11 for the three architectural options surfaced; this extension
implements option 3a (env-side diversification).

### Design

Three new `CausalGridWorldV2.__init__` kwargs (env-only, NOT surfaced
through `REEConfig.from_dims` -- matches SD-022 / SD-023 / SD-029 / SD-047 /
SD-048 / SD-054 precedent for env-only SDs). All defaults preserve
bit-identical legacy SD-054 behaviour:

```python
reef_bipartite_layout: bool = False,        # master switch
reef_bipartite_axis: str = "horizontal",    # or "vertical"
reef_bipartite_agent_band_radius: int = 1,  # 0 = midline-only; 1 = midline +/- 1
```

When `reef_bipartite_layout=True`:

| Region | Cells (axis="horizontal", radius=r) | Cells (axis="vertical", radius=r) |
|---|---|---|
| Reef half | rows in `(midline + r, sz - 2]` | cols in `(midline + r, sz - 2]` |
| Agent band | rows in `[midline - r, midline + r]` | cols in `[midline - r, midline + r]` |
| Forage half | rows in `[1, midline - r)` | cols in `[1, midline - r)` |

Reef patches are placed along the reef-half edge (`row = sz - 3` for
horizontal, `col = sz - 3` for vertical) with the remaining axis centres
evenly distributed across the interior. Patches that would intersect the
agent band or forage half are clipped by the `_is_in_reef_half(i, j)`
predicate before being added to `self._reef_cells`. The reef scent field is
computed identically to the legacy helper.

The agent always spawns in the agent band; hazards, resources, and
waypoints always spawn in the forage half. Cells in the reef half that are
not reef cells are intentionally unused (the reef half is reef-exclusive).
On a 12x12 grid with `n_reef_patches=3`, `reef_patch_radius=2`,
`agent_band_radius=1`, the typical layout has ~28 reef cells (rows 8-10),
4 agent-band rows used out of 3 (rows 5-7 minus any walls), and ~32
forage-half cells (rows 1-4 minus reefs and walls).

### Action-axis correspondence

For axis="horizontal" with `CausalGridWorldV2.ACTIONS = {0: (-1, 0), 1: (1, 0),
2: (0, -1), 3: (0, 1), 4: (0, 0)}`:

- Reef approach (toward bottom): `action 1` ("down", row +1)
- Forage approach (toward top): `action 0` ("up", row -1)

These are categorically opposite action argmaxes. A candidate pool that
includes both reef-mode and forage-mode trajectories MUST have at least
two distinct first-action argmaxes -- there is no policy that gets both
modes via the same first action under this geometry.

### Reset partitioning

`reset()` branches at the reef-placement step:

```python
if self.reef_enabled:
    if self.reef_bipartite_layout:
        self._place_reef_patches_bipartite()       # does NOT consume `available`
        agent_pool, forage_pool = self._build_bipartite_pools(available)
    else:
        self._place_reef_patches(available)        # legacy: removes reef cells
        agent_pool = forage_pool = available       # aliased single list
else:
    self._reef_cells = set()
    agent_pool = forage_pool = available

ax, ay = agent_pool.pop()                          # agent spawn
# hazards, resources, waypoints pop from forage_pool
```

Legacy mode aliases the two pools to the same `available` list so
`pop()`-from-shared-pool semantics are preserved bit-identically. Bipartite
mode uses two disjoint pools that are independently shuffled by `self._rng`
inside `_build_bipartite_pools`.

### Fallback under degenerate configs

If `agent_pool` would be empty after partitioning (e.g., `agent_band_radius=0`
on a grid where the midline is mostly walls or already reef cells), the
band is widened iteratively by +1 radius until a valid cell exists. The
widen count is recorded in `self._sd054_bipartite_band_widen_count` (0 in
legacy mode and in successful bipartite resets) for diagnostic surfacing.
If `forage_pool` is empty, it falls back to `agent_pool` so `hazards.pop()`
does not crash; the substrate-readiness diagnostic will catch this via low
forage-pool cell counts.

### What does NOT change

`world_obs_dim` is unchanged (still 275 with `reef_enabled=True`, +25 from
the static reef scent field view). No new observation channels. No new
encoder. No new training target. `harm_obs` is unaffected. The `step()`
movement, hazard, and resource-consumption logic is unchanged. The legacy
`hazard_food_attraction` knob continues to work in both modes -- with the
bipartite layout, hazards in the forage half drift toward food (also in
the forage half), so the forage path becomes actively dangerous over time
in exactly the way it does under the legacy layout.

### Backward compatibility

`reef_bipartite_layout=False` (default) preserves bit-identical legacy
SD-054 behaviour: `_place_reef_patches` (corner pattern) is called,
`available` is partitioned to remove reef cells but is otherwise a single
shared pool, and all entities pop from it. RNG draws are unchanged because
`_build_bipartite_pools` is not invoked. Bit-identical-OFF verified at
smoke-test time 2026-05-11 (reef_cells count 33, world_obs_dim 275,
band_widen_count 0 across seeds 0/1/2/42).

### Validation

V3-EXQ-548 substrate-readiness diagnostic to be queued via `/queue-experiment`
immediately following this implementation. Acceptance criteria (proposed):

- C0 backward-compat: `reef_bipartite_layout=False` reproduces V3-EXQ-521
  baseline (reef_cells=33, world_obs_dim=275, band_widen=0)
- C1 structural partition: with bipartite ON across 3 seeds, all reef cells
  are in rows > midline + radius; all hazards / resources / waypoints in
  rows < midline - radius; agent_pos always in midline +/- radius
- C2 first-action argmax entropy: at probe states sampled from a 40-episode
  P0 warmup, mean per-state argmax entropy across K=8 CEM candidates is
  >= 1.5x the ARM_0 (legacy) baseline value. ARM_0 baseline expected ~0
  (smoke-test value 0); ARM_1 expected >= 0.3 (i.e., at least one probe
  state of 32 produces 2+ distinct argmaxes)
- C3 reef-vs-forage signal: at agent-midline probe states with hazard
  pressure present, the per-candidate first-action argmax distribution
  contains both `0` (forage / up) and `1` (reef / down) in at least 30%
  of probe states (the structural-readiness threshold)

Acceptance is structural-only in this pass (`experiment_purpose=diagnostic`).
A full-pipeline rerun of V3-EXQ-543b/c (with bipartite ON in 543b's env
kwargs) is deferred until V3-EXQ-548 PASS confirms the env-side fix
sufficient.

### Related claims

- SD-054 (this SD; substrate-readiness PASS, purpose-claim v3_pending still
  applies until the rule-apprehension layer lands and is re-tested on the
  enriched substrate)
- MECH-309 (logical-necessity monomodal-collapse claim; the substrate
  enables a sharper falsifier but the architectural claim is unchanged)
- ARC-062 (Phase 2 GAP-B downstream consumer; this extension creates the
  structural conditions under which the GAP-B falsifier becomes testable)
- arc_062_rule_apprehension_plan.md GAP-B (status `blocked`; resume
  condition is V3-EXQ-548 PASS)
- SD-023 / SD-047 / SD-048 / SD-049 (parallel env-only substrate-enrichment
  pattern -- env-only kwargs, no REEConfig.from_dims surfacing)
- MECH-094 (not applicable -- env observation stream, not replay content)
