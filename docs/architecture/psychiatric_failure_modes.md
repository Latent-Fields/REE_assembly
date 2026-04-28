---
nav_exclude: true
---

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
| MECH-202 | commitment_gate_developmental_failure | Impulsivity, OCD, catatonia (commit-gate paralysis subtype) |
| SD-036 | gabaergic.cross_stream_decay_regulator | Catatonia (harm-stream lock-in subtype) -- see EXQ-471 exemplar below |
| MECH-279 | pag.gabaergic_freeze_gate | Freeze response duration; failure -> sustained immobility |

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

## Serotonergic Cross-State Architecture (MECH-203, MECH-204)

> **Registered 2026-04-06.** The serotonergic system operates across waking and sleep states.
> The three waking mechanisms (MECH-186/187/188) are incomplete without their sleep-state
> counterparts.

### The Incomplete Substrate Problem

MECH-186/187/188 model tonic regulatory systems during waking behavior. But serotonin's
architectural role spans the wake-sleep boundary:

1. **During waking**: tonic 5-HT maintains the benefit gradient (MECH-186), regulates
   incentive salience gain (MECH-187), and supports goal persistence (MECH-188).

2. **During SWS**: the tonic 5-HT level *tags* which experiences get prioritized for
   replay. High-5-HT experiences (benefit-salient) should be replayed alongside
   harm-salient experiences from the residue field. (**MECH-203**)

3. **During REM**: 5-HT *withdrawal* (dorsal raphe quiescence) defines the zero-point
   for precision recalibration. Without this, MECH-123 has no reference state to
   recalibrate against. (**MECH-204**)

### MECH-203: Serotonergic Replay Salience Tagging

The residue field marks harm-dense experiences for preferential NREM replay (MECH-099,
MECH-121). But benefit-salient experiences are equally important for consolidation --
particularly missed opportunities (high benefit_exposure, low z_goal_norm) where the
agent *could have* formed a goal but failed to.

Tonic 5-HT level at time of experience serves as the benefit-salience tag:
- High tonic 5-HT -> experience tagged for benefit-replay
- Low tonic 5-HT (depressive state) -> benefit-experiences under-tagged

**Psychiatric prediction:** Depressed agents show reduced benefit-replay density during
SWS relative to harm-replay density. This creates a consolidation asymmetry: harm
knowledge is maintained (the world remains threatening in memory) while benefit
knowledge degrades (opportunities are forgotten). This contributes to the depressive
maintenance loop (INV-054) via a sleep-mediated pathway.

### MECH-204: Serotonergic REM-Gate Zero-Point

MECH-123 (REM precision recalibration) currently has no specification for how the
recalibration target is established. This claim proposes: 5-HT withdrawal during REM
actively *sets* the zero-point by removing the benefit gradient that biases waking
precision. The system recalibrates against a neutral reference.

This makes REM recalibration not merely "allowed by" 5-HT withdrawal but "calibrated
by" it. Connects to:
- **INV-045** (phase ordering): SWS needs active benefit gradient (for MECH-203 tagging);
  REM needs gradient absent (for MECH-204 zero-point). The serotonergic state transition
  implements the SWS-to-REM computational boundary.
- **MECH-178**: noradrenergic REM suppression blocks 5-HT withdrawal, disrupting both
  replay salience (MECH-203) and recalibration zero-point (MECH-204) -- a double hit
  explaining rigidity rather than just reduced recalibration.

**Pharmacological prediction:** 5-HT agonists administered during REM should impair
precision recalibration quality specifically (not SWS consolidation), because they
prevent the zero-point from being established.

---

*Architecture note: EXQ-237a LONG_HORIZON condition (3 hazards, 1 resource, 150 steps),
seed=42. Full replication pending seeds 7 and 13.*

---

## Dream Phenomenology as Diagnostic and Treatment-Response Marker (INV-062, MECH-205–210)

The four-type dream taxonomy (INV-062) follows directly from the offline pipeline architecture and provides a clinically accessible window into which process is running, whether it converged, and whether the pipeline is intact.

### The four types and their computational signatures

| Dream type | Process | Phase | Key phenomenological marker |
|-----------|---------|-------|----------------------------|
| **Type 1: Stress/escape frustration** | Harm-contrastive replay not converging (MECH-205) | SWS / early REM | Agent trying to escape; everything fails systematically; no resolution |
| **Type 2: Joy/goal frustration** | Goal-contrastive replay not converging (MECH-205) | SWS / early REM | Agent trying to reach goal; everything fails systematically; no resolution |
| **Type 3: Procedural superposition** | NREM SWR semantic consolidation (MECH-121, MECH-209) | NREM2 / SWS | No agent; one thing as all instances simultaneously; all angles, scales, times at once; peaceful |
| **Type 4: Detailed story, close to reality** | REM E1 world-model free-running (MECH-210, MECH-123) | REM | Agent in coherent novel world; narrative arc; close to plausible; super interesting |

The frustration in Types 1 and 2 is not incidental affect — it is the convergence failure signal. The dream continues because the termination criterion (causally relevant features extracted) has not been met. Non-resolution is a direct phenomenological report of the replay loop still running. The self-dissolution in Type 3 is the signature of episodic context being stripped during semantic abstraction. The narrative coherence and novelty in Type 4 is E1's world model generating in-distribution but never-experienced sequences — interesting because E1 is surfacing latent structure from its prior.

### Psychiatric predictions

**PTSD (MECH-205, MECH-094, MECH-208):**
Recurring non-resolving Type 1 dreams are a direct marker of convergence failure on harm-contrastive replay. The causal features of the threatening episode have not been extracted; the residue field update is incomplete. The intrusive quality of PTSD nightmares follows from MECH-094 hypothesis tag degradation under high-affect replay load — the replay loses its simulation marker and is processed as real re-occurrence rather than a search procedure.

*Treatment-response prediction:* Successful trauma therapy should produce a shift from non-resolving to resolving Type 1 dreams before the patient reports conscious relief. The dream convergence precedes the waking resolution because the offline process completes before the waking narrative catches up. This is testable with prospective dream diaries alongside standard clinical outcome measures.

**Anxiety disorders (MECH-208):**
Elevated harm-weighting (z_beta / residue field) allocates excess replay budget to Type 1 at the expense of Types 3 and 4. Anxious individuals are predicted to report:
- Predominantly Type 1 dreams, longer and more intense
- Reduced frequency of Type 3 (insufficient budget for semantic consolidation)
- Reduced frequency or degraded quality of Type 4 (insufficient budget for world model exploration)

The self-reinforcing loop (MECH-208): elevated harm-weighting → more harm-path replay → more harm-predictive feature extraction → more avoidance → less corrective evidence → maintained harm-weighting. Dream diary composition (ratio of Type 1 to Types 3+4) is a potential proxy for the state of this loop.

**Depression (MECH-203, INV-054):**
Reduced benefit-replay density during SWS relative to harm-replay density (MECH-203 disruption under low tonic 5-HT) predicts a specific Type 2 deficit: the joy-frustration goal dreams should be reduced or absent, while Type 1 may be maintained. This is the replay-mediated maintenance of the depressive maintenance loop — the system has insufficient approach-side contrastive replay to extract goal-predictive features, while harm-side replay continues normally.

**Dementia (MECH-210, MECH-178, INV-046):**
As E1's world model degrades through the noradrenergic rigidity pathway (MECH-178), Type 4 dreams should degrade in a predictable sequence:
1. Type 4 becomes less interesting (prior no longer surfaces novel structure — repetitive familiar patterns)
2. Type 4 collapses toward habit-like sequences (the world model can only generate well-worn paths)
3. Type 4 disappears entirely (REM integrity too disrupted to sustain free-running)

This gradient may precede other detectable symptoms. Prospective dream diary tracking in cognitively healthy individuals over-65 may identify early E1 degradation before standard neuropsychological tests reach threshold.

**REM-suppressing medications (MECH-173, MECH-210):**
Any medication that suppresses REM (anticholinergics, MAOIs, most antidepressants, benzodiazepines) should selectively eliminate Type 4 while leaving Types 1–3 relatively intact. Type 3 (NREM SWS process) may actually increase if the replay budget freed from REM is redistributed, but Types 1/2 (early REM contrastive replay) may also be affected by REM suppression. A testable cross-over design: measure dream-type composition before and after REM-suppressing medication, with and without sleep-stage verification.

### Epistemic status

The four-type taxonomy is first-person phenomenological data from one observer (DG), noted as definite types but not claimed to be exhaustive. The mapping to computational processes is an interpretation requiring corroboration from other observers and eventual connection to polysomnographic sleep-stage measurement. Dream diaries from multiple individuals, classified by structural type (agent/no-agent, resolving/non-resolving, sequential/simultaneous), would allow initial corroboration without sleep-lab equipment.

---

## Self-Model Failure Modes: E1 Schema Poverty and E2 Capacity Degradation (INV-064, MECH-214, MECH-215)

> **Registered 2026-04-07.** A class of failure modes distinct from motivational/reward
> pathology: the preconditions for coherent goal-directed agency are absent, not the
> motivational system itself.

### The Architectural Distinction

The motivational failure modes above (INV-052–054, 2x2 taxonomy) assume that the
agent has a functioning self-model and an accurate model of its own capabilities.
These failures are located in the goal-seeding and terrain-maintenance pipeline —
the agent could form goals but the signal is absent or degraded.

A separate class of failure exists upstream of that pipeline: **the self-model
required to be the subject of goal-directed action is itself degraded**. This
produces a superficially similar phenomenology (absence of goal-directed behaviour,
motivational flatness, inability to plan) but through a different architectural
pathway with different treatment implications.

The distinction maps onto three claims:

- **INV-064**: E1 schema differentiation → E2 transition differentiation → E3
  evaluative capacity is a strict computational dependency. E3 cannot productively
  train until its inputs (z_world from E1, action_objects from E2) carry sufficient
  information. The biological fact that the prefrontal cortex myelinates last is an
  architectural necessity, not a developmental accident.

- **MECH-214**: Goal *content* is constituted by E1 schema space. A goal aimed at
  an E1-unrepresented state is a random vector in E3's operating space — it cannot
  generate coherent viability terrain or trajectory proposals. Goal coherence
  co-develops with E1 schema richness.

- **MECH-215**: Goal *pursuit* requires E2 self-transition accuracy. The "I" that
  makes a goal first-personal — *I* can reach *that* — is constituted by E1's
  self-schemas (who I am, what I feel, what my body is) and E2's self-transition
  model (what I can do, how my actions transform my state). Without both, E3's
  viability estimates have no coherent subject.

### Two Failure Modes

**Mode A — Goal incoherence (MECH-214 failure):**

E1 schema differentiation is insufficient. The agent cannot form stable representations
of the states it nominally wants. Goal-directed behaviour appears absent or directionless
— not because the wanting system is suppressed (MECH-187 failure) but because there is
no representationally coherent object for wanting to point at.

| Signature | Clinical mapping | REE mechanism |
|-----------|-----------------|---------------|
| Wanting without object — diffuse, undirected motivation | Certain anhedonic/dysthymic presentations | z_goal seeded but referent E1-unrepresented; z_goal is effectively noise |
| Goals stated but behaviorally inert | Alexithymia, emotional-cognitive disconnection | Goal object not grounded in affective E1 schema; E3 evaluates an abstract token |
| Difficulty identifying what one wants at all | Schizoid features, depersonalisation | E1 self-schema and world-schema both poorly differentiated; goal space is near-empty |
| Repeated pursuit of goals that produce no satisfaction | Compulsive achievement without hedonic gain | Goal object represented abstractly (status, money) but E1 has no schema for the hedonic state they were proxies for |

Crucially, this failure is **not dopaminergic**. The wanting system (MECH-187 gain)
may be intact; there is simply no coherent target for it to amplify. Standard
antidepressants and dopamine agonists do not address E1 schema poverty.

**Mode B — Capacity estimate failure (MECH-215 failure):**

E2 self-transition accuracy is degraded. The agent's model of what it can do — how
its actions transform its own z_self state — is systematically wrong. E3 receives a
corrupted capacity model and produces viability estimates that are either
catastrophically pessimistic (the world looks unnavigable) or unrealistically
optimistic (the agent overestimates its reach).

| Direction | Signature | Clinical mapping | REE mechanism |
|-----------|-----------|-----------------|---------------|
| Pessimistic | Cannot start — world appears unnavigable | Learned helplessness, agoraphobia, avoidance | E2 self-transitions predict action → no change or harm; E3 viability estimates uniformly low |
| Pessimistic | Knows the goal, cannot move toward it | Depression (action-initiation subtype) | E2 capacity model: I cannot do what this goal requires |
| Optimistic | Overestimates capability, repeatedly fails | Manic planning, grandiosity | E2 self-transitions inflated; E3 produces unreachable viability trajectories |
| Noisy | Variable, unpredictable capacity | Chronic fatigue, chronic pain, episodic illness | E2 self-transition model trained on inconsistent data; capacity estimates unreliable across days |

The pessimistic direction is particularly important: **avoidance, agoraphobia, and
learned helplessness may be E2 failures rather than E3 over-valuations of harm**.
The standard cognitive framing — the patient overestimates threat — aims treatment at
E3's harm evaluation. But if E2's capacity model is degraded (I cannot do what is
required to be safe), E3's output is not biased — it is responding correctly to a
broken capacity input. Correcting E3's output directly (cognitive restructuring) will
fail if E2 remains inaccurate.

### Developmental Etiology (INV-064)

Both failure modes have a developmental pathway: **early-life disruption of E1 and E2
differentiation constrains E3 training quality permanently**. E3 trains on E1/E2 outputs.
If those outputs carry low information during the critical developmental window, E3 learns
to evaluate degraded inputs — and its harm/goal representations are noise-fitted to the
actual structure of the world.

Early-life adversity that disrupts sensory schema formation (sensory deprivation, trauma
that narrows the experienced world, chronic unpredictability that prevents schema
stabilisation) therefore does not merely cause emotional injury. It degrades the
representational substrate from which coherent goals and accurate capacity estimates can
ever be drawn. The downstream effects on executive function and goal-directed behaviour
persist into adulthood not because of stored trauma but because E3 was trained on
impoverished inputs.

This is consistent with the empirical finding that early adversity produces deficits in
goal-directed behaviour and executive function that are disproportionate to, and
dissociable from, the emotional sequelae of the same adversity.

### Treatment Implications

The treatment target for Mode A (MECH-214 failure) is **E1 schema enrichment**:
expanding the experiential vocabulary, building representational differentiation.
Novel high-entropy environments, arts, movement, practices developing fine perceptual
discrimination, and (carefully) psychedelic experiences that temporarily dissolve
existing schema boundaries can expand the space of coherent goals available to E3.
This is not symptom management — it is enlarging the space from which goals can form.

The treatment target for Mode B pessimistic direction (MECH-215 failure) is **E2
self-transition recalibration via action in the world**. This is why exposure-based
therapies show consistent superiority over purely cognitive approaches in phobias and
PTSD. Cognitive restructuring addresses E3's harm estimates directly; exposure-based
therapy rebuilds E2 self-transitions through direct experience of what the agent can
actually do. The capacity model is updated from below, not argued into shape from above.

Somatic and interoception-focused therapies (body-based trauma approaches, movement
practices, breathwork) operate at the correct architectural level: they rebuild E1
self-schemas (who I am, what my body is) and E2 self-transitions (what I can do)
directly, restoring the preconditions for coherent agency rather than targeting E3
output.

### Claims Covered

| ID | Label | Failure type |
|----|-------|-------------|
| INV-064 | e1_e2_e3_maturational_sequence_necessity | Developmental: E3 cannot train on degraded E1/E2 inputs |
| MECH-214 | goal_referent_e1_representability | Mode A: goal content requires E1 schema differentiation |
| MECH-215 | self_model_prerequisite_for_agentive_prediction | Mode B: goal pursuit requires E1 self-schema + E2 capacity model |

---

## Catatonia, Subtype II: Harm-Stream Lock-In (SD-036, MECH-279)

> **Registered 2026-04-22 from V3-EXQ-471 exemplar.** Distinct from MECH-202 Direction B
> ("commit-gate paralysis"). The two subtypes share the surface phenomenology — sustained
> motor immobility despite preserved consciousness — but differ in proximal mechanism.

### The exemplar

V3-EXQ-471 (full-stack agent fishtank showcase, seed 0, episode 0) produced a clean
catatonia trace. The agent began the episode with apparently competent goal-directed
behaviour (ate food, navigated to resources). After encountering a hazard (`harm_signal =
-0.084` at t=0), behaviour collapsed:

- **Mode locked to `avoid` for all 200 steps.** No flip back to a goal-seeking mode.
- **Action locked to motor `2` for all 200 steps** — single repeated motor command.
- **Position stuck at `[2,1]` for 194 consecutive steps** (`world_change_norm = 0`).
- **Energy fell from 0.99 to 0.00 by t=110**, then remained at 0 for 90 more steps with
  no mode flip and no homeostatic rescue.
- **`harm_signal` returned to 0 at t~10**, but `z_harm_norm` stayed pinned at ~0.7 for
  the remaining 190 steps. The harm latent was self-sustaining absent input.
- **`z_beta_val` flat at ~0.0019** for all 200 steps. The bistable beta gate (MECH-090) was
  not oscillating.
- **`n_cands = 32` every step.** Candidacy gating was not pruning.

Not the MECH-202B failure: the commit gate was not "frozen at maximum threshold" — the
agent *was* committing, repeatedly, to the same evade action. The lock was upstream of
the commit gate, in the harm-stream representation feeding it.

### Mechanism

Three architectural absences compound:

1. **No harm-stream decay regulator.** SD-010/SD-011 integrate harm input but contain no
   mechanism by which the absence of harm over time drives `z_harm` back toward baseline.
   A single harm event therefore produces a permanently elevated harm latent, which biases
   mode arbitration toward `avoid` indefinitely.

2. **No homeostatic priority override.** SD-012 (drive-modulated goal seeding) requires
   `benefit_exposure > 0` to seed `z_goal`. In `avoid` mode the agent does not approach
   resources, so `benefit_exposure` stays at zero. Drive saturates as energy depletes, but
   has no authority to override mode lock and force approach.

3. **No anchor reset criterion.** The hippocampal proposer (MECH-269) has no signal that
   says "the situation has changed; re-anchor on a new world state." The proposer keeps
   producing trajectories anchored on the t=0 harm event, even as 190 quiet steps
   accumulate. Each proposal is a variation on "evade the threat from the original frame."

The single-action repetition is the policy reading a frozen state vector and emitting the
deterministic best response to it. From the agent's internal point of view, t=200 still
*is* t=0.

### Distinction from MECH-202 Direction B

| Feature | MECH-202B (commit-gate paralysis) | SD-036/MECH-279 (harm-stream lock) |
|---|---|---|
| Commitment behaviour | Gate never fires; endless re-evaluation | Gate fires repeatedly; same action |
| z_harm trajectory | Variable; not the locus of failure | Pinned high without input |
| Action diversity | Variable (no commit reached) | Single action repeated |
| Mode behaviour | Variable | Locked in `avoid` |
| Treatment target | Lower commit threshold; pretend-play calibration | Restore decay; restore homeostatic override; anchor reset |
| Clinical analogue | Severe indecision; rumination-loop catatonia | Stupor/freeze catatonia; PTSD-adjacent immobility |

These are *different routes to the same surface*. Treating one as the other will fail.
The MECH-202B treatment (lowering commit threshold) would, on an SD-036/MECH-279 agent,
*accelerate* the lock — more rapid commitment to the same evade action.

### Clinical mapping

The clinical picture this matches is the **stuporous / akinetic catatonia** seen in:

- Severe melancholic depression with psychomotor freeze
- Post-traumatic immobility (the "frozen" pole of PTSD)
- Some neuroleptic malignant / catatonic spectrum presentations
- Anti-NMDA-receptor encephalitis catatonia (where GABAergic regulation is disrupted)
- Lethal catatonia of the Stauder type (sustained autonomic activation + immobility)

The shared signature is **sustained autonomic activation (z_harm-equivalent elevated)
without behavioural exit** — distinct from the *resistive* catatonia of MECH-202B
(rumination, indecision, gate paralysis).

The clinical observation that **benzodiazepines (GABAergic agonists) are first-line for
this catatonia subtype** is the empirical hook for SD-036: the missing decay regulator is
GABAergic. Restoring GABAergic tone allows `z_harm` decay to proceed, which unlocks mode
arbitration. By the same logic, ECT — which produces broad GABAergic and homeostatic
recalibration effects — is second-line and works on the same architectural target from a
different angle.

### What SD-036 and MECH-279 commit to

**SD-036 (gabaergic.cross_stream_decay_regulator):** A regulatory layer that applies
exponential decay to specified latent streams in the absence of input, with the decay rate
itself modulated by a tonic GABAergic level. Stream coverage at minimum: `z_harm` (both
sensory and affective per SD-010/SD-011), `z_beta` (precision-weighting), and possibly the
drive accumulator. Architectural commitment: decay is a property of a *regulatory layer
that touches multiple streams*, not a property of each stream's update rule. This predicts
that GABAergic disturbance produces **simultaneous failures across streams** — matching the
clinical observation that benzodiazepine withdrawal, GABA-A receptor antibodies, and other
GABAergic insults produce clusters (catatonia + autonomic dysregulation + perceptual
changes + sleep disruption) rather than isolated single-stream failures.

**MECH-279 (pag.gabaergic_freeze_gate):** PAG-analog gating of the freeze response
specifically. When `z_harm` × duration crosses threshold, the system commits to freeze
(motor immobility + sustained autonomic activation). Exit from freeze requires GABAergic
decay to complete via SD-036. Failure of this exit pathway produces sustained freeze even
after the precipitating harm has passed. The fact that the freeze response itself is
GABA-mediated (calming -> immobilization is one mechanism, not two) is the clinical hook —
the same neurotransmitter system that initiates freeze is responsible for terminating it,
and disturbance produces stuck-in-freeze.

### Predictions

1. **Adding SD-036 to the V3 substrate should resolve the EXQ-471 lock pattern** without
   any other change. Specifically, with a `z_harm` decay rate tuned so the latent returns
   to baseline within 30–50 quiet steps, the seed-0 ep-0 trace should show mode flip from
   `avoid` back to a goal-seeking mode by ~t=50.

2. **Adding SD-036 alone should not rescue seeds 1 and 2** (the more severely degraded
   seeds), because their failure has additional contributors. This is a substrate-readiness
   test, not a single-cause test.

3. **A homeostatic-override mechanism (separate, see homeostatic_override_litpull
   session prompt) is required to fully prevent the SD-036-rescued agent from
   re-locking** under sustained threat with depleting energy. SD-036 provides decay; the
   override provides authority for hunger to outweigh threat when survival demands it.

4. **MECH-269 anchor-reset criteria** (see hippocampal_anchor_selection.md) must specify
   conditions under which the proposer re-anchors despite a sustained mode. Without this,
   even a decayed `z_harm` may leave the proposer producing stale trajectories from the
   original harm anchor.

### Claims Covered

| ID | Label | Role |
|----|-------|------|
| SD-036 | gabaergic.cross_stream_decay_regulator | Substrate: cross-stream decay layer with GABAergic gain |
| MECH-279 | pag.gabaergic_freeze_gate | Freeze response gating with same GABAergic substrate |

**Updated claims:**
- MECH-202: noted as a *distinct* catatonia subtype (commit-gate paralysis) from the
  harm-stream lock subtype documented here. Both are real; treatment differs.

---

## Hyperarousal Insomnia and Schema-Repair Starvation (MECH-286, MECH-285, MECH-094)

### The exemplar

A trauma-exposed patient (combat veteran, assault survivor, ICU survivor with
post-intensive-care syndrome) presents with chronic insomnia: cannot initiate sleep
despite exhaustion, frequent nocturnal awakening with full alertness, intrusive
ruminative imagery on attempted sleep onset, no recoverable dream-narrative content
in the morning. Daytime computation appears intact in the consulting room — language,
working memory, planning all measure within normal limits. But the patient describes
deteriorating performance on novel tasks at work, increasing rigidity in familiar
routines, and a sense that "nothing new sticks." Standard hypnotics (z-drugs,
short-acting benzodiazepines) produce sedation but not restoration: the patient
sleeps and still wakes feeling unrested. Standard SSRI augmentation does not
durably help.

This is not depression-with-insomnia (the depressive-maintenance loop INV-054).
It is not the harm-stream catatonic subtype (SD-036 / MECH-279) — the patient is
*hyper*-active not hypo-active. It is not MECH-202 frame-tag failure — reality
testing is intact. The architectural account REE owes is: the agent's offline
schema-repair pipeline is being starved of the offline phase it requires to run.

### Mechanism

The cluster involves three interacting failures, each separately documented:

1. **Saturated MECH-286 override (sleep-onset gate stays high)**: under chronic
   threat re-experiencing, SD-037 `override_signal` does not relax. The
   wake-stability arm of orexin keeps the agent above `theta_sleep_permit`. Sleep
   onset is suppressed.

2. **MECH-284 staleness accumulator continues to fill**: waking experience continues
   to deposit V_s residuals (the schema's running record of "this prediction did
   not match"). Under chronic novel-and-unprocessed input, this accumulator grows
   monotonically. There is no clearance pathway in waking — clearance requires
   the offline replay readout (MECH-285).

3. **MECH-285 priority readout never fires (or fires degraded)**: because MECH-286
   never permits sleep onset, the priority readout that would consume the staleness
   tags never runs. Schema regions with the most accumulated "this is wrong"
   evidence are never replayed, never re-aggregated by the sleep-half of MECH-273,
   and the schema does not update.

The compounding result is **schema-repair starvation**: novel input continues to
deposit residuals that never clear, the schema becomes progressively more
mis-fitted to the world the agent is currently in, and waking computation becomes
progressively more rigid (defaulting to old-schema responses because the new-schema
update never lands). This is a slow-motion failure: a single missed night does not
produce it; weeks-to-months of pinned override do.

### The PTSD-chronicity architectural account

Acute PTSD has a recoverable trajectory in many patients. Chronic PTSD does not.
REE's account of the difference is a co-failure pattern across this cluster:

- **MECH-285 priority loss alone** → degraded but not absent schema repair;
  emotionally salient events still get dopaminergically tagged for replay;
  recoverable.
- **MECH-094 hypothesis-tag loss alone** → simulated content can no longer be
  distinguished from real content; replay events can intrude as flashbacks; but
  the schema can still update if MECH-285 is intact, eventually integrating the
  trauma narrative; recoverable.
- **MECH-286 saturation alone** → acute insomnia, daytime exhaustion, but on a
  reasonable timescale (days) the override relaxes and sleep is restored;
  recoverable.
- **All three jointly (MECH-286 saturated + MECH-285 priority lost + MECH-094
  tag dysfunctional)** → the staleness tag accumulates from the traumatic
  episode but never gets cleared, because (i) the priority signal that should
  pull it into replay is broken, (ii) the override signal that should permit
  the offline phase is pinned, and (iii) the replay that does manage to occur
  cannot update the schema because simulated and real are conflated.

The chronic phenotype is the joint failure. This is consistent with the clinical
observation that PTSD chronicity correlates with persistent sleep architecture
disruption and that interventions which restore sleep architecture (prazosin for
nightmares, sleep-targeted CBT) move some patients out of chronicity even when
the explicit trauma-processing arm has stalled.

### Distinction from depressive-maintenance loop (INV-054)

INV-054 is a goal-pipeline failure (terrain-maintenance MECH-186, gain MECH-187,
goal-persistence MECH-188 collectively underactive). Its phenotype is anhedonic
withdrawal, low arousal, motivational poverty. The hyperarousal-insomnia cluster
is the *opposite* arousal sign: SD-037 override is *over*-active, drive-coupled
arousal is *over*-recruited via MECH-281, and the failure is in the offline
recovery pipeline rather than the waking goal pipeline.

Both can co-occur (depression with hyperarousal-insomnia is common) but they are
architecturally distinct and should respond to distinct interventions:
- INV-054 → serotonergic gain restoration, behavioural activation
- This cluster → sleep architecture restoration; in V3, predicted to require
  damping of the override signal under conditions where threat context has
  attenuated but the override has not relaxed (orexin-receptor antagonist
  literature; suvorexant/lemborexant clinical signal in chronic insomnia)

### Distinction from acute insomnia

A single bad night, jet lag, exam stress: the override is transiently elevated
but relaxes within days; MECH-284 staleness has not yet accumulated to clinically
significant levels. The architectural cluster only produces the schema-repair-
starvation phenotype under *sustained* override saturation, on the order of
weeks-to-months.

This timeline matches the clinical timeline: acute insomnia is common and
self-limiting; the cognitive deterioration profile only emerges in chronic
hyperarousal states.

### Predictions

1. **Override-relaxation interventions (orexin-receptor antagonist analogs)
   should restore schema-repair function** even without targeting the trauma
   narrative directly. Specifically: in a V3 agent with pinned override and
   accumulated MECH-284 staleness, pharmacological-analog damping of the
   override signal should permit sleep-mode entry, MECH-285 priority firing,
   and observable clearance of the staleness map across cycles.

2. **MECH-286 saturation should be diagnostically distinguishable from
   MECH-281 cataplexy** despite sharing an upstream substrate (orexin-analog).
   Both predicted to co-occur clinically (narcolepsy with cataplexy) but
   pharmacological dissociation possible: agonising the motor-coupling axis
   without affecting the sleep-state axis, or vice versa, should produce
   selective rescue of one phenotype.

3. **Chronic schema-repair starvation should produce a characteristic cognitive
   profile**: preserved working-memory and crystallised performance, degraded
   novel-stimulus learning, degraded schema flexibility on tasks requiring
   updating of prior beliefs. This is dissociable from the depressive cognitive
   profile (which shows generalised slowing) and from substance-induced
   cognitive impairment (which shows acute attention deficits). The signature
   is *learning failure under preserved performance*.

4. **Time-course prediction**: in a V3 agent with chronically pinned override,
   the deterioration in schema fit on novel inputs should follow a predictable
   accumulation curve (roughly linear in number of cycles with high MECH-284
   deposition and no MECH-285 firing), distinguishable from the step-function
   degradation produced by acute substrate damage.

### Claims Covered

| ID | Label | Role |
|----|-------|------|
| MECH-286 | sleep.override_gated_state_transition | Sleep-onset recruitment authority, the failing component when over-saturated |
| MECH-285 | hippocampal.sleep_consolidation_priority_from_v_s_residuals | The offline-phase readout that is never recruited |
| MECH-284 | hippocampal.v_s_residual_schema_staleness_accumulator | The waking-phase accumulator that fills without clearance |
| MECH-094 | hypothesis_tag_routing | Co-failure that converts the cluster into chronic-PTSD architecture |
| MECH-281 | orexin.drive_arousal_coupling | Sibling axis (motor-coupling); co-lesioned in narcolepsy/cataplexy but dissociable in this insomnia phenotype |
| SD-037 | broadcast.override_regulator | Substrate: the override signal whose pinning produces the cluster |

---

## Narcolepsy and Cataplexy: Bilateral Orexin-Loss Failure (MECH-281, MECH-286)

> A note on scope: REE does not partition disorders into "psychiatric" and
> "neurological" in the way clinical specialty boundaries do. The split is
> institutional, not architectural — narcolepsy and cataplexy involve the same
> regulatory substrate (SD-037 override layer) as the insomnia, depressive, and
> PTSD-chronicity failure modes already documented here. We document them in
> this file because they share the substrate and because the architectural
> account *unifies* what specialty boundaries fragment.

### The exemplar

A patient (typically adolescent or young adult) presents with two symptom clusters
that conventional nosology treats as a single syndrome (narcolepsy with cataplexy)
but which REE's architecture treats as two dissociable failures of the same
upstream substrate:

- **Sleep-state instability**: irresistible sleep attacks during the day even in
  alerting contexts (driving, conversation, eating); fragmented nocturnal sleep
  with frequent awakenings; sleep-onset REM (collapse of the normal NREM-first
  architecture); hypnagogic and hypnopompic hallucinations (REM-content intrusion
  into wake transitions); sleep paralysis (REM motor atonia outlasting the sleep
  state).
- **Cataplexy**: sudden bilateral loss of muscle tone triggered by emotional input
  (laughter, surprise, anger), preserved consciousness throughout, lasting seconds
  to minutes. The emotional state is computed normally — the patient laughs, then
  loses motor recruitment.

Standard treatment recognises both clusters but treats them with separate agents
(modafinil/sodium oxybate for sleep stability; venlafaxine/clomipramine for
cataplexy via REM-suppression). The architectural account should explain why one
substrate lesion produces two clinically separable phenotypes treated with
different drugs.

### Mechanism

Narcolepsy with cataplexy is, architecturally, the bilateral failure of the
SD-037 orexin-analog override at its two principal downstream targets:

1. **MECH-286 axis (wake-stability gate)** fails → loss of `theta_sleep_permit`
   gating. Sleep-mode entry can occur without staleness demand, without
   permissive threat context — the agent transitions to offline mode at
   inappropriate times. Sleep architecture also degrades because the same
   override signal stabilises the wake state against premature REM intrusion;
   when override is absent, REM can intrude on wake (hypnagogic hallucinations,
   sleep paralysis).

2. **MECH-281 axis (drive-arousal coupling)** fails → drive_level and
   emotional/affective input still compute (the patient feels the surprise,
   feels the joke is funny) but they fail to recruit the motor-pipeline gain
   needed to maintain postural tone. The architectural signature is
   *recruitment failure under preserved upstream computation* — exactly what
   distinguishes cataplexy from a primary motor disorder.

The two axes are **dissociable in principle but co-lesioned in practice** when
the substrate (SD-037) itself is damaged, because both downstream gates are
fed by the same override signal. This is the architectural prediction of the
clinical co-occurrence pattern: the substrate lesion explains why *both*
phenotypes appear, and the dissociable downstream targets explain why each
phenotype responds to a different pharmacological intervention.

### Dissociation predictions

The architecture is falsifiable through the dissociation pattern:

1. **Selective MECH-286 lesion (sleep-state instability without cataplexy)**:
   should be observable in early/prodromal narcolepsy patients before cataplexy
   onset, in narcolepsy type 2 (without cataplexy), and in some idiopathic
   hypersomnia presentations. The architectural prediction: a partial or
   selective failure of the sleep-state gating axis without the motor-coupling
   axis.

2. **Selective MECH-281 lesion (cataplexy without narcolepsy)**: rarer but
   reported as "isolated cataplexy" in case-series. Architectural prediction:
   selective failure of the drive-arousal coupling axis without the sleep-
   state axis. Should respond to MECH-281-targeted intervention without sleep-
   architecture restoration.

3. **Substrate-level lesion (full narcolepsy with cataplexy)**: orexin neuron
   loss as in narcolepsy type 1 / Hcrt-deficient cases. Both axes co-lesioned.
   This is the most common clinical presentation precisely because substrate
   damage is more common than selective downstream-target damage.

4. **V3 substrate prediction**: in a V3 agent with SD-037 implemented, lesioning
   the override_signal at source should produce both sleep-state instability
   and drive-arousal decoupling. Lesioning at the MECH-286 readout while
   preserving the MECH-281 readout should produce sleep-state instability only.
   Lesioning at the MECH-281 readout while preserving MECH-286 should produce
   cataplexy-analog motor decoupling only. This three-arm dissociation is the
   architectural test.

### Distinction from related failure modes

- **vs MECH-202 catatonia (commit-gate paralysis)**: catatonia is a *commit*
  failure (cannot initiate or terminate motor sequences); cataplexy is a
  *recruitment* failure (cannot maintain motor tone despite intact emotional
  computation). Catatonia patients do not show emotional-trigger pattern;
  cataplexy patients do. Different substrate, different intervention.

- **vs SD-036 / MECH-279 catatonic harm-stream lock**: that is a stream-level
  pinning failure under intact regulatory machinery; this is a regulatory
  machinery failure under intact streams. The harm-stream-lock patient is
  *immobile and silent*; the cataplexy patient is *hypotonic but alert and
  communicating*.

- **vs hyperarousal-insomnia (preceding section)**: the *opposite* failure
  mode of MECH-286 — saturated rather than absent. Both phenotypes share a
  substrate (SD-037 override) and they sit at opposite ends of its operating
  range, predicting that interventions which restore mid-range function (rather
  than purely up-regulating or down-regulating) should help both. This is
  consistent with the modafinil-and-sodium-oxybate combination in narcolepsy
  (selectively targeting different parts of the operating curve).

- **vs primary REM-sleep behaviour disorder (RBD)**: RBD is REM motor atonia
  failure during sleep (acting out dreams); cataplexy is REM motor atonia
  *intrusion* into wake. Architecturally both involve atonia-gate dysregulation
  but at different state transitions. RBD is plausibly a separable claim cluster
  not yet registered in REE.

### What this places in REE

This failure mode adds the *positive lesion* clinical evidence anchor for
SD-037: narcolepsy with cataplexy is the natural lesion experiment that the
architecture predicts should produce bilateral phenotype, and the clinical
literature confirms this pattern. The dissociation predictions above sharpen
the SD-037 claim from "there exists an override regulator" to "the override
regulator has at least two dissociable downstream readouts (MECH-281, MECH-286)
which can fail jointly under substrate damage and selectively under downstream-
target damage".

The point about psychiatric/neurological boundaries: a regulator-layer failure
that produces depression-like phenomena (hyperarousal-insomnia, schema-repair
starvation) when saturated and produces narcolepsy/cataplexy when absent is,
mechanistically, a *single* dysregulation surface viewed from two clinical
specialties. The REE architecture commits to that unification — the same
SD-037 → {MECH-281, MECH-286} substrate failure space generates both clinical
clusters depending on whether the failure is over- or under-recruitment, and
whether the downstream targets fail jointly or selectively.

### Predictions

1. **Pharmacological dissociation tests**: agents acting selectively on the
   MECH-286 axis (sleep-state stability) should rescue sleep architecture
   without rescuing cataplexy, and vice versa. The current clinical landscape
   already shows this dissociation (modafinil/sodium oxybate vs anti-cataplectic
   antidepressants); the architecture predicts the dissociation rather than
   merely accommodating it.

2. **Prodromal MECH-286 signal in prodromal narcolepsy**: sleep-state
   instability should be detectable architecturally before cataplexy onset,
   consistent with clinical observation that hypersomnia often precedes
   cataplexy by months to years.

3. **Co-lesioning prediction in iatrogenic / immune-mediated cases**:
   autoimmune-mediated orexin neuron loss (the established etiology in
   narcolepsy type 1) should produce roughly synchronous emergence of both
   axes' phenotypes, distinguishable from selective downstream-target damage
   which should produce one phenotype and not the other.

4. **V3 substrate experiment**: a three-arm lesion in a V3 agent with SD-037
   implemented (substrate-source lesion vs MECH-286-only lesion vs
   MECH-281-only lesion) should produce the three predicted phenotype
   patterns above. This is the architectural validation experiment for the
   downstream-readout dissociability claim.

### Claims Covered

| ID | Label | Role |
|----|-------|------|
| SD-037 | broadcast.override_regulator | Substrate: the override layer whose source-level damage produces full narcolepsy-with-cataplexy |
| MECH-286 | sleep.override_gated_state_transition | Wake-stability axis: selective failure produces sleep-state instability without cataplexy |
| MECH-281 | orexin.drive_arousal_coupling | Motor-coupling axis: selective failure produces cataplexy without sleep-state instability |

---

## OCD: A Three-Layer Architectural Failure (SD-034, MECH-260, MECH-266, SD-045, SD-046)

*Consolidated 2026-04-28 from the four-pull architectural-question chain. Earlier framing in
`docs/thoughts/2026-04-20_ocd1.md` through `ocd4.md` (goal-side reading); this section adds
the chunk-side and multi-goal-arbitration readings that emerged from the action-policy
decomposition lit-pull (`evidence/literature/targeted_review_action_policy_decomposition/`)
and the type-prototype follow-on (`docs/thoughts/2026-04-28_action_policy_and_multi_goal.md`).*

### The exemplar

Compulsive hand-washing, ordering rituals, checking behaviours, intrusive doubts that cannot
be released even when the patient agrees they are unfounded. Two phenomenological hallmarks:
(a) an active goal that the patient cannot release ("I have to be sure my hands are clean"
won't yield to "I have washed three times, I will be late for work"); (b) a stereotyped
action sequence that, once entered, plays out to a fixed completion that exceeds what the
goal would justify (a single thorough washing becomes a 20-minute ritual). Egodystonia is
common: the patient knows the goal is over-weighted, knows the ritual is excessive, and
still cannot interrupt either.

The 2026-04-20 ocd1-ocd4 thought files framed OCD as goal-side over-binding -- inability
to release the active goal slot. This is correct but incomplete. Graybiel 2008 (Annu Rev
Neurosci, [DOI 10.1146/annurev.neuro.29.051605.112851](https://doi.org/10.1146/annurev.neuro.29.051605.112851);
indexed at `evidence/literature/targeted_review_action_policy_decomposition/`) frames OCD
compulsions and rituals as *runaway action chunking* -- the basal-ganglia chunk substrate
gets stuck in a self-reinforcing loop that the goal-release machinery cannot terminate
because the failure mode is on the action-chunk side, not the goal side. Both readings
are true; they describe two architectural layers that fail in characteristic combination.

### Mechanism

Three interlocking failure layers, each anchored to a distinct REE substrate:

**Layer 1 -- Goal-side over-binding (SD-034 closure operator failure).**
The current goal slot persists past the point where the closure operator would normally
fire. SD-034's five-part closure signal -- beta_gate.release, dacc.inject_nogo, residue
domain discharge, salience signal_event, dacc.reset_episode_pe -- depends on detecting
that the agent's rule-state is stable, beta gate is elevated, and the closure-domain
predicate is satisfied. In OCD, the closure-domain predicate is set so tightly (per
ocd4 over-bound mode-exit thresholds) that no realistic completion state crosses the
closure threshold. The goal does not release because the closure operator cannot fire.

**Layer 2 -- Chunk-side runaway (SD-045 action-chunk cache failure mode).**
Independent of the goal-side problem, the action-chunk substrate (when added) can enter
a self-reinforcing loop where successful execution of a cached chunk strengthens the
chunk's reinforcement signal via MECH-290 backward credit sweep, which raises its
priority for retrieval next tick, which favours re-invoking it. Without an explicit
chunk-level No-Go injection (the basal-ganglia task-bracketing-cell analogue), there
is nothing to attenuate the runaway. SD-034's MECH-260 No-Go injection currently fires
on action-class indexing at the dACC level; a chunk-side analogue is required to attenuate
runaway chunking specifically.

**Layer 3 -- Multi-goal-arbitration failure (SD-046 multi-slot GoalState absent).**
The patient cannot maintain a competing goal ("get to work") alongside the active goal
("be sure my hands are clean") because the GoalState is single-slot. There is no
substrate where the competing goal can sit in parallel and accumulate priority through
drive amplification, dACC arbitration, or MECH-266 asymmetric mode hysteresis. The
phenomenology of "I know I should stop but I can't switch" is, architecturally, "the
GoalState slot is occupied and there is no second slot for the alternative to compete
from."

In combination, the three layers explain the egodystonic quality of OCD: the patient's
*knowledge* that the ritual is excessive and the alternative goal is more important is
*not represented in the goal-arbitration system at all*. The cognitive evaluation is
present in higher-level frontal substrates (SD-033b OFC analogue, SD-033c vmPFC
analogue) but cannot be translated into goal-arbitration action because there is no
multi-slot GoalState to receive the alternative. Goal-side closure cannot fire because
the rule-state never stabilises in the over-bound mode-exit-threshold regime. Chunk-
side runaway proceeds because the chunk substrate has no goal-independent No-Go.

### Distinction from related failure modes

**vs GAD-like state (z_harm_a elevated, z_goal intact):**
GAD has goals that get *interrupted* by threat responses; OCD has goals that *cannot be
released*. GAD is engagement-with-derailment; OCD is engagement-with-non-termination.
The architectural difference is in which mechanism fails: GAD fails the AIC urgency-
interrupt threshold (SD-032c) or the harm-driven mode switch (MECH-091); OCD fails the
closure-domain predicate (SD-034) and the chunk No-Go (SD-045 missing).

**vs catatonia subtype II (SD-036 / MECH-279 harm-stream lock-in):**
Catatonia has freeze-state persistence with elevated z_harm_a sustaining the freeze
gate; OCD has goal-state persistence with the closure operator failing to fire.
Catatonia is motor-suppression locked open; OCD is motor-execution locked into a
specific cached sequence. Both show "stuck" phenomenology but at different substrate
layers -- one is PAG-analogue motor gating, the other is goal-arbitration plus chunk
cache.

**vs psychosis / delusion (MECH-094 hypothesis-tag failure, MECH-201 synthetic-real
confusion):**
Delusion is about *what the agent believes*; OCD is about *what the agent does despite
its beliefs*. The MECH-094 / MECH-201 framing is at the latent-stream level (frame-tag
errors); OCD is at the action-arbitration level (goal release plus chunk cache). The
patient with OCD has correct frame tags -- they know the threat is unfounded -- and the
failure is downstream of belief.

### Clinical mapping

| OCD phenomenology | Architectural locus |
|---|---|
| Inability to release current goal | SD-034 closure-operator threshold over-tightened (Layer 1) |
| Stereotyped ritual sequence | SD-045 action-chunk cache runaway (Layer 2) |
| Inability to switch to competing task | SD-046 multi-slot GoalState absent (Layer 3) |
| Egodystonia (knowing the ritual is excessive) | Higher cognitive evaluation (SD-033b/c) intact but cannot reach goal-arbitration without Layer 3 |
| Resistance escalates ritual length | Layer 2 chunk-cache runaway: blocked execution increases reinforcement on completion |
| Comorbid OCD + tic disorder | Layer 2 chunk-cache failure shared substrate: tics are sub-second motor chunks; OCD compulsions are second-to-minute behavioural chunks; same runaway primitive at different timescales (Graybiel 2008) |
| Symptom heterogeneity (washers vs checkers vs orderers) | Different chunk-cache content with shared Layer 1 + Layer 3 vulnerability |
| Familial / heritable component | Vulnerability is in substrate-level parameters (closure threshold, chunk-cache update rule, goal-slot capacity) more than in any specific symptom-content trace |

### What the substrates commit to

- **SD-034 closure operator** (V3 implemented): the closure-domain predicate threshold
  is the parameter that distinguishes healthy goal-release from over-binding. EXP-0156
  (V3-EXQ-460) and EXP-0162 (V3-EXQ-466) validate the substrate; the OCD failure mode
  is what happens when the predicate is set too tight relative to the rule-state
  variance.
- **MECH-260 No-Go injection** (V3 implemented): the goal-side No-Go that currently
  fires on dACC arbitration. The OCD-specific extension is a chunk-side No-Go
  (Layer 2) that fires when a chunk has been re-executed beyond a context-dependent
  count threshold. Currently absent in V3.
- **MECH-266 asymmetric mode hysteresis** (V3 implemented): per-mode enter / exit
  thresholds. OCD over-binding is the case where exit threshold is set extremely low
  (the current mode must collapse to near-zero probability before leaving). Already
  implemented; V3-EXQ-464 (smoke-PASSed all sub-tests) validates substrate; OCD
  behavioural validation deferred to V3-EXQ-464b when the dual-resource environment
  variant lands.
- **SD-045 action-chunk cache** (V4 default, V3 PULL-FORWARD CONDITION):
  highest-priority candidate for V3 pull-forward if EXQ-495 successors surface
  monostrategy persistence. The chunk-cache failure mode (Layer 2) cannot be expressed
  without this substrate. Without it, REE can model the goal-side reading of OCD but
  not the chunk-side reading.
- **SD-046 multi-slot GoalState** (V4 default, V3 PULL-FORWARD CONDITION):
  second pull-forward candidate. The multi-goal-arbitration failure mode (Layer 3)
  cannot be expressed without this substrate. Without it, REE can model an agent that
  fails to release a goal but cannot model an agent that fails to switch to a competing
  goal -- the two are subtly distinct, and the second is the more clinically faithful
  reading.

### Predictions

1. **Closure-threshold sweep predicts symptom severity.** SD-034 closure-domain
   predicate threshold parameter, swept at fixed rule-state variance, should produce
   a continuous gradient from healthy goal-release to compulsive non-release. The
   sweep is the falsifiable test that the over-binding reading is parametric rather
   than categorical.
2. **Chunk-cache No-Go ablation produces comorbid tic-OCD signature.** With SD-045
   landed and a chunk-side No-Go added, ablating the No-Go selectively (leaving
   goal-side No-Go intact) should produce stereotyped ritual repetition with
   intact goal-arbitration -- pure compulsion without obsession. With ablation
   extended to multiple timescales of chunk cache, sub-second-chunk repetition
   surfaces as tic-like behaviour.
3. **Multi-slot vs single-slot ablation distinguishes "won't release" from
   "can't switch".** With SD-046 multi-slot GoalState landed, single-slot ablation
   in an environment with two equally-rewarded competing goals should produce
   pure non-switching behaviour even when closure operates correctly on the active
   slot. This dissociates Layer 1 (closure failure) from Layer 3 (multi-slot
   failure).
4. **SSRI augmentation pattern follows Layer 3 dependency.** SSRIs in clinical OCD
   produce gradual symptom improvement over 8-12 weeks. The architectural reading:
   tonic 5-HT (MECH-203 / MECH-187) modulates GoalState seeding gain; with chronically
   elevated 5-HT, the threshold for the alternative goal to enter a competing slot
   (when the slot exists, Layer 3) drops, allowing arbitration to start working
   again. This predicts that SSRI response in OCD should correlate with measures
   of competing-goal *availability* (was there an alternative the patient was
   ignoring?) more than with measures of compulsion *intensity*. Falsifiable in a
   naturalistic-data study or via an ecological-momentary-assessment trial.
5. **CBT exposure-response prevention works on Layer 1.** ERP forces the patient
   to experience the chunk-cache invocation followed by *failure to complete the
   chunk to its cached endpoint*. The architectural reading: ERP attenuates the
   chunk-cache reinforcement signal (Layer 2) and forces the closure operator to
   fire from a non-canonical termination state (Layer 1). This predicts CBT-ERP
   should be partially effective in single-slot architectures but maximally effective
   when combined with interventions that recruit competing goals (Layer 3) --
   e.g. CBT-ERP plus behavioural activation. Existing meta-analytic evidence
   supports this combined approach; the architectural account makes the dissociation
   testable in component analyses.

### Claims Covered

- SD-034 (governance.closure_operator) -- Layer 1 substrate
- MECH-260 (cingulate.dacc_bias_suppression) -- existing goal-side No-Go
- MECH-266 (cingulate.asymmetric_per_mode_hysteresis) -- mode-stickiness substrate
- SD-045 (bg.action_chunk_cache_dorsolateral_loop) -- Layer 2 substrate, V4 default with V3 pull-forward
- SD-046 (goal.multi_slot_state_per_goal_workstream) -- Layer 3 substrate, V4 default with V3 pull-forward
- MECH-187 / MECH-188 / MECH-203 (5-HT goal-pipeline gain) -- SSRI prediction substrate
- MECH-290 (hippocampal.backward_trajectory_credit_sweep) -- chunk reinforcement source
- SD-033b / SD-033c (PFC subdivisions) -- egodystonic-cognition substrate (intact in OCD)

### Claims NOT covered

- The vulnerability factor (heritability, prefrontal cortical thickness, striatal
  volume, etc.) is not modelled. The architectural account locates the failure
  parametrically (in closure threshold, chunk-cache update rule, multi-slot
  capacity) but does not commit to which biological mechanism sets those parameters
  developmentally.
- Pharmacological prediction (4) above is registered tentatively; entry into the
  PHARM-NNN registry pending review of clinical-trial literature on SSRI dose-response
  curves in OCD subtypes (washers vs checkers etc.).
- The relationship between OCD and OCPD (obsessive-compulsive personality disorder)
  is not modelled. OCPD's perfectionism / inflexibility may share Layer 1 / Layer 3
  failure modes at sub-clinical thresholds without the Layer 2 chunk-cache runaway.
  This is testable but not registered.

---

## Pharmacological Predictions Registry

The pharmacological / clinical-intervention predictions surfaced in the failure-mode
sections above are registered structurally in
`evidence/planning/pharmacological_predictions.v1.json`. Each PHARM-NNN entry is tagged
with the claim IDs it depends on, the phenotype it targets, the dissociation pattern the
architecture predicts, the falsification condition that would weaken the cited claims,
and the literature anchors (existing trials, naturalistic data, or studies the
architecture indicates are needed).

Relevant claims in `claims.yaml` carry a `pharmacological_predictions` field listing the
PHARM-IDs that depend on them. This is the first cycle of pharmacological-prediction
registry; governance review of these predictions against clinical literature is a
separate cycle from substrate-evidence governance and has not yet been instituted.

| PHARM ID | Intervention | Axis | Phenotype | Polarity |
|----------|-------------|------|-----------|----------|
| PHARM-001 | DORA class (suvorexant, lemborexant, daridorexant) | substrate (override damping) | hyperarousal-insomnia / schema-repair starvation | positive |
| PHARM-002 | modafinil, sodium oxybate | downstream sleep-state (MECH-286) | narcolepsy with cataplexy (sleep-attack endpoint) | positive |
| PHARM-003 | venlafaxine, clomipramine, anti-cataplectic SNRI/TCA | downstream motor-coupling (MECH-281) | narcolepsy with cataplexy (cataplexy endpoint) | positive |
| PHARM-004 | lorazepam, benzodiazepines | regulator-layer GABA (SD-036) | catatonia subtype II (harm-stream lock) | positive |
| PHARM-005 | prazosin (alpha-1 antagonist) | indirect override damping | PTSD nightmares + hyperarousal-insomnia | positive |
| PHARM-006 | SSRIs (sertraline, paroxetine) | regulator-layer 5-HT (orthogonal) | hyperarousal-insomnia / schema-repair starvation | **negative** |
| PHARM-007 | anticholinergics (oxybutynin, diphenhydramine, TCAs, paroxetine) | dual pathway (REM-suppression + diurnal cholinergic mimicry) | dementia conversion in MCI/older adults | **negative** |
| PHARM-008 | mirabegron (beta-3 agonist; non-CNS antimuscarinic alternative) | indication substitution (urinary urgency without ACh load) | dementia conversion in older adults on bladder anticholinergics | positive |
| PHARM-009 | benzodiazepines / Z-drugs (zolpidem, zopiclone) | regulator-layer GABA (architecture-disrupting at hypnotic dose) | dementia conversion via Phase 1/2 SWS suppression | **negative** (cf. PHARM-004 positive in catatonia -- same drug class, different phenotype) |
| PHARM-010 | DORA class for MCI/dementia | substrate (architecture-preserving sleep) | MCI/early-AD episodic decline rate | positive (sibling of PHARM-001) |
| PHARM-011 | trazodone 25-100mg (5-HT2A antagonism, sub-antidepressant dose) | downstream Phase 1/2 SWS enhancement | MCI/early-AD episodic decline rate | positive |
| PHARM-012 | mirtazapine, sertraline, escitalopram (low-REM-burden antidepressants) vs paroxetine/TCA/MAOI | antidepressant-class dissociation | dementia risk in long-term antidepressant users | positive (low-REM-burden) / negative (REM-suppressing) |
| PHARM-013 | ramelteon, melatonin-ER | upstream Phase 0 circadian restoration | MCI/early-AD episodic decline rate | positive |
| PHARM-014 | composite pipeline-rebuild dissociation (cross-class predictor) | falsifiable architecture test | reverse phase-dependency ordering of cognitive recovery | architectural |

The dementia/medications cluster (PHARM-007 to PHARM-014) is not a "psychiatric" failure
mode in the standard nosological sense — but the same scope note applied to narcolepsy
and cataplexy applies here: REE does not partition disorders into psychiatric and
neurological. Dementia is a sleep-pipeline failure mode under INV-046/047/048 with a
substantial pharmacological prediction surface; full mechanistic discussion lives in
[`sleep/medications_dementia.md`](sleep/medications_dementia.md).
