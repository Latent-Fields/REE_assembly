# Le Lan et al. 2022 (AISTATS) — value-function quality is provably bounded by the state representation

**Claim tested:** INV-088 — *E3's z_world-reading evaluators are strictly bounded by E1's z_world representational differentiation.*
**Direction:** supports · **Confidence:** 0.72

## Why I reached for the ML literature at all

The three developmental-neuroscience entries give me the biological ordering and its mechanism, but they all share the same limitation: none of them actually measures an evaluator degrading as a function of representation quality. That is a *computational* question, and INV-088 is, underneath the developmental framing, a computational claim about a learned substrate. So the honest move is to bring in the machine-learning result that states the same dependency in a form where it can be proven and measured. Le Lan, Tu, Oberman, Agarwal, and Bellemare do exactly that.

## What the paper proves

They derive an informative bound on the *generalization error* of a value function in terms of the state representation, formalized through a quantity they call the **effective dimension** — a measure of how much knowing the value at one state tells you about the value at others. The bound applies to *any* state representation, and it exposes a fundamental tension: representations that generalize well and representations that approximate values accurately are pulling in different directions. They validate the framework empirically, showing that the generalization behavior of classic learned representations (and of deep RL agents on Atari) tracks their effective-dimension predictions.

## The mapping to INV-088

This is nearly a one-to-one translation. In REE, z_world *is* the learned state representation; harm_eval(z_world), benefit_eval, and the goal/trajectory scorers *are* value-function-like readouts sitting on top of it. INV-088 says the quality of those readouts is bounded by z_world's differentiation. Le Lan et al. say, in the general case, the quality of a value readout is bounded by the state representation it is built on. A poorly-differentiated z_world is, in their terms, a low-quality representation, and the theorem says the evaluator on top of it cannot do better than the representation permits. This is the cleanest support in the set for the *bound itself* — not the ordering, the bound — and it lives in the same domain family as the REE substrate, which is why I set transfer risk low (0.25) where the imaging entries sit at 0.35–0.40.

## Where I hold back, and a link to our own data

Two caveats keep this at 0.72 rather than higher. First, "effective dimension" is a *generalization* construct, whereas INV-088's differentiation proxy is task-relevant *decodability* (world_feat_decode_r2 — held-out ridge R² of z_world[t] → harm_obs[t+1]). These are cousins, not twins: both are notions of representation quality, but a bound stated in one need not transfer cleanly to a threshold measured in the other. Second, and more interestingly, the paper's central result is a *tradeoff*, not a monotone "more is better" — representations that generalize well can approximate poorly. That predicts the evaluator-quality-vs-differentiation relationship may not be a clean monotone curve, which is a striking echo of what V3-EXQ-744a actually found: a real-but-weak, high-variance coupling where two seeds coupled strongly and one was an outlier, failing the monotonicity gate (rho=0.69). The ML theory here is arguably *more* consistent with that messy, near-miss empirical picture than with a sharp threshold. Finally, the bound concerns generalization across states, not the training-time noise-fitting that INV-088's developmental framing emphasizes — so it certifies the dependency exists without certifying REE operates in the regime where it bites hardest.

## Confidence reasoning

Source quality 0.8 (AISTATS, rigorous theory plus Atari validation). Mapping fidelity 0.7 — near-direct, docked for the effective-dimension-vs-decodability gap and the tradeoff nuance. Transfer risk 0.25 — same domain. Net 0.72: the strongest support in the set for the bound as stated, and usefully, its tradeoff structure predicts the non-monotone, high-variance coupling our own 744a re-estimate keeps running into.

*Source: [arXiv:2203.00543](https://arxiv.org/abs/2203.00543), AISTATS 2022 ([DOI 10.48550/arXiv.2203.00543](https://doi.org/10.48550/arXiv.2203.00543)).*
