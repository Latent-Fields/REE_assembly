---
closure_plan:
  id: memory_lifecycle_v4
  generation: v4
  title: "Memory Lifecycle: allocation gate + consolidation anti-overwrite + provenance/rollback (V4 roadmap)"
  registered: 2026-06-10
  last_updated: 2026-07-14
  scope_claims: [MECH-261, MECH-094, ARC-035, MECH-272, MECH-273, INV-039, INV-049, MECH-068, MECH-124, MECH-147, ARC-007, ARC-020, MECH-257, SD-017]
  sibling_plans: [sleep_substrate, hippocampal_planning_v4, self_model_v4, inference_belief_state_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 substrate step is honest to build. The recurring
    REE finding across both seed intakes is the same: REE already owns the
    GATES (MECH-094 / MECH-261 / ARC-035 / SD-016) but NOT the gating POLICY,
    and it has offline-consolidation infra (INV-039 / INV-049 / SD-017 /
    MECH-272 / MECH-273) but NO anti-overwrite / provenance / rollback
    discipline over it. generation: v4 keeps these nodes OUT of the V3 closure
    percentage (serve.py read_closure, generate_closure_snapshot.py, and
    check_closure_drift.py are all generation-aware). A node graduates from
    roadmap to closure-tracked by gaining an owner_exq once its first V4
    experiment is queued -- and per both intakes, that experiment must NOT be
    queued before the memory-lifecycle store substrate exists (vacuous-probe
    risk).
  nodes:
    - id: "memory_lifecycle_v4:MEM-1"
      title: "Allocation-gate decision stage on MECH-261 (integrate / partial_overlap / separate)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-261, MECH-391]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "V3 OWNS THE GATES already: MECH-094 (hypothesis tag = categorical write gate, stable), MECH-261 (mode-conditioned write gating, stable, implementation_phase v3) -- these are the actuators the policy steers, not the policy"
        - "ARC-035 (vmPFC stored->active converter, candidate) supplies the control-plane that would set thresholds + weights"
        - "DECISION the policy stage forces: the de Sousa 2026 inputs (context_similarity x temporal_distance interaction, schema_fit, salience, PE, uncertainty, goal_relevance) drive integrate vs partial_overlap vs separate -- temporal_distance x context_similarity must be an INTERACTION (similar contexts link even at 7 days), not additive (lit-pull verdict G3)"
        - "Lit DONE 2026-06-06: targeted_review_contextual_memory_allocation_gate VERDICT (de Sousa 2026 + Cai 2016 + Bakker 2008 + Tse 2007 + Sahay 2011; mean ~0.73; candidate-isolated)"
      last_updated: 2026-06-14
      completion_note: "Per the contextual-memory-allocation-gate intake (Section 3): the control-plane DECISION ALGORITHM for when to engage the existing gates is NOVEL (no current home). Verdict G1: amend MECH-261 with an allocation-decision stage rather than mint a new INV (subsumed by MECH-094/261 + INV-039). The policy is the work this node tracks; the gates it steers are V3-live. CLOSED 2026-06-14 (IGW plan reconcile, user-approved): the allocation-decision stage is registered as the distinct mechanism_hypothesis MECH-391 (substrate_conditional/v4, depends_on MECH-261) with exactly the named decision variables, and the false-linking cost as INV-079 -- both minted 2026-06-10, so registration IS the deliverable. Residual artifact added this pass: MECH-261 now carries a dated mem1_amendment_2026_06_14 note acknowledging the allocation-decision-stage extension and cross-referencing MECH-391 + INV-079 (the MECH-391->MECH-261 link was previously one-directional). No new claim minted; Verdict G1 honored (mechanism_hypothesis, not a new INV). exp_conf 0 -- PROMOTES NOTHING; DO NOT build in V3."
    - id: "memory_lifecycle_v4:MEM-2"
      title: "Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing"
      phase: 1
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-391]
      depends_on: ["memory_lifecycle_v4:MEM-1"]
      cross_plan_link:
        - "sleep_substrate"
        - "hippocampal_planning_v4:HPL-3"
      blocking_on: "MECH-147 (DG-mediated pattern separation, candidate, implementation_phase v4) is itself unbuilt in V3 -- there is no DG-like sparse non-redundant encoder of similar z_world. Active separation needs that substrate to write into."
      readiness_gate:
        - "MECH-147 DG pattern separation must land (V4): non-redundant sparse encoding of similar z_world before rollout"
        - "de Sousa 2026 open-question Q4: REE needs an explicit 'do not link' (separate) op distinct from 'no match' -- active separation, not just failed integration"
        - "SD-016 z_world-only cue-isolated query (the MEC-analog indexing layer this policy actuates against)"
      last_updated: 2026-06-10
      completion_note: "Intake Q4: active separation is a first-class output of the allocation policy, paired with MECH-147 (DG) + an MEC-analog indexing layer (SD-016). Distinct from 'no match retrieved' -- the system can decide to keep two traces apart even when they overlap. DEDUP 2026-06-16: MECH-147 (DG-equivalent pattern separation) build owned by hippocampal_planning_v4:HPL-3; MEM-2 consumes the separated encoder via cross-link rather than re-tracking the gate."
    - id: "memory_lifecycle_v4:MEM-3"
      title: "False-linking-risk / reality-coherence cost term (the single aspect with no REE home)"
      phase: 2
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [INV-079]
      depends_on: ["memory_lifecycle_v4:MEM-1"]
      cross_plan_link: []
      readiness_gate:
        - "MECH-094 (sim-vs-real confabulation gate) is the nearest reality-coherence machinery V3 has -- the cost term prices what MECH-094 currently only tag-gates"
        - "Lit verdict G2 caveat: the cost is so far ONE-SIDED (Sahay 2011 evidences only the under-separation pole); the V4 design MUST price BOTH over- and under-linking"
        - "Substrate to test it on does not yet exist -> register the new claim as substrate_conditional (no V3 substrate)"
      last_updated: 2026-06-10
      completion_note: "Verdict G2: mint ONE new candidate -- a false-linking-risk / reality-coherence cost at allocation time. Intake Section 3 marks this the ONLY proposal aspect with no existing REE home (nothing currently prices false linking). Generalisation and delusion are neighbours; the difference is whether the overlap is governed."
    - id: "memory_lifecycle_v4:MEM-4"
      title: "Raw-episode-preservation invariant (consolidation_output MUST NOT replace source_episode_evidence)"
      phase: 2
      status: done
      ethical_metadata:
        welfare_relevance: low
        applicable_ethics_gates: [SENT-13]
        requires_welfare_review: false
        note: "Raw-episode-preservation = memory-containment scaffold; consolidation must not overwrite the source harm-record (harm-occurred/repaired/unresolved distinction)."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-007, ARC-020, INV-080]
      depends_on: []
      cross_plan_link:
        - "sleep_substrate"
      readiness_gate:
        - "ARC-007 (hippocampal path store/replay residue field, architectural_commitment) IS the raw-episode-ish substrate that must not be overwritten by abstraction"
        - "ARC-020 (offline consolidation protected by typed authority/write boundaries, candidate) is the nearest existing isolation discipline; the anti-overwrite rule is an adjacent constraint within the offline locus"
        - "MECH-094 already carries a replay_origin audit flag; the new invariant generalises preservation from sim-vs-real to ALL consolidation transformations"
      last_updated: 2026-06-14
      completion_note: "Consolidation-faults intake (arXiv:2605.12978, VERIFIED): utility rises then degrades below the no-memory baseline; the regression traces to the consolidation STEP not the experience; agents preserving raw episodes double the accuracy of forced-consolidation. Standing rule: abstraction must never delete the evidence base. CLOSED 2026-06-14 (IGW plan reconcile, user-approved): the new-INV-vs-amend decision was already settled at registration -- INV-080 was minted 2026-06-10 as a NEW invariant stating this verbatim (depends_on ARC-007/ARC-020/MECH-094/INV-049/MECH-392), so registration IS the deliverable. This pass settled the open invariant_type question: RECLASSIFIED emergent -> universal. Rationale (invariant_types.md): the rule is a substrate-independent decision-theoretic law (grounding source arXiv:2605.12978 is substrate-agnostic; MEM-8 lit sharpened it to 'no SILENT/ungoverned overwrite'); the emergent test (retract the SD/ARC -> subject ill-defined) FAILS because consolidation_output/source_episode_evidence are well-formed wherever any consolidation op exists, not only under MECH-392; same family as the universal INV-049. emergent_from dropped, pending_substrate_reconfirmation cleared. epistemic_category stays substrate_conditional (no V3 substrate to test/build on). exp_conf 0 -- PROMOTES NOTHING; DO NOT build in V3."
    - id: "memory_lifecycle_v4:MEM-5"
      title: "Provenance + contradiction-flag + rollback layer on consolidated memory"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: low
        applicable_ethics_gates: [SENT-13]
        requires_welfare_review: false
        note: "Provenance + contradiction-flag + rollback = containment scaffold; lets memory mark harm repaired-vs-unresolved before autobiographical pain exists."
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-094, MECH-068, MECH-124, MECH-392]
      depends_on: ["memory_lifecycle_v4:MEM-4"]
      cross_plan_link:
        - "sleep_substrate"
        - "self_model_v4"
      blocking_on: "Requires a memory-lifecycle store with the 6-state model (retained/indexed/summarised/consolidated/contested/retired) that does not exist in V3; provenance fields have nowhere to live until MEM-4 raw-episode pointers exist."
      readiness_gate:
        - "MECH-068 (consolidation selectivity lives in the operator, candidate) is the on-point precedent: a bad operator degrades utility -> provenance must make the operator auditable"
        - "MECH-124 (maladaptive consolidation / PTSD-overbinding) is the existing pathological-consolidation precedent the rollback layer protects against"
        - "MECH-273 (sleep-half Bayesian self-model aggregation, candidate v3_pending) + MECH-272 (state-gated routing, candidate v3_pending) are the consolidation operators that would emit transformation_history + contradiction_flags"
        - "INV-039 (schema-primed assimilation rate gated by map stability, emergent invariant) is the schedule sensitivity the gated-write-authority half enforces -- aggressive consolidation onto an unstable map is the degradation regime"
      last_updated: 2026-06-10
      completion_note: "Intake Section 3 (c): every consolidated summary carries transformation_history + contradiction_flags; a summary that conflicts with its source is flagged, not silently authoritative; Schema retired -> source episodes remain (rollback). Generalises the MECH-094 replay_origin audit-flag family. Likely amends MECH-094/MECH-261 rather than a new MECH, plus possibly governs REE_assembly's own evidence base."
    - id: "memory_lifecycle_v4:MEM-6"
      title: "Retrieval-scope vs action-authority split (reflection-retrieval != action-authority-retrieval)"
      phase: 3
      status: done
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-257, ARC-035, MECH-393]
      depends_on: ["memory_lifecycle_v4:MEM-4"]
      cross_plan_link:
        - "inference_belief_state_v4"
      readiness_gate:
        - "MECH-257 (E2_x dual-function: retrospective comparator vs prospective rollout-scoring, candidate v3_pending) is the existing dual-mode-readout substrate the split refines"
        - "ARC-035 (stored != active; vmPFC converts stored -> active at eval time, candidate) is the existing stored-vs-active distinction the authority gate extends"
        - "MECH-150/151/152 (cue retrieval feeds bias, decoupled from integration) -- the retrieval path that must be tagged retrieval_scope vs action_authority"
      last_updated: 2026-07-14
      completion_note: "Consolidation-faults intake Section 2: retrieval_scope vs action_authority as distinct fields on a memory record is NOVEL (no current home). A consolidated abstraction lacking source-episode grounding may inform reflection but not unilaterally drive committed action. Distinct from MECH-257's read-mode arbitration: this gates AUTHORITY, not read-mode. CLOSED 2026-07-14 (IGW-20260714-119 plan reconcile): the new-claim-vs-amend decision was already settled at registration -- MECH-393 was minted 2026-06-10 as a distinct mechanism_hypothesis (subject memory.retrieval.scope_vs_authority, substrate_conditional/v4, depends_on MECH-257/ARC-035/MECH-150, distinct_from MECH-257 [gates READ-MODE] + ARC-035 [gates stored-vs-active]). Intake row 73 confirms retrieval_scope vs action_authority had NO existing home (verdict NEW), so registration IS the deliverable. Residual artifact added this pass: MECH-257 and ARC-035 now each carry a dated mem6_backref_2026_07_14 note acknowledging MECH-393 and making the previously one-directional MECH-393->anchor distinct_from links bidirectional (MECH-257: authority is orthogonal to comparator/evaluator read-mode; ARC-035: authority is a further axis beyond stored-vs-active). No new claim minted; no anchor amendment (both stay candidate). exp_conf 0 -- PROMOTES NOTHING; DO NOT build in V3."
    - id: "memory_lifecycle_v4:MEM-7"
      title: "Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)"
      phase: 2
      status: blocked
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-261, INV-039, INV-049, MECH-401]
      depends_on: ["memory_lifecycle_v4:MEM-4"]
      cross_plan_link:
        - "sleep_substrate"
      blocking_on: "Requires the SD-017 SWS/REM replay infra plus MECH-272/273 consolidation operators to be live enough to schedule against; over-frequent-rewrite is only testable once a real consolidation schedule exists."
      readiness_gate:
        - "INV-049 (offline-update necessity, universal invariant) is the complementary law: offline update is NECESSARY but the operator can corrupt -- this node prices the corruption side"
        - "INV-039 (schema-primed assimilation rate gated by map stability) supplies the schedule-sensitivity gate; consolidation is not automatic-after-every-interaction"
        - "SD-017 (SWS/REM replay infra) is the phase machinery the write-authority gates; MECH-261 offline_consolidation mode is the gate this amends"
      last_updated: 2026-06-10
      completion_note: "Consolidation-faults intake Section 5 (2): consolidation fires under explicit gating (state, map-stability per INV-039, schedule); over-frequent rewriting is a failure mode (utility-rises-then-degrades because each update rewrites prior updates). Likely amends MECH-261 / SD-017, not a new gate."
    - id: "memory_lifecycle_v4:MEM-8"
      title: "Biology + source grounding completion (allocation-policy lit DONE; consolidation-faults source verify)"
      phase: 2
      status: done
      lit_pull_status: done
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-391, INV-080]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Allocation-gate lit DONE 2026-06-06: VERDICT at evidence/literature/targeted_review_contextual_memory_allocation_gate/ (de Sousa 2026 + Cai 2016 + Bakker 2008 + Tse 2007 + Sahay 2011; all supports, mean ~0.73)"
        - "MULTI-STATE-LIFECYCLE + FALLIBLE-OPERATOR biology DONE 2026-06-13: VERDICT at evidence/literature/targeted_review_memory_lifecycle_store/ -- 7 entries. MECH-391 lit_conf 0->0.842 (Frankland&Bontempi 2005 systems-consolidation staging; Dudai&Eisenberg 2004 reconsolidation-as-lingering-consolidation = contested state; Nader&Hardt 2009 dynamic/reconstructive memory; Schlichting&Preston 2015 integration = allocation 'integrate' pole). INV-080 lit_conf 0->0.767 (Sekeres/Winocur/Moscovitch 2018 trace-transformation precision-loss = the THREAT; Richards&Frankland 2017 transience-is-adaptive = grounds 'retired' state + SHARPENS INV-080 to 'no SILENT/ungoverned deletion' not 'never forget'; Xiong 2025 arXiv:2505.16067 LLM-agent corroboration). exp_conf stays 0 -- PROMOTES NOTHING."
        - "Consolidation-faults primary source VERIFIED 2026-06-09 (arXiv:2605.12978, UIUC + Tsinghua); secondary arXiv:2505.16067 RE-VERIFIED 2026-06-13 (Xiong et al., 'How Memory Management Impacts LLM Agents'; advocates preserving quality-labelled episodic records over lossy consolidation; error-propagation from inaccurate experiences) -- folded as the INV-080 computational-corroboration entry."
        - "Adjacent corroboration to fold if a NEW consolidation claim registers (none registered this pass): SSGM arXiv:2603.11768 (drift taxonomy) + survey arXiv:2603.07670 / arXiv:2605.06716"
      last_updated: 2026-06-13
      completion_note: "CLOSED 2026-06-13. Per feedback_biology_before_formal_definitions: both halves now grounded. Allocation-gate half was already lit-closed (2026-06-06) but those entries were tagged to a placeholder CANDIDATE id, NOT to MECH-391 (registered 2026-06-10), so MECH-391's literature_confidence read None; the new targeted_review_memory_lifecycle_store entries tag the real claim IDs and lift MECH-391 to 0.842 / INV-080 to 0.767. The biology of memory as a multi-state lifecycle with FALLIBLE operators is grounded (systems-consolidation staging; reconsolidation = contested/labile state; trace-transformation = lossy summarised/consolidated states; transience = adaptive governed retirement). KEY honesty note recorded in entries: INV-080 is biology-INFORMED-but-not-biology-MANDATED -- the biological default is detail LOSS (Sekeres 2018) and adaptive forgetting (Richards & Frankland 2017), so the invariant must read 'no SILENT/ungoverned overwrite of the evidence base', not 'never delete'. No completion-set partner claim registered (proposal-first; nothing surfaced that is not already covered by MECH-392/INV-079/INV-080). exp_conf 0 on both -- promotes nothing; substrate-BUILD gate unchanged (DO NOT build in V3)."
---
# Memory Lifecycle -- V4 Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the three memory-lifecycle gaps both 2026-06 intakes
surface -- (1) the contextual memory-ALLOCATION gate POLICY (when/how to
integrate vs separate traces), (2) the consolidation ANTI-OVERWRITE +
raw-episode-preservation discipline, (3) the PROVENANCE / contradiction-flag /
rollback + retrieval-scope-vs-action-authority layer -- so V4 substrate work
slots in against the gates REE already owns instead of building a parallel
memory store or, worse, an automatic-rewriting consolidator that degrades
utility over time.

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant against them.
The value here is the **readiness gates** -- for each step, exactly which
V3-era prerequisites (claims/tracks) must land before the V4 substrate step is
honest to build.

---

## One-line framing

> Memory in REE is already plural -- residue field (ARC-007), hippocampal store,
> viability map, schema buckets, ghost-goal banks -- and already gated
> (MECH-094, MECH-261, ARC-035, SD-016) and already consolidated offline
> (INV-039, INV-049, SD-017, MECH-272/273). What REE does NOT own is (a) the
> POLICY that decides integrate-vs-separate at allocation time, and (b) a
> discipline that stops consolidation from silently overwriting the evidence it
> abstracts. Both intakes converge: do not add a memory store; add a
> governance LAYER over the stores that exist.

---

## The three gaps (and the eight nodes that sequence them)

| Gap | Node(s) | Anchor claims | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| 1 -- allocation POLICY | MEM-1, MEM-2, MEM-3 | MECH-261, ARC-035, MECH-147, MECH-094 | V4 (gates are V3-live) | amend MECH-261 with a decision stage; MECH-147 DG must land for active separation; price false-linking |
| 2 -- anti-overwrite | MEM-4, MEM-7 | ARC-007, ARC-020, INV-039, INV-049, SD-017 | V4 (infra is V3-live) | raw-episode-preservation invariant; gated write-authority on the SD-017/MECH-272/273 schedule |
| 3 -- provenance / authority | MEM-5, MEM-6 | MECH-094, MECH-068, MECH-124, MECH-257, ARC-035 | V4 | provenance+rollback needs the 6-state store; retrieval-scope vs action-authority split |
| grounding | MEM-8 | (lit anchors) | cross-cutting | allocation lit DONE 2026-06-06; consolidation-faults source verified 2026-06-09 |

---

## What this plan deliberately does NOT pull into V3

- **No biological memory-allocation gate in V3.** Per the allocation-gate
  intake (Section 7) the gate is V3-relevant ONLY if current V3 failures
  resolve toward *memory contamination / false cross-run reuse /
  overgeneralisation* (open-question Q2). The active V3 threads (cue-authority
  638b/640a, goal-pipeline GAP-7) point at action pressure / goal-stream lift,
  NOT memory contamination -- so this stays V4/V5.
- **No discriminative experiments before the substrate exists.** Both intakes
  flag the vacuous-probe risk: a memory-lifecycle store (raw-episode pointers,
  6-state model, allocation policy) must exist before any probe is meaningful.
  Nodes carry `owner_exq: null` by design.
- **No new INV minted for the allocation policy.** Verdict G1: the policy is an
  AMENDMENT to MECH-261 (subsumed by MECH-094/261 + INV-039), not a fresh
  invariant. Only one genuinely new claim is warranted (the false-linking-risk
  cost, MEM-3) plus the consolidation-discipline candidates (MEM-4/5/6/7).
- **No claim promotions, no substrate code.** Registering this roadmap changes
  no V3 behaviour.

---

## Source artefacts

| Artefact | Role |
|---|---|
| evidence/planning/thought_intake_2026-06-06_contextual_memory_allocation_gate.md | allocation-gate POLICY intake (Stage-2); REE owns gates not policy; verdict G1-G3 |
| evidence/planning/thought_intake_2026-06-06_agent_memory_consolidation_faults.md | consolidation-as-fallible-operator intake (Stage-2); anti-overwrite + provenance + retrieval-scope-vs-authority |
| evidence/literature/targeted_review_contextual_memory_allocation_gate/VERDICT.md | allocation-gate lit-pull (de Sousa 2026 + 4; mean ~0.73; DONE 2026-06-06) |
| claims.yaml MECH-261 / MECH-094 / ARC-035 / MECH-272 / MECH-273 | the gates + consolidation operators the policy/discipline steers |
| claims.yaml INV-039 / INV-049 / SD-017 / ARC-007 / ARC-020 | the offline-consolidation infra the anti-overwrite rule constrains |
| claims.yaml MECH-068 / MECH-124 / MECH-147 / MECH-257 | operator-selectivity, maladaptive-consolidation, DG-separation, dual-mode-readout precedents |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap in the
  generation-segmented closure-map pipeline. Eight nodes seeded from the two
  2026-06-06 memory intakes and grounded in 14 existing claims. Readiness gates
  pinned per node. Four prose-only NEWCLAIM stubs proposed (allocation-gate
  policy, false-linking-risk cost, raw-episode-preservation, provenance-required,
  retrieval-scope-vs-action-authority); the gated-write-authority candidate is
  folded into MEM-7 as an MECH-261/SD-017 amendment rather than a separate stub.
  `generation: v4` set so the V3 closure % is unaffected. No claims.yaml edits.
- **2026-07-14** -- MEM-6 CLOSED (IGW-20260714-119 plan reconcile). Retrieval-scope
  vs action-authority split. Registration deliverable already landed: MECH-393 was
  minted 2026-06-10 as a distinct `mechanism_hypothesis` (subject
  `memory.retrieval.scope_vs_authority`, substrate_conditional/v4), `distinct_from`
  MECH-257 (gates read-mode) + ARC-035 (gates stored-vs-active). Intake row 73
  confirms the field pair had no existing REE home (verdict NEW), so no
  amendment was warranted. Residual artifact this pass: added dated
  `mem6_backref_2026_07_14` notes to MECH-257 and ARC-035 making the previously
  one-directional MECH-393->anchor links bidirectional. No new claim minted, no
  anchor amendment; exp_conf 0 -- promotes nothing; DO NOT build in V3. With MEM-6
  done, phase-3 provenance/authority now has MEM-5 (blocked on the 6-state store)
  as its sole remaining open node.
- **Noted for the orchestrator:** the consolidation-faults intake references
  "SD-024 (sleep.protected_offline_consolidation_boundary)" but the actual
  SD-024 in claims.yaml is "DA-modulated RBF center density." The nearest real
  offline-write-boundary claim is ARC-020 (used here instead). Flagging so the
  intake's SD-024 reference is not silently propagated as a claim anchor.
