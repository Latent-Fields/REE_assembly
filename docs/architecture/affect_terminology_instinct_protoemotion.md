# Affect terminology: instinct, protoemotion, emotion

**Document type:** Architecture terminology addendum  
**Status:** provisional terminology / architecture note  
**Date:** 2026-06-09  
**Home cluster:** `docs/architecture/affect_primitives.md`  
**Related:** harm-affect register, relief/safety streams, proto-feelings audit, 603 lineage hazard-survival work

---

## Purpose

This note records a terminology distinction that should be used when reading or extending the affect-primitives register.

The terms **instinct**, **protoemotion**, and **emotion** overlap in ordinary language, but they should not be treated as exact synonyms inside REE.

The proposed distinction is:

```text
Instinct = preloaded prior / policy scaffold.
Protoemotion = runtime primitive affective-control signal.
Emotion = higher integrated appraisal state.
```

This keeps REE from collapsing inherited structure, active control signals, and later narrative/social appraisal into one word.

---

## Definitions

### Instinct

An **instinct** is a preloaded prior or policy scaffold over salience, learning, action, and control.

It is not necessarily a hard-coded behaviour. In REE terms, an instinct can preload:

```text
- what should be attended to;
- which state changes should be treated as salient;
- which action families are plausible;
- which learning rates should rise;
- which thresholds should shift;
- which mode switches should become easier or harder.
```

So the instinctive form is not:

```text
threat -> always run left
```

but rather:

```text
threat -> raise precision,
          narrow attention,
          bias freeze / escape candidates,
          increase harm learning,
          lower threshold for avoidance commitment.
```

### Protoemotion

A **protoemotion** is a primitive runtime affective-control signal generated when a state activates, violates, or resolves one of these priors/scaffolds.

Protoemotions modulate:

```text
- attention;
- action-selection pressure;
- learning rate;
- commitment threshold;
- precision / gain;
- mode switching;
- memory tagging.
```

Examples in the current REE register include or border on:

```text
fear / threat-state,
relief,
safety,
blocked agency,
effort / fatigue,
autonomic rebound,
soothing / comfort.
```

These are not merely labels for feelings. They are control signals with downstream computational consequences.

### Emotion

An **emotion** is a higher integrated appraisal state built from protoemotion plus additional structure:

```text
protoemotion
    + memory
    + context
    + self-model
    + social meaning
    + narrative / reportability
    + action history
```

Full emotion therefore belongs to later, more integrated REE versions. V3 mostly handles protoemotional control primitives and their architectural substrates.

---

## Relationship between the terms

The relationship is:

```text
Instinct is the preloaded bias.
Protoemotion is the active control signal.
Emotion is the interpreted / integrated state.
```

An instinct may produce or bias a protoemotion, but the two are not the same thing.

A protoemotion may be partly learned rather than fully instinctive.

A reflex may be instinctive without being protoemotional.

An emotion may include protoemotion without being reducible to it.

---

## Examples

### Threat / fear

```text
Preloaded instinct:
    threat cues should bias freezing, avoidance learning, attention narrowing,
    and high-priority harm prediction.

Protoemotion:
    fear / danger-state becomes active and alters E3 scoring, harm learning,
    action suppression/release, and future avoidance.

Emotion:
    fear as reportable experience, contextualised by memory, self-model,
    appraisal, and social meaning.
```

### Relief

```text
Preloaded instinct:
    aversive offset after a directed action should be treated as important.

Protoemotion:
    relief fires as an event-locked aversive-offset reinforcement signal and
    teaches that the preceding action was escape-relevant.

Emotion:
    relief as experienced, remembered, interpreted, and narrated in context.
```

### Safety

```text
Preloaded instinct:
    reliable threat absence should reduce defensive commitment thresholds and
    permit approach / exploration.

Protoemotion:
    safety is a learned prospective predictor that threat is absent; it gates
    commitment-release and approach.

Emotion:
    felt safety, trust, calm, or reassurance in a larger self/social context.
```

---

## Boundary with reflexes and drives

A useful local stack is:

```text
Reflex:
    fixed local stimulus-response pattern.
    Example: withdraw from sharp pain.

Instinct:
    preloaded prior or policy scaffold.
    Example: threat should bias freezing / escape learning.

Drive:
    homeostatic or motivational deficit gradient.
    Example: hunger, thirst, fatigue, social need.

Protoemotion:
    primitive affective-control signal that changes attention, learning,
    action thresholds, valuation, and mode.
    Example: fear, relief, safety, wanting, aversion, curiosity.

Emotion:
    protoemotion plus appraisal, memory, context, social meaning,
    narrative, and self-model.
```

This distinction lets REE model instinct without requiring fully hard-coded behaviour, and model protoemotion without prematurely claiming full human-like emotion.

---

## Design consequence for REE

The 603 lineage illustrates why this distinction matters.

The system did not merely need a generic fear instinct. It needed:

```text
- a trained harm valuation pathway;
- a working threat / safety signal;
- escape-affordance linkage;
- action-contingent relief/safety credit;
- bounded E3 action-selection authority.
```

The protoemotional signals only become behaviourally useful when the relevant representational and action-selection substrates are wired.

Therefore, future REE design should avoid treating instincts as whole behaviours and avoid treating protoemotions as narrative emotions.

Use this rule:

```text
Instincts preload priors.
Protoemotions express those priors as live control pressure.
Emotions integrate those pressures into self/context/narrative states.
```

---

## Status

This is a terminology addendum, not a new mechanism or claim. It should be folded into `docs/architecture/affect_primitives.md` when that file next receives a safe architecture-reference edit.
