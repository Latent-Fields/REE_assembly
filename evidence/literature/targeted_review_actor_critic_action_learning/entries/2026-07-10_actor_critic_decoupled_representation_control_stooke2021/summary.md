# Stooke, Lee, Abbeel & Laskin (2021) — Decoupling representation learning from reinforcement learning

*ICML 2021, PMLR 139:9870-9879. [arXiv:2009.08319](https://arxiv.org/abs/2009.08319).*

## What the paper did

This is the ML paper that speaks most directly to the *shape* of REE's proposed fix, so it is worth being precise about what it does and does not show. Stooke et al. ask whether the encoder that turns pixels into features has to be trained by the RL reward signal, or whether it can be learned separately. Their unsupervised objective, **Augmented Temporal Contrast (ATC)**, trains a convolutional encoder to associate pairs of observations a short time apart, under augmentation, with a contrastive loss. Two results matter here. First, training the encoder with ATC *alone* matches or beats end-to-end RL in most of their environments. Second, when they pre-train encoders and **freeze** them inside RL agents, ATC-frozen encoders outperform other unsupervised objectives. But in every configuration, the **policy is still trained by RL on reward** on top of the (possibly frozen) encoder. The decoupling is of *representation* from *policy* — not the removal of policy learning.

## Why it matters — and why it cuts both ways

This is the closest published precedent for REE's actual `f_dominance_conversion_ceiling` proposal: keep the perceptual/prediction encoder (e2 world-forward contrastive) and add a separately-trained policy over it — which is exactly V3-EXQ-737, a PPO policy head on a frozen `z_world`. I logged it as **mixed** on purpose, because an honest reading points in two directions at once.

**It supports the H1 build design.** Stooke et al. are an existence proof that a decoupled shape — self-supervised (even temporally-contrastive) encoder, plus an RL-trained policy — *can* produce competent control, and that a frozen encoder can even be sufficient. REE's contemplated architecture is not exotic; it is a known-good pattern.

**And it is evidence that REE's status quo is broken for a reason the other papers don't state as sharply.** In ATC, the policy is *always* trained by RL on reward. A decoupled encoder never substitutes for the actor. REE's `bias_head` is not the ATC agent's RL-trained policy — it is the piece REE is missing. So the same paper that validates the design also indicts the current implementation: having a good (prediction-trained) encoder does not buy you control; you still have to train an actor on reward, and REE doesn't.

## The caveat that keeps H2 alive

ATC's frozen-encoder success was **conditional**. It depended on a temporal-contrastive objective over control-relevant pixel streams, with reward dense enough for the downstream policy to learn. REE's e2 is temporally-contrastive in spirit, but its features were shaped to predict sensory transitions, and it is far from guaranteed they expose resource-vs-hazard structure under a 5x5 partial view with implicit reward. So this paper supports the *design* (decoupled encoder + RL policy) more strongly than it supports the *prediction* that REE's specific frozen e2 will suffice. That gap is the residual H2 — feature adequacy — which 738 began to bound (the floor is reachable from the local view) and which 737 will pressure directly by asking whether a real policy over `z_world` recovers competence. If 737 stalls, this paper tells us where to look next: unfreeze or replace the encoder, not just enlarge the policy.

## Confidence

**0.71, mixed.** High source quality (ICML spotlight, directly on the decoupled-representation question) and high relevance — it is the nearest precedent for REE's exact frozen-encoder-plus-trainable-policy design. I hold it at 0.71 rather than higher because the verdict is genuinely two-edged: it strongly supports building the actor while explicitly flagging that a frozen prediction encoder only works if its features are control-relevant. Transfer risk is the highest in this dossier (0.42) — pixel DMControl/Atari with denser reward is an easier regime than REE's forager, and "frozen encoder suffices" is precisely the claim most at risk in that transfer. Which is the right note to end the dossier on: the biology and the theory say *build the actor*; this paper says *build it, and be ready for the encoder to be the next thing you have to fix.*
