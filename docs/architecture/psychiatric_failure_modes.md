# Psychiatric Failure Modes as Architectural States

*Emergent from EXQ-237a LONG_HORIZON condition. Seed=42. First observed 2026-04-06.*

---

## Overview

The REE architecture produces psychiatric phenomenology as emergent failure modes, not by design.
When specific architectural components fail or are absent, the resulting behavioural patterns
correspond structurally to recognised clinical syndromes. This document catalogues the 2x2
motivational state taxonomy, the three missing serotonergic mechanisms that define the V4
treatment model, and the predictions that follow.

The key insight from EXQ-237a is that the LONG_HORIZON condition (3 hazards, 1 resource,
150 steps) produced goal_norm=0.004 in the PLANNED condition, with resource_rate and harm_rate
identical between HABIT and PLANNED modes. The goal-directed planning system was structurally
intact, but behaviourally silent -- the environment had collapsed the motivational terrain that
planning requires.

---

## 2x2 Psychiatric State Taxonomy

The motivational state of the agent at any time can be characterised by two independent
variables: the level of z_harm_a (aversive arousal) and the status of z_goal (wanting signal).

| | z_goal INTACT | z_goal ABSENT |
|----------------------|--------------------------------|--------------------------------------|
| **z_harm_a ELEVATED** | GAD-like state | Anxious depression (INV-053 attractor)|
| **z_harm_a LOW** | Healthy goal-directed behaviour | Melancholic depression (burnt-out) |

### Cell descriptions

**Healthy (z_harm_a low, z_goal intact)**
Normal goal-directed behaviour. Planning and habitual modes diverge: PLANNED achieves higher
resource_rate, lower harm_rate. The architecture functions as designed.

**GAD-like (z_harm_a elevated, z_goal intact)**
Goals exist but are repeatedly interrupted by threat responses. z_harm_a fires during goal
pursuit, triggering avoidance that displaces goal-directed sequences before completion.
The agent wants but cannot sustain action sequences long enough to succeed. Anxiety without
motivational collapse: the planning system is engaged but constantly derailed.

**Anxious depression (z_harm_a elevated, z_goal absent) -- INV-053 attractor**
This is the state observed in EXQ-237a LONG_HORIZON. Chronic harm exposure has suppressed
benefit_exposure below the SD-012 seeding threshold. z_goal cannot form. The VALENCE_WANTING
terrain in the residue field has collapsed to near-zero. HABIT and PLANNED modes are
behaviourally identical because the planning system has no motivational signal to act on.
Aversive arousal is elevated (harm_rate=0.14) but wanting is absent (goal_norm=0.004).
This corresponds structurally to anxious depression: the patient is activated (aroused,
vigilant, distressed) but cannot initiate or sustain goal pursuit.

**Melancholic depression / burnt-out attractor (z_harm_a low, z_goal absent)**
A further evolution of the anxious depression attractor: z_harm_a has habituated to the
chronic aversive environment, leaving flat affect (low aversive arousal) combined with
absent wanting. The agent is neither distressed nor motivated. This corresponds to
melancholic depression: psychomotor retardation, anhedonia, flat affect, absent initiative.
Both depressive cells share the z_goal=0 foundation; they differ in whether aversive arousal
remains active.

---

## The Three-Stage Motivational Pipeline

Goal-directed behaviour in aversive environments requires tonic regulation at three stages
(INV-052):

```
Stage 1: TERRAIN         Stage 2: TRANSDUCTION    Stage 3: MAINTENANCE
VALENCE_WANTING floor    benefit -> z_goal gain    z_goal persistence
(MECH-186)               (MECH-187)                (MECH-188)
```

### Stage 1 -- Terrain maintenance (MECH-186)

A slow-accumulating tonic signal (serotonergic analog) maintains a non-zero floor on
VALENCE_WANTING entries in the residue field even when phasic benefit events are sparse.
Without this, a chronic harm-dominated environment suppresses the benefit gradient until
it is flat. The agent has no terrain to navigate toward resources.

**Failure mode:** benefit terrain collapse. Agent cannot orient toward goals because the
residue field contains no WANTING gradient. HABIT and PLANNED modes become equivalent.

### Stage 2 -- Gain regulation (MECH-187)

The serotonergic system modulates the gain on the benefit->z_goal transduction function.
Currently SD-012 implements a hard threshold: benefit_exposure must exceed a floor to
produce any z_goal seeding. MECH-187 converts this to an adaptive graded function.

**Failure mode:** anhedonia as wanting failure. Benefit events occur (liking is intact),
but z_goal is not seeded (gain is suppressed). This is the Berridge dissociation
(MECH-117): liking preserved, wanting abolished. The agent can enjoy resources when it
encounters them reactively but does not seek them.

### Stage 3 -- Goal persistence (MECH-188)

Once z_goal has been seeded, a PFC-mediated working memory mechanism (modulated by
5-HT projections from DRN to dlPFC) maintains the representation through periods of
elevated harm or temporarily reduced benefit exposure.

**Failure mode:** goals form but cannot be held. z_goal collapses at the first harm
event. This is the "cannot hold a plan" phenomenology: the patient articulates goals
but fails to sustain them against distraction, threat, or delay. Architecturally
distinct from the GAD-like state (where goals are present but interrupted by z_harm_a)
because here z_goal itself collapses, not just execution sequences.

---

## The Depressive Maintenance Loop (INV-054)

Once the INV-053 attractor is established, it is self-maintaining:

```
VALENCE_WANTING terrain collapses
         |
         v
Benefit-oriented exploration reduces (no gradient to follow)
         |
         v
Benefit encounters reduce
         |
         v
benefit_exposure stays below SD-012 threshold
         |
         v
z_goal seeding remains blocked
         |
         v
VALENCE_WANTING terrain cannot recover  <-- closed loop
```

This closed negative feedback loop predicts:

1. **Chronicity**: the depressive attractor is self-maintaining once established;
   environmental improvement alone may be insufficient.

2. **Phase transition recovery**: the transition from depressive attractor to normal
   function requires a threshold crossing (sufficient benefit_exposure to cross the
   SD-012 seeding threshold), not a gradual linear improvement. This maps to the
   clinical observation that antidepressant response is often non-linear.

3. **Behavioural activation as first-line treatment**: externally scaffolding benefit
   encounters (behavioural activation therapy) directly targets the maintenance loop
   by restoring benefit_exposure above threshold, rebuilding the terrain gradient,
   allowing z_goal to re-form.

---

## Q-034: The Hazard/Resource Ratio Prediction

EXQ-237a revealed the depressive attractor by varying environment structure (3 hazards,
1 resource). Q-034 asks whether the relevant parameter is the ratio of harm exposure
to benefit exposure opportunity, not absolute stress intensity.

**Prediction:** a fixed hazard_harm level with sufficient resource density never produces
the INV-053 attractor; the same hazard_harm with insufficient resources does.

**Testable:** CausalGridWorldV2, hold hazard_harm constant, vary num_resources (or hold
num_hazards constant, vary num_resources). Sweep the ratio.

**Implications if confirmed:**
- Depression is a resource-availability disorder as much as a stress disorder
- The same stressor produces depression or not depending on available positive affordances
- Interventions targeting benefit availability (not just stress reduction) are therapeutic
- Environmental enrichment (adding positive affordances) has mechanistically distinct
  effects from anxiolytic treatment

---

## Frame-Tag Failure Modes: Developmental Etiology (INV-061, MECH-200, MECH-201, MECH-202)

> **Registered 2026-04-06.** Extends MECH-094 (hypothesis tag loss = psychosis mechanism)
> with a developmental pathway via MECH-198 (pretend play as frame-distinction training).

### Common Architectural Substrate (INV-061)

The REE architecture distinguishes real from synthetic/hypothetical frames via two
co-operating tag systems: the **hypothesis tag** (MECH-094, agent-internal, marks
simulation/replay as non-real) and the **play frame tag** (ARC-049, bilateral, marks
play episodes as authorized-synthetic). Pretend play (MECH-198) is the developmental
phase where these two systems first co-operate.

When pretend play is absent or insufficient, the frame-distinction mechanism is
undertrained. The resulting adult failure modes are not independent disorders but
**different failure signatures of the same undertrained mechanism**, varying by:

1. **Direction of confusion**: real→synthetic (derealization cluster) vs synthetic→real (delusion cluster)
2. **Affected subsystem**: frame tag, commitment gate, or threat evaluation

This provides a unified developmental etiology for conditions that are clinically
distinct but architecturally related.

### MECH-200: Real→Synthetic Confusion (Derealization Direction)

The agent treats real consequences as if they were synthetic. The frame tag reads
"play" when the environment is real.

**Mechanism**: the real/synthetic distinction was never properly calibrated during
pretend play. The agent defaulted to tagging ambiguous frames as synthetic (the
safer error during play, where real consequences are absent). In adulthood, this
default persists: when frame signals are ambiguous, the agent discounts real harm
signals as if they were play-harm.

**Behavioral signatures:**
- Actions under real-harm conditions with play-appropriate (i.e. absent) defensive responses
- Commitment without adequate threat evaluation
- Harm signals discounted or experienced as distant/unreal

**Psychiatric mappings:**

| Signature | Clinical analogue | REE mechanism |
|-----------|------------------|---------------|
| Real harm experienced as unreal | **Derealization** | Frame tag stuck on "synthetic"; z_harm_s fires but is discounted |
| Elevated commitment, reduced consequence-sensitivity | **Manic episodes** | Play frame leaks into real operation; commitment gate fires without harm-gate check |
| Actions feel consequence-free | **Dissociative states** | Frame tag intermittently flips to "synthetic" under stress |

### MECH-201: Synthetic→Real Confusion (Delusion Direction)

The agent treats internally generated or simulated representations as real. The
hypothesis tag (MECH-094) fails to suppress real-consequence responses during
simulation, replay, or imagination.

**Mechanism**: during pretend play, the hypothesis tag must be active (the stick
is not really a sword) while the play tag is also active (the fight is not really
dangerous). If pretend play was insufficient, the hypothesis tag was never properly
co-exercised with the play tag. In adulthood, internally generated representations
— simulation, replay, imagination — lack the hypothesis tag marker and are processed
through the real-consequence pipeline.

**Behavioral signatures:**
- Internally generated scenarios trigger full emergency responses
- Replay episodes experienced as happening now, not as memory
- Pre-commit simulation generates real threat responses

**Psychiatric mappings:**

| Signature | Clinical analogue | REE mechanism |
|-----------|------------------|---------------|
| Internal representations experienced as external | **Delusion formation** | Hypothesis tag absent; E3 treats simulated trajectories as real percepts |
| Replay triggers full emergency response | **PTSD flashback** | SWR replay (MECH-121) lacks hypothesis tag; experienced as real re-occurrence |
| Simulation generates real threat | **Anxiety disorders** | Pre-commit simulation (normally hypothesis-tagged) triggers z_harm_a as if real |
| Imagined social scenarios feel real | **Paranoid ideation** | Simulated other-agent threat (MECH-127 counterfactual) processed without hypothesis tag |

### MECH-202: Commitment Gate Developmental Failure

The commitment gate (E3 commit boundary) is undertrained because it was never
exercised in synthetic mode during pretend play. Two failure directions:

**Direction A — Insufficient inhibition (impulsivity):**
The gate fires without completing E3 evaluation. During pretend play, the gate
would have been exercised in a low-stakes context where premature commitment has
no real consequences, allowing calibration. Without this calibration, the gate
threshold is set too low.

| Signature | Clinical analogue | REE mechanism |
|-----------|------------------|---------------|
| Commits without evaluation | **Impulsivity** | Commitment gate fires before E3 harm/benefit evaluation completes |
| Elevated commitment + reduced harm sensitivity | **Mania** (commitment component) | Gate threshold too low + MECH-200 frame confusion compound |
| Cannot delay gratification | **Impulse control disorders** | Gate does not wait for E2 rollout to complete |

**Direction B — Excessive inhibition (paralysis):**
The gate never fires even when evaluation is complete. Without pretend play
calibration, the gate threshold was never lowered from the infant default
(very high commit threshold, INV-055). The agent remains in perpetual
pre-commit evaluation.

| Signature | Clinical analogue | REE mechanism |
|-----------|------------------|---------------|
| Endless re-evaluation without commitment | **OCD** (checking/rumination) | Gate threshold never calibrated down from infant default; E3 loops without committing |
| Complete inability to initiate action | **Catatonia** | Gate frozen at maximum threshold |
| Decision paralysis despite completed evaluation | **Severe indecision** | Commitment gate signal never reaches threshold |

### Developmental Evidence

The frame-confusion etiology predicts that pretend play deficits in early childhood
should correlate with later frame-distinction failures. Existing evidence is consistent:

- Reduced pretend play predicts later psychotic symptoms (Cannon et al. 2002)
- Children with autism show reduced pretend play AND elevated psychosis risk
- Pretend play → theory of mind → reality testing are developmentally linked
- Imaginative play correlates with later impulse control (Diamond & Lee 2011)

### Relationship to MECH-094

MECH-094 identifies hypothesis tag loss as a psychosis mechanism. The frame-confusion
cluster (MECH-200/201/202) extends this by explaining WHY the tag system might be
fragile: because pretend play (MECH-198) is where the real/synthetic frame distinction
is first calibrated. MECH-094 describes the proximal mechanism (tag loss); MECH-198/200/201
describe the developmental etiology (insufficient calibration during childhood).

---

## Claims Covered

| ID | Label | Stage |
|----|-------|-------|
| MECH-186 | 5HT_tonic.benefit_gradient_maintenance | Terrain (Stage 1) |
| MECH-187 | 5HT.incentive_salience_gain_regulation | Transduction (Stage 2) |
| MECH-188 | 5HT_PFC.goal_persistence_under_adversity | Maintenance (Stage 3) |
| INV-052 | tonic_regulatory_system_for_goal_persistence | All three stages required |
| INV-053 | computational_depression_attractor | Anxious depression cell |
| INV-054 | depressive_maintenance_loop | Chronicity mechanism |
| Q-034 | hazard_resource_ratio_depression_threshold | Open testable question |

| INV-061 | frame_confusion_unified_developmental_etiology | All frame-tag failures share common substrate |
| MECH-200 | frame_confusion_real_as_synthetic | Derealization, mania, dissociation |
| MECH-201 | frame_confusion_synthetic_as_real | Delusions, PTSD flashbacks, anxiety |
| MECH-202 | commitment_gate_developmental_failure | Impulsivity, OCD, catatonia |

**Updated claims:**
- INV-034: added clinical inverse note (goal maintenance failure = depression, EXQ-237a)
- MECH-117: added clinical note (Berridge dissociation as architectural consequence of MECH-187 failure)
- MECH-094: developmental etiology added via MECH-198/200/201 (pretend play calibrates the tag system)

---

## Implementation Status

All three serotonergic mechanisms (MECH-186, 187, 188) are V4 scope. They are not present
in the current V3 substrate. The depressive attractor state (INV-053) is therefore an
emergent property of the V3/current architecture under adversarial environment conditions.

V4 design will need to specify:
- Tonic accumulator separate from phasic DA signals in the residue field update rule
- Gain parameter on the SD-012 seeding function, modulated by tonic 5-HT level
- PFC working memory module for z_goal maintenance between benefit events

---

*Architecture note: EXQ-237a LONG_HORIZON condition (3 hazards, 1 resource, 150 steps),
seed=42. Full replication pending seeds 7 and 13.*
