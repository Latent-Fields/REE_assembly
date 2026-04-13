# Model-Based Reinforcement Learning Under Confounding -- Venkatesh and Malikopoulos (2025)

## The Question That Should Have Been Asked Sooner

Most model-based RL papers treat the learned transition model as a faithful surrogate for the environment. Venkatesh and Malikopoulos ask what happens when the data generating that model is confounded -- when an unobserved variable C correlates both with the behavioral policy and with the transition dynamics. Their answer is stark: the model is fundamentally inconsistent. It does not converge to the interventional distribution P(s' | do(a)) even with infinite data. It converges to something else: the distribution of next states conditioned on the behavioral policy's action, which encodes the confounding correlation rather than the causal mechanism.

## The SD-013 Connection

This paper provides the closest structural match to SD-013's claim among the available literature. E2_harm_s is a forward model -- a transition model for the harm stream z_harm_s -- and it faces exactly the confounded training data problem Venkatesh and Malikopoulos analyze. The agent's behavioral policy in the REE training environment will tend to occupy certain states when harm is elevated; this tendency is an unobserved contextual variable from E2_harm_s's perspective, and it induces the confounding that makes the learned model inconsistent. SD-013's specific prediction -- that causal_sig will be unreliable or compressed in confounded states -- follows directly from the paper's inconsistency result: if E2_harm_s does not represent P(z_harm_s | do(a)), then E2_harm_s(z_t, a_actual) - E2_harm_s(z_t, a_cf) is not the interventional contrast it needs to be.

## The Remedy: Proximal Adjustment vs. Counterfactual Execution

The paper proposes a proximal adjustment approach using proxy variables correlated with the unobserved context. This is technically elegant -- it requires no additional environment interactions, only the right proxy variables. ARC-033 takes a different path: explicitly execute a_cf from the confounded state and observe the resulting z_harm_s. These are two implementations of the same necessary move: break the confounding. The proximal approach works without new interactions but requires identifiable proxy variables; the ARC-033 approach requires environment access but makes no proxy assumptions. For an active learning agent -- which is what the REE agent is -- counterfactual execution is the more tractable route. The paper's necessity argument is independent of which remedy is chosen: some form of adjustment is required, and no observational training alone will substitute for it.

## Caveats

This is an arXiv preprint from December 2025 and has not undergone peer review at a major venue. The theoretical framework uses contextual MDPs, and the specific structure of E2_harm_s's confounding (behavioral policy correlation with harm-proximal state occupancy) is not an exact instance of the C-MDP formalism. These are real limitations. The core inconsistency result, however, follows from arguments that are standard in causal inference -- unconfounded estimation requires either adjustment or interventional data -- and is unlikely to be overturned by peer review. The structural match to SD-013 is the strongest of any paper in this review.

## Summary

Venkatesh and Malikopoulos (2025) prove directly that transition models trained from confounded offline data are fundamentally inconsistent for evaluating interventional quantities. This is the forward-model-level instantiation of the problem SD-013 identifies for E2_harm_s. The paper corroborates both the diagnosis (observational training is insufficient) and the logical structure of the remedy (some form of adjustment or interventional sampling is necessary), providing strong theoretical grounding for ARC-033's counterfactual perturbation requirement.
