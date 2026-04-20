# Targeted review: ARC-058 (shared forward-model trunk for aversive prediction)

**Claim:** ARC-058 -- a single HarmForwardTrunk substrate encodes a modality-independent unsigned aversive-PE signal shared across z_harm_s and z_harm_a; stream-specific HarmForwardHeads produce signed per-stream predictions. COMPETES WITH ARC-033 (independent per-stream forward models).

**Pulled:** 2026-04-20. 4 entries in this directory; 1 cross-referenced from `targeted_review_pain_predictive_coding_substrate` (Horing & Buchel 2022 -- the foundational paper ARC-058 was registered on).

**Aggregate direction:** mixed-supporting for the weak reading of ARC-058 (shared unsigned trunk + stream-specific signed heads, as the spec actually says); weakens the strong reading (trunk dominates per-stream variance). Independent-per-stream ARC-033 is narrowed but not killed.

## Entries in this directory

| Entry | Paper | Year | Direction | Confidence | Key contribution |
|---|---|---|---|---|---|
| `2026-04-20_arc_058_nps_somatic_pain_signature_wager2013` | Wager et al, NPS | 2013 | weakens | 0.78 | Somatic pain has a reproducible distributed signature 85% separable from social pain -- weakens strong shared-trunk. |
| `2026-04-20_arc_058_siips1_cerebral_beyond_nociception_woo2017` | Woo et al, SIIPS1 | 2017 | supports | 0.80 | Partitioned cerebral pain signature exists beyond nociception, with partial AIC overlap -- the biological signature ARC-058 predicts. |
| `2026-04-20_arc_058_somatic_vicarious_dissociation_krishnan2016` | Krishnan et al | 2016 | mixed | 0.72 | NPS generalises across thermal/mechanical/electrical (supports trunk WITHIN z_harm_s); somatic/vicarious fully dissociable (calibration for larger modality gaps). |
| `2026-04-20_arc_058_sensory_affective_double_dissociation_hofbauer2001` | Hofbauer / Rainville | 2001 | weakens | 0.70 | Hypnotic double dissociation of intensity vs unpleasantness -- kills strong ARC-058, leaves weak ARC-058 and ARC-033 both standing. |

## Cross-references

- **Horing & Buchel 2022** (PLoS Biology, DOI 10.1371/journal.pbio.3001540). Entry lives in `targeted_review_pain_predictive_coding_substrate/entries/2026-04-19_pain_pc_signed_unsigned_pe_horing2022/`. This is THE foundational paper ARC-058 was registered on: direct evidence that anterior insula codes an unsigned modality-general aversive PE while dorsal posterior insula codes signed modality-specific PE. It is already tagged to MECH-258 and SD-032b; the governance layer may want to add ARC-058 to its `claim_ids_tested` in a later sweep, or keep this synthesis as the cross-reference.

## Integration

The five papers together describe a two-layer architecture:

1. **Upstream unsigned layer.** Anterior insula codes a modality-general unsigned aversive PE (Horing 2022 direct; Woo 2017 NPS/SIIPS1 partial AIC overlap is consistent). This layer is what ARC-058's HarmForwardTrunk corresponds to.
2. **Downstream signed layer.** Dorsal posterior insula carries signed pain-specific PE (Horing 2022); partitioned NPS and SIIPS1 signatures carry sensory-discriminative vs affective-contextual pain variance (Wager 2013, Woo 2017); hypnotic top-down modulation can pry apart intensity (S1) and unpleasantness (ACC) readouts (Hofbauer 2001 + Rainville 1997). This layer is what ARC-058's HarmForwardHead corresponds to.
3. **Within-stream sub-modality generalisation.** The somatic-pain signature generalises across thermal, mechanical, and electrical pain (Krishnan 2016). This supports a shared trunk WITHIN the z_harm_s stream and is the cleanest direct evidence for shared substrate in the literature.

## Arbitration verdict (literature only)

The biology favours the SPECIFIED form of ARC-058 (weak shared-trunk + partitioned signed heads) over both (i) a strong shared-trunk reading (falsified by Wager 2013 separability, Hofbauer 2001 double dissociation) and (ii) a pure ARC-033 reading with no shared substrate (weakened by Horing 2022's shared AIC unsigned PE and Krishnan 2016's within-somatic generalisation).

However, ARC-058 as actually specified and ARC-033 as actually specified produce overlapping predictions for most of these measures -- the literature cannot fully arbitrate without direct computational-model fitting of the kind V3-EXQ-445 attempts. The EXQ-445 C4 metric finding (mean_r2 = 0.899, indistinguishable) is consistent with the literature: at the per-stream forward_r2 level, the two architectures should produce very similar accuracy, and they do. The informative test will be on per-stream parameter efficiency and on downstream consumer usability (dACC bundle, MECH-258 precision-weighted PE).

## Recommended next steps for governance

1. ARC-058 should not be demoted or retired on V3-EXQ-445 alone -- the literature supports the weak reading, and the C4 indistinguishability is expected, not diagnostic.
2. The arbitration experiment needs a metric beyond per-stream forward_r2. Candidates: parameter count at matched performance; downstream usability of the unsigned-trunk signal for the SD-032b dACC bundle; mediation analysis of chronic-exposure sensitisation (Baliki 2010/2012 signature).
3. Add ARC-058 to the claim_ids_tested of the existing Horing 2022 entry in the pain_predictive_coding directory at the next governance sweep.

## Aggregate confidence

Mean confidence across the 4 entries in this directory: 0.75. Cross-referenced Horing 2022 (from the pain_predictive_coding directory) is 0.88. Combined aggregate, 0.78. The claim is well-grounded for a V3-pending candidate.
