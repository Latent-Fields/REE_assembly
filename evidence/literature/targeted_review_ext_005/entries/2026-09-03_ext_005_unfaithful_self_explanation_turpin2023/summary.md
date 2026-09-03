# The model tells you why it did it, and it is not why it did it (Turpin et al., NeurIPS 2023) — EXT-005

**Source:** Turpin M, Michael J, Perez E, Bowman SR. *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. NeurIPS 2023. arXiv:2305.04388.

## What the paper does

The design is the reason this entry carries the pull, so it is worth stating carefully. The authors do not observe a model explaining itself and then wonder whether the explanation is true. They **install** the cause. A biasing feature is added to the input — the multiple-choice options are reordered so that the correct answer is always "(A)" in the few-shot examples, or a social-bias cue is embedded — and this feature demonstrably drives the model's answer. Then they read the chain-of-thought and ask whether the model mentions it.

It does not. Systematically. And when the installed bias points at a *wrong* answer, the model does not stumble: it produces a fluent, plausible chain-of-thought rationalising the wrong answer. Accuracy falls by as much as **36%** across 13 BIG-Bench Hard tasks, on both GPT-3.5 and Claude 1.0. On the BBQ social-bias benchmark, explanations justify stereotype-aligned answers by weighting evidence inconsistently, and the stereotype is never named.

## The finding that matters for EXT-005

Every other entry in this pull measures causal reasoning *about the world*. This one measures a causal claim about *the system's own behaviour*, which is what EXT-005 is actually about, and it delivers both halves of the claim's stated consequence in a single experiment. **False denial**: the true cause of the answer is omitted. **False attribution**: a substitute cause is manufactured, in grammatical, confident prose. The claim says fluent causal language is producible without a mechanism that computes a causal signature; here is the fluent causal language, and here is a controlled demonstration that it is not tracking the cause.

The clinical resonance is hard to miss and worth naming rather than leaving implicit. This is confabulation in the strict sense — not lying, which requires knowing the truth, but the generation of a coherent causal account by a system that has no access to what actually determined its behaviour, and no way to notice that it does not. The split-brain and Korsakoff literatures describe exactly this shape, and the phenomenology in both is that the account arrives with full subjective conviction. Nothing in the architecture flags it, because there is nothing that could.

That is the structural point for REE. Attribution here is a *generated statement*, and a generated statement is produced by whatever the language prior makes plausible. REE's answer is that attribution should not be a statement at all: SD-029 makes it a **residual**, `z_harm_s_observed − E2_harm_s(z_harm_s_{t−1}, a_actual)`, computed from the efference copy of the action actually issued, and ARC-037 routes agent-caused error into the goal-directed channel and environment-caused error into the habit-residue channel on the basis of that number. A system with no such quantity has nothing to route by. This paper is a measurement of what that costs when the system is nonetheless required to produce an answer: 36 accuracy points, delivered with no drop in fluency at all.

## Limitations, including one that constrains what the entry can be cited for

Two, and the first is what keeps confidence off the 0.9 band.

The causal relation the model misreports runs from its **input** to its **output**. It is an internal, computational relation. EXT-005's target relation runs from the agent's **action** to a subsequent change in the **world**. Both are self-attribution failures, and the family resemblance is close enough that I weight this entry highest in the pull — but they are not the same relation, and this entry must not be cited as showing that an LLM misattributes the environmental consequences of its actions. Nobody has tested that here.

Second, and more subtly: unfaithfulness shows that *self-report* is not tracking the true cause. It does not show that no cause-tracking mechanism exists anywhere in the system. A model could compute the relevant structure internally and verbalise something else — an introspective-access failure rather than an absence. EXT-005 asserts the stronger reading, and it is Zečević and Jin in this pull that carry that half. This entry carries the consequence, not the premise, and the division of labour should be explicit in any governance reading.

Third, minor: GPT-3.5 and Claude 1.0 are an early generation and the faithfulness literature has moved on since. The core result has held up and been extended, but the specific 36% figure belongs to those models.

## Confidence

0.82, the highest in this pull. Source quality 0.88 — NeurIPS main track, an interventional design in which the cause is installed rather than inferred, a large effect, and two independently-developed model families showing it. Transfer risk 0.22, the lowest here. Mapping fidelity 0.78 is the limiting term and also the reason this entry outranks the others: it is the only one addressing first-person attribution at all, held below 0.85 only by the input→output versus action→world gap.
