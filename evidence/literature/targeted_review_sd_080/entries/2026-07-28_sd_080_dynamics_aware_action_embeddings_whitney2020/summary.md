# Dynamics-aware Embeddings (Whitney, Agarwal, Cho & Gupta, ICLR 2020)

## What the paper did

Whitney and colleagues train state embeddings and action-sequence embeddings *jointly*, under a single forward-prediction objective: given an embedded state and an embedded action sequence, predict the resulting state. The point of the joint objective is that neither embedding is trained to be a good compression in isolation -- they are trained to be a good compression *of the dynamics*. Two action sequences land near each other when they take the world to the same place. They then evaluate the two halves separately, which is the part that matters here: an ablation on low-dimensional-state control isolating the action embedding, and a combined result on goal-conditioned control from pixels reaching high-quality policies in 1-2M environment steps.

## Findings relevant to SD-080

The isolating ablation is the finding I care about. Action embeddings *alone* -- with the state representation left as-is -- improve both sample efficiency and peak performance of model-free RL on control from low-dimensional states. That is a clean statement that the action side of the representation carries independent value, not merely value contingent on also fixing the state side.

This matters for SD-080 because the 2026-07-22 spike established, unusually carefully, that REE's defect is action-side-*only*. The control in that spike was not an afterthought: z_world genuinely varies across the 120 sampled world states (total variance 0.0031, mean per-dimension std 0.0096, mean norm 0.42), and the trained sibling `world_forward` moves from `r2_explained_by_action_alone` of 0.791 untrained to 0.558 after warmup -- it *acquires* state-dependence over training, which is what a dynamics-aware representation is supposed to do. The same z_world variation that moves `world_forward` leaves `action_object_head` at a between-state variance of about 6e-05. So REE is sitting in precisely the configuration Whitney et al.'s ablation isolates: state representation working, action representation not dynamics-aware. Their result says that configuration leaves performance on the table.

## How this translates to REE

The translation is close, and the closeness is the point. SD-004 specifies `o_t = f(z_world_t, a_t)` -- a state-conditioned map to world-effects. Whitney et al.'s action embedding is state-conditioned in exactly this way because the forward objective cannot be satisfied otherwise: to predict the next state you need the embedding to know what this action does *from here*. REE's head takes `z_world` as input and, frozen, throws it away. The architecture is compatible with SD-004; the parameters are not, and never became so.

## Limitations and caveats

I want to be careful about three gaps, because each of them could make the transfer weaker than it looks.

First, these are embeddings of action *sequences*, and that choice is deliberate -- the authors go to sequences because that is where the informative dynamics structure lives. REE's action objects are single-step. If the useful consequence structure is genuinely multi-step, then repairing SD-080 as currently framed (train the single-step head) might be necessary without being sufficient, and REE would find a smaller effect than this paper reports for reasons that have nothing to do with the training path.

Second, continuous control is the friendly case. A continuous action space has metric structure sitting there waiting to be recovered; five discrete grid actions have very little. It is entirely possible that in REE's environment there is almost nothing for a learned action-object head to *find*, and the frozen projection is close to as good as any learned one. That would not rescue SD-004 as written -- the specification would still be unmet -- but it would change what governance should do about it.

Third, the consumer differs. Model-free RL is helped here; REE runs a CEM planner that refits a sampling distribution inside O. My intuition is that CEM should be *more* sensitive to a geometrically uninformative space, since it has no gradient and depends entirely on whether nearby samples mean nearby outcomes. But that is a conjecture and I would rather it live in an experiment design than in a confidence number.

## Confidence reasoning

0.74, a little below the Chandak entry. The ablation structure is what earns it -- it is the single closest match in the literature to REE's actual configuration, state-side healthy and action-side frozen. What holds it down is that transfer risk here is the highest of the three SD-080 entries: continuous control with sequence-level embeddings is close to the best case for the mechanism, and REE's five-action single-step discrete setting is close to the worst. So this entry supports the direction of SD-080 firmly and the magnitude not at all.
