---
closure_plan:
  id: biology_grounding_convergence_v4
  generation: v4
  title: "Biology-Grounding Convergence (ARC-106 forward roadmap)"
  registered: 2026-06-20
  last_updated: 2026-07-24
  scope_claims: [ARC-106, MECH-439, SD-034, MECH-090, MECH-436, ARC-035, SD-011]
  sibling_plans: [behavioral_diversity_isolation, commitment_closure, drives_motivation_v4, goal_deliberation_v4, ethics_perimeter]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. Tracks the ARC-106 grounding programme:
    moving each functional component from its current grounding level toward L3
    (divergence-audited AND validated on a REE falsifier). This is a DISTINCT
    concern from the per-component substrate plans -- it tracks GROUNDING-LEVEL
    transitions and validation, not the substrate build itself -- so nodes
    cross_plan_link the owning substrate plan rather than duplicate it. Nodes
    carry no owner_exq; each node's readiness_gate lists the V3-era prerequisite
    that must land before that component's grounding can honestly advance (that
    prerequisite IS the deferral). generation: v4 keeps these nodes OUT of the V3
    closure percentage (serve.py read_closure, generate_closure_snapshot.py and
    check_closure_drift.py are all generation-aware). Design doc:
    docs/architecture/arc_106_biology_grounding_framework.md. The convergence
    backlog source is brain_region_map.yaml non_anatomy_prefixes (the components
    deliberately left unmapped). A node graduates from roadmap to closure-tracked
    by gaining an owner_exq once its first grounding-validation experiment is
    queued -- EXCEPT BG-2, whose validation is already V3-owned by
    behavioral_diversity_isolation:GAP-I (it mirrors, never duplicates).
    PULL-INTO-V3: generation is per-plan (generate_closure_snapshot.py reads it at
    the plan level and stamps every node), so a node that becomes REQUIRED to
    close a V3 node is NOT retagged in place here. It is instantiated as a node in
    the OWNING v3 closure plan (where it counts toward the V3 %) and the backlog
    node becomes its cross_plan_link mirror -- exactly the BG-2 <-> GAP-I pattern,
    already live. Trigger = phase-label-follows-dependency (work that blocks a v3
    closure node IS v3 by definition; enrichment is recouped to V3).
  nodes:
    - id: "biology_grounding_convergence_v4:BG-1"
      title: "Grounding method + standing constraint (the framework itself)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-106]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Grounding ladder L0 ungrounded -> L1 functional-analogy-named -> L2 literature-anchored -> L3 divergence-audited-and-validated-on-a-REE-falsifier"
        - "Load-bearing-vs-decorative ablation test; 4 anti-cargo-cult guardrails; living divergence ledger; REQUIRED per-component psychiatric-failure-mode column"
      last_updated: 2026-06-20
      completion_note: >
        DONE 2026-06-20. ARC-106 registered (architectural_commitment,
        substrate_coherence) + design doc
        docs/architecture/arc_106_biology_grounding_framework.md authored
        (REE_assembly master ae66798e88). Construction-time complement to the
        registration-time biology-before-formal-definitions rule. This node
        anchors the plan; the BG-2..BG-7 nodes are the convergence backlog it
        spawns.
    - id: "biology_grounding_convergence_v4:BG-2"
      title: "Action selector (E3) grounding L2 -> L3 [V3 instance -- mirrors GAP-I (falsifier front) + GAP-J (build front)]"
      phase: 2
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-439, ARC-107, MECH-448, MECH-449]
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["behavioral_diversity_isolation"]
      readiness_gate:
        - "V3-OWNED by behavioral_diversity_isolation:GAP-I (falsifier front, generation:v3) AND behavioral_diversity_isolation:GAP-J (the ARC-107 BG-selector-constitution BUILD front, generation:v3, lead MECH-448 / follow-on MECH-449). This node MIRRORS that grounding-level status and does NOT duplicate or own it -- no owner_exq, generation:v4"
        - "Neural analog: basal-ganglia disinhibitory competition (direct/indirect Go-NoGo + hyperdirect/STN conflict-graded hold + pallidal permission gate), NOT argmax-over-value. Divergence: deterministic argmin over a near-monopolised scalar F (88-89% committed-selection variance, V3-EXQ-571)"
        - "L2 -> L3 transition: 689a SETTLED no-lift (conflict-grade near-tie family exhausted; A1B1 0/3) => escalate to the rank-preserving F->eligibility demotion build (MECH-448) carried by GAP-J. GAP-J's MECH-448 falsifier PASSED as V3-EXQ-689d (2026-06-21: committed-class entropy strict-above both collapsed controls, reaching the proposer ceiling; acceptance arc_107_selector_constitution_design_2026-06-20.md s4 MET) and GAP-J went status:done on that PASS. 689d was then WITHDRAWN 2026-07-20 (failure_autopsy_V3-EXQ-689d_2026-07-20, non_contributory/measurement_test_design_defect: hold-weighted DV + a matched-noise control bit-identical to its own baseline; MECH-448 reverted provisional->candidate in claims.yaml). The repaired-instrument successor V3-EXQ-689i (confirmed 2026-07-24, user-adjudicated 'gate defect, science upheld') closes the defects 689d's own autopsy identified and RECONFIRMS C_PRIMARY (committed-class entropy strict-above both collapsed controls) cleanly -- 6 of 8 load-bearing criteria pass, including C_PRIMARY, C_RANK_PRESERVING and C_SAFETY. This restores the L3-advancing criterion this node names, on valid grounds, with 689i superseding the withdrawn 689d as its evidentiary basis. The two gates 689i did NOT clear (C_NOISE_LIFTS -- a first-use Factor-B noise-control power gap; C_READINESS -- a comparator-direction ambiguity needing a script read) are instrument-side per the autopsy's four-layer diagnosis, not the mechanism test. V3-EXQ-689j (queued 2026-07-24) is a TARGETED, non-gating follow-up repowering ONLY C_NOISE_LIFTS (2 arms / 12 seeds, ARM_ON/ARM_OFF dropped entirely) -- it explicitly does NOT retest C_PRIMARY and does not bear on this transition. L3 is REACHED on GAP-J's build-validation front specifically (this node mirrors GAP-J status:done); the broader GAP-I falsifier front (downstream generalisation of the F-dominance conversion across behavioural channels beyond GAP-A) stays in-progress separately and was never what this node's L2->L3 criterion gated on -- only GAP-J's MECH-448 discrimination test was. CAVEAT: GAP-J's own plan-doc text (last_updated 2026-06-21) has not itself been reconciled for the 689d-withdrawal/689i-restoration cycle and still cites only 689d as if unwithdrawn -- a staleness gap in the owning node, flagged here but NOT corrected (do not edit GAP-I/GAP-J from this plan)"
      last_updated: 2026-07-24
      completion_note: >
        L2 -> L3 REACHED 2026-07-24, mirroring GAP-J status:done. The selector
        is the worked example of the framework and the only currently-V3
        slice. Its grounding convergence (F->eligibility-set + stochastic-commit)
        is the F-dominance campaign: the GAP-I falsifier front (689a settled
        no-lift, 2026-06-20) plus the GAP-J build front (ARC-107 BG-selector
        constitution; MECH-448 rank-preserving F->eligibility demotion lead,
        MECH-449 Go/No-Go follow-on). GAP-J's MECH-448 falsifier PASSED as
        V3-EXQ-689d (2026-06-21), was WITHDRAWN 2026-07-20 on a measurement
        defect (hold-weighted DV + a vacuous matched-noise control;
        failure_autopsy_V3-EXQ-689d_2026-07-20), and was RESTORED on a repaired
        instrument by V3-EXQ-689i (confirmed 2026-07-24, "gate defect, science
        upheld" -- C_PRIMARY passes cleanly, 6/8 load-bearing criteria).
        V3-EXQ-689j (queued 2026-07-24) is a narrow open follow-up on 689i's
        one instrument-side gap (Factor-B noise-control power); it does not
        retest C_PRIMARY and does not reopen this transition. CLAIM PROMOTION
        IS SEPARATE from grounding level (same pattern as BG-4): MECH-448's
        claims.yaml `status` field stays `candidate` pending a full governance
        re-promotion pass, though `live_status.reading` already reads
        `provisional` as of 689i (2026-07-24) -- the L3 grounding criterion
        (divergence-audited AND validated on a REE falsifier) is satisfied
        independent of that formal claim-status lag. BG-3's live-grounding-front
        trigger ("FIRED: 689a routed readiness-met/no-lift") already fired
        independently in 2026-06-20 on 689a's routing verdict alone -- it does
        NOT depend on 689i's PASS or on this node reaching done; the two are
        separate triggers that happen to share the BG-2 depends_on edge. This
        node exists only so the grounding programme is visible as a whole. Do
        not edit GAP-I or GAP-J from here -- the live F-dominance campaign owns
        them; GAP-J's own text is flagged (not fixed) as stale for the
        689d-withdrawal/689i cycle. Reconcile session festive-moser-b1aebf,
        2026-07-24.
    - id: "biology_grounding_convergence_v4:BG-3"
      title: "Commitment / de-commit latch grounding L1 -> L3"
      phase: 3
      status: in_progress
      severity: high
      owner_exq: null
      unblocks_claims: [SD-034, MECH-090]
      depends_on: ["biology_grounding_convergence_v4:BG-2"]
      cross_plan_link: ["commitment_closure"]
      readiness_gate:
        - "Neural analog: BG/thalamic commit + maintenance-release. Divergence: beta-gate refractory dynamics are tuned, not bio-sourced"
        - "Biology lit-pull on commit/maintenance-release dynamics owed before any refractory re-grounding (biology-before-formal-definitions) -- DONE 2026-06-20, evidence/literature/targeted_review_commit_release_duration_latch/ (5 anchors; L1->L2 reached; load-bearing divergence D1 = duration set by tuned refractory vs biology's graded urgency/behaviour-co-extensive maintenance)"
        - "Gated behind BG-2: if 689a routes readiness-met-no-lift, the blocker is here (the commit latch), and this node becomes the live grounding front -- FIRED: 689a routed readiness-met/no-lift 2026-06-20, BG-3 is now the live grounding front"
      last_updated: 2026-06-20
      completion_note: >
        SD-034 / MECH-090 / MECH-342 (+ MECH-445 / MECH-446) cluster.
        Refractory-too-long maps to rigidity/perseveration; too-short maps to
        distractibility/disorganisation (psychiatric column). Owning substrate work
        is commitment_closure_plan; this node tracks the grounding-validation step only.
        GROUNDING L1->L2 DONE 2026-06-20 (lit-pull triggered by 689a readiness-met/no-lift):
        evidence/literature/targeted_review_commit_release_duration_latch/SYNTHESIS.md --
        5 anchors (Resulaj 2009 change-of-mind/de-commit; Jin 2014 BG start/stop +
        sustained maintenance; Thura 2022 commitment-as-state-transition + urgency-set
        timing; Loh/Rolls/Deco 2007 one-stability-parameter -> both psychiatric poles;
        Seif 2025 catatonia = No-Go over-pressure over-maintenance pole). Each cluster
        component now has >=1 biological anchor; the load-bearing divergence (D1: REE
        times the hold with a tuned committed-run-scaled refractory, biology times it
        with a graded BG/pallidal urgency signal and/or behaviour-co-extensive
        maintenance) is stated with a named falsifier; the two-poled psychiatric column
        is anchored. Status open->in_progress (L2 reached). L2->L3 is gated on a REE
        falsifier, NOT more literature: the 460i-successor (refractory-independent /
        graded-release lever vs the fixed refractory) on the f_dominance_conversion_ceiling
        commit-entry-decisiveness rung -- which is itself gated behind the GAP-I
        selection-face front (do NOT queue on the current selector before GAP-I closes).
        Distinct from the SELECTION-face grounding (targeted_review_connectome_mech_439,
        ARC-107 MECH-448/449); cross-referenced where the No-Go/indirect pathway is the
        shared locus of the over-maintenance pole.
    - id: "biology_grounding_convergence_v4:BG-4"
      title: "Drive / incentive salience grounding L2 -> L3"
      phase: 3
      status: done
      severity: medium
      owner_exq: "V3-EXQ-514u"
      unblocks_claims: [MECH-436]
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["drives_motivation_v4"]
      readiness_gate:
        - "Neural analog: mesolimbic incentive salience (wanting != liking). Divergence AUDITED: the scalar kappa gain was FALSIFIED as non-monotone/exhausted across the 514r/s/t lineage (doubling kappa REGRESSED the delta; the 'needs more kappa' prediction is dead) -- the diagnosed ceiling was the MEASUREMENT layer (an argmax-flip gate discarding continuous sub-flip re-weighting), not the substrate"
        - "FIRED: the V3-EXQ-514u measurement-redesign (continuous incentive-amplitude readout at moderate kappa <= 6.0 on the SD-049-PHASE-2 enriched substrate) LANDED PASS/supports and was reviewed + governance-applied 2026-06-21 -- mean continuous amplitude shift 0.164 > 0.05 floor on all scored seeds (k_sd 1.0, n=76), enriched per-axis drive spread 0.222 > 0.1, OFF/argmax-relevance readiness all met. MECH-436 substrate ceiling LIFTED (epistemic_category substrate_ceiling -> standard; pending_retest_after_substrate cleared). L2 -> L3 reached on the load-bearing INTENSITY disjunct (incentive-salience amplitude ~ base_value*(1+kappa*per_axis_drive))"
      last_updated: 2026-07-07
      completion_note: >
        DONE 2026-07-07 (plan reconcile; PROMOTES NOTHING). L2 -> L3 grounding
        transition FIRED. The divergence (REE's scalar kappa gain vs mesolimbic
        incentive salience) was divergence-AUDITED to falsification of the scalar-
        gain sub-claim (514r/s/t: kappa-magnitude lever non-monotone/exhausted;
        the ceiling was re-diagnosed to the argmax-flip measurement layer), and
        the replacement continuous-amplitude reading was then VALIDATED ON A REE
        FALSIFIER -- V3-EXQ-514u (supersedes 514t; PASS, supports, non_degenerate;
        reviewed + /governance-applied 2026-06-21) cleared the drive-coupling
        effect margin on the enriched substrate. That is the L3 definition
        (divergence-audited AND validated on a REE falsifier), met on the claim's
        load-bearing INTENSITY disjunct. RESIDUAL (does not block L3, recorded for
        honesty): the SECONDARY discrete target-FLIP disjunct still fails at
        natural magnitude (mean wl_drive_delta -0.133) -- only the overshoot
        positive control flips most_wanted (0.81); this is a magnitude artifact,
        NOT a falsification (drive re-weights wanting INTENSITY toward the depleted
        axis but does not re-select the argmax target without overshoot). CLAIM
        PROMOTION IS SEPARATE from grounding level: MECH-436 stays candidate /
        v3_pending: true (hold_pending_v3_substrate) -- the 514u amplitude reading
        was sufficient to lift the ceiling and reach L3 grounding, NOT to promote
        the claim. Psychiatric column intact (wanting-liking dissociation ->
        addiction; flat wanting -> apathy). owner_exq set to V3-EXQ-514u per the
        roadmap_note graduation rule (first grounding-validation experiment has run
        + been applied); generation stays v4, so this node remains OUT of the V3
        closure %. Owning substrate work is drives_motivation_v4_plan /
        SD-049-PHASE-2 (the differential-depletion + bounded-kappa env amend that
        514u ran on). NOTE for a future session: because 514u is a V3 falsifier and
        MECH-436 is implementation_phase v3, this grounding could be pulled fully
        into V3 (instantiate a counted V3 node) IF MECH-436's promotion becomes
        required to close a live V3 node -- not done here (the claim is v3_pending-
        held and closes no V3 node today; phase-label-follows-dependency has not
        fired).
    - id: "biology_grounding_convergence_v4:BG-5"
      title: "Goal / wanting layer grounding L1 -> L2 [L2 REACHED 2026-07-07 via on-file anchors]"
      phase: 4
      status: in_progress
      severity: medium
      owner_exq: null
      unblocks_claims: []
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["goal_deliberation_v4"]
      readiness_gate:
        - "Neural analog (function level): frontal goal-directed control -- vmPFC/dlPFC/dACC goal encoding + routing, ventral-striatal / mesolimbic-dopamine effort-based goal-directed action initiation, and the current-concern commit->pursue->disengage lifecycle. Distinct from BG-4 (drive / incentive-salience GAIN knob): BG-5 owns the goal-LIFECYCLE face, BG-4 owns the amplitude face -- flagged so the two rows do not double-count the shared 'wanting' construct"
        - "L1 -> L2 REACHED 2026-07-07 (IGW-20260707-036 plan-reconcile; GDL-8 no-re-pull pattern -- anchors were already on file, ASSEMBLED here rather than re-pulled to avoid double-count): the defining constraint is literature-sourced and the divergences are IDENTIFIED (not yet tested), per S4.1. Anchors: (frontal goal encoding) targeted_review_frontal_goal_grounding -- Spellman 2015 HPC->PFC rich encoding-write / Ito 2015 PFC->reuniens->HPC compact-handle goal-directed retrieval / Schmitt 2017 MD-thalamic sustaining gain / Hallock 2016 demand-conditional thalamic gate / Baram 2020 vmPFC abstract task-graph store; (goal-directed effort + clinical poles) targeted_review_goal_disengagement -- Husain & Roiser 2018 apathy/anhedonia = effort-based decision-making breakdown across ventral striatum / vmPFC-ACC / mesolimbic DA; (current-concern lifecycle) Klinger 1975 commit-onset -> consummation-OR-disengagement-offset, obstruction-appraisal trigger; Brandstaetter 2013 action-crisis = disengagement is a contested state, within-crisis goal-devaluation is NOT the trigger; (goal maintenance / progress proxy) targeted_review_proxy_progress_goal_maintenance -- Carver 1990 velocity-affect loop / Sutton 1988 TD-value-as-progress-proxy / Bandura 1981 proximal subgoals; (wanting!=liking, shared with BG-4) Berridge & Robinson 1998 / Dickinson & Balleine 1994"
        - "Load-bearing divergence D1 (stated, not yet tested): REE's goal/wanting layer represents wanting as a scalar drive-gain x static goal value and treats goal maintenance/abandon as a THRESHOLD / one-shot flag; biology times goal-directed pursuit as a current-concern STATE whose offset is gated by an obstruction-appraisal -- NOT a value-drop or accumulated-cost tally -- with an effort-cost computation that is value-relative and continuously recomputed. A static-threshold abandon lands ON a clinical pole by construction (see psychiatric column). Secondary divergence D2: REE frontal goal encoding is a single compact z_goal handle on slow EMA; biology splits rich encoding-write (Spellman) from compact goal-directed retrieval (Ito), adds a demand-conditional thalamic gate (Hallock) + an abstract task-graph store (Baram vmPFC) -- REE collapses these into one channel (the frontal_goal_grounding review's event-gated-rich-write / structural-encoding V4 scoping)"
        - "Psychiatric failure-mode column (two-poled, required per S7): OVER-disengagement pole = apathy / anhedonia / avolition (effort-cost overweighted or reward sensitivity blunted; goal abandoned while its outcome is still valued) -- Husain & Roiser 2018. UNDER-disengagement pole = perseverative striving / rumination (stuck in the invigoration phase) and clinical depression (abandonment arrested without redirection) -- Klinger 1975, Brandstaetter 2013. The abandon trigger must occupy the band BETWEEN the two poles"
        - "L2 -> L3 gate (named falsifier, NOT more literature): an obstruction-appraisal-gated-abandon vs static-threshold-abandon falsifier -- does a disengage/abandon trigger keyed on obstruction-appraisal (vs value-drop or cost-tally) yield adaptive disengagement bounded STRICTLY between the apathy pole and the perseveration pole? Testable only once the goal layer holds a parked goal slot to abandon/redirect BETWEEN (goal_deliberation_v4 GDL-1 multi-slot + GDL-5 interrupt/reorient/resume). Off the V3 critical path; BG-5 stays sequenced behind BG-2 (goal->committed-action conversion rides the same E3 gate) and its owning substrate is v4"
      last_updated: 2026-07-07
      completion_note: >
        GROUNDING L1 -> L2 REACHED 2026-07-07 (IGW-20260707-036 plan-reconcile;
        PROMOTES NOTHING -- no claims.yaml touch). Status open -> in_progress.
        The goal/wanting layer already had comprehensive literature on file across
        four targeted reviews (frontal_goal_grounding, goal_disengagement,
        proxy_progress_goal_maintenance, wanting_liking synthesis); per the GDL-8
        precedent (do not re-pull anchors already on file, to avoid double-count)
        this pass ASSEMBLES them into the ARC-106 goal/wanting grounding rather
        than commissioning a fresh pull. Each face of the layer -- frontal goal
        encoding/routing, effort-based goal-directed initiation, the
        current-concern commit->pursue->disengage lifecycle, goal maintenance --
        now carries >=1 biological anchor; the load-bearing divergence D1
        (static-threshold/one-shot abandon vs obstruction-appraisal-gated
        current-concern state) is stated with a named falsifier; the two-poled
        psychiatric column (apathy/anhedonia over-disengagement pole vs
        perseverative-striving/arrested-depression under-disengagement pole) is
        anchored. L2 -> L3 is gated on a REE falsifier (the obstruction-appraisal
        abandon test), NOT more literature, and that falsifier needs the v4
        goal-deliberation substrate (GDL-1 multi-slot + GDL-5 interrupt/resume) to
        have a parked slot to abandon/redirect between -- so it stays off the V3
        critical path. Owning substrate work is goal_deliberation_v4 (cross_plan_link;
        GDL-8 grounded the DELIBERATION cluster claims) / goal_pipeline. ARC-106
        design-doc S5 ledger gains a goal/wanting row and S9 C4 moves L1 -> L2 /
        open -> in-progress in the same pass (S10.3 zero-silent-divergence). BG-4
        <-> BG-5 boundary: BG-4 owns the incentive-salience GAIN face (kappa knob,
        divergence-audited to falsification), BG-5 owns the goal-LIFECYCLE face --
        same 'wanting' construct at cue vs goal granularity, kept as two rows so
        neither double-counts the other's grounding.
    - id: "biology_grounding_convergence_v4:BG-6"
      title: "Attention (distributed precision-selection) grounding -- containment, not a module"
      phase: 4
      status: blocked
      blocker_class: v4_scope
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: []
      blocking_on: "Attention is already distributed across ARC-005 / MECH-251 / MECH-254 / MECH-255 / MECH-259 / MECH-261 / MECH-347 / SD-032a / SD-057. The missing work is a unifying MAP, not a substrate. Containment-only for V3: do NOT build a parallel attention module; ground only on a specific failure."
      readiness_gate:
        - "Reuse-before-duplicate guardrail (G2): attention functions are already implemented; grounding = a unifying functional map, not a new module"
      last_updated: 2026-06-20
      completion_note: >
        Tracks the attention non_anatomy_prefix. Deferred and containment-only --
        a map node, not a build node. Promotes nothing.
    - id: "biology_grounding_convergence_v4:BG-7"
      title: "Ethics / commitment policy grounding (or honest 'no clean analog')"
      phase: 5
      status: blocked
      blocker_class: v5_scope
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["ethics_perimeter"]
      blocking_on: "The ethics/governance layer is a non_anatomy_prefix the atlas deliberately leaves unmapped; the ethics perimeter is generation v4/v5/v6 and non-blocking for the V3 green-board."
      readiness_gate:
        - "Function-ground each ethics/commitment-policy component OR record 'no clean neural analog' (honest, per the psychiatric-column guardrail) -- a speculative disorder mapping that would mislead a clinician is worse than none"
      last_updated: 2026-06-20
      completion_note: >
        Lowest-priority, latest-generation grounding node. Owning governance work
        is ethics_perimeter_plan (generation governance/v5).
---
# Biology-Grounding Convergence -- ARC-106 Forward Roadmap

**Registered:** 2026-06-20
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Design doc:** [arc_106_biology_grounding_framework.md](../../docs/architecture/arc_106_biology_grounding_framework.md)
**Claim:** ARC-106 (architectural_commitment, substrate_coherence)

## What this plan is

ARC-106 makes biology-grounding a standing construction constraint. The
constraint itself is not a closure gap -- it is a policy that persists, so it
gets no V3 node. This plan tracks the **convergence programme** the constraint
spawns: moving each functional component from its current grounding level toward
**L3** (divergence-audited and validated on a REE falsifier), per the design
doc's S9 roadmap.

It is a *forward roadmap*, not a closure map. It tracks a concern distinct from
the per-component substrate plans -- **grounding-level transitions and
validation**, not the substrate build -- so each node `cross_plan_link`s the
owning substrate plan rather than duplicating it. `generation: v4` keeps every
node out of the V3 closure percentage.

## The deferral structure

Each node's `readiness_gate` is the V3-era prerequisite that must land before
that component's grounding can honestly advance. That prerequisite **is** the
deferral:

- **BG-2 (selector)** -- the only currently-V3 slice -- mirrors
  `behavioral_diversity_isolation:GAP-I` (falsifier front) and `:GAP-J` (build
  front). L2->L3 DONE 2026-07-24: 689a settled no-lift on the near-tie family,
  escalating to GAP-J's MECH-448 rank-preserving demotion build, whose
  falsifier reached a confirmed PASS on C_PRIMARY via V3-EXQ-689i (2026-07-24,
  repaired-instrument successor to the withdrawn V3-EXQ-689d). V3-EXQ-689j
  (queued 2026-07-24) is a narrow, non-gating follow-up on a residual
  noise-control instrument gate only.
- **BG-3 (commitment latch)** was gated behind BG-2: if 689a routes
  readiness-met-no-lift, the blocker is the latch and BG-3 becomes the live
  front -- FIRED 2026-06-20 on 689a's routing verdict alone, independent of
  BG-2's later GAP-J outcome.
- **BG-4 (drive)** -- L2 -> L3 DONE 2026-07-07. Was gated on the V3-EXQ-514u
  measurement-redesign (the scalar gain knob was falsified); 514u LANDED
  PASS/supports and was governance-applied 2026-06-21 (MECH-436 ceiling lifted),
  reaching L3 on the load-bearing intensity disjunct.
- **BG-5 (goal / wanting)** -- L1 -> L2 REACHED 2026-07-07. The goal/wanting
  layer's defining constraint is now literature-anchored by assembling on-file
  reviews (frontal_goal_grounding, goal_disengagement, proxy_progress,
  wanting_liking) rather than a fresh pull (GDL-8 no-re-pull pattern); its
  load-bearing divergence (static-threshold abandon vs obstruction-appraisal-gated
  current-concern state) and two-poled psychiatric column (apathy vs
  perseverative-striving/arrested-depression) are stated. L2 -> L3 is gated on the
  obstruction-appraisal abandon falsifier, which needs the v4 goal-deliberation
  substrate (GDL-1 multi-slot + GDL-5 interrupt/resume) -- off the V3 critical path.
- **BG-6 (attention)**, **BG-7 (ethics)** are later-generation and mostly
  map-not-build; both are explicitly containment-only / honest-no-analog.

## Promotion to V3 (pull-in path)

If a grounding node turns out to be **required for V3 completion** (not merely a
better-finish enrichment), it is pulled into V3 like this -- `generation` is a
**per-plan** field, so you never just retag one node here:

1. **Trigger.** The node's grounding work becomes a prerequisite for closing a
   live V3 closure node. By `phase-label-follows-dependency`, that work is V3 by
   definition (a heavier rung needed to lift a V3 node is recouped to V3).
2. **Instantiate in the owning V3 plan.** Add the work as a node in the V3
   closure plan that owns the component (e.g. `commitment_closure_plan` for BG-3,
   the relevant V3 node for BG-4) with an `owner_exq`. *There* it counts toward
   the V3 closure %.
3. **Demote this node to a mirror.** The BG node here becomes a `cross_plan_link`
   pointer to the new V3 node (status `in_progress`, `owner_exq: null`), so the
   programme stays legible end-to-end without double-counting.

This is not hypothetical: **BG-2 ↔ `behavioral_diversity_isolation:GAP-I`/`:GAP-J`
is the pattern already running.** The selector grounding was the first node to
be V3-required; it lives as counted V3 nodes in GAP-I (falsifier front,
in-progress) and GAP-J (build front, done), and BG-2 is their mirror --
reaching L2->L3 itself on 2026-07-24 once GAP-J's build-validation front
(MECH-448, confirmed on the repaired-instrument V3-EXQ-689i) went done, per
the BG-2 node's own text. BG-3 (commitment) followed the same trigger
structure, but on its own separate condition -- it fired the moment 689a
itself routed readiness-met-no-lift (2026-06-20), not when BG-2 later reached
done. BG-4
(drive) has reached L3 grounding on a V3 falsifier (514u, applied 2026-06-21) but
is NOT pulled into V3: MECH-436 is v3_pending-held and closes no live V3 node
today, so phase-label-follows-dependency has not fired -- it stays a graduated
(owner_exq V3-EXQ-514u) but generation-v4 node, out of the V3 %. Each BG node's
`readiness_gate` already names the V3-era prerequisite that fires the trigger.

## Convergence backlog source

The backlog is `docs/architecture/brain_region_map.yaml` `non_anatomy_prefixes`
(ethics / love / play / language / goal / commitment / attention / self / drive)
-- the components the atlas deliberately leaves unmapped. As each is grounded to
L3, this roadmap is its tracking home until (if ever) it earns an `owner_exq`.
