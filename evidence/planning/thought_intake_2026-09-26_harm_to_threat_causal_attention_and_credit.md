# Thought intake -- harm-to-threat causal attention and credit assignment

**Date:** 2026-09-26
**Status:** intake / candidate refinement; **NOT yet registered as a new claim** pending overlap adjudication against SD-099, MECH-074d, ARC-155/156 and the current harm-stack work.
**Origin:** user observation after V3-EXQ-1109 that bodily harm should plausibly drive immediate defensive primitives and negative affect, but that the *thing that caused the harm* may also deserve privileged attention so that the organism can learn fear/avoidance of the cause.
**Immediate empirical trigger:** V3-EXQ-1109 (`v3_exq_1109_pag_freeze_veto_earliest_edge`) showed that `z_harm_a` is highly faithful to its own input (mean held-out encoder-fidelity R² ~0.992) while only weakly/variably tracking hazard proximity, because in this harness `harm_obs_a` is a 7-d accumulated body-damage stream. The PAG freeze gate simultaneously sat above its exit operating point across sampled states. This makes a semantic distinction between **injury state** and **predicted external threat** load-bearing rather than cosmetic.

---

## 1. Core thought

A harm system should not be a single scalar or latent that is asked to mean all of the following at once:

1. **damage / bodily state:** "I have been harmed";
2. **negative affective value:** "this change/state is bad for me";
3. **threat prediction:** "this object/place/action/context predicts future harm";
4. **source attribution:** "this particular thing/action/event probably caused the harm";
5. **defensive control:** "freeze / withdraw / flee / inspect / fight / continue";
6. **learning priority:** "the recent causes and cues around this event deserve extra model update and memory strength".

The recent V3 result is compatible with REE currently giving a representation of **injury** to machinery that sometimes treats it as a representation of **immediate threat**. Persistent damage is not equivalent to persistent imminent danger. A wounded organism may continue to hurt after the predator, hazardous tile or damaging action is gone; conversely, a learned threat cue can predict danger before any current bodily damage exists.

The candidate missing bridge is therefore not another generic harm encoder and not a hard-coded "fear module". It is a **non-oracular harm-to-cause attention and credit-assignment operation**:

> A sufficiently unexpected negative change in valued self-state should transiently increase attention, eligibility and learning pressure on candidate world-states, entities, contexts and actions that could have caused it.

In compact form:

```text
negative self-state change / aversive prediction error
    -> interrupt + orient
    -> preserve recent causal eligibility window
    -> increase associability/attention of candidate causes
    -> compare candidate causal explanations
    -> bind harm expectation to the best-supported cause/context
    -> store/update predictive threat representation
    -> future cue predicts harm before damage occurs
    -> select defensive policy according to imminence, controllability and affordance
```

This turns "harm happened" into "learn what is dangerous" without supplying the answer as an oracle.

---

## 2. Literature support

### 2.1 Aversive events act as teaching signals, not merely reflex triggers

Johansen, Tarpley, LeDoux & Blair (2010) showed that aversive unconditioned-stimulus responses in both lateral amygdala and periaqueductal gray (PAG) are reduced when the aversive outcome becomes expected, and that PAG inactivation attenuates the amygdala unconditioned-stimulus response and impairs acquisition of fear conditioning. This supports a role for PAG-linked aversive signals as **instructive signals for learning**, not only as output commands for defensive behaviour.

- Johansen JP, Tarpley JW, LeDoux JE, Blair HT. *Neural substrates for expectation-modulated fear learning in the amygdala and periaqueductal gray.* Nature Neuroscience. 2010;13:979-986. DOI: 10.1038/nn.2594. PMID: 20601946. https://pubmed.ncbi.nlm.nih.gov/20601946/

Iordanova et al. (2021) review causal and recording evidence for appetitive and aversive prediction error across PAG, amygdala, hippocampus, cortex, locus coeruleus/noradrenaline and dopamine systems. The important architectural point for REE is that aversive prediction error is distributed across **learning, attention and defensive circuitry**, rather than belonging to a single "fear" variable.

- Iordanova MD, Yau JO-Y, McDannald MA, Corbit LH. *Neural substrates of appetitive and aversive prediction error.* Neuroscience & Biobehavioral Reviews. 2021;123:337-351. DOI: 10.1016/j.neubiorev.2020.10.029. PMID: 33453307. https://pubmed.ncbi.nlm.nih.gov/33453307/

### 2.2 Surprise changes what receives attention and future learning credit

The Pearce-Hall family of learning results is especially relevant to the user's "the thing that harms perhaps deserves attention" proposal. Holland & Schiffino (2016) review evidence that prediction error changes **cue associability**: surprising delivery or omission of an outcome increases subsequent processing and learning about cues that were present around the surprising event. Central amygdala (CeA) circuitry is implicated in this surprise-induced increase in associability.

This is close to the computational operation REE appears to need: an adverse prediction error should not simply raise a global harm scalar; it should alter **which representations are eligible for learning**.

- Holland PC, Schiffino FL. *Mini-review: Prediction errors, attention and associative learning.* Neurobiology of Learning and Memory. 2016;131:207-215. DOI: 10.1016/j.nlm.2016.02.014. PMID: 26948122. https://pubmed.ncbi.nlm.nih.gov/26948122/

The distinction is useful:

- a Rescorla-Wagner-like operation changes associative strength because the outcome was surprising;
- a Pearce-Hall-like operation changes the **learning rate / attentional eligibility of the cues** around the surprise.

REE may need both. The present thought is primarily about the latter: *harm should focus learning onto candidate causes*.

### 2.3 Threat learning builds predictive cue representations that can precede damage

Levy & Schiller (2021) explicitly frame threat processing as a sequence spanning first encounter, learning and storage of cues that predict danger, updating those associations, and choosing actions. Their review argues against studying "threat" as one isolated computation. This strongly supports separating current injury from learned prediction of future injury.

- Levy I, Schiller D. *Neural Computations of Threat.* Trends in Cognitive Sciences. 2021;25(2):151-171. DOI: 10.1016/j.tics.2020.11.007. PMID: 33384214. https://pubmed.ncbi.nlm.nih.gov/33384214/

A useful REE interpretation is:

```text
pain/damage = adverse outcome / teaching event
fear-like state = learned anticipation that some cue/context/action predicts that outcome
```

Thus "fear" need not be primitive. Primitive machinery can consist of aversive valuation, phasic orienting/defence, eligibility/attention, causal attribution and associative updating. A fear-like anticipatory state can emerge when the predictive model learns the relationship.

### 2.4 Threat also recruits orienting machinery

Koller et al. (2019) found human evidence that individual differences in a superior-colliculus -> pulvinar -> amygdala pathway predicted behavioural orienting bias toward threatening visual stimuli. This does not establish the entire causal-learning loop, but it supports the general division between **rapid orienting to potentially important threat information** and slower identification/model updating.

- Koller K, Rafal RD, Platt A, Mitchell ND. *Orienting toward threat: Contributions of a subcortical pathway transmitting retinal afferents to the amygdala via the superior colliculus and pulvinar.* Neuropsychologia. 2019;128:78-86. DOI: 10.1016/j.neuropsychologia.2018.01.027. PMID: 29410291. https://pubmed.ncbi.nlm.nih.gov/29410291/

This supports a staged architecture in which an organism can first say, in effect, **"something important happened there"**, before it knows exactly what the source was.

---

## 3. Reconciliation with existing REE architecture

This thought initially looked like "REE is missing orienting." That is **too broad and would duplicate existing work**.

### SD-099 already owns phasic defensive orienting

`docs/architecture/sd_099_defensive_orienting_response.md` already implements a candidate pipeline:

```text
surprise / phasic harm onset
    -> orienting arrest
    -> identification-confidence accumulation
    -> release
    -> approach / withdraw / resume bias
```

It was explicitly created because earlier REE traces lacked a pathway from sudden unexpected harm/surprise to arrest and reorientation. It consumes `residue_surprise` and phasic `z_harm_s`, and is kept separate from chronic PAG freeze.

Therefore the present thought should **not** register "harm causes orienting" as a new claim.

### MECH-074d already owns part of causal attribution/remapping

`docs/architecture/sd_035_amygdala_analog.md` gives BLAAnalog a remap operation (MECH-074d) that requires both a harm prediction-error spike and a predictor-attribution head selecting candidate latent codes. This is importantly close to the current thought.

However, the present proposal appears to add a missing **cross-mechanism contract**:

1. SD-099 can notice/arrest/reorient;
2. MECH-074d can attribute a harm prediction error to candidate codes and issue a remap;
3. hippocampal/E1 machinery can store contextual/world representations;
4. E3 can evaluate trajectories;
5. **but it is not yet established that a real harm event causes selective attention/eligibility to the responsible world representation, creates a durable source-specific threat prediction, and then changes future behaviour *before another harm event occurs*.**

The candidate gap is therefore the **harm -> source-specific learning bridge**, not any one of those components in isolation.

### Relation to ARC-155 / ARC-156

The distinction also sharpens the current operating-point work:

- **ARC-155:** even a semantically correct control signal needs endogenous scale/operating-point regulation.
- **ARC-156:** strong regimes require termination evidence they do not themselves suppress.
- **This thought:** scaling and termination cannot solve a signal whose *semantic role is wrong*. Injury magnitude, threat imminence, cause identity and negative valence are related but non-interchangeable variables.

The V3-EXQ-1109 finding is therefore a useful example of the already-noted signal-validity principle: `z_harm_a` can be a high-fidelity representation of its input while still being the wrong quantity for a particular consumer.

---

## 4. Candidate architectural decomposition

The following decomposition should be treated as a hypothesis to test, not as an implementation prescription.

### H1 -- damage state must remain distinct from threat prediction

Maintain a representation of current/persistent self damage or suffering. It should influence negative valence, self-preservation pressure, recovery/guarding and perhaps vigour.

It should **not by itself mean that an external threat is currently present**.

### H2 -- aversive prediction error should open a causal eligibility window

When a negative self-state change exceeds what the current model predicted, REE should preserve a bounded recent window containing at least:

- recent `z_world` / object or location representations;
- recent actions / committed trajectory;
- salient contextual state;
- any already-active entity or schema hypotheses.

The harm event increases the temporary **associability / update priority** of these representations.

This is an attentional-learning primitive, not a source oracle.

### H3 -- candidate causes should compete for credit

The system should estimate which eligible representation best explains the self-state change. Candidate evidence could include:

- temporal proximity;
- counterfactual prediction (would harm have been predicted without this candidate?);
- recurrence across experiences;
- action contingency;
- spatial/object continuity;
- existing world-model causal predictions;
- self-vs-world attribution where available.

The output should be a distribution or confidence over candidate causes, not necessarily a winner-take-all label.

### H4 -- credited causes should become predictive threat representations

The attributed object/place/action/context should acquire an association with expected future harm. On later perception, it should be able to increase predicted harm **before current damage rises**.

This is the point at which a fear-like state can emerge as learned anticipation.

### H5 -- defensive policy should consume predicted threat, not raw injury alone

Freeze / withdrawal / escape / orienting should be selected from variables such as:

- predicted near-term harm;
- threat imminence;
- uncertainty / identification confidence;
- escape affordance and controllability;
- current injury and capacity;
- available actions.

Persistent bodily damage can modulate these quantities, but should not be treated as a synonym for external threat.

---

## 5. Minimal V3 test that would distinguish this idea

A useful experiment should avoid building an elaborate new system first. It should ask whether the **existing SD-099 + MECH-074d + hippocampal/E1 machinery already closes the loop** when wired and trained appropriately.

### Environment

Use a small world containing at least:

- two discriminable candidate cues/objects/locations that are often co-present;
- only one of them causally produces damage;
- occasional harmless exposure to both;
- a contingency reversal or relocation phase;
- enough action choice that anticipatory avoidance is measurable before contact.

No direct hazard identity is supplied to the agent.

### Conditions

1. **Current stack / control** -- ordinary harm learning without special post-harm associability manipulation.
2. **Orienting-only** -- SD-099 active, but no selective credit/learning boost to candidate causes.
3. **Causal-attention bridge** -- on an unexpected negative self-state transition, preserve the recent eligibility window and transiently raise learning/encoding weight for candidate causes; let existing attribution machinery choose which code(s) receive the update.
4. **Broadcast control** -- apply the same total learning gain indiscriminately to all recently active world representations. This is essential: improvement from merely "learning harder after harm" is not evidence for causal attention.

### Primary outcomes

A successful bridge should produce **source-specific anticipatory learning**:

- after limited harmful encounters, the agent avoids or changes trajectory around the harmful cue *before* receiving new damage;
- the neutral co-present cue acquires substantially less avoidance value;
- when contingencies reverse, attention/learning reopens and the threat association updates;
- the learned representation predicts harm better than current body-damage magnitude alone;
- ablation of the bridge removes or slows anticipatory source-specific avoidance while preserving immediate nociceptive/defensive response to actual damage.

### Causal tests

The strongest test is not behavioural appearance but intervention:

- ablate the post-harm associability boost;
- scramble which eligible candidate gets credit;
- replace selective credit with equal broadcast gain;
- preserve credit but block hippocampal/E1 write;
- preserve memory but block its later access to E3 threat/trajectory evaluation.

These interventions should fail at different stages if the proposed chain is real.

---

## 6. Falsifiers / ways this thought could be wrong

This idea should be rejected or narrowed if any of the following occur:

1. **Existing loop already sufficient.** When SD-099, MECH-074d and the existing learning/memory paths are activated under a valid harm representation, REE already shows rapid source-specific anticipatory avoidance and appropriate reversal without adding any new attentional/credit mechanism.
2. **Selective attention gives no advantage.** A causal-attention condition does not improve source specificity, sample efficiency or reversal relative to a matched broadcast-learning-gain control.
3. **Threat learning does not require post-harm orienting.** Source-specific prediction emerges equally when the orienting/arrest stage is ablated, implying the required credit assignment already occurs elsewhere.
4. **Attribution is not the bottleneck.** Candidate causes are correctly identified in telemetry, but the representation never changes future E1/E3 predictions or behaviour. The missing edge would then be downstream consumption rather than attention/credit assignment.
5. **Representation is the bottleneck.** The world model does not carry stable cue/entity/context identity well enough for source-specific credit. In that case the thought is directionally correct but premature; the prerequisite is representation/identity, not a new learning gate.
6. **Defensive behaviour is entirely explained by operating-point repair.** Correcting ARC-155/156 issues yields anticipatory, source-specific threat behaviour without any special harm-linked associability change. Then the proposed mechanism would be unnecessary for V3, though it might remain a biological refinement.

---

## 7. Novelty / registration recommendation

**Do not immediately mint a broad new claim.** Much of the apparent idea is already distributed across existing REE machinery:

- SD-099: phasic surprise/harm -> defensive orienting;
- MECH-074d: harm prediction error + predictor attribution -> selective remap;
- MECH-074a/b: arousal-linked encoding/retrieval modulation;
- existing hippocampal/E1 machinery: context and world memory;
- E3/residue: future trajectory cost/avoidance;
- ARC-155/156: operating-point and regime-exit correctness.

The genuinely novel candidate is narrower:

> **Unexpected negative self-state change should transiently increase the learning eligibility/associability of candidate causal world representations, and the resulting source attribution should be converted into a durable predictive threat association that can influence behaviour before recurrent damage.**

Before registration, audit whether MECH-074d's attribution head plus SD-099 already instantiate this exact causal chain end-to-end. If they do, this intake should become a **wiring/validation plan** rather than a new mechanism claim. If they do not, the missing bridge deserves a narrowly scoped mechanism or substrate decision rather than another generic "harm" claim.

Candidate working names if a new entry is required:

- `harm.causal_associability_gate`
- `threat.source_specific_credit_assignment`
- `aversive_prediction_error.causal_attention_bridge`

The last is probably the clearest description of the proposed computational role.

---

## 8. Ethical relevance

This is not merely a threat-avoidance optimisation. It maps cleanly onto REE's ethical foundation.

A4 (causal power and vulnerability) means the agent can be changed for the worse by the world. D2 (model refinement) then implies more than recording the negative state: the agent should improve the model that explains **what caused the harmful change**.

Thus vulnerability can generate an epistemic obligation internal to the organism:

> "Something changed my future possibilities for the worse; identify the cause well enough to predict and avoid repetition."

That is a useful bridge between self-preservation and learning without inserting an externally authored rule saying which things are dangerous.

It also creates the substrate needed later for ethically richer attribution. Before REE can distinguish accidental, environmental, self-caused and other-agent-caused harm, it first needs a non-oracular mechanism that binds adverse consequences to candidate causes at all.

---

## 9. Bottom line

The literature supports the user's intuition in a fairly precise form:

- aversive events are **teaching signals** as well as triggers of defence;
- prediction error changes **attention/associability** of cues around surprising outcomes;
- threat is a **learned predictive relation** between cues/context/actions and future harm, not the same variable as current bodily damage;
- rapid threat orienting and slower causal/model learning can be distinct stages;
- REE already contains pieces of this loop, so the likely problem is **cross-component causal closure**, not wholesale absence of threat machinery.

The highest-value next question is therefore:

> **After an unexpected harm event, can current REE identify and selectively strengthen the representation of the thing/action/context that caused it, such that the cause later changes prediction and action before harm recurs?**

If not, that is a concrete, falsifiable missing edge in the organism loop.