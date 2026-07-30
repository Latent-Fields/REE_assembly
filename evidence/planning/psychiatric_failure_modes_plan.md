---
# Closure-map CLINICAL-lane view. `generation: clinical` keeps these nodes OUT of
# the V3 closure % (read_closure counts only generation: v3), exactly as the
# governance and process lanes do.
#
# WHY THIS IS ITS OWN LANE, and not any existing one:
#   * not v3/v4/v5/v6 -- a syndrome is not a version. Its claims are scattered
#     ACROSS generations by construction (MECH-279 is v3, MECH-214/215 and
#     SD-045/046 are v4), so filing the programme under any single version
#     splits every syndrome in half. Catatonia subtype II is one clinical
#     object whose parent regulator is v3 and whose consumers are not.
#   * not `governance` -- that lane is the SENT-*/GOV-* ethics perimeter.
#   * not `process` -- that lane is infrastructure/tooling owning no science.
#     This lane owns science; it is the architecture's clinical face.
#   * not `deferred` -- nothing here is parked by commitment. It is unbuilt or
#     untested, which is the opposite of deliberately not-built.
#
# This plan is deliberately NOT on scripts/check_closure_drift.py's KNOWN_PLANS
# allowlist (same choice as ethics_perimeter_plan.md), so it renders as a
# standalone board without entering the V3 drift machinery.
#
# STATUS DISCIPLINE. Every node status below is derived from claims.yaml
# `status` plus the experimental counts in
# evidence/experiments/claim_evidence.v1.json (`genuine_exp_count`, `pass_runs`,
# `fail_runs`), read 2026-07-30. Literature confidence is NOT counted toward a
# node's status -- lit and exp evidence are reported separately in this
# programme, and a syndrome supported only by literature is `open`, not
# `partial`. Where the two disagree the node text says so.
closure_plan:
  id: clinical_failure_modes
  generation: clinical
  title: "Psychiatric Failure Modes as Architectural States"
  registered: 2026-07-30
  last_updated: 2026-07-30
  source_doc: docs/architecture/psychiatric_failure_modes.md
  scope_claims: [INV-053, INV-054, MECH-186, MECH-187, MECH-188, Q-034,
                 INV-061, MECH-200, MECH-201, MECH-202,
                 MECH-203, MECH-204,
                 INV-062, MECH-205, MECH-206, MECH-207, MECH-208, MECH-209, MECH-210,
                 INV-064, MECH-214, MECH-215,
                 SD-036, MECH-279,
                 MECH-285, MECH-286, MECH-094, MECH-281,
                 SD-034, MECH-260, MECH-266, SD-045, SD-046,
                 MECH-343, Q-056]
  nodes:
    - id: "clinical_failure_modes:MOTIVATIONAL-TAXONOMY"
      title: "2x2 motivational state taxonomy + three-stage pipeline (depression / GAD)"
      status: partial
      severity: high
      join:
        scope_claims: ["INV-053", "INV-054", "MECH-186", "MECH-187", "MECH-188", "Q-034"]
      unblocks_claims: [INV-054, MECH-186, MECH-187, MECH-188]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "SPLIT NODE. The attractor is the best-evidenced object in this
        whole lane -- INV-053 is `stable`, 7 experimental entries, 7 PASS / 0 FAIL,
        exp_conf 0.775, confirmed_established. The PIPELINE that is supposed to explain
        it is not: MECH-186 0 PASS / 2 FAIL, MECH-188 0 PASS / 1 FAIL, MECH-187 1 PASS,
        INV-054 (depressive maintenance loop) 0 PASS / 3 FAIL. So the phenomenon
        replicates and the proposed mechanism keeps failing -- that gap, not the
        attractor, is what this node tracks. Note the source doc marks MECH-186/187/188
        as V4 scope while claims.yaml has all three at implementation_phase v3; that
        disagreement is itself unresolved."
    - id: "clinical_failure_modes:CATATONIA-II"
      title: "Catatonia subtype II: harm-stream lock-in (SD-036 decay regulator, MECH-279 PAG freeze gate)"
      status: partial
      severity: high
      join:
        scope_claims: ["SD-036", "MECH-279"]
      unblocks_claims: [SD-036]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "INVERTED PAIR -- the consumer is validated, the regulator it
        depends_on has never been tested. MECH-279 (PAG freeze gate) is `provisional`,
        promoted 2026-07-18 on V3-EXQ-776 PASS (3 signatures x 5/5 seeds),
        confirmed_established, exp_conf 0.746. SD-036 (the cross-stream decay regulator,
        which MECH-279 lists in depends_on) is `candidate` with ZERO experimental
        entries -- 0 runs, 0 PASS, 0 FAIL, exp_conf 0.0, plausible_unproven. The
        471/475/483/490 cohort that was supposed to test it was voided by the
        update_z_goal TypeError contamination and never replaced; V3-EXQ-776 does not
        close the gap (its manifest mentions gaba_tone as a freeze-gate parameter but
        never use_gabaergic_decay and never z_harm). The pre-registered SD-036 test is
        already written -- docs/architecture/sd_036_gabaergic_decay_regulator.md
        'Predicted observables', observables 1-3: lock resolution, the gaba_tone
        {0.3,0.5,1.0,1.5,2.0} dose-response (the actual falsifier), and the multi-stream
        cluster at 0.3 that discriminates SD-036 from per-stream decay. Observable 4 is
        the one that ran (as 776). Buildable now: REEConfig.gaba_tone (default 1.0,
        range [0,2]), set_gaba_tone(), per-stream tau_z_harm_s/a/beta all exist."
    - id: "clinical_failure_modes:OCD-THREE-LAYER"
      title: "OCD as a three-layer architectural failure"
      status: partial
      severity: high
      join:
        scope_claims: ["SD-034", "MECH-260", "MECH-266", "SD-045", "SD-046"]
      unblocks_claims: [MECH-260, SD-045, SD-046]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "Best-developed syndrome account in the lane and still thin on
        experiment. SD-034 `provisional`, 1 PASS, confirmed_established (exp_conf 0.696).
        MECH-266 `provisional` but on ZERO experimental entries -- promoted without an
        experiment. MECH-260 `candidate`, 0 PASS / 1 FAIL. SD-045 and SD-046 are v4-phase
        and untested. The doc carries an explicit 'Claims NOT covered' section, which is
        the right shape and is why this is `partial` rather than `open`."
    - id: "clinical_failure_modes:PTSD-HYPERAROUSAL-INSOMNIA"
      title: "Hyperarousal insomnia and schema-repair starvation (PTSD chronicity)"
      status: partial
      severity: medium
      join:
        scope_claims: ["MECH-285", "MECH-286", "MECH-094"]
      unblocks_claims: [MECH-286]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "MECH-094 `stable` (2 PASS, confirmed_established) and MECH-285
        `candidate` but confirmed_established on 1 PASS (exp_conf 0.692). MECH-286
        (the hyperarousal/schema-repair-starvation half, and the claim the PTSD-chronicity
        account actually turns on) has ZERO experimental entries. The doc separately
        distinguishes this from the INV-054 depressive-maintenance loop and from acute
        insomnia; those distinctions are architectural, not yet empirical."
    - id: "clinical_failure_modes:DREAM-PHENOMENOLOGY"
      title: "Dream phenomenology as diagnostic and treatment-response marker"
      status: partial
      severity: medium
      join:
        scope_claims: ["INV-062", "MECH-205", "MECH-206", "MECH-207", "MECH-208", "MECH-209", "MECH-210"]
      unblocks_claims: [INV-062, MECH-206, MECH-208, MECH-209, MECH-210]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "One of seven claims carries the node: MECH-205 is `stable`,
        3 experimental entries, 2 PASS / 1 FAIL, confirmed_established. INV-062 and
        MECH-206/207/208/209/210 all have ZERO experimental entries (MECH-207 is v4).
        The four dream types and their computational signatures are specified in the
        doc; only the first has been probed."
    - id: "clinical_failure_modes:SEROTONERGIC-CROSS-STATE"
      title: "Serotonergic cross-state architecture (replay salience tagging, REM-gate zero-point)"
      status: in_progress
      severity: medium
      join:
        scope_claims: ["MECH-203", "MECH-204"]
      unblocks_claims: [MECH-203]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "The only node in this lane with live in-flight work, which is why
        it is in_progress rather than open. MECH-204 has 5 experimental entries but 1 PASS
        / 4 FAIL (exp_conf 0.506) -- being actively probed and mostly failing. MECH-203
        has ZERO experimental entries and an auto-spawned IGW /queue-experiment assignment
        open against it (IGW-20260730-214, claimed 2026-07-30T18:55Z). The doc's framing
        is that MECH-186/187/188 are 'incomplete without their sleep-state counterparts',
        so this node and MOTIVATIONAL-TAXONOMY fail or close together."
    - id: "clinical_failure_modes:FRAME-TAG"
      title: "Frame-tag failure modes: derealization, delusion, commitment-gate (developmental etiology)"
      status: open
      severity: high
      join:
        scope_claims: ["INV-061", "MECH-200", "MECH-201", "MECH-202"]
      unblocks_claims: [INV-061, MECH-200, MECH-201, MECH-202]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "ENTIRELY UNTESTED: all four claims have ZERO experimental
        entries. This is the lane's largest untested block and arguably its highest-value
        one -- MECH-200 (real->synthetic confusion) and MECH-201 (synthetic->real) are a
        directional PAIR sharing one architectural substrate (INV-061), so a single
        experiment that moves the frame-tag in both directions bears on three claims at
        once. MECH-202 is separately load-bearing: the doc's catatonia section defines
        subtype II specifically BY its distinction from MECH-202 Direction B, so
        SD-036/MECH-279 rest on a distinction whose other half has no evidence."
    - id: "clinical_failure_modes:SELF-MODEL-DEGRADATION"
      title: "Self-model failure modes: E1 schema poverty vs E2 capacity degradation"
      status: open
      severity: medium
      join:
        scope_claims: ["INV-064", "MECH-214", "MECH-215"]
      unblocks_claims: [INV-064, MECH-214, MECH-215]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "All three claims have ZERO experimental entries; MECH-214 and
        MECH-215 are implementation_phase v4, so this node is not V3-actionable as it
        stands. The architectural distinction (schema poverty vs capacity degradation)
        and its treatment implications are specified but unprobed."
    - id: "clinical_failure_modes:NARCOLEPSY-CATAPLEXY"
      title: "Narcolepsy and cataplexy: bilateral orexin-loss failure"
      status: open
      severity: low
      join:
        scope_claims: ["MECH-281", "MECH-286"]
      unblocks_claims: [MECH-281]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "Both claims have ZERO experimental entries. The doc carries an
        unusually specific set of DISSOCIATION predictions, which is the cheap way in:
        a dissociation is falsifiable without needing the full syndrome to be produced.
        Shares MECH-286 with PTSD-HYPERAROUSAL-INSOMNIA, so one MECH-286 experiment
        moves two nodes."
    - id: "clinical_failure_modes:PROPOSAL-ENTROPY"
      title: "Difficulty-gated proposal entropy: stuck-state cognition (working hypothesis)"
      status: open
      severity: low
      join:
        scope_claims: ["MECH-343", "Q-056"]
      unblocks_claims: [MECH-343, Q-056]
      depends_on: []
      last_updated: 2026-07-30
      completion_note: "Zero experimental entries on both. The source doc labels this a
        working hypothesis rather than a registered account, and Q-056 is an open
        question, so `open` here is the honest resting state and not a stalled gap."
    - id: "clinical_failure_modes:PHARMACOLOGICAL-PREDICTIONS"
      title: "Pharmacological predictions registry + receptor-subtype resolution layer"
      status: tracked
      severity: medium
      join:
        scope_claims: []
      unblocks_claims: []
      depends_on: ["clinical_failure_modes:CATATONIA-II",
                   "clinical_failure_modes:SEROTONERGIC-CROSS-STATE",
                   "clinical_failure_modes:MOTIVATIONAL-TAXONOMY"]
      last_updated: 2026-07-30
      completion_note: "A REGISTRY, not a claim -- `tracked` is the correct status, and
        this node deliberately owns no scope_claims. It is the lane's convergence point:
        every syndrome node above emits drug-response predictions into it (the
        gaba_tone benzo-analog dose-response from CATATONIA-II is the concrete worked
        case), and the 2026-06-12 receptor-subtype resolution layer is where those
        predictions get sharpened from 'serotonergic' to a subtype. Its value is
        cross-cutting falsifiability: a registry of pharmacological predictions is the
        cheapest external check this architecture can offer, because the clinical
        literature has already run the experiments."
---

# Psychiatric Failure Modes -- Programme Board

Board view for [`docs/architecture/psychiatric_failure_modes.md`](../../docs/architecture/psychiatric_failure_modes.md)
(1361 lines, first registered 2026-04-06 from EXQ-237a). The frontmatter above is
what the closure map renders; this body is the reading guide.

## Why this lane exists

The psychiatric material had no board. Its claims were scattered across the V3,
V4 and V5 lanes by implementation phase, which is the wrong axis for it: a
syndrome is a **clinical object**, and its claims land in whatever generation
their substrate happens to belong to. Catatonia subtype II is the clean example
-- SD-036 is `v3`, and the self-model failure modes it needs to be distinguished
from (MECH-214/215) are `v4`. Filing by generation splits every syndrome.

It is equally not `governance` (that lane is the SENT-*/GOV-* ethics perimeter),
not `process` (infrastructure owning no science), and not `deferred` (nothing
here is parked by commitment -- it is unbuilt or untested, which is the
opposite). Hence a lane of its own, excluded from the V3 closure % like every
other non-v3 lane.

## What the board says, as of 2026-07-30

Read across the eleven nodes and the programme has one dominant feature:

**21 of the 35 scope claims have zero experimental entries.** Not weak evidence
-- none. The lane's total experimental base is carried by six claims: INV-053
(7 entries, 7 PASS), MECH-205 (3, 2 PASS), MECH-094 (2 PASS), MECH-279, MECH-285
and SD-034 (1 PASS each).

Three further patterns are worth naming, because each is a different kind of
debt and they want different responses:

1. **Phenomenon replicates, mechanism keeps failing.** INV-053 is the
   best-evidenced claim in the lane (7/7 PASS). The three-stage pipeline that
   is supposed to explain it runs 1 PASS / 6 FAIL across MECH-186/187/188 and
   INV-054. This is not missing evidence; it is evidence pointing the other way.
2. **Consumers validated ahead of the mechanisms they depend on.** MECH-279 is
   `provisional` and confirmed_established while SD-036 -- which it lists in
   `depends_on` -- has never been tested. MECH-266 is `provisional` on zero
   experimental entries. A promotion that outruns its own substrate is a
   different failure from a claim that was never probed.
3. **Whole syndromes at zero.** FRAME-TAG (4 claims), SELF-MODEL-DEGRADATION (3),
   NARCOLEPSY-CATAPLEXY (2) and PROPOSAL-ENTROPY (2) have no experimental
   contact at all.

## Cheapest next moves

Not a queue -- these are the places where one experiment moves more than one
node, which is the only ordering argument the board itself can make:

- **SD-036 dose-response.** Fully specified since 2026-04-22 (observables 1-3 of
  the design doc), never run, and buildable today -- `gaba_tone`, `set_gaba_tone()`
  and the per-stream taus all exist. Closes the inverted pair in CATATONIA-II and
  feeds the benzo-analog row of PHARMACOLOGICAL-PREDICTIONS.
- **A frame-tag directional experiment.** MECH-200 and MECH-201 are opposite
  directions on one substrate (INV-061), so a single experiment that moves the
  tag both ways bears on three claims -- the best claims-per-run ratio in the lane.
- **Any MECH-286 experiment.** It is shared by PTSD-HYPERAROUSAL-INSOMNIA and
  NARCOLEPSY-CATAPLEXY, so it moves two nodes.

## Status derivation

Node statuses come from claims.yaml `status` plus `genuine_exp_count` /
`pass_runs` / `fail_runs` in `evidence/experiments/claim_evidence.v1.json`, read
2026-07-30. **Literature confidence is deliberately not counted** toward a node
status: this programme reports lit and exp evidence separately, and several
claims here have high literature confidence with no experiment (SD-036 sits at
lit_conf 0.805 / exp_conf 0.0). A syndrome supported only by literature is
`open`, not `partial`. Per-node `completion_note` carries the counts so the
board is auditable against its sources rather than taken on trust.
