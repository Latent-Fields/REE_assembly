# Hafner et al. 2019 -- Latent overshooting (PlaNet)

**Claim(s):** MECH-135 | **Direction:** mixed | **Confidence:** 0.62

## What the paper did

PlaNet learns a latent dynamics model from pixels and plans by online search in that latent space. The part that matters for us is the training objective. The standard variational bound for a latent sequence model only ever ties the model's *one-step* prior to the filtered posterior. Hafner and colleagues observed that this leaves multi-step prediction -- the thing planning actually consumes -- untrained, and proposed **latent overshooting**: for every distance `d` from 1 up to some `D`, add a KL divergence between the model's `d`-step-ahead prior prediction and the corresponding filtered posterior, computed entirely in latent space with no image decoding. Gradients through the posteriors are stopped for `d > 1`, so the multi-step predictions are pulled toward the informed posteriors rather than the posteriors being dragged out to meet them. Their own one-line characterisation is the clearest statement of the idea I have found anywhere: latent overshooting "can be interpreted as a regularizer in latent space that encourages consistency between one-step and multi-step predictions."

That is, almost word for word, the property V3-EXQ-108b found E1 to lack. So this is the correct anchor paper for the first of the three candidate fixes the autopsy named, and it grounds that candidate as a precisely-specified objective rather than a vague direction.

## What the paper found -- including the part that cuts against it

Here is where I have to be careful, because the obvious reading of "latent overshooting is the anchor for candidate 1" is more favourable than the evidence supports.

The paper's own ablation (Appendix D) reports that latent overshooting **substantially helped purely stochastic recurrent models (DRNN)** but **slightly reduced performance of their proposed RSSM on all six tasks**. The authors say so directly: several dynamics models benefit from latent overshooting, "although our final agent using the RSSM model does not require it." And the follow-on work from the same group -- Dreamer (Hafner, Lillicrap, Ba, Norouzi, ICLR 2020) -- states in its hyperparameter appendix: "We did not find latent overshooting for learning the model, an entropy bonus for the action model, or target networks for the value model necessary."

So the technique is real, well-specified and canonically cited, but the field's own trajectory has been *away* from it. The natural reading of the ablation is that the benefit is architecture-conditional: a transition model with a deterministic recurrent path carrying state across steps already resists compounding error fairly well, and the extra multi-step KL then buys little and costs some capacity. A purely stochastic model, whose every step resamples, needs the multi-step tie far more.

## How this maps to REE

REE-v3's E1 is trained in the 108b driver by single-step MSE only (`agent.e1(total_prev, horizon=1)` against the next real transition) and then applied autoregressively thirty times to score each of forty candidate action sequences. That is precisely the objective/usage-horizon mismatch latent overshooting was designed for, and if the mismatch were the *whole* story this paper would be a clean prescription.

Two things stop it being one, and the second is serious enough that I would not want anyone reading only the record's headline direction.

First, the transposition. PlaNet's objective is a KL between distributions in a variational latent-state model. E1 is a deterministic LSTM emitting point predictions under MSE. You can transpose the idea -- an L2 consistency term between E1's `d`-step prediction and a detached encoder target at `t+d` -- and TD-MPC (Hansen et al. 2022, in this same review) shows that transposition working well. But what you transpose is the intuition, not the derivation; the variational justification does not survive the move.

Second, and this is the one that changes the recommendation: **PlaNet's transition model is action-conditioned and REE's E1 is not.** Latent overshooting regularises `p(s_t | s_{t-1}, a_{t-1})` over multiple steps. E1's interface, verified in `ree_core/predictors/e1_deep.py`, has no action argument anywhere -- `predict_long_horizon(current_state, horizon)` and `forward(current_state, horizon, z_goal)` take a latent and a horizon and nothing else. In the 108b scorer the candidate action only reaches z_world by a second-order path: action to E2 to z_self, then z_self into E1's `prior_generator` through a `world_dim` bottleneck that zeroes the z_self half of the LSTM input. Adding a multi-step consistency term to that model would make its one trajectory more self-consistent while leaving the forty candidates just as indistinguishable as they are now. A more self-consistent rollout is not the same thing as a more *discriminative* one, and it is discrimination that C3 measures.

## Confidence reasoning

Source quality is high and uncontroversial (ICML 2019, heavily cited, the canonical reference for the named technique). Mapping fidelity I put at 0.55 -- the failure mode matches beautifully in the abstract and matches poorly in the specifics, because of the action-conditioning gap and the variational-to-deterministic transposition. Transfer risk at 0.50 is unusually high for a paper of this stature, and it is earned: the ablation shows the sign of the effect flipping with transition architecture, and E1's deterministic LSTM sits on the side of that split where the technique did not help.

Aggregate 0.62, weighted down from source quality because for an architectural claim it is the mapping that decides, and here the mapping has a named hole in it. Direction is **mixed** rather than **supports** for the same reason: the paper grounds the candidate and simultaneously supplies the best available evidence that the candidate may not be the right one.
