---
closure_plan:
  id: mech357_avoidance_efficacy
  title: "MECH-357 Avoidance-Efficacy / Freeze-Suppression Gate (SD-058)"
  owner_claim: MECH-357
  registered: 2026-08-13
  last_updated: 2026-08-29
  scope_claims: [MECH-357]
  sibling_plans: [sleep_substrate]
  registered_note: "NEW plan doc (session jovial-shannon-35d300, 2026-08-13). MECH-357 (candidate, v3_pending, implementation_phase v3) is the mechanism instantiating SD-058: infralimbic-PFC-analog freeze-suppression + instrumental-avoidance gate, driven by an eligibility-trace avoidance_efficacy learner. Four consecutive Stage-H onboarding attempts to establish discriminating hazard pressure (603h/603k/603r/603s) and a fifth config-only redesign (603t, scheduled_external_hazard) all returned inconclusive-by-design-defect -- config-only pressure levers (static field, mobile-predator drift, scheduled discrete adjacency) are exhausted across 3 distinct designs (failure_autopsy_V3-EXQ-603t_2026-08-13). The one remaining candidate is agent-directed hazard pursuit (ree_core/environment/causal_grid_world.py hazard_agent_pursuit, already built per commit 39b5ca8 but never wired into the Stage-H curriculum). Registered as substrate_queue mech357-freeze-incompatible-pressure-mechanism (added_utc 2026-08-12T18:24:49Z, node_class complex (probe-gated) -- unlike MECH-303/MECH-267's complicated (buildable) siblings, whether agent-directed pursuit actually produces the needed G_H_INTACT/G_H_LESION discrimination is a genuine empirical unknown, not just an implementation gap; ready=true). Prior to this plan doc, MECH-357 was not wired to the closure_plan graph despite being the single most heavily-worked v3 substrate thread by chip count (>15 chips across litpull, fishtank design, hazard-pursuit fallback, validation-cache fixes, and this pressure-mechanism scoping itself). This node is also entangled with sleep_substrate:GAP-9 (both surfaced from the same 906/920-lineage true-single-continuous-life Fishtank research program; see cross_plan_link) and with the developmental_life_definition_decision_2026-08-12.md scoping memo, which named MECH-357's fair test as one of two prerequisites for a long-development experiment design. One chip already covers the wiring step: chip-20260813-implsub-mech357-hazard-pursuit (open); this plan doc does not spawn a second."
  nodes:
    - id: "mech357_avoidance_efficacy:BUILD"
      title: "Wire agent-directed hazard pursuit into Stage-H onboarding curriculum; run the discrimination test agent-directed pursuit was held out as the last untried candidate for"
      status: partial
      governance_2026_08_29: >
        Status flipped open -> partial by /governance 2026-08-29 (session
        governance-20260829-mac), absorbing the events the reconcile_2026_08_27
        field staged: the BUILD half is DONE (pursuit wiring landed 2026-08-14,
        validated negative via V3-EXQ-603u -- G_H_LESION_frac 1.0, all four
        pressure designs exhausted, substrate entry validated_negative) and the
        sibling eligibility-trace repair is DONE and REVIEWED (V3-EXQ-603v
        PASS, walked in the 2026-08-28 cycle; its 'supports' adjudicated down
        to instrument-repair per failure_autopsy_V3-EXQ-603v_2026-08-28, which
        also reclassified MECH-357). Remaining owed work is NOT a build: the
        zero-compute reanalysis of the recorded 603s/603t/603u per-episode
        trajectories (chip-20260827-mech357-trajectory-reanalysis, open) --
        node_class mystery (known data). Resolves the closure-drift
        stale-since-update hint and GFLAG-0052/GFLAG-0068.
      severity: high
      reconcile_2026_08_27: >
        NODE OVERTAKEN BY EVENTS (session f-dominance-regime-retest-ddbe10,
        debt-classification sweep; plan-frontmatter only, status left open
        for /governance to flip, nothing queued). The BUILD half LANDED
        2026-08-14 (scaffold_hazard_stage_hazard_agent_pursuit threaded,
        session intelligent-elgamal-222d2b) and VALIDATED NEGATIVE via
        V3-EXQ-603u (governance 2026-08-16: G_H_LESION_frac = 1.0, so the
        discrimination could not pass; all four pressure designs now
        exhausted -- substrate_queue
        mech357-freeze-incompatible-pressure-mechanism status
        validated_negative). The sibling eligibility-trace repair was
        implemented 2026-08-16 (ree-v3 93d5d98b80) and its validation
        V3-EXQ-603v RAN PASS/supports 2026-08-27T18:47Z (UNREVIEWED at this
        writing -- pending_review walk owes it). The node's owed work has
        therefore MIGRATED from a build to the zero-compute reanalysis of
        the already-recorded 603s/603t/603u per-episode trajectories (the
        substrate entry's own named precondition for any fifth pressure
        mechanism) -- chipped as chip-20260827-mech357-trajectory-reanalysis.
        node_class reading migrates complex (probe-gated) -> mystery (known
        data). Governance flag raised (stale_note, MECH-357).
        Classification record:
        evidence/planning/work_graph_debt_classification_20260827.md.
      join:
        bears_on: []
        scope_claims: ["MECH-357"]
      unblocks_claims: [MECH-357]
      depends_on: []
      cross_plan_link: ["sleep_substrate:GAP-9"]
      last_updated: 2026-08-29
      registered_note: "node_class complex (probe-gated), not buildable -- the wiring itself (thread hazard_agent_pursuit through scaffolded_sd054_onboarding.py's Stage-H _build_env, mirroring how scheduled_external_hazard/env_drift are already threaded) is ordinary implementation, but whether it produces G_H_INTACT_frac > G_H_LESION_frac discrimination with headroom (G_H_LESION_frac < 0.333, per 603t's readiness R4) is genuinely untested. A separate, not-yet-substrate-queued defect was flagged alongside this one: infralimbic_avoidance_gate.py's eligibility trace decays ~90-100x faster than it credits (leak_rate=0.02 vs learn_rate=0.05 on very different tick counts), underflowing to numerical zero in every run to date -- may need its own substrate_queue line item rather than folding into this build. Substrate paths: ree-v3/experiments/scaffolded_sd054_onboarding.py, ree-v3/ree_core/environment/causal_grid_world.py, ree-v3/ree_core/pfc/infralimbic_avoidance_gate.py. Open chip: chip-20260813-implsub-mech357-hazard-pursuit."
---

# MECH-357 Avoidance-Efficacy Plan

**Registered:** 2026-08-13
**Status:** active
**Scope:** land the last untried Stage-H pressure design (agent-directed hazard
pursuit) needed to run MECH-357's discrimination test, after three
config-only pressure designs (static field, mobile-predator drift, scheduled
discrete adjacency) all failed to establish a discriminating gap across five
attempts (603h/603k/603r/603s/603t).

## One-line framing

> Every config-only way to make a hazard "freeze-incompatible" has been
> tried and failed to discriminate. The one remaining candidate -- letting
> the hazard actively pursue the agent -- is already built in the
> environment and simply never wired into the curriculum that would test it.

## Remaining work to close (1)

| node | title | status | severity | active blocker |
|------|-------|--------|----------|-----------------|
| `mech357_avoidance_efficacy:BUILD` | Wire hazard_agent_pursuit into Stage-H onboarding + run the discrimination test | partial | high | build DONE + validated negative (603u); trace repair DONE + reviewed (603v); remaining: trajectory reanalysis (chip-20260827-mech357-trajectory-reanalysis) |

## Decision log

- **2026-08-13** (session jovial-shannon-35d300): plan doc registered to fold
  MECH-357 into the v3 closure map. No code, claims.yaml, or substrate_queue
  change -- frontmatter + plan-doc only.
