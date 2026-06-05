# Targeted review — fatigue/effort-depletion vs suffering/learned-helplessness withdrawal

**Date:** 2026-06-05
**Question (from the ProtoFeelings P0 audit):** "fatigue / overload / stop-recover" was flagged as a candidate P0 control signal. Is it mechanistically DISTINCT from suffering-driven withdrawal (learned helplessness)? They converge behaviourally on *stop / disengage* but from opposite antecedents — "I'm depleted" (homeostatic) vs "this is hopeless/painful" (aversive-uncontrollable). Should a "fatigue/stop-recover" signal register on the **SD-012 homeostasis** side, NOT the **SD-011 suffering** side?

**Anchors in this directory (5 entries):**

| Entry | Pole | DOI | Direction |
|---|---|---|---|
| Maier & Watkins 2005 (Neurosci Biobehav Rev) | SUFFERING — uncontrollable aversion, DRN 5-HT / CRF, vmPFC controllability-gate | 10.1016/j.neubiorev.2005.03.021 | supports |
| Boksem & Tops 2008 (Brain Res Rev) | FATIGUE — cost/benefit recalibration, not depletion; ACC | 10.1016/j.brainresrev.2008.07.001 | supports |
| Meyniel et al. 2013 (PNAS) | FATIGUE — two-bound cost-evidence accumulator; posterior insula; *smallest computational form* | 10.1073/pnas.1211925110 | supports |
| Müller & Apps 2019 (Neuropsychologia) | FATIGUE — motivational signal; state-vs-trait scoping line | 10.1016/j.neuropsychologia.2018.04.030 | supports |
| Borbély et al. 2016 (J Sleep Res) | FATIGUE — Process S homeostatic accumulator; adenosine; offline reset | 10.1111/jsr.12371 | supports |

Corroborating anchor cited but not separately entried (already grounded under Q-034 / goal_disengagement): **Hashimoto et al. 2021, Brain Commun (10.1093/braincomms/fcab285)** — 5-HT firing attenuation in learned helplessness, reversed by ketamine; reinforces that the suffering pole's recovery is pharmacological/controllability-based, not rest-based.

---

## (a) Are they mechanistically distinct? — YES.

The two converge on the same behavioural output (stop/disengage) but separate cleanly on **four axes**:

| Axis | Suffering / learned helplessness (SD-011 side) | Fatigue / effort-depletion (SD-012 side) |
|---|---|---|
| **Antecedent** | Uncontrollable *aversive* stress; gated on a controllability appraisal (Maier & Watkins) | Cumulative *effort / time-on-task*; controllability-independent — accumulates from your own *successful* effort (Boksem & Tops, Meyniel, Borbély) |
| **Substrate** | Aversive neuromodulation: dorsal raphe 5-HT sensitisation + CRF; vmPFC gate | Interoceptive/proprioceptive cost-accumulator (posterior insula, ventromedial thalamus) + ACC effort-valuation; adenosine/SWA for the slow variant |
| **Valence/computation** | Escape-failure driven by an aversive signal | Value recalibration — down-weights the *value of continued effort*; reversible by incentive (a depletion/aversion account mispredicts this) |
| **Recovery dynamics** | Does **not** remit with rest; needs controllability experience or pharmacological reversal (Hashimoto) | **Recovers with rest/sleep** — the "recover" half is intrinsic (Meyniel dissipation slope Sr; Borbély Process S exponential decline in NREM) |

The recovery-dynamics axis is the single most decisive dissociator: fatigue is a *stop-AND-recover* signal with an offline reset; helplessness-withdrawal is a *stop* with no rest-recovery. Honouring **"biology before formal definitions"** (memory `feedback_biology_before_formal_definitions`): the biology does not treat tiredness as a kind of pain. Fatigue is an effort/energy-budget homeostatic accumulator with a distinct circuit and a recovery phase; the aversive "feeling bad about being tired" is a *secondary appraisal*, not the primitive. Modelling fatigue as a nociceptive/harm stream would import the wrong antecedent (aversion), the wrong gate (controllability), and the wrong dynamics (no recovery).

**Verdict (a): CONFIRMED distinct.** Fatigue/stop-recover is not a variant of suffering/SD-011. It belongs with hunger/drive on the homeostatic family.

---

## (b) Register a "fatigue/stop-recover" homeostatic control signal? — YES, on the SD-012 side, gated.

### Where it lives
- **SD-012 (homeostatic drive)** is the correct home: same family as `drive_level` (energy depletion already computable from `obs_body[3]`). Fatigue is a second homeostatic deficit variable alongside hunger.
- **SD-048 (interoceptive noise dynamics)** is the natural substrate host — its functional restatement already names "fatigue drift" as a component of the agent-independent interoceptive background. The new signal would *read from* the SD-048 interoceptive channel and *write to* arbitration.
- It is the affect-register realisation of the ProtoFeelings P0 gap "fatigue / overload / stop-recover," and the upstream fix for the DEV-NEED-002 conflation ("harm, hunger, fatigue, and survival pressure blur together") — the cure is keeping the *signals* separate even though they share a downstream consumer.
- **NOT SD-011.** Do not wire it as a z_harm stream.

### Smallest computational form (from Meyniel 2013)
A single scalar leaky accumulator with two bounds (hysteretic):

```
F += Se * effort_per_step      # accumulate during exertion
F -= Sr                        # dissipate during rest / low-effort
if F >= F_upper:  emit STOP / disengage      # upper bound
recover until F <= F_lower before re-engage  # lower bound (hysteresis)
```

- `Se`, `Sr`, and the bound gap can be modulated by SD-012 `drive_level` and incentive-token strength (Meyniel: difficulty steepens Se; incentive slows Se, speeds Sr, widens the gap → "work closer to exhaustion").
- **Two bounds, not one threshold** — the lower bound is the "recover" half; a single-threshold flag would lose recovery and chatter.
- **Two time-constants, not one variable:** a fast within-task accumulator (Meyniel) and a slow sleep-pressure accumulator (Borbély Process S). The slow one's recover phase is *offline* (SD-017 sleep), not task-switching.

### Shared MECH-342 decommit consumer? — YES for the in-task stop; NO for the recover half.
- MECH-342 (commit-maintenance release) is already a *graded, bounded-accumulation, drift-to-a-release-bound*, targeted to the active committed program, hysteretic with a reengagement path. That is structurally the *same shape* as the fatigue accumulator's stop bound.
- **Recommendation:** fatigue feeds MECH-342 as a **new deficit input** to the release accumulator, alongside the existing R-c degraded-execution-readiness deficit. The **SIGNAL is distinct** (homeostatic effort-expenditure vs execution-readiness deficit); the **release actuator is shared** (the in-task disengage from the current committed program). Fatigue also feeds the **ARC-078 goal-disengagement consumer** via a cost/benefit (not aversive) channel — the same consumer helplessness uses, reached from the opposite antecedent (Boksem & Tops; Müller & Apps).
- The **recover / re-accumulation half is NOT in MECH-342** (it has a reengagement path but no homeostatic recovery integrator). That belongs on the SD-012 / SD-017 side.

### V3-vs-V4 scope
- **V3-minimal (but gated):** the transient **state-fatigue** accumulator (Meyniel form) feeding (i) MECH-342 as a deficit term for in-task disengage and (ii) SD-017 sleep timing for the offline recover. This is the recoverable, value-modulating "state fatigue" of Müller & Apps. Recommend gating it **behind the in-flight cue-authority / z_goal work** (don't build before 638b/640a route) — consistent with the containment-only ethos; over-persistence prevention is real but not the current critical path.
- **V4-completeness:** multidimensional fatigue (physical/mental/motivational split, MFI-20), and **trait/chronic** fatigue shading toward anhedonia/depression (Müller & Apps state-vs-trait). The trait end is where fatigue and mood disorder become continuous — but that continuity is *not* a reason to model the V3 primitive as aversive; it is the boundary at which to stop, for now.

### What NOT to do
- Do **not** register fatigue as an SD-011 / z_harm nociceptive stream.
- Do **not** model it as energy depletion only (an empty tank) — it is a cost/value signal, incentive-sensitive, with a recover phase.
- Do **not** collapse the within-task and sleep-pressure accumulators into one variable.
- Do **not** build it before the in-flight cue-authority/z_goal experiments route (containment).
- This is a **lit-pull recommendation only** — no claims.yaml or affect_primitives.md edits in this pass. Registration (a candidate MECH on the SD-012 side + an affect_primitives.md row + the MECH-342 deficit-input wiring) is a follow-up governance decision.

---

## One-line verdict
Fatigue/effort-depletion and suffering/learned-helplessness are **mechanistically distinct** (opposite antecedents, different substrate, and — decisively — fatigue recovers with rest while helplessness does not). Register **fatigue/stop-recover on the SD-012 homeostatic side** (substrate-hosted by SD-048), smallest form = a **two-bound leaky cost-evidence accumulator** (Meyniel), **sharing the MECH-342 release actuator** for the in-task disengage but with its own homeostatic recover integrator on the SD-012/SD-017 side; **V3-minimal-but-gated**, with multidimensional/trait fatigue deferred to V4. Do **not** put it on SD-011.
