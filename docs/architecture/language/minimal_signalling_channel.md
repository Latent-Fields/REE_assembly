---
title: Minimal Signalling Channel
parent: Language
grandparent: Architecture
nav_order: 7
---

# Minimal Signalling Channel

**Claim Type:** mechanism_hypothesis  
**Scope:** Minimal signalling channel  
**Depends On:** ARC-009, ARC-010  
**Status:** candidate  
**Claim ID:** MECH-014
<a id="mech-014"></a>

---

Source: `docs/processed/legacy_tree/architecture/language/minimal_signalling_channel.md`

> **Elaborates Section 5 (Social Extension: Language) of `REE_CORE.md`.**

# Minimal Signalling Channel (Pre-language)

Before full language, REE benefits from a minimal signalling interface that can externalise:
- harm/degradation alerts
- intent/commitment markers
- uncertainty/confidence markers
- "stop/avoid" priors (trajectory warnings)

### Interface sketch
Inputs: internal summaries (z_theta/z_delta slices, residue flags, confidence)
Outputs: discrete or continuous signals that other agents can condition on

**Evidential note (2026-09-14 targeted literature pull, `evidence/literature/targeted_review_mech_014/`, 5 entries, avg confidence 0.57):** none of the three design constraints below is refuted, but two were written more strongly or less conditionally than the evidence supports. See the note under **Related Claims** for the full breakdown and citations; the revisions are folded into the list itself here.

### Design constraints
- Signals are integrated via trust-weighting (reliability inference); the reliability estimate is volatility-sensitive (updates faster when a sender's trustworthiness is currently unstable) and enters selection as its own weighted term, alongside rather than overwriting the receiver's own value/harm estimates
- Signals may legitimately shift the receiver's expectation and arousal, but cannot suppress the experiential harm-learning update that registers harm when it actually arrives in the receiving agent -- narrower than "cannot mask embodied harm channels" as originally stated: a signal overriding expectation or arousal is not itself a masking failure; a signal suppressing registration of harm that is actually occurring is
- Signals should be cheap relative to full other-model inference when sender and receiver interests are aligned; under conflicting incentives, part of the other-model cost re-enters through the trust estimator rather than being avoided
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-014

**2026-09-14 targeted literature pull** (`evidence/literature/targeted_review_mech_014/`, 5 entries, avg confidence 0.57): narrowed and conditioned two of the claim's three design constraints rather than splitting the claim into new ids -- MECH-014 remains substrate-blocked behind ARC-009/ARC-010, so minting untestable children would inflate the candidate tail without adding near-term testability; the reworded constraints above capture the refinement instead. The non-masking constraint was narrowed: Atlas et al. (2016, confidence 0.60, mixed) found verbal instruction left amygdala reinforcement-driven threat learning untouched (supporting a protected experiential harm stream) while it reversed skin conductance almost completely (rho=0.943) and updated striatal/OFC value signals before any shock was delivered -- so "cannot mask embodied harm channels" as originally stated is false if arousal/expectation count as embodied; what the evidence actually supports is narrower, that the experiential harm-learning update itself stays closed to incoming signals. The cheapness constraint was conditioned: Diaconescu et al. (2014, confidence 0.52, mixed) found that when an adviser's incentive to mislead varied, receivers' best-fitting strategy was hierarchical inference on the adviser's intentions -- exactly the costlier other-model computation the constraint says signals should let an agent avoid -- so cheapness holds only under sender-receiver interest alignment, not unconditionally. The trust-weighting constraint was sharpened (not narrowed) by two supporting sources: Behrens et al. (2008, confidence 0.66, supports) showed reliability inference is volatility-sensitive and combines with the receiver's own value estimates only at choice, in a separate weighted stream, rather than overwriting them; Diaconescu et al. (2014) independently showed the same volatility-sensitivity from the receiver side. Kendal et al. (2018, confidence 0.50, supports) gives the evolutionary rationale for both trust-weighting and cheapness (indiscriminate copying is rarely adaptive; selectivity can be implemented by ordinary associative learning) but tests neither constraint directly. Seyfarth, Cheney & Marler (1980, confidence 0.55, supports) is the canonical existence proof that a small set of discrete pre-linguistic signals can carry action-specific harm/stop-avoid warnings cheaply, grounding the claim's premise rather than any one constraint; its infant data also note, as an open point this doc does not otherwise address, that the sender side of such a channel is learned and starts over-inclusive. No REE agent currently has a signal substrate or a second agent to test any of this against (this claim is substrate-blocked behind ARC-009/ARC-010). Flagged to governance as GFLAG-0277 (contested_disposition) to confirm this reword is an adequate disposition.

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/language/minimal_signalling_channel.md`
- `evidence/literature/targeted_review_mech_014/entries/2026-09-14_mech_014_instructions_do_not_update_amygdala_threat_learning_atlas2016/`
- `evidence/literature/targeted_review_mech_014/entries/2026-09-14_mech_014_hierarchical_inference_on_adviser_intentions_diaconescu2014/`
- `evidence/literature/targeted_review_mech_014/entries/2026-09-14_mech_014_trust_weighted_advice_parallel_acc_streams_behrens2008/`
- `evidence/literature/targeted_review_mech_014/entries/2026-09-14_mech_014_selective_social_learning_strategies_kendal2018/`
- `evidence/literature/targeted_review_mech_014/entries/2026-09-14_mech_014_vervet_alarm_calls_cheap_referential_warnings_seyfarth1980/`
