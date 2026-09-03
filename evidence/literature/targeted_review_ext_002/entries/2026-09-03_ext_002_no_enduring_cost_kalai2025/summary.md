# Why Language Models Hallucinate (Kalai, Nachum, Vempala & Zhang, 2025)

**Claim tested:** EXT-002 -- *Hallucination: no persistent error residue accumulates to shape future outputs.*
**Direction:** supports (of the "no enduring cost" half) | **Confidence:** 0.72

## What the paper does

This is an analytic paper, not an empirical one. It asks why hallucination survives scale, RLHF, and a decade of engineering attention, and answers in two parts. In pretraining, the model is doing density estimation over text; for facts that are arbitrary -- a birthday, a citation, a one-off number -- there is no signal in the corpus that separates the true completion from a plausible false one, so a non-zero error rate follows from statistical pressure alone, and reduces to the difficulty of a binary "is this statement valid" classification. In post-training, the survival of the behaviour is explained differently: the benchmarks that dominate leaderboards grade answers on a binary right/wrong basis, under which an abstention scores exactly what a wrong answer scores. A model optimised to be a good test-taker therefore learns to guess. The authors' proposed remedy is socio-technical -- rescore the existing dominant benchmarks so uncertainty is not penalised -- rather than architectural.

## What it says about EXT-002

EXT-002's notes assert two things: that transformers have no mechanism for prediction errors to leave a persistent trace penalising future outputs, and that "a false statement incurs no enduring cost." This paper is a direct, argued defence of the second. Its contribution is that the absence of cost is not an oversight but a consequence of the objective: nothing in the pipeline distinguishes *having been wrong* from *having declined to answer*, so there is no quantity for a persistent error record to be the record of. That is a stronger statement than the usual survey observation that LLMs lack a feedback loop, because it names the place where the missing term would have to live.

The REE contrast the claim draws is that E1 prediction errors accumulate into phi(z) and modulate trajectory selection on subsequent steps (ARC-005, INV-006, INV-008). Read against Kalai et al., the REE mechanism is doing two separable jobs: it attaches a cost to error at all, and it makes that cost *persistent and state-borne*. This paper speaks decisively to the first and only by implication to the second.

## Limitations and the mapping caveat

The caveat matters and I do not want to paper over it. The paper's missing penalty is in the **objective**; EXT-002's residue is in the **runtime state**. Those are not the same absence. One could take the paper's own recommendation -- rescore the benchmarks so that confident falsehood is penalised relative to abstention -- and end up with a model that has an enduring cost for being wrong and still has no per-episode error trace shaping the next step. If that intervention substantially reduced hallucination, it would weaken the specifically *architectural* reading of EXT-002 while leaving the economic reading intact. So this entry should not be counted as evidence that a persistent residue is *necessary*, only that the cost EXT-002 says is absent is genuinely absent and absent for a nameable reason.

Second caveat: it was an arXiv preprint at pull time. I checked arXiv, OpenAlex, Crossref and DBLP on 2026-09-03 and found no refereed venue. The authorship is strong and the related, peer-reviewed *Calibrated Language Models Must Hallucinate* (Kalai & Vempala, STOC 2024, doi:10.1145/3618260.3649777) covers the pretraining half of the argument under review, but the post-training grading argument -- the part that bears most directly on EXT-002 -- is the preprint's own. I have discounted `source_quality` to 0.70 for that.

## Confidence reasoning

`mapping_fidelity` is the field carrying most of the weight here (0.85): the paper's subject is literally the claim's subject, and its thesis restates the claim's second sentence. `transfer_risk` is low (0.25) because there is no cross-species or cross-task transfer to discount -- the objection is a level mismatch, already charged against fidelity, not a transfer. The aggregate sits at 0.72 rather than the component mean because the preprint discount and the objective-vs-runtime gap are the two things a governance reader should see, and I would rather the number under-claim than over-claim on an `external_failure_mode` claim whose whole function is to anchor a contrast with REE's own design.
