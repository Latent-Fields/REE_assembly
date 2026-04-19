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

## Net aggregate

Literature support across all three prongs is strong. Mean confidence 0.80 across seven entries (range 0.72–0.85). All seven entries point in the same direction: the "PFC analogue" that REE currently treats as a monolith is biologically a graded, multi-subdivision system, and registering it properly as an SD cluster (rather than as a single substrate) will prevent the same kind of late re-split that SD-003 and SD-010 required.
