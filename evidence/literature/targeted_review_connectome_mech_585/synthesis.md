# MECH-585 targeted pull -- report (targeted_review_connectome_mech_585)

## Entries
- 2026-09-24_mech_585_insula_risk_prediction_error_preuschoff2008 -- mixed, 0.50 -- anterior insula carries a risk prediction error (expected-error channel beside the first-order PE), but risk is aleatoric lottery variance in a reward task, not predictor self-reliability.
- 2026-09-24_mech_585_pain_expectation_precision_pag_grahl2018 -- supports, 0.55 -- precision of a pain expectation is represented (PAG/RVM) and weights its influence; belief precision, calibration not tested.
- 2026-09-24_mech_585_aversive_volatility_learning_rate_browning2015 -- mixed, 0.50 -- aversive learning rate tracks volatility in low-anxious people, fails in high-anxious; reliability tracked is a world property.
- 2026-09-24_mech_585_pain_expectancy_confirmation_bias_jepma2018 -- weakens, 0.45 -- pain PEs are weighted by whether they confirm the prior (confirmation bias), the opposite of calibrated world-vs-model attribution.
- 2026-09-24_mech_585_uncertainty_increases_pain_yoshida2013 -- mixed, 0.40 -- uncertainty of a pain prediction is separate from its mean but AMPLIFIES harm (hyperalgesia) rather than discounting the prediction.

## Anchors named in the claim
- Yu & Dayan 2005 (PMID 15944135), Bach & Dolan 2012 (PMID 22781958), Seymour 2019 (PMID 30897355): not re-pulled; the claim marks them as existing-corpus entries, and they were outside this pull's focus. Not checked here.
- The OWED pull on harm-predictor reliability (insula/ACC) is this one. Also checked: Behrens 2007 (ACC volatility, PMID 17676057) and Geuter 2017 (insula predictive coding of pain, PMID 28524817) are already in the corpus for other claims (MECH-003/Q-041/Q-042; SD-020) and were not duplicated. Browning 2015 is also in the corpus under ARC-052; the MECH-585 entry maps it to this claim specifically.

## Implications for the claim text
1. No paper found shows a biological harm predictor estimating ITS OWN model error, or separating world surprise from model error. Every reliability signal found is either aleatoric outcome variance (Preuschoff), environmental volatility (Browning, Behrens), or subjective belief precision (Grahl, Yoshida). Suggested amendment: state that the epistemic/aleatoric attribution and the competence floor are engineering requirements, with biology supporting only "a harm prediction carries a separately represented, used precision". Do not cite biology for the attribution half.
2. Falsifier/design risk: Yoshida 2013 shows low reliability raising harm salience rather than lowering PE weight. The claim should specify what a low harm-predictor reliability does to the harm signal downstream (discount the PE for learning vs. keep caution for action); otherwise "weight by own precision" could suppress harm avoidance exactly when the predictor is weak.
3. Jepma 2018 shows biology does not self-correct a biased harm predictor (confirmation bias). That fits the claim's motivation (the competence floor is needed) but means human data cannot be used as a template for calibrated attribution.
4. Anatomical anchor: the precision evidence found is split between anterior insula (risk PE) and PAG/RVM (pain precision); nothing located a harm-predictor reliability signal in dACC, the consumer the claim names. Worth noting as a gap rather than an assumption.

## Could not verify
- Nothing unverified used. All five citations taken from PubMed metadata retrieved this session.
- validate_literature.py only scans inside a repo; validated by copying the dir plus the schema into a throwaway repo root in the scratchpad: 5 records, 0 findings.
