# Synthesis — Cingulate Integration Substrate for REE

**Session:** litpull-cingulate-integration-substrate-2026-04-19
**Claims informed (target):** new SD cluster (proposed SD-032 and sub-claims) for cingulate substrate; disambiguates z_harm_a consumer question (Options A/B/C) as one sub-problem
**Papers:** 9 entries, covering affective/sensory dissociation (Price 2000), ACC/MCC/PCC subdivisions (Vogt 2005), AIC interoception/salience (Craig 2009), dACC integration meta-analysis (Shackman 2011), ACC-NAc value coupling (Baliki 2010), pain as precision-weighted control signal (Seymour 2019), dACC effort learning (Scholl/Kolling 2015), PCC arousal/attention coordinator (Leech & Sharp 2013), salience-network framework (Menon & Uddin 2010)

---

## The reframing this pull forces

The original governance question -- "how should z_harm_a reach action selection: Option A (add to trajectory cost), Option B (forward-rollout cost), or Option C (urgency interrupt)?" -- is mis-posed. The biology says **all three are real, each performed by a different cingulate subdivision, and the substrate that unifies them is a network-level coordinator, not a wire**.

The investigation of EXQ-395 revealed a wiring gap -- z_harm_a is produced and not consumed. That framing was too narrow. The actual gap is that ree-v3 has no **cingulate integration substrate**: no coordinated network that partitions the cingulate's several computational jobs across subdivisions and selects between operating modes on the basis of salient events. The z_harm_a wiring gap is one surface symptom; the monostrategy failure (fishtank_viz), the SD-021 broken descending modulation, the unspecified urgency interrupt, and the lack of mode-conditioned write gating are all other surface symptoms of the same missing substrate.

## Cingulate subdivisions and their ree-v3-relevant functions

Synthesising across the 9 entries:

| Region | Primary function | ree-v3 analog needed | Current state |
|---|---|---|---|
| **AIC (anterior insula)** | Interoceptive salience, urgency detection, network switching | Salience-network hub that triggers mode transitions on any salient event (z_harm_a spike, z_goal gap, z_harm_s surprise) | **Absent.** `urgency_weight` is a local stub, off by default |
| **dACC / aMCC (dorsal ACC / anterior midcingulate)** | Integration of negative affect, pain, cognitive control -> behavioural-adjustment magnitude | dACC-analog: reads (z_harm_a PE, z_conflict, control demand); outputs policy-update magnitude that shapes trajectory scoring | **Absent.** Trajectory cost sums z_harm_s only; no integration |
| **pMCC (posterior midcingulate)** | Motor engagement, effort gating | Beta-gate on committed actions; suppresses motor output during non-commit phases | **Partial.** MECH-090 beta propagation gate exists; SD-021 broken |
| **pACC / sgACC (perigenual / subgenual)** | Affective pain -> autonomic/valence coupling; visceral integration | Connection from z_harm_a to autonomic/valence state (drive_level) and through SD-012 homeostatic state | **Absent.** z_harm_a has no autonomic coupling |
| **PCC (posterior cingulate)** | Internal/external attention partition, metastability tuning, DMN coordinator | Mode-switching coordinator between task-execution and replay/consolidation | **Partial.** INV-049 sleep, MECH-092 quiescence replay exist but no explicit coordinator |
| **Salience network coordinator (AIC+dACC coupling)** | Switches operating modes on salient events | Network-level mode variable that gates all the above | **Absent.** No operating-mode abstraction |

The ree-v3 pattern is clear: **each subdivision's function is either absent or present as a fragment**. Nothing coordinates them. The new SD cluster must specify both the individual subdivision functions and the network-level coordinator that binds them.

## The algorithmic form (from Seymour 2019 + Shackman 2011)

Seymour's precision-weighted framing gives the algorithmic backbone that the other papers support:

1. **z_harm_a enters as a precision-weighted prediction error** against an internal pain forward model (SD-020, harm_surprise_PE, currently provisional -- this pull upgrades it to prerequisite).
2. **dACC-analog integrates** this PE with cognitive-conflict and control-demand signals, producing a **behavioural-adjustment magnitude** (Shackman's adaptive control hypothesis, made algorithmically specific by Seymour's framework).
3. **dACC writes to a striatal-analog action-value target** (Baliki's ACC-NAc coupling), with the weight being **learnable** (plasticity finding -- chronic pain shifts the coupling).
4. **If precision/urgency exceeds a threshold**, the AIC-dACC salience network triggers a **network-level mode switch** (Menon & Uddin) rather than an incremental policy update -- the smooth-RL/mode-switch threshold is where Craig's urgency-interrupt lives.
5. **The current operating mode** (selected by the salience-network coordinator, with PCC-analog contribution) **determines which downstream gates are open**: write-gates on E3, policy-commitment, access to offline replay, autonomic coupling.

So the three original options resolve like this:

- **Option B (forward rollout) is prerequisite.** The precision-weighted PE requires a pain forward model. Without this, z_harm_a is a scalar magnitude, not a control signal. Build first.
- **Option A (trajectory-level integration) is the dACC function.** Given the forward model, the dACC-analog integrates PE with control demand and writes to a striatal-analog target that shapes trajectory selection.
- **Option C (urgency interrupt) is the salience-network-switch function.** Fires when precision/urgency exceeds a threshold; produces whole-system mode change, not local cost modification.

All three must exist; they operate in a specific sequence; and they are not substitutes for each other.

## Proposed claim structure for the new SD cluster

Not registering in this session -- proposing structure for the governance discussion that follows.

### Substrate claims (new)

- **SD-032** (proposed): Cingulate integration substrate. A network-level module with AIC-, dACC/aMCC-, pMCC-, pACC-, and PCC-analog subdivisions coupled into a salience-network coordinator. Primary output: operating-mode variable + behavioural-adjustment-magnitude signal.
- **SD-032a**: Salience-network coordinator. Network-level module reading all subdivisions; outputs discrete operating-mode variable (external_task, internal_replay, internal_planning, offline_consolidation). Triggers mode switches on salient events.
- **SD-032b**: dACC-analog (adaptive control). Reads z_harm_a precision-weighted PE, z_conflict, control-demand; outputs behavioural-adjustment magnitude. Writes to striatal-analog action-value target. Weight is learnable.
- **SD-032c**: AIC-analog (interoceptive salience). Detects salient interoceptive events (including z_harm_a); gated on interoceptive baseline (drive_level from SD-012); triggers network-switch signal.
- **SD-032d**: PCC-analog (attention partition). Coordinates transitions between task-execution and internal modes; contributes metastability / stability-of-mode parameter.
- **SD-032e**: pACC-autonomic coupling. Connects affective-pain stream to valence/drive update pathway.

### Mechanism claims (new)

- **MECH-258** (proposed): Precision-weighted pain PE drives dACC-analog policy updates. Upgrades SD-020 from provisional to prerequisite.
- **MECH-259** (proposed): Salience-network switch threshold. Below threshold -> smooth-RL update; above threshold -> network-mode switch.
- **MECH-260** (proposed): dACC bias-suppression against recency. Counter-bias that resists monostrategy. Possible mechanistic explanation of fishtank_viz monostrategy pattern.
- **MECH-261** (proposed): Mode-conditioned write gating. Operating mode (from SD-032a) determines which substrates can write to E3, memory consolidation, policy update. Generalises MECH-094 hypothesis tag.

### Existing claims affected

- **SD-011** (dual nociceptive streams): supported, unchanged -- the dual-stream substrate is correct.
- **SD-020** (harm_surprise_PE): upgraded from provisional to prerequisite for SD-032b.
- **SD-021** (descending modulation): folded into SD-032c -- descending modulation in biology is the AIC-analog dialling down sensory pain via autonomic coupling. The current SD-021 bug may resolve naturally when SD-032c is implemented.
- **SD-012** (homeostatic drive): now load-bearing for SD-032c (interoceptive baseline that gates AIC).
- **MECH-091** (salient-event phase reset): identified as specifically an AIC -> dACC phase-reset mechanism; stays as-is but gains biological context.
- **MECH-094** (hypothesis tag): generalised by MECH-261 (mode-conditioned write gating).
- **MECH-220** (cingulate-insula harm hub): weakened as posed but replaced by SD-032. The "hub" was the right intuition; the architecture needed wasn't a single modification module, it was a full network coordinator.
- **INV-049** (sleep necessity), **MECH-092** (micro-quiescence replay): both become expressions of PCC-analog operating-mode coordination.

## Implementation order (proposed sequencing)

If the governance discussion accepts the cingulate-substrate framing, the implementation dependency graph suggests this sequence:

1. **Pain forward model (SD-020 / MECH-258)** -- must come first. E2_harm_a module forecasting expected z_harm_a given trajectory. Shares substrate with the already-planned E2_harm_s for SD-003.
2. **Homeostatic drive state (SD-012)** -- provides the interoceptive baseline AIC-analog needs. Already has substrate work pending.
3. **dACC-analog (SD-032b)** -- the z_harm_a consumer proper; reads the forward-model PE, writes striatal action-value target. This is what "fixing z_harm_a wiring" becomes.
4. **AIC-analog + salience-network coordinator (SD-032c + SD-032a)** -- interrupt-switch function. Requires dACC-analog to be running.
5. **Mode-conditioned write gating (MECH-261)** -- generalisation of MECH-094, depends on operating-mode variable from SD-032a.
6. **PCC-analog (SD-032d)** and **pACC autonomic (SD-032e)** -- last, because they are refinements rather than core functionality.

Step 3 alone would resolve the EXQ-395 wiring gap and give ree-v3 a principled affective-pain action-value pathway. Steps 1-3 together give the minimum viable cingulate substrate.

## Honest uncertainties

- **Whether this is one substrate or a cluster.** The biology supports a network framing (salience-network coordinator binds the subdivisions), but ree-v3 can in principle implement the subdivisions in one torch module or several. The anatomy does not dictate the software architecture; it dictates the *functions* that must be separately computable. A single module that computes all of them cleanly would be acceptable biology; a several-module design tracking the anatomy is also acceptable.
- **Whether the full Seymour precision framework is worth the substrate cost.** Adopting it means building a pain forward model, a precision estimate, and the PE-integration pathway before any dACC-analog can be tested. A simpler alternative (bypass precision, wire z_harm_a directly to a striatal-analog) would get the wiring fixed faster but wouldn't reproduce the context-dependence the biology documents. Cost-benefit is a judgement call.
- **Whether ree-v3's trajectory-based planning paradigm is the right target for this substrate.** The biology was selected for evolved embodied mammals making real-time decisions in sensorimotor environments; ree-v3's current paradigms (causal grid world, etc.) are crude approximations. The cingulate substrate may reveal itself only in richer paradigms with real temporal dynamics and context.
- **The monostrategy / bias-suppression finding (Scholl/Kolling).** I've proposed MECH-260 on the strength of one paper -- this should probably get its own lit-pull before registering, or be registered as candidate with a note that the bias-suppression claim needs replication evidence.

## Recommendation

**Accept the cingulate-substrate framing for the new SD cluster.** The biological evidence strongly supports treating the cingulate as an integration network, not as an ad hoc set of modules. The EXQ-395 "z_harm_a consumer" question is genuinely one sub-problem in this framing, and it gets a clean biological answer: the consumer is a dACC-analog that integrates a precision-weighted pain PE with control demand and writes to a striatal action-value target, with network-level mode switching handling the urgency-interrupt case.

**Next steps:**
1. This synthesis is the scoping input. Present to governance for decision on whether to register SD-032 and the sub-claims.
2. Reclassify EXQ-395 manifest: `evidence_direction: non_contributory` with note "diagnostic of missing cingulate integration substrate; evidence replaced by lit-pull on cingulate architecture".
3. Decision on pacing: register the full cluster now or start with SD-032b (dACC-analog) as a minimum-viable z_harm_a consumer and extend later.
4. A second lit-pull may be worthwhile on the MCC effort-value / credit-assignment line (Rushworth lab beyond Scholl/Kolling) if SD-032b is to be implemented with full computational specification.

The broader implication: ree-v3 has been building individual substrates without a clear model of the *network-level* control architecture. The cingulate-substrate framing suggests the system currently has many of the right components (E1, E2, E3, hippocampal map, harm streams, commit boundary) but no coordinator that selects among operating modes on salient events. Several "wiring gap" and "condition-dispatch bug" failures (EXQ-395, EXQ-325a SD-021, EXQ-355a ARC-038, EXQ-435 INV-054) may share this common root: the substrate for coordinated mode selection does not exist yet.
