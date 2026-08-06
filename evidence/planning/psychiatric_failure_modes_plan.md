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
        it is not: MECH-186 0 PASS / 2 FAIL (2026-08-06 correction: those 2 FAILs were
        governance-reclassified non_contributory/substrate_limitation on 2026-04-08 --
        the reclassification was already applied to the flat manifests but had never
        propagated to the run-pack manifests or the derived claim_evidence.v1.json
        index, so exp_conf read 0.175/weakens=2 until the pack copies were re-synced
        and the index regenerated 2026-08-06; MECH-186 now correctly reads 0 genuine
        experimental entries either direction, confidence carried entirely by
        literature at 0.742), MECH-188 0 PASS / 1 FAIL, MECH-187 1 PASS, INV-054
        (depressive maintenance loop) 0 PASS / 3 FAIL. So the phenomenon replicates and
        the proposed mechanism remains untested-at-V3-scale (MECH-186) or failing
        (MECH-187/188/INV-054) -- that gap, not the attractor, is what this node
        tracks. V3-vs-V4 SCOPE RESOLVED 2026-08-06 (user decision): MECH-186/187/188
        are V3 scope, matching claims.yaml's implementation_phase -- the phase-label-
        follows-dependency rule applies (if a claim is needed to complete V3, it is V3
        scope regardless of what an older planning doc's framing says); the source
        doc's V4-scope framing is superseded and should not be treated as authoritative
        going forward."
    - id: "clinical_failure_modes:CATATONIA-II"
      title: "Catatonia subtype II: harm-stream lock-in (SD-036 decay regulator, MECH-279 PAG freeze gate)"
      status: partial
      severity: high
      join:
        scope_claims: ["SD-036", "MECH-279"]
      unblocks_claims: [SD-036]
      depends_on: []
      last_updated: 2026-08-01
      completion_note: "BLOCKER CLEARED, VALIDATION QUEUED AS V3-EXQ-854 -- awaiting
        evidence. Until 2026-08-01 this note declared the experiment un-buildable as
        pre-registered; both halves of that are now discharged. The defect that blocked
        observables 1-3 was FIXED in ree-v3 35e8969 (2026-08-01), and the experiment is
        queued as V3-EXQ-854 (ree-v3 81a447e867 + 56c33052a2, both on origin/main), which
        reuses the design block below verbatim. `status` stays `partial` until 854
        produces a manifest. The measurement record that follows is the durable finding
        and is retained in the PAST TENSE as a description of what the defect WAS.
        WHAT THE DEFECT WAS (measured 2026-07-31, session elated-germain-9aff71): the
        knobs existed but had NO TEMPORAL AUTHORITY over 2 of the 3 registered streams.
        SD-036's design (sd_036_gabaergic_decay_regulator.md, Mechanism 1) is
        autoregressive -- z_s(t+1) = z_s(t) * exp(-tau_s * gaba_tone). The wiring was
        not, for the harm streams: latent/stack.py set z_harm = harm_encoder(harm_obs)
        and z_harm_a = affective_harm_encoder(...), both PURE FEEDFORWARD from the
        current observation with no prev_state term -- unlike z_world/z_self/z_beta,
        which DID blend with prev_state. agent.py ticks the regulator on new_latent
        AFTER that encode, so for z_harm/z_harm_a the decay was a one-step constant
        rescale, DISCARDED when the next sense() re-encoded. z_s(t+1) was not a function
        of z_s(t) at all for those two streams.
        MEASURED, replaying ONE identical recorded observation sequence into agents
        differing only in gaba_tone (60 steps, seed 0, 471-lineage env): peak-normalised
        trajectory max-deviation vs tone=1.0 was <= 2.0e-07 for z_harm and <= 1.4e-07 for
        z_harm_a across tone in {0.0, 0.3, 1.0, 2.0} -- i.e. the trajectory SHAPE was
        bit-identical and only the scale moved, by exactly exp(-tau*delta_tone)
        (z_harm tone=0.0 ratio 1.05127107 vs exp(0.05)=1.0512711; tone=2.0 ratio
        0.95122942 vs exp(-0.05)=0.9512294; z_harm_a 1.02020133 / 0.98019867 vs
        exp(+-0.02)=1.020201/0.980199 -- 8 significant figures). tone=0.0 was bit-equal
        to decay-OFF. z_beta, which IS recurrent, behaved differently and correctly:
        peak-normalised max-dev 2.0e-02 to 2.9e-02 (5 orders of magnitude larger) and a
        raw ratio 1.0958 that does NOT reduce to a single-tick exp(0.03)=1.03045, so the
        decay genuinely compounded there. That z_harm-vs-z_beta contrast is what
        localised the defect.
        CONSEQUENCES that made it unbuildable as pre-registered. #1 (471 lock
        resolution): the lock is z_harm_norm pinned by a sustained ENVIRONMENT harm
        observation, and a constant per-tick rescale moved it from ~0.7 to ~0.666 and
        pinned it there -- it could not return to baseline. #2 (the gaba_tone
        dose-response, the registered falsifier) was STRUCTURALLY VACUOUS on the harm
        streams: any scale-free recovery DV (fraction-of-peak recovery time, half-life,
        and specifically harm_norm_sustain_ratio = mean/peak in
        _lib/goal_pipeline_tier1.py, the DV this experiment was expected to reuse) was
        EXACTLY invariant to gaba_tone because the constant cancels -- measured spread
        8.6e-08, a structural null and not a small effect. A fixed-ABSOLUTE-threshold DV
        would instead have shown a clean monotone dose-response, but as the trivial
        rescale rather than a decay-rate change: a confident-but-wrong confirmation, and
        the reason it was not queued as designed. #3 (the multi-stream cluster at tone
        0.3) would have fired, but for the wrong reason in 2 of 3 streams -- only z_beta
        responded genuinely -- so it could not discriminate regulator-layer from
        per-stream decay, which is its entire purpose.
        WHY THIS SURVIVED TO NOW: tests/contracts/test_sd_036_gabaergic_decay.py
        exercised decay only against a synthetic `_Latent()` stand-in re-ticked in place
        (C5/C6/C7), where compounding holds trivially. No test stepped a real REEAgent
        through sense() and asserted z_harm decays across ticks, so the gap between the
        autoregressive design and the feedforward wiring was never observable.
        MECH-279 WAS NEVER UNDERMINED: agent.py passes gaba_tone to PAGFreezeGate.tick()
        as a direct SCALAR (exit_threshold = theta_freeze * gaba_tone), never through the
        decay path, so V3-EXQ-776's PASS stands and 854 does not tag MECH-279.
        THE FIX (ree-v3 35e8969, 2026-08-01): a prev_state blend in encode(),
        z_s(t) = alpha_s*encode(obs_t) + (1-alpha_s)*z_s_decayed(t-1), which composes
        with the regulator's end-of-tick rescale into a leaky integrator with pole
        (1-alpha_s)*exp(-tau_s*gaba_tone) -- so gaba_tone now moves the trajectory SHAPE
        and not just its scale. The decay arithmetic STAYS IN THE REGULATOR; encode()
        supplies only the recurrence, preserving SD-036's `regulation lives at the
        regulator, not in each target` commitment. Post-fix sustain-ratio spread across
        the registered sweep is 1.4e-03 (z_harm) and 1.0e-01 (z_harm_a, monotone in
        tone), against the 8.6e-08 structural null above.
        DESIGN (unchanged, and reused VERBATIM by V3-EXQ-854): 2 trained agents per seed,
        decay-OFF vs decay-ON, then a set_gaba_tone() sweep over {0.3,0.5,1.0,1.5,2.0} on
        the trained ON agent, with use_pag_freeze_gate held OFF to de-confound from
        MECH-279.
        THREE POST-FIX CONSTRAINTS 854 ENCODES -- these CORRECT the design text above and
        must travel with it. (i) The CONTROL ARM is use_gabaergic_decay=False, NOT
        gaba_tone=0.0: post-fix, tone 0.0 suspends the decay but leaves the recurrence
        live, so tone 0.0 is no longer bit-equal to the legacy arm the way it was
        pre-fix. (ii) The PRIMARY DV is z_harm_a sustain ratio, not z_harm sustain ratio
        alone -- the z_harm effect is real but modest (spread 1.4e-03) beside z_harm_a
        (1.0e-01). (iii) OBSERVABLE #1 IS NOT ACHIEVABLE AS WORDED: the measured encoder
        floor (harm_norm ~0.509, from harm_encoder(zeros) ~0.46 / affective_harm_encoder
        (zeros,zeros) ~0.33) EXCEEDS the 471-lineage avoid threshold (0.25), so the mode
        lock cannot be resolved by ANY decay rate under that classifier -- decay reaches
        an equilibrium against the floor rather than returning to baseline, and the 471
        lock is substantially an ENCODER FLOOR response to the ambient hazard field
        rather than pure temporal persistence. 854 records this as
        `observable_1_reachability` and treats it as NON-GATING, alongside the 475-lineage
        mode readout, precisely so that avoid_frac=1.000 at every tone is not misread as a
        refutation of SD-036 while C1 concurrently shows the regulator working (smoke
        rho=-1.0).
        PRIOR CONTEXT (unchanged) -- INVERTED PAIR: the consumer is validated, the
        regulator it
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
      last_updated: 2026-08-01
      completion_note: "The only node in this lane with live in-flight work, which is why
        it is in_progress rather than open. MECH-204 has 5 experimental entries but 1 PASS
        / 4 FAIL (exp_conf 0.506) -- being actively probed and mostly failing. MECH-203's
        prior IGW auto-spawn (IGW-20260730-214) was abandoned mid-work and closed
        2026-08-01; a separate session finished the script and it is now queued as
        V3-EXQ-843 (ree-v3 main 1d9d451aee, SWS replay-selection dose-response over tonic
        5-HT; backing proposal EVB-0157 marked executed), coordinator-confirmed live in
        /queue/active but not yet run. The doc's framing is that MECH-186/187/188 are
        'incomplete without their sleep-state counterparts', so this node and
        MOTIVATIONAL-TAXONOMY fail or close together."
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
