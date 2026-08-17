---
closure_plan:
  id: mech303_safety_threshold
  title: "MECH-303 Safety-Threshold Sourcing"
  owner_claim: MECH-303
  registered: 2026-08-13
  last_updated: 2026-08-16
  scope_claims: [MECH-303]
  sibling_plans: [behavioral_diversity_isolation]
  registered_note: "NEW plan doc (session jovial-shannon-35d300, 2026-08-13). MECH-303 was promoted candidate->provisional 2026-07-15 (V3-EXQ-760 representation-level PASS) but its promote-to-active behavioural falsifier was blocked by a measurement defect surfaced by V3-EXQ-917 (2026-08-11): the production damage_sourced signal feeding contextual_safety_harm_threshold caps at AUC<=0.52 (chance) safe-vs-unsafe discrimination across all 18 swept thresholds -- no threshold is both reachable and discriminating. Routing was user-adjudicated 2026-08-12 (/governance, session sd-016-h3-algorithm-3370cd): build a DEDICATED proximity-anticipatory signal (option a), not a threshold retune on the shared damage_sourced signal (option b, rejected -- would break other z_harm_a consumers), consistent with the SD-011 dual-stream separation. Registered as substrate_queue SD-MECH303-THRESHOLD-SOURCING (added_utc 2026-08-12T18:24:49Z, node_class complicated (buildable), ready=true). Prior to this plan doc, MECH-303 was not wired to the closure_plan graph -- it appeared only in narrative governance notes (behavioral_diversity_isolation_plan.md, inference_belief_state_v4_plan.md) and was invisible to the v3 closure percentage despite being an actively-worked v3 claim with an open, ready, scoped build. Two chips already cover this build: chip-20260812-mech303-threshold-sourcing (fully-scoped) and chip-igw-20260812-216 (IGW auto-staged pointer to the same substrate_queue entry) -- both open as of this registration; this plan doc does not spawn a third."
  nodes:
    - id: "mech303_safety_threshold:BUILD"
      title: "Give MECH-303's contextual_safety_harm_threshold a dedicated proximity-anticipatory harm signal, decoupled from SD-022 damage-sourced z_harm_a"
      status: done
      severity: high
      join:
        bears_on: []
        scope_claims: ["MECH-303"]
      unblocks_claims: [MECH-303]
      depends_on: []
      cross_plan_link: ["behavioral_diversity_isolation:GAP-C"]
      last_updated: 2026-08-16
      completion_note: "CLOSED 2026-08-16 (/governance cycle cranky-driscoll-126a36) on confirmed failure_autopsy_V3-EXQ-930_2026-08-16. The build LANDED 2026-08-14 (ree-v3 b257e7ad14) and V3-EXQ-930 validated it at the SIGNAL layer under the production scenario limb_damage_enabled=True: the dedicated obs_dict['safety_proximity_harm'] channel is monotone across hazard density (per-density means 0.000/0.283/0.536/0.840/0.867, spread 0.331) and separable safe-vs-unsafe at every threshold from 0.02 to 0.30, best AUC 1.0 at tau=0.08 -- exceeding the 0.84 acceptance target this node registered from V3-EXQ-917, and the SHIPPED default contextual_safety_proximity_threshold=0.25 sits inside that band (reach 0.648, AUC 1.0). The decoupling from damage-sourced z_harm_a also reproduced (z_harm_a per-density spread 6.96e-05 vs the same-run positive control's 0.331, ~4760x; best AUC 0.52), and biology is load-bearing and supportive -- anticipatory exteroceptive threat-proximity vs interoceptive tissue-damage is a genuine mammalian dissociation, so the damage-sourced null is what biology predicts and the 2026-08-12 option-(a) routing is vindicated. THIS NODE'S SCOPE (build the dedicated signal and calibrate a threshold into the reachable+discriminating band) IS DELIVERED. What is NOT delivered, and is deliberately NOT this node's debt: the MECH-303 BEHAVIOURAL falsifier. V3-EXQ-930 never enabled the MECH-303 gate itself (use_contextual_safety_terrain default False; contextual_safety_gate_source default 'z_harm_a'; the accumulate_safety block at agent.py:5166-5212 did not execute), the agent was untrained, and no vigilance/avoidance readout was taken -- so 930 is non_contributory TO THE CLAIM and MECH-303 keeps status provisional + pending_retest_after_substrate true. That retest's stated condition ('once the dedicated signal lands') is now MET, so it is UNBLOCKED and owed; it is tracked on the claim and chipped to /queue-experiment, not held open here. Recording caveat carried forward to that retest: the per-tick z_harm_a series and a damage-exposure readout existed at run time and were DISCARDED, so a per-seed-standardised discrimination cannot be computed post hoc -- fold both into its recording spec per experimental_recording_standard_2026-07-12.md rather than re-running blind."
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
