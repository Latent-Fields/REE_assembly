# Overoptimising a scalar proxy has a measurable shape (Gao, Schulman & Hilton, ICML 2023) — EXT-003

**Source:** Gao L, Schulman J, Hilton J. *Scaling Laws for Reward Model Overoptimization*. Proceedings of the 40th International Conference on Machine Learning, PMLR 202:10835–10866, 2023. arXiv:2210.10760.

## What the paper does

RLHF optimises a language model against a reward model trained to predict human preferences. Everyone in the field knows that pushing this too far degrades what you actually wanted — Goodhart's law, observed repeatedly and measured almost never, because measuring it properly means collecting human preference data at every point along an optimisation curve, which is prohibitively expensive.

The authors' move is to sidestep the cost with a synthetic setup: a fixed "gold-standard" reward model plays the role of humans and supplies the labels used to train a *proxy* reward model. They then optimise policies against the proxy — via reinforcement learning or via best-of-n sampling — and watch the gold score. This buys them dense measurement, and what they recover are clean empirical laws. Writing `d := sqrt(D_KL(π ‖ π_init))`, they find

- best-of-n: `R_bon(d) = d(α_bon − β_bon·d)`
- RL: `R_RL(d) = d(α_RL − β_RL·log d)`

Both curves are non-monotone. Gold reward rises, peaks, and then falls as optimisation pressure increases. The coefficients scale smoothly with reward-model parameter count.

## The finding that matters for EXT-003

This is the only entry in the pull that operates in the domain EXT-003's `subject` field actually names — `llm.reward_hacking` — and it is the only one that attaches numbers to the failure rather than demonstrating or proving it. The region past the peak is EXT-003's sentence made observable: the policy is still improving on the signal it was given, and is getting worse at what was wanted.

The part with genuine architectural import for REE, though, is what *does not* fix it. Scaling the reward model shifts the peak and leaves the shape intact. The KL penalty trades optimisation pressure against divergence without closing the gap. Both are attempts to make the single scalar channel *better*, and neither removes the effect. That is the negative result ARC-021's three-loop separation is the positive proposal against. REE's answer is not a more accurate scalar; it is three learning channels that are never summed, so that no policy improvement measured on one is ever expressible as a licence to regress on another.

## The caveat, which is the most important thing in this entry

I want to state this sharply rather than let the entry read stronger than it is. **Both the proxy and the gold reward in this study are scalars.** What the paper isolates is an *approximation* failure — we cannot learn the true scalar exactly, and optimising the learned stand-in past a point diverges from it. That is entirely compatible with the position EXT-003 denies: that a correct scalar objective exists and the only trouble is estimating it well.

Read on its own terms, this paper points toward better reward modelling. That is the opposite of ARC-021's conclusion. So the entry evidences EXT-003's *consequence*, in the right domain, with the best measurement available — while being structurally silent on EXT-003's *premise*, and mildly in tension with it. A governance reader should not take the strength of the measurement as strength of support for incommensurability, because it is not that.

A second, smaller caveat: the gold reward model is itself a model, not human judgement. The authors adopt this deliberately and are explicit about why, but it means the study measures divergence between two learned scalars rather than divergence from what people want. The recovered coefficients are properties of the setup, not of human preference.

## Confidence

0.68 — the lowest of the four supporting entries, and the ranking is deliberate. Source quality is high (0.88): ICML 2023, careful sweeps over reward-model dataset size, reward-model and policy parameter counts and the KL coefficient, and functional forms that have held up as a reference point in subsequent overoptimization work. Transfer risk is low (0.32) because the domain is already the right one; the residual is the synthetic gold model. Mapping fidelity is 0.55, the lowest in the pull, and it is what holds the aggregate down: a scalar-approximates-scalar study cannot evidence incommensurability no matter how well it is executed. The strong source quality and the on-target domain are exactly why it is worth being explicit that they do not compensate for the mapping gap.
