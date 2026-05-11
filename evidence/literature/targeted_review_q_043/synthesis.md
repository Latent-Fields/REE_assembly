# Q-043 Lit-Pull Synthesis — MECH-313 / MECH-314 calibration

**Claim under review.** Q-043: How should the relative weights of MECH-313 (stochastic noise floor, LC-NE tonic analog) and MECH-314 (structured curiosity bonus, frontopolar uncertainty-driven curiosity) be calibrated for V3 substrates? Falsifiable with parametric sweep on SD-054 reef substrate plus ARC-062 gated-policy.

**Anchor set.** Six papers, dated 2006–2019: Daw et al. 2006 (foundational fMRI); Wilson et al. 2014 (behavioural Horizon task); Zajkowski et al. 2017 (right-frontopolar TMS); Warren et al. 2017 (atomoxetine pharmacology); Gershman 2018 (hybrid algorithmic model); Schulz & Gershman 2019 (review).

**Aggregate.** Five supports + one mixed. Indexer-derived lit_conf will be in the 0.78–0.82 range. Evidence quadrant expected: `plausible_unproven` (high lit, low exp — there are no V3 experiments addressing this calibration question yet).

---

## R1 — Do MECH-313 and MECH-314 correspond to separate underlying mechanisms in the substrate REE is modelling?

**Verdict.** **CONFIRMED.** Two-mechanism architecture supported by partial double dissociation in the human literature: rTMS over right frontopolar cortex selectively impairs directed (uncertainty-driven) exploration without affecting random exploration (Zajkowski 2017); atomoxetine selectively affects random exploration without affecting directed (Warren 2017). Behavioural dissociation (independent tunability with task horizon) is established by Wilson 2014. The fMRI dissociation between frontopolar-cortex exploration loci and striatal/vmPFC exploitation loci is established by Daw 2006. The synthesis review (Schulz & Gershman 2019) endorses the dual-system architecture as the consensus view of the field.

**Implication for REE.** The architectural commitment to MECH-313 and MECH-314 as separate substrates with independent ablation flags is well-grounded. Q-043's calibration question is well-posed: the relative weighting of the two mechanisms is a genuine architectural parameter, not a redundant scaling factor.

## R2 — What does the literature say about the optimal CALIBRATION (relative weighting)?

**Verdict.** **HYBRID-NON-ZERO REQUIRED; DIRECTION NOT MONOTONE.** Gershman 2018 is the most direct evidence: a hybrid uncertainty-bonus + sampling model fits human behaviour better than either single-mechanism alternative. Neither extreme (w_313=0 nor w_314=0) is consistent with the human data. The PASS-as-question-resolution outcome that Q-043 hypothesises — a Pareto frontier with non-zero contribution from both mechanisms — is the prior prediction the human literature licenses.

The directional caveat is Warren 2017: atomoxetine REDUCES random exploration rather than increasing it, contrary to a naive monotone reading of the adaptive-gain (Aston-Jones & Cohen 2005) theory. This means the relationship between MECH-313 weight and behavioural diversity is unlikely to be monotone. REE should not assume that higher w_313 = more diversity at all weight ranges; the V3 sweep should be prepared for a non-monotone (potentially inverted-U) Pareto frontier.

**Implication for the V3 sweep design.** The parametric grid should cover both very low and very high MECH-313 weights, not just an interval centred on a putative "linear" optimum. The expected Pareto-optimal regime is interior (not at any boundary) and may show non-monotone behaviour in either or both axes.

## R3 — How well does the human literature TRANSFER to the SD-054 reef substrate?

**Verdict.** **PARTIAL.** All six anchors use simple bandit tasks (two- to four-armed, mostly two-armed) with stationary or slowly-drifting reward distributions. SD-054 reef is structurally different: rule-discriminative rather than payoff-discriminative, dynamic hazard schedule, no fixed "arms". The algorithmic-class match (uncertainty-bonus mechanism vs randomisation mechanism) transfers; the implementation-level details (where uncertainty is computed, how randomness enters the action-selection layer) may not. The bias-vs-slope diagnostic from Gershman 2018 may not have the same signature in REE's policy-class output.

**Implication for REE.** The lit-pull supports the EXISTENCE premise of Q-043 strongly but supports a SPECIFIC numerical calibration only weakly. The V3 sweep should not pre-anchor on any particular (w_313, w_314) ratio derived from human experiments; the optimum is substrate-specific.

The most useful methodological transfer is the bias-vs-slope diagnostic (Gershman 2018). If V3-EXQ-543b/c-successor produces a MECH-313-OFF arm that shows a BIAS-shift signature (rather than a slope-shift), that would indicate MECH-314 is compensating in the wrong direction — useful failure-mode signal that the parametric sweep should be designed to detect.

---

## Substrate-readiness note

Q-043 cannot run until ARC-062's GAP-B substrate-readiness issue is closed (CEM-candidate-distinguishability, see arc_062_rule_apprehension_plan.md 2026-05-11 decision log). The Q-043 sweep is downstream of the same gated-policy substrate that V3-EXQ-543b exposed as inert. The order of operations is: (a) close ARC-062 substrate-readiness; (b) MECH-313 / MECH-314 substrate-readiness diagnostics (V3-EXQ-544, V3-EXQ-545 — already PASSed 2026-05-10); (c) Q-043 parametric sweep with ARC-062 enabled on SD-054.

## Recommended next actions

1. Update Q-043 `evidence_quality_note` in claims.yaml to cite this synthesis and capture R1–R3 verdicts.
2. Reflect the R2 non-monotone-direction prediction in the Q-043 sweep design when /queue-experiment is invoked for the parametric sweep — the grid should span at least one decade in each weight and include both very low and very high values.
3. Adopt the Gershman 2018 bias-vs-slope diagnostic as a methodological tool for interpreting MECH-313-OFF / MECH-314-OFF ablation arms.

---

*Authored 2026-05-11, automated lit-pull skill run. Six papers extracted; one mixed-direction entry (Warren 2017) preserves the directional caveat for the calibration verdict.*
