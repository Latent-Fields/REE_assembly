# V4 Assembly Map -- cross-plan blocker taxonomy + lit-pull sweep

Generated: 2026-06-13T18:47:52Z by `scripts/generate_v4_assembly_map.py`

Roll-up over the V4/V5 forward roadmaps. Reads each node's `blocker_class` (v3_gate | v3_substrate | sibling_node | lit_gap | deferred) and grounding `lit_pull_status` (none | active | partial | done). **Generation v4/v5 only -- the V3 closure % is untouched.** Warn-only planning aid; regenerate after editing any `*_v4_plan.md`.

**Blocker classes**

| class | meaning | how it clears |
|---|---|---|
| `v3_gate` | a V3-phase claim/experiment must close | run/close the V3 experiment |
| `v3_substrate` | a V3 substrate is inert/coarse/missing | V3 substrate repair or enrichment |
| `sibling_node` | waiting on another roadmap node | build the upstream node first |
| `lit_gap` | biology grounding owed before build | run the /lit-pull (see sweep) |
| `deferred` | explicitly off the critical path | nothing now; revisit on trigger |

**Totals:** 99 nodes across 13 plans -- v3_gate=3, v3_substrate=12, sibling_node=36, lit_gap=2, deferred=8. Only 15 of the blocked nodes are gated on the V3 side; the rest are intra-V4 sequencing.

## Per-plan blocker taxonomy

| plan | nodes | v3_gate | v3_sub | sibling | lit_gap | defer | grounding |
|------|------:|-------:|------:|-------:|-------:|-----:|-----------|
| affect_expression_v4 | 9 | 0 | 2 | 4 | 0 | 1 | done |
| autobiographical_memory_v4 | 9 | 0 | 1 | 4 | 0 | 1 | partial |
| developmental_dmn_v4 | 8 | 0 | 1 | 4 | 1 | 0 | none |
| drives_motivation_v4 | 5 | 1 | 0 | 1 | 0 | 1 | done |
| goal_deliberation_v4 | 8 | 1 | 2 | 2 | 0 | 1 | done |
| hippocampal_planning_v4 | 9 | 1 | 0 | 6 | 0 | 1 | partial |
| inference_belief_state_v4 | 7 | 0 | 3 | 0 | 1 | 0 | done |
| memory_lifecycle_v4 | 8 | 0 | 0 | 3 | 0 | 0 | partial |
| object_reasoning_abstraction_v4 | 8 | 0 | 0 | 5 | 0 | 1 | partial |
| object_representation_v4 | 6 | 0 | 1 | 1 | 0 | 0 | partial |
| perceptual_adaptors_v4 | 7 | 0 | 0 | 2 | 0 | 0 | done |
| plasticity_neuromodulation_v4 | 7 | 0 | 1 | 1 | 0 | 2 | none |
| self_model_v4 | 8 | 0 | 1 | 3 | 0 | 0 | done |

## V3-side bottleneck register (15)

The nodes that gate V4 from the V3 side -- closing these is what actually moves the roadmap. Everything classed `sibling_node` ultimately waits behind one of these (or behind a lit-pull).

| plan | node | class | sev | unblocks | blocker |
|------|------|-------|-----|----------|---------|
| drives_motivation_v4 | `drives_motivation_v4:DRV-4` | v3_gate | high | MECH-395 | Gated on the live cue-recall diagnostic thread: register the orienting MECH only if V3-EXQ-640+ shows the discriminating pattern (cue fires, no contact, AND no orienti... |
| goal_deliberation_v4 | `goal_deliberation_v4:GDL-5` | v3_gate | high | MECH-389 | Gated on a V3 demonstration that the interrupt->resume span is the actual failure mode: register the resumption mechanism as a candidate MECH only when a V3 autopsy (6... |
| hippocampal_planning_v4 | `hippocampal_planning_v4:HPL-1` | v3_gate | load-bearing | MECH-163 | MECH-163 is implementation_phase: v3 and held under hold_pending_v3_substrate (9 lit supports, 0 genuine exp entries). The VTA/hippocampal model-based system (goal-see... |
| affect_expression_v4 | `affect_expression_v4:AE-1` | v3_substrate | load-bearing | MECH-359 | behavioral_diversity_isolation:GAP-A (cand_world_pairwise_dist=0.0 -- candidate trajectories collapse to a single regime, so there is no cross-candidate basis to attac... |
| affect_expression_v4 | `affect_expression_v4:AE-6` | v3_substrate | medium | MECH-364,Q-059 | MECH-364 needs an E3 conflict/constraint-LOAD readout (regime-level, not the per-tick MECH-110 tag-clear); Q-059 (crying analogue + laughter repair-vs-damage adjudicat... |
| autobiographical_memory_v4 | `autobiographical_memory_v4:ABM-5` | v3_substrate | high | MECH-368,Q-062 | Requires an online world-model/policy WRITE channel to gate; the goal_relevance input depends on a competitive z_goal (goal_pipeline GAP-4), which is the main reason M... |
| developmental_dmn_v4 | `developmental_dmn_v4:DMN-3` | v3_substrate | load-bearing | ARC-090 | The V3 play cluster (ARC-049/050, MECH-194-199, INV-058/060) is substrate_blocked: no play_frame_tag, no synthetic-signal seeding, no bilateral frame in ree-v3 code. A... |
| goal_deliberation_v4 | `goal_deliberation_v4:GDL-2` | v3_substrate | load-bearing | SD-033e | Gated on the V3 operating_mode primitive being behaviourally exercisable: SD-032a discrete operating_mode + MECH-259 switch threshold landed (V3-EXQ-446/455 PASS), but... |
| goal_deliberation_v4 | `goal_deliberation_v4:GDL-6` | v3_substrate | medium | SD-027,SD-028,MECH-254,MECH-255 | Gated on the V3 attention substrate being more than the MECH-089 packaging op: SD-027 asserts a SELECTION gate UPSTREAM of packaging, and there is no boundary-gate pri... |
| inference_belief_state_v4 | `inference_belief_state_v4:INF-3` | v3_substrate | load-bearing | MECH-385 | MECH-022 hypothesis injection is the V3 generator (control-plane gated). The belief-SET (multiple competing hypotheses each with confidence + predicted transitions, sc... |
| inference_belief_state_v4 | `inference_belief_state_v4:INF-4` | v3_substrate | high | MECH-386 | Affordances must be grounded in object->action binding (cross-plan OBJ-4 / ARC-082), whose V3 path SD-016 cue_action_proj is inert (V3-EXQ-449 found 0.0 gradient; SD-0... |
| inference_belief_state_v4 | `inference_belief_state_v4:INF-5` | v3_substrate | load-bearing | MECH-387 | SD-059/MECH-358 escape-affordance bridge is candidate + pending_retest_after_substrate (2026-06-09 autopsy: retest gated on a Stage-H nav/survival-competence leg + MEC... |
| object_representation_v4 | `object_representation_v4:OBJ-4` | v3_substrate | high | ARC-082 | SD-016 cue_action_proj is inert in V3 (V3-EXQ-449 found 0.0 gradient; non-differentiable CEM severs the path before E3.select). Grounding must land before object->acti... |
| plasticity_neuromodulation_v4 | `plasticity_neuromodulation_v4:PLW-3` | v3_substrate | load-bearing | MECH-398 | MECH-333 open-phase mechanism is planned-but-unbuilt (epistemic_category substrate_conditional 2026-06-10; only the plastic-channel-injection option landed, the F-grad... |
| self_model_v4 | `self_model_v4:SELF-6` | v3_substrate | high | MECH-214 | CausalGridWorldV2 conflates location with reward, so the MECH-214 addiction failure mode (wanting fires on an E1-unrepresented satisfaction state) is structurally invi... |

## Literature-pull sweep order (7 pulls owed)

The first pass of assembly work. Each grounding node's /lit-pull must (a) ground its registered claims AND (b) harvest the co-constitutive circuit partners the mechanism presupposes -- so building the substrate does not omit jointly-necessary components. In-progress pulls are listed first (finish them); the rest are ordered by how much load-bearing blocked work the plan's grounding unblocks.

### 1. hippocampal_planning_v4 -- `hippocampal_planning_v4:HPL-9` [partial; gates 5 load-bearing/high blocked nodes]

- **Ground:** MECH-147, MECH-148, MECH-149, MECH-207, ARC-040
- **Pull + completion-set harvest:**
  - L1 DG pattern separation (Sakon & Suzuki 2019; Leutgeb 2007) -- AND harvest the completion-set: hilar mossy-cell feedback inhibition + CA3 recurrent-collateral pattern COMPLETION are co-constitutive of the separation property; building a DG expansion layer without the inhibitory/completion partners will not yield the claimed property
  - L2 pure time cells (Omer/Las/Ulanovsky 2022; Eichenbaum 2014) + theta-gamma phase-coding partner; L3 CA1 match-mismatch novelty (Lisman & Grace 2005) + VTA dopaminergic loop partner (MECH-075)
  - L4 ACh permissive write-gate (Sinclair 2021; Hasselmo 2006) + septohippocampal cholinergic projection source; L5 dorsal/ventral segregation (Fanselow & Dong 2010; Strange 2014)

### 2. object_reasoning_abstraction_v4 -- `object_reasoning_abstraction_v4:OBJ-ABS-8` [partial; gates 5 load-bearing/high blocked nodes]

- **Ground:** SD-040, SD-045, SD-042
- **Pull + completion-set harvest:**
  - L-type type-prototype substrate (Quiroga 2005, Schapiro 2016/2017, Constantinescu 2016, Hennies 2017) -- DONE: targeted_review_hpc_type_prototype_substrate (grounds SD-040 / MECH-296 / MECH-297)
  - L-action action-policy decomposition (Graybiel 2008, Daw 2005, Dolan & Dayan 2013, Botvinick 2009) -- DONE: targeted_review_action_policy_decomposition (grounds SD-045 / SD-042)
  - L-theta theta-abstraction-scaling (Gupta 2012, Bellmund 2018, Constantinescu 2016) -- DONE: targeted_review_theta_abstraction_scaling (grounds MECH-299 / MECH-300)
  - REMAINING DEBT: biology-before-formal-definitions check on any V4 SD/MECH that operationalises options as a formal Sutton-Precup-Singh construct before its substrate is built (per project rule feedback_biology_before_formal_definitions)

### 3. autobiographical_memory_v4 -- `autobiographical_memory_v4:ABM-9` [partial; gates 3 load-bearing/high blocked nodes]

- **Ground:** ARC-085, MECH-365, MECH-366, MECH-368, MECH-361
- **Pull + completion-set harvest:**
  - L1 emotional modulation of consolidation as the write-weight (McGaugh 2004; Cahill & McGaugh 1998; Ballarini 2009 behavioural tagging) -- the anchor for MECH-368/MECH-361 affect-weighted write authority
  - L2 source/provenance monitoring (Johnson, Hashtroudi & Lindsay 1993 source-monitoring framework; reality-monitoring) for the ARC-085 provenance fields + the imagined-vs-experienced viewpoint label (MECH-366)
  - L3 imagination-learning constraints (Stickgold 2013; Schapiro 2017 CLS; confabulation literature) -- already anchored for ABM-4; harvest the hippocampal-vmPFC schema partner + the SWS/REM content-vs-weights split (MECH-252/253) co-constitutive of honest replay-based learning

### 4. memory_lifecycle_v4 -- `memory_lifecycle_v4:MEM-8` [partial; gates 2 load-bearing/high blocked nodes]

- **Ground:** MECH-391, INV-080
- **Pull + completion-set harvest:**
  - Allocation-gate lit DONE 2026-06-06: VERDICT at evidence/literature/targeted_review_contextual_memory_allocation_gate/ (de Sousa 2026 + Cai 2016 + Bakker 2008 + Tse 2007 + Sahay 2011; all supports, mean ~0.73)
  - Consolidation-faults primary source VERIFIED 2026-06-09 (arXiv:2605.12978, UIUC + Tsinghua); secondary arXiv:2505.16067 NOT yet re-verified -- pull via /lit-pull if it becomes load-bearing for a registered claim
  - Adjacent corroboration to fold if a consolidation claim registers: SSGM arXiv:2603.11768 (drift taxonomy) + survey arXiv:2603.07670 / arXiv:2605.06716

### 5. object_representation_v4 -- `object_representation_v4:OBJ-6` [partial; gates 2 load-bearing/high blocked nodes]

- **Ground:** ARC-080, ARC-006
- **Pull + completion-set harvest:**
  - L1 object-files & feature-binding (Kahneman/Treisman/Gibbs 1992; Treisman & Gelade 1980 FIT) -- ACTIVE 2026-06-04
  - L2 object permanence (Piaget; Baillargeon; Spelke core-knowledge; Kellman & Spelke 1983) -- ACTIVE 2026-06-04
  - L3 affordances (Gibson); L4 self-as-object (Gallagher/Botvinick); L5 ToM (Woodward/Csibra) -- follow when their pillars are scheduled

### 6. developmental_dmn_v4 -- `developmental_dmn_v4:DMN-8` [none; gates 3 load-bearing/high blocked nodes]

- **Ground:** ARC-090, MECH-380, MECH-383
- **Pull + completion-set harvest:**
  - Current state: architectural-analogy anchors only (Vygotsky private speech; Lupyan/Swingley labels-alter-search; Kross/Moser third-person self-talk; DMN self-reflection/simulation literature) -- recorded as anchors, NOT a citable out-of-domain dataset (no research_anchor claim)
  - Per project rule feedback_biology_before_formal_definitions: each pillar that instantiates a formal developmental concept needs a biology lit-pull BEFORE its substrate is built
  - Schedule per-pillar: private-speech/inner-speech (MECH-380/381), label-as-perceptual-control (MECH-383), self-distancing (MECH-382) -- follow when their pillars are scheduled

### 7. plasticity_neuromodulation_v4 -- `plasticity_neuromodulation_v4:PLW-2` [none; gates 2 load-bearing/high blocked nodes]

- **Ground:** MECH-398, ARC-093
- **Pull + completion-set harvest:**
  - Project rule feedback_biology_before_formal_definitions: commission this /lit-pull BEFORE registering any ACh/PV/BDNF substrate claim; the opening-side claims have NO biology lit-pull today
  - Anchors named in the framing note: Hensch 2005 (PV/GABA critical-period closure), Bear & Singer 1986 (ACh+NE pairing abolishes plasticity), Froemke 2015 + Kilgard & Merzenich 1998 (nucleus basalis -> cortical remapping), Sale 2007 (GABA reduction reopens CP), Lehmann & Lowel 2008 + Trachtenberg 2015 (windows shift in gain, not binary)
  - Do NOT pull pre-emptively: gate the pull on PLW-1's decision-to-build passing first

## Cross-cutting planning gaps

**Environment-substrate gated (3)** -- blockers needing a richer V4 environment than gridworld. A shared prerequisite: build the env once, unblock all of these.

- `object_reasoning_abstraction_v4:OBJ-ABS-5` (object_reasoning_abstraction_v4): Gated on ARC-021 three-loop framework (where option arbitration sits) + SD-004 continuous action substrate (which options refine into an indexable library) + a V4 environment with tool use / social co
- `perceptual_adaptors_v4:PA-3` (perceptual_adaptors_v4): MECH-103 is untestable in V3 (EXQ-128 / EXQ-134 FAIL, both superseded: no genuine multimodal input). A real multimodal V4 input substrate must exist before a deep visual adaptor is meaningful.
- `self_model_v4:SELF-6` (self_model_v4): CausalGridWorldV2 conflates location with reward, so the MECH-214 addiction failure mode (wanting fires on an E1-unrepresented satisfaction state) is structurally invisible. Requires a new env where p

**Author-flagged no-owning-node gaps (1)** -- a blocker names a substrate/module that has no roadmap node yet.

- `affect_expression_v4:AE-9` (affect_expression_v4): no owning substrate node exists yet

