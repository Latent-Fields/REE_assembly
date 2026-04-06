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
