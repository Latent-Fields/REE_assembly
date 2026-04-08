# Thought Intake: Wanting-Guided Proxy Goals and Schema Binding

**Date:** 2026-04-08
**Raw thought:** `docs/thoughts/2026-04-08_wanting_proxy_goals_schema_binding.md`
**Session context:** Discussion during SD-015 resolution (VALENCE_WANTING gradient in
HippocampalModule._score_trajectory()) led to broader insight about how wanting signal
propagates beyond immediate resource encounters to create emergent multi-level goal hierarchy.

---

## Summary of Insight

Wanting guides approach behaviour (SD-015 resolution). Upon goal achievement, co-active
signals (E1 schemas, z_world waypoints, action-objects) become associated with wanting.
These associations create proxy goals -- intermediate z_world states with acquired wanting
value that enable multi-step planning beyond CEM horizon (~10 steps). Three mechanisms
populate the wanting landscape at different scales: (1) direct contact wanting, (2) E1
schema-conditioned predictive wanting, (3) trajectory-consolidated wanting via reverse replay.
Together they produce an emergent multi-level goal hierarchy from a single VALENCE_WANTING
field without explicit goal-hierarchy design.

---

## Claims Registered

| ID | Title | Type | Phase | Description |
|----|-------|------|-------|-------------|
| INV-065 | proxy_goal_necessity | invariant | -- | Bounded-horizon planner in sparse environment requires proxy goals for multi-step behaviour |
| MECH-216 | e1_predictive_wanting | mechanism | v3 | E1 schema activations seed VALENCE_WANTING before resource contact (Pavlovian conditioned wanting) |
| MECH-217 | temporal_wanting_propagation | mechanism | v3 | Reverse replay spreads wanting backward along approach trajectories during consolidation |
| MECH-218 | interoceptive_predictive_wanting | mechanism | v4 | z_self depletion trend seeds anticipatory homeostatic wanting (requires DR-13) |
| ARC-051 | multi_level_wanting_goal_hierarchy | arch_hypothesis | v3 | SD-014 + MECH-216 + MECH-217 = emergent multi-level goal hierarchy without explicit design |

---

## Dependency Graph

```
INV-065 (proxy_goal_necessity)
  depends: SD-014, SD-015, MECH-216, MECH-217

MECH-216 (e1_predictive_wanting)
  depends: SD-014, SD-018, MECH-203, INV-065
  requires: E1 schema activation readout + threshold-gated wanting seed in SerotoninModule

MECH-217 (temporal_wanting_propagation)
  depends: MECH-165 (reverse replay substrate), SD-014, INV-065
  blocked by: MECH-165 not yet implemented (gap plan exists)

MECH-218 (interoceptive_predictive_wanting)
  depends: SD-012, MECH-203, INV-065
  blocked by: DR-13 (z_self temporal depth) -- V4

ARC-051 (multi_level_wanting_goal_hierarchy)
  depends: SD-014, MECH-216, MECH-217, INV-065, SD-018
  emergent: requires no additional implementation beyond MECH-216 + MECH-217
```

---

## Validation Path

**EXQ-259** (already queued, V3-EXQ-259): Tests Level 1 wanting gradient navigation
(SD-015 resolution). WITH_WANTING vs WITHOUT conditions. Does not test MECH-216/217/218
directly -- those require their substrate implementations first.

**Future experiments needed:**
- MECH-216 validation: requires E1 schema readout + wanting seed implementation, then
  test whether approach behaviour begins before direct resource proximity signal.
- MECH-217 validation: requires MECH-165 (reverse replay) implementation, then test
  whether consolidation spreads wanting backward along approach trajectories and
  improves multi-step resource acquisition.
- ARC-051 validation: ablation study removing MECH-216 or MECH-217 independently,
  measuring multi-step performance degradation at the predicted scale.

---

## Substrate Implementation Notes

- **MECH-216 (V3):** Moderate complexity. Needs E1 hidden state readout mechanism
  (currently implicit in LSTM). Could use a linear projection from E1 hidden state
  to a schema activation scalar, thresholded to gate wanting seeding. Implementation
  site: agent.py waking loop + serotonin.py update_benefit_salience().
- **MECH-217 (V3):** Depends on MECH-165. Implementation plan exists at
  `ree-v3/docs/substrate_plans/mech165_reverse_replay_impl_plan.md`. Wanting spread
  function would be added to HippocampalModule.reverse_replay().
- **MECH-218 (V4):** Gated on DR-13. No V3 path.
