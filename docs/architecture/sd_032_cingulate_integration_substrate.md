---
nav_exclude: true
---

# SD-032: Cingulate Integration Substrate

**Claim ID:** SD-032 (parent) + SD-032a–e (subdivisions)
**Subject:** `cingulate.integration_substrate`
**Status:** candidate, v3_pending — SD-032b IMPLEMENTED 2026-04-19; SD-032a IMPLEMENTED 2026-04-19; SD-032c IMPLEMENTED 2026-04-19; parent cluster still pre-implementation.
**Registered:** 2026-04-19
**Depends on:** SD-011, SD-012, SD-020, SD-021, MECH-091, MECH-094, MECH-220
**Paired with:** SD-033 (PFC subdivision architecture) — together form the V3 cognitive-control backbone

---

## Problem

ree-v3 produces a z_harm_a stream (SD-011) but has no substrate that integrates it with cognitive control, urgency interrupt, effort credit assignment, or offline-mode coordination. EXQ-395 exposed this as a "z_harm_a consumer gap" and triaged it under the original MECH-220 cingulate-insula hub claim. Three other FAILs — EXQ-325a (SD-021 descending pain modulation), EXQ-355a (ARC-038 schema assimilation), EXQ-435 (INV-054 phase transition) — show the same surface pattern: a signal is computed correctly at the substrate level but does not produce coherent downstream behaviour because the coordinator for mode selection is absent.

The lit-pull (`targeted_review_cingulate_integration_substrate`, 9 entries) reframes the problem. The three candidate consumers of z_harm_a — (A) trajectory cost, (B) forward-rollout cost, (C) urgency interrupt — are not alternatives. They are different subdivisions' jobs, sequenced by a network-level salience-network coordinator. ree-v3 has fragments of each function but no substrate that binds them. MECH-220 was the right intuition ("there is a cingulate hub that integrates affective pain into action value") with the wrong architecture (a single module). The correct form is a network coordinator gating five functional subdivisions.

---

## Subdivisions

| ID | Subdivision | Biological analogue | ree-v3 function | Status in ree-v3 |
|---|---|---|---|---|
| SD-032a | Salience-network coordinator | AIC-dACC coupled salience network (Menon & Uddin 2010) | Reads all subdivisions; outputs `operating_mode` vector + mode-switch trigger | Absent |
| SD-032b | dACC / aMCC-analog (adaptive control) | dorsal ACC / anterior midcingulate (Shackman 2011; Baliki 2010) | Integrates z_harm_a PE + z_conflict + control demand; writes striatal-analog action-value target | Absent |
| SD-032c | AIC-analog (interoceptive salience / urgency) | Anterior insula (Craig 2009) | Detects salient interoceptive events; gates on SD-012 baseline; fires mode-switch trigger; subsumes SD-021 descending modulation | IMPLEMENTED 2026-04-19 |
| SD-032d | PCC-analog (attention partition / metastability) | Posterior cingulate (Leech & Sharp 2013) | Biases external-vs-internal attention; emits mode-stability scalar | Partial (INV-049, MECH-092 exist) |
| SD-032e | pACC-autonomic coupling | Perigenual / subgenual ACC (Vogt 2005; Craig 2009) | Writes z_harm_a into SD-012 valence / drive_level over slow timescale | Absent |

### SD-032a — Salience-network coordinator

Network-level module whose inputs are the five subdivisions' signals and whose outputs are (i) `operating_mode`: a soft probability vector over {external_task, internal_planning, internal_replay, offline_consolidation}, and (ii) `mode_switch_trigger`: a boolean that fires when any subdivision's precision-weighted salience exceeds the MECH-259 threshold. Mode transitions are discrete (atomic broadcast to all downstream gates); the threshold itself may be graded and learnable. The `operating_mode` vector is the primary input to MECH-261's write-gating family.

**Substrate signature:** an ablation of SD-032a (forcing `operating_mode` to a fixed external_task vector) should abolish coordinated mode switching without affecting the within-mode computations in SD-032b/c/d/e.

**Implementation (2026-04-19):** `ree_core/cingulate/salience_coordinator.py`
(`SalienceCoordinator`, `SalienceCoordinatorConfig`, `DEFAULT_MODE_NAMES`,
`DEFAULT_GATE_WEIGHTS`). Non-trainable arithmetic. Reads SD-032b dACC
bundle (`pe`, `foraging_value`, `choice_difficulty`), SD-012 `drive_level`,
and the agent offline-mode flag (proxy for SD-032d stability). Registered
input slots `aic_salience`, `pcc_stability`, `pacc_autonomic` are no-op
until SD-032c/d/e land -- callers extend via `update_signal(name, value)`.
Outputs (i) `operating_mode` soft probability vector over the four V3 modes
(softmax over per-mode affinity logits, default biased to external_task),
(ii) discrete `current_mode` updated only on threshold crossing
(hysteresis), (iii) MECH-259 `mode_switch_trigger` boolean fired when
salience aggregate exceeds `switch_threshold * (1 + stability_scaling *
pcc_stability)` AND the soft-vector argmax differs from the current mode.
Hosts MECH-261 dict-keyed write-gate registry (`{target: {mode: weight}}`)
populated from the spec table; `write_gate(target_name)` returns the
soft-weighted sum. `register_target(name, weights)` allows V4 substrates
(e.g. SD-033e parallel_goal_deliberation) to register their own gate
profile without coordinator schema changes -- mode_names is also a list,
not a fixed-arity tuple. Integrated into `ree_core/agent.py
REEAgent.select_action` immediately after the dACC bundle is built; ticks
on every action selection. Config flag `REEConfig.use_salience_coordinator`
(default False); knobs `salience_switch_threshold` (default 1.0),
`salience_stability_scaling` (1.0), `salience_softmax_temperature` (1.0),
`salience_external_task_bias` (1.0), `salience_dacc_pe_weight` (1.0),
`salience_dacc_foraging_weight` (0.5), `salience_apply_to_dacc_bias`
(False -- when True, scales the dACC score_bias by the e3_policy
write-gate so internal_replay attenuates dACC influence on action
selection). DACCtoE3Adapter is RETAINED as the score_bias source until
SD-033 substrates consume `operating_mode` natively (staged removal).
MECH-094: not authored here -- coordinator emits the gate that MECH-094
generalises to. Validation experiment: V3-EXQ-446 queued.

### SD-032b — dACC / aMCC-analog (adaptive control)

Minimum-viable substrate that resolves EXQ-395. Reads z_harm_a_PE (precision-weighted; MECH-258), z_conflict (top-vs-runner-up trajectory value margin from E3), and control_demand (expected value of control; Shenhav 2013). Outputs a behavioural-adjustment magnitude that is written to a striatal-analog action-value module with a learnable ACC→striatum weight (Baliki 2010 ACC-NAc coupling). Dopamine-analog credit assignment via SD-003 counterfactual attribution shapes that weight over time.

**MECH-260 (bias suppression)** is hosted here: an additional output channel producing a counter-bias against recently-executed trajectories. Candidate mechanistic explanation of the fishtank_viz monostrategy failure.

**Substrate signature:** precision-weighted PE → action-value shift with the expected scaling (large adjustment under high precision, small under low). Chronic-pain-like plasticity signature: sustained z_harm_a exposure shifts the ACC→striatum weight (Baliki 2012 finding).

**Implementation (2026-04-19):** `ree_core/cingulate/dacc.py`
(`DACCAdaptiveControl`, `DACCConfig`, `DACCtoE3Adapter`) + MECH-258
prerequisite `ree_core/predictors/e2_harm_a.py` (`E2HarmAForward`,
`E2HarmAConfig`). Integrated into `ree_core/agent.py
REEAgent.select_action`. Config flag `REEConfig.use_dacc` (default
False); sub-weights `dacc_weight`, `dacc_interaction_weight`,
`dacc_foraging_weight`, `dacc_suppression_weight`,
`dacc_suppression_memory` (default 8), `dacc_precision_scale` (default
500), `dacc_effort_cost` (default 0.1), `dacc_drive_coupling` (default
0).
Bundle output (Croxson 2009 × Shenhav 2013 × Kolling 2015 integration;
NOT a scalar): `{mode_ev[K], choice_difficulty, foraging_value,
harm_interaction[K], suppression[K], pe, drive_gain}`. The stopgap
`DACCtoE3Adapter` converts the bundle to `score_bias[K]` passed to
`E3.select()`; the adapter is explicitly marked for replacement when
SD-032a salience-network coordinator lands (coordinator is the
architectural consumer of the bundle per this doc's design).
MECH-258 E2_harm_a supports both an ARC-033-parallel independent path
and an ARC-058 shared-trunk path (constructor arg `shared_trunk`).
Phased training required for E2_harm_a (P0 encoder warmup → P1 frozen-
encoder forward-model training on `.detach()`ed targets → P2 eval).
Validation experiment: V3-EXQ-445 (3-arm ablation).

### SD-032c — AIC-analog (interoceptive salience / urgency)

Decides when the current operating mode is no longer sustainable. Inputs: z_harm_a, drive_level / fatigue / metabolic estimate (SD-012), plus other salient-event signals (unexpected z_goal drop, reward-prediction surprise, detected irreversibility). Computation: `salience = f(z_harm_a, interoceptive_baseline, ...)`. If `salience > threshold`, fires the mode-switch trigger into SD-032a.

**Subsumes SD-021.** The descending pain-modulation pathway (ACC / AIC → PAG) is an AIC function in biology: it attenuates z_harm_s gain as a function of current operating mode (attenuated during committed external_task, unattenuated during internal_planning). SD-021's EXQ-325a FAIL should resolve when SD-032c wires the modulation correctly.

**Substrate signature:** same z_harm_a produces different mode-switch behaviour in depleted vs well-resourced agents (interoceptive-baseline dependence). Failure: mode-switch rate is invariant to SD-012 state.

**Implementation (2026-04-19):** `ree_core/cingulate/aic_analog.py`
(`AICAnalog`, `AICConfig`). Non-trainable arithmetic over scalars.
Single EMA buffer for interoceptive baseline. Inputs per `sense()` tick:
`z_harm_a_norm` (scalar `||z_harm_a||_2` from SD-011), `drive_level`
(SD-012 GoalState), `beta_gate_elevated` (MECH-090), `operating_mode`
(SD-032a coordinator, previous tick; `None` treated as
`p_external_task=1.0` waking baseline so SD-032c remains functional
without coordinator), `extra_salient` dict (optional; unexpected
z_goal drop, reward-surprise, irreversibility; `aic_extra_weight=0`
default). Computation: EMA baseline <- alpha * z_harm_a_norm, urgency
= max(0, (z_harm_a_norm - baseline)/(baseline + eps)), `aic_salience =
urgency * (1 + drive_coupling * drive_level) + extra_weight * sum(extra)`,
`harm_s_gain = clip_[0,1](1 - base_attenuation * p_external *
float(beta_gate_elevated) * drive_protect)` where `drive_protect =
max(0, 1 - drive_protect_weight * drive_level)`. Outputs: `aic_salience`
fed to SalienceCoordinator via `update_signal("aic_salience", ...)` in
`select_action()` BEFORE `coordinator.tick()`; `harm_s_gain` applied
as multiplier on `z_harm` in `sense()` replacing the legacy SD-021
raw-beta-gate check when `use_aic_analog=True`; `urgency_signal` bool
(diagnostic). Config flag `REEConfig.use_aic_analog` (default False);
sub-knobs `aic_baseline_alpha` (0.02, ~50-step window),
`aic_drive_coupling` (1.0; MUST be non-zero for falsification signature),
`aic_urgency_threshold` (1.0, diagnostic), `aic_base_attenuation` (0.5,
matches legacy `descending_attenuation_factor`), `aic_drive_protect_weight`
(1.0; alterable-configuration knob flagged by SD-032c spec -- +1 preserve
depleted-agent signal, 0 drive-independent, -1 opposite-sign hypothesis),
`aic_extra_weight` (0.0, reserved). One-step lag on operating_mode read
is biologically plausible (AIC->dACC->SAL circuit delay). Falsification
signature: BOTH `aic_salience` AND `harm_s_gain` depend structurally on
`drive_level` -- only V3 substrate that makes the dependence structural.
EXQ-325a FAIL (DESCENDING == CONTROL bit-identical under raw beta_gate
check) resolves because the descending branch is now a genuinely
different function of state. MECH-094: not applicable (waking stream).
Subsumes SD-021: legacy raw-beta-gate code path retained behind
`harm_descending_mod_enabled` when `use_aic_analog=False`. Validation
experiment: V3-EXQ-325b queued (supersedes V3-EXQ-325a).

### SD-032d — PCC-analog (attention partition / metastability)

Conservative computational spec (Leech & Sharp 2013 is a proposal, not consensus): a scalar stability parameter in [0, 1] that modulates MECH-259's switch threshold in SD-032a. High stability → coordinator resists mode transitions; low stability → transitions happen at lower salience. Stability is itself a function of recent task success, fatigue, and time-since-last-offline-phase.

Coordinates within-session offline phases (MECH-092 micro-quiescence replay) and cross-session offline phases (INV-049 sleep). Does **not** trigger mode switches directly — that is SD-032c's job.

**Substrate signature:** ablating SD-032d makes the mode-switch threshold insensitive to fatigue / time-since-offline; agent over-commits to external_task without rest-driven relaxation of the threshold.

### SD-032e — pACC-autonomic coupling

Slow write-back channel from z_harm_a into SD-012 (drive_level, valence). In biology, perigenual / subgenual ACC drives autonomic and endocrine responses to pain; in ree-v3 this is what lets sustained affective pain shift the interoceptive baseline over longer timescales than a single action cycle.

**Substrate signature:** sustained z_harm_a exposure produces drift in drive_level, which in turn modulates SD-032c's switch threshold. Behavioural signature: chronic-pain-like sensitization (Baliki 2012). Without SD-032e, z_harm_a has no path into long-timescale state.

---

## MECH-261 write-gating profile

The `operating_mode` vector from SD-032a gates writes into the SD-033 PFC subdivisions (and the hippocampal viability map, cortical-sensory buffer, autonomic pathway). Gates are soft — each substrate reads a weighted sum over the mode vector, not a one-hot switch (Carr/Jadhav/Frank 2011 awake-SWR subpopulations; Tambini & Davachi 2019 cross-state persistence).

| Target | external_task | internal_planning | internal_replay | offline_consolidation |
|---|---|---|---|---|
| SD-033a (lateral-PFC rule/goal) | write | write | **suppressed** (protect held rule) | consolidative |
| SD-033b (OFC state-space) | read | speculative write | suppressed | consolidative (slow) |
| SD-033c (vmPFC value) | write | read | reduced-gain write | consolidative |
| SD-033d (premotor/SMA sequence) | write (tagged, MECH-094) | write (tagged) | suppressed unless tag set | consolidated |
| HC viability map (ARC-038) | write | read | write | consolidative |
| Cortical-sensory buffer | read | read | write | write |
| SD-032e autonomic coupling | active | attenuated | attenuated | attenuated |
| E3 policy update | full | gated | near-zero (must propagate via SD-033a) | gated |

"Suppressed" means near-zero gate weight; "consolidative" means a slow, low-rate write consistent with systems consolidation (Frankland & Bontempi 2005). The soft-boundary property matters: replay events tagged with partial external_task weight will still produce some write to SD-033a — which is what Peyrache 2009 SWR-coupled rule-learning replay actually does.

---

## Information flow

```
  sensory               SD-032c (AIC)  ----salience + baseline---\
    |                         |                                    \
  z_harm_s -> SD-011         ----drive_level <--- SD-012          \
    |          |                                                   v
  z_harm_a ---+-> E2_harm_a(PE) ---+                           SD-032a
                                    |                     (salience-network
                                    v                       coordinator)
  E3 (z_conflict, control_demand)-> SD-032b (dACC) --> striatal action-value
                                    |  ^                          |
                                    |  |MECH-260 bias-suppression |
                                    |                             |
  PCC stability scalar ---------> SD-032d --- mode-stability ---> |
                                                                  |
  z_harm_a ----slow write----> SD-032e -----> SD-012 drive/valence
                                                                  |
                                                                  v
                                                        operating_mode vector
                                                         + mode_switch_trigger
                                                                  |
                                                                  v
                                                     MECH-261 write-gating family
                                                                  |
                            +-----+-----+-----+-----+-----+-------+
                            v     v     v     v     v     v
                         SD-033a ... SD-033e   HC-map  sensory buf.  autonomic
                         (PFC subdivisions)    (ARC-038)              (SD-032e)
```

The core asymmetry: SD-032c is the **switch trigger** source (urgency detection); SD-032b is the **within-mode** adaptive-control output (graded policy shift); SD-032a is the **arbiter** that decides which of the two applies on any given cycle. Below the MECH-259 threshold, salience modulates behaviour smoothly through SD-032b. Above threshold, SD-032c fires, SD-032a broadcasts a new mode, and downstream gates reconfigure atomically.

---

## Minimum-viable V3 implementation path

Ordered. Do not skip ahead.

1. **SD-020 / MECH-258: pain forward model (E2_harm_a).** Build as a shared-substrate sibling of E2_harm_s (ARC-033, MECH-256/257 pattern). Without this, z_harm_a is a raw magnitude, not a precision-weighted control signal. Prerequisite for everything downstream.
2. **SD-012: homeostatic drive baseline.** Already partially scoped. SD-032c needs drive_level / fatigue as input. Must exist before SD-032c.
3. **SD-032b: dACC-analog alone (minimum viable).** Resolves EXQ-395. Wire z_harm_a_PE → adaptive-control → striatal action-value. Includes MECH-260 bias-suppression output. Test behavioural signature before building the coordinator.
4. **SD-032c + SD-032a: AIC-analog + coordinator.** Adds urgency-interrupt / mode-switching. Implement MECH-259 threshold and the soft `operating_mode` vector. Folds SD-021 descending modulation into SD-032c.
5. **MECH-261: mode-conditioned write gating.** Generalises MECH-094. Implement as a dictionary keyed on mode names so V4 `deliberative_branching` can be added without disruptive schema changes (see SD-033e).
6. **SD-032d (PCC-analog stability scalar) and SD-032e (pACC-autonomic slow write).** Refinements. SD-032e is required for the chronic-pain-like sensitization signature but not for the core loop.

**Steps 1–3** are the minimum viable cingulate substrate. The full cluster is steps 1–6.

**Register-only (no V3 implementation required):** none in this cluster — every subdivision has a substrate-level job. This contrasts with SD-033 where SD-033c/d are registration-only.

---

## Falsification signatures

Substrate-level (not merely behavioural). Each signature is designed to distinguish "this subdivision is missing or misconfigured" from "something else downstream is broken."

**SD-032 parent cluster is over-specified** if: a ree-v3 implementation of SD-032b alone reproduces coordinated mode switching on salient events (z_harm_a spike → operating_mode flip → coordinated downstream gate change) without an explicit SD-032a coordinator. Falsifies the network-level framing; collapses the cluster to a single adaptive-control module.

**SD-032a is required** (coordinator is load-bearing) if: SD-032b alone fails to produce coherent mode switching — e.g., agent continues committed trajectory despite z_harm_a spike, or downstream gates fail to reconfigure atomically. Piecemeal subdivision wiring then cannot substitute for the coordinator.

**SD-032b (dACC-analog) failure** if: precision-weighted PE is computed correctly but the ACC→striatum weight does not shift action selection toward harm-reducing trajectories, or sustained z_harm_a fails to produce Baliki-like plasticity (weight shift proportional to accumulated PE). Indicates the write target is wrong, not the PE computation.

**SD-032c (AIC-analog) failure** if: same z_harm_a triggers same behaviour in depleted vs well-resourced agents (i.e., mode-switch rate invariant to SD-012 drive_level). Indicates the interoceptive-baseline gating is broken — SD-032c is not reading SD-012 meaningfully.

**MECH-259 (switch threshold)** is over-specified if: purely graded / continuous coordinator (no discrete mode switches) reproduces coherent behaviour including both within-mode adjustment and urgency-interrupt dynamics. Redesign SD-032a as a graded-modulation layer.

**MECH-258 (precision weighting)** is over-specified if: non-precision-weighted (raw-magnitude) consumer of z_harm_a reproduces chronic-pain-like ACC-NAc coupling shift (Baliki 2010/2012). Indicates the biological context-dependence can be captured without explicit precision estimation.

**MECH-260 (bias suppression)** is falsified if: SD-032b without MECH-260 resolves the fishtank_viz monostrategy pattern; or if SD-032b + MECH-260 still produces monostrategy (indicating the fix is elsewhere, probably in exploration noise / entropy regularisation).

**SD-032e failure** signature: sustained z_harm_a exposure produces no drift in drive_level; agent cannot become chronically stressed. Indicates the slow write-back channel is disconnected from SD-012.

---

## Cross-cluster interaction with SD-033

SD-032 produces `operating_mode`. SD-033 holds the substrates `operating_mode` gates writes into. See `sd_033_pfc_subdivision_architecture.md` for the PFC-side design. The MECH-261 write-gating profile in the table above is the interface contract: SD-032a emits, SD-033 subdivisions consume.

Two concrete interaction signatures:

1. **Forward propagation bias** (MECH-261 primary falsification target). Content active in internal_replay should produce a measurable bias on subsequent external_task action selection, mediated by writes into SD-033a during replay (Tambini & Davachi 2019). If this bias persists when SD-032a is ablated (fixed external_task mode), forward propagation is coordinated locally rather than by the salience network — SD-032a's coordinator role is wrong.

2. **Rule protection during replay** (SD-033a + MECH-261 interaction). SD-033a rule representations should remain stable across internal_replay events even when replay content is rule-incompatible, because MECH-261 suppresses writes into SD-033a during replay. Failure signature: replay events overwrite the held rule → rule-selective persistence collapses → MECH-262 falsified at source.

---

## Related claims

- **SD-032, SD-032a–e** — this cluster
- **MECH-258** — precision-weighted z_harm_a PE driving SD-032b
- **MECH-259** — salience-network switch threshold
- **MECH-260** — dACC bias suppression against recency / monostrategy
- **MECH-261** — mode-conditioned write gating (generalises MECH-094)
- **SD-011** — dual nociceptive streams (prerequisite; produces z_harm_a)
- **SD-012** — homeostatic drive (interoceptive baseline for SD-032c)
- **SD-020** — harm_surprise_PE (upgraded to prerequisite via MECH-258)
- **SD-021** — descending pain modulation (folded into SD-032c)
- **SD-033** — PFC subdivision architecture (paired cluster; MECH-261 write targets)
- **MECH-091** — salient-event phase reset (specific AIC→dACC mechanism)
- **MECH-094** — hypothesis tag (special case of MECH-261)
- **MECH-220** — cingulate-insula harm hub (weakened; subsumed by SD-032 + SD-032a)
- **ARC-033, MECH-256/257** — E2_harm_s parallel architecture (E2_harm_a reuses substrate)
- **INV-049, MECH-092** — sleep / micro-quiescence (coordinated by SD-032d)

## References

Primary lit-pull: `evidence/literature/targeted_review_cingulate_integration_substrate/synthesis.md`
(9 entries, mean confidence ~0.80, 2026-04-19).

Supplementary: `evidence/literature/targeted_review_mcc_effort_value/synthesis.md` (MCC effort-value, bias suppression, Rushworth lab beyond Scholl/Kolling 2015, 2026-04-19).

Systems-consolidation grounding for MECH-261: `evidence/literature/targeted_review_systems_consolidation_waking_propagation/synthesis.md` (5 entries, aggregate literature_confidence 0.883, 2026-04-19).

Key entries:
- Menon & Uddin 2010 (*Brain Struct Funct*): salience network as AIC-dACC coordinator switching DMN ↔ CEN.
- Shackman et al 2011 (*Nat Rev Neurosci*): dACC/aMCC as common substrate for pain, negative affect, cognitive control (coordinate-based meta-analysis, 380+ studies).
- Craig 2009 (*Nat Rev Neurosci*): AIC as interoceptive-salience hub with autonomic and motor efferents.
- Baliki et al 2010 / 2012: ACC-NAc pathway for affective pain → action value; chronic-pain plasticity.
- Seymour 2019 (*Neuron*): pain as precision-weighted control signal (computational form for MECH-258).
- Vogt 2005 (*Nat Rev Neurosci*): cingulate subdivision anatomy (pACC, dACC, aMCC, pMCC, PCC).
- Leech & Sharp 2013: PCC "Arousal, Balance, Breadth" framing (conservative use only).
- Scholl, Kolling et al 2015 (*J Neurosci*): dACC + lateral aPFC bias-suppression against recency (MECH-260).
- Carr, Jadhav & Frank 2011; Tambini & Davachi 2019; Rothschild/Eban/Frank 2017; Peyrache et al 2009; Frankland & Bontempi 2005 (MECH-261 systems-consolidation grounding).
