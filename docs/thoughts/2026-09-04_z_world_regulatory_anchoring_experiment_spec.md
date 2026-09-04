# z_world Regulatory Anchoring: Minimal Discriminating Experiment Specification

Status: experiment proposal / hypothesis test  
Date: 2026-09-04  
Related thought: `2026-09-04_from_regulation_to_knowledge_organizing_subjective_experience.md`

## Purpose

Test whether `z_world` should be organised primarily as a perceptual/predictive latent or whether it benefits from preserving distinctions that are consequential to the organism's regulation and agency.

The motivating hypothesis is:

> Constraints come first; meaning follows.

If this is right, a useful world latent should retain distinctions that matter to the machine's persistence, harm, benefit, controllability, and action consequences, even when those distinctions are not required for reconstructing raw observation.

This experiment is deliberately designed as a discriminating test rather than an architectural commitment.

## Core question

Holding environment, observation stream, downstream model capacity, optimiser budget, and evaluation protocol as constant as practical:

> Does regulatorily anchored `z_world` training improve downstream predictive, behavioural, counterfactual, and transfer performance relative to perceptual/predictive-only training?

A secondary question is whether agency-relevant distinctions emerge or need explicit support.

## Experimental arms

### A. Perceptual baseline

Train `z_world` only with the existing perceptual and/or generic predictive objective.

This is the control condition.

### B. Regulatory anchoring

Add auxiliary targets or constraints requiring `z_world` to preserve organism-relevant distinctions, selected from variables already causally present in the environment rather than newly invented labels.

Candidate targets:

- harm exposure or imminent harm;
- benefit/resource opportunity;
- internal regulatory state;
- controllability / action-relevance;
- persistent versus transient consequences;
- directional resource or threat structure where already available.

The experiment should prefer a minimal subset that can be implemented cleanly with current infrastructure.

### C. Agency anchoring

Add supervision or contrastive structure for outcome causation:

- self-caused outcome;
- externally caused outcome;
- potentially controllable but not selected outcome;
- uncontrollable outcome.

This arm tests whether agency is an organising axis in its own right rather than merely another regulatory signal.

### D. Developmental anchoring

Introduce regulatory and agency constraints progressively rather than all at once.

Suggested sequence:

1. immediate harm/benefit and internal-state consequence;
2. directional opportunity and threat;
3. controllability and self-caused consequence;
4. delayed consequence and counterfactual alternatives.

This arm tests whether representational ontology benefits from developmental staging rather than a fully specified mature objective from the start.

## Essential controls

The main danger is a trivial extra-supervision explanation. The anchored arms must not win merely because they receive more labelled information.

At minimum include one or more matched controls:

- **Random auxiliary target control:** same auxiliary-head capacity and loss weight, but with shuffled or non-causal targets.
- **Perceptual auxiliary control:** same number of auxiliary dimensions predicting equally easy scene features that are not organism-relevant.
- **Capacity control:** keep encoder and downstream model parameter counts matched across arms.
- **Information-access control:** ensure all arms receive the same raw observation; only the training objective differs.

If regulatory anchoring only beats the baseline but not these matched controls, the result should not be interpreted as evidence for the organising hypothesis.

## Evaluation domains

### 1. E1/E2 rollout quality

Measure whether `z_world` supports more accurate downstream rollout prediction across multiple horizons.

Important: examine not only average prediction loss but specifically errors around:

- harm transitions;
- resource transitions;
- changes in controllability;
- self-caused versus external consequences;
- delayed consequences.

### 2. Behavioural competence

Evaluate behaviour in held-out episodes with emphasis on:

- avoiding preventable harm;
- exploiting directional resource structure;
- choosing actions with delayed consequences;
- adapting when familiar cues change meaning;
- distinguishing controllable from uncontrollable outcomes.

### 3. Counterfactual discrimination

Test whether nearby alternatives that are perceptually similar but differ in consequence remain distinguishable in latent space and in rollout.

Example class:

- same visual arrangement;
- different action affordance or vulnerability state;
- different predicted consequence.

### 4. Latent geometry

Probe whether consequence-relevant distinctions are linearly or otherwise simply decodable from `z_world`.

The goal is not merely high probe accuracy. Also ask whether the geometry supports:

- smooth ordering by consequence;
- separation of controllable and uncontrollable states;
- preservation of directional structure;
- stable representation across nuisance perceptual variation.

### 5. Transfer

Construct matched environments with similar sensory statistics but altered vulnerability, affordance, or action consequence.

Prediction of the regulation-first hypothesis:

> Internal organisation should change systematically when the same scene has different consequences for the organism.

A purely scene-centred latent should be less sensitive to this manipulation.

### 6. Replay / sleep sensitivity

Where practical, compare post-replay changes after matched perceptual novelty and regulatory surprise.

Prediction:

Regulatory surprise should produce larger future changes in categorisation, rollout, or action than perceptual novelty of similar magnitude if replay is reorganising experience by organism consequence.

## Primary discriminating predictions

The regulation-first hypothesis gains support if, after matched controls:

1. regulatory anchoring improves downstream E1/E2 rollout particularly at consequential transitions;
2. behavioural transfer improves when vulnerability or affordance changes without major sensory change;
3. counterfactuals differing only in consequence remain more separable;
4. agency/controllability structure becomes more usable downstream;
5. replay of regulatory surprise changes future behaviour more than matched perceptual novelty;
6. benefits survive removal of the auxiliary heads at evaluation time.

## Falsifying or weakening outcomes

The hypothesis is weakened if:

- perceptual/predictive-only training matches anchored training across behaviour, transfer, and rollout;
- matched arbitrary auxiliary targets perform equally well;
- anchored latents improve probe accuracy but not downstream behaviour or prediction;
- benefits vanish outside the exact supervised variables;
- developmental staging adds no robustness or transfer advantage over mature-at-once training;
- vulnerability changes do not alter internal organisation once observations are matched.

A null result would be useful: it would argue that generic predictive learning already preserves the needed distinctions, reducing pressure to complicate `z_world`.

## Minimal first experiment

Do not start with all four arms.

Run the smallest useful comparison:

**A. Perceptual baseline** versus **B. Regulatory anchoring**, with a matched non-regulatory auxiliary control.

Use the already available directional resource-field supervision mechanism if it is still the cleanest current intervention, because it directly tests whether information with clear action/regulatory significance is otherwise being discarded.

Suggested initial readouts:

- E1/E2 rollout error by event type;
- directional resource decoding;
- behaviour around resource acquisition and harm avoidance;
- held-out scene transfer;
- latent separation of perceptually similar states with different consequences.

Only if this shows a real effect should agency-specific and developmental arms be added.

## Interpretation discipline

A positive result should be described as evidence that regulatorily consequential distinctions are useful organising constraints for `z_world`, not as proof that all knowledge is reducible to self-maintenance or that `z_world` is equivalent to cortex.

A negative result should not be patched away automatically. It may indicate that:

- the existing predictive objective already captures the relevant structure;
- the chosen regulatory signal is redundant;
- the bottleneck lies after `z_world` rather than within it;
- the representational problem is about temporal coordination rather than retained content;
- the supervision form is too literal and misses the organising principle.

## Immediate implementation questions

Before coding, inspect the live implementation and answer:

1. Where exactly is `z_world` produced and consumed?
2. Which losses currently shape it?
3. What did the directional resource-field head change, if anything, in representation or downstream behaviour?
4. Is E1/E2 rollout currently trained through `z_world` end-to-end or partly detached?
5. Which held-out environment manipulations already exist that can serve as matched consequence-changing tests?
6. Can event-type rollout metrics be extracted without modifying training?

## Decision rule

Do not redesign `z_world` wholesale on the basis of this thought.

First ask whether a small, controlled regulatory anchoring intervention produces a robust, non-trivial gain that survives matched controls and transfers beyond the exact supervised target. If yes, expand the hypothesis. If no, narrow or reject it.
