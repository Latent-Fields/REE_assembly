# Targeted Review -- ARC-068 opportunity_cost_no_op_penalty

**Pull date:** 2026-05-10. **Entries:** 6.
**Anchor claim:** ARC-068 (architectural commitment that no-op / repeated-stationary trajectories pay an additive cost in E3 scoring proportional to a tonic average-reward-rate scalar).

## Per-entry summary

| Entry | Authors | Year | Venue | DOI | Direction | Confidence | Verdicts informed |
|---|---|---|---|---|---|---|---|
| 2026-05-10_arc_068_tonic_dopamine_opportunity_cost_niv_2007 | Niv, Daw, Joel, Dayan | 2007 | Psychopharmacology (Berl) | [10.1007/s00213-006-0502-4](https://doi.org/10.1007/s00213-006-0502-4) | supports | 0.86 | R1, R2, R3, R4 |
| 2026-05-10_arc_068_subjective_effort_opportunity_cost_kurzban_2013 | Kurzban, Duckworth, Kable, Myers | 2013 | Behav Brain Sci | [10.1017/S0140525X12003196](https://doi.org/10.1017/S0140525X12003196) | supports | 0.74 | R1, R4 |
| 2026-05-10_arc_068_acc_search_value_kolling_2016 | Kolling, Behrens, Wittmann, Rushworth | 2016 | Curr Opin Neurobiol | [10.1016/j.conb.2015.12.007](https://doi.org/10.1016/j.conb.2015.12.007) | mixed | 0.71 | R1, R2 |
| 2026-05-10_arc_068_dacc_choice_difficulty_shenhav_2016 | Shenhav, Straccia, Botvinick, Cohen | 2016 | Cogn Affect Behav Neurosci | [10.3758/s13415-016-0458-8](https://doi.org/10.3758/s13415-016-0458-8) | weakens | 0.72 | R1 |
| 2026-05-10_arc_068_da_depletion_effort_salamone_correa_2003 | Salamone, Correa | 2003 | Behav Brain Res | [10.1016/s0166-4328(02)00282-6](https://doi.org/10.1016/s0166-4328(02)00282-6) | supports | 0.78 | R1, R4 |
| 2026-05-10_arc_068_patch_foraging_learning_constantino_daw_2015 | Constantino, Daw | 2015 | Cogn Affect Behav Neurosci | [10.3758/s13415-015-0350-y](https://doi.org/10.3758/s13415-015-0350-y) | supports | 0.82 | R2 |

## Verdict cohort summary

- **R1 (ARC-068 vs SD-032b boundary):** SEPARATE-AT-ARCHITECTURE-VIA-KERNEL. Confidence 0.78. Anchored on Niv 2007 + Constantino & Daw 2015 (long-window historical kernel) vs Kolling 2016 (current-environmental kernel). Contested by Shenhav 2016 (which weakens the dACC-foraging-value substrate claim that SD-032b leans on). Recommendation: keep ARC-068 architecturally separate from SD-032b, anchored on different timescales / kernels rather than on different substrates.
- **R2 (reward-rate kernel):** PRIMARY long-window historical EMA. Confidence 0.85. Anchored on Constantino & Daw 2015 empirical decisiveness. SECONDARY fallback hybrid current+historical for non-stationary environments.
- **R3 (ARC-066 + ARC-068 collapse):** YES-AT-IMPLEMENTATION-LAYER. Confidence 0.78. Anchored on Niv 2007 mathematical symmetry. Slot-level registration kept them separate; child-MECH design should prefer single signed scalar at score-aggregation.
- **R4 (effort-cost vs opportunity-cost separation):** SEPARATE. Confidence 0.82. Anchored on Salamone & Correa 2003 dissociation. ARC-068 is architecturally distinct from existing MECH-258 effort-cost machinery; both ride on DA system but compute different things.

## Aggregate ARC-068 lit_conf (estimate)

Pre-indexer estimate: lit_conf in the **0.78-0.82** range, supports-direction-dominant (4 supports + 1 mixed + 1 weakens), 6-entry cohort. The cohort spans theoretical derivation (Niv), unified phenomenology (Kurzban), mechanistic review (Kolling), empirical reinterpretation (Shenhav), pharmacological dissociation (Salamone-Correa), and behavioural model comparison (Constantino-Daw). Substrate, form, and kernel are all anchored.

Final lit_conf will be set by the indexer (`evidence/experiments/scripts/build_experiment_indexes.py`) and recorded in `claim_evidence.v1.json` under ARC-068.

## See also

- `synthesis.md` -- full R1-R4 verdicts with reasoning
- ARC-066 lit-pull (`targeted_review_arc_066_tonic_vigor/`) -- companion family slot, includes Niv 2007 with a different mapping
- SD-032b in `claims.yaml` -- existing dACC adaptive-control substrate; ARC-068 architectural boundary verdicts apply
- `docs/architecture/non_deficit_action_drives.md` -- family doc
