# SYNTHESIS -- ARC-068 opportunity_cost_no_op_penalty

**Pull date:** 2026-05-10. **Entries:** 6 papers (across theoretical RL derivation, unified phenomenology, dACC review, dACC-reinterpretation fMRI, DA-pharmacology dissociation, human patch-foraging behaviour).
**Anchor claim:** ARC-068 (architectural commitment that no-op / repeated-stationary trajectories pay an additive cost in E3 scoring proportional to a tonic average-reward-rate scalar; companion to ARC-066 / ARC-067 in the non_deficit_action_drives family).
**Source attribution:** the per-paper records cite PubMed and include DOI links; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull was commissioned

ARC-068 was registered on 2026-05-10 alongside ARC-066 and ARC-067 from a single user phenomenological observation ("I observe a drive in me to do something while I have energy rather than nothing / imagination"). Slot registration was sufficient to motivate the architectural commitment but not to fix child-MECH design. Per the project rule (`feedback_biology_before_formal_definitions`), formal-concept claims need a biology lit-pull before child-MECH design.

The cleanest disambiguation challenge for ARC-068 is the boundary against existing substrate. SD-032b dACC adaptive control already carries a `foraging_value` bundle component (the Kolling 2015 framing) that biases mode-switch when the current option falls below the environmental average. ARC-068's framing is the always-on cost-of-passivity at the trajectory-score level. Whether these are two architecturally separate computations on related substrates, or one biological computation that REE has registered twice under different names, is the load-bearing R1 question. The pull was commissioned to settle this and three secondary questions before child-MECH design begins.

---

## R1 -- ARC-068 vs SD-032b boundary

### Verdict: SEPARATE AT ARCHITECTURE, VIA KERNEL DISTINCTION (not substrate). Confidence 0.78.

The most parsimonious literature reading is that SD-032b and ARC-068 compute related-but-distinct opportunity-cost-like signals at DIFFERENT TIMESCALES on PARTLY OVERLAPPING substrate. The kernel distinction is what most cleanly separates them; the substrate distinction is partly a design choice rather than a strict biological commitment.

The case for clean separation rests on three pieces of evidence:

1. **Niv et al. 2007** ([DOI](https://doi.org/10.1007/s00213-006-0502-4), PMID 17031711) derives the long-run-average-reward-rate scalar as the substrate of opportunity cost on time, attributing it to tonic mesolimbic dopamine in nucleus accumbens. This is a slow, history-integrated scalar.
2. **Constantino & Daw 2015** ([DOI](https://doi.org/10.3758/s13415-015-0350-y), PMID 25917000) empirically tests the long-window historical kernel against TD-learning in a human patch-foraging task; the long-window kernel wins decisively. Subjects' opportunity-cost-driven decisions are governed by a slow EMA over reward history, not a fast TD update.
3. **Kolling, Behrens, Wittmann & Rushworth 2016** ([DOI](https://doi.org/10.1016/j.conb.2015.12.007), PMID 26774693) characterises the dACC `search value` signal as a CURRENT environmental average -- the value of alternatives currently available -- which biases switching when the current option falls below this current-context scalar. This is a faster, context-conditioned scalar, distinct from Niv's history-integrated one.

The kernels are different: Niv / Constantino-Daw operate over reward history (slow EMA, tens of episodes); Kolling operates over current environmental alternatives (fast, current-context). The architectural separation between ARC-068 (always-on, history-integrated, score-side) and SD-032b (task-conditioned, current-environmental, mode-switch-side) survives at this kernel-distinction level even if the substrate is partly shared.

The case AGAINST clean separation comes from two pieces:

1. **Shenhav, Straccia, Botvinick & Cohen 2016** ([DOI](https://doi.org/10.3758/s13415-016-0458-8), PMID 27580609) reinterprets the dACC `search value` signal as choice-difficulty tracking after methodological corrections. If Shenhav is right, SD-032b's dACC-as-foraging-substrate anchor is weakened. ARC-068 retains its Niv mesolimbic-DA anchor unaffected, but the architectural distinction can no longer rest on "different signals in dACC".
2. **Kolling 2016** itself argues for MULTIPLE coexisting signals in dACC -- commitment-to-action, search/exploration, model-updating, search-value. The multi-signal framing simultaneously LICENCES separation (different signals can coexist) and undermines clean separation (they share substrate). The architectural separation between ARC-068 and SD-032b is therefore partly a design choice.

The Shenhav vs Kolling dispute is unresolved in the literature; the synthesis cannot pretend otherwise. The recommendation is therefore robust to either side of the dispute prevailing:

**Implementation recommendation:** Implement ARC-068 as an additive E3 score-side cost on no-op / repeated-stationary trajectories proportional to a long-window EMA over realised E3-score-receipts (the Niv / Constantino-Daw kernel). Anchor the substrate primarily on tonic mesolimbic DA (Niv 2007), not on dACC. Keep SD-032b's existing dACC `foraging_value` bundle component on its current-environmental kernel (Kolling 2016). Do NOT collapse ARC-068 into SD-032b; the kernel distinction is the discriminator. Acknowledge in the child-MECH design doc that the architectural separation is at the algorithmic level (different timescales, different kernels) and may not correspond to a clean biological double-dissociation. The R1 verdict therefore is SEPARATE rather than ABSORB, with the reservation that biology likely runs both computations on overlapping cingulate / striatal substrate.

If the synthesis were forced to pick one side of the Kolling-Shenhav dispute and got it wrong, the architectural recommendation does not break: the kernel-form distinction (long-window vs current-context) holds either way, and the ARC-068 anchor on mesolimbic DA holds either way. The contested question (what dACC computes) only affects how strong SD-032b's dACC anchor is, not whether ARC-068 deserves its own slot.

---

## R2 -- reward-rate kernel: current vs historical?

### Verdict: PRIMARY long-window historical EMA. SECONDARY hybrid current+historical for non-stationary environments. Confidence 0.85.

The strongest empirical evidence in the cohort is **Constantino & Daw 2015** ([DOI](https://doi.org/10.3758/s13415-015-0350-y)), which directly tests this question. Two human patch-foraging experiments with parametric blockwise variation of opportunity cost. Model comparison: marginal-value-theorem threshold-learning (long-window EMA over previous rewards) versus temporal-difference learning (fast incremental update). The MVT threshold-learning rule wins decisively. Subjects adjust to blockwise opportunity-cost changes with a kernel consistent with a slow EMA over reward history, not a fast TD-style estimator.

This converges with Niv et al. 2007's theoretical derivation, which explicitly assumes the long-run average reward rate as the relevant scalar. The kernel form -- slow EMA, window covering tens of episodes / minutes of agent-time -- is what both papers identify.

The cohort also shows that a separate current-context scalar is real (Kolling 2016 search value) and likely operates on a faster timescale at a different substrate (dACC). The architectural arrangement is therefore plausibly TWO kernels in parallel: a slow history-integrated scalar feeding ARC-068's always-on score-side cost, and a fast current-environmental scalar feeding SD-032b's task-conditioned mode-switch.

**Primary recommendation for the ARC-068 child MECH:** a long-window EMA over realised E3-score-receipts. Window length should be configurable but default in the range covering tens of episodes / minutes of agent-time (matching Constantino & Daw's central-tendency estimate, scaled by REE's episode duration).

**Secondary fallback:** a hybrid current+historical estimator if the primary kernel produces poor adaptation in highly non-stationary environments (a regime Constantino & Daw did not test). Implementation: the long-window kernel as the dominant term, with a small current-context modulator to accelerate adaptation after sharp environmental shifts. This fallback should be a separate child-MECH (not silently bundled into ARC-068's primary mechanism), and its registration should be experimentally motivated rather than pre-emptive.

**Falsifiable prediction:** in a stable environment, the long-window-only ARC-068 should produce action-density that scales monotonically with reward history. After an abrupt environmental shift (drop in available reward), the long-window-only ARC-068 should adapt slowly -- on a timescale matching its EMA window -- whereas a hybrid kernel would adapt faster. Both are testable on SD-054 reef substrate or any non-stationary environment.

The R2 verdict has a knock-on effect on R1: the kernel distinction (long-window historical for ARC-068 vs current-environmental for SD-032b) is exactly what most cleanly separates the two claims architecturally. R1 is partially downstream of R2.

---

## R3 -- ARC-066 + ARC-068 collapse?

### Verdict: COLLAPSE AT IMPLEMENTATION LAYER LICENSED, but slot-level registration kept separate by design. Confidence 0.78.

Niv et al. 2007's derivation is symmetric. The same average-reward-rate scalar produces (a) a positive bias on action vigor / response rate (the ARC-066 territory), and equivalently (b) an additive cost on time-spent-passive (the ARC-068 territory). At the score-aggregation layer of E3, these are mathematically the same scalar viewed from opposite sign-on-different-candidates: adding +(rate * time_action) on action candidates is equivalent (up to a baseline shift in the score function) to subtracting (rate * time_passive) on passive candidates.

This licenses an implementation choice: a single signed scalar at the E3 score-aggregation layer can do both jobs. The slot-level registration of ARC-066 and ARC-068 as separate ARCs preserves the design space (the child MECH could in principle go either way) but the literature default is the unified-scalar implementation.

The case for keeping them separate even at implementation:

1. **Salamone & Correa 2003** ([DOI](https://doi.org/10.1016/s0166-4328(02)00282-6), PMID 12445713) shows that the activational scalar is dissociable from primary appetitive scoring. Whether the activational scalar itself can be further dissociated into vigor-on-action and cost-on-passivity components is not directly answered; Salamone's framework treats them as a single "willingness to expend effort against work cost" computation.
2. The phenomenology is asymmetric (cf. ARC-067 notes in claims.yaml: "restlessness when bored feels different from energised when surplus"). If subjective experience tracks substrate, ARC-066 and ARC-068 could be separate even though they're mathematically dual.

**Implementation recommendation:** for the v3 child-MECH design, implement ARC-066 + ARC-068 as a SINGLE signed capacity-keyed scalar at the score-aggregation layer. The scalar is positive on action candidates (ARC-066 contribution) and negative on no-op / repeated-stationary candidates (ARC-068 contribution). The slot-level separation is preserved as architectural-commitment registration so that future evidence (especially psychiatric failure-mode dissociations -- e.g. anhedonia preserves opportunity-cost felt-pressure but blunts vigor-on-action, suggesting they CAN dissociate) can revise the implementation without revising the architectural slot.

**Falsifiable prediction:** if ARC-066 and ARC-068 are implemented as separate scalars rather than a single signed scalar, the agent should be able to fail asymmetrically: a high-cost-on-passivity but low-vigor-on-action regime (something like depressive restlessness, a chronic urge to do something with no energy to act on it) versus a high-vigor-on-action but low-cost-on-passivity regime (something like manic activation without aversive pressure to fill rest). The unified-scalar implementation does NOT permit these dissociations. If REE later needs to model these psychiatric phenotypes, the unified-scalar implementation may need to be re-split. The slot registration permits that.

---

## R4 -- effort-cost vs opportunity-cost: same DA system or architecturally separate?

### Verdict: SEPARATE. Both ride on overlapping DA substrate but compute different cost terms. Confidence 0.82.

This is the question Salamone & Correa 2003 most directly answer. Their dissociation: low/moderate doses of DA antagonists and accumbens DA depletions suppress instrumental responding for food UNDER HIGH RATIO REQUIREMENTS while leaving primary appetite intact. DA-depleted animals reallocate AWAY from high-effort-high-reward TOWARD low-effort-low-reward options. The cost that DA depletion alters is the WORK / EFFORT cost -- a movement-energy / response-cost term that scales with action requirements.

Niv 2007's opportunity-cost-on-time scalar also rides on tonic mesolimbic DA, but it scales with elapsed time against avg reward history, NOT with action requirements. The two costs are simultaneously DA-mediated but compute on different task variables.

For REE, this licenses keeping ARC-068 architecturally separate from the existing effort-cost machinery (MECH-258 cingulate.precision_weighted_pain_PE, plus the SD-032b dacc_effort_cost bundle component, default 0.1, see SD-032b implementation_note in claims.yaml). The two cost terms appear as separate additive components in E3 score-aggregation:

```
score(trajectory) =
   ...
 - effort_cost(trajectory)            # MECH-258 / SD-032b: scales with action requirements
 - opportunity_cost(trajectory)       # ARC-068: scales with elapsed time * avg_reward_rate
   ...
```

**Implementation recommendation:** Do NOT collapse ARC-068 into the existing effort-cost machinery. Keep them as separate score-side components even though their upstream DA modulators may be coupled. The child-MECH design doc should make this separation explicit and cite the Salamone dissociation as the licence.

**Failure-signature test:** if REE collapses ARC-068 into effort-cost at the score-aggregation layer, the resulting agent will fail to dissociate Salamone-style under simulated DA reduction. A parametric reduction of the effort-cost scalar would suppress action under high-cost requirements (correct) AND suppress action under high-elapsed-time low-effort regimes (incorrect; Salamone's animals retain some of this kind of activation, the dissociation is precisely between the two).

**Kurzban et al. 2013** ([DOI](https://doi.org/10.1017/S0140525X12003196), PMID 24304775) provides the FELT-OUTPUT-LAYER unification of the two costs. Their unified opportunity-cost model treats subjective effort as the introspective readout of the cost-benefit computation -- and they argue for a UNIFIED felt output even when the substrate inputs differ. This is consistent with the R4 verdict: the costs are architecturally separate (different upstream computations, Salamone's dissociation), but the felt-effort output layer plausibly integrates them. For REE, this means the score-side ARC-068 cost can also feed a valence-side signal (z_harm_a affective channel, where ARC-067 boredom routes) that integrates with effort-cost outputs to produce a unified felt-cost signal -- without collapsing the separate cost computations at the score layer.

---

## What this pull does NOT settle

Items deferred to subsequent work:

1. **The Kolling-Shenhav dACC dispute itself.** R1's recommendation is robust to either side prevailing, but the specific question of what dACC actually computes (foraging value vs choice difficulty vs both) remains open in the literature. A future targeted_review_dacc_foraging_value pull (commissioned by SD-032b directly, not ARC-068) would benefit from the Kolling 2012 Science primary paper as a separate entry plus the Shenhav 2014 Nature Neuroscience paper as another.
2. **Whether ARC-066 + ARC-068 should be a single signed scalar or two separate scalars at child-MECH implementation time.** R3 recommends the unified scalar as default but flags psychiatric failure-mode dissociations (anhedonia, mania) as potential evidence for re-splitting. This is an empirical question for psychiatric_failure_modes.md cross-reference work.
3. **The exact EMA window length for ARC-068's kernel.** R2 recommends "tens of episodes / minutes of agent-time" but Constantino & Daw 2015's central-tendency estimate is task-specific. The window length should be a configurable parameter and explored empirically in REE rather than fixed from this pull.
4. **The hybrid current+historical kernel.** R2's secondary recommendation is a fallback if the primary kernel performs poorly in non-stationary environments. Whether to register a separate child-MECH for the hybrid kernel, or to leave it as a v4 future extension, depends on early validation experiments on the primary kernel.
5. **The valence-side routing of ARC-068 felt-output.** R4 notes that Kurzban's unified-felt-effort framework licences a routing through z_harm_a (the affective channel ARC-067 also uses) but the synthesis does not commit to it. This is an architectural detail for the child-MECH design doc.
6. **The MECH-216 / MECH-313 / MECH-260 cross-references** were declared orthogonal in the ARC-068 functional_restatement (predictive wanting only fires when a target is in scope; noise floor is uniform entropy; anti-recency is action-recency-not-no-op-specific). The lit-pull confirms the orthogonality at the literature level: none of these claims have substantive overlap with the Niv / Constantino-Daw / Salamone / Kolling cluster.

---

## Recommended next actions

1. **Update claims.yaml ARC-068 evidence_quality_note** with a paragraph summarising the four R verdicts and the lit-pull cohort. Cite this synthesis as the source.
2. **Author the ARC-068 child MECH design doc** as part of the child-MECH design phase. Use the unified-scalar (R3) + long-window-EMA (R2) + Niv-substrate-anchor (R1) + separate-from-effort-cost (R4) design as the primary recommendation. Cite this synthesis throughout.
3. **Defer registration of the secondary hybrid-kernel child MECH** until early ARC-068 validation experiments motivate it.
4. **Add a cross-reference note in SD-032b's evidence_quality_note** acknowledging the Shenhav 2016 reinterpretation as a constraint on how strongly SD-032b can lean on the dACC-as-foraging-substrate claim. SD-032b retains its current architecture but the synthesis flag should propagate.
5. **Cross-reference psychiatric_failure_modes.md** for the future ARC-066 + ARC-068 re-split question (R3). Anhedonia and mania are the canonical clinical phenotypes that would test the unified-scalar implementation.

---

## Per-paper summary index

| Entry | DOI | Verdicts informed | Direction | Confidence |
|---|---|---|---|---|
| Niv et al. 2007 | [10.1007/s00213-006-0502-4](https://doi.org/10.1007/s00213-006-0502-4) | R1, R2, R3, R4 | supports | 0.86 |
| Kurzban et al. 2013 | [10.1017/S0140525X12003196](https://doi.org/10.1017/S0140525X12003196) | R1, R4 | supports | 0.74 |
| Kolling et al. 2016 | [10.1016/j.conb.2015.12.007](https://doi.org/10.1016/j.conb.2015.12.007) | R1, R2 | mixed | 0.71 |
| Shenhav et al. 2016 | [10.3758/s13415-016-0458-8](https://doi.org/10.3758/s13415-016-0458-8) | R1 | weakens | 0.72 |
| Salamone & Correa 2003 | [10.1016/s0166-4328(02)00282-6](https://doi.org/10.1016/s0166-4328(02)00282-6) | R1, R4 | supports | 0.78 |
| Constantino & Daw 2015 | [10.3758/s13415-015-0350-y](https://doi.org/10.3758/s13415-015-0350-y) | R2 | supports | 0.82 |

**Aggregate ARC-068 lit_conf** (post-indexer): expected to land in the 0.78-0.82 range, supports-direction-dominant (4 supports + 1 mixed + 1 weakens), 6-entry cohort. Substrate (Niv mesolimbic DA), form (additive opportunity cost on time-consumed), kernel (long-window historical EMA), and architectural-separation-from-effort-cost are all anchored.

According to PubMed, all PubMed-sourced entries in this synthesis are sourced under the cited PMIDs with DOIs as listed above.
