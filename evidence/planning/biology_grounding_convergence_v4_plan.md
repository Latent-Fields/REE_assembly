---
closure_plan:
  id: biology_grounding_convergence_v4
  generation: v4
  title: "Biology-Grounding Convergence (ARC-106 forward roadmap)"
  registered: 2026-06-20
  last_updated: 2026-07-07
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
      status: in_progress
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-439, ARC-107, MECH-448, MECH-449]
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["behavioral_diversity_isolation"]
      readiness_gate:
        - "V3-OWNED by behavioral_diversity_isolation:GAP-I (falsifier front, generation:v3) AND behavioral_diversity_isolation:GAP-J (the ARC-107 BG-selector-constitution BUILD front, generation:v3, lead MECH-448 / follow-on MECH-449). This node MIRRORS that grounding-level status and does NOT duplicate or own it -- no owner_exq, generation:v4"
        - "Neural analog: basal-ganglia disinhibitory competition (direct/indirect Go-NoGo + hyperdirect/STN conflict-graded hold + pallidal permission gate), NOT argmax-over-value. Divergence: deterministic argmin over a near-monopolised scalar F (88-89% committed-selection variance, V3-EXQ-571)"
        - "L2 -> L3 transition: 689a SETTLED no-lift (conflict-grade near-tie family exhausted; A1B1 0/3) => the import as a near-tie parametric tweak is NOT validated -> escalate to the rank-preserving F->eligibility demotion build (MECH-448) carried by GAP-J. L3 promotion now gated on GAP-J's MECH-448 falsifier, which is queued + in flight as V3-EXQ-689d (ree-v3 main 8d87d4a; coordinator DB pending ree-cloud-3; script experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py): a 689d PASS (committed-class entropy strict-above the conflict-grade controls >=2/3, acceptance arc_107_selector_constitution_design_2026-06-20.md s4) advances the selector grounding to L3. 689d PROMOTES NOTHING (MECH-448 stays candidate). 689c (Factor-B-alone, also in flight) does NOT gate build scope -- stripped of decision authority by the MECH-442 Section-7 fidelity steer (no-authority confirmatory data only; GAP-J governance_2026_06_20c)"
      last_updated: 2026-06-20
      completion_note: >
        The selector is the worked example of the framework and the only
        currently-V3 slice. Its grounding convergence (F->eligibility-set +
        stochastic-commit) is the F-dominance campaign: the GAP-I falsifier
        front (689a settled no-lift) plus the GAP-J build front (ARC-107
        BG-selector constitution; MECH-448 rank-preserving F->eligibility
        demotion lead, MECH-449 Go/No-Go follow-on). This node exists only so
        the grounding programme is visible as a whole. Do not edit GAP-I or
        GAP-J from here -- the live F-dominance campaign owns them.
        CROSS-LINK 2026-06-20: the MECH-448 falsifier that gates this node's
        L2->L3 transition is now queued as V3-EXQ-689d (mirrors GAP-J owner_exq;
        this node keeps owner_exq null by the v4-mirror design). No status change
        (stays in_progress; 689d PROMOTES NOTHING). Reconcile session
        reconcile-arc107-689d-closure-nodes-20260620T1934Z.
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
      title: "Goal / wanting layer grounding L1 -> L2"
      phase: 4
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: []
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["goal_deliberation_v4"]
      readiness_gate:
        - "Goal layer currently has no region map (non_anatomy_prefix 'goal'). First step is a function-grounding lit-pull, not a substrate build"
        - "Sequenced behind the selector (BG-2): goal->committed-action conversion rides the same E3 gate"
      last_updated: 2026-06-20
      completion_note: >
        Function-ground the goal/wanting layer (L1 -> L2). Off the V3 critical
        path; owning substrate work is goal_deliberation_v4 / goal_pipeline.
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

- **BG-2 (selector)** -- the only currently-V3 slice -- mirrors the live
  `behavioral_diversity_isolation:GAP-I` node (owner V3-EXQ-689a). It does not
  own or duplicate it. Its L2->L3 transition is gated on 689a's
  gap-concentrated-vs-uniform verdict (the framework's load-bearing test).
- **BG-3 (commitment latch)** is gated behind BG-2: if 689a routes
  readiness-met-no-lift, the blocker is the latch and BG-3 becomes the live front.
- **BG-4 (drive)** -- L2 -> L3 DONE 2026-07-07. Was gated on the V3-EXQ-514u
  measurement-redesign (the scalar gain knob was falsified); 514u LANDED
  PASS/supports and was governance-applied 2026-06-21 (MECH-436 ceiling lifted),
  reaching L3 on the load-bearing intensity disjunct.
- **BG-5 (goal)**, **BG-6 (attention)**, **BG-7 (ethics)** are later-generation
  and mostly map-not-build; BG-6/BG-7 are explicitly containment-only / honest-no-analog.

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

This is not hypothetical: **BG-2 ↔ `behavioral_diversity_isolation:GAP-I` is the
pattern already running.** The selector grounding was the first node to be V3-
required; it lives as a counted V3 node in GAP-I, and BG-2 is its mirror. BG-3
(commitment) follows the same route the moment 689a makes it V3-blocking. BG-4
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
