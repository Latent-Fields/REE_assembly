# Literature Summary: 2026-04-04_mech060_counterfactual_credit_assignment_mesnard2021

## Claims Tested

- `MECH-060`

## Source

- Mesnard T, Weber T, Viola F, Thakoor S, Saade A, Harutyunyan A, Dabney W, Stepleton T, Heess N, Hutter M, Buesing L, Munos R (2021), *Counterfactual Credit Assignment in Model-Free Reinforcement Learning*. ICML Proceedings 139: 7654-7664.
- DOI: 10.48550/arXiv.2011.09464
- URL: https://arxiv.org/abs/2011.09464

## Mapping to REE

MECH-060's write-boundary requirement states that pre-commit simulation error and post-commit realized error must be kept responsibility-distinct. This is not merely an architectural preference; it is a constraint whose violation should be detectable and harmful. The REE experimental evidence (EXQ-005, write_locus_contamination, PASS) confirms this in the specific domain of harm attribution. Mesnard et al. (2021) offer a complementary line of support from pure RL theory.

The authors address the credit assignment problem: given a trajectory of actions and returns, which actions deserve credit for which outcomes? Their solution is to train a future-conditional value baseline that estimates, for any action, what the return would have been under a counterfactual action -- had the agent chosen differently at that step. This counterfactual baseline is the ML analogue of MECH-060's pre-commit simulation channel: it computes the expected outcome of an action before (or independently of) that action's realized consequence. The policy gradient then uses the difference between the actual return and this counterfactual baseline as the error signal -- the realized-error channel.

The architectural detail most relevant to MECH-060 is the independence loss. Mesnard et al. impose a constraint that the counterfactual baseline must not encode information that is only available after the action executes -- specifically, it must be conditionally independent of post-action trajectory information given the action. This is the computational equivalent of write-boundary enforcement: the pre-commit simulation channel is not permitted to access post-commit realised information, which would create exactly the kind of contamination MECH-060 predicts is harmful. When this constraint is enforced, policy gradient variance falls and learning improves. When it is relaxed, the counterfactual baseline degenerates toward the actual return, collapsing the two channels.

The practical upshot for REE is that the case for write-boundary enforcement in harm attribution is not just neurobiologically motivated; it has a computational motivation in RL as well. Keeping the simulation channel from being contaminated by post-commit information preserves the signal-theoretic separation that makes the realized-error channel informative.

## Caveats and Mapping Limits

- The paper is in the model-free RL domain; there is no notion of harm attribution, residue fields, or moral responsibility. The mapping to MECH-060 is by analogy to the computational structure, not by domain equivalence.
- The write-boundary here is an optimisation constraint (reducing policy gradient variance) rather than a safety or responsibility constraint. This is a weaker motivation than MECH-060 requires.
- The independence loss is a soft regulariser, not a hard architectural gate. MECH-060's write-boundary enforcement is a harder constraint: the residue field simply does not receive pre-commit harm predictions at all, by construction. The RL analogy has a continuous relaxation; REE does not.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.60`
- Rationale: provides a well-motivated computational existence proof that separating simulated-outcome estimation from realized-outcome error is beneficial -- both in terms of variance reduction and learning performance -- with the independence loss acting as a functional analogue of write-boundary enforcement; confidence limited by domain mismatch and the softness of the separation mechanism.
