# Jin & Costa 2010 — Start/stop signals in nigrostriatal circuits (SD-045 chunk bracketing)

**Claim grounded:** SD-045 (action-chunk cache in the ARC-021 dorsolateral-loop slot).
**Direction:** supports. **Confidence:** 0.84.

## What the paper did

According to PubMed, Jin & Costa (2010, *Nature*; [DOI](https://doi.org/10.1038/nature09263)) trained mice on a self-paced operant task in which the animal had to perform a particular sequence of actions to obtain an outcome, and recorded from nigrostriatal circuits across learning. The central finding is that, as the sequence was learned, a population of neurons developed activity that fired specifically at the **initiation** or the **termination** of the whole action sequence — not throughout it. This start/stop activity was not present early in training; it *emerged* with learning. Critically, it was specific to particular actions and did not track interval timing, movement speed, or action value, ruling out the obvious confounds. The authors then genetically altered striatal circuit function and showed this both disrupted the development of start/stop activity and selectively impaired sequence learning — establishing the signal as causally necessary, not merely correlated.

## Why it matters for SD-045

SD-045 is the only one of the abstraction-substrate pillars with an explicit pull-forward condition, and it rests on a specific computational picture: frequently-traversed action sequences get cached as a unit, executed without re-rolling through E2+CEM, and **gated by task-bracketing-analogue start/end signals**. The Graybiel 2008 review (already in this directory) is the synthesis that names this picture; Jin & Costa supply the direct circuit-level evidence underneath it. They show the bracketing signals are (a) real, (b) learned rather than innate, (c) dissociable from value and timing — which is exactly the property SD-045 needs, since the cache is indexed by a start-state signature and an expected-outcome signature, not by reward — and (d) causally required for the sequence to consolidate. So the entry upgrades SD-045's grounding from "a leading authority asserts chunking exists" to "the start/stop gating mechanism has been recorded and lesioned."

## Limits and honest caveats

The evidence is rodent motor-sequence learning under heavy over-training, and the start/stop signature *emerged* only after substantial repetition. REE's episodes are short (200–500 steps), so it is genuinely unclear whether a V3 substrate would ever accumulate enough repetition to induce a chunk-bracketing signature — this is a real constraint on any monostrategy-triggered pull-forward, not a footnote. The paper also localises the signal to nigrostriatal circuits broadly and does not resolve the dorsolateral-vs-dorsomedial split that SD-045 assumes when it places the cache in the ARC-021 dorsolateral-loop slot. And the leap from fixed motor sequences to REE's context-variable cognitive "chunks" (resources respawn, hazards move) means the primitive must be made context-conditional rather than fixed-trigger. So I read this as strong warrant for the *existence and learnability* of the gating mechanism, and weaker warrant for the specific dictionary-cache instantiation — hence 0.84 rather than higher.

This raises SD-045's literature_confidence only. Experimental_confidence stays 0 (SD-045 is `implementation_phase: v4`, no V3 experiment) — **this promotes nothing.**
