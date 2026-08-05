# Thought Intake: Epistemic Deficit and Orienting as an Information-Seeking Drive

Status: processed

Processed in:
- docs/claims/claims.yaml#MECH-482
- docs/claims/claims.yaml#MECH-483
- docs/claims/claims.yaml#Q-089

**Date:** 2026-08-05  
**Original status label:** Candidate architectural and developmental intake  
**Scope:** Information need, uncertainty, curiosity, boredom, orienting, prediction failure, learning progress, replay, and developmental competence acquisition  
**Related mechanisms:** MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-320, ARC-065, SD-070, E1 prediction machinery, hippocampal proposal generation, residue, and replay  
**Likely version:** Conceptual registration now; implementation should probably follow V3 closure unless a minimal diagnostic is cheap and directly relevant to competence acquisition.

---

## 1. Core intuition

There is a familiar internal state that is not well captured by novelty alone:

> I do not know, and this unresolved absence of knowledge continues to bother me.

This state differs from noticing something new, behaving randomly, enjoying stimulation, seeking ordinary reward, or responding only to immediate prediction error.

It is a persistent motivational deficit generated when the organism judges that its current model is inadequate.

The candidate REE hypothesis is:

> **Information insufficiency can function as an interoceptive-like deficit. Curiosity, investigation, orienting, questioning, observation, and replay are behaviours used to reduce that deficit.**

The proposed underlying drive may be called:

- epistemic deficit;
- information need;
- model insufficiency;
- unresolved uncertainty drive.

Curiosity should remain the name of one behavioural expression rather than the entire drive.

---

## 2. What REE already contains

REE does not lack curiosity machinery.

### MECH-313 — stochastic noise floor

Maintains behavioural variation and prevents complete policy collapse. This permits exploration but does not direct it toward useful information.

### MECH-314a — novelty curiosity

Favours unfamiliar candidate states or regions.

This answers:

> What have I not encountered?

Novelty is not equivalent to ignorance. A familiar situation may remain poorly understood, while a novel stimulus may be trivial and irrelevant.

### MECH-314b — uncertainty curiosity

Uses uncertainty to increase exploratory preference.

In the existing curiosity intake, its current implementation is described as a global scalar rather than a fully candidate-specific signal.

This begins to answer:

> Where is my prediction uncertain?

It does not yet necessarily create an accumulating, self-maintaining need state.

### MECH-314c — learning-progress curiosity

Tracks whether prediction error is changing.

This distinguishes potentially learnable uncertainty from irreducible noise.

It answers:

> Where does further engagement appear capable of improving my model?

### MECH-320 — tonic vigour

Promotes action rather than passivity. This can help curiosity produce behaviour but is not itself an information need.

### ARC-065 — behavioural diversity

Coordinates stochasticity, structured curiosity, and vigour so that the agent generates varied experience from which rules and competence may be learned.

This is an important upstream condition for learning, but behavioural diversity is not equivalent to experiencing inadequate knowledge as a deficit.

---

## 3. The possible missing layer

The current curiosity family primarily modulates:

- which candidates are attractive;
- whether behaviour remains diverse;
- whether action occurs;
- whether unfamiliar or learnable regions are sampled.

The proposed missing construct is a persistent internal variable representing the adequacy of the agent's model.

Candidate name:

`epistemic_deficit`

It should rise when:

- important predictions repeatedly fail;
- action selection is blocked by unresolved uncertainty;
- competing models remain unresolved;
- a salient causal question remains open;
- an important outcome occurs without an adequate explanation;
- the agent encounters novelty relevant to harm, goals, self-maintenance, or social prediction;
- replay repeatedly fails to reconcile an inconsistency.

It should fall when:

- uncertainty relevant to the unresolved issue is reduced;
- prediction becomes reliably calibrated;
- a causal distinction is learned;
- a useful rule is acquired;
- the environment becomes controllable enough for competent action;
- the system establishes that the uncertainty is currently irreducible or irrelevant.

The signal should therefore encode neither raw novelty nor raw error.

A possible conceptual form is:

```text
epistemic_deficit
    = unresolved_importance
    × uncertainty
    × expected_resolvability
    × persistence
    - verified_resolution
    - irrelevance
    - accepted_irreducibility
```

No exact equation should be adopted before the components are operationally defined.

---

## 4. Why this may be drive-like

A drive has more structure than an immediate reward bonus.

A genuine information-need drive should possess at least some of the following properties:

1. **Accumulation** — unresolved important uncertainty should continue to exert pressure rather than disappearing after one action-selection cycle.
2. **Satiation** — obtaining explanatory or decision-relevant information should reduce the state.
3. **Specific appetite** — the drive should preferentially seek information capable of resolving the deficit, rather than arbitrary novelty.
4. **Competition with other drives** — epistemic need should enter arbitration alongside harm avoidance, ordinary goals, rest, commitment, and vigour.
5. **Anticipatory quenching** — predicted access to reliable information may partially reduce epistemic pressure before learning is complete.
6. **Rebound or persistence** — suppressed unresolved uncertainty may reappear during replay, idle periods, or renewed task relevance.
7. **Developmental calibration** — young agents may require stronger epistemic pressure, greater tolerance of uncertainty, and stronger exploratory behaviour than mature agents.
8. **Pathological extremes** — too little pressure may produce incuriosity and developmental stagnation; too much may produce compulsive exploration, inability to commit, distraction by uncertainty, or noisy-television behaviour.

---

## 5. Distinguishing related constructs

### Novelty

Have I encountered this before?

Novelty can be high even when no useful learning is possible.

### Uncertainty

How variable or unreliable is my prediction?

Uncertainty can be high because of irreducible noise.

### Prediction error

Was this particular prediction wrong?

Prediction error may be transient and need not indicate a persistent knowledge deficit.

### Learning progress

Is my prediction improving?

Learning progress helps distinguish productive from unproductive uncertainty.

### Epistemic deficit

Is my current understanding inadequate for something that matters, and does that inadequacy remain unresolved?

### Curiosity

What behaviour should I perform to reduce this epistemic deficit?

### Boredom

Is the current information environment failing to offer sufficient useful novelty, uncertainty reduction, or learning progress?

Boredom may therefore be a low-information-density manifestation of epistemic deficit, whereas directed curiosity is a deficit attached to a particular unresolved question.

---

## 6. Primitive behavioural modes: orient as a third regime

Observations from mammalian behaviour and emerging REE behaviour suggest that a more primitive behavioural regime may precede directed curiosity.

Rather than only two primary behavioural modes:

- approach;
- avoid;

there may be a third:

- **orient / survey.**

This regime is characterised by a temporary reduction in commitment while the organism acquires information sufficient to determine what should subsequently be approached or avoided.

Its functional purpose is not immediate reward. Its purpose is to improve the organism's situational model.

### Candidate behavioural characteristics

During orient mode the organism may:

- widen behavioural sampling;
- increase environmental observation;
- reduce premature commitment to a single policy;
- gather landmarks and contextual information;
- estimate uncertainty;
- identify potential opportunities and hazards;
- establish a better world model before acting.

The resulting behaviour should therefore appear exploratory without being random.

### Relationship to curiosity

Curiosity may be a later developmental refinement of orienting.

```text
uncertain situation
        ↓
   orient / survey mode
        ↓
identification of unresolved question
        ↓
 directed curiosity
        ↓
information-gathering behaviour
        ↓
updated world model
        ↓
approach / avoidance / commitment
```

Under this view:

- orienting is broad;
- curiosity is targeted;
- epistemic deficit determines how strongly orienting or curiosity should persist.

### Relationship to existing REE mechanisms

Orient mode may emerge from interaction between:

- MECH-313 stochastic behavioural variation;
- MECH-314 structured curiosity;
- MECH-320 tonic vigour;
- uncertainty estimation;
- weak action dominance within arbitration.

It therefore need not require a wholly separate architectural subsystem.

Instead, it may represent a characteristic global behavioural regime generated when information acquisition temporarily dominates exploitation.

### Experimental prediction

Survey behaviour should be distinguishable from random exploration.

Evidence supporting orient mode would include:

- increased state coverage;
- structured rather than random trajectories;
- improved later policy quality;
- increased information gain;
- termination once uncertainty falls.

Evidence against the hypothesis would include:

- random wandering without improved competence;
- persistent orienting despite adequate information;
- no measurable benefit to later action selection.

---

## 7. Relevance to the recent competence split

V3-EXQ-875a and V3-EXQ-882a suggest that some seeds enter a competent regime while others do not.

A possible developmental hypothesis is:

> Successful seeds develop an adequate information-seeking loop early enough to acquire useful world structure, while unsuccessful seeds fail to generate or sustain the experiences needed to close their model deficits.

This is only one hypothesis among several.

The observed split could still arise from:

- environmental difficulty;
- initialisation effects;
- premature deaths;
- exploration lock-in;
- curriculum timing;
- interactions among the world model, bias head, orbitofrontal-style devaluation, and policy learning.

However, the existing curiosity machinery makes information-seeking a plausible contributor.

The critical question is not simply whether successful seeds visit more states.

It is whether they:

- encounter informative transitions earlier;
- respond more strongly to unresolved prediction failures;
- enter orient mode before premature commitment;
- return to learnable uncertainty;
- avoid perseverating on irreducible noise;
- use replay to consolidate unresolved but tractable structure;
- reduce uncertainty before competence acquisition.

---

## 8. Architectural proposal

Do not initially add a wholly separate large module.

A conservative implementation path would extend the existing curiosity stream.

### 8.1 Epistemic-deficit accumulator

Maintain a bounded state reflecting unresolved, consequential, potentially resolvable uncertainty.

Possible inputs:

- candidate-specific predictive uncertainty;
- persistent prediction error;
- disagreement between predictive systems;
- failure of current plans;
- unresolved causal alternatives;
- low model confidence in harm-relevant states;
- failed replay resolution;
- competence-blocking uncertainty.

### 8.2 Question or target binding

A global "I do not know" scalar is insufficient.

The deficit should be attached to:

- a region;
- a transition class;
- an object;
- a goal;
- a hazard;
- a causal hypothesis;
- eventually, a self-state or other-agent model.

This produces:

```text
epistemic deficit
    + target identity
    + estimated resolvability
    + relevance
    + age
```

### 8.3 Candidate generation

The hippocampal or planning system should be able to propose information-gathering actions specifically relevant to a live deficit.

Examples:

- approach for better observation;
- inspect from a safe distance;
- try an action that discriminates between causal models;
- revisit a region where learning was progressing;
- seek another agent likely to possess relevant information;
- defer action until sufficient evidence is available.

### 8.4 Arbitration

Epistemic deficit should have genuine but limited causal authority.

It must not automatically override:

- imminent harm;
- strong commitments;
- exhaustion or resource collapse;
- already sufficient information;
- evidence that the uncertainty is irreducible.

### 8.5 Residue and replay

Unresolved epistemic deficits should leave inspectable traces.

Replay should preferentially process experiences that are:

- surprising;
- unresolved;
- consequential;
- potentially learnable;
- capable of discriminating between live models.

Resolution should reduce both the deficit and future replay priority.

---

## 9. Developmental hypothesis

The epistemic drive may be especially important during early REE development.

Candidate developmental sequence:

1. Novelty and stochastic exploration generate varied experience.
2. Diffuse uncertainty recruits orient / survey mode.
3. Prediction failures create target-bound epistemic deficits.
4. Curiosity directs behaviour toward potentially resolving evidence.
5. Learning progress identifies productive regions.
6. Replay consolidates useful structure.
7. Resolved structure supports competence and reduces diffuse uncertainty.
8. Mature information seeking becomes more selective and goal-sensitive.

This suggests a developmental Goldilocks zone:

- **Too little epistemic pressure:** insufficient exploration and weak competence acquisition.
- **Moderate pressure:** orienting, directed information seeking, and reliable learning.
- **Excessive pressure:** instability, compulsive exploration, failure to commit, or attraction to endless uncertainty.

This should not be inferred from the earlier V3-EXQ-590 novelty Goldilocks lineage. That experiment concerned novelty-channel weight and was rendered non-contributory by missing causal authority. A developmental epistemic-drive experiment would be a separate question.

---

## 10. Candidate falsifiers

The hypothesis would be weakened if:

- epistemic-deficit variation does not alter information-seeking behaviour;
- raw novelty predicts exploration just as well as the richer construct;
- uncertainty reduction occurs without any persistent deficit state;
- the accumulator remains high after verified resolution;
- the system prefers irreducible noise over learnable uncertainty;
- curiosity behaviour does not improve competence acquisition;
- successful and unsuccessful developmental seeds show no difference in information-seeking trajectories;
- the same effects are fully explained by ordinary external reward;
- apparent orienting is indistinguishable from random wandering or indecision.

The hypothesis would gain support if:

- unresolved consequential uncertainty accumulates across time;
- obtaining diagnostic information specifically quenches the state;
- the state directs behaviour toward information rather than reward;
- candidate-specific deficits predict chosen information-gathering actions;
- orient mode improves later action selection and terminates after uncertainty reduction;
- moderate epistemic pressure improves competence acquisition across seeds;
- excessive or absent pressure impairs development in distinguishable ways;
- replay selectively resolves deficits and reduces later exploration of solved questions.

---

## 11. Minimal experimental sequence

### Experiment A — Orient versus random exploration

Create conditions in which the agent begins with weak action dominance and incomplete situational information.

Compare:

- baseline;
- stochastic exploration only;
- structured orient / survey mode.

Primary measures:

- state coverage;
- trajectory structure;
- observation-before-commitment;
- information gain;
- later decision quality;
- termination after uncertainty falls.

Prediction:

A true orient mode should improve subsequent action selection rather than merely increasing entropy.

### Experiment B — Deficit versus novelty

Create conditions separating:

- novel but irrelevant information;
- familiar but poorly understood information;
- uncertain but irreducibly noisy information;
- uncertain and learnable information.

Prediction:

A true epistemic-deficit system should prefer consequential, learnable uncertainty rather than novelty alone.

### Experiment C — Satiation

Allow an unresolved uncertainty to persist, then provide diagnostic evidence.

Measure whether:

- the internal deficit rises;
- orienting or information-gathering behaviour appears;
- the deficit falls after resolution;
- related exploratory behaviour diminishes.

### Experiment D — Developmental competence acquisition

Across many seeds, manipulate epistemic-drive authority during early acquisition:

- low;
- moderate;
- high.

Hold mature evaluation constant.

Primary outcome:

- proportion of seeds acquiring transferable competence.

Secondary outcomes:

- time to competence;
- early state coverage;
- prediction-error trajectories;
- replay content;
- survival;
- policy entropy;
- commitment stability;
- frequency and timing of orient mode.

### Experiment E — Irreducible-noise trap

Provide a noisy source that remains unpredictable and a structured source whose uncertainty can be reduced.

Prediction:

Learning-progress-sensitive epistemic need should eventually abandon the noisy source and prefer the learnable one.

---

## 12. Version placement

This concept is relevant to V3 because competence acquisition and curiosity already exist there.

However, the full drive may become clearer in V4, when REE has a richer self-model capable of representing:

> My model is inadequate.

It becomes still more important in V5, when deficits may concern other minds:

- What does this other agent know?
- Why did it act that way?
- What state is it in?
- Can it teach me?
- Does my model of its pain or goals remain uncertain?

The information drive could therefore become one bridge from individual cognition to social cognition, imitation, teaching, and language.

---

## 13. Provisional conclusion

REE already possesses novelty, uncertainty, learning-progress, stochasticity, and vigour mechanisms.

The candidate missing element is not another curiosity bonus.

It is an inspectable, persistent, target-bound state of epistemic insufficiency:

> **The nagging experience that something important remains unknown.**

A related primitive behavioural regime may already be visible:

> **Orient / survey: broad, structured information acquisition before approach, avoidance, or commitment.**

The scientific question is whether giving this state and regime bounded causal authority improves development, competence, and adaptive information seeking without producing compulsive uncertainty pursuit.

This should be registered as a candidate extension and compared carefully against the simpler explanation that the existing MECH-314 curiosity family is sufficient once made fully candidate-specific and behaviourally effective.
