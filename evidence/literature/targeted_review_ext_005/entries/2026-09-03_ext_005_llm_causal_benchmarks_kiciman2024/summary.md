# The counterweight: 97%, 92%, 86% — and the qualifier that saves the claim (Kıcıman et al., TMLR 2024) — EXT-005

**Source:** Kıcıman E, Ness R, Sharma A, Tan C. *Causal Reasoning and Large Language Models: Opening a New Frontier for Causality*. Transactions on Machine Learning Research, 2024. arXiv:2305.00050. Code/datasets: https://github.com/py-why/pywhy-llm.

## What the paper does

This is the serious case for the other side, and it is in this pull because a claim like EXT-005 deserves to meet its best opponent rather than a straw one. The authors run a behavioural benchmarking study across causal tasks and report that GPT-3.5/4-based algorithms **beat the best existing dedicated methods**: 97% on pairwise causal discovery (a 13-point gain), 92% on a counterfactual reasoning task (a 20-point gain), and 86% accuracy on event causality — determining necessary and sufficient causes in vignettes.

That last one deserves emphasis, because it is not a peripheral task. Necessary-and-sufficient-cause judgement over vignettes *is* actual causation. It is the closest published benchmark to the thing EXT-005 says LLMs have no mechanism for.

And the authors anticipate the obvious rebuttal. They run robustness checks and report that the capabilities cannot be explained by dataset memorisation alone, because performance holds on datasets constructed *after* the training cutoff. The simplest version of the recitation account — Zečević's causal parrots, measured by Jin's Corr2Cause — does not survive that.

## What this does to EXT-005, honestly

Read literally, EXT-005 says LLMs produce fluent causal language "without **any** internal mechanism that computes a genuine causal signature." These numbers embarrass that wording. A claim that predicts poor performance on actual-causation vignettes has been contradicted by an 86%, and the post-cutoff generalisation blocks the easy escape.

So the direction on this entry is `weakens`, not `mixed`. It is genuine contrary evidence, and recording it as anything softer would be dishonest.

But the qualifier the authors themselves supply is what tells REE where the real boundary lies, and it is a better boundary than the one EXT-005 currently draws. Their words: LLMs operate **on the text metadata**, and consequently they **ignore the actual data**. The 97% is obtained by reasoning over variable *names* and described context — the semantics of "altitude" and "temperature" — not over observations, and certainly not over interventions. That is an excellent causal-knowledge retrieval-and-composition system. It is not a causal signature.

The distinction matters because REE's proposed mechanism is on the other side of it. SD-029 computes `z_harm_s_observed − E2_harm_s(z_harm_s_{t−1}, a_actual)`: a residual against a forward model's prediction for an action *this agent just issued*. There is no text metadata for that. There is no variable name to reason over. The quantity exists only for a system holding an efference copy of its own action, and it is indexed to an occasion that has never been described by anyone. Nothing in this paper's task suite touches it, and nothing in this paper's method could produce it.

The conclusion I would actually draw for governance is that **EXT-005 should be narrowed rather than defended**. The blanket "no causal machinery" reading is now hard to hold. The claim that survives — and that REE's architecture actually answers — is: LLMs lack a *first-person, run-time* causal signature over their own interventions. That is narrower, it is more defensible, and it loses nothing REE needs.

## Limitations, in both directions

Against the paper: every task is third-person and textual — vignettes, variable pairs, described counterfactuals. Nothing here tests whether a model can attribute a state change to *its own* action, so this cannot be cited as evidence that it can. The 97%/92%/86% figures also depend on particular prompting strategies and particular benchmarks, and the authors' own report of "unpredictable failure modes" means they are not a floor. A system that is right 97% of the time with no signal about *which* 3% is not offering a causal signature; it is offering a good prior. And "surpassing the best-performing existing methods" is a comparison against prior causal-NLP algorithms, which were not strong.

In the paper's favour, and against the temptation to dismiss it: "it's only operating on text" is precisely the mode in which EXT-005 says the *illusion* is produced. If text-mode operation can reach 86% on necessary-and-sufficient causation, then the illusion is a good deal more capable than the claim's framing implies, and that is uncomfortable in a way worth sitting with rather than explaining away.

## Confidence

0.66. Source quality 0.85 — TMLR, presented at ICLR 2025 with Outstanding Certification finalist status, credible causal-inference authorship, and robustness checks the authors ran *against their own preferred conclusion*, which is the mark of a study worth taking seriously. Transfer risk 0.28. Mapping fidelity 0.58 is the lowest in this pull and caps the aggregate: the tasks contradict EXT-005's blanket wording while never once touching its self-attribution content.
