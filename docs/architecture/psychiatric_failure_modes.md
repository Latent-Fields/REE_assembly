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

**Updated claims:**
- INV-034: added clinical inverse note (goal maintenance failure = depression, EXQ-237a)
- MECH-117: added clinical note (Berridge dissociation as architectural consequence of MECH-187 failure)

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
