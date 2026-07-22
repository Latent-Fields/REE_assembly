---
closure_plan:
  id: arc_005_control_plane_routing
  generation: v3
  title: "ARC-005 Control-Plane Routing (does the plane route, and which channel carries it)"
  registered: 2026-07-22
  last_updated: 2026-07-22
  scope_claims: [ARC-005]
  sibling_plans: [perceptual_adaptors_v4_plan.md, inference_belief_state_v4_plan.md]
  roadmap_note: >
    TWO-NODE VALIDATION LADDER for the registry's highest fan-in claim.
    GAP-A asks whether the control plane has ANY causal authority over precision
    and mode occupancy, dissociable from content (owner V3-EXQ-802, queued).
    GAP-B asks WHICH of the four implemented channels carries that authority --
    it is strictly downstream of GAP-A and is currently UNOWNED, which is the
    reason this doc exists. Registered by a /queue-experiment session that was
    spawned to author GAP-B and correctly STOPPED at its start-time gate because
    802 had not yet run.
  nodes:
    - id: "arc_005_control_plane_routing:GAP-A"
      title: "Does the control plane route at all? Channel-vs-content double dissociation over precision and mode occupancy"
      phase: 0
      status: in-progress
      severity: load-bearing
      owner_exq: "V3-EXQ-802"
      unblocks_claims: [ARC-005]
      depends_on: []
      last_updated: 2026-07-22
      resume_condition: "V3-EXQ-802 is queued in ree-v3/experiment_queue.json (status pending, priority 47, machine_affinity any, 6 conditions x 5 seeds, est 360 min) and has NOT run -- no manifest exists in REE_assembly/evidence/experiments/ (flat or runs/<run_id>/ pack) as of 2026-07-22T03:28Z. Node closes when 802 lands a manifest AND is adjudicated. Script: ree-v3/experiments/v3_exq_802_arc005_control_plane_routing_double_dissociation.py (ree-v3 main fd8b309050). Design: all four control-plane channels moved TOGETHER along a 3-level ladder (L0/L1/L2) x 2 content sets on a fixed arena; the proposal's 2x2 is the {L0,L2}x{A,B} sub-grid, and L1 exists because the acceptance check requires monotonicity, which two levels cannot show. DVs: E3 precision readout + mode-occupancy distribution. Lineage mint: exq802_arc005_control_plane, every cell emitted with include_driver_script_in_hash=False, so this run IS the cross-driver-reusable baseline mint."
    - id: "arc_005_control_plane_routing:GAP-B"
      title: "Which channel carries it? Per-channel leave-one-out ablation grid (UNOWNED -- nothing re-derives this)"
      phase: 1
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-005]
      depends_on: ["arc_005_control_plane_routing:GAP-A"]
      blocked_by: ["V3-EXQ-802 has not run -- per-channel attribution is only meaningful once the plane is shown to route at all"]
      last_updated: 2026-07-22
      resume_condition: "RESUME WHEN V3-EXQ-802 LANDS A MANIFEST. Nothing re-derives this node: it is /queue-experiment work, which has no standing worklist, and 802's completion triggers nothing that re-raises it. Authoring route: /queue-experiment (mandatory skill path -- do NOT hand-write into ree-v3/experiments/ or the queue). Pick the next free EXQ id AT WRITE TIME (several parallel sessions collided in the 800s: 802 ARC-005, 804 ARC-003, 805 ARC-016)."
      design_sketch: "Leave-one-out at the L2 (fully perturbed) setting on content set A: ARM_ALL_ON plus four ARM_<channel>_OFF arms that each return EXACTLY ONE channel to its L0 value, contrasted against ARM_ALL_OFF (= L0). Per-channel authority = the DROP in the channel-vs-L0 effect when that channel alone is returned to baseline. REUSE: ree-v3/experiments/_lib/baselines/exq802_arc005_control_plane.py (verified exports: CHANNEL_LEVELS=[0.0,0.5,1.0], channel_settings(level), agent_kwargs(level), content_env_kwargs(content,seed), off_path_config_slice(), cell_config_slice(level,content), arm_id(level,content)); cite reuse_baseline_from: <802 run_id> with include_driver_script_in_hash=False so the L0 cells are REUSED rather than re-run. This is a refinable sketch, not a fixed design."
      channels: "The four implemented control-plane channels, with the readiness-probe expectation that channels 3 and 4 carry most of the OCCUPANCY authority (600-tick probe -- an EXPECTATION to test, not an established finding): (1) 5-HT rigidity via serotonin gain_min/gain_max -> mainly PRECISION; (2) phasic-burst gain via phasic_burst_temp_delta -> mainly PRECISION, and it is an E3 SOFTMAX TEMPERATURE hence ARGMAX-INVARIANT; (3) mode prior via salience_external_task_bias -> DIRECT occupancy authority (per-mode logit shift); (4) pcc_stability mu via pcc_stability_baseline -> occupancy via the MECH-259 switch-threshold leg, while its MECH-048 mu leg is a softmax temperature and is ARGMAX-INVARIANT."
      mandatory_design_check: "DV-SYMMETRY, per the /queue-experiment rule -- do NOT skip. State per arm the symmetry group of that arm's DV and confirm the manipulation is NOT invariant under it. Channels 2 and 4-mu are BOTH pure softmax temperatures, so an arm ablating only one of them is at real risk of being ARGMAX-INVARIANT and therefore producing a delta that is an ARITHMETIC IDENTITY rather than a measurement. Such an arm must be scoped OUT of scoring and routed non_contributory under substrate_ceiling -- NEVER 'mixed'. This is exactly the V3-EXQ-604c failure class."
      substrate_notes: "Carried over from 802, ALL identical in every arm: (a) use_dacc=True AND use_aic_analog=True are REQUIRED -- with both off the SalienceCoordinator's salience_aggregate is identically 0, argmax is always external_task, and the discrete mode can NEVER switch (occupancy would be single-mode by configuration, not by substrate); (b) phasic_burst_signal_source='instantaneous_pe' with phasic_burst_baseline_continuity='carry' is REQUIRED or channel 2 fires zero events and is inert; (c) 5-HT must be set at the channel OUTPUT (cfg.serotonin.gain_min == gain_max) because harm suppression crushes any tonic baseline to ~0 within tens of steps; (d) NON-DEGENERACY gates on the DESIGN-level 'n_distinct_argmax_modes_across_design >= 2', NOT a per-arm 'arm occupies >= 2 modes' -- 802 measured that the per-arm form VACATES the strongest instance of the effect under test (every corner arm single-mode while the channel manipulation moved the mode end-to-end, TV 1.0, and content moved it not at all, TV 0.0). Keep within-arm multi-modality as a NON-GATING diagnostic."
      why_it_matters: "ARC-005 carries 88 reverse dependencies -- the highest fan-in in the registry -- on exp_conf 0.0 with ZERO experimental entries, held up entirely by lit_conf 0.783. A PASS on GAP-A establishes that THE PLANE is causal but NOT that each channel independently routes; 802's own docstring ('WHICH CHANNEL CARRIES A PASS') and its manifest custom_information.channel_attribution_limit both declare per-channel dissociation UNTESTED. Without GAP-B those 88 dependents cannot tell WHICH channel they may rely on."
---

# ARC-005 -- Control-Plane Routing (Plan of Record)

**Created:** 2026-07-22 &nbsp;|&nbsp; **Status:** GAP-A in-progress (V3-EXQ-802 queued, not yet run) — GAP-B blocked and **unowned**.

## Why this doc exists

ARC-005 ("Control plane routes precision and modes") has the **highest fan-in in the claims
registry — 88 reverse dependencies** — on `exp_conf 0.0` with **zero** experimental entries.
Its entire support is literature (`lit_conf 0.783`). V3-EXQ-802 is the first experiment of any
kind against it.

The validation splits cleanly into two questions, and only the first has an owner:

| Node | Question | Owner | Status |
|---|---|---|---|
| GAP-A | Does the plane route **at all**, dissociably from content? | V3-EXQ-802 (queued) | in-progress |
| GAP-B | **Which channel** carries that authority? | **none** | blocked on GAP-A |

## The ownership gap this doc closes

A `/queue-experiment` session was spawned on 2026-07-22 to author GAP-B. It **correctly stopped
at its start-time gate**: V3-EXQ-802 is still `status: "pending"` in
`ree-v3/experiment_queue.json` and has landed no manifest, so the per-channel design could not
be written. That is the right outcome — but it left the GAP-B specification living only in a
session transcript.

**Nothing re-derives GAP-B.** It is `/queue-experiment` work, which has no standing worklist
(unlike `/governance` and `/failure-autopsy`, which re-derive their own queues every cycle), and
802's completion fires no trigger that re-raises it. This node is that record.

## Why GAP-B must wait for GAP-A, not run beside it

The leave-one-out design measures *the drop in the channel-vs-L0 effect when one channel is
returned to baseline*. Three things fail if 802 has not run:

1. **If 802 returns FAIL** — the plane has no measurable authority — then every per-channel drop
   is a difference of two nulls, and the follow-up would report four arithmetic identities as
   channel attributions.
2. **The baseline cells cannot be reused.** `reuse_baseline_from: <802 run_id>` needs a run_id
   that does not exist yet, so every L0 cell would have to be re-run at full cost.
3. **The argmax-invariance risk cannot be checked**, only asserted. Channels 2 and 4-mu are both
   softmax temperatures; whether their ablation arms are degenerate is answerable against 802's
   measured diagnostics, not against the 600-tick readiness probe.

## Resume procedure

```bash
# 1. Has GAP-A landed?
grep -l v3_exq_802 /Users/dgolden/REE_Working/REE_assembly/evidence/experiments/*.json
ls -d /Users/dgolden/REE_Working/REE_assembly/evidence/experiments/runs/*802* 2>/dev/null
# 2. If yes, read the verdict + channel diagnostics before designing GAP-B.
# 3. Author via the skill -- /queue-experiment. Never hand-write the script or queue entry.
```

Then work the GAP-B frontmatter fields in order: `design_sketch` (refine, don't take as fixed),
`channels`, `mandatory_design_check` (the DV-symmetry rule — the V3-EXQ-604c failure class),
`substrate_notes` (all four carry over from 802 unchanged).

## Scope

This plan owns **ARC-005's own V3 experimental validation only**. It is not the home for the V4
consumers that ride the control plane — `perceptual_adaptors_v4` names ARC-005 as the host for
its cross-modal negotiation/precision layer (PA-5) but is a forward roadmap with no experiments
and a dormant drift checker. Cross-plan edges belong there, not here.
