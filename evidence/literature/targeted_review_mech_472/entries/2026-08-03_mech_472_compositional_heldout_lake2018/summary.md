# Generalization without Systematicity (Lake & Baroni, ICML 2018)

**Claim under test:** MECH-472 -- held-out context distinguishes skill acquisition from task memorisation; promote to durable only on evidence from contexts that did not generate the competence. Of particular interest here is MECH-472's non-degeneracy guard: the held-out contexts must be genuinely reachable, or the gap is a floor artefact rather than evidence of memorisation.

## What the paper did

Lake and Baroni introduced SCAN, a synthetic dataset pairing compositional navigation commands ("jump twice", "run and jump") with action sequences. They trained sequence-to-sequence recurrent networks and evaluated them on three different train/test splits: a random split, a split requiring longer output sequences than seen in training, and a split requiring a primitive ("jump") learned in isolation to be recombined into novel commands (the "add jump" split).

## Key findings relevant to the claim

The models scored near-perfect on the random split and failed badly on the compositional and length splits -- below roughly 40% on add-jump even after being shown the jump primitive. The critical point for MECH-472 is not "networks can't do compositionality"; it is that **the same trained system looks fully competent under one held-out split and near-incompetent under another.** Whether the held-out set detects memorisation depends entirely on how it is constructed. A random hold-out -- the naive default -- gives a small gap and a false certificate of acquisition, because the held-out items are near-duplicates of training structure. A hold-out that demands recombination in a context the training data never generated exposes the memorisation.

## How this translates to REE

This is the paper that speaks most directly to MECH-472's *design*, not just its premise. MECH-472 proposes to threshold an in-context-vs-held-out gap; Lake & Baroni show that the threshold is meaningless until the held-out context is chosen to actually lie outside the generating distribution. For REE this is a concrete warning: if the "contexts that did not generate the competence" are only superficially different, the falsifier will pass a memorising agent. The held-out set has to be constructed to require the competence to be *re-applied*, not *re-encountered*.

It is a genuinely double-edged example, and I have kept confidence at 0.74 for that reason. The add-jump split sits at near-zero baseline for its held-out combinations -- which is precisely the floor-artefact regime MECH-472's non-degeneracy guard flags as the most likely source of a false positive. So SCAN illustrates *both* things at once: that a well-chosen hold-out reveals memorisation, and that an unreachable hold-out produces a large gap for reasons unrelated to memorisation. It should be read as evidence about how to construct the split, not as a template to copy wholesale. The domain gap is also real: this is supervised seq2seq language on a synthetic grammar, not an RL agent promoting a behavioural competence to durable storage.

## Confidence reasoning

Source quality is high (an influential ICML paper that spawned a whole compositional-generalization literature). Mapping fidelity is moderate: the methodological lesson about split construction transfers cleanly to MECH-472's falsifier design, but the task domain does not match REE's substrate closely. Transfer risk is moderate for the same reason. The entry earns its place less for the headline result than for sharpening exactly the guard MECH-472 says is most likely to be skipped.
