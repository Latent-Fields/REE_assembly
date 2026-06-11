---
closure_plan:
  id: deferred_by_commitment
  generation: deferred
  title: "Deferred-by-Commitment (parking lot + reversal triggers)"
  registered: 2026-06-11
  last_updated: 2026-06-11
  scope_claims: [ARC-053, ARC-054, ARC-055, MECH-225, MECH-226, MECH-227, MECH-228, MECH-270, ARC-084]
  sibling_plans: []
  roadmap_note: >
    NOT a version tier and NOT a closure map. This is the parking lot for work
    that is DELIBERATELY held -- a reversible architectural commitment, not an
    omission. Each node is a substrate the project chose NOT to build, with the
    explicit condition that would pull it back into scope written into its
    readiness_gate as the REVERSAL TRIGGER. generation: deferred keeps these out
    of every generation percentage (V3 closure and the V4/V5/V6 roadmaps);
    all nodes are status: deferred (weight excluded). The point is visibility:
    the map is the durable resume primitive, so the "what would un-defer this"
    condition belongs ON the map, not only in a boundary doc. A node leaves this
    plan by being promoted into its real generation tier when its trigger fires.
  nodes:
    - id: "deferred_by_commitment:DEF-1"
      title: "Temporal Coherence Loop substrate (ARC-053/054/055 phase-coherent V(t))"
      phase: 1
      status: deferred
      severity: high
      owner_exq: null
      unblocks_claims: [ARC-053, ARC-054, ARC-055]
      depends_on: []
      cross_plan_link: []
      blocking_on: "Held by architectural commitment: V3 substitutes a synaptic approximation (MECH-269 per-region V_s scalar; D_V temporal-depth) for phase-coherent V(t). The full oscillator/TCL infrastructure (inferior olive + cerebellum + thalamus + pacing) is NOT built."
      readiness_gate:
        - "REVERSAL TRIGGER 1: a V3 working-model failure mode the synaptic forms demonstrably cannot represent (governance must articulate WHY a synaptic approximation could not have produced the missing signal)"
        - "REVERSAL TRIGGER 2: an EXQ FAIL whose diagnostic narrows to 'missing phase variable' (distinct from 'missing substrate')"
        - "REVERSAL TRIGGER 3: multi-agent V3 work is attempted (not currently planned) -- would promote ARC-054 multi-agent extension"
        - "REVERSAL TRIGGER 4: an external constraint (clinical use case / third-party comparison) requires biological-substrate fidelity (a goal-posts shift, framed as such, not a substrate discovery)"
        - "NON-TRIGGER: 'phase/ephaptic coupling is biologically real and REE lacks it' -- true but is the entire point of the boundary; the criterion is FUNCTIONAL INSUFFICIENCY, not biological completeness"
      last_updated: 2026-06-11
      completion_note: "Authoritative disposition: docs/architecture/v3_v4_phase_substrate_boundary.md 'When to revisit (revocation conditions)'. NOTE phase-tag drift: ARC-053/ARC-054 currently read implementation_phase: v3 in claims.yaml while this doc treats the cluster as v4-deferred -- reconcile in the held-reassignment batch (the v4_planning_index already flags this produces misleading hold_pending_v3_substrate recs)."
    - id: "deferred_by_commitment:DEF-2"
      title: "Oscillatory multiplexing + ephaptic coherence mechanisms (MECH-225/226/227/228/270)"
      phase: 1
      status: deferred
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-225, MECH-226, MECH-227, MECH-228, MECH-270]
      depends_on: ["deferred_by_commitment:DEF-1"]
      cross_plan_link: []
      blocking_on: "Held by architectural commitment: oscillatory multiplexing (gamma/theta/beta/delta), TCL biophysics, anaesthesia model, ephaptic (field) coupling, and the ephaptic V_s substrate all require the oscillator infrastructure DEF-1 lacks; V3 substitutes synaptic approximations."
      readiness_gate:
        - "REVERSAL TRIGGER (concrete, from the boundary doc): if the MECH-271 routing audit cannot distinguish a SUBSTRATE-level confabulation from a TAG-LOSS confabulation without phase-channel information, MECH-228 ephaptic gets promoted"
        - "Otherwise inherits DEF-1's four triggers (these mechanisms ARE the TCL substrate)"
        - "Continuous-ephaptic-broadcast soft path already partially probed by MECH-287b (parallel session) on top of the MECH-287 binary trigger -- watch whether that forces the full substrate"
      last_updated: 2026-06-11
      completion_note: "Same authoritative doc as DEF-1. MECH-270 currently reads implementation_phase: v3 (drift, same note as DEF-1)."
    - id: "deferred_by_commitment:DEF-3"
      title: "Explicit signed competitive multi-field coupling (ARC-084)"
      phase: 2
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: [ARC-084]
      depends_on: []
      cross_plan_link: []
      blocking_on: "substrate_conditional: V3 has no explicit multi-field signed-edge layer to ablate, so a cooperative-only vs cooperative+signed-competitive probe TODAY would be vacuous. Wait for the V4 substrate."
      readiness_gate:
        - "REVERSAL TRIGGER: a V4 multi-field signed-edge layer exists, making the cooperative-only vs cooperative+long-range-competitive ablation (Luppi et al. 2026) non-vacuous"
        - "DISTINGUISH two non-equivalent failure axes -- do NOT conflate: (a) runaway POSITIVE coupling / hypersync (this claim's target: feedback entrapment, shared-delusional coupling, over-stabilised attractor MECH-076); (b) MONOSTRATEGY / regime-collapse (MECH-309, owned by ARC-062/063) -- the OPPOSITE pole. Signed-coupling damping addresses (a); the rule-apprehension layer addresses (b)"
      last_updated: 2026-06-11
      completion_note: "Disposition recorded in claims.yaml ARC-084 (epistemic_category substrate_conditional, implementation_phase v4). V4/V5; off the V3 critical path. DO NOT build in V3."
    - id: "deferred_by_commitment:DEF-4"
      title: "Attention = distributed precision-selection (a MAP, not a substrate -- containment only)"
      phase: 3
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: []
      cross_plan_link: []
      blocking_on: "Containment-only by design: REE has NO explicit attention module because attention is already distributed across ARC-005 / MECH-251/254/255/259/261/347 / SD-032a / SD-057 / GAP-7 / ARC-062/063. The missing thing is a unifying MAP, not a substrate."
      readiness_gate:
        - "REVERSAL TRIGGER: a SPECIFIC attention-bottleneck failure that the existing distributed precision-selection mechanisms demonstrably cannot handle -- only THEN consider promoting a unifying claim, and even then a MAP/coordination claim before any parallel module"
        - "HARD GUARD: do NOT build a parallel attention module; do NOT register a new attention substrate on general grounds. Promotion is failure-driven only"
      last_updated: 2026-06-11
      completion_note: "Canonical paragraph: docs/thoughts/2026-06-04_attention_distributed_precision_selection.md. This node exists so the containment decision is visible on the map and cannot be silently re-litigated into a substrate build."
---
# Deferred-by-Commitment -- Parking Lot + Reversal Triggers

**Registered:** 2026-06-11
**Generation:** deferred (excluded from every closure/roadmap percentage)
**Status:** parking lot

This plan exists because the closure map is the project's **durable resume
primitive**, and the one category it was silently omitting was the work the
project deliberately chose *not* to build. "Deferred by commitment" is not the
same as "unknown" or "forgotten": each item below has a documented disposition
and an explicit **reversal trigger** -- the condition that would pull it back
into an active generation tier. Putting those triggers on the map means a future
session can *watch* for them instead of rediscovering the decision.

## What is parked, and why

| Node | Item | Disposition | Authoritative source |
|---|---|---|---|
| DEF-1 | TCL / phase-coherent V(t) (ARC-053/054/055) | deferred-by-commitment, reversible (4 triggers) | `v3_v4_phase_substrate_boundary.md` |
| DEF-2 | Oscillatory + ephaptic mechanisms (MECH-225/226/227/228/270) | deferred-by-commitment (concrete MECH-271 trigger) | `v3_v4_phase_substrate_boundary.md` |
| DEF-3 | Signed competitive multi-field coupling (ARC-084) | substrate_conditional -- wait for V4 multi-field layer | claims.yaml ARC-084 |
| DEF-4 | Attention = distributed precision-selection | containment-only MAP, failure-driven promotion only | `docs/thoughts/2026-06-04_attention_distributed_precision_selection.md` |

## How a node leaves this plan

When a node's reversal trigger fires, it is promoted out of `generation: deferred`
into its real tier (DEF-1/DEF-2 -> a V4 substrate plan; DEF-3 -> V4 once the
multi-field layer exists; DEF-4 -> a narrow MAP claim, never a module). Until
then it stays here, visible and excluded from every percentage.

## Decision log

- **2026-06-11** -- Plan registered to give the deferred-by-commitment substrate
  its first home on the closure map. No claims changed; reversal triggers lifted
  verbatim from the boundary doc + the attention thought doc. Phase-tag drift on
  ARC-053/054 + MECH-270 (read v3, should be v4) noted for the held-reassignment
  batch.
