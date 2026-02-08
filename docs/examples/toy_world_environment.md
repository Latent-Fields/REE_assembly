# Toy World Environment

**Claim Type:** implementation_note  
**Scope:** Toy world environment contract  
**Depends On:** IMPL-003  
**Status:** stable  
**Claim ID:** IMPL-011
<a id="impl-011"></a>

---

Source: `docs/processed/legacy_tree/examples/toy_world/environment.md`

# Toy world environment contract (REE-v0)

This is a minimal, reproducible environment contract that supports REE concepts.

## Entities

- Self agent (the REE agent).
- Other agents (at least one) with observable state and damage.
- World resources (energy sources, obstacles).

## Observation vector \(o_t\)

Split into channels:

1. **Exteroception A:** local grid / lidar-like distances.
2. **Exteroception B:** visual-like embedding (synthetic or low-dimensional).
3. **Interoception:**
   - energy level
   - temperature (or analogous load variable)
   - actuator fatigue
4. **Damage / integrity:**
   - self integrity (0–1)
   - recent damage delta
5. **Homeostasis targets:**
   - desired energy band
   - desired temperature band
6. **Other-agent channel:**
   - other position / velocity
   - other integrity
   - other “distress” proxy (e.g., negative integrity delta)

## Actions \(a_t\)

- movement controls
- interaction (help / harm / noop)
- resource consumption

## Ground truth degradation

Define degradation for legacy scoring proxy \(M\) (evaluation-only; not required for E3 selection):

- `degrade_self`: predicted decrease in self integrity or predicted departure from homeostatic band.
- `degrade_other`: predicted decrease in other integrity or predicted departure from other homeostatic band.

## Success criteria

An REE implementation should show:

- persistence: after harming others, later trajectories are repelled from similar states even if reward would be higher
- repair behavior: preference for trajectories that restore integrity/homeostasis of self and others
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-011
- IMPL-003

## References / Source Fragments

- `docs/processed/legacy_tree/examples/toy_world/environment.md`
