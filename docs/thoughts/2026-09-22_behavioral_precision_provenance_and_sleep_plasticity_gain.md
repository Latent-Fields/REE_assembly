# Thought — Behavioural precision provenance should survive into replay and consolidation

Status: processed
Intake: evidence/planning/thought_intake_2026-09-22_behavioral_precision_provenance_and_sleep_plasticity_gain.md

**Date:** 2026-09-22
**Status:** raw/integrative thought
**Scope:** hippocampal episodic memory, E1/E2 world-model learning, precision/confidence, sleep/replay, plasticity gain, metacognition

## Verbatim seed

> “And it may need stored precision values from the relevant behavioural ‘test’.”

This arose while discussing MECH-572: the current sleep consolidator can impose almost the same parameter displacement on a nearly converged representation as on a poorly fitted one. That makes the emerging problem look less like “choose a better loss” and more like a failure to regulate **how much a replayed experience is allowed to change an already-learned model**.

The new thought is that the regulator may need information that exists during waking behavioural interaction but can disappear if an episode is stored only as state/action/outcome content.

When an organism behaviourally tests a prediction, the epistemic event is richer than “X happened”. It contains at least:

- what the organism predicted;
- how precise/confident that prediction was at the time;
- what action exposed the prediction to the world;
- what outcome was observed;
- how reliable/precise that observation or outcome was;
- the resulting prediction error or mismatch;
- the context in which the test occurred;
- whether the evidence was actually experienced, reconstructed, or simulated;
- and perhaps the downstream behavioural consequence of trusting that prediction.

A hippocampal/episodic trace may therefore need to preserve an **epistemic provenance packet** alongside its content, not merely the content itself.

A first-pass abstraction is:

```
behavioural test
  -> episode/content
  + prediction-at-test
  + precision-of-prediction-at-test
  + precision-of-observation/outcome
  + prediction error / mismatch
  + provenance
  + context
  -> later replay
  -> compare with current model + current precision
  -> choose replay priority and plasticity gain
  -> candidate durable update
```

The important distinction is between **stored historical precision** and **current precision**. Historical confidence should not automatically protect a representation from revision: that would make a confidently wrong attractor self-sealing. Instead, historical precision is evidence about what the organism believed and how diagnostic the later outcome was. During replay, the current model must be allowed to reassess that evidence in the light of later episodes, contradiction, calibration history, and changed context.

Thus a useful replay record may need at least two reliability terms:

1. **prior/model precision at the behavioural test** — how strongly the prediction was believed before exposure to the outcome;
2. **evidence/outcome precision** — how trustworthy or diagnostic the observed consequence was.

Sleep can then derive a new update gain relative to the **current** model precision rather than replaying the original update blindly.

This suggests a possible bridge between several existing REE families that should not yet be assumed identical:

- MECH-572: consolidation step-to-residual ratio;
- MECH-016: sleep precision/gain recalibration;
- ARC-055: confidence available to learning updates;
- MECH-043: precision-weighted prediction error;
- MECH-368 / MECH-431: write authority and tag-and-capture eligibility;
- MECH-285 and replay-priority machinery;
- hippocampal episodic indexing and replay;
- counterfactual / attractor-confidence correction.

The candidate architectural principle is stronger than “use an adaptive learning rate”:

> **Behaviourally grounded evidence should carry enough reliability/provenance information into memory that later replay can decide both whether the episode deserves processing and how strongly it is allowed to alter a persistent model.**

Potential affected components:
- hippocampal episodic/index memory
- E1/E2 predictive models
- precision/confidence machinery
- replay prioritisation
- sleep consolidation
- plasticity/write-authority gates
- counterfactual reprocessing
- attractor revision / model calibration
