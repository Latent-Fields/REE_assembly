# Limanowski, Adams, Kilner & Parr 2024 -- The Many Roles of Precision in Action

**Source:** Limanowski J, Adams RA, Kilner J, Parr T (2024). *Entropy* 26(9):790. [DOI: 10.3390/e26090790](https://doi.org/10.3390/e26090790). PMID: 39330123.

---

## What the paper did

This is a review and theoretical synthesis published in a special issue of Entropy dedicated to Karl Friston. The paper's distinctive contribution relative to earlier active inference work is its focus on the multi-level role of precision in action: rather than treating precision as a single parameter, the authors trace how precision estimates function across the full action hierarchy, from discrete policy selection at the top, through trajectory planning, to continuous motor control and muscle activation at the bottom. The paper introduces and elaborates a class of "hierarchical mixed models" -- generative models that span both discrete levels (policy or mode selection) and continuous levels (trajectory execution and motor command) -- and argues that precision plays a qualitatively different role at each level.

## Key findings relevant to ARC-016

The paper articulates several points that bear directly on ARC-016. First, at the policy level, the basal ganglia are proposed as the anatomical substrate for encoding the precision of beliefs about policies (i.e., how confidently the system should commit to a particular course of action), with dopamine as the primary neuromodulator of this policy-level precision. Second, the hierarchical mixed model framework makes explicit that precision at the policy/mode level (discrete) and precision at the motor execution level (continuous) are distinct quantities requiring separate estimation -- they are not simply scalar multiples of each other. Third, the paper emphasises that inadequate precision estimates at any level produce characteristic failure modes: insufficient policy-level precision yields excessive exploration (inability to commit); excessive policy-level precision yields inflexibility (pathological commitment). These correspond directly to ARC-016's uncommitted and committed mode extremes.

## Translation to REE / ARC-016

ARC-016's circuit runs: E3-derived prediction variance -- commitment threshold -- BetaGate -- action selection. Limanowski et al. (2024) provide the most complete formal framework available in the active inference literature for understanding what each step of this circuit is doing. E3 functions as the agent that estimates and adjusts policy-level precision -- it is the circuit node that takes prediction errors and updates the confidence weight over competing policies (plans). The BetaGate implements the boundary between the discrete policy-selection level and the continuous execution level of the hierarchical mixed model: the gate determines whether the currently selected policy's precision is sufficient to drive committed execution. This is not simply an analogy; the hierarchical mixed model architecture is the formal computational structure that ARC-016 is a biological instantiation of. The paper thus provides the closest existing theoretical grounding for ARC-016 as a full circuit claim, not merely for one component of it.

## Limitations and caveats

The paper is a theoretical review, not a primary empirical study. The mapping from hierarchical mixed models to specific neural circuits remains partly programmatic -- the paper identifies the BG as the likely substrate for policy-level precision, and cites empirical support for dopamine's role, but the specific prefrontal mechanism computing prediction-variance-to-precision conversion (ARC-016's E3 role) is not anatomically specified in detail. More importantly for the threshold question: the paper generally treats precision as a continuous quantity that biases inference at each level, without explicitly modelling whether the transition between policy regimes is abrupt (threshold-gated) or gradual. ARC-016's BetaGate implies a commit-or-not threshold event; the hierarchical mixed model framework is formally compatible with either gradual or abrupt transitions, so this paper does not resolve the threshold-gating question.

## Confidence reasoning

Confidence 0.72. Source quality is good (Entropy, open-access, multiple well-regarded authors from UCL ICN and Oxford NDCNeuro, directly within the active inference research programme that ARC-016 draws on). Mapping fidelity is the highest of the three new entries: the hierarchical mixed model framework, BG as policy-precision substrate, and dopamine as the precision neuromodulator together constitute a nearly complete formal grounding for ARC-016's circuit. Confidence is moderated by the review nature of the paper and by the unresolved threshold-vs-gradient question. Transfer risk is low because the paper explicitly addresses cognitive action selection and commitment, not just motor execution.
