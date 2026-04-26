# Ghost Goal Search

**Status:** design sketch  
**Created:** 2026-04-26  
**Scope:** explicit unresolved-goal traces for awake hippocampal search in V3  
**Related claims:** MECH-216, MECH-217, MECH-230, ARC-051, MECH-269, MECH-284, MECH-285, MECH-291, SD-039, MECH-292, MECH-293, ARC-060

## 1. Why this note exists

`ree-v3` already has three important ingredients:

1. A persistent goal latent (`z_goal`) and wanting-related terrain signals.
2. A dual-trace anchor substrate with inactive anchors preserved instead of erased.
3. A staleness readout that says which regions remain epistemically unresolved.

What it does **not** yet have is an explicit representation of "what was still
wanted there" when an anchor becomes inactive or when a path remains blocked.
Current waking search can therefore answer:

- where the current terrain looks good
- where verisimilitude is stale

but it cannot reliably answer:

- which stale regions still correspond to a live but currently blocked goal
- which deferred goals should receive probe budget before random exploration

This note defines the missing layer.

## 2. Existing substrate and current gap

### Present in V3

- `GoalState` gives a recurrent positive attractor in `z_goal` space.
- `VALENCE_WANTING` can bias hippocampal scoring.
- `AnchorSet` preserves active and inactive anchors (`mark_inactive`, not erase).
- `StalenessAccumulator` provides a graded unresolved-region signal.
- `SleepReplaySampler` already draws from active + inactive anchors using staleness.

### Missing in V3

- Anchors preserve `z_world`, but not an explicit goal snapshot.
- There is no ranked bank of unresolved or deferred goals.
- Waking `propose_trajectories()` does not seed from inactive/high-wanting/high-
  staleness anchors.
- Between ticks, `generate_trajectories()` mostly reuses cached candidates
  instead of running cheap probe refreshes around unresolved goals.

## 3. Core proposal

Add an explicit **ghost-goal layer** on top of the existing wanting and anchor
substrates.

The term "ghost goal" means:

- a goal that is still motivationally live
- but is not currently executable through the active plan
- and therefore survives as a preserved unresolved trace rather than as the
  current committed trajectory

This is not a replacement for ARC-051's emergent wanting hierarchy. It is a
complement to it. ARC-051 says that wanting can emerge as a multi-scale field.
The ghost-goal layer adds a discrete memory of unresolved goal traces when a
continuous field is too lossy.

## 4. New claim stack

### SD-039: anchor goal snapshot payload

When anchors are written, remapped, or invalidated, they should preserve not
just `z_world` but also a compact "what was being wanted here" payload:

- `z_goal_snapshot`
- `wanting_strength`
- `arousal_tag`
- optional `last_vs` / `staleness_at_write`
- cause tag: `boundary`, `reset`, `blocked`, `goal_relocated`

Without this payload, staleness only says "this region is unresolved", not
"this unresolved region still matches a live goal".

### MECH-292: ghost-goal bank

Inactive or strained anchors with preserved goal payloads are ranked into a
bank of unresolved goals. This bank is not the same as the replay sampler's
broad pool:

- the broad pool is about seed eligibility
- the ghost bank is about motivational relevance under current goals

The bank should rank by something like:

`ghost_priority ~ wanting x goal_match x staleness x recoverability`

where:

- `wanting` says how motivationally live the trace was
- `goal_match` compares current `z_goal` to stored `z_goal_snapshot`
- `staleness` says the region remains unresolved
- `recoverability` prevents rumination on hopeless regions

### MECH-293: awake ghost-centered probe search

Waking hippocampal search should allocate a minority proposal budget to top
ghost-goal traces. This means:

- not pure current-anchor CEM only
- not pure random noise probing
- but a mixed proposal policy that can revisit blocked/deferred goals

The probe channel remains MECH-094-tagged and should not update the viability
map until realized validation.

### ARC-060: explicit unresolved-goal hierarchy

A good agent needs both:

- the continuous wanting landscape of ARC-051
- a discrete bank of unresolved goal traces

The first supports smooth navigation over known gradients. The second preserves
goals that remain important even when local gradients collapse.

## 5. Data model

### 5.1 Anchor payload extension

Suggested extension to `Anchor`:

```python
@dataclass
class GhostGoalPayload:
    z_goal_snapshot: Optional[torch.Tensor]
    wanting_strength: float
    arousal_tag: float
    last_vs: float
    staleness_at_write: float
    cause: str
    tick_written: int

@dataclass
class Anchor:
    ...
    ghost_payload: Optional[GhostGoalPayload] = None
```

### 5.2 Ranked ghost-goal view

Suggested derived view in `HippocampalModule`:

```python
@dataclass
class GhostGoalRef:
    anchor_key: AnchorKey
    z_world_anchor: torch.Tensor
    z_goal_snapshot: Optional[torch.Tensor]
    wanting_strength: float
    arousal_tag: float
    staleness: float
    goal_match: float
    recoverability: float
    priority: float
```

This view can be rebuilt on demand from `AnchorSet + StalenessAccumulator +
GoalState`; it does not need to be a separately persisted store on day one.

## 6. Search policy

### 6.1 Proposal mixture

At each waking E3 tick, split candidate budget into:

- `base_current`: proposals from current terrain prior
- `ghost_probe`: proposals seeded from top ghost-goal anchors
- `novelty_tail`: small residual random or anti-recency exploration budget

Initial conservative default:

- `base_current = 0.70`
- `ghost_probe = 0.20`
- `novelty_tail = 0.10`

Later, replace fixed fractions with a dynamic `ghost_pressure` gate.

### 6.2 Ghost priority

Recommended first-pass scoring:

```python
goal_match = cosine(curr_z_goal, ghost.z_goal_snapshot).clamp(min=0.0)
recoverability = sigmoid(a0 + a1 * ghost.last_vs - a2 * ghost.staleness)
priority = (
    ghost.wanting_strength
    * max(goal_match, eps)
    * math.sqrt(max(ghost.staleness, eps))
    * max(recoverability, eps)
)
```

Important constraint: do **not** reward low `V_s` alone. Otherwise the system
will ruminate over incoherent traces instead of probing recoverable blocked
goals.

### 6.3 Between-ticks micro-search

Current `generate_trajectories()` returns cached candidates between E3 ticks.
The minimal extension is:

- if `ghost_pressure <= threshold`: keep current cache behavior
- if `ghost_pressure > threshold`: refresh only the ghost-probe slice of the
  cache with a tiny budget

This preserves MECH-090 commitment stability while allowing unresolved goals to
stay computationally live between full replans.

## 7. Implementation order

### Phase 1: preserve goal identity

Files:

- `ree-v3/ree_core/hippocampal/anchor_set.py`
- `ree-v3/ree_core/hippocampal/module.py`
- `ree-v3/ree_core/agent.py`

Tasks:

- add goal payload fields to anchors
- snapshot current `z_goal`, wanting, and arousal on anchor writes/remaps
- expose a `build_ghost_goal_refs()` helper

This is SD-039 only. No search behavior changes yet.

### Phase 2: rank unresolved goals

Files:

- `ree-v3/ree_core/hippocampal/module.py`
- `ree-v3/ree_core/utils/config.py`

Tasks:

- compute `goal_match`, `recoverability`, and `priority`
- add diagnostics:
  - `n_ghost_candidates`
  - `mean_ghost_priority`
  - `top_ghost_goal_match`
  - `top_ghost_staleness`

This is MECH-292.

### Phase 3: wake-time probe budget

Files:

- `ree-v3/ree_core/hippocampal/module.py`
- `ree-v3/ree_core/agent.py`
- `ree-v3/ree_core/utils/config.py`

Tasks:

- add ghost-seeded proposal branch to `propose_trajectories()`
- add budget split config
- ensure ghost probes carry strengthened hypothesis tagging

This is MECH-293.

### Phase 4: between-ticks micro-refresh

Files:

- `ree-v3/ree_core/agent.py`

Tasks:

- permit tiny ghost-only refresh between full E3 ticks when ghost pressure is high
- preserve current default when feature flags are off

This is still MECH-293, but should land after the full-tick path is stable.

### Phase 5: downstream consumers

Not first-pass critical, but high leverage later:

- BLA retrieval bias can up-rank emotionally tagged ghost goals
- sleep replay can use goal payloads in addition to staleness
- self-model writeback can mark certain ghost goals resolved or obsolete

## 8. Falsifiable predictions

### Primary

In a blocked-goal or relocated-reward environment, ghost-goal search should:

- increase proposals concentrated on the previously wanted path
- shorten recovery latency after path invalidation
- avoid pure monostrategy lock better than current-anchor-only search

### Secondary

Compared with flat random probes, ghost probes should show:

- higher goal-match with current `z_goal`
- higher realized recovery yield
- lower wasted probes into fully incoherent stale regions

### Failure mode

If ghost-goal search only increases revisitation of impossible regions, then the
recoverability term is wrong and the system is implementing rumination, not good
planning.

## 9. Recommended experiment stack

1. **Payload diagnostic**
   Show that blocked/replaced anchors retain `z_goal_snapshot` and non-zero
   wanting.
2. **Ranking diagnostic**
   Inactive anchors associated with current goals rank above unrelated stale
   anchors.
3. **Probe-allocation ablation**
   Compare current-only vs current+ghost vs current+random-probe.
4. **Recovery task**
   Reward relocation or blocked corridor task with recovery-latency and
   strategy-diversity metrics.
5. **Rumination guardrail**
   Environment with permanently impossible decoys to ensure recoverability gate
   suppresses hopeless probes.

## 10. Short recommendation

The right next stack is:

1. SD-039 first
2. MECH-292 second
3. MECH-293 third
4. only then consider sleep-side goal-aware replay refinements

The decisive architectural point is simple: `ree-v3` already knows how to mark
regions as unresolved, but it does not yet preserve which unresolved regions
still correspond to a live goal. That is the exact gap this stack closes.
