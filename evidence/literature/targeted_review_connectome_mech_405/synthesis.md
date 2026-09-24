# MECH-405 targeted lit-pull (EMP-7 social-development + shared-representation)

## Entries
- 2026-09-24_mech_405_placebo_analgesia_reduces_pain_empathy_rutgen2015 -- supports, 0.68 -- placebo analgesia lowers own pain AND empathy for pain (AI/MCC), naltrexone reverses both: causal evidence other-directed pain affect runs through the self-pain channel.
- 2026-09-24_mech_405_empathy_pain_meta_analysis_shared_core_lamm2011 -- supports, 0.60 -- reliable AI/aMCC shared affective (not sensory) core, but paradigm-dependent mentalizing/action-understanding add-ons.
- 2026-09-24_mech_405_somatic_vicarious_pain_dissociable_patterns_krishnan2016 -- weakens, 0.60 -- own-pain and vicarious-pain fMRI decoders each at chance on the other; vicarious info sits in mentalizing circuits.
- 2026-09-24_mech_405_empathy_sharing_vs_mentalizing_review_zaki2012 -- mixed, 0.50 -- sharing route exists, but empathy also needs a separate mentalizing sub-process.
- 2026-09-24_mech_405_infant_concern_early_not_contagion_stage_davidov2020 -- mixed, 0.50 -- other-oriented concern present from 3 months with little self-distress; refutes contagion-first stage theory.

## Anchors
The claim names no specific citations, only "the EMP-7 social-development lit-pull". Focus anchors checked via PubMed this session:
- Singer et al. 2004 Science 303:1157-62 (PMID 14976305) -- verified; folded into the Lamm 2011 meta-analysis entry rather than given its own entry.
- Lamm, Decety & Singer 2011 NeuroImage 54(3):2492-502 (PMID 20946964; PubMed e-pub date 2010) -- verified.
- Zaki & Ochsner 2012 Nat Neurosci 15(5):675-80 (PMID 22504346) -- verified.
- Roth-Hanania, Davidov & Zahn-Waxler 2011 Infant Behav Dev 34(3):447-58 (PMID 21600660) -- verified; cited inside the Davidov 2020 entry (same cohort lineage, smaller n).
- Davidov et al. 2020 Dev Sci (PMID 32649796) -- verified.
- Decety developmental review: not pulled (Lamm 2011 co-authored by Decety covers the adult side).

## Implications for the claim TEXT (suggested; not applied)
1. Scope to the experience-sharing route: "other-bound affect DRAWS ON the agent's own affective streams via an other-model", not "IS own stream + binding". Krishnan 2016 and Zaki & Ochsner 2012 argue the other-bound representation is partly separately constructed by mentalizing machinery; the other-model is not a thin binding slot.
2. Restrict the shared streams to affective/motivational ones (explicitly exclude sensory) -- consistent with Singer 2004 / Lamm 2011; the claim already implies this, making it explicit costs nothing.
3. Revisit the gate "stable other-model required": infants show other-oriented concern from 3 months with rare self-distress (Davidov 2020; Roth-Hanania 2011). Either the gate is a rudimentary early other-model, or early concern runs without this mechanism. Also, no contagion->concern sequence should be assumed in any V5 developmental curriculum.
4. Candidate falsifiers for the eventual V5 experiment: (a) attenuating the self SD-011 channel should proportionally attenuate other-bound suffering (Rutgen 2015 analogue; intact other-bound affect would refute routing); (b) a probe trained on the self suffering channel should transfer to other-bound suffering magnitude above chance (Krishnan 2016 analogue; chance transfer favours a separate representation).
5. Overlap note: Lamm 2011's picture-based action-understanding recruitment is the ARC-010 mirror-modelling component, supporting the existing "review for merge with ARC-010" flag as a composition (ARC-010 input path + MECH-405 affective routing) rather than duplication.

## Could not verify / notes
- Did not pull emotional-contagion-in-neonates (e.g. reactive crying) or Decety developmental review; not needed for 2-5 entries.
- validate_literature.py --paths only scopes records inside the repo tree (records under /tmp gave "0 records checked"); validated instead by mirroring the schema + entries into a scratch --repo: OK, 5 records, 0 findings. All JSON parses.
