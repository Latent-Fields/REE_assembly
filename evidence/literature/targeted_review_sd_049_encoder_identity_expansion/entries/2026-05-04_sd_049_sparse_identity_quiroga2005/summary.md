# Quiroga et al. 2005 -- Concept cells and the sparse-identity-coding precedent

## What the paper did

Quiroga, Reddy, Kreiman, Koch and Fried recorded from 993 single units in the medial temporal lobe of 8 epilepsy patients while the patients viewed photographs of well-known individuals, landmarks, animals, and objects. They report what came to be called "concept cells": single units that fire selectively to strikingly different views of one specific individual or object -- different photographs, different angles, sometimes even the printed letter string of the named individual. The paper concludes that the underlying code is "invariant, sparse and explicit," and proposes this code as a substrate for transforming complex visual percepts into long-term memory.

## Why I pulled it for SD-049

The SD-049 Phase 2 implementation has to commit to an architectural choice for how `z_resource` represents resource identity. Option A is a one-hot identity slot concatenated with a magnitude latent -- engineering-clean, deterministic, no risk of representation collapse during joint training. Option B is a low-D learned embedding that captures similarity structure across types (food and water are both consummatory; novelty is not), at the cost of needing phased training and risking the EXQ-166b/c/d-style collapse pattern.

Concept cells are the canonical biological precedent that a real readout from a real identity-coding circuit can be sparse and explicit at the single-unit level. If the goal at validation time is identity-recovery accuracy from `z_resource` (V3-EXQ-514 acceptance criterion), then option A's labeled-line architecture is the most direct match to what these neurons look like at the read-out end.

## What the paper does not say

The single most important caveat is that Quiroga et al. record from the *output* of an identity-coding system -- the MTL neurons whose firing patterns we are reading. They do not, and cannot, tell us whether the substrate that *produces* these sparse readouts is itself sparse-and-explicit, or distributed-and-similarity-preserving with sparse readouts on top. Schapiro et al. (2016, 2017) -- pulled in the same lit-review -- argue strongly for the second reading: the hippocampus learns distributed temporal-community structure, and concept cells may be the read-out of that distributed substrate.

A separate caveat is the cross-domain transfer. The paradigm here is visual identity in humans recognising celebrities and landmarks. SD-049 is goal-identity in a rodent-analog grid world over a small set of resource types (food, water, novelty). The architectural shape -- sparse readout from an identity-coding circuit -- maps cleanly enough that the precedent has weight, but the specific representation that an MLP encoder will learn under supervised training on identity tags is not what these cells embody.

## Confidence

Source quality is very high: Nature publication, replicable methodology, large neuron yield, peer-reviewed and cited thousands of times. Mapping fidelity is moderate -- the paper supports the architectural plausibility of option A's supervision target (one-hot identity is what concept-cell firing looks like at readout), but it does not establish that the substrate Phase 2 should commit to one-hot rather than embedding. Transfer risk is substantial because the source domain is visual identity in human MTL and the target is goal identity in REE substrate. Aggregate 0.82, weighted toward source quality but discounted for the mapping caveat. The paper is best read as licensing option A as a plausible biological architecture, not as adjudicating against option B.

## How this enters the verdict

This entry pushes the verdict toward option A or toward a hybrid (option C) where option A's one-hot identity slot lives at the supervision target while a distributed substrate produces it. It does not adjudicate against option B on its own. The Schapiro-2016 entry pulls in the opposite direction.
