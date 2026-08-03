# Quantifying Generalization in Reinforcement Learning (Cobbe et al., ICML 2019)

**Claim under test:** MECH-472 -- held-out context distinguishes skill acquisition from task memorisation; a competence update should be promoted to durable only on evidence from contexts that did not generate it.

## What the paper did

Cobbe and colleagues built CoinRun, a procedurally generated platformer, specifically to break the near-universal RL practice of training and testing on the same environment. Because levels are generated from a seed, they can hold out an entire disjoint set of test levels and ask a sharp question the standard benchmarks cannot: how much of an agent's apparent competence is skill that transfers, and how much is memorisation of the particular levels it trained on? They trained PPO agents on training sets of increasing size and measured the gap between training-level reward and held-out-level reward.

## Key findings relevant to the claim

The headline result is that agents **overfit to surprisingly large training sets**. With a modest number of training levels an agent can reach near-ceiling reward on those levels while scoring far lower on held-out levels drawn from the identical generator -- the very definition of memorisation rather than acquisition. The gap only shrinks as the training set grows into the thousands of levels, and standard supervised-learning regularisers (L2, dropout, data augmentation, batch norm) plus deeper convolutional stacks help close it. The paper's methodological point is the one MECH-472 rests on: **same-context evaluation systematically overstates competence, and only a held-out context set reveals the true skill.**

## How this translates to REE

This is the closest published analogue to MECH-472's substrate. REE's agents are reward-driven and act across contexts; a "competence update" in REE is exactly the kind of thing that can look strong on the situations that produced it and collapse elsewhere. Cobbe et al. give the empirical warrant for the falsifier MECH-472 specifies -- pair in-context and held-out-context evaluation of the *same* learned competence, and treat a gap beyond threshold as memorisation. The held-out level set is precisely the "context that did not generate the competence."

There is a genuine caveat in the mapping, and it is the reason confidence is 0.82 rather than higher. CoinRun uses the held-out gap as a *reporting metric at the end of training*. MECH-472 goes one step further: it proposes to *gate a promotion-to-durable decision* on held-out evidence. "Held-out evaluation reveals memorisation" is strongly supported here; "therefore gate promotion on it" is a design inference REE must still earn on its own substrate. The paper licenses the diagnostic, not the specific control action. It is also worth flagging against MECH-472's non-degeneracy guard: because the gap only closes with very large context diversity, a naive held-out test with too few or too-hard held-out contexts will show a gap for reasons that have nothing to do with memorisation -- which is exactly the floor-artefact failure MECH-472 warns is the most likely false positive.

## Confidence reasoning

Source quality is high (a canonical, heavily replicated benchmark). Mapping fidelity is high because the substrate matches -- RL agent, held-out *context* rather than merely held-out samples. Transfer risk is low: unlike a rodent-electrophysiology pull, there is no species or modality jump. The confidence is held just below the top band because the paper supports the measurement principle cleanly but not the promotion-gating action that is MECH-472's actual novelty.
