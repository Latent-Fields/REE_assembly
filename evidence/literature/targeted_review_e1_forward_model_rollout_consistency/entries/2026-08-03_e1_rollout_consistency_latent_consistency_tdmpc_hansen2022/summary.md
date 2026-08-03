# Hansen, Wang & Su 2022 -- TD-MPC latent state consistency

**Claim(s):** MECH-135 | **Direction:** supports | **Confidence:** 0.76

## What the paper did

TD-MPC learns a Task-Oriented Latent Dynamics model (TOLD) and plans by local trajectory optimisation in its latent space, with temporal-difference value learning bootstrapping beyond the planning horizon. Three objectives are optimised jointly: reward prediction, TD value learning, and -- the part relevant here -- a **latent state consistency loss**.

That term (their Eq. 10) is `|| d_theta(z_i, a_i) - h_theta-(s_i+1) ||^2`: the action-conditioned latent dynamics prediction regressed onto the target-network encoding of the true next observation, accumulated over an **H-step unroll during training**. No observation is ever decoded -- the authors describe it as "circumventing prediction of observations altogether." They adopted it in preference to reconstruction and contrastive alternatives, reporting latent consistency as the more consistent choice.

## Why this is the most useful entry in the review

Of the papers surveyed here, this is the one I would actually hand to whoever implements the fix, because it is the only one that has all three of the properties REE needs *at once*.

**The objective transposes with no reinterpretation.** PlaNet's latent overshooting is a KL between distributions in a variational model; getting it into E1's deterministic MSE setting requires an argument. TD-MPC's consistency term is already an ordinary squared error between a predicted latent and a detached encoder target. It is the same shape as E1's existing loss. You would be adding a term, not changing loss families.

**The training horizon is the planning horizon.** The H-step unroll is the concrete, implemented form of "train at the horizon you plan at." For REE that means unrolling E1 toward its 30-step scoring horizon instead of the current `horizon=1`.

**The dynamics function is `d(z, a)`, not `d(z)`.** This is the property that, on my reading of the code, is logically prior to everything else in this review. A consistency term over `d(z, a)` constrains how the latent trajectory differs *between* action sequences. That is precisely the quantity C3 measures -- `e1coe_score_var` is the variance of goal-proximity scores across forty different action sequences -- and it is a quantity an action-blind model cannot express no matter how well trained.

It also gives an empirical data point on the autopsy's third candidate. The sibling E2 review's leading recommendations were contrastive and MI-based objectives; TD-MPC's authors compared latent consistency against contrastive and reconstruction alternatives and went with consistency. That is not decisive -- different setting, different failure -- but it is directly relevant, and it cuts against assuming the E2 conclusions carry over.

## Limitations

Four, and none of them is fatal but the last is a scope warning.

The consistency term is one of three jointly-optimised objectives, and the paper does not ablate it against long-horizon rollout *distinctiveness* specifically. Its contribution to the quantity REE cares about is inferred from the form of the objective, not measured. TD-MPC's planning horizon is short -- single digits -- against REE's thirty, and nothing here establishes the technique holds at that depth.

TOLD is *task*-oriented by design: trained to model what matters for reward and to discard the rest. E1 is not task-oriented. It is a general world model with several consumers besides the goal evaluator -- `generate_prior` feeds HippocampalModule terrain conditioning (SD-002), `cue_action_proj` produces the MECH-151 action_bias into E2, `schema_readout_head` produces MECH-216 schema salience. Importing a task-oriented objective wholesale would optimise E1 for the evaluator at those consumers' expense. Whatever is adopted here needs to be additive rather than a replacement of E1's training signal.

And the scope warning: the action-conditioning that makes this template attractive is exactly what E1 lacks. Adopting it means changing E1's *interface* -- `predict_long_horizon(current_state, horizon)` gaining an action argument, and every call site updating -- not merely adding a loss term. That is a larger piece of work than `substrate_queue.json`'s current implementation hint ("add a multi-step/rollout-consistency term to E1's training objective") implies, and whoever picks up SD-e1-rollout-consistency-training should know that before scoping it.

## Confidence reasoning

Source quality 0.86 -- ICML 2022, strong results (near 10x sample-efficiency improvements on DMControl Humanoid and Dog), widely adopted and extended in TD-MPC2. Mapping fidelity 0.74, the highest here, because the objective's form transposes cleanly and the multi-step-plus-action-conditioned combination is exactly where this review's evidence converges. Transfer risk 0.35 for the task-oriented-versus-general-world-model tension and the horizon gap.

Aggregate 0.76, direction **supports**. This is the blueprint. It is also the entry that makes clearest why the fix is bigger than one loss term.
