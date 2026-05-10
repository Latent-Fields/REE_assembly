# Solway et al. 2014 -- Optimal Behavioural Hierarchy

## What the paper did

Solway, Diuk, Cordova, Yee, Barto, Niv and Botvinick derived a normative account of what makes a behavioural hierarchy optimal for a given distribution of tasks. The optimum balances two terms: the task-decomposition entropy (how cleanly the task structure is captured by the hierarchy) and the reusability of subroutines across tasks. They show analytically that the optimal hierarchy is characterised by *bottleneck states* -- states that lie on many task trajectories -- and that subroutines naturally form around getting to and from those bottlenecks. They then run four behavioural experiments showing that humans, given novel maze tasks, spontaneously discover hierarchies close to the optimum.

## Key findings relevant to the rule-apprehension vocabulary question

For Pull 4, this paper supplies the *normative target* that ARC-064 (bottom-up rule discovery) and MECH-316 (cross-episode-regularity-extraction) should be approximating. Two specific transfers:

1. **An explicit objective function for option-discovery.** Solway's hierarchical-cost objective gives REE a candidate loss to drive MECH-316 / MECH-317 training, with a normative justification rather than an ad-hoc one.

2. **A falsifiable empirical prediction.** In environments with identifiable bottleneck states, the discovered behavioural chunks should align with those bottlenecks. This is a directly testable signature for a future REE substrate-validation experiment -- ideally a multi-room grid environment where doorways are obvious bottlenecks. If MECH-316 chunks produced by ARC-064 do not concentrate at bottlenecks, the substrate is implementing something other than optimal decomposition.

## How the findings translate to REE

The translation is conceptually clean. ARC-064 should be re-stated as "approximate Solway-optimal hierarchy discovery", with MECH-316 doing the bottleneck-state identification (closely related to graph-theoretic / successor-representation-based methods, see Stachenfeld 2017 already in Pull 2) and MECH-317 doing the chunk formation around those bottlenecks.

The vocabulary contribution is "bottleneck state" as a primitive. REE has nothing equivalent in its current claim registry -- "context" and "rule" are coarser. Adopting the Solway vocabulary gives REE a precise way to talk about *where* options should form, not just that options should form.

## Limitations and caveats

The optimal-hierarchy derivation assumes a fixed task-distribution prior. In REE's open-ended online setting, the task distribution is implicit and changes over time -- so Solway optimality is a moving target. The bottleneck-state definition also assumes a reasonably well-defined state-transition graph. In continuous-state environments, bottleneck identification needs a soft / density-based version (graph-Laplacian methods, eigenvector decomposition of the successor representation -- Stachenfeld 2017 already covers this).

The behavioural experiments are simple grid mazes. The transfer to richer substrate is plausible but not free -- in particular, the result may break down in environments where the optimal hierarchy is sensitive to task ordering, or in environments where multiple bottleneck candidates compete. Those edge cases are exactly where REE's monomodal-collapse failures live; whether Solway-optimal-hierarchy discovery is robust to them is an open empirical question.

## Confidence reasoning

Scored 0.79. Source quality is high (PLOS Comp Biol, peer-reviewed, open-access, code released). Mapping_fidelity is high (0.78) because this is the most explicit normative-target paper for bottom-up hierarchy discovery in the literature. Transfer_risk is moderate-high (0.40) due to the fixed-task-distribution assumption and the discrete-graph bottleneck formalisation, both of which need softening for REE's continuous online substrate. The paper feeds R2 (this is an inheritable formal result REE can adopt) and R4 (it argues for adding "bottleneck state" to REE vocabulary, as a lower-level primitive than "rule" or "context").
