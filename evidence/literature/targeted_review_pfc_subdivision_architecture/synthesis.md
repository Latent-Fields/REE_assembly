# PFC Subdivision Architecture — Three-Prong Synthesis

Literature pull scoping the PFC subdivision substrate that REE's claim graph currently references but does not properly register. Runs over three prongs: (A) lateral-PFC rule representation — load-bearing for MECH-261; (B) OFC vs vmPFC dissociation — resolving existing lumping in ARC-035 and MECH-151/152; (C) premotor/SMA sequence control and frontopolar branching — V3/V4 scoping.

## Audit context

Before the pull, I audited REE's claim graph for how PFC function is currently represented:

- **vmPFC:** well-covered (ARC-035 as value-regulation hub, MECH-151/152/209/211/212/213/235, ARC-041).
- **dlPFC:** covered only for working-memory function (MECH-116 LSTM, MECH-133 5-HT persistence).
- **OFC:** under-registered. Existing value-related claims lump OFC under vmPFC.
- **dACC:** SD-032b exists (registered but unimplemented).
- **Gaps:** lateral-PFC rule representation (nothing beyond generic working memory), premotor/SMA-analogue (functions embedded in E3 but not explicitly substrate-tied), frontopolar / branching (absent entirely).

MECH-261 was committing to write into a "PFC-analog policy/rule-level substrate" that had no corresponding claim. This pull grounds that substrate.

## Prong A — Lateral-PFC rule representation (load-bearing for MECH-261)

- **Miller & Cohen 2001** (Annu Rev Neurosci, conf 0.82): PFC as active maintenance of task-relevant rules, biasing posterior processing. Foundational but pre-subdivision.
- **Badre & Nee 2018** (TiCS, conf 0.80): caudal-rostral abstraction gradient within lateral PFC; multiple separable levels, not one flat substrate.
- **Mansouri, Freedman & Buckley 2020** (NRN, conf 0.85): stimulus-abstracted rule-selective neurons in primate lateral PFC; persistence across delays; training-dependent emergence.

**Synthesis:** there is a biologically well-supported lateral-PFC substrate that holds stimulus-abstracted rule/policy representations and persists them across delays. This is exactly what MECH-261 writes into during external_task and internal_planning modes. The substrate is gradient-organised (Badre & Nee), so REE should recognise at least two levels — mid-lateral (rule-holding, V3 scope) and frontopolar (branching, V4 scope, see Prong C).

## Prong B — OFC vs vmPFC dissociation

- **Rudebeck & Murray 2014** (Neuron, conf 0.83): selective fiber-sparing lesion evidence dissociates OFC (specific-outcome prediction / credit assignment) from vmPFC (subjective value integration).
- **Stalnaker, Cooch & Schoenbaum 2015** (Nat Neurosci, conf 0.80): OFC represents cognitive maps of task structure, not scalar value. Value rides on top.

**Synthesis:** REE has been lumping OFC under vmPFC. This is the same class of premature lumping that produced SD-003 before the SD-010/011 split and SD-010 before the SD-011 split. The fix is to register an OFC-analog substrate distinct from vmPFC-analog. Functionally the OFC-analog is the natural home for E2 harm predictions (specific-outcome prediction) and for the learned task-structure representation that E2/E3 query during model-based rollout. The vmPFC-analog remains the scalar value integrator (already well-covered in existing claims). MECH-261 gating rules for OFC-analog: writes during internal_planning (speculative outcome predictions), suppression during internal_replay, consolidative writes during offline_consolidation.

## Prong C — Premotor/SMA sequence control + frontopolar branching (V3/V4 scoping)

- **Tanji & Hoshi 2008** (Physiol Rev, conf 0.78): graded executive control across lateral PFC → pre-SMA → SMA → dorsal premotor. Rule/goal upstream; sequence planning middle; sequence execution downstream.
- **Koechlin & Summerfield 2007** (TiCS, conf 0.72): frontopolar cortex as substrate for branching and nested control — holding pending operations while executing current ones.

**Synthesis:** REE's existing E3 sequence-selection machinery already implements most of the premotor/SMA-analogue function (proposing and selecting sequences, binding actions to states). What is missing is the upstream rule-holding substrate (covered by Prong A) and the downstream branching substrate (frontopolar, V4 scope). The V3/V4 boundary recommendation is: V3 stops at mid-lateral rule-holding; V4 adds frontopolar branching. The operating_mode_vector in MECH-261 should already accommodate a future "deliberative_branching" mode even if V3 doesn't implement it — schema forward-compatibility saves disruptive changes later.

## Cross-cutting implications for REE

**1. Register an SD cluster for PFC subdivision architecture.** Template follows SD-032 (cingulate cluster): parent SD with subdivisions. Proposed structure:

- **SD-033 — PFC subdivision architecture** (parent, meta-cluster)
- **SD-033a — lateral-PFC-analogue rule/goal substrate** (mid-lateral, rule-holding; V3 scope; primary MECH-261 write target)
- **SD-033b — OFC-analogue outcome-prediction substrate** (specific-outcome prediction, task-structure representation; V3 scope; E2's natural substrate address)
- **SD-033c — vmPFC-analogue value-integration substrate** (existing ARC-035 / MECH-151 functions, consolidated under SD-033 for coherence)
- **SD-033d — premotor/SMA-analogue sequence-execution substrate** (already implemented inside E3; register for completeness of claim graph)
- **SD-033e — frontopolar-analogue branching substrate** (V4 scope; hooks only in V3)

This matches the SD-032 pattern — parent cluster, subdivisions, each with its own mechanism claims.

**2. Update MECH-261 depends_on.** Currently cites ARC-038/039 (from the 2026-04-18 absorb edit). Add SD-033a specifically as the primary write target. Add SD-033b as a secondary write target. Add ARC-035 / SD-033c to the set of gated substrates.

**3. Audit pass on cross-references.** MECH-116 (dlPFC LSTM working memory), MECH-235 (vmPFC), MECH-251 (whatever it is, per the audit), and ARC-035 may benefit from cross-references pointing to the new SD-033 cluster. This is a low-priority follow-up — not blocking for V3 implementation.

**4. EXP-0148 revision.** The three-arm SD-032a-ablation experiment previously queued to test MECH-261's falsification signature should be extended (or a sibling EXP queued) to include an analogous test of the SD-033a / lateral-PFC-analogue substrate once implemented. The current EXP-0148 tests MECH-261's coordinator claim; a sibling EXP would test that MECH-261 writes actually land in the correct subdivision under each mode.

## Priorities for immediate integration

1. Register SD-033 cluster (parent + five subdivisions) in claims.yaml — mirrors SD-032 template.
2. Update MECH-261 depends_on to include SD-033a/b/c.
3. Update existing ARC-035 / MECH-151/152 to cross-reference SD-033c (vmPFC subdivision) as their substrate address.
4. Defer V3 implementation work on SD-033a until governance reviews the registration.
5. Defer frontopolar-analogue (SD-033e) to V4.
6. Schedule follow-up lit-pull on frontopolar function (Burgess, Mansouri, Boorman, Christoff) when V4 design work begins — the current entry (Koechlin 2007) is the entry point, not the complete survey.

## Net aggregate (A + B + C)

Literature support across the original three prongs is strong. Mean confidence 0.80 across seven entries (range 0.72–0.85). All seven entries point in the same direction: the "PFC analogue" that REE currently treats as a monolith is biologically a graded, multi-subdivision system, and registering it properly as an SD cluster (rather than as a single substrate) will prevent the same kind of late re-split that SD-003 and SD-010 required.

---

# Prong D — frontopolar function (V4 follow-up pull, 2026-04-19T11:47:33Z)

SD-033e was registered 2026-04-19 as V4-scope with intentionally thin evidence — only the Koechlin & Summerfield 2007 entry from Prong C. The SD-033e evidence_quality_note committed to a detailed follow-up lit-pull before V4 implementation begins. This prong is that follow-up pull. Six new entries are added, focused on the substrate-specific literature for frontopolar cortex (BA 10). They are:

- **Burgess, Veitch, de Lacy Costello & Shallice 2000** (Neuropsychologia, conf 0.78): large-N human focal-lesion study; rule-breaking and task-switching failures concentrate in medial polar BA 8/9/10; first clean lesion-based evidence for a BA 10 substrate distinct from lateral-PFC rule-holding.
- **Burgess, Dumontheil & Gilbert 2007** (Trends Cogn Sci, conf 0.82): gateway hypothesis — BA 10 mediates the switch between stimulus-oriented (external) and stimulus-independent (internal) attending, with medial vs lateral BA 10 carrying opposite sides of the gateway. Directly biologically grounds MECH-261's operating_mode vector.
- **Boorman, Behrens, Woolrich & Rushworth 2009** (Neuron, conf 0.85): model-based fMRI; lateral frontopolar cortex tracks the value of counterfactual (unchosen) alternatives, dissociating from vmPFC which tracks chosen-option value. Individual variation predicts propensity to switch.
- **Christoff, Gordon, Smallwood, Smith & Schooler 2009** (PNAS, conf 0.72): mind-wandering engages both default network and executive substrates including rostral PFC. Meta-awareness modulates the signal. Useful corroboration that internal cognitive modes are computationally active, not idle.
- **Mansouri, Buckley, Mahboubi & Tanaka 2015** (PNAS, conf 0.82): selective bilateral FPC lesions in macaques; FPC-lesioned animals are MORE focused under distraction but IMPAIRED at rapid learning of novel alternative rules. FPC function = disengagement-for-exploration.
- **Mansouri, Koechlin, Rosa & Buckley 2017** (Nature Reviews Neuroscience, conf 0.86): multi-lab integrative synthesis; FPC monitors relative importance of current vs alternative goals; parallel-goal monitoring is the distinctively human capacity. Subsumes the Koechlin 2007 branching framing.

## What the literature converges on

Four methodologically distinct lines of evidence — human lesion (Burgess 2000), human fMRI (Boorman 2009, Christoff 2009), primate selective lesion (Mansouri 2015), and theoretical synthesis (Burgess 2007, Mansouri 2017) — converge on a single functional specification for frontopolar cortex that is richer than any single entry's framing:

1. **Counterfactual value tracking** (Boorman 2009): lateral FPC maintains a running estimate of the value of alternatives that were not chosen, in parallel with vmPFC's chosen-option value signal.
2. **External/internal attentional gateway** (Burgess 2007): BA 10 mediates the switch between engagement with the current external world (medial BA 10) and internally-generated cognition about alternatives (lateral BA 10).
3. **Disengagement-for-exploration** (Mansouri 2015): FPC enables releasing executive control from the current task and redistributing it to novel options. Without FPC, the animal over-focuses and cannot learn novel alternative rules.
4. **Relative-importance monitoring over competing goals** (Mansouri 2017 synthesis): FPC monitors the relative importance of current vs alternative goals and, in humans specifically, supports parallel monitoring of multiple goals with flexible switching.

These are not four separate functions — they are four different methodological views of what is plausibly one underlying computation: **maintenance of a parallel, competing-goal representation with relative-value-weighted switching logic**. The Koechlin & Summerfield 2007 "branching" framing (Prong C) is one special case of this, specifically the case where switching involves holding a pending task through execution of another.

## Implications for SD-033e scope

The SD-033e specification as currently written — "branching / nested control substrate" — is too narrow. It captures Koechlin's framing but misses three of the four converging functions. A broader specification that honours the literature is:

> SD-033e — Frontopolar-analog (parallel-goal deliberation substrate): V4-scope module maintaining counterfactual-value estimates for alternatives to the current course of action, mediating transitions between external engagement and internally-generated deliberation, enabling disengagement from the current task to explore novel alternatives, and monitoring relative importance across multiple active goals. Hooks reserved in V3 via the operating_mode vocabulary; substrate deferred to V4.

This is substantively what SD-033e should ultimately cover in V4. V3 scope does not change — no implementation work happens until V4 — but the functional framing in the claim should be tightened before V4 design begins.

## Implications for MECH-261 reserved mode name

SD-033e currently reserves a V4 mode name via MECH-261's operating_mode_vector. The committed name is **"deliberative_branching"**. This is the Koechlin framing, and the literature above argues it is the wrong name. Three candidate replacements:

| Candidate | Captures | Loses | Assessment |
|---|---|---|---|
| `deliberative_branching` | Koechlin tree-search framing | Boorman counterfactual, Mansouri relative-importance, Burgess gateway | Narrow — recommended against |
| `counterfactual_deliberation` | Boorman counterfactual-value computation | Mansouri parallel-monitoring across >2 alternatives | Acceptable; pairs well with Boorman grounding |
| `parallel_goal_deliberation` | Mansouri 2017 parallel-monitoring framing + Burgess gateway | Specific reference to counterfactual value | **Preferred** — captures the integrative Mansouri 2017 synthesis |

Recommendation: **rename the reserved V4 mode from `deliberative_branching` to `parallel_goal_deliberation`**. Zero schema cost (MECH-261 is already implemented as a dictionary keyed on mode names, not a fixed tuple). Gets the naming aligned with the literature REE is actually grounding on.

## Proposed new mechanism claims

Two new MECH claims would ground SD-033e's functional scope in the literature. These are proposals only — to be executed in a separate governance session after the Prong D synthesis has been reviewed.

**MECH-264 (proposed) — Frontopolar counterfactual-value tracking.** SD-033e maintains, in parallel with SD-033c's chosen-option value signal, a running estimate of the value of unchosen alternatives. This signal drives switch-to-alternative decisions when the counterfactual estimate exceeds the chosen estimate by a threshold-sensitive margin. Grounded in Boorman 2009. Distinct from MECH-151 (vmPFC-analog value integration) in that the value is over unchosen options specifically.

**MECH-265 (proposed) — Frontopolar relative-importance monitoring across competing goals.** SD-033e maintains a representation of relative importance across a set of active goals (not just pairwise chosen-vs-alternative), enabling parallel-goal monitoring and flexible switching. Grounded in Mansouri 2017 synthesis; Mansouri 2015 lesion data specify the failure mode (ablation produces over-focus + inability to learn novel alternatives). Distinct from MECH-264 in that the signal is over-all-goals rather than pairwise, and distinct from MECH-261 in that it operates within SD-033e rather than gating writes across substrates.

A possible third claim (not proposed for registration in this pull) would cover the external/internal gateway function — but this overlaps too heavily with MECH-261's operating-mode gating to register separately without redundancy. The gateway function is better captured as part of SD-033e's substrate-level role description, with MECH-261 handling the cross-substrate write gating.

## Implications for SD-033e evidence_quality_note

SD-033e's current evidence_quality_note says: "Registered pre-implementation with intentionally thin evidence (one entry-level paper). A detailed lit-pull on frontopolar function (Burgess, Boorman, Christoff, Mansouri) is deferred until V4 design begins."

Proposed update after this pull: "Registered pre-implementation. Seven literature entries from Prong C (Koechlin & Summerfield 2007) and Prong D (Burgess 2000, Burgess 2007, Boorman 2009, Christoff 2009, Mansouri 2015, Mansouri 2017) support the V4 scoping. The Mansouri 2017 Nature Reviews synthesis is the load-bearing integrative account. Functional spec broadened from 'branching / nested control' to 'parallel-goal deliberation' (see Prong D synthesis). Mechanism claims MECH-264 (counterfactual value tracking) and MECH-265 (relative-importance monitoring) to be registered in a subsequent governance session."

## Priority ordering (for V4 design session, not for this session)

1. Apply evidence_quality_note update on SD-033e to reflect the broader functional spec.
2. Rename reserved V4 mode from `deliberative_branching` to `parallel_goal_deliberation` in MECH-261 and in SD-033e notes.
3. Register MECH-264 and MECH-265 grounding the Boorman and Mansouri 2017 mechanisms.
4. Update the SD-033 parent note to cite the extended evidence base.
5. When V4 design actually begins, revisit this synthesis — the four-converging-functions framing is the starting point for SD-033e's computational specification.

## Net aggregate (Prong D)

Literature support for the V4 scoping of SD-033e is strong. Mean confidence 0.81 across six entries (range 0.72–0.86). The four converging functions — counterfactual value, gateway switching, disengagement-for-exploration, relative-importance monitoring — form a coherent computational picture that integrates the Koechlin, Burgess, Boorman, Mansouri, and Christoff lines of work. The V3 implementation does not change; V4 scope is now better specified than the Koechlin-only framing originally registered.

