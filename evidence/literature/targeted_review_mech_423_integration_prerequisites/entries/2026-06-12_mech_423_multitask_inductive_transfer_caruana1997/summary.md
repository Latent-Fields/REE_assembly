# Caruana (1997) — the ML precedent for "integrated beats isolated", and the relatedness condition that bounds it

**Claim grounded:** MECH-423 (cross-model super-additivity) — the headline mechanism (shared representation yields transfer gains) *and* the readiness/regime caveat (gain is conditional on relatedness).
**Direction:** mixed. **Confidence:** 0.72.

## What the paper did

Caruana's *Multitask Learning* is the paper that established hard parameter sharing. The thesis: if you train several related tasks in parallel through a shared hidden representation, the inductive bias carried in each task's training signal helps the others, and every task generalises better than it would trained alone. The shared layer discovers features useful across tasks; the task-specific heads read them off. Critically, he showed backprop MTL discovers task relatedness *without* being told which tasks are related, and replicated the effect across backprop nets, k-nearest-neighbour and kernel regression. This is the direct ancestor of essentially all shared-representation learning.

## Why it speaks to MECH-423

MECH-423's INTEGRATED-PAIR arm — E1 world-model and E2 affordance-model trained over a shared L-space latent with cross-module gradient flow — *is* a hard-parameter-sharing MTL system. Caruana is therefore the closest existing demonstration that the integrated configuration can beat the isolated one, and that the gain comes precisely from features developed for one objective being reused by another. This supports the *existence* of the phenomenon MECH-423 asserts: cross-pollination over a shared representation is a real, repeatedly-demonstrated source of capability gain, not a speculation.

But the entry is tagged **mixed**, and the reason is the load-bearing caveat for the whole lit-pull. Caruana is explicit that the benefit is *conditional on task relatedness*. Share a representation across tasks that do not share underlying structure and you get no transfer — and sometimes you get interference. This is exactly the readiness/regime point: a sub-additive or null result on EXP-0380 could mean the modules paired in the integrated arm were not related enough, *not* that integration-over-shared-latents fails as a mechanism. It is the ML-side echo of Kumaran's schema-consistency result. The design implication is the same: pair modules whose features genuinely overlap (the E1<->E2 overlap that the proposal already centres on), and pre-register that relatedness so a null is interpretable.

## Limitations and mapping caveats

Caruana measures *generalisation improvement over single-task baselines*, which is a weaker bar than EXP-0380's framing of super-additivity as *gain exceeding the sum of the isolated modules' marginal gains*. The additive-baseline test is stricter, so Caruana grounds the direction of the effect more than its exact magnitude. And because the benefit is conditional, the paper simultaneously supports the mechanism and bounds its universality — hence the mixed direction.

## Confidence reasoning

Source quality 0.85 (foundational, thousands of citations, the origin of the technique REE's integrated arm uses). Mapping fidelity 0.72 — REE's integrated arm is genuinely an MTL system, though the additive-baseline bar is stricter than Caruana's comparison. Overall 0.72, with the mixed direction capturing that this paper is both the strongest support for the claim's plausibility and the clearest statement of the relatedness condition the readiness gate must enforce.
