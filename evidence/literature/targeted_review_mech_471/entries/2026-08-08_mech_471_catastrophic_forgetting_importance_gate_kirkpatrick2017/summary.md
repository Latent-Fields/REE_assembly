# Kirkpatrick et al. (2017) — Overcoming catastrophic forgetting in neural networks

**PNAS 114:3521-3526 · [10.1073/pnas.1611835114](https://doi.org/10.1073/pnas.1611835114) · arXiv:1612.00796**
**Claim tested: MECH-471 · direction: supports · confidence: 0.74**

## What the paper did

Neural networks trained on tasks in sequence forget the earlier ones — not gracefully, but catastrophically, often to near-chance. The paper's framing sentence is worth noting because it explains something about why MECH-471's asymmetry exists at all: it "has been widely thought that catastrophic forgetting is an inevitable feature of connectionist models". If degradation is believed inevitable, no one registers a discipline against it.

Kirkpatrick and colleagues show it is not inevitable. Elastic weight consolidation (EWC) estimates, for each parameter, how important it was to previously learned tasks — using a Fisher-information estimate at the previous task's optimum — and then selectively slows learning on the important ones when a new task arrives. They demonstrate retention across a sequence of permuted-MNIST classification tasks and, more relevantly here, across several Atari 2600 games learned sequentially by a deep RL agent.

## Why this speaks to MECH-471

The other two entries in this directory are biological. This one matters because it is the *same machine class as REE*: an artificial, gradient-trained, goal-conditioned agent acquiring behavioural competences sequentially in interactive environments and losing the earlier ones. There is no cross-species transfer to argue about.

MECH-471 asserts that REE's competence path has "no gate against a single successful rollout propagating widely". Catastrophic forgetting is the standard name for what that absence produces, and the baseline condition of this paper *is* the FAIL outcome that MECH-471's local-update interference test is designed to detect. The Atari sequence is the closest published analogue to REE's own setting.

EWC is then an existence proof for the bounding half of the discipline, and a cheap one: a per-parameter importance weight and a quadratic penalty, no architectural surgery. That supports MECH-471's own self-assessment that this is `complicated (buildable)` rather than `complex (probe-gated)` — the mechanism is not waiting on an unknown, it is waiting on someone building it. Which is consistent with the claim's judgement that the interference probe is "the cheapest real probe in cluster E and the right first move": you would run the probe not to find out whether a remedy exists, but to find out whether REE needs one.

## Limitations, and two disanalogies that constrain how far this can be leaned on

**EWC requires explicit task boundaries.** It consolidates at the moment a task is declared finished, and computes its importance estimate per task. REE has no such boundary — competence accrues continuously, within and across episodes, with no signal saying "that competence is now complete, freeze its parameters". An REE implementation cannot port the algorithm; it would need a boundary-free importance signal, which is a genuinely different and harder problem. Anyone reading this entry as "the fix is off the shelf" is reading it wrong.

**EWC delivers bounding only.** It is deliberately amnesic about *which* experiences made a parameter important — the Fisher estimate records that a parameter matters, not what wrote it — and it offers no operation to revert a specific past update. So a system can satisfy MECH-471's bounding property in full and still have no provenance and no rollback. Citing this entry as support for the claim's full triple would be a category error; it supports one leg of three, and I have set `mapping_fidelity` accordingly.

There is also a live methodological dispute worth recording rather than smoothing over. Huszár's PNAS comment ([10.1073/pnas.1717042115](https://doi.org/10.1073/pnas.1717042115)) argues that the multiple-quadratic-penalty scheme is not the correct Bayesian recursion the paper's derivation suggests. This does not touch the phenomenon — catastrophic forgetting is real and importance-gating helps — but it means the specific formulation should be treated as one instantiation of the principle rather than the settled solution. If REE builds a bounding gate, the continual-learning literature since 2017 (replay-based and constraint-based approaches, among others) is a wider design space than this one paper implies.

## Confidence reasoning

Source quality 0.85 — PNAS, enormously influential, thoroughly replicated as a *phenomenon*, discounted for the contested derivation and for the fact that later work has found EWC's retention on harder continual-learning benchmarks less impressive than the original results suggest. Mapping fidelity 0.70 — carries the discount for the task-boundary requirement and the one-of-three-properties coverage. Transfer risk 0.30, the lowest of the three MECH-471 entries, precisely because there is no biological transfer to make: this is REE's own machine class, and what fails here fails for the same reasons it would fail in REE. Aggregate 0.74.
