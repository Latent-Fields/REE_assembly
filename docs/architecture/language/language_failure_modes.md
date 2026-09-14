---
title: Language Failure Modes
parent: Language
grandparent: Architecture
nav_order: 5
---

# Language Failure Modes

**Claim Type:** mechanism_hypothesis  
**Scope:** Language failure modes  
**Depends On:** ARC-009, ARC-010  
**Status:** candidate  
**Claim ID:** MECH-013
<a id="mech-013"></a>

---

Source: `docs/processed/legacy_tree/architecture/language/language_failure_modes.md`

> **Elaborates Section 6 (Failure Modes) of `REE_CORE.md`.**

# Language Failure Modes

When language decouples from embodied ethical signals, failure can be severe.

**Evidential note (2026-09-11 targeted literature pull, `evidence/literature/targeted_review_mech_013/`, 6 entries, lit_conf 0.674):** the five failure modes below do not share the same evidential standing, and the pull found the list needs to be read as two well-supported items, one mechanism-shaped-but-thin item, one contested item, and one item whose pathology mapping was wrong. See the note under **Related Claims** for the full breakdown and citations; the summary is folded into the list itself here.

Common failure modes:
- **Rationalisation -- MISREPORT reading** (well-supported): language generates a justification that is not constrained by, and does not reflect, the evaluation that actually drove the choice. Hall, Johansson & Strandberg (2012) showed 69% of participants failed to detect a covert reversal of their own stated moral position and argued unequivocally for the opposite of what they had endorsed; Turpin, Michael, Perez & Bowman (2023) showed LLM chain-of-thought explanations build a plausible case for a biased answer without ever mentioning the bias that produced it. Both are silent on suppression -- see below.
- **Rationalisation -- SUPPRESSION reading** (weakly supported, kept as a hypothesis): language turns an aversive/harm signal down, rather than merely narrating around it. Jarcho, Berkman & Lieberman (2011) is the only source found that measures anything at the signal level -- reduced bilateral anterior insula activity paired with later attitude change in a non-linguistic, non-ethical (name/painting) choice task, n=12 analysed -- and supplies a plausible mechanism *shape* (a regulatory gain reduction on the harm/residue stream at the commit step, i.e. the claim's own "precision misrouting" pathology) without showing language does the suppressing or that the suppressed signal is harm-related. Walker et al. (2021) bears on this only indirectly: the euphemism effect on harm judgment shrinks, but does not vanish, as the concreteness of the non-linguistic evidence about the act increases -- i.e. language's leverage is gated by how well-specified the non-linguistic harm evidence already is, not evidence that language suppresses an agent's own signal.
- **Bureaucratic dissociation** (supported, now with a mechanism): harm abstracted until it no longer registers as degradation. Walker et al. (2021, n=1906) found an agreeable label ("enhanced interrogation" vs "torture") shifted harm judgment on an identical described act, an effect that weakens as descriptive detail about the act increases -- bureaucratic language works less by lying than by removing the concrete detail that would otherwise anchor the appraisal.
- **Moral licensing** (CONTESTED -- do not treat as a common/established mode): symbolic 'good acts' used to justify later harm. Kuper & Bott (2019) applied two bias corrections to the moral-licensing meta-analytic literature (91 studies, n=7,397) and found the effect shrinks from the published d=0.31 to d=-0.05 (PET-PEESE, non-significant) or d=0.18 (3-parameter selection model, small), disagreeing on whether anything survives; the effect is also culture-moderated, so not a general property. Even a real effect maps only loosely onto this claim's mechanism, since licensing experiments manipulate recalled/performed good deeds rather than isolating language as the decoupling agent. Do not build symbolic moral-credit discounting into REE as a default dynamic on this basis.
- **Reputation substitution** (untested directly; one indirect anchor): moral residue replaced by social scoring. No source tested this limb directly. Walker et al. (2021) gives it an indirect anchor: participants rated euphemistic (but not literally false) descriptions as largely truthful, and rated speakers using them as more trustworthy than liars -- a reframe that carries no reputational penalty is exactly the kind of move a social-scoring system would reward, though this was not tested as substitution for residue.
- **Ideological capture -- pathology mapping corrected**: fixed symbolic frames were asserted to override perception and residue. Kaplan, Gimbel & Harris (2016) scanned belief resistance to counterevidence and found the opposite of an override signature: participants who changed their minds *more* showed *less* insula/amygdala response to counterevidence, i.e. the frame appears to **recruit** affect to defend itself (identity-bound propositions evoke a harm-like signal when threatened) rather than silencing it. This maps to the "spurious residue from narrative contamination" pathology below, not to suppression/override, and gives a distinguishable future prediction: capture should appear as harm-like signal evoked by frame-threatening evidence, not as an absent harm signal on frame-consistent harm.

These map to REE pathologies:
- residue externalisation,
- precision misrouting (the suppression reading of rationalisation, per Jarcho 2011 above),
- other-model collapse,
- spurious residue from narrative contamination (ideological capture, per Kaplan 2016 above -- not suppression/override).

**What would answer this (future test sketch, substrate-blocked -- see below):** once a REE instance has a real (non-sketch) symbolic output channel (ARC-009) reporting on its own action selection, the misreport and suppression readings of rationalisation come apart cleanly and should be tested separately: misreport is whether the reported justification tracks the actual E3/residue determinants of the choice (read the residue field and harm streams directly, never the language report, per the Hall/Turpin evidence above); suppression is whether emitting the justification is accompanied by a measurable gain reduction on the harm/residue stream at the commit step (the Jarcho signature). Bureaucratic dissociation and reputation substitution predict that the *precision* of the non-linguistic harm evidence available to the reporting layer gates the size of any language-driven shift in downstream harm appraisal or reputational cost (Walker 2021). Ideological capture predicts a harm-like signal evoked by frame-threatening evidence on identity-bound propositions, not an absent signal on frame-consistent harm (Kaplan 2016). Reputation substitution and any social-scoring failure additionally require a second agent (ARC-010) to score against. No REE agent currently has a symbolic output channel or a multi-agent substrate to condition on (GFLAG-0269 tracks substrate classification for the whole ARC-009/ARC-010 language cluster, MECH-011 through MECH-015, including this claim).

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-013

**2026-09-11 targeted literature pull** (`evidence/literature/targeted_review_mech_013/`, 6 entries, lit_conf 0.674): separated MECH-013's five failure modes by evidential standing rather than splitting the claim into new ids -- all five remain substrate-blocked behind the same ARC-009/ARC-010 dependency (GFLAG-0269), so minting untestable children would inflate the candidate tail without adding near-term testability; the differentiated `what_would_answer` above and the reworded list capture the granularity distinction instead. Rationalisation's misreport reading (Hall 2012, Turpin 2023) and bureaucratic dissociation (Walker 2021) are the best-supported items. Rationalisation's suppression reading has only a thin mechanism-shape source (Jarcho 2011, n=12, non-linguistic, non-ethical) plus an indirect gating result (Walker 2021). Moral licensing is contested (Kuper & Bott 2019, bias-corrected d approx 0 to small) and should not be treated as common. Ideological capture's pathology mapping moved from suppression/override to "spurious residue from narrative contamination" (Kaplan 2016). Reputation substitution remains untested directly, with one indirect anchor (Walker 2021's dishonesty-rating result). Flagged to governance as GFLAG-0276 (contested_disposition).

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/language/language_failure_modes.md`
- `evidence/literature/targeted_review_mech_013/entries/2026-09-11_mech_013_moral_choice_blindness_confabulated_arguments_hall2012/`
- `evidence/literature/targeted_review_mech_013/entries/2026-09-11_mech_013_unfaithful_cot_rationalization_turpin2023/`
- `evidence/literature/targeted_review_mech_013/entries/2026-09-11_mech_013_rationalization_insula_downregulation_jarcho2011/`
- `evidence/literature/targeted_review_mech_013/entries/2026-09-11_mech_013_euphemism_shifts_harm_judgment_walker2021/`
- `evidence/literature/targeted_review_mech_013/entries/2026-09-11_mech_013_moral_licensing_publication_bias_kuper2019/`
- `evidence/literature/targeted_review_mech_013/entries/2026-09-11_mech_013_political_belief_resistance_dmn_kaplan2016/`
