# Large Language Models Cannot Self-Correct Reasoning Yet (Huang et al., ICLR 2024)

**Claim tested:** EXT-002 -- *Hallucination: no persistent error residue accumulates to shape future outputs.*
**Direction:** supports | **Confidence:** 0.74

## What the paper does

The paper takes a live claim in the 2023 literature -- that LLMs can improve their own answers by reviewing and revising them -- and asks what the reported gains actually depend on. Its key move is to define *intrinsic* self-correction precisely: revision using only the model's own capabilities, with no external feedback, and crucially with no oracle label used to decide when to stop revising. Prior work, the authors show in their Table 1, does not meet that bar. RCI (Kim et al. 2023) and Reflexion (Shinn et al. 2023) use oracle labels; multi-agent debate is compared against an unfair baseline rather than self-consistency; Self-Refine's gains partly reflect a weak initial prompt.

Stripped of the oracle, the result reverses. Across GSM8K, CommonSenseQA and HotpotQA, and across GPT-3.5, GPT-4, GPT-4-Turbo and Llama-2, accuracy after self-correction *falls*. GPT-4-Turbo on GSM8K goes 91.5 -> 88.0 after one round and 90.0 after two -- still below where it started. Llama-2 collapses: 62.0 -> 43.5 -> 36.5. The authors also vary the feedback prompt and find the decrease is consistent rather than an artefact of one wording.

The diagnostic analysis is the part I find most useful for EXT-002. On GSM8K, GPT-3.5 keeps its original answer 74.7% of the time; among the cases where it does change, it is more likely to turn a correct answer into an incorrect one than to fix a wrong one. Revision is not selective toward error. The authors' own summary is that the model "cannot properly judge the correctness of its reasoning."

## What it says about EXT-002

EXT-002's most direct behavioural prediction is that a second attempt should not be systematically better than a first, because nothing carried forward marks which parts of the first were wrong. That is what this paper measures. Where REE would deposit the E1 prediction error of attempt one into phi(z) and let it bias E3 selection on attempt two (ARC-005, INV-006, INV-008), a transformer's second pass is conditioned on the first pass's *text* with no annotation of which spans cost anything. The revision is therefore unguided, and an unguided edit on a mostly-correct answer is expected to be net harmful -- which is exactly the observed asymmetry.

The oracle finding is the same point in a cleaner form. When the gains are present, the signal deciding *when to stop* came from outside the model. Remove it and the gains go. The correcting signal was never endogenous. This is worth carrying forward because it constrains how the Reflexion entry in this same pull can be read: Huang et al. classify Reflexion's improvements as oracle-dependent, which does not undercut Reflexion's usefulness as evidence that an *exogenously supplied* error record helps -- if anything it sharpens it.

## Limitations

This is a null-to-negative result, and null results are weaker evidence for a mechanistic absence than a positive dissociation. A defender could argue that the prompting protocol failed, not the architecture; the authors' own title says "Yet", which signals they take the limitation to be contingent on current training rather than architectural. EXT-002 takes the stronger, architectural position, and this paper does not settle that.

The transfer is also not free. These are checkable-answer reasoning benchmarks, not open-ended factual generation, and EXT-002's subject is `llm.hallucination`. The extension is by argument -- both are cases where a produced error should acquire a cost and does not -- rather than by measurement. I have charged that against both `mapping_fidelity` (0.68) and `transfer_risk` (0.30) rather than hiding it in the aggregate.

## Confidence reasoning

`source_quality` is high at 0.85: a peer-reviewed ICLR paper whose main contribution is a control other people had omitted, with the numbers to back it. `mapping_fidelity` is the limiting term at 0.68, for the reasoning-benchmark-to-hallucination gap and the underdetermination inherent in a negative result. The 0.74 aggregate sits above the component mean because the oracle dissociation is a genuinely mechanistic finding, not merely a failure to replicate -- it locates *where* the correcting signal was coming from, which is the kind of evidence EXT-002 needs.
