---
nav_exclude: true
---

# SD-037: Broadcast Override Regulator (orexin-analog)

**Claim ID:** SD-037 (parent), MECH-280 / MECH-281 / MECH-282 (children)
**Subject:** `broadcast.override_regulator`
**Status:** candidate, v3_pending
**Registered:** 2026-04-22
**Origin:** Lit-pull synthesis (homeostatic override under sustained threat),
2026-04-22, motivated by V3-EXQ-471 catatonic lock-in. Source:
[targeted_review_homeostatic_override/SYNTHESIS.md](../../evidence/literature/targeted_review_homeostatic_override/SYNTHESIS.md).
**Depends on:** SD-036, SD-012, SD-032a, MECH-279

---

## Problem

SD-036 (GABAergic cross-stream decay) addresses one half of the V3-EXQ-471 catatonic
lock: in the absence of input, harm streams now relax toward baseline. But the lit-pull
on homeostatic override is convergent that **decay alone is not how biology breaks
harm-stream lock-in under sustained threat**. The biology uses a dedicated *override
authority* — a small, broadly-projecting gain modulator (canonically orexin/hypocretin)
that integrates internal homeostatic state and threat context and reweights downstream
arbitration without silencing the upstream signals.

The convergent picture across the lit-pull (SYNTHESIS.md §1, §4, §5):
- z_harm continues to be computed and broadcast even when override fires (Burnett 2016,
  de Araujo Salgado 2023). The mouse still perceives the predator; it just acts on hunger.
- The override is implemented downstream as **reweighting at commit gates**, not upstream
  as silencing of harm computation (Bjorness/Greene 2024; Marino 2020).
- The override is recruited specifically under high effort, sustained threat, or
  metabolic demand — it is not a continuous baseline modulator (James/Aston-Jones 2017).
- The bridge between drive_level and z_goal seeding (SD-012) is gated by this override
  authority. Without it, drive accumulates but does not gain authority to seed goal-mode
  behaviour under threat (Marino 2020 peri-LC; cataplexy in narcolepsy as the
  decoupling failure mode, Bassetti 2019).

The architectural commitment SD-037 makes is that **the V3 regulatory stack needs a
third layer**, parallel to and dissociable from:

- **5-HT layer** (MECH-186/187/188) — goal-pipeline gain, slow tonic modulation.
- **GABA layer** (SD-036) — cross-stream decay; tonic + phasic relaxation when input
  drops below threshold.
- **Orexin-analog layer** (SD-037, this doc) — broadcast override; reweights
  z_harm at downstream commit gates and gates SD-012 drive→z_goal seeding under
  metabolic-demand + threat conditions.

These three layers are mutually dissociable in failure: 5-HT depletion ≠ GABA decay
loss ≠ orexin loss, and clinical phenomenology bears this out (depression vs benzodiazepine
withdrawal vs narcolepsy/cataplexy).

---

## Mechanism

SD-037 introduces a scalar (or low-dimensional vector) **override_signal** computed
from drive_level (SD-012), sustained-threat context (rolling window of z_harm magnitude
above threshold), and a recruitment threshold. When override_signal exceeds its
recruitment threshold:

1. **Reweight z_harm at commit gates** — the weight of z_harm in commit-gate threshold
   computations (SD-032a SalienceCoordinator arbitration, MECH-279 PAG freeze-gate
   threshold) is scaled down. z_harm itself is *not* modified — the decay layer
   (SD-036) remains responsible for that — but its arbitration influence drops.

2. **Gate drive→z_goal seeding (the SD-012 bridge)** — when override_signal is below
   recruitment threshold, drive_level cannot seed z_goal even if benefit_exposure is
   non-zero. Above threshold, drive_level seeds z_goal directly. This is the
   architectural answer to the homeostatic-override question: drive does not have to
   compete with threat in arbitration; under override conditions it acquires authority.

3. **Threshold-like recruitment, not continuous** — the regulator is not a continuous
   baseline modulator. It accumulates evidence (drive accumulating, threat sustained)
   until a recruitment threshold crosses, then fires. This matches James/Aston-Jones
   2017 and the sigmoid-like behavioural switch in de Araujo Salgado 2023.

### Failure-mode predictions

The lit-pull surfaced two clean failure-mode signatures the regulator must reproduce:

- **Saturated override (PWS-analog)**: override_signal pinned high → compulsive drive
  pursuit despite negative outcomes, hyperphagic-equivalent (Brown 2022).
- **Lost override (narcolepsy/cataplexy-analog)**: override_signal absent → z_harm and
  drive_level both compute normally but fail to integrate into coordinated behaviour;
  emotional/drive input fails to recruit motor coupling (Bassetti 2019).

These failure modes are diagnostic for distinguishing SD-037 dysfunction from SD-036
(GABA decay) dysfunction or from MECH-186/187/188 (5-HT) dysfunction — they look
clinically different.

---

## Child mechanisms

### MECH-280: LH-PAG override projection

**Statement:** A direct projection from LH (orexin and/or peri-LC GABA analog) to PAG
modulates the GABAergic freeze-gate (MECH-279) under metabolic demand. The projection
does not silence the freeze gate; it raises its threshold (`theta_freeze` scales with
override_signal). This produces the behavioural transition from freeze to active
foraging under sustained hunger + threat.

**Substrate prediction:** MECH-279 `theta_freeze` and `exit_threshold` parameters
become functions of override_signal: `theta_freeze_effective = theta_freeze_base *
(1 + alpha_override * override_signal)`.

**Evidence anchors:** Marino 2020 (LH GABA → peri-LC for foraging engagement);
de Araujo Salgado 2023 (sustained hunger overrides predator avoidance); Wang/Lin 2015
(PAG as downstream arbiter of broadcast threat signals).

### MECH-281: Orexin gain modulation of drive-coupled arousal

**Statement:** An orexin-analog modulator gates the coupling between drive_level and
arousal-relevant downstream targets (PFC for SD-033a deliberation, BLA/CeA for SD-035
amygdala arbitration, beta-gate for MECH-090). Loss of this coupling produces a
cataplexy-analog failure: emotional/drive input fails to recruit motor activation.

**Substrate prediction:** override_signal scales the gain on drive→action-pipeline
projections (drive→z_goal weight, drive→beta_gate sensitivity). Lesion test: setting
override_signal to constant zero should produce decoupling between drive accumulation
and any motor/action consequence — drive computes, threat computes, but they fail to
integrate at action selection.

**Evidence anchors:** Bjorness/Greene 2024 (orexin as coupling signal); James/Aston-Jones
2017 (orexin recruitment under high effort/demand); Bassetti 2019 (narcolepsy as
coupling-loss clinical model).

### MECH-282: LPB interoceptive routing into harm-arbitration

**Statement:** A lateral-parabrachial-nucleus analog (LPB) routes interoceptive
distress signals (visceral malaise, taste-aversion analogs, hypoxia, hypoglycemia) into
the harm-arbitration network via PBN-CGRP → CeA → PAG. This is the upstream broadcast
arm of the threat-side architecture, parallel to VMHdm's predator-side broadcast. Both
feed downstream arbiters where SD-037's override_signal reweights them.

**Substrate prediction:** A separate input channel into the z_harm computation that
carries interoceptive/metabolic-distress signal, dissociable from external-threat
z_harm. Under SD-037 override conditions, the *interoceptive* harm-channel is *not*
suppressed (hunger-as-pain remains felt), but its weight in arbitration becomes the
input that drives the override_signal recruitment threshold from below.

**Evidence anchors:** Palmiter 2018 (PBN CGRP general alarm review); Pyeon 2025 (PBN
CGRP active defense modulation); Strigo/Craig 2016 (insular common-currency framing).

---

## Architecture context

SD-037 sits at the third regulator layer of the V3 control stack. Stream computation
happens in SD-010/SD-011/SD-012 (sensory and drive); decay happens in SD-036 (tonic
relaxation); arbitration happens in SD-032a (SalienceCoordinator) and at downstream
commit gates (MECH-279 freeze, beta-gate). SD-037 is the regulator that intervenes
*between stream computation and arbitration* — it does not modify the streams
themselves but modifies the weights with which they are read at commit gates and
gates the drive→goal bridge.

The relationship to SD-036 is critical and easy to confuse:

| | SD-036 (GABA decay) | SD-037 (orexin override) |
|---|---|---|
| Acts on | The streams themselves (z_harm_s, z_harm_a, z_beta) | The arbitration weights and the SD-012 bridge |
| Trigger | Absence of input below threshold | Drive accumulation + sustained threat above recruitment threshold |
| Effect on z_harm | Decays its magnitude | Leaves its magnitude untouched |
| Effect on commit gate | Indirect (smaller z_harm crosses threshold less) | Direct (changes the threshold itself) |
| Failure mode | Pinned streams; catatonic lock under input absence | Decoupled drive and arousal; no override under sustained threat with metabolic demand |
| Clinical analog | Catatonia subtype II / benzo deficiency | Narcolepsy/cataplexy + PWS hyperphagia |
| Recovery from V3-EXQ-471 lock | Removes the pinned z_harm | Even with z_harm=0, would let drive seed z_goal under metabolic demand |

**Both are required.** SD-036 unsticks the stream; SD-037 grants drive the authority
to drive behaviour once unstuck. EXQ-471 lock-in needs both to be unconditionally
broken. This is the headline finding of the lit-pull synthesis (§"Bottom line").

---

## What this SD enables

- **Resolution of V3-EXQ-471 at architectural depth** — not just unsticking the lock
  via decay, but providing the override authority that lets metabolic demand drive
  z_goal seeding under threat.
- **Bridge between SD-012 and the goal pipeline** — the missing piece that prevents
  drive_level alone from seeding z_goal in V3 (the EXQ-085 cluster's failure was
  partly this).
- **Diagnostic dissociation of three regulator-layer failures** — SD-036, SD-037, and
  MECH-186/187/188 each predict distinct clinical/behavioural failure phenotypes.
- **Foundation for compulsive-pursuit and decoupling failure modes** — PWS-analog
  hyperphagia and narcolepsy-analog decoupling become testable in V3.

---

## Validation experiment (deferred)

A full SD-037 validation experiment is not yet queued — implementation is gated by
EXQ-475 results (whether SD-036 decay alone produces partial recovery or no recovery
on the EXQ-471 lock). Once EXQ-475 results land, the SD-037 validation should be a
factorial:

- 4 arms: {SD-036 OFF, SD-037 OFF}, {SD-036 ON, SD-037 OFF}, {SD-036 OFF, SD-037 ON},
  {SD-036 ON, SD-037 ON}.
- Same conditions as EXQ-471.
- Predicted: arms 2 and 3 show partial recovery (each addresses one half); arm 4
  shows full recovery; arm 1 reproduces the EXQ-471 lock.

This dissociation experiment is the empirical test of the SYNTHESIS.md §"Bottom line"
prediction.

---

## Related claims

- **SD-036** — paired regulator (GABA decay); the stream-side complement to SD-037's
  arbitration-side intervention.
- **SD-012** — `homeostatic.drive_modulated_goal_seeding`; SD-037 is the gating
  authority for the SD-012 bridge.
- **SD-032a** — SalienceCoordinator; consumes override_signal as a weight modulator.
- **MECH-279** — PAG freeze-gate; consumes override_signal as a `theta_freeze` modulator
  (the MECH-280 projection).
- **MECH-186/187/188** — 5-HT regulatory layer; first regulator layer in the stack.
  SD-036 is the second; SD-037 is the third.
- **MECH-269** — hippocampal verisimilitude anchor selection; the override_signal
  recruitment threshold can plausibly be informed by V_s (anchored, high-V_s harm =
  *known* threat → over-ridable; novel low-V_s harm = take seriously, do not override).
  Cross-claim coupling deferred until EXQ-475 + SD-037 implementation.
