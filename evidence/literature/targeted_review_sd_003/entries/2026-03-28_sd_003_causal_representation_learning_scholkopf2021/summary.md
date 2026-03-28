# Scholkopf et al. (2021) — Summary for SD-003

**Source**: Scholkopf, B., Locatello, F., Bauer, S., Ke, N.R., Kalchbrenner, N., Goyal, A., & Bengio, Y. (2021). Towards Causal Representation Learning. *Proceedings of the IEEE*, 109(5), 612-634. DOI: [10.1109/JPROC.2021.3058954](https://doi.org/10.1109/JPROC.2021.3058954) / arXiv: [2102.11107](https://arxiv.org/abs/2102.11107)

## What the Paper Did

This is a high-level theoretical review bridging Pearl's do-calculus framework for causal inference with the representation learning literature in machine learning. The central argument is that most learned representations encode correlational statistical structure from observational data, which is insufficient for transfer, generalisation, and counterfactual reasoning. Representations must instead encode the underlying structural causal model (SCM) -- the generative mechanism governing how variables relate under interventions, not just how they co-vary in the observational distribution. The paper frames causal representation learning as the problem of discovering high-level causal variables and their relationships from raw observations.

The core technical content covers: (1) the distinction between observational, interventional, and counterfactual distributions; (2) why representations that support P(Y | X) do not in general support P(Y | do(X)); (3) identifiability conditions for causal variables under independence assumptions; and (4) proposed research directions for learning representations that support interventional and counterfactual queries.

## Key Findings Relevant to SD-003

SD-003 requires E2_harm_s to compute interventional distributions: P(z_harm_s_next | do(a_actual)) and P(z_harm_s_next | do(a_cf)). Scholkopf 2021 provides the formal theoretical framework for understanding when and how a learned forward model can serve this role.

The central relevant claim is that most learned models trained on observational data encode P(z_harm_s_next | z_t, a) -- the conditional distribution -- rather than P(z_harm_s_next | do(z_t, a)) -- the interventional distribution. These differ when there are confounders: variables that influence both the action taken and the harm-stream outcome independently of the causal path through the action. If E2_harm_s encodes a correlational model, causal_sig will be a biased estimate of the true causal contribution.

The paper argues this is not a minor technical detail but a fundamental architectural requirement: representations must be causally disentangled before they can support interventional queries. This directly motivates the ARC-033 design decision to treat E2_harm_s as a structural forward model with an explicit causal architecture (harm-stream observations, distinct from world-stream latents) rather than a generic regression target.

## Translation to REE / SD-003

The paper provides the formal justification for why SD-003 cannot simply use a standard regression-trained E2 for causal_sig. A regression-trained E2 minimises prediction error on observational trajectories but learns P(z_harm_s_next | z_t, a) rather than P(z_harm_s_next | do(a)). When the environment has confounders (e.g., certain situations where both the agent and the environment are more likely to produce harm simultaneously), E2's predictions under a_cf will be biased by the observational correlation, not the interventional distribution.

SD-003's design -- using the difference between two E2 evaluations as causal_sig -- is a step toward isolating the interventional from the observational distribution, but the step is only complete if E2 is trained with interventional signal. This points toward a specific implementation requirement: E2_harm_s should be trained with at least some counterfactual perturbations, where the actual action is replaced by a_cf and the resulting harm-stream change is observed. This is the REE-level analogue of the multi-environment or intervention-based training Scholkopf 2021 identifies as necessary for causal identifiability.

## Limitations and Caveats

The paper addresses the static causal graph discovery problem (identifying causal structure over a fixed set of observed variables with i.i.d. data), not the dynamic sequential action-conditional causal attribution SD-003 requires. SD-003 operates at each timestep in a Markov chain, computing an action-conditional forward prediction for two specific actions -- this is a different and harder problem than static causal discovery. The identifiability conditions the paper identifies apply to the static setting; their extension to sequential, non-i.i.d., action-conditional forward modeling is not straightforward. The paper motivates the problem and frames the formal requirements; it does not provide convergence guarantees for SD-003's specific implementation.

## Confidence Reasoning

Confidence 0.71. Proc IEEE, senior authors (Scholkopf, Bengio), influential theoretical contribution. The formal framing of interventional vs. observational distributions is directly relevant to SD-003's correctness requirements. The moderate confidence reflects the gap between static causal discovery and dynamic sequential forward modeling, and the fact that the paper motivates requirements without directly validating SD-003's specific architecture.
