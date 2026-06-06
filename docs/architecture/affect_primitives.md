---
nav_exclude: true
---

# Affect Primitives

**Document type:** Architecture reference  
**Scope:** V3 harm-affect register (SD-019 cluster); benefit/wanting register deferred to V4  
**Last updated:** 2026-04-20  
**Related claims:** SD-011, SD-019, SD-019a, SD-019b, MECH-219, Q-036, SD-032 cluster  

---

## Motivation

The clinical and experimental pain literature draws a firm three-way dissociation among dimensions of the pain experience that are commonly collapsed into a single "harm signal":

| Dimension | What it measures | Controllability effect | Neural substrate |
|-----------|-----------------|----------------------|-----------------|
| **Intensity** | Sensory magnitude of noxious input | None | Lateral pathway: A-delta, S1/S2, VPL thalamus |
| **Unpleasantness** | Immediate affective valence — "how bothersome right now" | None (Loffler et al. 2018) | Medial pathway: C-fiber, ACC/insula, fast component |
| **Suffering** | Accumulated psychological burden | Selectively reduces suffering (Loffler et al. 2018) | Medial pathway: ACC/insula + salience network (slow, persistent) |

The Löffler et al. (2018, Pain Reports) three-way dissociation is the empirical anchor: identical
stimuli, identical unpleasantness ratings, but selectively reduced suffering under controllable
conditions. Controllability is definitionally orthogonal to intensity; that it also leaves
unpleasantness unchanged means suffering is a third, functionally separate construct requiring its
own computational account.

Salomons et al. (2004, JNeurosci) confirm the neural substrate: perceived controllability
modulates ACC/insula activation for identical stimuli — the suffering circuit, not the sensory
circuit.

De Ridder et al. (2021, Neurosci BioBehav Rev) map this anatomically: the medial pathway (ACC +
insula, overlapping with the salience network) is the substrate of suffering; "salience and
context" — not sensory magnitude — determine the medial pathway's output. This directly connects
suffering computation to the SD-032 salience-network coordinator cluster.

---

## The Harm Affect Register

REE V3 maintains three named harm affect primitives. Each has a computational definition, a
substrate, and a distinct set of downstream effects.

### Primitive 1: harm_intensity

| Field | Value |
|-------|-------|
| **REE signal** | `z_harm_s` (sensory-discriminative harm stream) |
| **Claim** | SD-011 (dual nociceptive streams) |
| **Character** | Instantaneous; tracks current hazard proximity / noxious contact magnitude |
| **Time constant** | Fast — rises and falls with the hazard state within a single step |
| **Controllability dependence** | None |
| **Biological analogue** | A-delta fiber (fast nociception), spinothalamic tract, S1/S2, VPL thalamus |

**Downstream effects:**
- SD-029: comparator input for agency attribution (`residual = z_harm_s_observed − E2_harm_s(z_harm_s_{t-1}, a_actual)`)
- E3 trajectory scoring: immediate penalty weight on trajectories that approach hazard zones
- SD-020: harm prediction-error weighting

---

### Primitive 2: harm_unpleasantness

| Field | Value |
|-------|-------|
| **REE signal** | `z_harm_un` (new; pre-integration affective valence channel) |
| **Claim** | SD-019a |
| **Character** | Immediate affective valence — the "I want this to stop now" signal |
| **Time constant** | Fast-to-medium; faster than suffering, slower than raw sensory intensity |
| **Controllability dependence** | None (Loffler et al. 2018 key finding) |
| **Biological analogue** | C-fiber input to ACC/insula (fast medial component); unpleasantness dimension of the McGill Pain Questionnaire |

**Downstream effects:**
- AIC urgency input (SD-032c): `z_harm_un` is the primary source of the urgency salience signal driving the salience-network coordinator
- E3 short-horizon trajectory scoring: negative valence weight distinct from `z_harm_s` (a trajectory ending harm NOW scores differently from one that reduces future harm probability)
- MECH-219 input: `z_harm_un` is what MECH-219 integrates over time to produce suffering (`z_harm_a`)

**Design note:** `z_harm_un` is not required to be nonredundant with `z_harm_s` at every instant — the two can be correlated under typical harm conditions. The nonredundancy constraint (SD-019) applies between `z_harm_s` and `z_harm_a` (suffering), not between `z_harm_s` and `z_harm_un`. However, `z_harm_un` must encode something beyond raw intensity — it is a medial-pathway signal that includes affective/motivational weighting — so complete collinearity with `z_harm_s` would be architecturally wrong.

---

### Primitive 3: harm_suffering

| Field | Value |
|-------|-------|
| **REE signal** | `z_harm_a` (affective harm stream; refined definition) |
| **Claim** | SD-019b (suffering accumulator); mechanism SD-019 / MECH-219 |
| **Character** | Slowly-accumulated load state; persistence depends on exposure duration and controllability |
| **Time constant** | Slow; asymmetric onset/recovery (MECH-219: rise faster than decay) |
| **Controllability dependence** | High — escapability belief gates the accumulator (Q-036) |
| **Biological analogue** | Chronic activation of medial pathway + salience network; overlap with stress system; learned helplessness substrate (DRN serotonin, vmPFC control circuit) |

**Downstream effects:**
- MECH-259 / SD-032a: primary input to the mode-switch threshold trigger; when suffering exceeds threshold (modulated by SD-032d PCC stability), the coordinator fires a whole-system operating_mode switch
- SD-032e pACC autonomic coupling: slow write-back to `drive_level` via long-horizon integration of `z_harm_a`
- ARC-016 urgency modulation: `z_harm_a` feeds commitment-threshold adjustment in E3
- Behavioral withdrawal / learned helplessness: when `z_harm_a` is sustained and controllability estimate is low, the agent should transition from approach/escape to mode-change or help-seeking — the suffering primitive is what grounds this transition biologically

---

## Computational Pipeline

```
SENSATION
  │
  ├─ z_harm_s (intensity)  ──►  E3 trajectory scoring (immediate avoidance)
  │         │                   SD-029 comparator (agency attribution)
  │         │                   SD-020 harm PE
  │         │
  │         ▼
  │   [medial pathway encoding]
  │         │
  ├─ z_harm_un (unpleasantness) ──►  AIC urgency signal (SD-032c)
  │         │                        E3 short-horizon scoring ("stop this NOW")
  │         │
  │         ▼
  │   [MECH-219: hysteretic integrator, controllability-gated]
  │         │
  └─ z_harm_a (suffering) ─────►  MECH-259 mode-switch trigger (SD-032a)
                                   SD-032e pACC → drive_level coupling
                                   ARC-016 commitment-threshold adjustment
                                   Behavioral withdrawal / mode-change
```

The nonredundancy constraint (SD-019) enforces structural separation between `z_harm_s` and `z_harm_a`; it operates at the suffering level, not the unpleasantness level.

---

## What MECH-219 Actually Computes

Updated specification given the three-primitive model:

> MECH-219 is a hysteretic integrator that takes `z_harm_un` (harm_unpleasantness) as input and produces `z_harm_a` (harm_suffering). The conversion is not a pure temporal integral: the accumulation rate is modulated by an **escapability estimate** (Q-036: controllability/inescapability signal), such that identical exposure to `z_harm_un` produces higher `z_harm_a` when harm is perceived as inescapable than when it is perceived as controllable.

Falsifiable predictions (updated):
1. After harm offset, `z_harm_un` falls rapidly while `z_harm_a` remains elevated (persistence property).
2. Two trajectories matched on current `z_harm_un` but with different controllability histories produce different `z_harm_a`.
3. An agent with high `z_harm_a` but moderate `z_harm_un` (chronic load, current hazard manageable) should exhibit mode-switching behavior (SD-032a trigger) that an agent with high `z_harm_un` but low `z_harm_a` (acute spike, not yet accumulated) should not.

---

## Open Questions (Q-036 Bridge)

Q-036 asks: beyond temporal integration, which variables are required for suffering to be a genuinely distinct load state?

The Löffler dissociation establishes that **controllability** is load-determining and non-temporal. The current evidence (three Q-036 entries, lit_conf=0.812) supports adding an escapability-belief signal into MECH-219's integrator. The following variables from Q-036 remain open:

| Variable | Evidence status | REE implication |
|---------|----------------|----------------|
| Controllability / escapability | Supported (Salomons 2004, Loffler 2018) | Gate MECH-219 accumulation by escapability estimate |
| Persistence / recovery failure | Suggestive (De Ridder 2021 acute→chronic transition) | Asymmetric decay already in MECH-219; should be validated |
| Inescapability (learned helplessness) | Indirect (literature pull needed) | Maps to a separate learned state on top of the accumulator |
| Prediction error weighted threat | Open (Fazeli & Buchel 2018 partial) | PE may modulate unpleasantness encoding, not suffering directly |

---

## Extension Register: Beyond Harm

The harm register is V3-complete (or nearly so). The affect classes beyond harm are consolidated
here. This register was reconciled on **2026-06-05** against the three proto-feelings audit
lit-pulls (`thought_intake_2026-06-01_protofeelings_audit_register.md` §7) so that **every
confirmed-distinct stream is represented** — previously the table listed only a single under-specified
"Relief" row and had not caught up to the registered safety cluster (MECH-303/304) or the newer
streams. `claims.yaml` status is tracked per row; rows marked **gated** still need a `claims.yaml`
claim (a follow-up governance decision, not done here).

| Affect class | REE signal | Claim backing | Status / scope |
|-------------|-----------|--------------|----------------|
| Benefit / resource | `z_benefit` / `z_goal` | MECH-112 (wanting) | V4-deferred (full benefit register) |
| **Relief** | offset/derivative of harm stream | **MECH-302** | V3 (registered claim) |
| **Safety** | learned threat-absence predictor | **MECH-303** (contextual) + **MECH-304** (cue-specific) | V3 (registered claims) |
| **Soothing / comfort** | autonomic state-gain modulator | **MECH-355** (candidate, V4-social) | V4-social (+ optional V3-minimal hook) |
| **Autonomic rebound (endogenous parasympathetic recovery)** | offset-triggered recovery-rate boost (MECH-219 recovery + SD-032e leak) | **MECH-356** (candidate, V3) | V3-tractable sibling of MECH-355 (endogenous trigger; gated build) |
| **Blocked agency (control-failure)** | `z_block` (new) | **MECH-353** (candidate, V3) | V3-candidate (lit-grounded; pending experiment) |
| **Coercion / domination / injustice** | (not yet specified) | — | V4-deferred (social; needs other-agent model) |
| **Effort / fatigue (stop-recover)** | `drive_level` (SD-012) + SD-048 interoceptive | **MECH-354** (candidate, V3) | V3-minimal, gated |
| Social harm | (not yet specified) | — | Research phase |

Each stream is differentiated from its neighbours below. The differentiations honour
`feedback_biology_before_formal_definitions`: distinct biological systems get distinct rows, never
one merged primitive (the SD-010→SD-011 *philosophy-right/mechanism-wrong* failure). The three
2026-06-05 pulls are: `targeted_review_affect_stream_relief_safety_soothing` (relief/safety/soothing),
`targeted_review_fatigue_vs_helplessness_dissociation` (fatigue/stop-recover vs suffering), and
`targeted_review_blocked_agency_anger_stream` (blocked-agency/anger). *Based on articles retrieved
from PubMed.*

### Extension Primitive (V3, registered): relief / safety

**Relief** (`MECH-302`) is an **event-locked, phasic, value-coding reinforcement** signal at the
**offset** of an aversive event — it reuses the reward/goal machinery (NAc/VTA; D1+NMDA coincidence,
Bergado Acosta et al. 2017) reading the SD-011 suffering derivative. It tags "this reduced suffering."

**Safety** (`MECH-303` contextual passive + `MECH-304` cue-specific conditioned inhibition) is a
**learned prospective predictor that threat is absent** — an active prefrontal-hippocampal-thalamic
representation (mPFC IL/PL; nucleus reuniens→BLA, Silva et al. 2021; Corches et al. 2019), **not**
mere low harm. It licenses commitment-release and approach.

**Differentiation:** relief is *past-offset / phasic / appetitive* (reinforcer); safety is
*future / tonic / inhibitory* (predictor/gate). Neither is the other, and neither is `z_goal`/wanting
(MECH-112) — safety is inhibitory prediction, not appetite. **Enrichment APPLIED 2026-06-05 (not
contradiction):** Silva 2021 (NRe→BLA, conf 0.80) implicated a midline-**thalamic** relay (nucleus
reuniens) and a remote-vs-recent (time-since-encoding) dependence absent from MECH-303/304's stated
anatomy. Both are now folded into the claims: MECH-304 carries the reuniens transmission node + the
remote/recent axis (Silva bears most directly on the active cue-specific pole); MECH-303 carries the
lighter cluster-level note that the safety-expression machinery is prefrontal-hippocampal-**thalamic**.
The consolidation-age axis is recorded on MECH-304 as a **candidate third safety sub-mechanism**
(consolidation-state-conditional safety expression interfacing the MECH-092/sleep replay machinery),
deliberately not minted yet (single rodent anchor, off the V3 critical path, no consolidation-interface
design). Thalamic relay + remote/recent axis are documentation-only (UNIMPLEMENTED in SD-051/SD-052).
*Evidence:* `targeted_review_affect_stream_relief_safety_soothing/` (verdict, conf 0.82).

### Extension Primitive (V4-social; V3-minimal hook optional): soothing / comfort

| Field | Value |
|-------|-------|
| **REE signal** | autonomic state-gain modulator (`MECH-355`) |
| **Status** | **MECH-355** (candidate; V4-social, `substrate_conditional`) — registered 2026-06-05; V4 substrate + update rule are later design decisions |
| **Character** | **Down-regulation of the ongoing stress response** (present-tense), canonically via a conspecific (social buffering) |
| **Biological analogue** | oxytocinergic + parasympathetic/HPA + prefrontal regulation (Hostinar et al. 2014; Heinrichs et al. 2003) |

**Computational role:** a state-gain / recovery modulator that **lowers the gain or speeds the
recovery** of the active aversive trajectory — proposed home is MECH-219 (suffering accumulator)
decay + SD-012 (drive) + SD-032e (pACC autonomic coupling).

**Differentiation:** soothing acts on the **present** stress trajectory, where relief is *past-offset*
and safety is *future-prediction*; its substrate is oxytocin/parasympathetic/HPA (vs NAc/VTA for
relief, vs cortico-amygdalar for safety); its role is state-gain modulation (vs reinforcer, vs
predictor). It is **socially gated** — the canonical trigger is a conspecific, which V3 cannot
represent. **Do NOT fold into Relief (MECH-302) or Safety (MECH-303/304), and NOT into MECH-112.**
Scope: **V4-social** primary. The non-social V3-minimal autonomic-recovery hook that the verdict
left optional is now split out as its **own sibling claim, MECH-356** (endogenous parasympathetic
recovery / autonomic rebound) — same effector/update rule, endogenous offset trigger instead of a
conspecific. MECH-355 stays the social, V4 arm; do NOT fold the two together. When the MECH-355
substrate is built it must depend on MECH-219 + SD-032e (the affective/autonomic `drive_bias`
component, NOT base SD-012 drive_level) and be explicitly NOT-302/303/304/112.
*Evidence:* `targeted_review_affect_stream_relief_safety_soothing/` (verdict, conf 0.82). Update-rule
+ scope design pass: `evidence/planning/mech_355_soothing_update_rule_and_scope_design_2026-06-05.md`.

### Extension Primitive (V3-candidate; sibling of soothing): autonomic rebound / endogenous parasympathetic recovery

| Field | Value |
|-------|-------|
| **REE signal** | offset-triggered transient boost to the recovery side of the slow affective accumulators (`MECH-356`) |
| **Status** | **MECH-356** (candidate; V3, `epistemic_category: standard`, `v3_pending`) — registered 2026-06-06; build gated behind in-flight cue-authority / z_goal work (off the V3 critical path) |
| **Character** | **Active, present-tense acceleration of return-to-baseline** after the agent's OWN stressor ends — not the passive fade of the aversive signal |
| **Biological analogue** | vagal rebound at stressor offset despite residual sympathetic activation; central-autonomic-network (prefrontal-vagal) recovery driver (Mezzacappa et al. 2001; Thayer & Brosschot 2005; Cunha et al. 2015) |

**Computational role:** the same decay-acceleration effector as MECH-355 soothing — a transient,
state-scaled multiplier on the MECH-219 `z_harm_a` `recovery_rate` (recovery side only; onset
untouched) and the SD-032e `drive_bias` leak — but driven by an **endogenous** trigger:
offset-detection (`d||z_harm_a||/dt < 0`, the MECH-302 SufferingDerivativeComparator signal), with
**no conspecific** and **no prediction**. Load-proportional (multiplicative on existing state →
zero effect on a calm agent → recovery ≠ sedation). Never writes base SD-012 `drive_level`,
`z_harm_s`, or `z_harm_un`. MECH-094 waking-only.

**Differentiation:** sibling of MECH-355 (same effector, endogenous trigger vs conspecific —
register as siblings, not a fold-in: the literature shows social support modulates the same
vagal-rebound variable, Tung et al. 2021). Distinct from passive MECH-219 recovery (active
overshoot, not decay), from MECH-302 relief (shared offset trigger, different output — relief
writes a reinforcer, rebound boosts recovery rate), and from MECH-303/304 safety (no prediction).
Closes REE's **sympathetic-rich / parasympathetic-poor asymmetry**.
*Evidence:* `targeted_review_autonomic_rebound_parasympathetic_recovery/` (verdict, conf 0.74).

### Extension Primitive (V3-minimal, gated): effort / fatigue (stop-recover)

| Field | Value |
|-------|-------|
| **REE signal** | `drive_level` (SD-012) + SD-048 interoceptive channel — a second homeostatic deficit alongside hunger (`MECH-354`) |
| **Status** | **MECH-354** (candidate, V3-minimal) — registered 2026-06-05; `v3_pending` until a discriminative experiment; build gated behind in-flight cue-authority/z_goal work |
| **Character** | A **stop-AND-recover** signal: accumulates with effort/time-on-task, **recovers with rest/sleep** |
| **Antecedent** | Cumulative **effort / time-on-task**, controllability-INDEPENDENT — accumulates from your own *successful* effort (Boksem & Tops 2008; Meyniel et al. 2013; Borbély et al. 2016) |
| **Biological analogue** | interoceptive cost-accumulator (posterior insula) + ACC effort-valuation; adenosine/Process-S for the slow sleep-pressure variant |

**Smallest computational form (Meyniel 2013):** a two-bound (hysteretic) leaky cost-evidence
accumulator — `F += Se*effort` during exertion, `F -= Sr` during rest; emit STOP at the upper bound,
recover to the lower bound before re-engaging. Two time-constants: a fast within-task accumulator and
a slow sleep-pressure accumulator (offline reset via SD-017 sleep). `Se`/`Sr`/bound-gap are
incentive-modulated (incentive → work closer to exhaustion).

**Differentiation (vs suffering / learned helplessness, SD-011 side):** they converge behaviourally
on *stop/disengage* but separate on four axes — antecedent (effort-depletion vs uncontrollable
aversion), substrate (interoceptive cost-accumulator vs DRN 5-HT/CRF), computation (value
recalibration, incentive-reversible vs escape-failure), and **decisively recovery: fatigue remits
with rest, helplessness does NOT** (needs controllability/pharmacological reversal). **Do NOT wire
fatigue as a `z_harm` / SD-011 nociceptive stream** — that imports the wrong antecedent, gate, and
dynamics. This is the upstream fix for the DEV-NEED-002 conflation ("harm, hunger, fatigue blur
together").

**Consumers:** the **in-task STOP** feeds MECH-342 (commit-maintenance release) as a *new deficit
input* (alongside the R-c execution-readiness deficit) and the ARC-078 goal-disengagement consumer
via a cost/benefit (not aversive) channel — the **release actuator is shared** with the suffering
pole, reached from the opposite antecedent. The **recover / re-accumulation half is NOT in MECH-342**;
it belongs on the SD-012 / SD-017 side. *Evidence:*
`targeted_review_fatigue_vs_helplessness_dissociation/` (VERDICT).

### Extension Primitive (V3-candidate): blocked_agency

| Field | Value |
|-------|-------|
| **REE signal** | `z_block` (blocked-agency / control-failure stream; `MECH-353`) |
| **Status** | **MECH-353** (candidate, V3) — registered 2026-06-05; lit-grounded, `v3_pending` until the discriminative experiment lands |
| **Character** | Rises when an intended/expected action-outcome is **repeatedly blocked** while the goal and the agent's capacity-belief are retained |
| **Antecedent** | A **negative disparity between expected and realised action-outcome** — an expectation/agency violation, **not** noxious input (frustrative non-reward; Papini et al. 2024) |
| **Time constant** | Medium — integrates blocked attempts over a window; distinct from instantaneous harm |
| **Controllability dependence** | High, but **opposite polarity to suffering**: `z_block` is the **capacity-RETAINED** pole (assert), where `z_harm_a` is the **capacity-COLLAPSED** pole (withdraw) |
| **Biological analogue** | RAGE as a distinct primary-process system (Davis & Montag 2019); frustrative non-reward circuit (Papini et al. 2024); reactive-aggression assert channel under prefrontal gating (Bertsch et al. 2020) |

**Computational form (smallest):** `z_block` is layered on substrate REE already has —
1. **Detector (exists):** the agency comparator (SD-029) applied to the *action-outcome / goal channel* — intended effect predicted by the forward model (E2), realised effect diverges (the comparator-model account of agency and its breakdown; Carruthers 2012).
2. **Expectation (exists):** z_goal / wanting (MECH-112) supplies the "expected outcome."
3. **New work — readout + two gates:** integrate comparator mismatch over a window → `z_block ↑`; an **attribution gate** (mismatch caused by *external constraint*, not own motor error); a **capacity gate** (fires as *assert* only while goal/capacity is retained; hands off to `z_harm_a` as capacity-belief collapses).

**Differentiation (each neighbour, explicitly):**
- **vs harm (SD-011, `z_harm_*`):** harm's antecedent is noxious contact; `z_block` fires with **zero noxious input** (a merely-blocked/omitted outcome). Distinct antecedent, distinct biology (RAGE circuit vs nociceptive medial pathway). Collapsing them would repeat the SD-010→SD-011 *philosophy-right/mechanism-wrong* error.
- **vs suffering (SD-019b, `z_harm_a` + Q-036):** same controllability axis, **opposite pole**. Capacity-belief collapsed → withdraw (suffering, already in REE); capacity-belief retained → assert (`z_block`). REE currently encodes only the withdraw pole — the **energised assert pole is the piece this primitive adds.**
- **vs residue (MECH-056):** residue is the trace of an action *taken* at a value-cost; `z_block` is an action *prevented*. Opposite causal structure, different consumer.
- **vs commitment-hold (MECH-090 beta-gate):** MECH-090 is the **licit, self-imposed** gating of E3→action during a committed sequence; `z_block` is an **externally-imposed** block against a live goal. Self-hold (licit) vs external-block (the new signal).

**Consumers it drives:**
- **Assert / escalate-effort / try-different** (new behavioural pole) — raise drive/vigor (MECH-320), search an alternative action that restores the intended outcome (reactance direct-restoration; the adaptive analogue of reactive aggression).
- **Decommit (MECH-342)** — if assertion fails across the window, release the blocked commitment rather than escalate unboundedly; gated by the commitment-threshold (ARC-016), the prefrontal-analogue of reactive-aggression inhibition (Bertsch et al. 2020).
- **Withdraw** — *not* native to this stream; reached only via hand-off to `z_harm_a` when capacity-belief collapses.

**Scope:** V3-tractable as a **single-agent proxy** — "an intended, predicted-to-succeed action is repeatedly blocked by the environment/constraint." The **coercion / domination / injustice** extension (Stream B below) requires modelling an *other agent* as the source of the restriction and is **V4-deferred** (psychological reactance / autonomy-threat, Steindl et al. 2015; injustice/norm-violation appraisal). Anti-domination and anti-exploitation are inherently other-agent — defer; cross-link the V4 ethics cluster (`thought_intake_2026-05-31_musings_on_v4.md`).

**Smallest V3 test (gated; not yet queued):** an environment that repeatedly blocks an intended,
predicted-to-succeed action while harm and goal-value are held constant; measure whether a
comparator-mismatch readout rises, whether it drives *assert/persist* (effort escalation /
alternative-action search) distinct from the withdraw signature, and whether it dissociates from
`z_harm_a` under matched controllability.

*Evidence:* `evidence/literature/targeted_review_blocked_agency_anger_stream/` (5 entries + VERDICT).
*Based on articles retrieved from PubMed.*

---

## Lit-pull status

| Primitive | Coverage | Next pull |
|-----------|---------|-----------|
| harm_intensity | Strong (SD-011 targeted reviews) | — |
| harm_unpleasantness | Partial (Rainville 1997 in SD-019 pulls; SD-019a not yet targeted) | Needed — medial pathway fast component, ACC/insula unpleasantness encoding |
| harm_suffering | Moderate (Q-036 pull 2026-04-20, 3 entries) | Needed — inescapability / learned helplessness; prediction error in suffering |
| relief | Strong (`relief_completion_mechanism` 2026-05-03 + `affect_stream_relief_safety_soothing` 2026-06-05) | — (MECH-302 grounded) |
| safety | Strong (`affect_stream_relief_safety_soothing`, 2026-06-05) | — thalamic-relay (reuniens→BLA) + remote/recent enrichment APPLIED 2026-06-05 to MECH-303/304; candidate third (consolidation-age) sub-mechanism flagged, not minted |
| soothing / comfort | Strong (`affect_stream_relief_safety_soothing`, 2026-06-05, 2 entries) | — (V4-social; claim registration is the gated next step) |
| effort / fatigue (stop-recover) | Strong (`fatigue_vs_helplessness_dissociation`, 2026-06-05, 5 entries) | — (SD-012-side MECH registration is the gated next step) |
| blocked_agency | Strong (`targeted_review_blocked_agency_anger_stream`, 2026-06-05, 5 entries) | — for the V3 row; Stream B (coercion/injustice) is a V4 pull when the social substrate exists |
