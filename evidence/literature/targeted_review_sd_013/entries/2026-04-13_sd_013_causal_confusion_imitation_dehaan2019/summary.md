# Causal Confusion in Imitation Learning -- de Haan, Jayaraman, Levine (NeurIPS 2019)

## The Central Observation

There is something deeply disquieting about a system that learns to do the right thing for the wrong reasons. De Haan, Jayaraman, and Levine formalize precisely this problem: a policy trained on observational demonstrations learns the correlational distribution P(action | observation), not the interventional distribution P(action | do(observation-component)). When the training distribution contains spurious correlations -- features that co-occur with correct actions through non-causal paths -- the policy assigns causal credit to the correlate rather than the cause. The result looks fine in-distribution but degrades catastrophically when the spurious correlation breaks. The paper calls this causal confusion.

## Why This Matters for SD-013

SD-013 is a claim about a forward model (E2_harm_s), not a policy, but the underlying epistemic situation is identical. E2_harm_s trained on observational rollouts learns P(z_harm_s_next | z_t, a) -- the correlational distribution. In confounded states, this diverges from P(z_harm_s_next | do(a)) -- what harm would actually result if the agent intervened with action a from state z_t. The confounding structure in SD-013 is the agent's own presence in hazard-proximal regions: an agent that tends to be near hazards when harm occurs will produce training data where elevated harm correlates with both a_actual and a_cf, compressing the difference signal (causal_sig) toward zero. E2_harm_s then learns that harm is ambient -- a function of proximity -- rather than agentic -- a function of specific action choices.

## The Remedy and Its REE Instantiation

The paper's proposed remedy is targeted intervention: actively probe the environment with actions specifically chosen to break spurious correlations. This cannot be accomplished through passive observation, however rich the dataset. The paper shows empirically across continuous control and autonomous driving domains that targeted interventional data collection is sufficient to recover the causal policy -- and that adding more correlated observational data without interventional disambiguation can worsen causal confusion rather than remedy it. The REE-level analogue (ARC-033) requires explicit counterfactual perturbation steps in E2_harm_s training: actually execute a_cf from the same confounded state and observe the resulting z_harm_s trajectory. Observational rollout alone, regardless of quantity, cannot break the symmetry.

## Confidence and Caveats

This is a high-quality NeurIPS paper with empirical validation across multiple domains and a theoretically grounded argument. The mapping to SD-013 is structurally sound but involves a domain shift: the paper addresses policy learning (imitation), while SD-013 concerns forward model training. The confounding source also differs -- de Haan et al. focus on spurious correlational features in the observation space, while SD-013's confounder is the agent's behavioral tendency to occupy hazard-proximal states. These differences are real but do not undermine the core argument. If anything, forward model training is more vulnerable to observational bias because the model must not merely predict but support downstream causal reasoning -- causal_sig is only interpretable if P(z_harm_s | do(a_actual)) and P(z_harm_s | do(a_cf)) are the distributions being compared.

## Summary

De Haan et al. 2019 provides the clearest computational demonstration that observational training systematically produces causal confusion when spurious correlations are present, and that targeted interventional data collection is the necessary remedy. This directly supports SD-013's claim that E2_harm_s requires counterfactual perturbation signal -- not as a design preference but as a logical requirement for causal identifiability.
