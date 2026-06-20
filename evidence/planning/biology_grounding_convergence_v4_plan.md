---
closure_plan:
  id: biology_grounding_convergence_v4
  generation: v4
  title: "Biology-Grounding Convergence (ARC-106 forward roadmap)"
  registered: 2026-06-20
  last_updated: 2026-06-20
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
      title: "Action selector (E3) grounding L2 -> L3 [V3 instance -- mirrors GAP-I]"
      phase: 2
      status: in_progress
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-439]
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["behavioral_diversity_isolation"]
      readiness_gate:
        - "V3-OWNED by behavioral_diversity_isolation:GAP-I (generation:v3, owner V3-EXQ-689a). This node MIRRORS that grounding-level status and does NOT duplicate or own it -- no owner_exq, generation:v4"
        - "Neural analog: basal-ganglia disinhibitory competition (hyperdirect/STN conflict-graded hold), NOT argmax-over-value. Divergence: deterministic argmin over a near-monopolised scalar F (88-89% committed-selection variance, V3-EXQ-571)"
        - "L2 -> L3 transition gated on 689a's load-bearing/gap-concentrated verdict: gap-concentrated lift => L3 (import validated); uniform lift => decorative, escalate to rank-preserving F->eligibility demotion; readiness-met-no-lift => blocker downstream (commit latch, BG-3)"
      last_updated: 2026-06-20
      completion_note: >
        The selector is the worked example of the framework and the only
        currently-V3 slice. Its grounding convergence (F->eligibility-set +
        stochastic-commit) is the existing GAP-I campaign; this node exists only
        so the grounding programme is visible as a whole. Do not edit GAP-I from
        here -- the live F-dominance campaign owns it.
    - id: "biology_grounding_convergence_v4:BG-3"
      title: "Commitment / de-commit latch grounding L1 -> L3"
      phase: 3
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [SD-034, MECH-090]
      depends_on: ["biology_grounding_convergence_v4:BG-2"]
      cross_plan_link: ["commitment_closure"]
      readiness_gate:
        - "Neural analog: BG/thalamic commit + maintenance-release. Divergence: beta-gate refractory dynamics are tuned, not bio-sourced"
        - "Biology lit-pull on commit/maintenance-release dynamics owed before any refractory re-grounding (biology-before-formal-definitions)"
        - "Gated behind BG-2: if 689a routes readiness-met-no-lift, the blocker is here (the commit latch), and this node becomes the live grounding front"
      last_updated: 2026-06-20
      completion_note: >
        SD-034 / MECH-090 / MECH-342 cluster. Refractory-too-long maps to
        rigidity/perseveration; too-short maps to distractibility/disorganisation
        (psychiatric column). Owning substrate work is commitment_closure_plan;
        this node tracks the grounding-validation step only.
    - id: "biology_grounding_convergence_v4:BG-4"
      title: "Drive / incentive salience grounding L2 -> L3"
      phase: 3
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-436]
      depends_on: ["biology_grounding_convergence_v4:BG-1"]
      cross_plan_link: ["drives_motivation_v4"]
      readiness_gate:
        - "Neural analog: mesolimbic incentive salience (wanting != liking). Divergence: scalar kappa gain -- FALSIFIED as non-monotone/exhausted (V3-EXQ-514t regressed the delta)"
        - "Re-ground after the V3-EXQ-514u measurement-redesign (continuous incentive-amplitude readout) lands"
      last_updated: 2026-06-20
      completion_note: >
        Wanting-liking dissociation maps to addiction; flat wanting maps to
        apathy (psychiatric column). The gain-knob grounding is falsified; the
        open question is whether a continuous-amplitude readout grounds it. Owning
        substrate work is drives_motivation_v4_plan / SD-049-PHASE-2.
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
- **BG-4 (drive)** is gated on the V3-EXQ-514u measurement-redesign (the scalar
  gain knob is already falsified).
- **BG-5 (goal)**, **BG-6 (attention)**, **BG-7 (ethics)** are later-generation
  and mostly map-not-build; BG-6/BG-7 are explicitly containment-only / honest-no-analog.

## Convergence backlog source

The backlog is `docs/architecture/brain_region_map.yaml` `non_anatomy_prefixes`
(ethics / love / play / language / goal / commitment / attention / self / drive)
-- the components the atlas deliberately leaves unmapped. As each is grounded to
L3, this roadmap is its tracking home until (if ever) it earns an `owner_exq`.
