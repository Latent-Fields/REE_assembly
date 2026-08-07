# Optimum release time (Okumoto & Goel, 1980) -- Q-087

**Direction: supports (confidence 0.55)**

## What the paper did

Okumoto and Goel take the Goel-Okumoto non-homogeneous-Poisson-process software failure model and ask a decision-theoretic question on top of it: *when should testing stop and the system be declared ready for operational use?* Their answer is that this depends on two things -- the model of the failure phenomenon, and, crucially, **the criterion chosen for evaluating readiness**. They work through two such criteria, a reliability threshold and a total-expected-cost criterion, and derive an optimum release policy for the cost case, then study its sensitivity to the model parameters. It is a foundational, heavily-cited paper in the software-reliability-growth-model (SRGM) literature.

## Why it bears on Q-087

Q-087 asks what *event* counts as V3 closure for the purpose of the version-transition freeze gate (GOV-V3FREEZE-1) and the opacity-repayment boundary (GOV-OPACITY-1). The candidate options were a strict green board (all closure nodes/tests pass), governance acceptance (a decision records it), or green-board-plus-a-reproducibility-check. The user's 2026-08-01 decision chose governance acceptance, explicitly reasoning that a strict green board "may never fire" (nine nodes were blocked and a target date had already slipped), which would leave the gate permanently inert.

Okumoto and Goel's framing is the same shape of argument, one substrate down. Their entire contribution is that "ready to release" is not the passive arrival of a defect-free state -- exhaustive removal of faults is neither achievable nor the natural stopping point -- but a **decision made against an explicitly chosen criterion under residual uncertainty**. That is precisely the move Q-087 makes: it replaces "closed when everything is green" (a completeness criterion that may never be met) with "closed when a governance decision records it against a criterion." The paper grounds the resolution's core reasoning that a completeness-style gate is the wrong instrument.

## Mapping, honestly

The transfer is analogical, not literal, and I have kept the confidence at 0.55 to reflect that. Okumoto-Goel optimise a *continuous timing* decision on a converging reliability curve for a single deployed product, and they still require a **quantifiable metric** (a reliability function, a cost model). Q-087 deliberately chose a **non-metric** governance event -- a human decision recorded in a decision_log, independent of node count -- precisely *because* the metric may never complete. So the paper supports the framing ("readiness is a chosen criterion, not emergent completeness") but cannot support the specific choice of a non-metric decision over a metric one; if anything its own apparatus assumes the metric exists. It also addresses operational readiness of software for users, not the freezing of a research substrate as a manipulable causal reference, which is half of GOV-V3FREEZE-1's rationale.

## Confidence reasoning

Source quality is high (canonical peer-reviewed work). Mapping fidelity is moderate (0.5): the decision-theoretic skeleton maps cleanly, the metric/cost flesh does not. Transfer risk is moderate-to-high (software-product-timing to governance-milestone-definition is a real domain jump). Because Q-087 is a governance judgement call, no empirical paper can *settle* it; the literature can only show that its reasoning is the standard reasoning in an adjacent field, which is what this entry does.
