# Thought: Candidate-differentiated affective gradients as action-selection, expression, and hippocampal indexing primitives

**Date:** 2026-06-06  
**Status:** Thought intake / hypothesis / not a claim  
**Primary routing:** Link to V3-EXQ-643 failure autopsy; relevant to modulatory-bias-selection-authority and per-candidate-variance dependency  
**Version relevance:** V3-narrow; V4/V5-rich  
**Do not build yet:** Do not expand into emotional expression, social signalling, or hippocampal write integration until routed by experiment.

## Trigger

V3-EXQ-643 failed, but the failure autopsy clarified an important architectural point.

The modulatory / curiosity signal had magnitude, but it did not vary across candidate actions or candidate trajectories. It was effectively a per-tick scalar. Because the signal was uniform across candidates, E3 had no affective gradient to rescale into action-selection authority.

This suggests a deeper primitive:

> For affect to carve behaviour, it must become candidate-differentiated.

Affect should not only say:

> “I am in a state of curiosity / harm / safety / blocked agency / fatigue.”

It should also be able to say:

> “This candidate trajectory is more curious, more blocked, safer, more dangerous, more effortful, or more relieving than that candidate trajectory.”

That difference is the affective gradient.

## Core hypothesis

Candidate-differentiated affective gradients may be a shared primitive for:

1. action-selection authority;
2. affective expression;
3. hippocampal event indexing;
4. future retrieval and replay bias;
5. later V4/V5 social interpretation.

The same structure that lets affect choose between actions may also let affect become visible in behaviour and memorable as an event.

## Distinction from scalar affect

A scalar affective signal can colour the whole organismal state.

Examples:

- global curiosity;
- global fatigue;
- global danger;
- global blocked-agency;
- global safety;
- global relief.

But a scalar signal cannot directly choose between candidate actions unless it varies across those candidates.

A candidate-differentiated affective signal has comparative structure.

Example:

```text
candidate A: high curiosity, moderate safety, low harm
candidate B: high goal pull, high hazard, high uncertainty
candidate C: low reward, high safety, low effort
candidate D: blocked, high effort, possible retry value
candidate E: relief if retreating
```

This gives E3 something to arbitrate.

The issue exposed by 643 is therefore not “modulatory affect does not exist.” It is:

> the affective signal has not yet been made candidate-specific enough to become selection-relevant.

## Relevance to behavioural diversity

Behavioural diversity probably does not emerge merely from adding more drives.

It emerges when different internal pressures create different candidate rankings under different contexts.

Affective gradients could allow the same world state to support multiple action tendencies:

- approach;
- approach cautiously;
- inspect;
- retreat;
- persist;
- retry;
- rest;
- abort;
- reorient;
- resume;
- seek safety;
- seek novelty;
- avoid contamination;
- repair after harm.

This turns proto-affects into behavioural carving fields.

Without candidate differentiation, the system may have internal signals but still collapse into the same committed action.

With candidate differentiation, action selection can become sensitive to the reason-for-action, not merely the raw score.

## Relevance to affective expression

Affective gradients are also prime sources for expression.

Expression need not begin as face, voice, or explicit symbol. In V3/V4 it can begin as action geometry:

- hesitation;
- latency;
- approach angle;
- retreat;
- repeated retry;
- stopping;
- resumption;
- oscillation between candidates;
- avoidance margin;
- cautious advance;
- exploratory sampling;
- decommitment;
- repair-seeking.

If affective gradients shape which trajectory is selected, they will also shape the visible style of behaviour.

Thus expression may initially be an emergent readout of candidate-level affective arbitration.

A later social agent could observe not only what action occurred, but how it occurred.

## Relevance to hippocampal memory

Affective gradients may also provide a memory-write structure.

A minimal memory trace is:

```text
state → action → outcome
```

A richer REE event trace would be:

```text
state
→ candidates considered
→ affective gradients over candidates
→ selected action
→ outcome
→ residue / relief / harm / blocked-agency / safety update
```

This gives the hippocampal system a richer episode to index.

The memory is not only:

> “I was here and did this.”

It becomes:

> “I was here; I could have done these things; this option felt promising but unsafe; that option felt blocked; I chose this; this happened.”

This supports later retrieval of action-affect-outcome arcs rather than undifferentiated state-action-outcome tuples.

## Relation to emotional memory literature

The biological literature does not directly describe REE-style candidate gradients, but it strongly supports the wider seam.

Emotional arousal and affective salience modulate memory consolidation, including amygdala and hippocampal / medial temporal lobe interactions.

Behavioural tagging suggests that a salient event can convert otherwise weak learning into durable memory when it occurs in the right temporal window.

Somatic-marker style accounts support the idea that affective body/brain signals associated with past outcomes can bias later choice under uncertainty.

Hippocampal replay literature supports the idea that memories are not passive records, but replayable trajectories that can influence later behaviour and planning.

These are not identical claims, but they converge on a useful REE hypothesis:

> affect is not merely an output of cognition; it can help determine what is chosen, what is expressed, what is written, and what is later retrieved.

## Initial literature anchors

Initial anchors for later targeted review:

- McGaugh, J. L. (2004). *The amygdala modulates the consolidation of memories of emotionally arousing experiences*. Annual Review of Neuroscience.
- Cahill, L. & McGaugh, J. L. (1998). *Mechanisms of emotional arousal and lasting declarative memory*. Trends in Neurosciences.
- Dolcos, F., LaBar, K. S., & Cabeza, R. (2004). *Interaction between the amygdala and the medial temporal lobe memory system predicts better memory for emotional events*. Neuron.
- Girardeau, G., Inema, I., & Buzsáki, G. (2017). *Reactivations of emotional memory in the hippocampus–amygdala system during sleep*. Nature Neuroscience.
- Ballarini, F., Moncada, D., Martínez, M. C., Alen, N., & Viola, H. (2009). *Behavioral tagging is a general mechanism of long-term memory formation*. Proceedings of the National Academy of Sciences.
- Bechara, A., Damasio, A. R., Damasio, H., & Anderson, S. W. (1994). *Insensitivity to future consequences following damage to human prefrontal cortex*. Cognition.
- Damasio, A. R. (1994). *Descartes’ Error: Emotion, Reason, and the Human Brain*.
- Ólafsdóttir, H. F., Bush, D., & Barry, C. (2018). *The role of hippocampal replay in memory and planning*. Current Biology.
- Joo, H. R. & Frank, L. M. (2018). *The hippocampal sharp wave-ripple in memory retrieval for immediate use and consolidation*. Nature Reviews Neuroscience.

## Proposed REE formulation

Candidate-differentiated affective gradients should be considered as a possible bridge primitive between:

```text
proto-affect
→ E3 action selection
→ behavioural expression
→ hippocampal event indexing
→ future retrieval/replay
→ V4 other-attribution
→ V5 communication and grammar
```

This should remain a hypothesis, not a claim.

It should not be promoted into implementation until the current upstream substrate work clarifies how per-candidate affective variance will be generated and measured.

## Possible substrate implications

Future substrate work may need to distinguish:

1. affect magnitude;
2. affect range across candidates;
3. affect direction over candidate trajectories;
4. affect-action coupling;
5. affect-memory write weight;
6. affect-retrieval query role;
7. affect-expression visibility.

The 643 autopsy suggests that magnitude alone is insufficient.

A readiness gate should require measurable per-candidate affective variance before testing whether affective authority changes selection.

## Candidate metrics

Possible metrics:

- per-candidate affective range;
- per-candidate affective entropy;
- candidate rank shift after affective bias;
- selected candidate affect profile;
- difference between selected and rejected candidate affect vectors;
- correlation between affective gradient and later outcome;
- whether high-gradient episodes are preferentially written to memory;
- whether later similar affective-gradient states retrieve prior action-affect-outcome arcs;
- whether visible behaviour changes under different affective-gradient profiles.

## V3 relevance

For V3, this is relevant only insofar as it helps solve the action-selection authority problem.

The immediate implementation question is narrow:

> Can the modulatory / proto-affective signal be made to vary across candidate actions or trajectories enough for E3 to use it?

Do not expand this into full emotional expression, social signalling, or hippocampal narrative memory in V3 unless routed by experiment.

## V4/V5 relevance

For V4 and V5 this may become much larger.

If affective gradients become visible in action geometry, other agents can begin to infer internal state from behaviour.

If affective gradients are stored in event memory, they can support future self-attribution and other-attribution:

- I was afraid;
- I was blocked;
- I approached anyway;
- I caused harm;
- I avoided harm;
- the other retreated;
- the other persisted;
- the other signalled need;
- the other acted cautiously.

This may become part of the bridge from organismic affect to social interpretation and later language.

Grammar may eventually name these arcs:

```text
agent + action + object + affective stance + outcome
```

But the organismic substrate must come first.

## Status / routing note

Hypothesis / thought intake.

Not a V3 claim.

Suggested routing:

- link to V3-EXQ-643 autopsy;
- link to modulatory-bias-selection-authority substrate;
- mark as relevant to per-candidate-variance dependency;
- mark as V3-narrow / V4-V5-rich;
- do not implement expression or hippocampal write integration yet;
- revisit after 643a or equivalent per-candidate-affective-variance readiness result.
