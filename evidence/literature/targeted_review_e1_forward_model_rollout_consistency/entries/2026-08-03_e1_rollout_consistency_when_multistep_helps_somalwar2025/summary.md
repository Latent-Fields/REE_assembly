# Somalwar, Lee, Pappas & Matni 2025 -- When multi-step prediction actually helps

**Claim(s):** MECH-135, INV-088 | **Direction:** mixed | **Confidence:** 0.58

## What the paper did

Every other paper in this review answers "how should we train multi-step?". This one asks a question I think is more useful to us right now: *when is multi-step training worth it, and when is it just a more expensive way to learn a worse model?*

The authors observe that training multi-step predictors directly is a common mitigation for compounding error, but "it is not well understood when the benefits of multi-step prediction outweigh the added complexity of learning a more complicated model." For linear dynamical systems they give a rigorous answer, and it is a genuine two-sided result:

- When the model class is **well-specified** -- it accurately captures the true system dynamics -- **single-step** models achieve *lower* asymptotic prediction error. The multi-step predictor is harder to learn and there is no compensating bias to remove.
- When the model class is **misspecified due to partial observability**, direct multi-step predictors significantly reduce bias and outperform single-step approaches.

They also empirically evaluate an intermediate strategy: training a single-step model using a multi-step loss.

## Why I went looking for something like this

The `substrate_queue.json` entry for SD-e1-rollout-consistency-training carries `node_class: "complex (probe-gated)"`, and its `implementation_hint` says the choice among candidates "is a reducible unknown owed a lit-pull first, not yet a build decision." That is the right classification, but it is a procedural label until something tells you *what to probe*. This paper supplies the discriminating variable: **is E1's model class misspecified relative to the true dynamics?**

On the evidence available the answer looks like yes. E1 predicts a learned latent from partial CausalGridWorldV2 observation, through a `world_dim=32` encoder bottleneck, and the agent never observes full environment state. That is squarely the partial-observability-induced misspecification the theorem names as the regime where multi-step training pays. So the criterion, applied to REE, points the favourable way.

The third contribution is directly useful too. The intermediate strategy they evaluate -- a *single-step* model trained with a *multi-step* loss -- is precisely the cheap middle option between leaving E1 alone and rebuilding it as a sequence-conditioned model, and it is the option closest to what `substrate_queue.json` currently describes.

## Limitations, and why the direction is mixed

The rigorous analysis is for **linear** dynamical systems. E1 is a nonlinear LSTM over a learned latent. The numerical experiments go beyond the linear theory but the guarantees do not, so the misspecification criterion is a well-motivated heuristic for REE and not an applicable theorem. I would not want it cited as though it were the latter.

There is a subtler problem with the criterion itself. "Misspecified due to partial observability" is a precise condition in a linear-systems setting: the true system has hidden state that the model class cannot represent. REE's situation is arguably different in kind, because E1's latent is *learned* -- the model class is flexible in a way the paper's fixed classes are not. Whether the criterion carries over cleanly is not obvious to me, and I have not seen it addressed.

And the reason this is **mixed** rather than **supports**, which I want on the record explicitly: the same theorem that gives REE a favourable reading also says that *if E1's real problem is not misspecification, multi-step training buys nothing and costs learning complexity*. Combined with what the other entries in this review surface -- particularly that E1's transition takes no action argument at all, which is a different defect that no amount of multi-step training addresses -- this is an argument for probing before building. That is the honest use of this paper: it does not tell us multi-step training will work. It tells us the question has a determinate answer, that the answer turns on a substrate property nobody has measured, and that measuring it is cheap relative to the build.

## Confidence reasoning

Source quality 0.62: a 2025 arXiv preprint, not yet peer-reviewed, from a credible control-theory group (Matni and Pappas at Penn), rigorous within a narrow stated scope. Mapping fidelity 0.60 -- the *question* it answers is exactly REE's question, while the *setting* (linear, fixed model class) is far from E1's. Transfer risk 0.55, the highest in this review and deliberately so; a linear-systems asymptotic result should not bear much weight for a nonlinear recurrent model.

Aggregate 0.58. This entry earns its place by framing the decision, not by settling it -- which is the appropriate contribution to a node classified `complex (probe-gated)`.
