# Wanting Guides Approach, Achievement Binds Schema: Proxy Goals and Multi-Level Planning

**Date:** 2026-04-08
**Session:** wanting-gradient-nav + thought-intake
**Context:** Arose during discussion of SD-015 resolution (VALENCE_WANTING gradient in
_score_trajectory()) and the broader question of how the wanting signal propagates beyond
immediate resource encounters.

---

## The Core Insight

Wanting guides approach behaviour. The VALENCE_WANTING landscape in the residue field
provides directional pull toward resource-proximal z_world regions -- this is what
SD-015 resolved. But the conversation opened a deeper question: what happens *after*
the approach succeeds?

When the agent reaches the resource, it doesn't just consume it. It achieves a goal.
And in achieving it, various signals, schemas, and gradients that were active during
the approach become associated with what wanting gets trained on -- the resource
encounter itself.

So: the approach trajectory is now associatively linked to the resource's wanting
signal. The schema slots that predicted the resource (E1 predictive patterns), the
z_world states along the path, the action-objects used to navigate -- all of these
co-occur with the wanting peak.

What can this association *do*?

1. **E1 schema slots that reliably predict resource encounter start seeding
VALENCE_WANTING before contact.** If E1 has a schema that fires whenever certain
environmental features precede resource proximity, that schema activation can
populate wanting at the *current* z_world position, not just at the resource
location. This is E1 doing something Pavlovian: conditioned wanting, where the CS
(schema-activating feature) seeds the same wanting signal as the UCS (resource
contact). The hippocampus then navigates toward z_world regions where E1 schemas
associated with resource-prediction are active -- not just where resources have
previously been directly encountered.

2. **These E1-activated wanting seeds can act as proxy goals.** A proxy goal is a
z_world state that acquires wanting value through association, not through direct
hedonic experience. The landscape becomes multi-layered: raw resource positions
(SD-018 / MECH-203 wanting), plus E1-schema-mediated wanting at correlated but
distinct positions. Crucially, proxy goals can be further from the current position
than the direct resource encounter, enabling multi-step planning beyond the CEM
horizon (~10 steps).

3. **Temporal propagation via reverse replay.** MECH-165 reverse replay spreads
activation backward along approach trajectories during consolidation. This means
wanting doesn't just accumulate at the resource -- it propagates back along
the path taken to reach it. Waypoints acquire wanting signal. These waypoints
are now plannable-to. The hippocampus can navigate toward a waypoint (which is
within CEM horizon) that was previously a step en route to a resource, effectively
extending reachable planning depth beyond the single-step horizon.

4. **Interoceptive anticipatory wanting.** When z_self depletion is trending
(energy falling before drive_level becomes acute), the depletion trend is itself
a predictive signal. If E2's self-model carries temporal depth, it can project
forward and seed anticipatory homeostatic wanting -- wanting that fires before
the deficit is critical, not just reactively. This is the difference between
seeking food when hungry versus seeking food when the trajectory toward hunger
is established. This requires DR-13 (z_self temporal depth) and is V4.

---

## The Multi-Level Goal Hierarchy That Emerges

This is not a designed hierarchy -- it is an *emergent* hierarchy from the same
VALENCE_WANTING field, populated by three increasingly indirect sources:

- **Level 1:** Direct resource encounters (SD-018 + MECH-203 benefit_salience).
  Wanting is seeded at the exact z_world of resource contact. Short-range, precise.

- **Level 2:** E1 schema-conditioned predictive wanting (MECH-216 proposed).
  Wanting is seeded at z_world states where E1 schemas associated with resource
  prediction are active. Medium-range -- as far as E1's predictive reach extends.
  These are proto-proxy-goals: not the resource, but reliably predictive of it.

- **Level 3:** Trajectory-consolidated wanting (MECH-217 proposed, requires MECH-165).
  Wanting is propagated backward along previously successful approach trajectories
  via reverse replay. Long-range -- the entire approach path acquires wanting signal,
  enabling multi-step navigation from any waypoint.

- **Level 4 (V4):** Interoceptive anticipatory wanting (MECH-218 proposed, requires DR-13).
  Wanting is seeded by projected future self-state depletion, not by past resource
  proximity. Requires temporal self-model in z_self domain.

All four levels feed the same VALENCE_WANTING dimension. The CEM scorer doesn't
know which layer it's responding to -- it just prefers trajectories through
high-wanting regions. The multi-step planning capability emerges from the fact that
wanting-rich waypoints now exist at all distances, not just at the resource.

---

## The Proxy Goal Claim (INV-065)

For goal pursuit beyond the CEM planning horizon (~10 steps), the architecture
requires intermediate wanting-rich states that can serve as sub-goals. Without these,
the CEM can only plan toward resource regions it can reach within 10 steps. In
sparse or large environments, genuine multi-step goals require proxy goals -- intermediate
states that have acquired wanting value through schema binding or trajectory
consolidation. This is an invariant of the architecture, not a design choice:
any agent architecture with bounded planning horizon and a sparse reward landscape
will require proxy goals to exhibit multi-step goal-directed behavior.

---

## The Schema Binding Loop

The full loop:

```
resource encounter
  -> VALENCE_WANTING peaks at z_world(resource)
  -> E1 schema active during approach: schema-to-resource association forms
  -> E1 schema activation now seeds VALENCE_WANTING at approach z_world states
  -> hippocampus navigates toward high-wanting regions
  -> agent reaches schema-activating state (proxy goal achieved)
  -> continues to resource
```

And with consolidation:

```
sleep / SWS consolidation
  -> MECH-165 reverse replay: approach trajectory replayed in reverse
  -> VALENCE_WANTING propagated backward along trajectory
  -> waypoints at t-1, t-2, t-3, ... acquire wanting signal
  -> multi-step wanting landscape established
```

The proxy goals are not pre-specified. They are whatever z_world states the agent
has previously passed through on the way to resource encounters, after consolidation
has had a chance to spread the wanting signal backward. The architecture produces
goal hierarchies automatically from experience.

---

## Connection to Claims Already in Registry

- **MECH-165 (reverse replay):** The backward temporal propagation mechanism.
  Currently a substrate gap (not implemented). MECH-217 proposes a specific
  wanting-propagation function for it.

- **MECH-121 (SWR consolidation):** The full consolidation pipeline is V4.
  MECH-217 is a narrower claim: the replay-based backward wanting spread.

- **SD-018 (resource proximity head):** Ensures z_world encodes resource geography.
  This is the prerequisite for Level 1 wanting. MECH-216 extends it to Level 2
  via E1 schema conditioning.

- **INV-034 (goal maintenance necessary for ethical agency):** Multi-level goal
  hierarchy is part of what makes goal maintenance meaningful across time.

- **ARC-031 (z_self trajectory navigation, V4):** The interoceptive predictive
  wanting (MECH-218) is parallel to ARC-031 in the z_self domain.

---

## Open Questions

1. Can E1 schema seeding of VALENCE_WANTING be implemented within V3 substrate
   without major new architecture? (Schema slots are implicit in E1's LSTM hidden
   state -- would need an explicit read mechanism to query schema activation.)

2. Is temporal wanting propagation via reverse replay (MECH-217) separable from
   full MECH-165 implementation, or does it require the full diverse replay machinery?

3. At what density of proxy goals does the wanting landscape become too saturated
   to carry directional information? (The gradient is only useful if there are
   high- and low-wanting regions to distinguish.)

4. Does the proxy goal mechanism require novelty detection to know when a new
   schema association is worth forming, or does it form continuously?

---

## Why This Matters for the Architecture

The practical implication is that wanting-guided navigation (SD-015 resolution)
is not just a short-range local gradient but the substrate for an emergent
multi-scale goal architecture. The CEM planner, hippocampal navigation, E1 schema
conditioning, and offline consolidation together produce a system that can pursue
goals across time without any explicit goal-hierarchy design. This is an invariant
prediction about any architecture with these components, and a strong argument
that the REE architecture is sufficient for multi-step goal-directed behavior
without introducing a separate goal-planning subsystem.
