---
closure_plan:
  id: hippocampal_planning_v4
  generation: v4
  title: "Hippocampal dorsal/ventral planning + multi-step planning depth (V4 roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [ARC-040, INV-039, MECH-147, MECH-148, MECH-149, MECH-163, MECH-207, MECH-241, MECH-242, MECH-243]
  sibling_plans: [goal_pipeline, object_representation_v4, sleep_substrate]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 substrate step is honest to build. generation: v4
    keeps these nodes OUT of the V3 closure percentage (serve.py read_closure,
    generate_closure_snapshot.py, and check_closure_drift.py are all
    generation-aware). A node graduates from roadmap to closure-tracked by
    gaining an owner_exq once its first V4 experiment is queued.
    THE LOAD-BEARING GATE for this whole plan is MECH-163 (dual-system
    architecture): it is tagged implementation_phase: v3 -- it is the V3
    COMPLETION gate, not a V4 step -- and the multi-step hippocampally-planned
    system it names is the substrate every node below specialises. Until the
    VTA/hippocampal planned system is validated in V3, none of the V4
    enrichments (dorsal/ventral split, pattern separation, time cells, novelty
    gate, schema-priming, compression, dual-mode construction, approach-bias
    pathway) have a substrate to enrich. MECH-163 also unblocks the V5 social
    tier (prosocial planning has no substrate without it).
  nodes:
    - id: "hippocampal_planning_v4:HPL-1"
      title: "GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)"
      phase: 1
      status: blocked
      blocker_class: v3_gate
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-163]
      depends_on: []
      cross_plan_link: ["goal_pipeline:GAP-2"]
      blocking_on: "MECH-163 is implementation_phase: v3 and held under hold_pending_v3_substrate (9 lit supports, 0 genuine exp entries). The VTA/hippocampal model-based system (goal-seeded proposal generation + multi-step rollout) has no V3 discrimination evidence; EXQ-237a was non_contributory (z_goal substrate limit). z_goal->approach propagation is the live bottleneck (640a autopsy; substrate_queue modulatory-bias-selection-authority). [UPDATE 2026-07-24: leg-1's V3-EXQ-786a recruitment-DV result was WITHDRAWN by failure_autopsy_V3-EXQ-786a_2026-07-24_dv_degeneracy -- the DV read world_seq[:, :1, :] (the pre-action state, shared by every candidate before divergence), so it was structurally constant and the reported score measured stable-sort tie-break noise, not discrimination. MECH-163 leg-1 reverts to experimentally-untested. Repaired retest V3-EXQ-786b queued 2026-07-24 (ree-v3 2f43287cb6; coordinator DB queue entry live) with a fixed DV (HABIT_DEPTH=2 + new cross-candidate-range/distinct-value readiness gates); PENDING, not yet run. HPL-1 stays BLOCKED until it completes -- owner_exq stays null per this plan's convention (reserved for a queued V4 node experiment, not a V3-gate leg).]"
      readiness_gate:
        - "MECH-163 dual-system discrimination demonstrated in V3 (habit SNc/dorsal-striatum model-free vs VTA/hippocampal model-based): the planned system must show it can navigate to states a 1-step greedy policy cannot reach"
        - "z_goal must be competitive with harm salience at E3 selection (goal_pipeline:GAP-2 foraging contact + the modulatory-bias-selection-authority substrate item); without it the planned system is observationally indistinguishable from habit [READINESS MET 2026-06-16: goal_pipeline:GAP-2 CLOSED (status done) 2026-06-15 via V3-EXQ-514o PASS -- object-bound wanting!=liking dissociation demonstrated at E3, both readiness gates met, non_degenerate. This sub-gate is now satisfied. HPL-1 still BLOCKED on the remaining two refs: MECH-163 dual-system discrimination (candidate, phase v3, no V3 evidence) and ARC-071 transition machinery (candidate, v3_pending). Does not graduate the node.]"
        - "ARC-071 (composition_via_repeated_grounding, v3) -- the planned->habitual transition machinery MECH-163 presupposes -- landed so the division of labour is a continuum, not a static config"
      last_updated: 2026-07-24
      completion_note: "This is the ONLY node whose claim is implementation_phase: v3. It is the gate, not a V4 step: every V4 node below depends on it. Listed here so the plan's entry condition is explicit and so the V5 social tier's dependency on MECH-163 is visible from this plan."
    - id: "hippocampal_planning_v4:HPL-2"
      title: "PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)"
      phase: 2
      status: blocked
      blocker_class: sibling_node
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-040]
      depends_on: ["hippocampal_planning_v4:HPL-1"]
      cross_plan_link: []
      blocking_on: "V3 HippocampalModule is undifferentiated; segregation cannot be tested until the planned system (HPL-1 / MECH-163) is real. ARC-040 also depends on Q-020 (resolved Path A 2026-03-29) -- not a blocker -- and on ARC-007's no-new-value constraint, which the dorsal trajectory proposer must respect."
      readiness_gate:
        - "MECH-163 planned system validated (HPL-1): there must be a model-based trajectory proposer to split"
        - "R(x,t) residue-field geometry stable enough to source a ventral-analog valence PRIOR (accumulated, not computed on-the-fly) -- depends on sustained V3 training producing a dense map"
        - "ARC-007 strict-mode preserved: the dorsal proposer navigates existing R(x,t) terrain value-free; the ventral prior is segregated, not merged (a single undifferentiated module would violate ARC-007)"
      last_updated: 2026-06-10
      completion_note: "ARC-040 is the architectural keystone of this plan: it asserts the dorsal value-free trajectory proposer and ventral valence-prior must be ARCHITECTURALLY SEGREGATED. V3's undifferentiated module is an acceptable simplification that systematically underweights valence in trajectory selection until this lands."
    - id: "hippocampal_planning_v4:HPL-3"
      title: "DG-equivalent pattern separation before rollout proposal (MECH-147)"
      phase: 3
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-147]
      depends_on: ["hippocampal_planning_v4:HPL-1"]
      cross_plan_link: []
      blocking_on: "Requires SD-004 (action-object hippocampal map backbone, v3) and the kernel-chaining interface MECH-033; the sparse-expansion layer must precede a proposal generator that exists (HPL-1)."
      readiness_gate:
        - "SD-004 action-object hippocampal map backbone present (v3) and the MECH-033 kernel-chaining interface live as the proposal-generation path"
        - "z_world regions with measurable topological similarity exist in the trained map (so the lure/repeat collapse MECH-147 predicts is observable)"
        - "ablation harness: removing the DG-equivalent layer should collapse trajectory DIVERSITY specifically in high-similarity z_world regions without degrading quality in already-distinct regions"
      last_updated: 2026-06-10
      completion_note: "MECH-147 (Sakon & Suzuki 2019): a DG-equivalent sparse expansion layer must precede the trajectory proposer so similar z_world seeds do not collapse to near-identical rollouts. Operates on the SEED state; relies on E2 forward dynamics to amplify initial separation over rollout steps."
    - id: "hippocampal_planning_v4:HPL-4"
      title: "Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)"
      phase: 3
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-148]
      depends_on: ["hippocampal_planning_v4:HPL-1"]
      cross_plan_link: []
      blocking_on: "Requires the SD-004 hippocampal architecture and ARC-039 offline replay; multi-step rollouts (HPL-1) must exist before a per-step elapsed-time tag has anything to weight."
      readiness_gate:
        - "ARC-018 rollout viability module + ARC-039 offline replay live (both v3): E3 must already weight multi-step rollout outcomes for a temporal-distance signal to matter"
        - "discrete-step rollouts long enough that delayed-vs-immediate outcomes diverge (harm at step 3 vs step 15 along identical z_world paths)"
        - "ablation prediction: removing the time-coding layer should impair LONG-horizon credit assignment without degrading short-horizon evaluation"
      last_updated: 2026-06-10
      completion_note: "MECH-148 (Omer/Las/Ulanovsky 2022): a context-independent pure-elapsed-time layer tags each simulated rollout step regardless of z_world, so E3 discounts delayed outcomes instead of being step-local-myopic. The social-coding variant (time cells for another agent's events) is the bridge to multi-agent temporal credit (MECH-127), pulling this toward the V5 tier."
    - id: "hippocampal_planning_v4:HPL-5"
      title: "CA1 mismatch novelty gate on rollout injection (MECH-149)"
      phase: 3
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-149]
      depends_on: ["hippocampal_planning_v4:HPL-1"]
      cross_plan_link: []
      blocking_on: "Requires SD-004 and a differentiable CA1-mismatch signal (E1-predicted vs CA3-retrieved z_world) in the latent stack; MECH-022 hypothesis-injector + MECH-075 dopaminergic gain must be wired."
      readiness_gate:
        - "differentiable CA1 mismatch signal computable in the latent stack (E1 prediction error at the z_world level)"
        - "cached rollout-viability estimates exist (MECH-075) so the low-mismatch branch has something to fall back on instead of always proposing fresh"
        - "continuous (non-binary) gate: rollout injection frequency + diversity scale with mismatch magnitude"
      last_updated: 2026-06-10
      completion_note: "MECH-149 (Lisman & Grace 2005): the CA1 match-mismatch signal gates WHEN the hippocampus injects fresh proposals. High mismatch (novel) -> more, more-diverse proposals; low mismatch (familiar) -> rely on cached viability. The VTA->hippocampus arm IS the MECH-075 dopaminergic modulation of attractor stickiness (exploration/exploitation in rollout sampling)."
    - id: "hippocampal_planning_v4:HPL-6"
      title: "ACh permissive write-gate on the surprise buffer (MECH-207)"
      phase: 3
      status: blocked
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-207]
      depends_on: ["hippocampal_planning_v4:HPL-1"]
      cross_plan_link: ["sleep_substrate"]
      blocking_on: "Depends on MECH-205 surprise buffer + MECH-206 CA1 comparator + MECH-178 REM/NE replay gating -- the offline-consolidation stack owned by the sleep_substrate plan. This is the OPENING side of plasticity gating (state-conditional write), distinct from the closure side REE already owns."
      readiness_gate:
        - "MECH-205 surprise buffer + MECH-206 CA1 PE comparator present (sleep_substrate stack)"
        - "a basal-forebrain-analog ACh state signal exists to gate which PE-tagged episodes become eligible for offline updating (PE necessary but not sufficient)"
        - "two-gate separation honoured: NE/REM (MECH-178) controls WHEN offline replay occurs; ACh (MECH-207) controls WHICH episodes are eligible -- independent axes"
      last_updated: 2026-06-10
      completion_note: "MECH-207 (Sinclair 2021): ACh is the permissive write-gate on the surprise buffer. Cross-links the sleep_substrate plan (offline consolidation) and is the OPENING side of state-conditional plasticity REE currently lacks (closure side = EWC/MECH-333/334). Medium severity -- an efficiency/selectivity gate, not a prerequisite for basic planning."
    - id: "hippocampal_planning_v4:HPL-7"
      title: "Schema-primed rapid assimilation (INV-039)"
      phase: 4
      status: blocked
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [INV-039]
      depends_on: ["hippocampal_planning_v4:HPL-2"]
      cross_plan_link: ["sleep_substrate"]
      blocking_on: "Emergent invariant from ARC-007 + ARC-038; carries pending_substrate_reconfirmation. Requires a STABLE residue-field map (sustained V3 training) and ARC-039 offline replay before map-stability-gated consolidation is measurable."
      readiness_gate:
        - "stable, dense residue-field map from sustained V3 training (a sparse/unstable map reverts to slow multi-episode consolidation by construction)"
        - "the hippocampal module exposes a map-stability signal (coverage density / rollout-viability consistency over recent episodes) to the consolidation controller"
        - "E3 control plane actively GATES schema use (the mPFC role in Tse 2007), not passively receiving hippocampal output"
      last_updated: 2026-06-10
      completion_note: "INV-039 (Tse 2007): consolidation rate is dynamically gated by schema stability -- a mature map should consolidate new episodes without the full multi-episode warmup. Emergent invariant, so it cannot be cited as supporting evidence until governance reconfirms its emergent_from substrates (ARC-007/ARC-038) are active. Depends on HPL-2 because schema stability is a property of the segregated value/navigation map."
    - id: "hippocampal_planning_v4:HPL-8"
      title: "Improvement-tier enrichments -- compression, dual-mode construction, approach-bias pathway (MECH-241/242/243)"
      phase: 4
      status: deferred
      blocker_class: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-241, MECH-242, MECH-243]
      depends_on: ["hippocampal_planning_v4:HPL-2"]
      cross_plan_link: []
      blocking_on: "All three are self-described IMPROVEMENT-TIER: basic goal-directed navigation works without them (MECH-230/236/238 are sufficient, all v3). They are deferred until the base planned system + segregation (HPL-1/HPL-2) exist and a richer multi-action-dimension substrate is available (MECH-243 is untestable in the single-action-channel CausalGridWorld)."
      readiness_gate:
        - "MECH-230/236/238 V3 navigation substrate present (metric-space goal encoding) -- the base these enrichments improve"
        - "MECH-241 goal-state compression: a multi-distractor / long-path environment where a sharper goal gradient measurably improves convergence; resolve the causal-vs-consequence question (Muhle-Karbe is correlational)"
        - "MECH-242 dual-mode construction: a zero-shot-transfer / compositional-planning harness (novel environments not in the training map) to make vector-based construction necessary vs pattern completion"
        - "MECH-243 approach-bias output pathway: a richer substrate where approach (move-toward) and avoidance (move-away) are independent output dimensions during simultaneous motivational conflict"
      last_updated: 2026-06-10
      completion_note: "Grouped as deferred because all three are explicitly improvement-tier in claims.yaml and share the same gate (base navigation substrate + a richer action/environment substrate). MECH-243 in particular is untestable until approach and avoidance are separable output channels -- the current single-action-dimension substrate conflates them."
    - id: "hippocampal_planning_v4:HPL-9"
      title: "Biology grounding completion (DG separation / time cells / CA1 novelty / ACh write-gate / dorsal-ventral lit-pulls + circuit completion-set harvest)"
      phase: 2
      status: done
      lit_pull_status: done
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-147, MECH-148, MECH-149, MECH-207, ARC-040]
      depends_on: []
      cross_plan_link: ["sleep_substrate"]
      readiness_gate:
        - "L1 DG pattern separation (Sakon & Suzuki 2019; Leutgeb 2007) -- AND harvest the completion-set: hilar mossy-cell feedback inhibition + CA3 recurrent-collateral pattern COMPLETION are co-constitutive of the separation property; building a DG expansion layer without the inhibitory/completion partners will not yield the claimed property"
        - "L2 pure time cells (Omer/Las/Ulanovsky 2022; Eichenbaum 2014) + theta-gamma phase-coding partner; L3 CA1 match-mismatch novelty (Lisman & Grace 2005) + VTA dopaminergic loop partner (MECH-075)"
        - "L4 ACh permissive write-gate (Sinclair 2021; Hasselmo 2006) + septohippocampal cholinergic projection source; L5 dorsal/ventral segregation (Fanselow & Dong 2010; Strange 2014)"
      last_updated: 2026-06-13
      lit_pull_done:
        - "2026-06-13 /lit-pull -> evidence/literature/targeted_review_hippocampal_planning_mechanisms (9 entries, two passes). Pass 1 (6 entries) grounded the core: MECH-147 (Leutgeb 2007 DG/CA3 dual mechanism = separation + CA3-COMPLETION partner; Bakker 2008 human CA3/DG-sep vs CA1-completion); MECH-148 (Omer/Las/Ulanovsky 2022 pure-vs-contextual time cells + social time-cell = V5/MECH-127 bridge); MECH-149+MECH-075 (Lisman & Grace 2005 hippocampal-VTA loop = novelty detector + VTA-DA gain as ONE circuit); ARC-040 (Fanselow & Dong 2010 dorsal-cognitive/ventral-affective segregation)."
        - "Pass 2 (3 entries) closed the remaining debt: MECH-207 directionality RESOLVED by Sinclair 2021 PNAS primary (PE disrupts sustained hippocampal representations AND the PE->update relationship DEPENDS ON concurrent basal-forebrain/cholinergic activation = the permissive write-gate; reconciles Hasselmo's low-ACh-consolidation as a DIFFERENT operation, not a contradiction) -> MECH-207 lit_conf 0.56->0.75, supports. Completion-set partners grounded as standalone entries: hilar mossy-cell feedback inhibition / DG E-I-balance control (Hashimotodani 2017 Neuron) for MECH-147 (->0.835); theta-gamma ORDINAL sequence code (Lisman & Buzsaki 2008), the ordering partner complementary to MECH-148's metric elapsed-time core (->0.782)."
      lit_pull_remaining:
        - "DONE for grounding purposes. Residual (non-blocking, for the substrate-BUILD phase, not the grounding phase): Sinclair's cholinergic gate is fMRI-correlational (basal-forebrain BOLD as ACh proxy) -- a causal cholinergic x PE manipulation would strengthen MECH-207 before the gate is built; and the theta-gamma partner is ORDINAL (item rank) vs MECH-148's METRIC elapsed-time, so the substrate must keep them as complementary signals, not conflate them."
      completion_note: "Hippocampal_planning had NO dedicated grounding node at registration. DONE as of 2026-06-13 across two /lit-pull passes (9 entries): all five claims grounded (lit_conf MECH-147 0.835 / MECH-148 0.782 / MECH-149 0.72 / MECH-207 0.75 / ARC-040 0.75) AND every co-constitutive circuit partner the assembly brief named is harvested (CA3 completion, VTA-DA gain loop, hilar mossy-cell inhibition, theta-gamma ordering, basal-forebrain cholinergic gate). The one MIXED entry (Hasselmo 1999) is retained as honest record alongside the Sinclair 2021 supports that resolved the directionality. Off the V3 closure path (generation v4); promotes nothing (exp_conf unchanged 0). The substrate-BUILD readiness gate remains MECH-163/HPL-1 (V3 completion) -- grounding being done does not unblock the build."
---
# Hippocampal Planning -- V4 Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the V4 enrichments of the REE hippocampal planning module --
dorsal/ventral functional segregation (ARC-040), the four lit-pull mechanism
gates (DG pattern separation, pure time cells, CA1 novelty gate, ACh write-gate),
schema-primed assimilation (INV-039), and the three improvement-tier refinements
(compression, dual-mode construction, approach-bias pathway) -- all behind the
single load-bearing V3-completion gate MECH-163.

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant against them. The
value is the **readiness gates** -- for each enrichment, exactly which V3-era
prerequisites (claims/tracks) must land before the V4 substrate step is honest
to build.

---

## One-line framing

> REE already names a hippocampal planning module, but in V3 it is
> undifferentiated and runs a value-flat proposal-then-score loop. The whole V4
> enrichment programme -- dorsal/ventral split, DG pattern separation, time
> cells, novelty gate, schema-priming, compression, dual-mode construction,
> approach-bias channel -- is a specialisation of ONE thing that does not yet
> exist in validated form: the multi-step, goal-seeded, model-based planned
> system of MECH-163. MECH-163 is the gate; everything else is its anatomy.

---

## The gate and the pillars

| Node | Claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|
| HPL-1 (GATE) | MECH-163 | **V3 completion** | dual-system discrimination in V3; z_goal competitive at E3 (goal_pipeline:GAP-2); ARC-071 transition machinery |
| HPL-2 (PILLAR) | ARC-040 | V4 | HPL-1 planned system real; stable R(x,t) for ventral prior; ARC-007 strict segregation |
| HPL-3 | MECH-147 | V4 | SD-004 map backbone + MECH-033 chaining; similar z_world regions to disambiguate |
| HPL-4 | MECH-148 | V4 (-> V5 via MECH-127) | ARC-018 rollouts + ARC-039 replay; horizons long enough for delayed-outcome divergence |
| HPL-5 | MECH-149 | V4 | differentiable CA1 mismatch signal; cached viability (MECH-075) for the low-mismatch branch |
| HPL-6 | MECH-207 | V4 (sleep cross-link) | MECH-205/206 surprise-buffer stack; basal-forebrain ACh-analog state signal |
| HPL-7 | INV-039 | V4 (sleep cross-link) | stable dense map; map-stability signal to consolidation controller; E3 gates schema use |
| HPL-8 | MECH-241/242/243 | V4 (improvement-tier) | MECH-230/236/238 base navigation; richer multi-action-dimension substrate |

---

## What this plan deliberately does NOT pull into V3

- **MECH-163 is the gate, not new V4 work.** It is `implementation_phase: v3`
  and is the V3 FULL-completion requirement. This plan lists it as HPL-1 so the
  entry condition is explicit, but closing it is V3 work owned by the
  goal-pipeline / dual-system thread, not a V4 substrate build.
- **No dorsal/ventral split, no DG/time/CA1/ACh layers, no schema-stability
  gating, no improvement-tier refinements enter V3.** The V3 undifferentiated
  value-flat HippocampalModule is the deliberate, ARC-007-compliant
  simplification. Registering this roadmap changes no V3 behaviour and adds no
  V3 closure node.
- **The improvement-tier trio (MECH-241/242/243) is not a near-term target.**
  All three are self-described improvement-tier; basic navigation works without
  them (MECH-230/236/238). They are deferred, not blocked, and MECH-243 is
  untestable on the current single-action-channel substrate.

---

## Cross-tier note (V5 social)

MECH-163's planned system is the substrate the V5 social tier depends on:
prosocial planning ("sharing joys and sorrows", INV-029 benefit gradient)
requires planning trajectories that affect ANOTHER agent's harm/benefit
accumulation over time, which is structurally inaccessible to a 1-step greedy
policy. MECH-148's social time-coding variant (time cells anchored to another
agent's events) and the MECH-127 multi-agent temporal-credit extension are the
explicit bridges. This plan does not own the social work, but its gate (HPL-1)
unblocks it.

---

## Source artefacts

| Artefact | Role |
|---|---|
| claims.yaml MECH-163 | the load-bearing V3-completion gate (dual-system architecture) |
| claims.yaml ARC-040 | dorsal/ventral functional segregation (the V4 architectural keystone) |
| claims.yaml MECH-147/148/149/207 | the four lit-pull mechanism gates (DG / time cells / CA1 novelty / ACh) |
| claims.yaml INV-039 | schema-primed rapid assimilation (emergent invariant, pending_substrate_reconfirmation) |
| claims.yaml MECH-241/242/243 | improvement-tier enrichments (compression / dual-mode / approach-bias pathway) |
| evidence/planning/goal_pipeline_plan.md (GAP-2) | the V3 foraging-contact + z_goal-authority substrate gating HPL-1 |
| evidence/planning/sleep_substrate_plan.md | the offline-consolidation stack (MECH-205/206/178) HPL-6 + HPL-7 cross-link |
| docs/architecture/sleep/offline_phases.md#mech-207 | MECH-207 ACh write-gate location |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap, sibling to
  object_representation_v4. Nodes seeded from ARC-040, INV-039, MECH-147/148/149,
  MECH-163, MECH-207, MECH-241/242/243. MECH-163 placed as the single
  load-bearing gate (HPL-1) and flagged as `implementation_phase: v3` (the V3
  completion requirement, not a V4 step). Readiness gates pinned per node;
  improvement-tier trio grouped as deferred. `generation: v4` set so the V3
  closure % is unaffected. No claims.yaml edits. Generation-flag raised on
  MECH-163: it is correctly v3 but is the gate this V4 plan hangs on -- noted
  for the orchestrator rather than edited.
