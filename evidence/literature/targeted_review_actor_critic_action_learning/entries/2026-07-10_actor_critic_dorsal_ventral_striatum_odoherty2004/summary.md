# O'Doherty, Dayan, Schultz, Deichmann, Friston & Dolan (2004) — Dissociable roles of ventral and dorsal striatum in instrumental conditioning

*According to PubMed. [DOI: 10.1126/science.1094285](https://doi.org/10.1126/science.1094285). Science 304(5669):452-4.*

## What the paper did

If Schultz 1997 gave us the teaching signal, this paper gives us the architecture. O'Doherty et al. scanned humans with fMRI under two conditions: a **Pavlovian** task where reward arrives regardless of action, and an **instrumental** task where the subject must choose an action to obtain reward. They fit temporal-difference reinforcement-learning models and asked *where* in the striatum the model's prediction-error regressor explained the BOLD signal. The answer was a clean dissociation. Ventral striatum carried the prediction-error signal in **both** conditions — it behaves like the RL **critic**, learning to predict future reward whether or not you act. Dorsal striatum carried it **only** in the instrumental condition — it behaves like the **actor**, engaged specifically when an action must be selected and credited.

## Why it matters for the translation gap

This is the single closest biological anchor to the reference the V3-EXQ-724 autopsy actually named: "dorsal-striatal RPE-driven action learning." The brain does not fold action learning into its value-prediction machinery — it runs an explicit **actor-critic split across distinct substrates**. A critic that learns to predict reward, and a *separate* actor that learns which actions to emit, each in its own striatal territory.

Held against REE, the diagnosis sharpens. REE has a prediction learner (e2 world-forward contrastive), but it is not even a reward-critic — it predicts sensory transitions, not future reward. And it has no actor at all: action is a bias-head riding on those prediction features. So O'Doherty grounds the missing actor *directly* and the missing reward-critic *by contrast*. The owed `f_dominance_conversion_ceiling` build is precisely the actor this paper localizes to dorsal striatum: a dedicated action-learning module, trained on reward-error, sitting **alongside** the perceptual/prediction stack rather than being a thin readout of it. V3-EXQ-737 — a PPO policy head trained on REE's frozen `z_world` latent — is the minimal "actor over frozen upstream features" instantiation of exactly this idea, which is why it is the load-bearing H1 test.

## Limitations and honest caveats

fMRI is coarse and correlational, and the actor/critic labels come from *where model regressors fit BOLD*, not from causal lesion or optogenetic dissociation. A determined skeptic could reframe the dorsal-striatal signal as action-contingent value rather than a genuinely separate actor learner. More importantly for governance: the dissociation shows action learning is *localized to a distinct substrate*, but it does **not** by itself prove that a prediction-only representation *cannot* support competent action. That negative is REE's H1 to demonstrate empirically — the fMRI motivates the architecture, it does not license skipping the 737 test. And the task is explicit-reward human instrumental conditioning; REE's forager has implicit resource reward under a 5x5 partial view, so the mapping is a formal import, not a measured equivalence.

## Confidence

**0.83, supports.** High source quality and unusually high mapping fidelity (0.80) — the actor/critic decomposition maps almost verbatim onto REE's missing-actor diagnosis, and "dorsal striatum = actor" is the exact reference the autopsy invoked. I hold it just under the neuro ceiling because the identity is regressor-inferred rather than causal, and because the paper grounds the *need for* an actor without settling whether REE's specific env is learnable by one — the residual that keeps H1 and H2 both live until the discriminator lands.
