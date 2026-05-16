# Summary: Large-Scale Study of Curiosity-Driven Learning (Burda et al., ICLR 2019)

**Entry:** 2026-05-16_mech314c_large_scale_curiosity_noisy_tv_burda2018
**Claims:** MECH-314, MECH-314c, MECH-314b, ARC-065
**Direction:** mixed | **Confidence:** 0.78

---

## What the paper did

Burda and colleagues conducted the first systematic large-scale evaluation of purely intrinsic-curiosity-driven learning (no extrinsic task reward) across 54 benchmark environments including the full Atari game suite. They tested multiple feature space choices (random features, variational autoencoders, inverse dynamics features, raw pixels) and evaluated performance both in terms of game score obtained under curiosity-only training and the degree to which the intrinsic objective aligned with the extrinsic hand-designed reward. The study was designed to characterize when curiosity works, when it fails, and whether the type of feature space matters.

## Key findings relevant to the claim

The headline positive finding is that curiosity-driven learning achieves "surprisingly good" performance on many Atari games and procedurally generated environments without any task reward. This is strong evidence that prediction-error-based curiosity bonuses have genuine functional value as exploration drivers -- they are not just a theoretical exercise. For REE, this supports MECH-314c (and MECH-314b via the uncertainty/variance overlap) as meaningful contributors to the ARC-065 diversity pathway.

The headline negative finding -- the "noisy TV problem" -- is the most important for REE infant-stage design. When an agent can access an irreducibly random stimulus (a TV displaying random pixels), it fixates on the TV indefinitely. The curiosity signal from an unlearnable source stays perpetually high, and the agent stops exploring the rest of the environment. This is not a bug in the implementation; it is a fundamental property of any prediction-error-based curiosity measure: the agent is genuinely most curious about the thing it cannot predict, and irreducible randomness maximizes that. The practical consequence is that environments must not contain random attractor stimuli that the agent cannot learn to predict.

The feature space finding is also relevant: random features work well enough for static benchmarks but learned features generalize better to novel configurations (tested with Super Mario Bros at new levels). For REE, this suggests that the quality of z_world as a feature space affects how well MECH-314a-c will generalize to new environment configurations in later training stages.

## REE translation -- the central question

This paper provides the strongest direct answer to the user's question: "Is novelty_bonus_weight at maximum sufficient, or does the environment need richer structure?"

The answer from Burda 2018 is: novelty_bonus_weight at maximum is insufficient if the environment contains any accessible source of irreducible randomness. The curiosity signal will be captured by the random attractor. Richer, more structured environments (with learnable patterns at multiple levels of complexity) are necessary for curiosity bonuses to drive productive exploration rather than random-noise fixation.

The second finding is that curiosity aligns well with task reward in environments where task structure happens to correspond to what the prediction model finds challenging -- this alignment is not engineered, it is a coincidence that holds in many game environments. In REE's infant stage, there is no guarantee of this alignment, and the design should not assume it.

## Limitations and caveats

REE's CausalGridWorld is a discrete, structured gridworld with deterministic transitions; the noisy TV failure requires an accessible random stimulus that the agent can continuously encounter. A flat deterministic gridworld is much less susceptible to this failure than a 3D physics environment with freely accessible random objects. However, if the REE infant-stage design adds any stochastic elements (random reward delivery, random event generation), the failure mode becomes relevant. The most conservative implication is: ensure the environment has no accessible source of irreducible stochasticity before relying on prediction-error curiosity at high weight.

## Confidence reasoning

Source quality is high (ICLR 2019, large-scale empirical study). Mixed direction because the paper provides both strong support (curiosity works broadly) and strong caution (noisy TV failure mode). The mapping to REE is good for the design-principle findings and moderate for the specific failure-mode analysis.
