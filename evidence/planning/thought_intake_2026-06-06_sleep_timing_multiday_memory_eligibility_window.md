# Thought Intake (Stage 2): Multiday memory timing and plasticity eligibility windows

Raw thought file: [docs/thoughts/2026-06-06_sleep_timing_multiday_memory_eligibility_window.md](../../docs/thoughts/2026-06-06_sleep_timing_multiday_memory_eligibility_window.md)

**Intake date:** 2026-06-09
**Status:** processed; NO claims.yaml registration this pass (compass only)
**Classification:** offline-integration / plasticity-window design compass; off the V3 / GAP-7 critical path unless later linked to existing sleep / offline claims.

---

## 0. Source verification

The raw note flagged the primary article as "DOI/title identified but primary article not directly opened." **Resolved this pass -- primary source located and verified:**

- **Liu, Rong-Yu; Zhang, Yili; Calvo, Roberta; Smolen, Paul; Byrne, John H.** "The Right Time for a Synapse to Change: Windows and Mechanisms of Multiday Training Trials." *Journal of Neuroscience*, **April 29, 2026, 46(17):e1981252026**. DOI: **10.1523/JNEUROSCI.1981-25.2026**.
  - Publisher page: https://www.jneurosci.org/content/46/17/e1981252026
  - Author copy (UTHealth digital commons): https://digitalcommons.library.tmc.edu/uthmed_docs/3735/
- Secondary article (the one the saved REE email pointed at): Neuroscience News, "Perfect Timing for Memory Identified," https://neurosciencenews.com/24-hour-learning-interval-memory-30420/

**Verified findings (from the abstract + significance statement):**

- A second training block delivered **24 h** after an initial stimulus block significantly enhanced **LTF** (long-term synaptic facilitation) and **LTEE** (long-term enhancement of neuronal excitability); the same block at **18 h or 32 h** was **without effect**. The 24 h window is described as "fortuitous" -- 18/32 h "significantly less effective."
- Proposed mechanism: a **molecular "hour-glass-like" timer** driven by competition between the transcription **activator CREB1** and **repressor CREB2** (tracked via phosphorylated-CREB1/CREB2 immunofluorescence at 18/24/32 h; p38-MAPK pharmacological inhibition tested a mechanistic prediction).
- The timer is **intrinsic to individual neurons**: isolated *Aplysia* sensory neurons displayed the same ~24 h window for LTEE.
- **Methodology = empirical + computational.** Computational modeling predicted an effective window of ~20-30 h; electrophysiology + immunofluorescence + pharmacology tested it.

Caveat the raw note already raised and which the verified source confirms must be honoured: this is an *Aplysia* sensorimotor-synapse preparation. The 24 h figure is a property of that molecular system, not a universal learning schedule. The transferable abstraction is the *existence of a temporally-gated eligibility window*, not the number.

---

## 1. Verbatim thought (raw capture)

> **THOUGHT INTAKE: Multiday memory timing and plasticity eligibility windows**
>
> **0. Summary claim**
>
> A saved REE email pointed to a Neuroscience News article titled "Perfect Timing for Memory Identified". The article reports a Journal of Neuroscience paper in which Aplysia sensorimotor neurons showed a critical time window for a second learning-related stimulus block. A second exposure at 24 hours enhanced long-term synaptic facilitation and long-term enhancement of neuronal excitability, while 18-hour and 32-hour intervals did not produce the same effect.
>
> The important REE-relevant point is not the popular instruction to review material at the same time the next day. The useful architectural idea is narrower:
>
> > plasticity may depend on temporally gated eligibility windows, not merely on repetition or total exposure.
>
> For REE, this suggests that offline integration, replay, residue contextualisation, and memory consolidation may require explicit timing / eligibility gates rather than treating every replay or repeated exposure as equally write-capable.
>
> **1. Why this belongs in REE_assembly**
>
> This belongs in `REE_assembly` as a mechanism/open-question intake because REE already treats offline integration as a sleep analogue that consolidates and contextualises accumulated experience without bypassing waking action authority.
>
> The possible relevance is to future design of:
> - offline integration scheduling
> - replay eligibility
> - residue contextualisation windows
> - multiday consolidation
> - when repeated exposure should strengthen, weaken, or leave unchanged a latent trace
> - how intrinsic molecular/cellular timer analogues might be represented computationally
>
> This should not create a direct REE-v3 implementation task unless it later connects cleanly to existing offline-integration or plasticity-window claims.
>
> **2. Proposed classification**
>
> Likely classifications:
> - **mechanism hypothesis:** repeated training/replay updates require temporally gated eligibility windows.
> - **open question:** should REE distinguish replay exposure from write-eligible replay exposure?
> - **architectural commitment candidate:** offline integration should include gateable timing state, not merely batch replay.
>
> This should not be promoted directly to an invariant.
>
> **3. Relation to existing REE architecture** (mapping table)
>
> | Biological finding / framing | REE analogue |
> |---|---|
> | 24-hour second stimulus window | scheduled replay / consolidation eligibility window |
> | 18h and 32h not sufficient in the reported preparation | timing-sensitive write gate, not simple exposure count |
> | CREB1/CREB2 competition dynamics | competing consolidation vs repression / inhibition signals |
> | intrinsic neuronal timer | local state-dependent eligibility timer inside a latent trace |
> | long-term synaptic facilitation | strengthened predictive/transition pathway |
> | long-term enhancement of neuronal excitability | lowered activation threshold / increased future readiness |
> | multiday training | repeated offline integration cycles |
>
> **4. REE-specific hypothesis**
>
> REE may need to distinguish at least three forms of replay/re-exposure:
> 1. **Observation replay** -- a trace is reactivated but does not write durable change.
> 2. **Integration replay** -- a trace is contextualised or compressed but does not alter commitment authority.
> 3. **Eligibility-window replay** -- the trace is reactivated within a timing/state window that permits durable change in future trajectory selection.
>
> This could matter especially for residue. A harmful committed event should generate residue immediately, but the later meaning, contextualisation, and future action-landscape deformation may need time-gated integration rather than unrestricted rewriting.
>
> Speculative computational primitive:
> ```text
> trace_eligibility = f(time_since_event, offline_phase, arousal_state, prediction_error, residue_status, sleep_cycle_state)
> ```
> Replay should be able to inspect a trace outside the window, but only write durable consolidation when eligibility is open.
>
> **5. Important cautions**
>
> Do not overgeneralise from Aplysia to human learning schedules. Do not encode a literal universal 24-hour rule into REE. Do not use this to justify simplistic productivity advice. Do not make this a REE-v3 implementation target without first checking existing sleep/offline/plasticity claims.
>
> The useful extraction is:
> > repeated exposure may only become durable learning when the receiving substrate is in a write-eligible temporal state.
>
> **6. External anchors** (secondary article + identified primary; primary still needs direct verification before claim extraction)
>
> **7. Proposed next extraction** -- if the primary source is verified, consider linking this to an offline-integration or plasticity-window architecture note rather than creating a new standalone subsystem immediately. Possible future note: `docs/architecture/offline_integration_eligibility_windows.md`.
>
> **8. Guardrail for future agents** -- correct near-term extraction: "model consolidation eligibility as state-and-time gated write authority." Incorrect: "add a fixed 24-hour learning interval rule to REE-v3."

(Full raw text in the linked file; section headers above are condensed for the intake.)

---

## 2. What's New vs. Existing REE Docs

| Idea in the thought | Already owned by REE? | Where | New contribution |
|---|---|---|---|
| Offline phases consolidate / re-organise accumulated experience without bypassing waking action authority | **Yes** | INV-049 (offline phases mathematically necessary for model-building agents); SD-017 (SWS-analog + REM-analog phases) | None -- this is the existing frame the thought sits inside |
| Cross-episode aggregation of attribution during sleep is what consolidation is *for* | **Yes** | MECH-275 (general Bayesian aggregation), MECH-273 (self-model sleep half), MECH-272 (state-gated routing) | None |
| Replay is *prioritised*, not uniform (salience / staleness weighting) | **Yes (priority), partial** | MECH-285 (staleness-priority replay ordering), MECH-205 (surprise-gated generative replay) | REE already weights *which* traces replay and *how often*. It does **not** gate *whether a replayed trace is write-eligible as a function of time-since-event*. |
| Write gating by mode / provenance | **Yes** | MECH-261 (mode-conditioned write gating over the {external, planning, replay, consolidation} mode vector); MECH-094 (simulation-vs-real hypothesis tag) | REE gates writes by **operating mode** and by **provenance**, but **not by an elapsed-time eligibility window** keyed to a specific trace's own history. |
| Distinct *forms* of replay: inspect-only vs integrate vs write-eligible | **Partial / adjacent** | learning-onset write-authority-gate intake (2026-06-06, `thought_intake_2026-06-06_learning_onset_single_connection_gate.md`); plasticity-window-neuromodulators note (2026-06-01) | The learning-onset intake proposes an **event-level write-eligible state** (observed -> flagged -> write-eligible -> consolidated). This thought adds the **temporal-window axis** to that state: eligibility is not just a discrete gate but a *time-since-last-event-dependent window* that can open and close. **This is the genuinely-new rung.** |
| Plasticity learning-rate gating by neuromodulatory state (ACh/PV/BDNF) | **Adjacent (parked)** | plasticity-window-neuromodulators note (2026-06-01); MEMORY `project_plasticity_window_neuromodulators` | That note is the **opening side** keyed to neuromodulatory *state*. This thought is keyed to **elapsed time between consolidation episodes** (an intrinsic per-trace timer). Same family, different control variable -- must be cross-referenced, **not conflated**. |
| Critical-period open/close (crystallization) | **Yes, but different grain** | INV-074 / MECH-333 (open) / MECH-334 (closure) | Those govern a **lifetime-scale** plasticity window over the whole scoring pathway. This thought is an **inter-episode-scale** window over an individual trace's consolidation. Different timescale, different unit. |
| Residue: immediate generation vs time-gated *contextualisation* | **Partial -- novel split** | MECH-205 (surprise-gated replay of residue); MECH-285 (PTSD-rumination = priority loss + tag-lock) | REE generates residue immediately and replays it by priority. The thought's split -- *residue generation is immediate but residue re-meaning / action-landscape deformation is time-gated* -- is **not currently a registered distinction**. Potentially clinically interesting (consolidation-window account of why intervention timing matters in trauma). |
| Intrinsic per-trace molecular timer (CREB1/CREB2 hour-glass) | **No** | -- | An **intrinsic, trace-local eligibility timer** (vs REE's current global / mode-level / staleness-map signals) has no REE analogue. This is the substrate-shape question the thought raises. |

**One-line novelty verdict:** REE already owns the *frame* (INV-049/SD-017), the *cross-episode aggregation* (MECH-273/275), the *priority weighting* (MECH-205/285), and the *mode/provenance write gates* (MECH-261/094). The genuinely-new contribution is a **time-since-event eligibility-window axis on the write gate** -- replay can *inspect* a trace any time, but *durable consolidation writes* are licensed only inside a trace-local temporal window. This sharpens the just-seeded learning-onset write-eligible-state idea by adding the temporal dimension, and it cross-references but does not duplicate the 2026-06-01 plasticity-window-neuromodulators (state-keyed) note.

---

## 3. Key formulations

1. **Write-eligibility is time-gated, not exposure-counted.** "Repeated exposure may only become durable learning when the receiving substrate is in a write-eligible temporal state." Repetition / total exposure is necessary but not sufficient; a temporal eligibility gate sits between exposure and durable change.

2. **Inspect-anytime / write-in-window separation.** Replay should be able to *read* a trace outside the eligibility window (for planning, simulation, retrieval) but only *commit durable consolidation* when the window is open. This is the replay-occurrence vs replay-write-authority distinction, with an explicit temporal control variable.

3. **Three-tier replay taxonomy** (from the thought): observation replay (reactivate, no write) / integration replay (contextualise/compress, no commitment-authority change) / eligibility-window replay (durable change to future trajectory selection). Maps loosely onto REE's existing {internal_replay, offline_consolidation} mode split (MECH-261) but adds a finer gradation inside consolidation.

4. **Residue generation vs residue re-meaning split.** Harm-committed events generate residue immediately (preserve the existing immediate-residue commitment); but later contextualisation, meaning-revision, and action-landscape deformation are time-gated integration steps, not unrestricted rewriting available at all times.

5. **Speculative primitive (do not implement):**
   ```text
   trace_eligibility = f(time_since_event, offline_phase, arousal_state,
                         prediction_error, residue_status, sleep_cycle_state)
   ```
   Note this composes signals REE *already has separately* -- offline_phase (SD-017/MECH-261 mode vector), prediction_error (MECH-205), residue_status (residue system), sleep_cycle_state (SleepLoopManager) -- plus the **one missing input: `time_since_event` as a first-class per-trace eligibility variable.**

---

## 4. Affected existing claims (real ids, verified against claims.yaml + sleep_substrate_plan.md)

These are *related* claims the thought touches. **No edits are made to any of them this pass** -- listed for cross-reference and to scope where a future candidate would attach.

| Claim / artefact | Relation | Note |
|---|---|---|
| **INV-049** (offline phases mathematically necessary for model-building agents) | Parent frame | The thought refines *what* the offline phase gates, not *whether* it is needed. Any future candidate is downstream of INV-049, not a competitor. |
| **SD-017** (SWS-analog + REM-analog sleep infrastructure) | Host substrate | An eligibility-window gate would live *inside* the SWS/REM consolidation passes. Per `sleep_substrate_plan.md`, SD-017's retest cohort (GAP-2) is **upstream-blocked** on the ARC-065 rule-creator substrate; this compass adds no pressure to that gate. |
| **MECH-204** (serotonergic REM-gate zero-point / precision recalibration) | Sibling consolidation step | GAP-1 = **done** (F1 cumulative zero-point reference; V3-EXQ-541c PASS). MECH-204 already implements a *cross-cycle* recalibration timer of sorts; an eligibility-window gate would be a distinct, trace-local timer, not a recalibration of precision. |
| **MECH-205** (surprise-gated generative replay) | Closest existing replay-eligibility lever | MECH-205 decides *which* traces replay (by unexplained PE). The thought's eligibility window decides *whether the replayed trace may write durably right now* -- orthogonal gate, would compose with MECH-205. |
| **MECH-285** (staleness-priority replay ordering; PTSD-rumination account) | Adjacent priority signal | MECH-285 already supplies `time`-adjacent prioritisation via the staleness map (MECH-284). A `time_since_event` eligibility window is a *different* temporal signal (per-trace elapsed time, not accumulated staleness). The thought's residue-re-meaning split could extend MECH-285's PTSD account (window-miss as a second failure mode alongside priority-loss + tag-lock). |
| **MECH-272 / MECH-273 / MECH-275** (sleep-aggregation cluster: routing / self-model half / general Bayesian aggregation) | Consumers of consolidation writes | These are *what* gets written during consolidation. An eligibility window would gate *when* their offline writes are licensed. Per `sleep_substrate_plan.md` all three are substrate-`done` (GAP-3/4/8) but empirical promotion is still pending. |
| **MECH-261** (mode-conditioned write gating over {external_task, internal_planning, internal_replay, offline_consolidation}) | Structural nearest neighbour | The existing gate is **mode-keyed**; the thought proposes a **time-keyed** gate. A future candidate most likely *amends/extends MECH-261's gate family* rather than registering a standalone subsystem. |
| **MECH-094** (simulation-vs-real hypothesis tag) | Provenance gate | Provenance-keyed write gate; complementary axis to the proposed time-keyed gate. |
| **INV-074 / MECH-333 / MECH-334** (critical-period open / closure crystallization) | Different-timescale plasticity windows | Lifetime-scale window over the scoring pathway -- explicitly **not** the same as the inter-episode trace-local window here. Cross-ref only; do not conflate. |
| **learning-onset write-authority-gate intake** (`thought_intake_2026-06-06_learning_onset_single_connection_gate.md`) | Sibling intake (same week) | Proposes an event-level *write-eligible state*. This thought adds the **temporal-window dimension** to that state. The two should be reconciled when either is registered -- likely a single write-authority-gate claim family with (a) a discrete eligibility state and (b) a temporal window control variable. |
| **plasticity-window-neuromodulators note** (`docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md`) | Sibling thought (opening side) | State-keyed (ACh/PV/BDNF learning-rate gain) plasticity *opening*. This thought is elapsed-time-keyed. Same opening-side family, different control variable -- cross-reference, **do not merge** (mirrors the explicit non-conflation the learning-onset intake recorded). |

---

## 5. Candidate claims FOR FUTURE REGISTRATION (NOT registered this pass)

Per the raw note's own guardrails (sections 1, 2, 8) and the V3-first roadmap, **nothing is registered into claims.yaml this pass.** These are sketches for a *later* registration decision, contingent on (a) the learning-onset write-authority-gate family being registered first (so this attaches as an amendment rather than a parallel subsystem) and (b) a substrate that could actually express a trace-local timer (V4-leaning).

- **CANDIDATE-A (mechanism_hypothesis, substrate_conditional, implementation_phase v4):** *Time-gated write-eligibility window.* Durable consolidation writes from replay are licensed only inside a trace-local temporal window `f(time_since_event, ...)`; replay may inspect a trace at any time but commits durable change only when the window is open. Would most likely **amend the MECH-261 write-gate family** (add a temporal eligibility input) rather than stand alone. depends_on: MECH-261, MECH-094, INV-049, MECH-205, MECH-285, SD-017 + the learning-onset write-eligible-state claim.

- **CANDIDATE-B (open_question, epistemic_category substrate_conditional):** *Should REE distinguish replay occurrence from write-eligible replay occurrence as a function of elapsed time?* Falsifier: if mode-conditioned (MECH-261) + provenance (MECH-094) + staleness-priority (MECH-285) gating is already sufficient to prevent over-writing / premature consolidation, no separate time-keyed eligibility window is needed. (Mark substrate_conditional so `narrow_open_question` does not fire on a V4-bound question.)

- **CANDIDATE-C (open_question / mechanism sketch, substrate_conditional):** *Residue generation vs residue re-meaning timing split.* Residue is generated immediately on harm-commit (unchanged), but contextualisation / meaning-revision / action-landscape deformation is time-gated. Could extend MECH-285's PTSD-rumination account with a window-miss failure mode. depends_on: residue system, MECH-205, MECH-285.

**Reconciliation note for whoever registers these:** the learning-onset intake (same week) seeds an event-level write-eligible *state*; this intake seeds the *temporal window* on that state. If both are registered they should form **one** write-authority-gate family with a state machine + a temporal control variable, not two competing subsystems. Decide the merge at registration time.

---

## 6. Next steps

1. **No experiment, no substrate, no claim registration now.** A V3 probe would be vacuous: there is no trace-local `time_since_event` eligibility variable in the substrate to ablate, and SD-017's retest cohort (the natural host) is itself upstream-blocked (GAP-2). Honour the raw note's section-8 guardrail.
2. **Defer to the write-authority-gate family.** When/if the learning-onset write-eligible-state candidate (`thought_intake_2026-06-06_learning_onset_single_connection_gate.md`) is registered, fold CANDIDATE-A/B in as the temporal-window dimension of that family. Do not register a parallel "offline_integration_eligibility_windows" subsystem (the raw note's section-7 proposal) unless that family proves insufficient.
3. **Cross-reference, do not conflate, with the 2026-06-01 plasticity-window-neuromodulators note** (state-keyed opening) and the INV-074/MECH-333/MECH-334 critical-period cluster (lifetime-scale window). Three distinct timescales/control-variables in the same plasticity-gating family.
4. **If a later session does build a write-authority-gate substrate,** the residue generation-vs-re-meaning split (CANDIDATE-C) is the most REE-distinctive and clinically suggestive piece -- worth a focused lit-pull (consolidation-window / reconsolidation-window literature; memory-reactivation timing; trauma-intervention-timing) before registering.
5. **Source is fully verified** (section 0) -- the "primary not opened" gap from the raw note is closed; no further verification needed.
