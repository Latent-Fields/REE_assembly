# MECH-354 — Effort/fatigue stop-recover homeostatic accumulator: implementation design (GATED)

**Status:** design-ready, BUILD GATED. Design pass + gated experiment plan only.
**Claim:** MECH-354 (candidate, mechanism_hypothesis, `implementation_phase: v3`, `v3_pending: true`), registered 2026-06-05.
**Subject:** `affect.fatigue_stop_recover_homeostatic_accumulator`
**Author session:** design-mech354-fatigue-stop-recover-20260605T2022Z
**Date:** 2026-06-05

**Evidence basis:** `evidence/literature/targeted_review_fatigue_vs_helplessness_dissociation/VERDICT.md`
(Meyniel et al. 2013 two-bound cost-evidence accumulator = the smallest computational form; Boksem &
Tops 2008 cost/benefit recalibration; Borbély et al. 2016 Process-S; Müller & Apps 2019 state-vs-trait;
contrast Maier & Watkins 2005 learned-helplessness pole).
**Register row:** `docs/architecture/affect_primitives.md` Extension Register, "effort / fatigue (stop-recover)" subsection.

---

## 0. CONTAINMENT GATE (read first — this is design, not build)

The lit verdict gates the BUILD behind the in-flight cue-authority / z_goal work. **Do NOT implement
the accumulator module and do NOT queue the experiment until that work routes:**

- **V3-EXQ-640a** (cue-authority gain sweep; `cue_recall_gain` × incentive-token strength) must run and
  be reviewed. It is the measurement successor to V3-EXQ-640 and itself **gates V3-EXQ-638b**.
- **V3-EXQ-638b** must build and route off 640a.

**Why gate.** MECH-354's incentive-reversibility axis (acceptance criterion C2 below) reads the same
incentive-token / wanting-amplitude channel that 640a is currently characterising. Building the fatigue
accumulator before the cue-authority gain is known would (a) hard-code an incentive-modulation slope
(`Se`/`Sr`/bound-gap response to incentive) onto an un-calibrated wanting signal, and (b) add a second
new deficit input to the MECH-342 release actuator while the z_goal→action authority path it shares an
arbitration site with is still in flux. Over-persistence prevention is real but **not the current
critical path** — this is the containment-only ethos (see `feedback_ree_assembly_externalised_cognition`:
keep this off the V3 critical path).

**This document delivers:** (1) the full module + wiring design, ready to hand to `/implement-substrate`
the moment the gate clears; (2) the gated `/queue-experiment` plan with pre-registered acceptance. It
performs **no** `ree_core`, `claims.yaml`, or `experiment_queue.json` edit.

**Gate-clear trigger (one line for the future session):** when V3-EXQ-640a is reviewed AND V3-EXQ-638b
has routed, this design is build-ready — run `/implement-substrate` on Section 4, then `/queue-experiment`
on Section 6.

---

## 1. What MECH-354 is (and is decisively not)

Fatigue/effort-depletion and suffering/learned-helplessness **converge behaviourally on stop/disengage**
but separate on four axes (VERDICT §a). The single decisive dissociator is **recovery**: fatigue is a
*stop-AND-recover* signal with an offline reset; helplessness-withdrawal is a *stop* with no rest-recovery.

| Axis | Suffering / learned helplessness (SD-011 side) | **Fatigue / effort-depletion (MECH-354, SD-012 side)** |
|---|---|---|
| Antecedent | Uncontrollable *aversive* stress; controllability-gated | Cumulative *effort / time-on-task*; controllability-INDEPENDENT — accumulates from your own *successful* effort |
| Substrate | Aversive neuromod (DRN 5-HT + CRF); vmPFC gate | Interoceptive/effort cost-accumulator (posterior insula) + ACC effort-valuation; adenosine/SWA (slow variant) |
| Computation | Escape-failure driven by an aversive signal | **Value recalibration** — down-weights the value of continued effort; **incentive-reversible** |
| Recovery | Does NOT remit with rest; needs controllability/pharmacological reversal | **Recovers with rest/sleep** — intrinsic dissipation slope `Sr` (fast) / Process-S NREM decline (slow) |

**Biology-before-formal-definitions (memory `feedback_biology_before_formal_definitions`):** the biology
does not treat tiredness as a kind of pain. Modelling fatigue as a nociceptive/harm stream imports the
**wrong antecedent** (aversion), the **wrong gate** (controllability), and the **wrong dynamics** (no
recovery). MECH-354 belongs with hunger/drive on the SD-012 homeostatic family — a second deficit
variable alongside hunger — **not** on the SD-011 suffering pathway.

**Hard non-goals (the substrate must not collapse into any of these):**

- **NOT an SD-011 / z_harm nociceptive stream.** Fatigue's output must stay **off** the
  `harm_obs_a`/z_harm_a additive path. See §3.1 for the load-bearing SD-048 routing caveat.
- **NOT energy-depletion-only** (an empty tank). It is a cost/value signal, incentive-sensitive, with a
  recover phase. A pure `obs_body[3]` energy read is necessary substrate input but not the mechanism.
- **NOT one variable.** The within-task and sleep-pressure accumulators share the *form* but not the
  *time-constant*; they must be two state variables.
- **NOT the blocked_agency / control-failure stream (MECH-353).** That is capacity-RETAINED → assert;
  fatigue is capacity-budget → stop-and-recover. Different antecedent, different consumer polarity.

---

## 2. Smallest computational form (Meyniel 2013)

A single scalar **leaky cost-evidence accumulator with two bounds (hysteretic)**:

```
# per maintenance tick, while engaged on an effortful committed program:
F += Se * effort_per_step          # accumulate during exertion
F -= Sr                            # dissipate during rest / low-effort (leak toward F_lower)
F  = clip(F, 0, F_cap)

if not stopped and F >= F_upper:   emit STOP / disengage      # upper bound -> fire
if     stopped and F <= F_lower:   clear STOP, re-engage OK    # lower bound -> hysteresis release
```

- **Two bounds, not one threshold.** The lower bound is the "recover" half. A single-threshold flag
  loses recovery and chatters at the bound (the same hysteresis lesson MECH-342 already encodes for the
  decommit accumulator). `F_lower < F_upper`; the gap is the hysteresis band.
- **Incentive modulation.** `Se`, `Sr`, and the bound gap are modulated by SD-012 `drive_level` and
  incentive-token strength (the recall-time wanting amplitude / `incentive_drive_kappa_weight` that
  640a characterises): incentive **slows `Se`**, **speeds `Sr`**, and **widens the gap** → "work closer
  to exhaustion" (Meyniel: difficulty steepens `Se`; incentive does the reverse). Concretely:
  `Se_eff = Se0 * difficulty / (1 + k_inc * incentive)`; `Sr_eff = Sr0 * (1 + k_rec * incentive)`;
  `F_upper_eff = F_upper0 * (1 + k_gap * incentive)`. This is the falsifiable incentive-reversibility
  handle (acceptance C2). **The incentive coefficients (`k_inc`/`k_rec`/`k_gap`) are exactly what the
  gate protects** — they multiply the wanting signal 640a is still calibrating.

### Two time-constants, two state variables

| Variant | State | Time-constant | Recover phase | Consumer |
|---|---|---|---|---|
| **Fast within-task** (Meyniel) | `F_state` | task-length (tens of steps) | online: `-= Sr` during low-effort ticks | MECH-342 decommit deficit + ARC-078/079 cost channel |
| **Slow sleep-pressure** (Borbély Process-S) | `S_state` | episode/multi-episode | **OFFLINE only** (SD-017 sleep) — NREM exponential decline | SD-017 sleep-timing pressure term |

The slow variant's recover phase is **offline** — it does not dissipate by task-switching, only by a
sleep/offline phase. Collapsing the two into one variable is an explicit non-goal (§1).

---

## 3. Where it lives (substrate home + host)

### 3.1 SD-012 home, SD-048 host — and the load-bearing routing caveat

- **SD-012 (homeostatic drive)** is the home: same family as `drive_level` (computable from
  `obs_body[3]` energy; `goal.py` GoalConfig.drive_weight=2.0). Fatigue is a second homeostatic deficit
  variable alongside hunger. The recover/re-accumulation half lives here and on SD-017.
- **SD-048 (interoceptive noise dynamics)** is the natural substrate *host*: its restatement already
  names "fatigue drift" as a component of the agent-independent interoceptive background. MECH-354
  **reads from** the SD-048 interoceptive/effort channel and **writes to** arbitration.

> **CAVEAT (must not be skipped).** SD-048's existing "Source 3: Fatigue drift" models fatigue as a slow
> AR(1) drift that **adds to `harm_obs_a`** (z_harm_a) — i.e. it currently feeds the SD-011 harm stream
> as a *noise source the comparator must learn to filter*. **MECH-354 must NOT inherit that routing.**
> The SD-048 host supplies the *substrate channel* (a slow interoceptive background state variable);
> MECH-354's accumulator reads **effort-expenditure** (proprioceptive/effort cost, see §3.2), integrates
> `F` **separately**, and writes the STOP signal to MECH-342 / ARC-078 — **never** back onto the
> `harm_obs_a` additive path. Wiring `F` into z_harm_a would re-commit precisely the SD-010→SD-011
> conflation the verdict forbids. The SD-048 fatigue-drift→harm path stays as-is (it is a legitimate
> "is this body-noise or hazard?" comparator-training signal); MECH-354 is a *parallel, distinct reader*
> of the same body-state, with a distinct (non-aversive) output channel.

### 3.2 Effort signal (`effort_per_step`)

`effort_per_step` is the per-tick exertion cost, read from the substrate (NOT a new env field if
avoidable). Candidate sources, in order of preference:

1. **`energy_decay` per acting step + action-magnitude** — the env already decays `obs_body[3]` energy
   per step (`energy_decay=0.01`); effortful actions (move vs idle) are distinguishable. `effort_per_step
   = base_step_cost + move_cost * is_moving`. This keeps fatigue **controllability-independent**:
   it accrues from successful effort, not from harm.
2. **Committed-program activity** — while beta is elevated (an active committed motor program),
   `effort_per_step` is non-zero; during idle/rest ticks it drops to a rest floor so `F` leaks down.

The experiment (§6) instruments effort explicitly via a per-step effort accumulator in the harness so the
acceptance test does not depend on a particular env knob.

---

## 4. Wiring (the design hand-off for `/implement-substrate`)

Two halves with **different owners** — this split is the core of the design:

```
                          effort_per_step (SD-048 host read; §3.2)
                                  |
                                  v
        +----------------------------------------------+
        |  MECH-354 FastFatigueAccumulator (SD-012)     |   F += Se*effort ; F -= Sr ; hysteresis
        |  state: F_state ; bounds F_lower/F_upper      |
        +----------------------------------------------+
              | in-task STOP (bool + graded deficit_f)        | recover half (leak)  -> SD-012 (stays here)
              |                                                
   +----------+-----------------------------+
   |                                         |
   v                                         v
 MECH-342 release actuator             ARC-078 / ARC-079 goal-disengagement
 (NEW deficit input, alongside R-c)    (cost/benefit, NON-aversive channel)
 combined = max(deficit_d, deficit_n,  raise the COST side of the persistence
                deficit_f)             gate so the ungated disengage default fires

        +----------------------------------------------+
        |  MECH-354 SlowSleepPressure (Process-S)       |   S += Se_slow*effort ; recover OFFLINE only
        |  state: S_state ; recover gated on SD-017     |
        +----------------------------------------------+
              | sleep-timing pressure term -> SD-017 (offline recover)
```

### 4.1 In-task STOP → MECH-342 (shared actuator, distinct signal)

MECH-342 (`commit_maintenance_release.py`) is already a *graded, bounded-accumulation,
drift-to-a-release-bound, targeted, hysteretic-with-reengagement* regulator. Its tick computes:

```
deficit_d = clip((score_margin_floor - score_margin) / score_margin_floor, 0, 1)   # decisiveness axis
deficit_n = clip((nav_floor - nav_competence) / nav_floor, 0, 1)                    # motor-readiness axis
combined  = max(deficit_d, deficit_n)                                               # OR-composition
```

**MECH-354 adds a third OR-composed deficit term:**

```
deficit_f = clip((F_state - F_engage) / (F_upper - F_engage), 0, 1)   # fatigue axis (0 until F passes F_engage)
combined  = max(deficit_d, deficit_n, deficit_f)
```

- The **release ACTUATOR is shared** (the in-task disengage from the current committed program — same
  `beta_gate.release()` + committed-program reset). The **SIGNAL is distinct**: fatigue is a homeostatic
  effort-expenditure deficit, not an execution-readiness deficit. This is exactly the verdict's
  "shared MECH-342 consumer for the in-task stop — YES; for the recover half — NO".
- `deficit_f` is gated to **zero below `F_engage`** so OFF-default behaviour is bit-identical and fatigue
  only contributes pressure once it has genuinely accumulated. Like the existing axes, it is
  OR-composed: fatigue can drive release even when decisiveness and nav are healthy (the
  "I succeeded but I'm spent" case — the controllability-independent signature).
- MECH-094 gate preserved: `tick(simulation_mode=True)` is a no-op (a replay/DMN tick must not advance
  fatigue or abort a committed program — mirrors the existing MECH-342 / MECH-313 / MECH-320 pattern).

### 4.2 In-task STOP → ARC-078 / ARC-079 (cost/benefit, non-aversive)

ARC-079/MECH-340 resolved ARC-078's C3: **persistence is a gated operation; disengagement is the ungated
default.** MECH-354 feeds the **cost side** of that cost/benefit weighing — raising accumulated fatigue
raises the cost of continued pursuit, so the persistence gate **fails to fire** and the un-gated
disengage default takes over. This reaches the **same goal-disengagement consumer that helplessness
uses, from the opposite (non-aversive) antecedent** (Boksem & Tops; Müller & Apps). The channel is
**cost/benefit, NOT aversive** — fatigue does not write a harm/suffering signal into the disengagement
decision; it shifts a value term.

### 4.3 Recover / re-accumulation half → SD-012 / SD-017 (NOT MECH-342)

MECH-342 has a *reengagement path* (leak-toward-zero when readiness recovers) but **no homeostatic
recovery integrator**. The fatigue recover half is therefore **not** in MECH-342:

- **Fast variant:** `F_state -= Sr` during low-effort/rest ticks (online), owned by the MECH-354
  module on the SD-012 side. Re-engage permitted only after `F` falls below `F_lower` (hysteresis).
- **Slow variant:** `S_state` recovers **only** during an SD-017 offline/sleep phase (Process-S NREM
  decline). MECH-354 contributes `S_state` as a sleep-pressure term to SD-017 sleep timing; SD-017's
  offline phase is what dissipates it. This is the structural home of "fatigue recovers with sleep".

### 4.4 Config (all default no-op; bit-identical OFF)

Mirror the MECH-342 config pattern (`use_maintenance_release` + tunables, all default-OFF). Proposed
knobs on the fatigue module config (final names at implement time):

| Knob | Default (OFF) | Role |
|---|---|---|
| `use_fatigue_accumulator` | `False` | master gate; `deficit_f` inert when off |
| `fatigue_Se` / `fatigue_Sr` | tuned | accumulate / dissipate rates (fast) |
| `fatigue_F_lower` / `_F_upper` / `_F_engage` / `_F_cap` | tuned | hysteresis bounds + deficit-onset + clamp |
| `fatigue_incentive_k_inc` / `_k_rec` / `_k_gap` | `0.0` | **incentive-modulation slopes — the gated coefficients (§2); keep 0.0 until 640a calibrates the wanting signal** |
| `use_sleep_pressure` | `False` | slow Process-S variant gate |
| `sleep_pressure_Se_slow` / `_offline_decay` | tuned | slow accumulate + SD-017-gated offline recover |

OFF defaults must produce a byte-identical run (verify: `deficit_f == 0` every tick, `combined`
unchanged, no new term in any logged scalar).

---

## 5. Falsifiable predictions (claim-level)

An REE substrate with fatigue enabled should disengage from a long effortful task at a rate that:

1. **rises with time-on-task independent of harm/controllability** (the homeostatic, controllability-
   independent antecedent — accumulates from successful effort);
2. **is reduced by incentive** (incentive-reversibility — a pure-depletion / empty-tank account
   mispredicts this);
3. **RECOVERS after a rest/offline phase** — a signature absent from the suffering/helplessness withdraw
   pathway (which needs controllability experience, not rest).

---

## 6. GATED `/queue-experiment` plan

> **DO NOT QUEUE until V3-EXQ-640a is reviewed AND V3-EXQ-638b has routed (§0).** This section is the
> pre-registered plan to hand to `/queue-experiment` at gate-clear, not an authorisation to build now.

**Working title:** fatigue stop-recover dissociation (time-on-task disengage, incentive-reversible, with
rest-recovery).
**Substrate:** the long-effortful-task harness (a committed-program task with a tunable effort cost per
step; reuse the scaffolded committed-program family used by the MECH-342 / cue-authority experiments so
the release actuator and effort instrumentation already exist).
**`experiment_purpose`:** evidence (MECH-354). `claim_ids: ["MECH-354"]`.
**`run_id` ends `_v3`; `architecture_epoch: ree_hybrid_guardrails_v1`.**

### 6.1 Conditions (factorial, instrumented)

A 3-axis design isolating the three claim predictions, each against a matched control:

| Axis | Levels | Isolates |
|---|---|---|
| **Fatigue** | OFF / ON (`use_fatigue_accumulator`) | the mechanism vs baseline |
| **Time-on-task** | short vs long effortful run at FIXED harm and FIXED controllability | prediction 1 (controllability-independent disengage) |
| **Incentive** | low vs high incentive-token strength (the 640a wanting amplitude) | prediction 2 (incentive-reversibility) |
| **Rest phase** | no-rest vs rest/offline inserted mid-run | prediction 3 (recovery) |

Plus a **decisive cross-control against the SD-011 suffering pole**: a matched **harm/uncontrollability**
arm (raise z_harm_a / lower controllability to the level that produces equivalent baseline disengagement)
and confirm it does **NOT** recover after the rest phase, while the fatigue arm does. This is the
single most decisive dissociator (VERDICT §a) and the load-bearing acceptance term.

Seeds: ≥3 per cell. Phased (warmup → measure), arms split only at the measure phase.

### 6.2 Pre-registered acceptance (PASS)

PASS requires **all three** dissociators, on the fatigue-ON arm, vs the matched controls:

- **C1 — time-on-task disengage independent of harm/controllability:** disengage rate rises with
  time-on-task in the fatigue-ON / long arm while harm and controllability are held fixed; the
  harm/controllability held-fixed control does **not** show the time-on-task rise. (Establishes the
  controllability-independent antecedent.)
- **C2 — incentive-reversible:** high-incentive reduces the fatigue-driven disengage rate vs low-incentive
  (monotone in incentive-token strength), on the SAME time-on-task. A pure-depletion account predicts no
  incentive effect; observing the reduction falsifies depletion-only.
- **C3 — rest-recovery:** after the inserted rest/offline phase, the fatigue arm's disengage propensity
  **drops** (F recovers below `F_lower`, re-engagement resumes); the matched harm/helplessness arm's
  disengage propensity does **NOT** drop after the same rest. (The decisive fatigue-vs-suffering split.)

**PASS = C1 AND C2 AND C3.** Partial outcomes route per the grid below (a diagnostic interpretation grid
in the docstring + experiment.md, one row per plausible outcome → next action, per memory
`feedback_diagnostic_experiment_descriptions`).

### 6.3 Interpretation grid (docstring + experiment.md)

| Outcome | Reading | Next action |
|---|---|---|
| C1+C2+C3 all PASS | MECH-354 supported: dissociated, incentive-reversible, recovers | governance → raise MECH-354 exp_conf; keep on SD-012 side |
| C1+C3 but not C2 | stop-and-recover confirmed but not incentive-modulated | check incentive wiring (the gated `k_inc`/`k_rec`/`k_gap` slopes); fatigue is depletion-like, NOT the Boksem cost/benefit form — re-open incentive coupling |
| C1+C2 but not C3 | disengages + incentive-reversible but does NOT recover | **red flag** — looks like the SD-011 pole; audit that F is not routed into z_harm_a (§3.1 caveat); fix recover half on SD-012/SD-017 |
| C3 only | recovers but no clean time-on-task antecedent | effort signal (§3.2) too weak/noisy; strengthen effort instrumentation |
| none | fatigue inert at this scale | `pending_retest_after_substrate`; effort cost or bounds mis-tuned; failure-autopsy |

### 6.4 Honest scope

This tests the **transient state-fatigue** (fast Meyniel) variant feeding MECH-342 + ARC-078, with the
rest-recovery half. The **slow Process-S / SD-017 offline** variant (§2, §4.3) and **multidimensional /
trait** fatigue (MFI-20 physical/mental/motivational split; Müller & Apps trait end) are **V4-completeness**
and are explicitly out of scope for this V3-minimal probe.

---

## 7. V3-vs-V4 scope boundary

- **V3-minimal (this design, gated):** fast state-fatigue accumulator → (i) MECH-342 deficit term for
  in-task disengage, (ii) ARC-078/079 cost channel, (iii) SD-017 sleep-timing pressure for the offline
  recover. Recoverable, value-modulating "state fatigue" (Müller & Apps).
- **V4-completeness (deferred):** multidimensional fatigue (physical/mental/motivational, MFI-20), and
  **trait/chronic** fatigue shading toward anhedonia/depression — the boundary at which fatigue and mood
  disorder become continuous. That continuity is **not** a reason to model the V3 primitive as aversive;
  it is the boundary at which to stop, for now.

---

## 8. Cross-references

- Claim: `docs/claims/claims.yaml` MECH-354 (depends_on SD-012, SD-048, MECH-342, ARC-078, SD-017;
  differentiated-from SD-011).
- Register: `docs/architecture/affect_primitives.md` Extension Register, effort/fatigue subsection.
- Evidence: `evidence/literature/targeted_review_fatigue_vs_helplessness_dissociation/VERDICT.md`.
- Shared actuator: `ree-v3/ree_core/policy/commit_maintenance_release.py` (MECH-342);
  `docs/architecture/mech_342_commit_maintenance_release.md`.
- Disengagement consumer: ARC-078 / ARC-079 / MECH-340 (`docs/architecture/ghost_goal_search.md`).
- Host substrate: `docs/architecture/sd_048_interoceptive_noise_dynamics.md` ("Source 3: Fatigue drift" —
  the routing caveat §3.1).
- SD-012 home: `goal.py` GoalConfig.drive_weight; SD-017 sleep (offline recover).
- Sibling stream (do not conflate): MECH-353 blocked_agency (capacity-retained → assert).
- **Build gate:** V3-EXQ-640a (cue-authority gain sweep) → V3-EXQ-638b. Build-ready only after both route.
