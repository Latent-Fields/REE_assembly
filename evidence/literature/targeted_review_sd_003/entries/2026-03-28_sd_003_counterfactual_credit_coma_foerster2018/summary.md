# Foerster et al. (2018) — Summary for SD-003

**Source**: Foerster, J.N., Farquhar, G., Afouras, T., Nardelli, N., & Whiteson, S. (2018). Counterfactual Multi-Agent Policy Gradients. *Proceedings of the AAAI Conference on Artificial Intelligence*, 32(1). DOI: [10.48550/arXiv.1705.08926](https://arxiv.org/abs/1705.08926)

## What the Paper Did

COMA (Counterfactual Multi-Agent) proposes a policy gradient method for cooperative multi-agent reinforcement learning in which the credit assignment problem -- how to attribute shared team reward to the contribution of individual agents -- is solved using a counterfactual baseline. The architecture uses centralised training with decentralised execution: a centralised critic observes the full joint state-action space during training and produces a Q-function for each agent, while individual actors optimise their own policies from local observations.

The counterfactual baseline computes, for each agent i, the advantage function: A_i(s, a) = Q(s, a) - sum_a'_i [pi_i(a'_i | tau_i) * Q(s, (a'_i, a_{-i}))]. The second term marginalises out agent i's action while holding all other agents' actions fixed -- this is the counterfactual Q-value under agent i's policy distribution. The difference A_i isolates agent i's individual causal contribution to the joint outcome, above what would have occurred from the counterfactual marginal. The paper demonstrates significant performance improvements over non-counterfactual baselines in StarCraft unit micromanagement.

## Key Findings Relevant to SD-003

COMA provides the closest existing ML implementation to SD-003's causal_sig operation. The structural parallel is direct: a trained critic (E2 in SD-003 terms) is evaluated under the actual action (Q(s, a)) and under a counterfactual (E_pi[Q(s, a')]), with the difference extracted as the causal contribution signal (A_i = causal_sig). The paper demonstrates three things directly relevant to SD-003:

1. **Tractability**: The counterfactual forward-model difference is a learnable, convergent operation. Training a neural network critic to support this comparison is computationally feasible and produces stable gradients.

2. **Superiority over non-counterfactual baselines**: Removing the counterfactual baseline (using Q directly rather than A) significantly worsens credit assignment -- confirming that the counterfactual difference is doing real work and is not merely a computational convenience.

3. **Efficient single-pass computation**: The paper notes that COMA's architecture allows the counterfactual baseline to be computed efficiently in a single forward pass of the critic, by designing the output layer to cover all possible actions simultaneously. This suggests that the SD-003 causal_sig computation can be implemented efficiently without requiring a separate forward pass per counterfactual.

## Translation to REE / SD-003

SD-003 proposes causal_sig = E2_harm_s(z_t, a_actual) - E2_harm_s(z_t, a_cf). COMA demonstrates that this counterfactual difference operation, implemented as a trained neural forward model evaluated under actual and counterfactual actions, is a tractable, effective credit assignment mechanism. The multi-agent framing should not obscure the computational isomorphism: the COMA baseline does exactly what SD-003's causal_sig does -- it asks 'what would have happened if this agent had acted differently?' and extracts that difference as the causal attribution signal.

COMA also provides a specific architectural hint for SD-003 implementation: designing E2_harm_s to output harm-stream predictions for all possible actions in a single forward pass would allow causal_sig to be computed efficiently without doubling the inference cost.

## Limitations and Caveats

The mapping is not identical. COMA's counterfactual is over agent i's marginal action distribution (E_pi_i[Q(s, a'_i)]), not a specific counterfactual action. SD-003 uses a specific counterfactual action a_cf, which requires a mechanism for selecting which counterfactual to evaluate. COMA sidesteps this by marginalising over the policy distribution, which is a cleaner theoretical operation but a different one. The multi-agent setting also means the 'credit assignment' problem in COMA is about dividing team reward among cooperating agents, not about distinguishing self-caused from environment-caused outcomes, which is SD-003's purpose. The computational structure is shared; the semantic framing differs.

## Confidence Reasoning

Confidence 0.76. AAAI 2018, influential paper in multi-agent RL. The counterfactual forward model difference is structurally isomorphic to SD-003's causal_sig. The main caveat is the specific-vs-marginal counterfactual distinction and the multi-agent vs single-agent context. This is the strongest ML computational precedent for SD-003's tractability.
