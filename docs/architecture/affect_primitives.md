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

The harm register is V3-complete (or nearly so). For reference, the analogous structures in
other affect classes are noted here as V4-deferred stubs:

| Affect class | REE signal | Primitive split | Status |
|-------------|-----------|----------------|--------|
| Benefit / resource | `z_benefit` / `z_goal` | intensity / wanting / satisfaction | V4-deferred |
| Relief | (termination of harm stream) | relief_spike / relief_sustained | V4-deferred |
| Social harm | (not yet specified) | — | Research phase |
| Effort / fatigue | `drive_level` + SD-032b dACC | effort_cost / fatigue_load | Partially implemented |

---

## Lit-pull status

| Primitive | Coverage | Next pull |
|-----------|---------|-----------|
| harm_intensity | Strong (SD-011 targeted reviews) | — |
| harm_unpleasantness | Partial (Rainville 1997 in SD-019 pulls; SD-019a not yet targeted) | Needed — medial pathway fast component, ACC/insula unpleasantness encoding |
| harm_suffering | Moderate (Q-036 pull 2026-04-20, 3 entries) | Needed — inescapability / learned helplessness; prediction error in suffering |
