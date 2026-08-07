# Henderson et al. (2018) — a between-seed outcome split can be pure noise; the confound Q-089 must beat

**Claim tested:** Q-089 — does epistemic-deficit-driven information-seeking explain the cold-start competence split, as opposed to environmental difficulty, initialisation, premature death, or curriculum timing?

**Direction:** weakens · **Confidence:** 0.55

## What the paper did

"Deep Reinforcement Learning that Matters" is a reproducibility study of policy-gradient / actor-critic methods on continuous-control benchmarks. Its thesis, from the abstract, is that "non-determinism in standard benchmark environments, combined with variance intrinsic to the methods, can make reported results tough to interpret." The paper documents that deep-RL performance is strongly sensitive to random seeds, network initialisation, hyperparameters, and implementation details. Its most-cited demonstration takes a single algorithm and one set of random seeds, splits those seeds into two groups, and shows the two groups produce statistically significantly different learning curves — i.e. an *apparent* difference that reflects nothing but which seeds landed in which bucket. [arXiv:1709.06560](https://arxiv.org/abs/1709.06560) · [DOI](https://doi.org/10.1609/aaai.v32i1.11694)

## Why it weakens Q-089

Q-089's confirming signature is that *successful and unsuccessful seeds differ measurably in information-seeking trajectories, and that difference predicts the split*. Henderson et al. name the null this must be tested against: a between-seed competence split can arise from random seed and initialisation variance *alone*, with no systematic strategy difference of any kind. If the same algorithm with the same seeds, merely regrouped, can look statistically different, then observing that "some REE seeds acquire competence and some do not" carries, by itself, no mechanistic content. It is exactly Q-089's "initialisation" (and stochasticity) disconfirmer stated in its most general and most authoritative form. The practical bite: any Q-089 analysis that reads a competence split off a modest number of seeds risks labelling as "epistemic deficit" what is simply unremoved sampling variance — and the fix (many seeds, proper variance accounting, a control that predicts the split from seed/init alone) is a real design cost the confirming experiment has to pay.

## The mapping caveat

This weakens the *necessity* of Q-089's mechanism, not its *possibility*. Henderson et al. show seed/initialisation variance *can* be large and *can* be mistaken for real effects; they do not prove that any particular split — REE's included — is only noise. Their benchmarks are continuous-control MuJoCo, not REE's discrete substrate, so the magnitude does not transfer directly. So the correct reading is evidential-bar-raising: before an epistemic-deficit mechanism can be credited, the split must be shown to exceed, and not be accounted for by, seed/initialisation noise. One honesty note: the "split-the-seeds-into-two-groups" result is the paper's widely-known headline finding, taken here from the abstract and the established record rather than a fresh full-text extraction (the PDF did not render to text on fetch); the general sensitivity claims are from the abstract directly.

## Confidence reasoning

Source quality high (0.8 — one of the most-cited deep-RL reproducibility papers, AAAI 2018). Mapping fidelity moderate (0.6): it establishes the confound in general but measures a different substrate, not REE's. Transfer risk low-moderate (0.4): deep RL, though continuous-control rather than REE's discrete cold-start. Net 0.55 as a disconfirming caution — it makes the initialisation/stochasticity alternative concrete and formidable, which is what Q-089's confirming test must overcome, without asserting that REE's split is in fact noise.
