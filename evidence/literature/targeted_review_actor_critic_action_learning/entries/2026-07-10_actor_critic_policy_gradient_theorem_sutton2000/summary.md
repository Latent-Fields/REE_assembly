# Sutton, McAllester, Singh & Mansour (2000) — Policy gradient methods for reinforcement learning with function approximation

*NeurIPS 12 (NIPS 1999 proceedings), pp. 1057-1063. [Proceedings link](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html).*

## What the paper did

This is the ML-side foundation of the whole pull. Sutton et al. prove the **policy-gradient theorem**: a policy can be represented by *its own* function approximator, independent of any value function, and improved by gradient ascent on expected return. They then show that a compatible *learned value function* can serve as a baseline that reduces the variance of the gradient estimate without biasing it — this is the **actor-critic** form. The framing that matters for REE is the motivation the authors give for going this route at all: the obvious alternative — approximate a value function and read the policy off it — "had so far proven theoretically intractable" under function approximation. Directly parameterizing and pushing the *policy* is what makes control learnable when you cannot tabulate states.

## Why it matters for the translation gap

The three neuro entries say the brain runs a dedicated actor. This paper says *why that is the right engineering, not just the right biology.* Competent control comes from directly optimizing a dedicated policy object on return, with a value baseline to make the gradient usable. That is precisely the object REE does not have. REE learns action through a thin `bias_head` REINFORCE over a **frozen, prediction-trained** encoder, with no separately-parameterized policy and no value-baseline critic. In ML vocabulary, the `f_dominance_conversion_ceiling` build is simply: *give REE a real actor (parameterized policy) and a critic (value baseline).* And it tells us why V3-EXQ-737 — PPO, a modern actor-critic/policy-gradient method, trained on REE's frozen `z_world` — is the correct minimal H1 test: it supplies exactly the missing object over exactly the representation in question.

## The caveat that keeps me honest

There is a subtlety I want on the record, because it is easy to overclaim. REE's bias-head **already is** a policy-gradient (REINFORCE) method. So the theorem does *not* say REE picked the wrong algorithm family. It says REE applied a good family to an **inadequate object**: a low-capacity bias head, with no critic baseline (hence high-variance updates), riding on features frozen for prediction rather than shaped for control. The fix the theorem points to is structural — a full trainable policy plus a value baseline — not a change of algorithm.

The second caveat is the one that keeps H2 alive. Policy gradient guarantees convergence only to a **local** optimum. If the frozen encoder's features do not expose the control-relevant structure of the task, a full policy head can still stall in a poor optimum. The theorem cannot rule that out — it is exactly the feature-adequacy question (H2) that the local-view-achievable anchor (V3-EXQ-738) began to address and that 737 will pressure directly by training the policy on `z_world`. This paper de-risks the *actor* half of the build; it is silent on whether REE's representation is a good enough critic-substrate to build the actor on.

## Confidence

**0.80, supports.** Source quality is very high — this is the theorem the entire modern actor-critic/PPO lineage rests on. Mapping fidelity is high (0.82): it names the exact formal reason a separately-trained policy with a value baseline learns control that a value/prediction model alone will not, which is REE's precise gap. I keep transfer risk low-moderate (0.28) only because a local-optimum guarantee about the learning object cannot, by itself, promise that REE's frozen features suffice — the honest boundary between the H1 fix this grounds and the H2 residual it does not.
