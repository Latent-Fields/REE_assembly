# The common mean vector is not content — removing it makes representations stronger

**Mu, Bhat & Viswanath (2018), ICLR.** [arXiv:1702.01417](https://arxiv.org/abs/1702.01417) · [OpenReview](https://openreview.net/pdf?id=HkuGJ3kCb)

## What the paper did

This is the prior-art paper for the operation SD-078 performs. The authors observed that off-the-shelf word representations — word2vec, GloVe — are not centered at the origin: every vector in the table shares a large common mean, and beyond that a handful of directions dominate the variance in a way that is shared across the whole vocabulary rather than distinguishing any part of it. Their proposal is a postprocessing step of almost embarrassing simplicity: subtract the common mean vector, then project out the top few principal directions (they suggest d/100). They then evaluated the processed representations across lexical tasks (word similarity, concept categorization, word analogy) and sentence-level tasks (semantic textual similarity, text classification), over multiple datasets, multiple embedding methods, multiple hyperparameter settings and multiple languages.

The result is that the processed representations are consistently better than the originals — not on average, not on a favoured benchmark, but across the board. The authors are explicit that this is counter-intuitive, and I think their framing of *why* is the most useful thing in the paper. Standard denoising by dimensionality reduction discards the *weakest* directions on the assumption that low energy means noise. Here the opposite move works: the highest-energy directions are the ones to discard, because energy shared by everything is precisely energy that distinguishes nothing.

## How this maps to SD-078

SD-078 subtracts a slow EMA estimate of the common mean from the `z_world` context key before every `CandidateRuleField` cue comparison — the mint-block cosine, the `_context_bucket` sign pattern, and `gate_and_select`. That is the first and principal step of this procedure, moved from an offline table to an online latent.

What the paper buys us is the general principle, and it buys it broadly. The component shared by every vector in a learned representation cannot, by construction, discriminate between them; keeping it in a similarity computation is not a conservative choice but an actively destructive one. It also pre-empts the obvious objection to SD-078 — that subtracting a high-magnitude direction must be throwing away real signal. The authors flag their own result as counter-intuitive for exactly that reason and then show it isn't, across enough settings that the burden shifts to anyone claiming the opposite. That is worth having on the record, because a reviewer meeting SD-078 cold is likely to reach for precisely that objection.

## Where the mapping is partial, and why I capped confidence at 0.70

REE implements half the operation. "All-but-the-top" is mean removal **and** removal of the top ~d/100 principal directions, and every number in the paper is for the combination. The authors do not decompose the gain, so I cannot honestly attribute their result to the half SD-078 actually does. The sibling entry in this directory (Timkey & van Schijndel 2021) *does* isolate it, and finds mean-removal alone to be the weaker of the two subtractive corrections — so the fair reading is that this paper licenses the *direction* of SD-078's fix without establishing its *sufficiency*.

There is a reason not to simply extend SD-078 to the full procedure, and it is worth recording now rather than rediscovering later. The number of directions removed is a hyperparameter, and Timkey & van Schijndel report all-but-the-top to be highly sensitive to it — ineffective at the final layer of GPT-2 for *any* choice of D. Adding PC removal to SD-078 would therefore trade a parameter-free fix for one with a tuning surface, in a codebase where SD-078's own restatement already demonstrates that a threshold knob (`mature_mint_block_threshold`) can be swept across its whole expressible range without touching the problem. I would want a measured reason before making that trade.

Two smaller gaps. The paper's mean is a static quantity over a fixed corpus; SD-078's is an online EMA over a non-stationary stream, which is a strictly harder estimation problem and one this paper does not address at all — SD-079's alpha work (0.05 rather than 0.02, because `z_goal` drifts) is doing something with no counterpart here. And the evaluation target throughout is agreement with human semantic-similarity judgments, which maps onto nothing in REE; "better" in this paper is not measured on anything resembling rule minting or gate retrieval.

## Confidence

0.70, with mapping fidelity as the binding constraint rather than source quality. The paper is strong and unusually broad for what is essentially a three-line postprocessing note, and it has been reproduced widely enough that I am not worried about the finding itself. The discount is entirely about the gap between what was evaluated and what we built: this is prior art for the family, not validation of the instance. For an architectural `design_decision` claim the useful question is narrower than that — is this a known-good move? — and on that question the paper is clear.
