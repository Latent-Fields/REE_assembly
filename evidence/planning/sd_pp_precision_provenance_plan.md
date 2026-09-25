---
closure_plan:
  id: sd_pp_precision_provenance
  title: "SD-PP-1..4 precision-provenance substrate + the B-series behavioural/diagnostic follow-on (SD-PP-B1..B11)"
  generation: v3
  registered: 2026-09-25
  last_updated: 2026-09-25
  scope_claims: [MECH-572, MECH-573, MECH-574, SD-008, INV-063]
  sibling_plans: [zworld_adequacy, conversion_ceiling_campaign]
  related_threads:
    - "docs/architecture/precision_provenance_substrate_spec.md -- the SD-PP-1..4 interface contract (MECH-572 lead)"
    - "substrate_queue.json SD-PP-1..4 (implemented_pending_validation) and SD-PP-B1..B11 (the behavioural-consumer / diagnostic follow-on series)"
    - "GOV-DIAG-1 (scripts/check_diagnostic_chain_recurrence.py) -- diagnostic-chain recurrence audit"
  registered_note: >
    NEW plan doc (chip-20260924-sdpp-closure-plan-node). GOV-DIAG-1 fired an
    ACTIONABLE recurrence 2026-09-24 on bears_on tokens MECH-573 / MECH-574 --
    the pure-diagnostic (claim_ids: []), no-verdict (recommended_evidence_direction:
    non_contributory) chain V3-EXQ-1079 -> V3-EXQ-1081 -> V3-EXQ-1082, all
    circling the same "is the world-forward head's readout readable /
    action-sensitive at its current operating point" question. The user
    adjudicated the chain metabolized-as-re-posed at the 2026-09-24 /governance
    interactive gate (failure_autopsy_V3-EXQ-1082_2026-09-24.json
    mode_D_h_other_event, response partition_expansion; recommendation-ledger
    rec-20260924-aeac2558 / rec-20260924-002ff612): the three registered levers
    (H-margin-form, H-infonce-form, H-encoder-displacement) were all built on
    an assumed-blind head, and at SD-008's alpha_world >= 0.9 operating point
    on a live battery the head is demonstrably NOT blind on the axes measured
    (d_act, skill) -- so the chain converged on an omitted operating parameter,
    not on under-powered levers, and the correct disposition is
    diagnostic_recurrence_metabolized, not a fourth lever. But
    check_diagnostic_chain_recurrence.py reads that marker ONLY from a
    closure_plan node in evidence/planning/*_plan.md, and no plan node owned
    the SD-PP precision-provenance workstream -- it lived only in
    substrate_queue.json rows (SD-PP-1..4, SD-PP-B1..B11) and
    docs/architecture/precision_provenance_substrate_spec.md, neither of which
    the audit reads. Confirmed by search: zero existing *_plan.md mentions
    "SD-PP" or "precision_provenance" before this registration.
  registration_decision_note: >
    OWN PLAN rather than a node on an existing plan. zworld_adequacy_plan.md
    (registered 2026-09-11 for the same class of gap -- INV-088/MECH-457
    GOV-DIAG-1 recurrence with no closure-map home) is the nearest topical
    neighbour and the direct precedent for this registration's shape, but its
    scope is deliberately narrow to the observation -> z_world ENCODING half
    (its own frontmatter says so explicitly) and its scope_claims
    (INV-088, MECH-457, SD-015, ARC-030, MECH-117, ARC-065) do not include
    MECH-572/573/574 or SD-008. The MECH-572/573/574 chain is about whether
    SLEEP CONSOLIDATION improves an already-encoded world-forward head's
    held-out readout -- a downstream-of-encoding, operating-point-and-training-
    dynamics question, not an encoding-adequacy one. No other *_plan.md's
    scope_claims or node unblocks_claims mention MECH-572, MECH-573, MECH-574,
    or the SD-PP-* substrate_queue family (grep across all *_plan.md
    frontmatter, zero hits). This plan owns that workstream going forward:
    SD-PP-1..4 (the producer/carrier/consumer/gain substrate, implemented,
    pending validation) and the SD-PP-B* series (behavioural-consumer and
    diagnostic follow-on questions the intake's validation raised). NO
    claims.yaml edits were made by this registration -- this is closure-map
    registration only, not a promotion, demotion, or build authorisation.
  nodes:
    - id: "sd_pp_precision_provenance:PP-1"
      title: "world-forward head readability/action-sensitivity operating-point chain (MECH-572/573/574 sleep-consolidation readout question)"
      phase: 1
      status: assembling
      awaiting: null
      assembly_status: built
      severity: medium
      owner_exq: v3_exq_1082_sdppb5_alpha09_live_battery_revalidation_20260924T045004Z_v3
      unblocks_claims: ["MECH-572", "MECH-573", "MECH-574", "SD-008", "INV-063"]
      depends_on: []
      cross_plan_link: ["zworld_adequacy"]
      last_updated: 2026-09-25
      what_is_established: >
        V3-EXQ-1079 (SD-PP-B10 alpha_world operating-point probe) measured
        that the world-forward head's action-blindness (SD-PP-B5,
        V3-EXQ-1073, alpha_world=0.3) is an operating-point property (EMA
        damping of z_world) rather than a head/objective property. V3-EXQ-1081
        (SD-PP-B1 reach probe) found the premise "no default-on behavioural
        consumer of e2.world_forward exists" false (GFLAG-0437): a default
        consumer already reads it. V3-EXQ-1082 (SD-PP-B5 alpha=0.9 live-battery
        revalidation) confirmed H-operating-point: at SD-008's alpha_world >=
        0.9 on a live battery, the untouched world-forward head reads its
        action (d_act 0.341/0.216/0.227, CI lower > 0 on 3/3; skill_vs_identity
        +0.35/+0.22/+0.21) without any training-time lever -- deprioritising
        the three margin/infonce/encoder-displacement levers the chain had
        been iterating on. The inverted-map live_gate readout and the
        within-run alpha attribution remain open (decision.decidable is still
        false in the hypothesis-space ledger), so this node stays assembling,
        not closed.
      resume_condition: >
        Node advances when a driver measures the inverted-map live_gate
        readout at alpha_world >= 0.9 on a live battery (the gap
        H-operating-point's own resolution names as still open), or when a
        /governance cycle re-poses the question under a new hid/qid rather
        than re-running one of the three deprioritised levers. A same-question
        re-queue of H-margin-form, H-infonce-form, or H-encoder-displacement at
        the OLD alpha_world=0.3 operating point should be routed back to this
        node's diagnostic_recurrence_metabolized marker, not re-run.
      diagnostic_recurrence_metabolized:
        date: 2026-09-25
        metabolized_hits:
          - v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3
          - v3_exq_1081_sdppb1_world_forward_ranking_reach_probe_20260923T222438Z_v3
          - v3_exq_1082_sdppb5_alpha09_live_battery_revalidation_20260924T045004Z_v3
        covers_tokens:
          - MECH-573
          - MECH-574
        note: >
          Chain V3-EXQ-1079 -> 1081 -> 1082 (all claim_ids: [], all
          non_contributory) converged on an omitted operating parameter
          (alpha_world), not a mis-posed or under-powered question:
          H-operating-point (registered as labelled growth on qid
          zworld_action_readability_lever, not a new qid; hypothesis-space
          ledger applied 2026-09-24T07:29:21Z) is CONFIRMED that the
          world-forward head reads its action at SD-008's alpha_world >= 0.9 on
          a live battery, deprioritising the three lever hypotheses
          (H-margin-form, H-infonce-form, H-encoder-displacement) the chain had
          been iterating on at the stale alpha_world=0.3 operating point. Mode-D
          h_other_event recorded in failure_autopsy_V3-EXQ-1082_2026-09-24.json:
          "no registered leg explains the outcome -- an operating parameter
          omitted from the partition (alpha_world) accounts for the premise the
          three lever legs were built to remedy"; response partition_expansion.
          User-confirmed at the 2026-09-24 /governance interactive gate
          (confirmed_utc 2026-09-24T07:29:21Z; recommendation-ledger
          rec-20260924-002ff612, rec-20260924-aeac2558). GOV-DIAG-1 token
          reconciliation was the one open item the confirmation note flagged
          ("GOV-DIAG-1 token not reconciled") -- this marker closes it. A NEW
          diagnostic chain later circling the operating-point-corrected
          question (alpha_world >= 0.9, e.g. the still-open inverted-map
          live_gate readout) is a different question and can still accumulate
          to N; only these three specific hits are excluded.
---

# SD-PP precision-provenance closure plan

Closure-map home for the SD-PP-1..4 precision-provenance substrate
(`docs/architecture/precision_provenance_substrate_spec.md`, MECH-572 lead)
and its B-series behavioural-consumer / diagnostic follow-on
(`substrate_queue.json` SD-PP-B1..B11). Registered to give the 2026-09-24
GOV-DIAG-1 MECH-573/MECH-574 recurrence (chain V3-EXQ-1079 -> 1081 -> 1082) a
`diagnostic_recurrence_metabolized` home -- see the `registered_note` /
`registration_decision_note` / node `PP-1` marker above for the full
reasoning. No claims.yaml disposition is made or implied by this document;
see the plan-of-record docs this sits alongside
(`REE_Working/CLAUDE.md` Session Startup Protocol step 8) for that machinery.
