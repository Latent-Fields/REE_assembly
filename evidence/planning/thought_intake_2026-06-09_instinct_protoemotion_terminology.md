# Thought intake: instinct / protoemotion terminology

**Date:** 2026-06-09  
**Status:** captured thought / terminology seed  
**Related architecture note:** `docs/architecture/affect_terminology_instinct_protoemotion.md`  
**Related canonical home:** `docs/architecture/affect_primitives.md`

---

## User thought

The protoemotions could also be thought of as instincts. There may be two words for the same kind of processes. A clearer definition, now that REE has more functional mapping, may be that **instincts are where priors are preloaded**.

---

## Captured interpretation

This is a useful terminology distinction rather than a strict synonymy.

Proposed mapping:

```text
Instinct = preloaded prior / policy scaffold.
Protoemotion = runtime primitive affective-control signal.
Emotion = higher integrated appraisal state.
```

The key separation is:

```text
Instinct is the preloaded bias.
Protoemotion is the active control signal.
Emotion is the interpreted / integrated state.
```

This means instincts need not be hard-coded actions. They may be preconfigured biases over salience, learning rate, action classes, commitment thresholds, precision/gain, and mode switching.

Protoemotions are then the runtime signals through which those priors become behaviourally active.

---

## REE relevance

This helps avoid three conflations:

```text
1. instinct ≠ reflex-only hard-coded action;
2. protoemotion ≠ full narrative/reportable emotion;
3. emotion ≠ primitive affective-control signal alone.
```

It also fits the current 603 lineage: threat/relief/safety signals only become useful when the relevant harm pathway, safety predictor, escape-affordance linkage, and E3 action-selection authority are wired.

---

## Suggested future action

Fold the terminology addendum into `docs/architecture/affect_primitives.md` on the next safe full-file edit.

No new claim or mechanism should be registered from this note alone.
