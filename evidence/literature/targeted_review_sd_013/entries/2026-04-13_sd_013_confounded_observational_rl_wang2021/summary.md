# Provably Efficient Causal RL with Confounded Observational Data -- Wang, Yang, Wang (NeurIPS 2021)

## The Formal Problem

Wang, Yang, and Wang pose a question that deserves to be asked more often in machine learning: what is the cost of not knowing which part of your data is causal? They model this as a confounded MDP in which an unobserved context variable C influences both the behavioral policy and the reward or transition dynamics. The observational data distribution therefore conflates the effect of the agent's action with the effect of C that co-occurs with that action under the behavioral policy. They prove that no algorithm using only observational data from this distribution can achieve the regret attainable under unconfounded interventional data -- the confounding bias is formally irreducible.

## The Structural Argument and SD-013

This is exactly the structural problem SD-013 identifies for E2_harm_s. The training data for E2_harm_s comes from a behavioral agent navigating an environment where its own policy induces confounding: the agent tends to occupy hazard-proximal states when harm is elevated, so observational data correlates elevated harm with both a_actual and a_cf in those states. The unobserved context C in Wang et al.'s formalism corresponds, in the REE setting, to the agent's state-conditioned behavioral tendency. E2_harm_s trained on this data learns to predict harm as a function of that correlated trajectory -- not as a function of the action actually taken. The result is a causal_sig that is systematically compressed: the model predicts similar harm for a_actual and a_cf precisely because both were executed by a policy that tends to be near hazards in confounded states.

## Adjustment and the ARC-033 Requirement

Wang et al. show that causal adjustment is necessary and sufficient to recover the interventional quantities. Their adjustment relies either on instrumental variables -- variables that influence action independently of C -- or on interventional samples that break the confounding directly. In the REE framework, the counterfactual perturbation steps mandated by ARC-033 function as interventional samples: executing a_cf from the same state z_t, independently of the behavioral policy's correlational tendencies, produces a z_harm_s observation that is causally attributed to a_cf rather than to the confounded state-occupancy pattern. Observational rollouts, however numerous, cannot provide this. Wang et al. prove this rigorously; ARC-033 instantiates the remedy.

## Mapping Caveat

The paper's formal results address value function estimation and policy regret, not forward model prediction error directly. The formal gap between policy critic and forward model is not negligible -- one might ask whether E2_harm_s is being asked to estimate a value function or a transition distribution. The answer is: neither exactly, but both structurally. E2_harm_s must produce predictions that support interventional reasoning (causal_sig = E2_harm_s(z_t, a_actual) - E2_harm_s(z_t, a_cf)), and for causal_sig to be interpretable it must approximate the interventional distribution, not the observational. Wang et al.'s formal bounds apply to any quantity that requires identifying P(outcome | do(a)) from data generated under a confounded behavioral policy, which is precisely the SD-013 setting.

## Summary

Wang et al. (2021) provide rigorous theoretical justification for SD-013: confounding in training data produces bias that is formally irreducible without causal adjustment, and no amount of additional observational data removes this bias. The ARC-033 counterfactual perturbation requirement is the implementation of the adjustment that Wang et al.'s theory requires. This is one of the strongest formal supports for SD-013's necessity claim.
