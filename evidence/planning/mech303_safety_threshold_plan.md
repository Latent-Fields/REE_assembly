---
closure_plan:
  id: mech303_safety_threshold
  title: "MECH-303 Safety-Threshold Sourcing"
  owner_claim: MECH-303
  registered: 2026-08-13
  last_updated: 2026-08-13
  scope_claims: [MECH-303]
  sibling_plans: [behavioral_diversity_isolation]
  registered_note: "NEW plan doc (session jovial-shannon-35d300, 2026-08-13). MECH-303 was promoted candidate->provisional 2026-07-15 (V3-EXQ-760 representation-level PASS) but its promote-to-active behavioural falsifier was blocked by a measurement defect surfaced by V3-EXQ-917 (2026-08-11): the production damage_sourced signal feeding contextual_safety_harm_threshold caps at AUC<=0.52 (chance) safe-vs-unsafe discrimination across all 18 swept thresholds -- no threshold is both reachable and discriminating. Routing was user-adjudicated 2026-08-12 (/governance, session sd-016-h3-algorithm-3370cd): build a DEDICATED proximity-anticipatory signal (option a), not a threshold retune on the shared damage_sourced signal (option b, rejected -- would break other z_harm_a consumers), consistent with the SD-011 dual-stream separation. Registered as substrate_queue SD-MECH303-THRESHOLD-SOURCING (added_utc 2026-08-12T18:24:49Z, node_class complicated (buildable), ready=true). Prior to this plan doc, MECH-303 was not wired to the closure_plan graph -- it appeared only in narrative governance notes (behavioral_diversity_isolation_plan.md, inference_belief_state_v4_plan.md) and was invisible to the v3 closure percentage despite being an actively-worked v3 claim with an open, ready, scoped build. Two chips already cover this build: chip-20260812-mech303-threshold-sourcing (fully-scoped) and chip-igw-20260812-216 (IGW auto-staged pointer to the same substrate_queue entry) -- both open as of this registration; this plan doc does not spawn a third."
  nodes:
    - id: "mech303_safety_threshold:BUILD"
      title: "Give MECH-303's contextual_safety_harm_threshold a dedicated proximity-anticipatory harm signal, decoupled from SD-022 damage-sourced z_harm_a"
      status: open
      severity: high
      join:
        bears_on: []
        scope_claims: ["MECH-303"]
      unblocks_claims: [MECH-303]
      depends_on: []
      cross_plan_link: ["behavioral_diversity_isolation:GAP-C"]
      last_updated: 2026-08-13
      registered_note: "V3-EXQ-917 measured the legacy proximity_ema_sourced signal (limb_damage_enabled=False) at AUC 0.84-0.97 with reachability 0.23-0.98 across thresholds 0.4-0.8 -- the target band for the new dedicated signal. Implementation must audit which production drivers (764, 520, 916/916a, and any future use_contextual_safety_terrain driver) consume which signal, and calibrate a threshold into the reachable+discriminating band 917 established. Substrate paths: ree_core/utils/config.py, ree_core/environment/causal_grid_world.py, ree_core/agent.py. Once built, MECH-303's promote-to-active behavioural falsifier (context-safety lowers background vigilance/avoidance-commitment level) becomes runnable for the first time on a non-vacuous gate. Open chips: chip-20260812-mech303-threshold-sourcing, chip-igw-20260812-216."
---

# MECH-303 Safety-Threshold Sourcing Plan

**Registered:** 2026-08-13
**Status:** active
**Scope:** land a dedicated proximity-anticipatory harm signal for MECH-303's
`contextual_safety_harm_threshold` gate, replacing the shared damage-sourced
`z_harm_a` signal that V3-EXQ-917 showed cannot discriminate safe from
hazardous contexts at any threshold in production. This is the sole remaining
build gate on MECH-303's promotion from `provisional` to `active`.

## One-line framing

> MECH-303's representation-level claim already passed (V3-EXQ-760); what is
> missing is a measurement instrument good enough to run the behavioural
> falsifier at all. The fix is scoped, routing-decided, and unbuilt.

## Remaining work to close (1)

| node | title | status | severity | active blocker |
|------|-------|--------|----------|-----------------|
| `mech303_safety_threshold:BUILD` | Dedicated proximity-anticipatory signal for MECH-303's gate | open | high | none -- ready, routing decided 2026-08-12, unbuilt |

## Decision log

- **2026-08-13** (session jovial-shannon-35d300): plan doc registered to fold
  MECH-303 into the v3 closure map. No code, claims.yaml, or substrate_queue
  change -- frontmatter + plan-doc only, per CLAUDE.md's "when registering new
  claims, update in a single pass" convention (MECH-303 itself is not new; only
  its closure-graph wiring is).
