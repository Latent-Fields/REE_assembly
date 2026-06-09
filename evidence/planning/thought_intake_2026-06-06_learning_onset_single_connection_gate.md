# Thought Intake (Stage 2): Learning onset as a connection-level plasticity / write-authority gate

Raw thought file: [docs/thoughts/2026-06-06_learning_onset_single_connection_gate.md](../../docs/thoughts/2026-06-06_learning_onset_single_connection_gate.md)

**Stage-2 processed:** 2026-06-09
**Disposition:** architecture compass (learning-onset / plasticity write-authority). NOT a claim registration, NOT a substrate-design memo, NOT a REE-v3 critical-path item. Off the GAP-7 closure path.
**Source-check:** RESOLVED (the raw note left it "source-check pending" because the `share.google` link was dead and the title was not located during raw capture). See section 1.

---

## 1. Source verification (resolves the raw note's "pending" status)

The raw note recorded the `share.google` link as inaccessible and the exact title as not located. Both are now resolved by web search:

- **Neuroscience News article:** "Single Brain Connection Pinpointed as the Starting Point of Learning" -- https://neurosciencenews.com/basal-ganglia-synapse-learning-30679/ (the title and framing match the saved email exactly).
- **Primary peer-reviewed paper:** Drew C. Schreiner, Samuel Brudner, Amanda Li, John Pearson, Richard Mooney, **"A synaptic locus of song learning,"** *Nature* (2026), DOI 10.1038/s41586-026-10510-x (Duke University School of Medicine).
- **Species / system:** zebra finch (*Taeniopygia guttata*) vocal (song) learning.
- **Brain region / synapse:** a specific class of **cortico-basal-ganglia synapses** within the basal ganglia.
- **Key finding (quoted/paraphrased):** using optogenetics to isolate specific synapses, the authors pinpoint where song learning is "first expressed and maintained." Silencing that specific synapse set reverts the bird's song toward a more immature version, establishing those synapses as the locus where the learned motor behavior is **first expressed and held**, before consolidation spreads downstream.

**Evidentiary weight:** this is a genuine primary *Nature* study (not a press-only summary), but it is **single-system (songbird vocal motor learning) and lesion/optogenetic-localisation in scope**. It supports "learning has an identifiable first-expression locus in a cortico-BG circuit"; it does NOT support "all learning reduces to one synapse," and the raw note's own guardrails (section 6/9) correctly forbid that reading. For REE this remains a **compass-level architectural prompt**, not citable mechanism evidence for any REE claim. The cross-species bridge the article draws (songbird BG <-> human BG, dopamine-guided motor learning, Parkinson's/Tourette relevance) is suggestive, not established for REE's substrate.

---

## 2. Verbatim thought (raw capture, preserved)

> A saved REE email pointed to a Neuroscience News item titled "Single Brain Connection Pinpointed as the Starting Point of Learning". The direct `share.google` link was not accessible during intake, and exact-title searches did not locate the article. Therefore this note preserves the possible REE-relevant mechanism as source-check pending, not as verified evidence.
>
> The useful REE idea is:
>
> > learning may begin at a specific connection/gate where salience, prediction error, attention, and plasticity first become write-authorised.
>
> This is not a claim that all learning reduces to one synapse or one connection. The architectural prompt is that learning onset may require a specific transition from observation to writable update, and that this transition may be local, gated, and connection-specific.
>
> REE may need to distinguish at least four learning states:
> 1. **Observed** -- an event is represented but has no durable write authority.
> 2. **Flagged** -- salience/attention marks the event as potentially relevant.
> 3. **Write-eligible** -- the relevant pathway or trace opens to durable modification.
> 4. **Consolidated** -- later replay/offline integration stabilises or contextualises the update.
>
> Possible computational primitive:
> `learning_onset = f(prediction_error, salience, attention, pathway_state, residue_status, goal_relevance, plasticity_eligibility)`
>
> The correct near-term extraction is: preserve learning-onset as a gated transition from observation to write-eligible cognifold deformation. The incorrect extraction is: make all REE learning depend on one literal connection or undifferentiated global update.

(Full raw note, including the mapping table, cautions, and guardrails, is in the raw thought file.)

---

## 3. What's New vs Existing REE Docs (novelty table)

| Strand in the thought | Existing REE coverage | Genuinely new? |
|---|---|---|
| Learning has a local, gated **first-expression locus** (not a global undifferentiated update) | REE gates writes by **operating mode** (MECH-261 mode-conditioned write gating) and by **content provenance** (MECH-094 simulation-vs-real write profile); commitment is gated by an **eligibility layer** (MECH-058-family "commitment eligibility gated by tau/rho/phi"; E3 tri-loop pre-commit eligibility). | **Partly new.** REE has write-*gating* and commit-*eligibility*, but framed at the mode/provenance/commit-decision grain -- not as a distinct **per-event, local "write-eligible" learning state** sitting between salience-flagging and durable write. |
| Explicit **four-state ladder**: Observed -> Flagged -> Write-eligible -> Consolidated | Pieces exist but scattered: perception/E1 (Observed); salience/attention precision SD-032a + the distributed-attention cluster (Flagged); MECH-094/261 write gates (a write-decision, not a held "eligible" state); sleep/replay consolidation cluster MECH-273/275/285 (Consolidated). | **New as an explicit, named state ladder.** The middle "write-eligible" state -- an event held as plasticity-eligible-but-not-yet-written -- is the under-represented rung. |
| Learning-onset as `f(prediction_error, salience, attention, pathway_state, residue_status, goal_relevance, plasticity_eligibility)` | INV-034 (goal maintenance), z_goal goal-stream (MECH-112/116), salience network SD-032a, residue field, plasticity-window cluster -- all exist as separate primitives. | **New as a composition.** No single REE claim composes these into one onset/write-authorisation function. |
| **Opening side** of plasticity at the **event/connection grain** | The 2026-06-01 plasticity-window-neuromodulators note already owns the opening side at the **window/state grain** (ACh/PV/BDNF state-conditional learning-rate gain; developmental critical periods). | **Adjacent, distinct grain.** See section 5 -- cross-reference, do NOT conflate. |
| Harm-residue may open write authority **without** opening action authority | INV-011 imagination-without-belief; MECH-094 provenance gate; harm-stream separation (SD-010/SD-011). | **Sharp new question**, not currently posed as a claim: can a write-authority gate be opened by harm residue while the action-authority gate stays shut? |

---

## 4. Key formulations (REE-translated)

1. **Write-authority gate (the core extraction).** Model the transition *observed event -> write-eligible cognifold deformation* as an explicit gated state, distinct from (a) the operating-mode write gate (MECH-261), (b) the provenance write gate (MECH-094), and (c) the commit-eligibility layer for action selection. The gate's defining property: an event can be *salient and represented* yet still **not authorised to deform the durable model**.

2. **Four-state learning ladder.** Observed -> Flagged -> Write-eligible -> Consolidated. The architectural contribution is naming **Write-eligible** as a first-class intermediate state with its own entry/exit conditions, rather than collapsing "salient" directly into "written."

3. **Onset as a multi-input gate, not a scalar.** Learning onset is conditioned jointly on prediction error, salience/attention, local pathway state, residue status, goal relevance, and plasticity eligibility -- it is *what kind* of change, *where* in the cognifold, and *whether the system is licensed* to let it reshape future trajectories.

4. **Locality.** The biological result is that first-expression is **local and circuit-specific** (a particular cortico-BG synapse class). REE analogue: write-authorisation may be edge/field-local, not a global learning-rate switch -- consistent with REE's existing region/edge structure but not currently expressed as a learning-onset primitive.

5. **Decoupling write-authority from action-authority.** The guardrail that "plasticity write authority must not bypass ethical residue, provenance, or self/world tagging" maps onto a concrete open question: harm residue opening *write* authority without opening *action* authority.

---

## 5. Relationship to the plasticity-window-neuromodulators thought (cross-reference, NOT conflation)

Both notes are "opening side" of plasticity, but at **different grains** -- they are siblings, not duplicates:

| | 2026-06-01 plasticity-window-neuromodulators | 2026-06-06 learning-onset single-connection gate (this note) |
|---|---|---|
| Grain | **Window / global state** -- when is the system in a high-plasticity regime | **Event / local connection** -- does *this* perceived difference become write-authorised |
| Mechanism reference | ACh / PV-interneuron / BDNF; nucleus-basalis-analog state-conditional learning-rate gain; developmental critical periods | cortico-BG synaptic first-expression locus (Schreiner et al. 2026) |
| Question it poses | "What raises/lowers the learning-rate gain over a window?" | "What transitions an observed event into a write-eligible update, locally?" |
| REE status | processed, canonical framing paragraph; opening-side gap vs INV-074/MECH-333/MECH-334 closure side | this intake; opening-side at the per-event grain |

**Do not merge them.** A window-level plasticity gain can be open while a given event still fails the per-event write-authority gate (and vice versa). Conflating the two would erase exactly the distinction (state-level vs event-level gating) that makes each useful. If either is ever registered, they should cross-reference, not collapse.

The **closure side** is already built and is the inverse of both opening-side notes: INV-074 (plasticity crystallization necessity, universal invariant), MECH-333 (critical-period open-phase / trainable-substrate handling), MECH-334 (closure + EWC write-protect), ARC-075 (infant-curriculum plasticity-magnitude asymmetry), design doc `docs/architecture/critical_period_crystallization.md`. This note is upstream of all of those: it concerns *whether an event ever becomes write-eligible in the first place*, before crystallization closes the window.

---

## 6. Affected existing claims (real IDs, verified against claims.yaml)

None require any status change. Listed as the touch-points a future registration or architecture note would have to reconcile against:

- **MECH-094** -- simulation-vs-real write-profile distinction (provenance write gate; confabulation failure mode). The write-authority gate would sit alongside this, not replace it.
- **MECH-261** -- mode-conditioned write gating (operating mode determines which substrates can write to E3/episodic/policy/autonomic). **Closest existing structural match** to a "write-authority gate," but mode-conditioned, not event-local. A per-event write-eligible state would most naturally be an *extension/child* of MECH-261, not a new top-level invariant.
- **MECH-283** -- recognition-for-recall gate (retrieval-time eligibility). Analogue on the recall side of the same "eligibility-before-use" pattern.
- **MECH-058-family / E3 tri-loop pre-commit eligibility** -- "commitment eligibility gated by tau/rho/phi"; eligibility as the pre-commit layer for action. The thought's "write-eligible" is the *learning/plasticity* analogue of this *action/commit* eligibility -- a deliberate parallel worth preserving.
- **INV-034** + **z_goal goal-stream (MECH-112/116)** -- the `goal_relevance` input to the onset function. (Note the standing z_goal-salience-competitiveness caveat in project_v3_v4_boundary: any goal-gated write-authority depends on z_goal salience actually being competitive.)
- **INV-074 / MECH-333 / MECH-334 / ARC-075** -- the closure side; this note is the upstream complement (see section 5).
- **INV-011** (imagination-without-belief), **SD-010/SD-011** (harm-stream separation) -- the substrate against which the "harm residue opens write- but not action-authority" question would be posed.
- **SD-032a** salience-network coordinator + the distributed-attention cluster (per memory project_attention_distributed_precision_selection) -- the `salience`/`attention` inputs to the onset function.

---

## 7. Candidate claims FOR FUTURE REGISTRATION (do NOT register now)

Recorded for a future session only. Per the standard thought-intake default and this thought's own guardrails, **none are registered in claims.yaml in this pass.** All are off the V3/GAP-7 critical path and substrate-leaning (V4 or late-V3).

- **CANDIDATE Q (answer_state / open_question):** "Should REE represent a distinct **write-eligible** learning state between salience-flagging and durable write, or is mode-conditioned (MECH-261) + provenance (MECH-094) gating already sufficient?" Likely resolves as either *no new claim* (subsumed by MECH-261) or a child of MECH-261.
- **CANDIDATE MECH (mechanism_hypothesis, substrate_conditional, V4):** event-local **write-authority gate** -- a per-event transition `observed -> write-eligible` conditioned on (prediction_error, salience, pathway_state, residue_status, goal_relevance, plasticity_eligibility); most naturally an extension of MECH-261, not a new top-level invariant.
- **CANDIDATE Q (out_of_domain or substrate_conditional):** "Can harm **residue** open *write* authority without opening *action* authority?" -- posed against INV-011 / SD-010/SD-011.

**Explicit non-registration of duplicates:** the four-state ladder's endpoints (Observed = perception/E1; Consolidated = sleep/replay cluster MECH-273/275/285) are already owned and must NOT be re-registered. Only the middle **Write-eligible** rung is genuinely under-represented.

---

## 8. Next steps

1. **No claim registration, no substrate, no experiment** in this pass (compass; off critical path; substrate-leaning -> any probe would be vacuous on the current substrate, same posture as the play-mode and competitive-coupling intakes).
2. If/when revisited: decide first whether the "write-eligible" state is a **child of MECH-261** or a standalone primitive -- this fork determines everything downstream. Default expectation: child of MECH-261.
3. Keep the **opening-side pair** (this note + 2026-06-01 plasticity-window-neuromodulators) cross-referenced; if a unifying architecture note is ever written, locate it at something like `docs/architecture/plasticity_write_authority_gating.md` covering both grains plus the INV-074/MECH-333/MECH-334 closure side.
4. The harm-residue / write-vs-action-authority question is the most decision-relevant strand and the one most worth a future lit-pull (FEP epistemic value; eligibility-trace / three-factor plasticity literature; Schreiner et al. 2026 cortico-BG locus).

---

## 9. Guardrails carried forward (from the raw note)

- Do not cite the songbird result as evidence for any REE claim (compass only).
- Do not reduce REE learning to one literal connection or a single universal learning-onset site.
- Do not let any write-authority gate bypass ethical residue, provenance, or self/world tagging.
- Correct near-term extraction: **preserve learning-onset as a gated transition from observation to write-eligible cognifold deformation.**
