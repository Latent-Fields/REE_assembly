---
closure_plan:
  id: policy_decomposition_trigger
  title: "ARC-070 / MECH-321 decomposition trigger operationalization"
  owner_claim: ARC-070
  registered: 2026-08-14
  last_updated: 2026-08-21
  scope_claims: [ARC-070, MECH-321, MECH-288]
  sibling_plans: [mech303_safety_threshold]
  registered_note: "NEW plan doc (session metaworker-chip-20260812-govdiag1-repose-mech321-chain, 2026-08-14), created to home the GOV-DIAG-1 metabolized marker for the six-hit ARC-070 / MECH-321 / MECH-288 pure-diagnostic chain (816b, 816c, 816d, 830 x2, 839) routed by /governance 2026-08-12 (session sd-016-h3-algorithm-3370cd). No *_plan.md closure-plan node owned this work-stream, so the marker -- which by design lives on the plan node whose status row records the re-operationalization -- had nowhere to live; this is the same closure-graph gap mech303_safety_threshold_plan.md was registered to close on 2026-08-13. The full re-pose is evidence/planning/govdiag1_repose_mech321_chain_2026-08-12.md. This plan doc promotes and demotes nothing, queues no experiment, and writes no hypothesis-space resolution."
  nodes:
    - id: "policy_decomposition_trigger:REPOSE"
      title: "Re-pose ARC-070's prediction-failure decomposition trigger off the saturated region-V_s proxy onto a rank-based forward-PE readout with a rate-matched yoked control"
      status: blocked
      severity: load-bearing
      owner_exq: "V3-EXQ-938"
      join:
        bears_on: [ARC-070, MECH-321, MECH-288]
        scope_claims: [ARC-070, MECH-321]
      unblocks_claims: [ARC-070, MECH-321]
      depends_on: []
      last_updated: 2026-08-21
      queued_2026_08_18: "owner_exq V3-EXQ-938 queued via /queue-experiment 2026-08-18 (chip-20260814-mech321-pe-selectivity-repose, landed ree-v3 main b2a56fa87c); status open -> in_progress. This node's build step -- design and author the re-posed rank-based forward-PE trigger + rate-matched yoked control experiment -- is DISCHARGED (design unchanged from the diagnostic_recurrence_metabolized note below). The section 7 ledger resolutions this node's registered_note held open as a gating precondition landed first (REE_assembly a843ee6ebb, GFLAG-0038: H-vs-proxy-saturation -> confirmed; H-env-underdrives-uncertainty -> superseded/moot), which is what cleared V3-EXQ-938 to be authored. Smoke PASS, validate_experiments --strict clean. NOT YET SCHEDULABLE: queued from ree-cloud-5, which has no REE_assembly/coordinator.env, so /queue-experiment Step 8.6 (POST /queue/add) was not performed -- under Phase 3 the runners execute from the coordinator DB, not this file, so the run cannot start until a coordinator-capable box POSTs it. Tracked separately as chip-20260818-exq938-coordinator-post (carries landing sha b2a56fa87c). Do NOT read status:in_progress as 'running' until that POST is confirmed."
      resume_condition: "2026-08-21 governance applied confirmed failure_autopsy_V3-EXQ-938_2026-08-20: non_contributory (null at this grain, not a detected negative). Lettered 938 successor and fourth env-axis escalation REFUSED. ARC-070/MECH-321 stay candidate with pending_retest_after_substrate. This node's 938 owner_exq is terminal; reopen only on a different operationalization, not another env-axis letter."
      registered_note: >
        CONSUMES V3-EXQ-816b/816c/816d/830/839 (does not re-queue any of them).
        Six pure-diagnostic no-verdict autopsies circling one question; all six
        died at a TRIGGER-OCCUPANCY gate, and in five the load-bearing DV was
        conditional on that occupancy, so "no effect" and "no occasion" aliased
        into a single non-verdict. Re-operationalized: rank-based (top-q%
        within-run) forward-PE trigger instead of an absolute floor on a
        latent-stability proxy that V3-EXQ-816c measured as saturated
        (region_vs_min_over_cells 0.9338) and decoupled from forward-PE
        (spearman 0.0832 vs a 0.2 coupling floor); load-bearing contrast moved
        to ARM_PE vs a rate-matched ARM_YOKED (selectivity, not decomposition
        per se); DV unconditional whole-episode over n >= 40 paired seeds with
        an A-A null control, per the shape V3-EXQ-919 proved decisive on this
        substrate. REFUSED V3-EXQ-816e and the whole low_vs_steps-gated design
        class -- and 816e was NEVER MINTED (no queue entry in ree-v3 current or
        historical, no script, no manifest; verified 2026-08-15), so it is a
        refused DESIGN, never an owed successor this node is waiting on.
        Two ledger resolutions earned by existing data are handed to
        /governance rather than written here. Diagnostic lineage; claim_ids=[].
        Full re-pose: evidence/planning/govdiag1_repose_mech321_chain_2026-08-12.md.
      diagnostic_recurrence_metabolized:
        date: 2026-08-14
        metabolized_hits:
          - v3_exq_816b_mech321_policy_decomposition_harshened_env_20260726T123216Z_v3
          - v3_exq_816c_mech321_vs_pe_decoupling_comparator_20260726T105608Z_v3
          - v3_exq_816d_mech321_policy_decomposition_harshened_env_v2_20260726T185006Z_v3
          - v3_exq_830_mech321_scale_resolved_rollout_boundary_20260727T204927Z_v3
          - v3_exq_839_sd084_midexec_reachability_20260729T220727Z_v3
        covers_tokens:
          - ARC-070
          - MECH-321
          - MECH-288
        note: >
          GOV-DIAG-1's prescribed response was carried out for the
          816b -> 816c -> 816d -> 830 -> 839 chain (830 contributes two hits,
          adjudicated by two artifacts; naming its run_id subtracts both).
          (1) RE-POSED: the common failure across all six is a trigger-occupancy
          gate with an occupancy-conditional load-bearing DV, which aliases "no
          effect" with "no occasion" and returns a non-verdict either way. The
          re-pose moves the trigger off region-V_s -- measured saturated and
          statistically decoupled from forward-PE by V3-EXQ-816c on green
          positive controls -- onto a within-run RANK on forward-PE, which makes
          occupancy a design constant rather than a run outcome and so retires
          the environment-escalation ladder instead of extending it; moves the
          load-bearing contrast from ARM_PE-vs-OFF to ARM_PE-vs-a-rate-matched
          ARM_YOKED, which is what isolates ARC-070's actual selectivity claim
          from decomposition per se (no run in the chain had a rate-matched
          control); and makes the DV unconditional and whole-episode over n >= 40
          paired seeds with an A-A null control, the shape V3-EXQ-919 proved
          decisive on this substrate on 2026-08-11.
          (2) REFUSED: V3-EXQ-816e -- an id that was NEVER MINTED (no queue
          entry current or historical, no script, no manifest; verified
          2026-08-15), i.e. a refused DESIGN rather than an owed successor --
          and any fourth environment-axis escalation
          (816 -> 816b -> 816d moved forward-PE 0.0080 -> 0.008594 -> 0.008675,
          under 0.0007 total, never reaching the 0.01 floor, with low_vs_steps=0
          at every dose); ALSO the broader design class of any re-queue carrying
          a vs_heterogeneity_low_vs_steps_present readiness gate; ALSO the
          pre-registered H-algorithm-axis probe AS SPECIFIED (lowering the
          absolute V_s threshold keeps the dead proxy) -- the probe, not the
          hypothesis, whose disposition stays /governance's call. Recorded as
          re-derive-brake SPIRIT, not letter: 0 substrate_ceiling hits stand
          against ARC-070, MECH-321 or MECH-288.
          (3) RESTATED / SURFACED: two ledger resolutions already earned by data
          in the corpus and never applied -- H-vs-proxy-saturation -> confirmed
          (816c, positive controls green, and the 2026-07-26 deferral's own
          stated condition has since been tested at two doses and resolved
          against proxy usability), and H-env-underdrives-uncertainty ->
          superseded/moot (since V_s is decoupled from PE, raising PE cannot
          lower V_s, so the leg is no longer load-bearing whatever its truth
          value; NOT recommended as `eliminated`, because its pre-registered
          elimination branch required pe_elevated=true and neither 816b nor 816d
          took it). Handed to /governance rather than written here. Also
          surfaced: policy_decomposition_discrimination freezes SCIENCE and
          INSTRUMENT hypotheses into one rival set, which is why it stands at
          0 of 6 resolved after six runs -- a run producing no occasion can
          eliminate neither kind.
          (4) VERIFIED ALREADY METABOLIZED ELSEWHERE, in work post-dating the
          last hit and so invisible to the audit: decomposition_scale_heterogeneity
          (from 830) resolved 3 of 3; and the R4 mid-execution branch (830's R4
          half, 839) ran 839 -> 844 -> 867 -> 867a -> 867b -> 919, where 919
          performed the same DV re-pose independently ("the DV and the unit of
          comparison are what moved") and eliminated
          H-harm-aware-reduces-task-harm, with 867c and the magnitude-only
          re-letter both explicitly refused at the time.
---

# ARC-070 / MECH-321 Decomposition Trigger Operationalization Plan

**Registered:** 2026-08-14
**Status:** active
**Scope:** get ARC-070's "decompose when the prediction is unreliable" trigger onto a
readout that can actually produce an occasion to measure, so the claim's selectivity
prediction can reach a verdict in either direction.

## One-line framing

> The mechanism fires (V3-EXQ-904: 180 real MECH-288 boundary fires drove 180
> decompositions; V3-EXQ-839: 415 mid-execution evaluations). What has never worked is
> the *trigger readout* the claim's own R1 leg is operationalized on — and six
> diagnostics in a row died on that, not on the claim.

## Remaining work to close (1)

| node | title | status | severity | active blocker |
|------|-------|--------|----------|-----------------|
| `policy_decomposition_trigger:REPOSE` | Rank-based forward-PE trigger + rate-matched yoked control, unconditional whole-episode DV | in_progress | load-bearing | owner_exq V3-EXQ-938 queued in git (ree-v3 main b2a56fa87c) but not yet coordinator-registered -- POST /queue/add owed, tracked as chip-20260818-exq938-coordinator-post |

## Decision log

- **2026-08-18** (session `metaworker-chip-20260818-policydecomp-repose-plannode-status`,
  chip `chip-20260818-policydecomp-repose-plannode-status`): node status flipped
  `open` -> `in_progress`, `owner_exq: "V3-EXQ-938"` added. V3-EXQ-938 (the re-posed
  ARC-070/MECH-321 prediction-failure SELECTIVITY experiment this node's re-pose design
  specifies) was authored and queued via `/queue-experiment` 2026-08-18
  (chip-20260814-mech321-pe-selectivity-repose). Build step discharged; coordinator
  registration is a separate, still-open step (chip-20260818-exq938-coordinator-post) --
  see `queued_2026_08_18` / `resume_condition` above. No claims.yaml, substrate_queue,
  or hypothesis-space-registry change.
- **2026-08-14** (session `metaworker-chip-20260812-govdiag1-repose-mech321-chain`, chip
  `chip-20260812-govdiag1-repose-mech321-chain`): plan doc registered to home the
  GOV-DIAG-1 metabolized marker and to give this work-stream a closure-graph node. The
  analysis, refusals and handoffs live in
  [`govdiag1_repose_mech321_chain_2026-08-12.md`](govdiag1_repose_mech321_chain_2026-08-12.md).
  No claims.yaml, substrate_queue, hypothesis-space-registry or experiment-queue change.
