# MECH-329 literature synthesis — developmental-ordering anchor correction

**Claim:** MECH-329 — *"The wanting system (mesolimbic dopamine / approach motivation) seeds z_goal anchors via accidental benefit contacts before the liking system (hedonic evaluation) is calibrated."*
**Subject:** development.wanting_before_liking_goal_seeding_sequence
**Status at pull:** candidate / confidence 0.0 (experimental); child mechanism of MECH-189; depends_on MECH-189 / SD-014 / INV-037 / INV-038.
**Pull date:** 2026-06-10. **Entries:** 3 (this dir) + 1 companion (Smith, Berridge & Aldridge 2011, filed under `targeted_review_mech_189`, tagged MECH-329).
**Why this pull exists:** the 2026-06-09/10 MECH-189 biology-before-formal-definitions pass found MECH-329's developmental-ordering anchor — "Keren-Portnoy & Tomasello 2021" — could not be independently verified (Keren-Portnoy publishes in infant speech/phonology, not reward/intentionality). The neural *separability* premise (Berridge & Robinson 1998; Smith et al. 2011) was already grounded; the developmental *ordering* was the thin link. This pull replaces the unverifiable anchor with verifiable sources and corrects claims.yaml.

## Entry-by-entry

| Component of MECH-329 | Entry | Direction | Verdict |
|---|---|---|---|
| Developmental ordering — goal-directed/intentional structure is operational early in infancy | Behne, Carpenter, Call & Tomasello 2005 (Dev Psych 41(2):328-37, DOI 10.1037/0012-1649.41.2.328) | supports (0.60) | **Grounded lower bound.** Goal-directed-action understanding emerges ~9 months; the canonical, verifiable replacement for the bogus Keren-Portnoy anchor, from the same lineage. Caveat: third-person goal attribution, not first-person approach drive. |
| Accidental-contact + approach-drive seeding (the actual mechanism) | Corbetta 2021 (Curr Dir Psychol Sci 30(5):418-424, DOI 10.1177/09637214211031939) | supports (0.58) | **Grounded structure.** Infant reaching originates ~3-5 mo from an *accidental* hand-target contact that "intrinsically motivates infants to reproduce the behavior" — MECH-329's seeding story in the motor-development literature, earlier than the 9-mo milestone. Caveat: "intrinsic motivation" is not pinned to mesolimbic DA. |
| Neuromodulatory identity / ontogeny of the reward circuit | Opendak, Meyer, Callaghan et al. 2025 (Transl Psychiatry 15:53, DOI 10.1038/s41398-025-03280-z) | **mixed** (0.55) | **Ordering supported, mesolimbic specificity stressed.** Mesolimbic DA "exhibit[s] late functional maturation" and is "likely not functional in supporting learning in the perinatal infant"; early reward learning is locus-coeruleus norepinephrine. "Behavioral similarity does not imply circuit continuity." |
| Neural separability of wanting/liking (premise) | Smith, Berridge & Aldridge 2011 (companion, in `targeted_review_mech_189`) | supports premise (0.55) | Separability confirmed in adult brain; not developmental ordering. |

## Verdict on the developmental-ordering link

**The ordering is now grounded; the mesolimbic-dopamine *attribution* for the earliest window is not — and should be held loosely.** Two independent, verifiable strands (Behne et al.: early third-person goal attribution; Corbetta: early first-person accidental-contact seeding under intrinsic motivation) establish that goal-directed/approach structure is operational in the first year, before a calibrated hedonic preference function exists. That is the temporal premise MECH-329 needs, and it replaces the unverifiable anchor cleanly.

The honest qualification — surfaced by the mixed Opendak et al. entry — is that MECH-329's *literal mechanism* ("**mesolimbic dopamine** wanting seeds the first anchors") is over-specified for the perinatal window: the developmental reward-circuit review says mesolimbic DA matures late and the earliest reward learning runs on norepinephrine. The robust, well-evidenced version of MECH-329 is therefore: *an early approach/incentive drive (neuromodulatory identity not yet adult-mesolimbic) seeds goal anchors from accidental benefit contacts before calibrated hedonic evaluation is in place.* The "wanting/liking" Berridge framing remains the right adult-circuit vocabulary; its developmental onset is what these three papers constrain.

This is a literature (parallel) signal only. It does not change MECH-329's `experimental_confidence` (0.0) or `status` (candidate). The validation experiment remains EXQ-ISEF-002 (transient benefit patches in the infant substrate).

## Action taken on claims.yaml

The unverifiable "Keren-Portnoy & Tomasello 2021" citation in MECH-329's `description` and `notes` was replaced with Behne, Carpenter, Call & Tomasello 2005 (verified) plus the Corbetta 2021 accidental-contact mechanism, and a one-line note that the mesolimbic-specific attribution is held loosely per Opendak et al. 2025. `experimental_confidence` and `status` untouched (lit/exp decoupling rule).
