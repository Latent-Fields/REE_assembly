# Mather & Sutherland (2011) — arousal-biased competition

**Claim tested:** MECH-074b (content-selective per-trace retrieval weight, not scalar gain).
**Direction:** supports · **Confidence:** 0.68

## What the paper did

This is the theoretical synthesis behind "arousal-biased competition" (ABC). The authors argue that arousal does not raise the gain on everything; it *amplifies the existing competition* between representations, so that high-priority stimuli win more decisively and low-priority stimuli lose more decisively, in both perception and long-term memory. The framework was proposed precisely to reconcile the "puzzling contradictions" in the emotional-memory literature — why arousal sometimes enhances and sometimes impairs memory.

## Key finding relevant to the claim

The load-bearing point for MECH-074b is the *functional form* of the modulation. ABC says arousal is **priority-weighted, not uniform**: enhancement for high-priority items, impairment for low-priority items. That is the theoretical warrant for MECH-074b's central design decision — a per-trace weight vector w_i rather than a scalar retrieval gain. If the biologically correct modulation were a single multiplicative gain applied to all traces, ABC's central prediction (that arousal can *impair* peripheral memory) would be impossible. So this paper directly underwrites the "vector, not scalar" constraint and its named failure signature.

## Mapping to REE and its limits

Two caveats keep this at 0.68 rather than higher, and both are honest limits on the mapping, not on the theory.

First, **locus**. ABC is explicit that priority is set largely at perception and encoding (bottom-up salience plus top-down goals) and carried through consolidation. MECH-074b instead places the weight at *retrieval*, applied to already-stored hippocampal traces, and further asserts it *grows with trace age* (20 min → 1 week). ABC neither requires nor supplies a retrieval-time re-weighting; it is agnostic-to-contrary on MECH-074b's specific temporal claim.

Second, and more pointed, **substrate form**. ABC predicts genuine *absolute* impairment of low-priority items. MECH-074b's stated rule is w_i = 1 + α·arousal_tag_i with α ∈ [0.3, 1.0] — an additive weight that is always ≥ 1. That form can reproduce the *relative* advantage of central items but cannot, on its own, produce absolute suppression of peripheral traces. If REE wants to match the full ABC/lesion pattern (peripheral memory actually *worse*, as in Adolphs 2001), the substrate would need a competitive normalisation step, not just an additive per-trace boost. This is a concrete design flag worth carrying into the follow-up EXQ.

## Bottom line

Strong theoretical support for the *selectivity* MECH-074b is built around, with a genuine open question about whether the additive-only weight rule is rich enough to reproduce the competitive (winner-amplified, loser-suppressed) pattern the theory and the human data both show.

According to PubMed. Source: Mather M, Sutherland MR (2011), *Perspectives on Psychological Science* 6(2):114-33. [DOI](https://doi.org/10.1177/1745691611400234)
