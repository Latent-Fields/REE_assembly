# Thought intake -- harm-source attention and aversive causal credit assignment

**Date:** 2026-09-26  
**Status:** intake / candidate refinement -- NOT yet registered  
**Origin:** user proposal during interpretation of V3-EXQ-1109: "The thing that harms perhaps deserves attention." Followed by targeted literature search and reconciliation against the current REE threat/orienting architecture.  
**Scope:** this is not a proposal to add a generic "fear module". It asks whether REE is missing, or has not yet integrated, the bridge by which a negative change in valued self-state recruits attention and causal credit toward the thing/action/context that produced it, allowing prospective threat learning.

---

## 1. Core thought

A representation that says **"I have been harmed"** is not the same representation as **"that thing is dangerous"**.

The V3-EXQ-1109 result makes this distinction operationally important. In that harness, `z_harm_a` is highly faithful to its own input, but that input is accumulated bodily damage rather than a direct representation of environmental threat proximity. A controller that consumes persistent damage as though it meant "an external threat is immediately present" can therefore remain defensive after the causal threat has disappeared.

The candidate missing bridge is:

```text
negative valued-self-state change
        -> interrupt / orient
        -> preserve a short causal eligibility window
        -> allocate attention to candidate causes
        -> assign aversive credit under uncertainty
        -> update world/context/action predictions
        -> future cue predicts harm before damage occurs
        -> context/imminence-dependent defence or avoidance
```

This suggests at least four semantically distinct quantities:

1. **Damage / injury state -- "I am harmed."** A relatively persistent internal/self-state representation. It can remain high after the external threat is gone.
2. **Aversive valence / teaching signal -- "that change was bad."** A phasic negative outcome or prediction-error-like signal that marks the event as important for learning.
3. **Threat / source prediction -- "this object, context, action or trajectory predicts future harm."** A world-facing, prospective representation with uncertainty and causal attribution.
4. **Defensive policy state -- "what should I do now?"** Freeze, withdraw, flee, orient, inspect, inhibit, or resume depending on predicted imminence, uncertainty, controllability and available actions.

On this view, **fear is not current bodily damage**. A fear-like state is a learned prospective consequence of a model that predicts damage from a cue/context/source. Immediate nocifensive withdrawal may be primitive; cue-specific anticipatory defence should be learned.

---

## 2. Literature support

The literature supports both the separation and the coupling proposed above.

### 2.1 Pain is multidimensional rather than one scalar

Pain research distinguishes sensory-discriminative information from affective-motivational and cognitive/evaluative components. This already argues against treating one accumulated harm magnitude as simultaneously injury state, threat identity and behavioural command.

### 2.2 Aversive bodily signals can act as teaching signals for threat memory

Han et al. (2015) identified a calcitonin gene-related peptide (CGRP) parabrachial-to-central-amygdala pathway that conveys affective pain information. Silencing it impaired both pain responses and threat-memory formation, whereas stimulation could produce defensive responses and threat memory. Ito et al. (2021) similarly showed parabrachial-to-amygdala transmission of aversive information that induces avoidance.

The important computational point is not the literal biological mapping. It is that **the adverse event supplies an instructive signal that can attach negative predictive significance to another representation**.

### 2.3 Prediction error changes what gets learned about

Aversive prediction-error signals are measurable in the amygdala, and associative-learning work shows that surprising outcomes change not only reinforcement but the *associability* of cues present around the event. Prediction error can therefore be interpreted as both "update value" and "pay more attention to the representations that may explain this outcome."

This is close to the user's proposal: a harmful outcome should create an epistemic/attentional demand to identify its source rather than merely increasing a global harm scalar.

### 2.4 Freezing can support information gathering

Roelofs and Dayan (2022) argue that freezing is not simply passive immobility: it can support evidence gathering, sensory optimization, response prevision and preparation for fight or flight. This is a useful distinction for REE. A short orienting arrest that improves source identification is computationally different from an indefinitely self-maintaining PAG-like freeze caused by persistent damage magnitude.

### 2.5 Learned threat should become prospective

In aversive conditioning, a formerly neutral cue can acquire the ability to capture attention and evoke defensive behaviour before the adverse event occurs. That is exactly the behavioural signature expected if REE has successfully converted "I was harmed" into "this predicts harm."

---

## 3. Reconciliation with current REE: pieces exist, bridge is uncertain

This thought should **not** be registered as "REE lacks orienting." The repository already contains relevant machinery.

| Existing REE piece | What it already does | What appears not yet established |
|---|---|---|
| `z_harm_a` / SD-011 | represents affective/accumulated harm content | V3-EXQ-1109 shows that in the current harness its content is body damage, not necessarily external threat; direct control use therefore risks semantic mismatch |
| SD-099 / MECH-489 defensive orienting | phasic harm/surprise can trigger orienting arrest; captures trigger `z_world`; releases after an identification-confidence process and biases approach/withdraw/resume | its "identification" is principally resolution of the trigger signal plus a captured location; an explicit posterior/credit assignment over candidate causes and a demonstrated learned threat predictor are not established |
| MECH-074d basolateral-amygdala analogue | harm prediction-error spike plus attribution can remap E1 ContextMemory; includes a trainable attribution head over `z_self`, `z_world`, `z_harm_a` | default-off / mixed evidence; not yet demonstrated as the causal bridge from SD-099-like orienting to later cue-specific prospective threat behaviour |
| MECH-357 instrumental avoidance | learns whether a directed action reduces harm | credits action efficacy/controllability; this is not the same as identifying the external/contextual source of harm |
| ARC-155 / ARC-156 | operating-point normalization and regime-independent escape evidence | orthogonal: these can repair scale and release while leaving the semantic/learning question unresolved |

The candidate gap is therefore best phrased as an **integration and causal-credit question**:

> Does a negative change in REE's valued self-state cause candidate world/action/context representations to receive transient attentional and learning priority, such that one or more of them becomes a prospective predictor of future harm?

The answer may ultimately be "yes, MECH-074d + SD-099 already contain the necessary machinery, but it is not integrated/active." That is a legitimate outcome and would make this an activation/integration requirement rather than a new mechanism.

---

## 4. Candidate hypothesis: harm-source attention / aversive causal credit assignment

**Working hypothesis, not a registered claim:**

When an unexpected negative change in valued self-state occurs, REE should generate an endogenous, non-oracular aversive teaching event that transiently increases attentional gain, associability and learning eligibility for recent candidate world states, entities, actions and contexts. Credit should be distributed according to evidence for causal/predictive relevance rather than assigned to an oracle-labelled hazard. Learning should then make the credited representation predict future harm, allowing defensive behaviour before fresh damage occurs.

The mechanism must permit uncertainty. A harmful event need not reveal its cause immediately. Candidate causes may compete, retain graded credit and be revised by later evidence.

---

## 5. Minimal architectural implication: integrate before adding a subsystem

A minimal implementation should first attempt to connect existing machinery rather than create a new monolithic module:

1. **Trigger** from an abrupt adverse event: aversive prediction error, phasic sensory-discriminative harm (`z_harm_s`), or a negative valued-self-state delta -- not simply persistent `||z_harm_a||`.
2. **Eligibility window** retaining recent `z_world`, entity/context representations, actions and trajectory states.
3. **Orienting/interruption** using SD-099-like machinery to protect sampling and model revision from ongoing action commitment.
4. **Candidate attribution** using temporal contingency, spatial/contextual continuity, action dependence, self/world attribution and counterfactual fit. MECH-074d is an obvious existing candidate surface.
5. **Memory/model write** into E1/hippocampal/context or another explicitly prospective threat-predictor representation.
6. **Prospective consumer**: amygdala/PAG/E3 defensive control should primarily respond to *predicted imminent harm/threat* rather than accumulated injury magnitude alone.
7. **Persistent damage remains meaningful** for recuperation, guarding, negative affect and self-preservation pressure even after acute threat prediction has fallen.

This preserves a useful dissociation: the organism can still be hurt while correctly judging that it is currently safe.

---

## 6. Non-oracularity and anti-overgeneralisation constraints

The mechanism must not receive the environment's true hazard label or a privileged "nearest hazard" oracle.

- Candidate causes come from information the agent actually had before/around the adverse event.
- Temporal eligibility must decay; otherwise every recent representation becomes permanently suspect.
- Ambiguous events should retain distributed uncertainty rather than force one source assignment.
- Self-caused and externally caused harm must be distinguishable where evidence permits.
- Harm omission, relief and safe re-exposure must be able to reduce erroneous threat credit.
- Orienting cannot simply increase gain on *everything*: successful learning must become more source-specific, not merely more anxious/global.
- The same immediate nocifensive response should remain possible when source attribution is ablated; attribution is predicted to matter most for subsequent prospective behaviour.

---

## 7. Candidate discriminating experiments

### A. Cue -> harm acquisition
Expose the agent to two perceptually comparable cues/contexts; only one reliably precedes harm. No hazard identity is supplied. After learning, the predictive cue should acquire disproportionate attention/threat value and produce avoidance **before** harm occurs.

**Falsifier:** behaviour remains purely post-damage, or avoidance generalises equally to both cues.

### B. Persistent damage / removed threat dissociation
Produce damage, then remove the causal threat while the internal injury representation remains elevated.

**Prediction:** acute freeze/escape pressure should fall with predicted threat, while negative valence/recuperation pressure can remain high.

**Falsifier:** any elevated injury representation obligatorily maintains acute external-threat defence.

### C. Source-representation intervention
Hold the adverse event constant but intervene on the candidate source representation during the attribution/write window.

**Prediction:** later cue-specific avoidance should follow the causally used source representation if aversive attribution is operative.

### D. Eligibility-window ablation
Ablate the short recent-state/action eligibility trace while preserving the immediate harm signal and nocifensive action.

**Prediction:** acute withdrawal survives, but later source-specific prospective avoidance is greatly weakened.

This is a particularly clean causal discriminator between "harm causes defence" and "harm teaches what to fear."

### E. SD-099 vs attribution ablation
Compare orienting-system ablation with attribution/write ablation.

- Orienting ablation should impair information gathering/source resolution.
- Attribution/write ablation should particularly impair later cue-specific avoidance even if the initial orienting arrest occurs.

A double dissociation would strongly support the decomposition.

### F. Omission / relief / safety learning
After a cue predicts harm, repeatedly present it without harm.

**Prediction:** negative aversive prediction error / safety evidence should reduce source threat credit, attentional capture and defensive response.

### G. Self-caused vs external harm
Match the magnitude of harm but cause it either through the agent's own selected action or an external event.

**Prediction:** credit should partition differently -- action-outcome efficacy/avoidance learning for the former, world-source/context warning for the latter.

---

## 8. What would falsify or absorb this thought

This thought should be weakened, absorbed or rejected if any of the following occurs:

1. Current REE already learns robust cue-specific, pre-harm avoidance and attention from adverse events, and causal intervention on SD-099/MECH-074d or the proposed eligibility bridge does not affect it.
2. MECH-074d already supplies the complete source-specific aversive credit path when enabled; in that case no new mechanism is needed and the result becomes an integration/default-on/readiness problem.
3. Adding source-directed attention fails to improve causal discrimination once ordinary prediction error and replay are controlled, or instead causes global overgeneralisation.
4. After correcting ARC-155 scaling and ARC-156 release conditions, direct bodily-damage-to-defence control performs as well or better across threat-removal and cue-learning tests, with no benefit from a separate prospective threat representation.
5. An alternative existing route is shown causally to perform the same credit assignment and prospective prediction, making the proposed bridge redundant.

---

## 9. Relation to the REE ethical programme

This thought sits most naturally under **A4 -- causal power and vulnerability** and **D2 -- model refinement**.

Vulnerability need not produce only negative utility or reflex withdrawal. A harmful change is evidence that the agent's model failed to predict or avoid a causally important event. It can therefore create an endogenous epistemic demand:

> Something changed my valued state for the worse; improve the model so that the relevant cause can be predicted before it happens again.

That is useful experimentally because it produces a sharp causal prediction. Ablate the harm-triggered attention/credit bridge and **immediate nocifensive behaviour should remain while source-specific prospective threat learning fails**. Restore it and the agent should increasingly react to predictors rather than waiting to be damaged.

This is a self-preservation/model-refinement mechanism, not yet a claim about responsibility for others or love. Its ethical relevance is that it makes vulnerability causally capable of reorganising the agent's model and future trajectories rather than existing only as a score.

---

## 10. Disposition / next audit

**Do not register a new claim yet.** First run a narrow architecture/trace audit asking whether current REE has an end-to-end path for:

```text
adverse self-state change
 -> phasic orienting/attention change
 -> candidate-source eligibility/binding
 -> source-specific persistent model update
 -> source-specific prospective threat prediction
 -> pre-harm defensive/avoidance behaviour
```

For each edge record: producer, representation semantics, consumer, default status, causal evidence domain, and whether the edge survives without oracle information.

Then classify the result as one of:

- **integration refinement:** SD-099 + MECH-074d already provide the pieces but are not causally joined;
- **semantic split requirement:** injury state and threat prediction need explicitly separate representations/consumer contracts;
- **new mechanism:** a genuine aversive causal-credit/associability bridge is absent.

The highest-value immediate question is therefore not "should REE get a fear module?" but:

> **After harm occurs, what representation in REE gets blamed -- and does that representation later make the organism afraid before it is harmed again?**

---

## 11. Literature anchors

- Auvray M, Myin E, Spence C. *The sensory-discriminative and affective-motivational aspects of pain.* Neuroscience & Biobehavioral Reviews (2010). https://pubmed.ncbi.nlm.nih.gov/18718486/
- Han S, Soleiman MT, Soden ME, Zweifel LS, Palmiter RD. *Elucidating an Affective Pain Circuit that Creates a Threat Memory.* Cell (2015). https://pubmed.ncbi.nlm.nih.gov/26186190/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4512641/
- Ito M, Nagase M, Tohyama S, et al. *The parabrachial-to-amygdala pathway provides aversive information to induce avoidance behavior in mice.* Molecular Brain (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8223383/
- McHugh SB, Barkus C, Huber A, et al. *Aversive Prediction Error Signals in the Amygdala.* Journal of Neuroscience (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4078079/
- Holland PC, Schiffino FL. *Prediction errors, attention and associative learning.* Neurobiology of Learning and Memory (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4862921/
- Roelofs K, Dayan P. *Freezing revisited: coordinated autonomic and central optimization of threat coping.* Nature Reviews Neuroscience (2022). https://www.nature.com/articles/s41583-022-00608-2
- Moscarello JM, Penzo MA. *The central nucleus of the amygdala and the construction of defensive modes across the threat-imminence continuum.* Nature Neuroscience (2022). https://www.nature.com/articles/s41593-022-01130-5
- Koller D, et al. Review of sensory-discriminative versus affective-motivational pain processing and network separation. See PubMed search trail from the intake literature pull; use primary/review source verification before claim promotion.

### Literature interpretation boundary

The cited biology supports the **computational decomposition** -- aversive event, attention/associability, associative threat memory, defensive-state selection -- but it does not establish that REE should literally reproduce the named mammalian nuclei or neurotransmitter pathways. The architectural hypothesis is about causal function and separable representations, not neuroanatomical mimicry.
