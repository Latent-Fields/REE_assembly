# Regulatory Anchoring: Minimal Discriminating Experiment

Status: processed
Intake: evidence/planning/thought_intake_2026-09-04_regulation_first_organizing_subjective_experience.md
Claims registered: GOV-MATCHAUX-1 (the matched-control / scaffold-removal rule); the experiment itself is NOT queued -- gated chip chip-20260904-regulatory-anchoring-matched-aux, sequenced after V3-EXQ-1002
Original status line: experiment specification / hypothesis test
Date: 2026-09-04  
Parent thoughts: `2026-09-04_from_regulation_to_knowledge_organizing_subjective_experience.md`, `2026-09-04_z_world_representation_contract.md`

## Scientific question

Does anchoring `z_world` to organism-relevant regulatory structure produce a more useful world representation than generic extra supervision of equal capacity and training cost?

This experiment is deliberately designed to distinguish the regulation-first hypothesis from the trivial explanation that *any* auxiliary head or additional loss improves representation learning.

No V3-EXQ identifier is assigned here. It should receive one only through the live experiment/ledger convention.

## Primary hypothesis

A representation trained to preserve organism-relevant consequence information will outperform both a prediction-only baseline and a matched arbitrary-auxiliary-control condition on downstream generalization, rollout and counterfactual control, not merely on its auxiliary probe.

## Minimal first comparison

Run three conditions with the same environment, trajectories, encoder capacity and downstream architecture.

### A. Perceptual/predictive baseline

Train `z_world` with the current principal perceptual/predictive objective and no added organism-relevance supervision.

### B. Matched arbitrary auxiliary control

Add an auxiliary prediction task matched as closely as practical to condition C for:

- target dimensionality;
- entropy/difficulty;
- head parameter count;
- loss scale;
- training examples;
- update frequency.

The target should contain learnable structure but should not encode regulatory consequence. Examples could be deterministic nuisance features or transformations of observation variables that are equally predictable but irrelevant to action.

### C. Regulatory anchoring

Add auxiliary targets that require preservation of organism-relevant distinctions available in the environment, such as:

- harm/benefit or resource consequence;
- directional opportunity/threat where applicable;
- internal-state consequence;
- controllability when available without changing the task.

The goal is not to maximize these target scores. The targets are scaffolds intended to alter which information survives the `z_world` boundary.

## Matching requirements

Across A/B/C, hold fixed wherever possible:

- random seeds;
- training trajectories or trajectory-generation policy;
- encoder latent dimensionality;
- downstream E1/E2 capacity;
- optimizer and learning-rate schedule;
- number of updates;
- auxiliary-head size for B and C;
- aggregate auxiliary loss budget;
- total compute within a predefined tolerance.

If exact target entropy or difficulty matching is impossible, report the mismatch rather than silently accepting it.

## No privileged inference rule

The regulatory targets should not be supplied as privileged variables to downstream behaviour at evaluation time. They are training scaffolds and diagnostic probes.

A strong result survives disabling or removing the auxiliary head after training.

## Primary outcome measures

The experiment should prioritize organism-level usefulness over latent interpretability.

1. **E1 rollout quality** — one-step and multi-step predictive consistency.
2. **E2 rollout quality** — fast forward prediction where currently measurable.
3. **Behavioural outcome** — resource acquisition, harm avoidance, survival/regulation or the closest existing organism-level score.
4. **Counterfactual discrimination** — whether states with similar observation statistics but different consequences/actions remain distinguishable.
5. **Transfer** — performance when resource arrangement, vulnerability or contingencies change without retraining the entire stack.
6. **Perturbation recovery** — time and quality of recovery after a consequence-relevant environmental change.
7. **Latent probe scores** — diagnostic only, not primary success criteria.

## Critical matched challenge

Construct or identify state pairs in which perceptual similarity conflicts with organism relevance.

Examples:

- same local-looking scene, different directional route to benefit;
- visually similar object/state, different consequence because internal state differs;
- same sensory event, controllable in one context and uncontrollable in another.

If condition C is genuinely preserving organism-relevant structure, these pairs should separate in downstream prediction and behaviour even when condition B learns its nuisance target equally well.

## Success criterion

Support for regulation-first organization increases if C reliably exceeds both A and B on downstream generalization or counterfactual behaviour, with the gain persisting after the auxiliary head is removed and without a commensurate increase in model capacity or information available at evaluation.

The strongest result would be a selective advantage specifically on situations where perceptual similarity and regulatory consequence diverge.

## Results that weaken the hypothesis

The hypothesis should be weakened if:

- B performs as well as C once supervision and capacity are matched;
- C improves only its own auxiliary/probe accuracy;
- C's advantage disappears when the auxiliary head is removed;
- C simply memorizes labelled categories and fails on consequence-preserving transfer;
- prediction-only A learns the same regulatorily useful structure and downstream performance without special anchoring;
- performance differences are explained by target entropy, training signal density or compute.

## Second-stage extensions — only if the first comparison shows signal

### Agency anchoring

Add a condition distinguishing self-caused, controllable-but-not-currently-caused and externally caused outcomes.

### Developmental anchoring

Give the same total regulatory target exposure but compare simultaneous training with staged introduction. This tests whether developmental order changes the learned ontology rather than merely the total amount of supervision.

### Replay dependence

After a consequence structure changes, compare waking-only updating with the existing replay/sleep mechanism to test whether offline reorganization improves the new world carving.

## Interpretation discipline

This experiment is not intended to show that harm, benefit, agency or resources are the final natural coordinates of cognition. A positive result would show something narrower and more useful:

> requiring the early world representation to preserve organism-relevant distinctions can improve the emergence of predictive and actionable world structure beyond the effect of generic additional supervision.

That result would justify asking which regulatory distinctions are fundamental, which are developmental scaffolds, and which should eventually be learned without explicit labels.
