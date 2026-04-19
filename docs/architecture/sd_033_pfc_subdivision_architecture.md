---
nav_exclude: true
---

# SD-033: PFC Subdivision Architecture

**Claim ID:** SD-033 (parent) + SD-033a–e (subdivisions)
**Subject:** `pfc.subdivision_architecture`
**Status:** candidate, v3_pending (pre-implementation; SD-033c/d are graph-consolidation only)
**Registered:** 2026-04-19
**Depends on:** SD-032a, MECH-094, MECH-261, ARC-035, MECH-116, MECH-151, MECH-152, MECH-235
**Paired with:** SD-032 (cingulate integration substrate) — together form the V3 cognitive-control backbone

---

## Problem

MECH-261 (mode-conditioned write gating) commits to writing into "a PFC-analog policy/rule-level substrate," but ree-v3 has no registered substrate that does what primate / human lateral PFC actually does: hold stimulus-abstracted rule and goal representations across delays, persist them through distractor events, and emerge through training. The same audit turns up two other structural gaps. OFC is under-registered: existing claims lump OFC function under vmPFC (ARC-035 / MECH-151/152/235), losing the Rudebeck & Murray 2014 and Stalnaker et al 2015 dissociation between specific-outcome prediction and scalar-value integration. And nothing in ree-v3 reserves a substrate address for premotor/SMA sequence-execution (already implicit in E3) or frontopolar branching (V4 scope).

The risk is the same lumping failure mode that produced SD-003 → SD-010 → SD-011 on the nociceptive side: implement a monolithic "PFC-analog" module now and pay the cost of re-splitting later. The fix is to register the PFC as a five-subdivision cluster up front, using primate biology as the template, and scope implementation work to the subset that is actually load-bearing for V3.

The lit-pull (`targeted_review_pfc_subdivision_architecture`, 7 entries, mean confidence 0.80) supports this across three prongs: (A) lateral-PFC rule representation is a biologically distinct substrate (Miller & Cohen 2001; Badre & Nee 2018; Mansouri 2020); (B) OFC and vmPFC are dissociable by selective-lesion and cognitive-map evidence (Rudebeck & Murray 2014; Stalnaker et al 2015); (C) the lateral-PFC → pre-SMA → SMA → dorsal premotor gradient (Tanji & Hoshi 2008) locates sequence execution downstream of rule-holding, and frontopolar cortex (Koechlin & Summerfield 2007) carries the branching / nested-control function at the rostral end.

---

## Subdivisions

| ID | Subdivision | Biological analogue | ree-v3 function | V3 implementation status |
|---|---|---|---|---|
| SD-033a | Lateral-PFC-analog (mid-lateral rule/goal) | Mid-lateral PFC (Badre & Nee 2018 level) | Holds stimulus-abstracted rules/goals; projects top-down bias into E3 | **Build (minimum viable)** |
| SD-033b | OFC-analog (specific-outcome / task-structure) | OFC (Rudebeck & Murray 2014; Stalnaker 2015) | Specific-outcome prediction + cognitive map of task structure; E2's substrate address | Build (second priority) |
| SD-033c | vmPFC-analog (subjective value integration) | vmPFC (existing ARC-035 hub) | Scalar value integration across goals / needs / options | Register-only (graph consolidation) |
| SD-033d | Premotor/SMA-analog (sequence execution) | Pre-SMA + SMA + dorsal premotor (Tanji & Hoshi 2008) | Sequence proposal + execution (already inside E3) | Register-only (graph consolidation) |
| SD-033e | Frontopolar-analog (branching / nested control) | Frontopolar cortex / BA 10 (Koechlin & Summerfield 2007) | Counterfactual branching, suspended-operation return | **Defer (V4 scope)** — hooks only in V3 |

### SD-033a — Lateral-PFC-analog (mid-lateral rule/goal substrate)

**The V3 implementation priority.** Until SD-033a exists, MECH-261's "write gating on a PFC-analog" is vacuous — there is no real target for the gate to protect.

Must satisfy four functional signatures:

1. **Stimulus-abstracted format.** Representation encodes the rule that applies, not the specific stimulus the rule operates on (Mansouri 2020). Signature: transfer to novel stimuli under the same rule produces similar representational activity.
2. **Distractor-resistant persistence.** Rule-selective activity persists through simulated distractor stimuli, internal_replay events, and MECH-092 micro-quiescence cycles without being overwritten. This is what MECH-261's write-suppression-during-replay gate is protecting.
3. **Top-down bias into E3.** Projects a bias signal into E3's trajectory-selection machinery (multiplicative gain on trajectory scores or additive shift on rule-matched candidates — design choice during implementation). Miller & Cohen 2001 framing: rule-as-top-down-bias, not rule-as-direct-action-control.
4. **Training-dependent emergence.** Representations develop over many task exposures, driven by slow consolidation writes from hippocampal-cortical dialogue during offline_consolidation mode (Peyrache et al 2009; Frankland & Bontempi 2005).

**MECH-261 gating profile.** Writes licensed during external_task and internal_planning; suppressed during internal_replay (protect held rule); consolidative during offline_consolidation.

### SD-033b — OFC-analog (specific-outcome prediction / task-structure map)

Co-present representational content (MECH-263):

- **Specific-outcome prediction** (Rudebeck & Murray 2014 "oracle" framing). Given state s and action a, produce a prediction of the specific outcome — its identity, modality, expected magnitude — not just a scalar value. Devaluation sensitivity is the signature: if the value of outcome o changes while the state-action → outcome mapping does not, behaviour changes appropriately.
- **Cognitive map of task structure** (Stalnaker/Cooch/Schoenbaum 2015). Structured representation of what states the agent can be in, what transitions are possible, and what structural role each state plays — including discriminating between states that differ only in their latent structural role (same sensory input, same reward, different position in the task).

The two framings are not alternatives; they are complementary. The cognitive map carries structured outcome predictions, and specific-outcome queries are resolved against it. ree-v3's E2 is already a specific-outcome predictor computationally; SD-033b gives it a biological substrate address and makes its representational content (state-space structure) explicit.

**MECH-261 gating profile.** Speculative writes during internal_planning (counterfactual outcome queries); suppressed during internal_replay (do not overwrite the learned task model from imagined content); consolidative during offline_consolidation (slow updating from accumulated real-outcome experience — the systems-consolidation target); active read during external_task.

### SD-033c — vmPFC-analog (subjective value integration)

**Registration-only.** The computational function already exists in ree-v3 under ARC-035 / MECH-151 / MECH-152 / MECH-235. SD-033c registers it as a named subdivision of SD-033 so the PFC substrate graph is complete.

Reads specific-outcome predictions from SD-033b, affective / harm signals from SD-032, and homeostatic drive from SD-012; produces the unified subjective-value signal downstream selection machinery consults. Scalar value rides on top of SD-033b's structured representation — SD-033c does not itself represent specific outcomes or task structure (per Rudebeck & Murray 2014 and Stalnaker et al 2015 dissociations).

**MECH-261 gating profile.** Writes during external_task (value updates from realised outcomes); reduced-gain writes during internal_replay (replayed trajectories must not directly overwrite value estimates — this is what forces replay to propagate via SD-033a / SD-033b); consolidative during offline_consolidation.

### SD-033d — Premotor/SMA-analog (sequence execution)

**Registration-only.** Function already implemented inside E3's trajectory-proposal and selection machinery. Registered as a named subdivision so the claim graph mirrors the biology rather than implying a premotor-less architecture.

Corresponds to the Tanji & Hoshi 2008 pre-SMA (sequence planning, set-switching) + SMA (sequence execution) + dorsal premotor (stimulus-action binding) gradient, downstream of SD-033a. Finer-grained premotor subdivision is not registered here — if future evidence shows E3's trajectory machinery inadequately covers the pre-SMA / SMA / premotor distinctions, SD-033d can be split into SD-033d-i / d-ii / d-iii.

**MECH-261 gating profile.** Sequence-level writes are hypothesis-tagged via MECH-094 (the specific case): licensed during external_task and internal_planning; suppressed during internal_replay unless the hypothesis tag is explicitly set; consolidated during offline_consolidation.

### SD-033e — Frontopolar-analog (branching / nested control)

**V4 scope. Do not implement in V3.** Registered pre-emptively to (i) signal the architectural intent so V3 design choices stay forward-compatible, and (ii) prevent the SD-010/SD-011-style late-split failure mode from recurring at the V3/V4 boundary.

The substrate REE's V4 long-horizon ethical reasoning will eventually depend on — explicit counterfactual weighing of parallel policies is what Frankfurt-style reflective endorsement of first-order motivations requires, and Koechlin & Summerfield 2007 identify frontopolar cortex as the anatomical substrate for this function.

**V3 forward-compatibility requirement.** The MECH-261 `operating_mode` vocabulary should reserve a future mode name — candidate: `deliberative_branching` — and MECH-261's gate logic should be implemented as a dictionary keyed on mode names (not a fixed 4-tuple) so V4 can be added without disruptive schema changes.

**V4 prerequisite.** A follow-up lit-pull on frontopolar function (Burgess; Boorman; Christoff; Mansouri et al 2015 frontopolar review) is required before implementation. The Koechlin & Summerfield 2007 entry is the entry point, not the complete survey.

---

## Information flow

```
                     SD-032a (salience-network coordinator)
                          |
                          | operating_mode vector
                          v
                 +------------------------------------------+
                 |     MECH-261 mode-conditioned gates      |
                 +---+--------+---------+----------+--------+
                     |        |         |          |
                 external  internal  internal   offline
                    task   planning   replay   consolidation
                     |        |         |          |
                     v        v         v          v
  +----------------+   writes (soft-boundary, per-mode weight)
  |                |        |
  |  SD-033a <-----+--------+<----- consolidation writes
  |  (lateral PFC, |                 from HC/cortical dialogue
  |   rule/goal)   |                 (Peyrache 2009; Frankland
  |                |                  & Bontempi 2005)
  |  top-down bias |
  |  v             |
  |  E3 ------> SD-033d (premotor/SMA; inside E3)
  |  ^           |
  |  |           v
  |  |         actions
  |  |
  |  | queries (state, action)
  |  v
  |  SD-033b <----- writes: speculative (planning), consolidative (offline)
  |  (OFC, specific-outcome    suppressed during internal_replay
  |   + task-structure map)
  |    |
  |    | structured outcome predictions
  |    v
  |  SD-033c <----- value writes: external_task (realised),
  |  (vmPFC,         reduced-gain internal_replay
  |   scalar value)
  |    |
  |    | unified value signal
  |    v
  |  E3 trajectory scoring (combined with SD-033a bias)
  +----+
       |
       | (SD-033e frontopolar: deferred; hook = reserved mode name only)
       .
       .

  SD-032 (cingulate) <---- cross-cluster: SD-032b adaptive-control
                           writes to striatal-analog, bypassing SD-033c
                           for the affective-pain -> action-value channel.
                           Dopamine-analog credit assignment shapes
                           the ACC->striatum weight.
```

**The interface contract with SD-032.** SD-032a emits `operating_mode`; MECH-261 translates that vector into per-substrate gate weights; SD-033 subdivisions consume the gates. SD-033a is MECH-261's primary write target under external_task and internal_planning. SD-033b is the secondary target under internal_planning and offline_consolidation. SD-033c is gated with reduced-gain during internal_replay to force replay to propagate through SD-033a / SD-033b rather than directly overwriting value. SD-033d inherits MECH-094 hypothesis-tag gating as a special case.

**The within-cluster gradient.** SD-033a → SD-033d captures the Tanji & Hoshi lateral-PFC → pre-SMA → SMA → dorsal premotor executive-control gradient: rule at the rostral end, sequence execution at the caudal end. SD-033b and SD-033c sit off-axis as the specific-outcome and scalar-value substrates feeding E3's trajectory evaluation.

---

## Minimum-viable V3 implementation path

Ordered. Do not skip ahead.

1. **SD-033a (lateral-PFC-analog).** Minimum-viable substrate. Build as a persistent rule/goal-holding module with (i) stimulus-abstracted representation, (ii) distractor-resistant persistence, (iii) top-down bias projection into E3, (iv) MECH-261-gated write interface. Design-level choices to settle during implementation: format of rule representation (population code vs distributed embedding vs explicit symbolic), persistence mechanism (recurrent activity vs synaptic hold), bias-signal projection (multiplicative gain vs additive shift into E3 trajectory scores). Test MECH-262's three signatures (generalisation, distractor-resistance, training-dependent emergence) before declaring complete.
2. **SD-033b (OFC-analog).** Second priority. Give E2 a proper substrate address. Current E2 state carries both sensory prediction and harm prediction in an unstructured latent; SD-033b should carry the structured outcome representation explicitly and serve as the substrate E2's harm-prediction queries hit. Verify MECH-263 signatures (devaluation sensitivity; discrimination of same-value / different-outcome-identity states).
3. **SD-033c (vmPFC-analog).** Register-only. No new implementation — existing ARC-035 / MECH-151 / MECH-152 / MECH-235 code is the substrate. Update cross-references so those claims point to SD-033c as their substrate address.
4. **SD-033d (premotor/SMA-analog).** Register-only. No new implementation — existing E3 trajectory machinery is the substrate. Update cross-references. Finer-grained split is a follow-up if evidence demands.
5. **SD-033e (frontopolar-analog).** Defer to V4. In V3, the only change is the MECH-261 schema forward-compatibility: operating_mode as a keyed dict (not a fixed tuple), and reserve a `deliberative_branching` mode name.

**Steps 1–2** are the V3 implementation targets. Steps 3–4 are graph consolidation. Step 5 is a schema-only commitment with V4 follow-up lit-pull.

---

## Falsification signatures

Substrate-level. Each signature distinguishes a specific subdivision failure from downstream wiring issues.

**SD-033a (lateral-PFC-analog) is over-specified** if: ree-v3's existing E3 sequence-selection machinery reproduces — without an explicit rule/goal substrate — all three MECH-262 signatures: rule-abstracted generalisation (transfer to novel stimuli under the same rule), rule-selective persistence across distractor events, and training-dependent rule emergence. Collapses SD-033a back into E3 and makes MECH-261's "write target" vacuous in a different way (no substrate because none is needed).

**SD-033a failure at source** if: the implementation shows stimulus-bound persistence (fires only for trained stimuli, fails to generalise) or distractor-fragile persistence (representation collapses when internal_replay events intervene). MECH-262 is violated — SD-033a does not meet its functional spec.

**SD-033b (OFC-analog) is over-specified** if: E2's harm-prediction behaviour and rule-conditioned outcome-generalisation can be reproduced without distinguishing a state-structure substrate from a scalar-value substrate. The OFC/vmPFC functional dissociation does not carry at REE's level of description; SD-033b collapses back into SD-033c.

**MECH-263 failure at source** if: SD-033b activity encodes scalar value without discriminating between same-value / different-outcome-identity states; or fails the devaluation-sensitivity test. SD-033b is functionally indistinguishable from SD-033c.

**SD-033c / SD-033d registration failures** are not directly falsifiable at the substrate level — these subdivisions are registration-only consolidations of existing function. The load-bearing falsifications for their claimed function live on the source claims (ARC-035 / MECH-151 / MECH-152 / MECH-235 for SD-033c; E3 trajectory experiments for SD-033d).

**MECH-261 cross-mode gating over-specification** (primary SD-032 × SD-033 interaction test): if a ree-v3 implementation using purely local per-substrate gating (no shared `operating_mode` vector from SD-032a) reproduces the post-quiescence action-selection bias toward recently replayed trajectories, the coordinator overlay is wrong — forward propagation would be coordinated locally rather than by the salience network. See EXP-0148.

**Rule protection failure** (SD-033a × MECH-261 interaction): SD-033a rule representations should remain stable across internal_replay events even when replay content is rule-incompatible, because MECH-261 suppresses writes into SD-033a during replay. Failure signature — replay events overwrite the held rule, rule-selective persistence collapses — falsifies either SD-033a's persistence mechanism or MECH-261's replay-suppression gate. Use a replay-content-controlled ablation to distinguish the two.

---

## Cross-cluster interaction with SD-032

SD-032 produces `operating_mode`. SD-033 holds the substrates `operating_mode` gates writes into. See `sd_032_cingulate_integration_substrate.md` for the cingulate-side design and for the full MECH-261 write-gating profile table.

Two concrete interaction signatures expected to be visible in V3:

1. **Forward propagation bias** (MECH-261 primary behavioural signature). Content active in internal_replay produces a measurable bias on subsequent external_task action selection, mediated by writes into SD-033a during replay (Tambini & Davachi 2019). This is both a design requirement and MECH-261's primary falsification target.

2. **Cingulate → PFC bypass asymmetry**. SD-032b (dACC-analog) writes to a striatal-analog action-value target *bypassing* SD-033c (vmPFC value integration) — this is the Baliki 2010 ACC-NAc pathway. Predicts: affective-pain-driven action-value shifts are not reflected in SD-033c activity in the same way that reward-driven shifts are. The cingulate cluster has its own write-path into action selection that does not route through PFC value integration.

---

## Related claims

- **SD-033, SD-033a–e** — this cluster
- **MECH-262** — rule-selective persistence in SD-033a (three signatures)
- **MECH-263** — OFC-analog state-space / specific-outcome representation
- **SD-032, SD-032a–e** — paired cluster (coordinator + adaptive control)
- **MECH-261** — mode-conditioned write gating (primary consumer of SD-033)
- **MECH-094** — hypothesis tag (special case, specifically on SD-033d sequence commits)
- **ARC-035** — vmPFC value-regulation hub (subsumed by SD-033c)
- **MECH-151, MECH-152, MECH-235** — vmPFC value integration (folded into SD-033c)
- **MECH-116** — dlPFC LSTM working memory (adjacent to SD-033a)
- **ARC-038** — viability map (MECH-261 write target alongside SD-033)
- **ARC-039** — entorhinal grid loop (offline consolidation target alongside SD-033)
- **INV-049** — sleep necessity (coordinates offline_consolidation mode for SD-033 writes)

## References

Primary lit-pull: `evidence/literature/targeted_review_pfc_subdivision_architecture/synthesis.md`
(7 entries across three prongs, mean confidence 0.80, 2026-04-19).

Systems-consolidation grounding for MECH-261 offline writes into SD-033a/b:
`evidence/literature/targeted_review_systems_consolidation_waking_propagation/synthesis.md`
(5 entries, aggregate literature_confidence 0.883, 2026-04-19).

Key entries:

Prong A (lateral-PFC rule representation):
- Miller & Cohen 2001 (*Annu Rev Neurosci*): PFC as active maintenance of task-relevant rules, biasing posterior processing.
- Badre & Nee 2018 (*Trends Cogn Sci*): caudal-rostral abstraction gradient within lateral PFC.
- Mansouri, Freedman & Buckley 2020 (*Nat Rev Neurosci*): stimulus-abstracted rule-selective neurons in primate lateral PFC; persistence across delays; training-dependent emergence.

Prong B (OFC / vmPFC dissociation):
- Rudebeck & Murray 2014 (*Neuron*): selective fiber-sparing lesions dissociate OFC (specific-outcome prediction / credit assignment) from vmPFC (subjective value integration).
- Stalnaker, Cooch & Schoenbaum 2015 (*Nat Neurosci*): OFC represents cognitive maps of task structure, not scalar value.

Prong C (premotor/SMA + frontopolar V3/V4 scoping):
- Tanji & Hoshi 2008 (*Physiol Rev*): graded executive control across lateral PFC → pre-SMA → SMA → dorsal premotor.
- Koechlin & Summerfield 2007 (*Trends Cogn Sci*): frontopolar cortex as substrate for branching and nested control (entry point; full V4 survey deferred).

Systems-consolidation supporting MECH-261 writes into SD-033a/b:
- Peyrache et al 2009 (*Nat Neurosci*): SWR-coupled rule-learning replay in mPFC.
- Frankland & Bontempi 2005 (*Nat Rev Neurosci*): systems consolidation from hippocampus to neocortex.
- Carr, Jadhav & Frank 2011; Tambini & Davachi 2019; Rothschild/Eban/Frank 2017 (soft-boundary mode mixing; forward-propagation bias; cortical-hippocampal-cortical loop).
