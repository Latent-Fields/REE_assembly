# Cost-outcome sharpening in caudate during untutored sequence learning (Desrochers, Amemori & Graybiel 2015)

**Claim tested:** MECH-323 (policy_composition_chunk_accumulator)
**Direction:** supports · **Confidence:** 0.75

## What the paper does

Most of what we know about the signals driving behavioural learning comes from trained subjects on instructed tasks, which leaves an awkward gap: what drives learning in a *naive* subject, before there is a task to be trained on? Desrochers and colleagues exploited a sequential saccade task on which macaques spontaneously acquire repetitive scanning sequences without ever being instructed to.

Two findings. First, caudate spike activity after each trial corresponded to an **integrated cost-benefit signal**, and that signal was highly correlated with how much untutored learning each animal showed. Second, across learning, neurons encoding both cost and outcome acquired **increasingly sharp phasic trial-end responses**, and the sharpening paralleled the emergence of the habit-like repetitive sequences.

## Why this matters for MECH-323

This entry does more work than most because it lands on three of MECH-323's registered commitments independently.

**The R1 formation trigger.** MECH-323 says formation is driven by repetition *plus outcome consistency*, with an evaluative gate upstream, rather than by repetition alone. Because the macaques' learning was uninstructed, there is no experimenter-imposed reinforcement schedule confounding what drove crystallisation — and what tracked it was an integrated cost-benefit quantity. That is about as direct as biological support for an evaluative-gate trigger gets. It also refines the commitment in a way worth carrying into the substrate: the signal integrates *cost*, not only outcome. An accumulator gated purely on outcome consistency would form chunks the biology would not, and would be blind to a reliably-rewarded but too-expensive sequence.

**The R4 options structure.** MECH-323 inherits from Sutton 1999 the requirement that a chunked primitive carries an initiation set and a **termination condition**. The phasic response here is at trial-*end*, and it sharpens as the chunk crystallises. A boundary marker that becomes progressively more precise as the sequence consolidates is close to a neural picture of a termination condition being written onto the chunk and then refined. I would not push this further than an analogy — nobody in this paper is claiming to have found a termination field — but among the ARC-071 lit set this is the closest thing to it, and the parent set (Sakai 2003, Yin & Knowlton 2006, Smith & Graybiel 2013) does not have it.

**The R5 hysteresis framing.** The crystallisation is *gradual*. Neurons acquire increasingly sharp responses; they do not switch. That supports MECH-323's graded formation picture over a threshold-crossing event, and it carries a design consequence: implementing formation as a single F_low crossing produces a step-like commitment with no biological counterpart, and throws away the graded window in which a partly-formed chunk is still cheap to abandon. Whether that window matters is an empirical question for the substrate, but it exists in the biology and would not exist in the naive implementation.

## An implication for the write path

One thing here sits slightly awkwardly with MECH-323 as registered. The sequences emerged from *self-generated repetition*, not from deliberate planning — nothing proposed those scanning sequences as a unit. MECH-323's default write path is MECH-094-strict: real executions with `hypothesis_tag=False` are trusted, and the `replay_origin` flag distinguishes sleep-replay-derived chunks that need waking corroboration. But this paper shows that "real execution" is not itself a guarantee of deliberateness. A chunk can crystallise out of repetitive behaviour the planner never endorsed, and `replay_origin` does not separate that case from a genuinely planned trajectory. Whether that is a bug or a feature depends on what one thinks habits are for; it is at least a distinction the current two-valued flag cannot represent.

## Where the mapping breaks

The evidence is **correlational**. The sharpening parallels learning; there is no lesion or perturbation showing the caudate signal is required for chunk formation. So the trigger mapping is a correspondence, not a demonstrated causal role, and MECH-323 should not be read as having a validated mechanism on the strength of it.

The grain gap is the other real limit. A "sequence" here is a handful of saccades in a tightly constrained oculomotor task; "cost" is saccadic effort and "outcome" is juice. REE's chunked primitives sit at policy grain and would integrate considerably richer evaluative quantities. This is the standard ARC-071 transfer risk — motor-sequence chunking may simply not generalise to abstract policy chunks — and it is the reason mapping fidelity is capped at 0.72 despite the strength of the three correspondences.

Finally, note what this paper does *not* touch: the chunk-size budget of 2–5 elements per level, and the dissolution threshold F_high. Neither has literature grounding from this entry or from the Dezfouli & Balleine companion. Both remain design choices, and they should be labelled as such rather than inheriting borrowed confidence from the trigger evidence.

## Confidence reasoning

0.75. Source quality is high at 0.88 — *Neuron*, primate single-unit recording, and an unusually clean design in that untutored learning removes instruction as a confound on what drives crystallisation. Mapping fidelity 0.72, capped by the grain mismatch. Transfer risk 0.35. I have weighted source quality more heavily here than in the Dezfouli & Balleine entry, because MECH-323's R1 and R4 verdicts are empirical commitments about what the trigger *is*, and for empirical commitments the quality of the measurement is what should carry the weight.
