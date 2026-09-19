# Which Mutual-Information Representation Learning Objectives are Sufficient for Control? (Rakelly et al., NeurIPS 2021)

## What the paper did

Rakelly and colleagues take a question that the representation-learning literature had mostly left implicit -- *does this objective actually keep what a controller needs?* -- and make it formal. They define sufficiency of a state representation for learning and representing the optimal policy, and then run several popular mutual-information objectives through that definition. The results are proofs with explicit counterexamples, corroborated on a simulated visual game environment. Three objectives are adjudicated: forward information (predict the next latent from the current latent and action), state-only transition information (predict a future latent from the current one, no action), and inverse information (predict the action from a latent pair). Forward information is proved **sufficient for all reward functions**; state-only transition information and inverse information are proved **not** sufficient, "given mild and common assumptions on the structure of the MDP".

I want to record that I checked this attribution twice, because the first automated reading I got of the PDF had it backwards -- it reported forward information as one of the insufficient pair. The verbatim propositions say otherwise, and this matters here: which objectives are insufficient is the whole load of the paper for us.

## The sentence this entry turns on

The paper's own discussion contains the line that speaks directly to SD-106:

> "Of the objectives studied in our analysis, only J_fwd is sufficient to represent optimal Q-functions for any reward function. Note however that the representation obtained by this objective lacks a notion of 'task-relevance' as it must be equally predictive of all predictable elements in the state."

That is the formal name for the position SD-106 is in. SD-106 optimises a scale-normalised fraction-of-variance-unexplained term with its own linear decoder -- a task-agnostic criterion -- and V3-EXQ-1041 measured it reaching 0.951-0.980 of the achievable PCA-32 ceiling. It is being equally predictive of all predictable elements, and doing so close to optimally. There is no term in the objective by which a decision-relevant direction can outbid a merely high-variance one.

## How this translates, and where the translation stops

The honest reading is that this paper **splits** rather than settles. Its theorem defends genericity: a generic predictive objective can be sufficient, so there is no general principle condemning SD-106's shape. Its discussion undercuts genericity in exactly the regime SD-106 occupies. The reconciliation is the distinction between sufficiency and allocation. Sufficiency here is information-theoretic and capacity-unbounded -- it asks whether the information survives the encoder, not whether a fixed-width code spends its dimensions well. SD-106's deficit cannot be a retention failure of that kind, because the code is near its own linear ceiling; it is an allocation question, and these propositions are silent on allocation.

Two further boundaries, both real. Reconstruction is **not** among the analysed objectives -- the authors only conjecture in discussion that the ELBO alone cannot sufficiently control representation content -- so carrying the J_fwd task-relevance remark across to SD-106's FVU objective is an argument from family resemblance, not an instance of a proof. If anything reconstruction sits weaker than J_fwd in this ordering: it is predictive of the *observation* rather than of the dynamics, so a direction can be reconstructible and dynamically inert. And the analysis is over reward functions, whereas SD-106's consumer rung is scored as agreement with an oracle *action*.

## The warning that cuts the other way

It would be easy to read this pull as "task-conditioning is the fix" and stop. This paper is the entry that forbids that. The two objectives it proves **insufficient** -- state-only transition information and inverse information -- are both more task-shaped than plain reconstruction, and an inverse-model-flavoured successor to SD-106 could therefore be strictly worse on the paper's own analysis. Whatever replaces or augments the generic term has to be chosen against this result, not merely in the direction of "more task-relevant".

## Confidence

0.72. Source quality is high (NeurIPS, proofs with stated assumptions and explicit counterexamples, from a group central to this literature). The limiting component is mapping fidelity at 0.68, and deliberately so: the sentence REE leans on is an acknowledged limitation in the discussion rather than one of the paper's results, and the objective SD-106 actually ships is not among those proved on. Transfer risk is moderate (0.38) rather than high because the structural setting -- a bounded latent trained by a task-agnostic predictive objective and read by a downstream control consumer -- is the paper's own.
