# Ito et al. 2015 — A prefrontal-thalamo-hippocampal circuit for goal-directed spatial navigation

According to PubMed: Ito, Zhang, Witter, Moser & Moser. *Nature* 522:50-55 (2015). [DOI 10.1038/nature14396](https://doi.org/10.1038/nature14396). PMID 26017312.

## What the paper did

Rats ran a Y-maze task with two consistent reward locations. The authors recorded simultaneously from medial prefrontal cortex, nucleus reuniens of the ventral midline thalamus, and dorsal hippocampal CA1 and CA3 — and then optogenetically silenced reuniens during the task.

Trajectory-dependent firing — neuronal activity that distinguishes which goal the animal is heading toward, beyond simple place coding — was abundant in mPFC, in reuniens, and in CA1. It was essentially absent in CA3. Optogenetic silencing of reuniens substantially reduced trajectory-dependent firing in CA1 without affecting place-cell firing per se. The CA3-vs-CA1 dissociation is the architecturally decisive observation: CA3 does not receive reuniens input, and CA3 does not show trajectory-dependent firing. CA1 receives reuniens input, and CA1 shows trajectory-dependent firing that depends on that input.

## Why this matters for REE's question

The REE question is whether frontal subdivisions read rich content out of a posterior associative store via top-down query, or hold compact goal handles directly. Ito 2015 reverses the user's intuition. In the goal-directed-navigation regime, the *direction of information flow* is PFC → thalamus → HPC: the prefrontal cortex holds something that functions as a compact goal-context handle and routes it through reuniens to bias hippocampal trajectory representation downstream. The rich trajectory is constructed in CA1, but only because PFC has sent down the goal-context that shapes what kind of trajectory CA1 generates.

This maps directly onto REE V3's existing path. `GoalState.z_goal` flows into `HippocampalModule.propose_trajectories` and biases what the proposer generates. The MECH-293 ghost-goal probe search, where seeds are drawn from anchors whose `z_goal_snapshot` cosine-matches `current z_goal`, is functionally close to what reuniens does biologically: route a goal-keyed query into the rich substrate to bias which trajectory is generated. The frontal substrate doesn't need to "read out" rich HPC content for itself — it sends the compact handle down, and the rich downstream representation falls out of the receiving substrate's own dynamics.

## What it does NOT settle

The paper does not show that *no* HPC content goes back up to PFC — it doesn't address the encoding-direction question that Spellman 2015 covers. Goal-directed navigation might be a special case where the dominant traffic is top-down; encoding events of *new* goals might involve much heavier bottom-up traffic. The two papers together suggest a phase-and-context-dependent split: encoding events run HPC → PFC; goal-directed retrieval runs PFC → reuniens → HPC.

REE has no explicit reuniens-analogue substrate. The thalamic routing role is collapsed into the `GoalState → HippocampalModule` call chain (`z_goal` is the routed signal). This is biologically functional but architecturally lossy: there is no node where "PFC sends, thalamus sustains, HPC receives" is explicit. If REE wanted this explicit, it would be a new SD covering frontal-thalamo-hippocampal routing. Whether that is worth doing depends on whether the V3 dynamics are suffering from the absence of such a node — the EXQ-490 / EXQ-490b factorial on V_s gating is a more pressing path before this becomes architecturally load-bearing.

## Confidence reasoning

I sit this at 0.85. Source quality 0.92 — *Nature*, Moser lab, simultaneous three-region recording, optogenetic causal manipulation, the CA3-vs-CA1 anatomical dissociation as an internal control. Mapping fidelity 0.78 because the architectural finding maps cleanly onto REE's GoalState-driven proposer path. Transfer risk 0.25 because the regime under study is exactly the regime REE is trying to capture in V3.
