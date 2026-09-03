# Reflexion: Language Agents with Verbal Reinforcement Learning (Shinn et al., NeurIPS 2023)

**Claim tested:** EXT-002 -- *Hallucination: no persistent error residue accumulates to shape future outputs.*
**Direction:** supports (by remedy) | **Confidence:** 0.70

## What the paper does

Reflexion addresses a practical problem: LLM agents interacting with environments -- games, compilers, APIs -- cannot learn from trial and error the way an RL agent does, because the obvious route (fine-tuning on the failures) is slow and expensive. The authors' answer is to reinforce the agent "not by updating weights, but instead through linguistic feedback." After a failed trial the agent writes a verbal reflection on what went wrong; that reflection is stored in an episodic memory buffer; the buffer is fed back into the context on the next trial. Feedback can be scalar or free-form, external or internally simulated. Across ALFWorld, HotpotQA and code generation the gains are substantial -- the headline figure is 91% pass@1 on HumanEval against 80% for the GPT-4 baseline.

## Why this belongs in an EXT-002 pull

Not for its results, but for its architecture. EXT-002 asserts that transformer LLMs have no mechanism for prediction errors to leave a persistent trace that shapes future outputs. Reflexion is, in effect, that mechanism built by hand and bolted on from outside. The paper does not argue with the premise; it takes it as given and engineers around it. That a working research group had to construct an external text buffer, decide what to write into it, and manually re-inject it into the next trial's context is direct evidence about what the base system does not carry. The phrase "not by updating weights" is the concession: there is no route by which the failure changes the model, so the record has to live somewhere else.

Two structural differences between the buffer and REE's phi(z) are worth recording, because they mark what a native residue would buy. First, Reflexion's record is symbolic and episodic where phi(z) is continuous and latent -- the agent must *re-read and re-interpret* its own prose about a past failure, rather than having the failure modulate trajectory selection continuously as a field term (ARC-005, INV-006, INV-008). That re-interpretation step is itself a generation, with all the same failure modes. Second, the buffer lives outside the model and is therefore optional: it can be truncated, cleared, or never supplied. A residue field is not optional; it is part of the state that selection reads.

## The important caveat, and it is a live one

Huang et al. (ICLR 2024 -- also in this pull) explicitly list Reflexion in their table of self-correction work whose evaluation uses oracle labels to decide when to stop iterating. That matters here, and I want it stated rather than buried. It means the headline numbers cannot be cited as evidence that the model detects its own errors. What they can be cited for is narrower and, for EXT-002, still the relevant thing: that once an error record is supplied from outside, it is functionally useful. The claim EXT-002 makes is about the *absence* of the record, not about whether the model could generate the record's contents itself. The oracle dependency, if anything, deepens the support -- both the trace and the signal that an error occurred had to come from outside.

The broader caveat is that remedy evidence is indirect. "Adding X helps" is consistent with "X is absent" but also with "a degraded version of X is present." Nothing here rules out a partial internal error signal that the buffer merely augments. And the benchmarks -- agentic task completion and code generation -- sit further from open-ended factual hallucination than the other entries in this pull, so the argument runs through the design of the scaffold rather than through what was measured.

## Confidence reasoning

`source_quality` 0.85 reflects NeurIPS 2023 and a framework that has been widely reimplemented, with ablations over feedback type and source. `mapping_fidelity` at 0.62 is the limiting term, carrying both the indirectness of remedy evidence and the oracle-label restriction on which results are usable. `transfer_risk` 0.35 is the highest in this pull. The 0.70 aggregate is deliberately below the two directly-measuring entries: this is a good entry for *what the missing mechanism would be worth*, and a weak one for *establishing that it is missing*.
