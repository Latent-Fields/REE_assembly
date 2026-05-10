# INDEX -- targeted_review_arc_070_decomposition

**Claim:** ARC-070 policy.decomposition_on_prediction_failure (zoom in / re-segment imagined chains when chunks fail to ground)
**Family:** policy_primitive_granularity (parent ARC-069, sibling ARC-071)
**Family doc:** [docs/architecture/policy_primitive_granularity.md](../../../docs/architecture/policy_primitive_granularity.md)
**Pulled:** 2026-05-10
**Entries:** 7
**Synthesis:** [synthesis.md](synthesis.md)

## Verdicts (R1-R5)

| Verdict | Question | Decision | Confidence |
|---|---|---|---|
| R1 | Trigger primary | V_s drop on chunk's region (PE-driven, biologically anchored). E2-disagreement / completion-failure / mid-execution PE = convergent secondary signals. | 0.78 |
| R2 (LOAD-BEARING) | MECH-288 bidirectional or new module? | SHARED SUBSTRATE: ARC-070 implemented as bidirectional extension of MECH-288 event_segmenter, accepting both observation and imagination input streams. NO new module required. | 0.74 |
| R3 | Hierarchy depth | MULTI-LEVEL hierarchy supported. Recursive decomposition (chunk -> sub-chunk -> primitive) with implementation depth bounded at 3-4 levels. | 0.78 |
| R4 | Mid-execution decomposition vs pre-commitment-only? | BOTH supported. Same V_s-trigger mechanism handles both phases; downstream effects gated by MECH-094 hypothesis_tag. | 0.66 |
| R5 | Bottleneck-state vs error-driven decomposition: same mechanism or distinct? | DISTINCT mechanisms with overlapping outputs. PE-driven primary; bottleneck-aware secondary as optional consolidation-phase signal. | 0.74 |

## Entries

| # | Entry | DOI / Source | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|---|
| 1 | [Zacks et al. 2007](entries/2026-05-10_arc_070_event_segmentation_zacks_2007/) | [10.1037/0033-2909.133.2.273](https://doi.org/10.1037/0033-2909.133.2.273) | R1 primary, R2 theoretical, R3 corroborating, R5 primary | supports | 0.84 |
| 2 | [Schacter, Addis & Buckner 2008](entries/2026-05-10_arc_070_episodic_simulation_schacter_2008/) | [10.1196/annals.1440.001](https://doi.org/10.1196/annals.1440.001) | R2 LOAD-BEARING empirical | supports | 0.82 |
| 3 | [Badre & D'Esposito 2009](entries/2026-05-10_arc_070_rostro_caudal_hierarchy_badre_desposito_2009/) | [10.1038/nrn2667](https://doi.org/10.1038/nrn2667) | R3 empirical anchor | supports | 0.78 |
| 4 | [Pfeiffer & Foster 2013](entries/2026-05-10_arc_070_hippocampal_forward_sweeps_pfeiffer_foster_2013/) | [10.1038/nature12112](https://doi.org/10.1038/nature12112) | R1 substrate, R3, R4 substrate | supports | 0.78 |
| 5 | [Koechlin & Summerfield 2007](entries/2026-05-10_arc_070_cascaded_control_koechlin_summerfield_2007/) | [10.1016/j.tics.2007.04.005](https://doi.org/10.1016/j.tics.2007.04.005) | R3 theoretical, R5 hybrid | supports | 0.74 |
| 6 | [Schapiro et al. 2017](entries/2026-05-10_arc_070_cls_hippocampus_schapiro_2017/) | [10.1098/rstb.2016.0049](https://doi.org/10.1098/rstb.2016.0049) | R1 substrate, R2 pathway grounding, R3 multi-grain | supports | 0.74 |
| 7 | [McGovern & Barto 2001](entries/2026-05-10_arc_070_diverse_density_subgoals_mcgovern_barto_2001/) | [10.5555/645530.655681](https://doi.org/10.5555/645530.655681) | R5 foil (distinct mechanism) | mixed | 0.62 |

**Aggregate lit_conf:** computed by indexer; expected 0.74-0.78 range. Mean of per-entry confidence = (0.84 + 0.82 + 0.78 + 0.78 + 0.74 + 0.74 + 0.62) / 7 = 0.760. Direction: 6 supports + 1 mixed.

## Substrate disambiguation

ARC-070's lit-pull addressed four substrate-disambiguation requirements specified in the briefing:

- **MECH-269 V_s primitive:** R1 verdict confirms V_s drop on the chunk's region as the primary trigger. Biological anchor: Schapiro 2017 pattern-separation as candidate substrate for V_s; Zacks 2007 PE-as-trigger framework licenses V_s as the right signal class.
- **MECH-269b symmetric V_s gating:** ARC-070 will be the second major V_s consumer. The two readers can have independent thresholds; V_s primitive substrate is shared.
- **MECH-288 event_segmenter (observation side):** R2 verdict (LOAD-BEARING) recommends ARC-070 as bidirectional extension of MECH-288, NOT a new module. Schacter 2008 + Zacks 2007 + hippocampal substrate convergence (Pfeiffer-Foster 2013, Schapiro 2017) all support shared substrate.
- **MECH-094 hypothesis_tag:** R4 mid-execution decomposition needs hypothesis_tag-aware downstream effects; the same mechanism fires pre-commitment (no residue write) and post-commitment (residue write enabled).

## Key recommendations for child-MECH design

1. PRIMARY trigger: V_s drop on chunk's region (MECH-269 substrate read-out).
2. BIDIRECTIONAL extension of MECH-288 event_segmenter (shared substrate with observation-side segmenter).
3. RECURSIVE decomposition with depth cap at 3-4 levels.
4. Both pre-commitment AND mid-execution decomposition supported via the same mechanism with hypothesis_tag-conditional downstream effects.
5. PE-driven primary, bottleneck-state-aware secondary as optional consolidation-phase signal.
6. Cross-link with MECH-269b at integration time; share V_s primitive but allow independent thresholds.

See [synthesis.md](synthesis.md) for full verdict reasoning and falsifiable predictions.
