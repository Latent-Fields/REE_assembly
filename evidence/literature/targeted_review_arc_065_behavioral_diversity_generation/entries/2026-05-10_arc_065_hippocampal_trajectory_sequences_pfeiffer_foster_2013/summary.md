# Pfeiffer & Foster 2013 — Hippocampal place-cell sequences depict future paths to remembered goals

[DOI](https://doi.org/10.1038/nature12112) · PMID 23594744 · *Nature* 497(7447):74–9

## What the paper did

Place-cell recording in freely-moving rats navigating an open arena with goal locations. Before each goal-directed movement, the hippocampus generates brief place-cell sequences encoding trajectories that progress from the rat's current location to a known goal. The sequences are biased toward the goal even when the start-goal combination is novel, demonstrating that hippocampal sequence generation is a goal-directed *trajectory-finding* mechanism, not just replay of previously-traversed paths.

## Why this matters for ARC-065

The paper grounds a third candidate substrate channel for behavioural diversity that does not fit cleanly into the noise-vs-curiosity dichotomy: *proposal-side diversity*. The intuition: even if the action-selection layer is fully deterministic and the curiosity bonus is silent, behavioural diversity can still emerge if the proposal layer (which trajectories enter the candidate pool for selection) generates multiple distinct options. Pfeiffer & Foster show the rat hippocampus is doing exactly this — sampling forward trajectories into candidate goals.

REE already has partial substrate for this via MECH-293 awake ghost-goal probes (which sample trajectories seeded from the MECH-292 ranked ghost-goal bank) and the CEM trajectory generator in HippocampalModule. ARC-065's MECH-315 candidate (proposal-diversity-channel) would extend this by making diverse trajectory sampling itself a load-bearing diversity-generation mechanism, separable from MECH-313 noise and MECH-314 curiosity. Whether MECH-315 needs to be a separate sub-MECH or can be absorbed into MECH-293 is a sub-cluster registration question to revisit during the ARC-064 lit-pull (which will go deeper into hippocampal proposal mechanisms).

## Limitations and confidence

The paper documents the existence of forward-trajectory sequences in rats; it does not directly establish that these sequences are *the substrate of behavioural diversity in the explore-exploit sense*. The diversity-generation interpretation is one inferential step beyond the paper's direct claim, but it is well-rehearsed in the hippocampal-MCTS literature (Mattar & Daw 2018, Pfeiffer 2020 review). Confidence aggregate 0.78 reflects the foundational venue and rigorous methods, with moderate mapping fidelity at the diversity-interpretation step.

## Failure signature it would falsify

An REE substrate that wires only action-selection-side diversity (MECH-313 noise + MECH-314 curiosity bias) but no proposal-diversity (only one trajectory enters the candidate pool per tick) should fail to reproduce goal-biased multi-trajectory sampling — and consequently should under-explore in environments where the optimal action requires committing to a multi-step plan that has not yet been tried.
