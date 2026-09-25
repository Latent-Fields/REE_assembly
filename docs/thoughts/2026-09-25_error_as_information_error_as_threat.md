# Error as Information, Error as Threat: Learned Valence of Prediction Error

**Date:** 2026-09-25  
**Status:** raw thought / hypothesis seed; not yet claim-ingested  
**Scope:** developmental learning, prediction error, control-plane routing, curiosity, threat, correction, model revision  
**Origin:** discussion prompted by the observation that schooling can sometimes make being wrong feel dangerous rather than interesting. The educational example is motivational, not evidence for the computational claim.  
**Related internal material:** `docs/architecture/control_plane.md`, `docs/architecture/sd_020_harm_surprise_pe.md`, `docs/thoughts/2026-08-12_prediction_error_to_inferred_agency_and_gated_fast_empathy.md`, `docs/thoughts/2026-09-24_experimental_learning_beyond_literature.md`, `evidence/planning/loveability_ethical_agency_v5_plan.md`

## Core proposition

Prediction error need not have a fixed affective or control meaning.

The same basic event —

> **what happened differs from what I predicted**

— can plausibly become associated through development with very different downstream regimes.

In one developmental history, prediction error may mean:

> **Interesting. My model is incomplete. Look harder, explore, update.**

In another, prediction error may come to predict:

> **Danger. I am exposed, punishment is coming, status or attachment is at risk, act defensively.**

The computational distinction is not that one system detects prediction error and the other does not. Both detect it. The distinction is that the error has acquired a different **learned routing significance**.

The thought therefore proposes that REE should distinguish at least three things:

1. **the mismatch itself** — representational evidence that prediction and observation diverged;
2. **the inferred cause and consequence of the mismatch** — what the error appears to mean about the world, self, other agents, or future;
3. **the learned control-plane significance of being in error** — whether the mismatch recruits curiosity/orienting/model revision, threat/defence/rapid action, or some graded mixture.

This is a routing hypothesis, not a proposal to encode “prediction error = good” or “prediction error = bad” as a scalar reward.

---

## 1. Why error should not have a single valence

Prediction error is useful because it marks a place where the current model is inadequate.

But inadequacy can arise in radically different situations.

A prediction can fail because:

- the environment contains a harmless novelty;
- the agent has discovered a controllable regularity;
- the current abstraction is too coarse;
- another agent behaves unexpectedly;
- a hidden hazard has appeared;
- the agent has caused an unexpected harmful consequence;
- a trusted other corrects the agent;
- a hostile other punishes or humiliates the agent;
- the current self-model is contradicted;
- the error occurs in a context where being wrong has previously predicted loss, exclusion, pain, or status threat.

A system that routes all of these identically is under-differentiated.

The useful distinction is therefore not:

```text
prediction error -> learning
```

but something more like:

```text
prediction error
    -> causal/context appraisal
    -> learned routing prior
        -> epistemic orienting / curiosity / model revision
        -> defensive vigilance / rapid protective action
        -> social correction / repair
        -> uncertainty hold / further evidence collection
```

These routes can overlap. The claim is not that they are discrete emotional boxes. The claim is that the same mismatch signal can acquire different downstream control consequences through experience.

---

## 2. The educational example

School provides a useful human intuition for the hypothesis.

If an error is repeatedly followed by curiosity, explanation, permission to revise, and successful discovery, then the fast detection of “something is wrong” can plausibly become a cue for engagement.

If an error is repeatedly followed by ridicule, punishment, loss of marks experienced as status loss, public exposure, anger, or withdrawal of approval, then the same fast interrupt may become predictive of threat.

The subjective transformation would be approximately:

```text
"I was wrong" -> "there is information here"
```

versus:

```text
"I was wrong" -> "something bad is about to happen to me"
```

The important REE translation is structural rather than phenomenological. REE need not model school shame in V3. The general question is whether **the control significance of prediction error is learned from what historically follows prediction error**.

School is therefore an illustrative case of a more general developmental mechanism.

---

## 3. Error-as-information

In the information route, mismatch should tend to increase some combination of:

- orienting toward the unexplained variable;
- information-seeking;
- exploratory action where safe;
- counterfactual generation;
- temporary reduction in commitment confidence;
- writable model plasticity;
- preservation of the anomaly rather than forced assimilation;
- replay priority;
- comparison among competing explanations;
- pleasure/interest-like learning-progress signals where appropriate.

This route fits existing REE material around curiosity, MECH-482/483 epistemic deficit and orient/survey behaviour, control-plane precision routing, developmental babbling, and the recent finding that apparently unproductive exploration can be essential data acquisition.

The key property is:

> **The error remains epistemically available.**

The system is allowed to discover that its current model was wrong.

---

## 4. Error-as-threat

In the threat route, prediction error becomes evidence not merely that the model is wrong, but that **being wrong predicts danger**.

That may alter:

- fast salience classification;
- arousal;
- mode priors;
- action readiness;
- commitment interrupt thresholds;
- attention allocation;
- exploration breadth;
- precision weighting;
- whether counterfactual processing remains available;
- what gets written to memory;
- whether the agent updates the explanatory model or instead learns avoidance of the error-producing context.

Crucially, threat routing does **not** necessarily imply “less learning.”

It may produce **different learning**.

For example, the system might learn:

```text
avoid situations where uncertainty becomes visible
avoid actions likely to expose model inadequacy
commit early rather than remain uncertain
monitor for punishment rather than inspect the causal mismatch
conceal or externalise error when social machinery exists
```

while still becoming extremely efficient at detecting cues associated with correction or evaluation.

This distinction matters. A threat-conditioned learner can be highly plastic in the wrong target space.

---

## 5. Fast interrupt as the hinge

REE already contains a fast-interrupt/control-plane architecture. This makes the thought particularly relevant.

The proposed mechanism need not invent a new “error emotion.” A simpler possibility is:

1. prediction error is detected normally;
2. contextual features and developmental history determine the salience classification of that error event;
3. that classification changes control-plane mode priors before slower explanation is complete;
4. the resulting mode changes what information receives precision, what actions are available, and which learning writes occur.

In that architecture, the fast interrupt is adaptive.

Some errors really should be treated as danger signals. Unexpected acceleration toward a hazard is not an invitation to leisurely epistemic curiosity.

The pathology or developmental failure would be **overgeneralisation**:

> error events that are epistemically benign inherit the threat routing learned in contexts where error historically predicted harm, punishment, rejection, or loss of control.

Thus the goal is not to abolish error-threat coupling. It is to make the coupling discriminative.

---

## 6. Connection to correction without annihilation

This thought is adjacent to, but distinct from, the existing LOVE-4 “correction without annihilation” problem.

LOVE-4 asks where correction is attributed:

```text
this action / rule / model was wrong
```

versus:

```text
the self as a whole is bad / unsafe / unloveable
```

The present thought asks something temporally earlier:

> **What control regime is recruited by the detection of error before the system has fully localised what was wrong?**

These mechanisms may interact strongly.

If prediction error already recruits threat mode, then later correction may begin from a defensive control state in which:

- model revision is harder;
- self-protection is prioritised;
- counterfactual search narrows;
- social signals are interpreted through threat;
- global-self attribution becomes easier;
- repair competes with avoidance or appeasement.

Conversely, a safe-base developmental history may allow a large error signal to remain compatible with curiosity and specific credit assignment.

This gives a possible computational bridge between the safe-base/correction work and the control-plane architecture without collapsing either into the other.

---

## 7. A possible REE representation

The mechanism should preserve separation between **error content** and **error routing history**.

Do not make raw prediction error itself negative-valued.

A safer decomposition would be conceptually:

```text
PE_t = mismatch content / magnitude

C_t = context and inferred cause
      (hazard, novelty, social evaluation, controllability,
       responsibility, reversibility, safe-base cues, etc.)

R_t = learned routing state
      P(epistemic / threat / repair / hold | PE_t, C_t, history)

control plane consumes R_t
world/self models consume PE_t
```

The routing state may ultimately be distributed rather than represented as a literal categorical variable. The important invariant is that **the history-dependent control interpretation of an error must not overwrite the error itself**.

Otherwise a system trained to fear error could literally lose access to the evidence required to discover that its model is wrong.

---

## 8. Developmental hypothesis

The developmental prediction is stronger than merely saying “safe learning environments are helpful.”

It predicts **history dependence in the routing of an otherwise matched error signal**.

Two agents can encounter the same benign mismatch at time T but respond differently because prediction error had different consequences during development.

A minimal contrast:

### Development A — epistemically safe error

Prediction errors are followed by:

- time to inspect;
- no punishment;
- opportunities to act again;
- successful model improvement;
- learning-progress signals;
- preservation of safety.

### Development B — threat-paired error

Prediction errors of matched magnitude are followed by:

- aversive interrupt;
- loss of control;
- threat or punishment;
- forced termination of exploration;
- perhaps, in later social versions, status/relationship threat.

Then both agents receive the **same novel but safe mismatch**.

The prediction is that Development B should show altered routing even before any new harm occurs.

---

## 9. Candidate falsifiable consequences

The thought earns value only if it generates discriminating experiments.

### Prediction 1 — matched error, different routing

After different developmental histories, present a matched benign prediction error.

Measure:

- fast mode-prior shift;
- arousal/interrupt response;
- exploration entropy;
- orient/survey activation;
- commitment latency;
- counterfactual breadth;
- learning-rate allocation;
- actual correction of the responsible world-model component.

If developmental history does not change any of these despite successful conditioning elsewhere, the strong routing hypothesis weakens.

### Prediction 2 — threat pairing changes the target of learning

A threat-paired agent may learn the danger context while correcting the causal world model less effectively.

Thus separate:

- **threat-context acquisition**, from
- **model-error correction**.

A system can become better at predicting punishment while remaining worse at fixing the model that generated the original error.

### Prediction 3 — safety can restore epistemic routing

If the association is genuinely learned rather than a fixed architectural mode, extended safe error-and-repair experience should partly restore curiosity/model-revision routing.

Failure of any reversibility would suggest either a different mechanism or a developmental critical-period effect.

### Prediction 4 — context specificity before generalisation

Early in learning, error-as-threat should be more context-specific. Broad generalisation to unrelated error classes should emerge only under sufficiently shared cues or repeated cross-context pairing.

Immediate global generalisation would suggest an implementation shortcut rather than learned routing.

### Prediction 5 — safe-base signals protect correction without suppressing error

In later social REE, a trusted corrective relationship should allow:

- large error detection;
- preserved self stability;
- specific rule/model updating;
- continued relationship;
- repair behaviour;

without needing to attenuate the error itself.

If “safety” works only by reducing or hiding prediction error, it has failed the intended mechanism.

---

## 10. Near-term V3 experiment seed

This thought does not justify adding social shame machinery to V3.

A clean V3 proxy could test the non-social computational core after the native waking learner exists.

1. Train two otherwise matched developing agents.
2. Give both matched prediction-error statistics.
3. In one developmental arm, errors occur during safe exploratory continuation.
4. In the other, errors predict a fast aversive/hazard-linked control-state transition while preserving enough viability for learning.
5. Later, present an identical benign mismatch under a neutral environment.
6. Compare control-plane routing and actual model correction.

Important controls:

- equal total prediction-error magnitude;
- equal training budget;
- equal hazard exposure except for the error contingency;
- unpaired-hazard control;
- shuffled error/hazard timing control;
- demonstrate that both agents can correct the model under an externally forced neutral learning regime;
- preserve the raw error signal across arms so a result cannot be explained by one agent simply failing to detect error.

This should be downstream of the current native-waking-learning repair. Testing learned error routing before REE has a genuine waking learner would recreate the exact dead-loop problem exposed in September 2026.

---

## 11. Later social-development extension

The richer version belongs to a later social substrate.

There the experiment can distinguish:

- correction delivered within a stable relationship;
- correction paired with relationship rupture;
- public/status threat;
- punishment unrelated to causal responsibility;
- specific reparable harm;
- global condemnation.

The question is no longer only whether error triggers threat.

It becomes:

> **Can an agent learn that being wrong is survivable, informative, and reparable even when the error concerns harm it caused?**

That would connect directly to LOVE-2/4/5:

```text
I remain worth preserving
+
I can be wrong
+
my error can have consequences for another
+
I can update and repair
```

The desired endpoint is not an agent that enjoys all errors or lacks defensive reactions. It is an agent whose defensive machinery does not automatically treat epistemic correction as existential threat.

---

## 12. Failure modes and cautions

### Do not reward “being wrong”

The target is useful model revision, not error production. Rewarding error directly could create novelty seeking, deliberate misprediction, or noisy-TV behaviour.

### Do not suppress threat responses to real danger

Some unexpected events demand immediate defence. The test is discrimination, not global curiosity.

### Do not equate arousal with defensiveness

Arousal can support orienting and learning. The relevant readout is the whole routing pattern and downstream causal effect, not one scalar.

### Do not infer human phenomenology from REE

A computational threat-route is not automatically shame, anxiety, humiliation, or any other human experience. Those terms can motivate structural hypotheses but should not be smuggled in as established equivalences.

### Do not let the routing signal replace causal attribution

The system must still discover *what* was wrong. A learned “error is dangerous” prior is a control influence, not an explanation of the error.

### Do not judge success from behaviour alone

Avoidance after error could look prudent while reflecting epistemic collapse. The experiment must inspect whether the responsible model was actually corrected.

---

## 13. Relation to current REE themes

This thought joins several active strands without requiring them to be the same mechanism:

- **native waking learning:** there must be a real writable loop before error can causally revise models;
- **Phase-0 babbling:** early error can be information generated through self-produced exploration rather than evidence of failure;
- **prediction-error precision:** errors differ in reliability and consequence;
- **MECH-482/483 orienting:** unresolved structured error can recruit information seeking;
- **fast interrupt/control plane:** the same mismatch can alter operating regime before deep deliberation;
- **dynamic coordination:** different error contexts may require different routing coalitions rather than one global strategy;
- **LOVE-4:** correction can update a specific act/model without becoming global self-condemnation;
- **experimental-learning doctrine:** this may be a synthesis/frontier mechanism whose standing should come from discriminating experiments rather than conceptual attractiveness.

The unifying idea is:

> **An intelligent system should not merely detect that it was wrong. It should learn what being wrong means in context — while preserving access to the evidence that made the error visible.**

---

## 14. Candidate downstream fan-out

This document is a thought seed, not a claim registration.

A future thought-intake/orchestrator pass should:

1. audit existing REE claims for partial ownership before registering anything new;
2. identify the minimal routing locus — likely fast salience / mode-prior / precision control rather than a new affect module;
3. separate raw prediction-error representation from learned error-context routing;
4. determine whether MECH-482/483 already cover the epistemic branch and what is genuinely missing on the learned threat-association branch;
5. cross-check LOVE-4 so this does not duplicate the action-versus-global-self credit-assignment problem;
6. design the V3 matched-error developmental assay only after the native waking learner is demonstrably live;
7. later extend the assay to social correction, safe-base, status threat, and repair.

## Compact formulation

```text
prediction error is not itself the danger.

but an organism can learn that prediction error predicts danger.

when that happens, the fast interrupt that should sometimes say
"look -- your model is wrong"

may instead begin by saying
"protect yourself -- being wrong is unsafe."

the developmental problem is not to remove the interrupt.
it is to teach it the difference.
```
