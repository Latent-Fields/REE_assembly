# Asadi, Misra, Kim & Littman 2019 -- Direct multi-step models

**Claim(s):** MECH-135, INV-088 | **Direction:** mixed | **Confidence:** 0.68

## What the paper did

The argument is simple and, once stated, hard to unsee. Model-based RL almost always learns a *one-step* model mapping state and action to next state, then composes that model with itself to look further ahead. But "one-step prediction errors can get magnified" under self-composition, and the authors' point is that the composition is a *choice*, not a necessity. So they drop it: their multi-step model takes a state paired with a whole *sequence* of actions and directly outputs the resulting state. They report theoretical and empirical results showing this is more conducive to efficient value-function estimation and yields better action selection than the composed one-step model.

This entry does two jobs, pointing at two different claims, which is why its direction is **mixed** rather than **supports**.

## Job one: a fourth candidate, and it fits REE's usage better than the three we had

The V3-EXQ-108b autopsy named three candidate fixes -- latent overshooting, scheduled multi-step unrolling, contrastive next-state. All three share an assumption: that we keep composing E1 with itself thirty times and make the composition better behaved. Asadi and colleagues offer the option of not composing at all.

What makes this more than a curiosity for REE is a detail of how the evaluator actually works. `_score_sequence_e1coe_with_endpoint` iterates E1 thirty times, but look at what it returns: `score = goal_state.goal_proximity(z_world_curr)` on the *final* z_world. Every intermediate prediction is computed and thrown away. The evaluator wants a function from (start state, action sequence) to an endpoint score -- which is exactly the signature of Asadi et al.'s multi-step model. Building that directly would give the evaluator precisely what it consumes while removing the error-magnification mechanism entirely rather than regularising it.

I did not expect the fit to be that clean, and I think it deserves to be on the table when SD-e1-rollout-consistency-training is scoped, even though nobody has named it so far.

## Job two: literature grounding for the INV-088 dissociation

The paper's central claim is that one-step model quality and multi-step rollout quality are *decoupled* -- a model can be good at the former and useless at the latter, because the errors compound through the composition.

INV-088 asserts something close to the opposite for REE's evaluator: that world-goal-evaluator degeneracy is *bounded by* z_world's differentiation capacity. V3-EXQ-108b measured those two coming apart, with healthy real-state differentiation (CR_real 0.19-0.20) alongside a fully collapsed rollout (CR_rollout/CR_real around 3e-6). Governance has already confirmed the `weakens` reading for INV-088 on this pathway. What this paper adds is that the coming-apart is not an anomaly of REE's substrate -- it is the *expected* behaviour of composed learned models, and has been described as such in the model-based RL literature since 2019. That moves the 108b result from "surprising local finding" to "instance of a known and theorised failure family", which is worth something for the governance record.

## Limitations

The obvious objection to a direct multi-step model is combinatorial and the paper does not really confront it at our scale: the space of action sequences is |A|^H. For the 108b setting -- thirty steps over CausalGridWorldV2's action set -- that is astronomically larger than the forty sequences actually scored, so a sequence-conditioned model has to *generalise* across sequences it has never seen. The paper's empirical settings are much smaller than that, and I would not claim the result transfers to horizon 30 without a probe.

There is also a scope mismatch. E1 is a general world model with consumers beyond the goal evaluator -- HippocampalModule priors via `generate_prior`, the MECH-151 `action_bias` into E2, MECH-216 schema salience off the LSTM hidden state -- and all of those need the per-step trajectory. A sequence-to-endpoint model could not *replace* E1; it would be an additional evaluator-specific head. That is a larger and different design than `substrate_queue.json`'s current hint describes.

And on the INV-088 leg: this is a general argument about learned models, not a measurement of REE's substrate. It makes the dissociation *expected*. It does not independently confirm REE's instance of it -- 108b's own instrumentation does that.

## Confidence reasoning

Source quality 0.68 is the weak leg and I have set it deliberately low: strong group (Littman), genuine theory plus experiments, but it stayed an arXiv preprint rather than reaching a peer-reviewed venue, and the empirical scale is small. Mapping fidelity 0.76 -- high on both legs, because the endpoint-only usage in REE's scorer is an unusually exact fit for the direct multi-step formulation, and the decoupling argument is exactly the dissociation 108b measured. Transfer risk 0.40, driven by the |A|^H generalisation problem.

Aggregate 0.68. Direction **mixed**: supports the remedy path for MECH-135, weakens INV-088's boundedness proposition, and the record's `confidence_rationale` states the split explicitly so the index does not silently read it as uniform support.
