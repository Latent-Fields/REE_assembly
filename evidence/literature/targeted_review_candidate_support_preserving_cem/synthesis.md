# SYNTHESIS - Candidate-Support-Preserving CEM for V3 Proposal Repair

**Date:** 2026-05-14. **Entries:** 5 papers. **Primary claim:** ARC-065. **Cross-links:** ARC-018 and MECH-033 are design consumers, not directly tested by this pull.

## Why this pull was commissioned

V3-EXQ-563 showed that E3 score bias could not move action selection because the desired first-action class was absent from the candidate set. V3-EXQ-563a then used scaffolded action-class candidates and proved the E3 add-site and forced actuator are alive when a candidate support surface exists. The open engineering question is therefore local: how should the hippocampal/CEM proposal boundary preserve enough first-action support for E3, goal, curiosity, and tonic-vigor biases to be interpreted fairly?

## R1 - Is support collapse a plausible CEM failure, or a separate E3 failure?

**Verdict: CEM-LOCAL FAILURE PLAUSIBLE. Confidence 0.78.**

de Boer et al. 2005 is the anchor. CEM intentionally samples, ranks, selects an elite subset, and refits the proposal distribution toward those elites. If the elite subset contains only one first-action class, the next proposal distribution has no categorical evidence for absent classes. That makes V3-EXQ-563's collapse compatible with ordinary elite-refit mechanics and supports the current interpretation: score bias and motivation cannot act on alternatives that the proposer has erased.

**Implementation consequence:** add proposer diagnostics and non-contributory preflight checks before treating behavioural FAILs as evidence against E3, goal, curiosity, or tonic-vigor mechanisms.

## R2 - Should the first repair be a new motivation term?

**Verdict: NO. Keep the repair at the proposal boundary. Confidence 0.76.**

iCEM (Pinneri et al. 2021) is the closest MPC/CEM repair model. Its changes are proposal-side and conservative: memory, correlated action sequences, momentum/refit changes, and executing evaluated actions. It does not justify a new REE drive. Information-theoretic MPC (Williams et al. 2017) reinforces the same diagnostic posture from another angle: the distribution of sampled trajectories and the scale of cost/bias terms matter to control.

**Implementation consequence:** `use_action_class_scaffold_candidates` remains diagnostic, default off. `use_support_preserving_cem` should also be default off, experimental, and instrumented. Do not make scaffolds always dominate normal CEM.

## R3 - What support-preserving option is least distorting?

**Verdict: MINIMAL SUPPORT FLOOR BEFORE MIXTURE CEM. Confidence 0.68.**

Moss 2020 weakly supports mixture proposals as a way to combat local-minima convergence, but it is too indirect and too broad for the first V3 repair. A full mixture proposer would change the architecture more than the current evidence requires. The smallest live-path test is:

- run normal CEM;
- inspect first-action class support;
- if support is below a floor, inject or preserve minimal one-hot first-action candidates for missing classes;
- record which candidates were injected and whether support preservation changed selected actions.

This tests whether a support-preserving intervention actually touches the live proposal path without committing to a permanent mixture-distribution architecture.

## R4 - Should categorical-first proposal be implemented now?

**Verdict: LATER OPTION ONLY. Confidence 0.62.**

Jang et al. 2017 gives a credible implementation family for future categorical-first-action proposal stages. It is relevant because REE's support failure sits at a categorical first-action boundary. But it is a differentiable discrete-latent method, not a CEM repair. It should not be imported for V3-EXQ-563b.

**Implementation consequence:** keep categorical-first / Gumbel-Softmax out of the patch. Mention it as a later design option if minimal support preservation fails.

## Design bottom line

V3-EXQ-563a proves E3 can use score bias when candidate support exists. The next repair should make the candidate-support surface measurable and minimally reliable:

1. expose candidate support diagnostics from `HippocampalModule.propose_trajectories()`;
2. mark experiments non-contributory when support collapses;
3. preserve diagnostic scaffold candidates but keep them default-off;
4. add a weaker default-off `use_support_preserving_cem` flag;
5. run V3-EXQ-563b comparing normal CEM, scaffold support, and support-preserving CEM with weak forced-bias dose response.

Do not claim behavioural agency is solved until naturalistic selected-action entropy or task-relevant behavioural diversity improves without diagnostic scaffolding.
