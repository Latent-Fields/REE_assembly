# targeted_review_mech_308 -- REPORT

## Entries
- 2026-09-24_mech_308_symbolic_play_language_meta_analysis_quinn2018 -- supports, 0.52 -- 35-study meta-analysis, r ~ .35 play-language association stable across age 1-6 and concurrent/longitudinal designs; correlational only.
- 2026-09-24_mech_308_pretend_play_causal_review_lillard2013 -- weakens, 0.55 -- Psych Bull review: for language the evidence cannot separate crucial-cause, equifinality and epiphenomenon; no support for play being necessary.
- 2026-09-24_mech_308_joint_engagement_predicts_communication_carpenter1998 -- supports, 0.50 -- joint engagement and maternal follow-in talk predict first gestures/words; social skills ordered where nonsocial ones are not (n=24).
- 2026-09-24_mech_308_walking_onset_predicts_language_walle2014 -- weakens, 0.40 -- walking onset predicts a vocabulary jump independent of age, so a motor milestone also tracks language (challenges A1 specificity).
- 2026-09-24_mech_308_play_language_dissociate_with_age_otoole2006 -- mixed, 0.35 -- in Down syndrome, play-language link specific vs nonverbal IQ but weakens with age as language becomes domain-specific.

Validator: `validate_literature.py` run against a scratch copy of the entries (the script only scopes paths inside a repo): OK, 5 records, 0 findings. All JSON parses.

## Anchors named in the claim
- Tomasello joint-attention -> language onset: VERIFIED. Carpenter, Nagell & Tomasello 1998 (PMID 9835078), entered. Tomasello & Farrar 1986, "Joint attention and early language", Child Dev 57(6):1454-63, PMID 3802971, also verified (joint-play episodes, follow-in reference correlates with 21-month vocabulary; experimental word learning). Not entered separately to avoid overweighting one research programme; worth adding if the parent wants a sixth entry.
- Bates (symbols): VERIFIED as a book, Bates (with Benigni, Bretherton, Camaioni, Volterra) 1979, The Emergence of Symbols: Cognition and Communication in Infancy, Academic Press (WorldCat/Google Books hits). Not entered: no full text retrieved, and its "common symbolic capacity" reading is a rival to MECH-308's play-substrate reading, not support for it.
- "pretend-play -> theory of mind -> compositional language" chain: no direct source found; Lillard et al. 2013 finds pretense-ToM correlations inconsistent and leaning epiphenomenal. Treat this chain as unsupported.
- Also verified, not entered: Bottema-Beutel 2016, Autism Res 9(10):1021-1035, PMID 27059941, doi 10.1002/aur.1624. Joint attention-language meta-regression (71 reports): the association is weaker in typical development than in ASD, which the author reads as TD language "untethered" from JA variation above a threshold. That is a threshold/permissive-gate pattern, not continuous tracking, and is relevant to the claim's "tracks" wording.

## Implications for the claim text (suggested, not applied)
1. The literature supports co-variation (r ~ .35 for symbolic play; joint engagement predicts first words) but not the substrate/necessity assertion ("not via a parallel language-acquisition substrate"; "systems without play_mode fail"). Suggest splitting the claim: a weak developmental-tracking claim (supported, correlational) and a separate architectural claim that language is instantiated within play_mode (currently unsupported by human data, testable only via A2).
2. A1 specificity is at risk: Walle & Campos show walking onset also predicts vocabulary gains independent of age. A1 needs a head-to-head play vs motor comparison; none was found. Walking's effect may be mediated by social/play opportunities, which the claim could accommodate if stated in advance.
3. Consider a "bootstrap then consolidate" amendment: O'Toole & Chiat 2006 and Bottema-Beutel 2016 both show the play/JA-language coupling weakening as language matures. The claim's current wording predicts continued dependence; the data fit play as an onset scaffold better.
4. Name equifinality (Lillard et al. 2013) as an explicit falsifier risk: if language reaches normal levels by routes that bypass play, the claim's prediction for play-less systems fails.
5. Lillard's review is 2013 in print (Psychol Bull 139(1)); PubMed's epub date is 2012. Entry uses 2013.

## Could not verify
- Quinn, Donnelly & Kidd 2018: publisher, Semantic Scholar and MPG pages were egress-blocked. Title, authors, venue, year and DOI (10.1016/j.dr.2018.05.005) come from WebSearch result listings; volume 49 and pages 121-135 and the r = .35 figure come from a search snippet quoting a later paper (Creaghe et al. 2021). Worth a quick check by the parent before commit.
- McCune's play-language level correspondence work: not searched to completion; not entered.
- No study found where language develops normally despite absent play (the strongest possible dissociation test of MECH-308).
