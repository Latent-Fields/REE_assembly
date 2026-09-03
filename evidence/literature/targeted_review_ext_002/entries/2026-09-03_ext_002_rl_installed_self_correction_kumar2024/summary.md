# Training Language Models to Self-Correct via Reinforcement Learning (Kumar et al., 2024)

**Claim tested:** EXT-002 -- *Hallucination: no persistent error residue accumulates to shape future outputs.*
**Direction:** mixed | **Confidence:** 0.62

## Why this entry is here

Four of the five entries in this pull support EXT-002. This one is the counterweight, and it is included deliberately: an `external_failure_mode` claim whose whole function is to anchor a contrast with REE's own design is exactly the kind of claim that will drift into an article of faith if only confirming evidence is registered against it.

SCoRe is the strongest published answer to Huang et al.'s "not yet". The authors take the same starting point -- self-correction is largely ineffective in current LLMs -- and ask whether it can be *trained in* rather than prompted out. Their route is multi-turn online RL on the model's own correction traces, with no oracle labels, no teacher model, and no second critic. The negative results are as informative as the positive ones: supervised fine-tuning on offline correction traces does not work, failing either because the data-collection policy's mistakes do not match the model's own, or through behaviour collapse onto a single correction mode that does not generalise. SCoRe fixes this by training under the model's own distribution, with a regularised initialisation phase and a reward bonus that specifically amplifies correction. Gemini 1.0 Pro gains 15.6% self-correction performance on MATH; Gemini 1.5 Flash gains 9.1% on HumanEval.

## What it does and does not do to EXT-002

EXT-002 can be read two ways, and this paper separates them cleanly.

The **strong architectural reading** -- that there is no mechanism at all by which a transformer's prediction errors can come to penalise its future outputs -- is weakened. SCoRe is such a mechanism. Errors made during training are converted, through the RL objective, into a standing change in the model's behaviour on subsequent attempts. If EXT-002 is read as "impossible in principle for this architecture," this paper is a counterexample.

The **operative reading** -- the one the claim's own notes actually spell out, that errors do not "leave a persistent trace" that "actively modulate[s] trajectory selection on subsequent steps" -- survives intact, and the distinction is about timescale and specificity. SCoRe produces a *population-level prior*: the deployed model is better at the general behaviour "reconsider your last answer," learned offline over a distribution of past errors. It carries nothing forward from *this* error, just now, into the next step. REE's phi(z) is the opposite shape: a per-episode deposit, made at inference, read by the very next selection (ARC-005, INV-006, INV-008). Those are competing implementations of the same functional role -- letting error change behaviour -- separated by whether the record is episode-specific and whether it exists at inference time at all.

I want to be honest that this distinction is my reading, not the paper's finding. Kumar et al. are not testing EXT-002 and do not frame their contribution in these terms. A governance reader could reasonably decide the distinction is thinner than I have drawn it, and I have priced that in by capping `mapping_fidelity` at 0.60.

## Limitations

The paper was an unrefereed preprint at pull time -- I checked arXiv, OpenAlex, Crossref, DBLP and OpenReview on 2026-09-03 and found no venue. It evaluates two proprietary Gemini models on checkable-answer benchmarks (MATH, HumanEval), which is two steps removed from EXT-002's subject of open-ended factual hallucination: the tasks have verifiable answers, and the models are closed. The authors' own account of how easily the training collapses -- the SFT variants fail outright, and SCoRe needs a specific two-phase regularisation to avoid the same fate -- suggests the installed capability is fragile rather than a robust new architectural property. That fragility is itself mildly consistent with EXT-002: a genuine residue mechanism would not need to be coaxed into existence and defended against collapse.

## Confidence reasoning

`source_quality` 0.72: strong lab, well-designed negative controls, unrefereed. `mapping_fidelity` 0.60: this is a boundary case rather than a test, and the timescale argument that preserves the claim is interpretive. `transfer_risk` 0.40, the highest in the pull. The 0.62 aggregate is intentionally modest -- the entry's value to governance is that it exists and marks where EXT-002 must be stated carefully, not that it settles anything. If EXT-002 is ever promoted past `candidate`, its wording should be tightened to the per-episode inference-time reading, because the absolute reading has a published counterexample.
