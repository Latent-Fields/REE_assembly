# SYNTHESIS -- MECH-269b: V_s gating extends to E1/E2 cortical rollouts

## Scope

This targeted review grounds candidate claim MECH-269b: that the MECH-269 V_s (regional verisimilitude) signal -- per-stream prediction/realization alignment -- gates not only hippocampal proposer anchor selection (the original MECH-269 scope) but also which streams ground forward predictions in cortical world models (E1 sensory predictor, E2 transition model). The architectural prediction is that without V_s gating on E1/E2 rollouts, downstream consumers (e.g. dACC adaptive control / SD-032b) receive stale-but-confident-looking prediction errors, which suppresses behavioural revision and produces wired-but-inert failure modes.

## Entry count and breakdown by support type

Total entries: 7

Per the user-stated tagging principle, entries are tagged by support type:
- (a) direct support for cortex-side per-stream precision/reliability gating of forward predictions
- (b) support for the symmetric application across hippocampal vs cortical world models
- (c) inferential support from precision-weighting predictive-coding generally
- (d) measurement gap (paper does not address the question; tag is descriptive of where biology is silent)

Breakdown:

| Entry | Year | Tag(s) | Conf | Direction |
|---|---|---|---|---|
| Bastos et al. -- Canonical microcircuits for predictive coding | 2012 | a, c | 0.72 | supports |
| Feldman & Friston -- Attention, uncertainty, and free-energy | 2010 | a, c, d | 0.70 | supports |
| Kanai, Komura, Shipp & Friston -- Cerebral hierarchies / pulvinar | 2015 | a, c, d | 0.78 | supports |
| Adams et al. -- The computational anatomy of psychosis | 2013 | c, d | 0.66 | supports (failure-mode) |
| Lawson, Rees & Friston -- Aberrant precision account of autism | 2014 | c, d | 0.64 | supports (failure-mode) |
| Ernst & Banks -- Visual-haptic statistically optimal integration | 2002 | c, d | 0.74 | supports |
| Daw, Niv & Dayan -- Uncertainty-based competition PFC vs DLS | 2005 | b, c | 0.58 | mixed |

Tag totals across entries (entries can carry multiple tags):
- (a) cortex-side per-stream precision: 3 entries (Bastos 2012, Feldman & Friston 2010, Kanai 2015)
- (b) symmetric hippocampal+cortical application: 1 entry (Daw, Niv & Dayan 2005), and that 1 is structural-precedent-only rather than direct evidence
- (c) inferential precision-weighting / predictive coding: 7 entries (all)
- (d) measurement gap: 6 entries (every entry except Bastos 2012 explicitly carries a measurement gap; Bastos carries one implicitly via the column-vs-stream caveat)

## Strongest support

Kanai, Komura, Shipp & Friston (2015), confidence 0.78. Pulvinar-cortex precision gating is the most directly mapped substrate proposal in the anchor list -- a dedicated thalamic structure computes per-cortical-region precision and broadcasts it to consumers, which mirrors REE design where V_s is computed in a separate verisimilitude-tracking module. The two-stream architecture (driving content vs modulatory precision) maps directly onto MECH-269b separation of stream content from stream gain.

Bastos et al. (2012) and Feldman & Friston (2010) anchor the predictive-coding column-level primitive: cortical microcircuits are biologically equipped to gate prediction-error contribution by a precision parameter (post-synaptic gain modulated by NMDA, neuromodulators, recurrent inhibition).

Ernst & Banks (2002) supplies the canonical empirical demonstration that the human nervous system performs reliability-weighted (per-stream) integration -- the cleanest psychophysical foundation for the per-stream V_s primitive.

Adams et al. (2013) and Lawson, Rees & Friston (2014) supply the failure-mode predictions that match MECH-269b wired-but-inert warning: when precision is mis-set, behavioural revision fails in characteristic ways. These are the strongest indirect-evidence entries, corroborating the architectural claim by showing the predicted clinical signature.

## Weakest gaps

The principal gap is tag (b) -- direct biological evidence for symmetric application of the same V_s/precision signal across hippocampal proposer anchor selection AND cortical forward-prediction gating. Daw, Niv & Dayan 2005 is the only paper in the anchor list that even structurally engages this question, and the analogy (cross-system action arbitration vs within-loop per-stream weighting) is structural rather than direct. No paper in this set demonstrates that the same precision parameter is computed and consumed in both hippocampal and cortical modules in the way MECH-269b proposes.

A secondary gap is per-stream (vs per-region) precision granularity within cortex. Pulvinar-cortex gating in Kanai et al. is per-region; Lawson et al. gestures at per-modality differences in autism; Ernst & Banks is per-modality. None demonstrates per-latent-stream precision at the resolution MECH-269b assumes (z_world, z_self, z_harm_s, z_harm_a, z_goal as independently gated streams).

A third gap is empirical-vs-theoretical. The strongest substrate proposals (Kanai 2015, Bastos 2012, Feldman & Friston 2010) are theoretical / synthesis papers; the strongest empirical papers (Ernst & Banks 2002, Adams 2013, Lawson 2014) are one mathematical step away from MECH-269b setting (cue integration, clinical psychopathology) rather than direct measurement of forward-prediction-error gating.

## Verdict

Sparse-but-not-falsifying. The cortical-side primitive (precision-weighted PE gating in cortex) is well-supported by the predictive-coding programme. The per-stream specialisation has empirical foundation in cue integration but no direct demonstration in the forward-prediction-rollout setting MECH-269b asks about. The symmetric hippocampal+cortical application is genuinely novel architectural ground -- the closest available precedent (Daw 2005) is structural rather than direct, and no paper in the anchor list demonstrates the symmetric-V_s claim biologically.

Per the user-stated principle: low evidence count for the symmetric-application claim does NOT mean the mechanism is wrong. The predictive-coding framework supplies the architectural primitive; biology has not been measured at the resolution MECH-269b proposes. The verdict is therefore: register MECH-269b as candidate with explicit evidence_quality_note flagging the symmetric-application novelty as the principal gap. Falsifying evidence would be a study showing precision-weighting in cortex AND a separate non-precision arbitration mechanism in hippocampus -- this would refute the symmetric claim. No such study appeared in the anchor searches.

## Recommended evidence_quality_note language

Recommended evidence_quality_note text for MECH-269b in claims.yaml:

> Literature support is asymmetric across the claim two architectural halves. Cortex-side per-stream precision/reliability gating of prediction errors has strong inferential support from the predictive-coding programme: cortical microcircuits implement precision-weighted PE (Bastos et al. 2012, Neuron, doi:10.1016/j.neuron.2012.10.038), attention is precision (Feldman & Friston 2010, Front Hum Neurosci, doi:10.3389/fnhum.2010.00215), pulvinar-cortex modulatory gain is the most direct biological substrate proposal (Kanai et al. 2015, Phil Trans R Soc B, doi:10.1098/rstb.2014.0169), and aberrant precision produces the wired-but-inert clinical phenotype the claim warns about (Adams et al. 2013, doi:10.3389/fpsyt.2013.00047; Lawson et al. 2014, doi:10.3389/fnhum.2014.00302). The empirical foundation for per-stream reliability-weighted integration is psychophysically demonstrated for cue integration (Ernst & Banks 2002, Nature, doi:10.1038/415429a). However, the symmetric-application half of the claim -- that the SAME V_s signal gates BOTH hippocampal proposer anchor selection AND cortical E1/E2 forward predictions -- is genuinely novel architectural ground. The closest available precedent is Daw, Niv & Dayan 2005 (Nat Neurosci, doi:10.1038/nn1560), which arbitrates between two distinct world-model systems by uncertainty, but is structural rather than direct. No paper in the targeted review demonstrates symmetric hippocampal+cortical precision-gating at the resolution MECH-269b assumes. Sparse direct support for symmetric-application does NOT falsify the mechanism; biology may not have been measured at this resolution. Substrate validation must therefore distinguish behavioural signatures predicted by symmetric-V_s gating (cortex-side wired-but-inert failure mode without V_s on E1/E2 rollouts; downstream consumers receive stale-but-confident-looking PE) from cortex-only-gating null hypotheses.

## Confidence verdict

Aggregate confidence across entries: mean ~0.69, weighted toward the cortex-side primitive (a/c tags). Symmetric-application confidence (b tag) is materially lower at ~0.58 (Daw 2005 alone). The cortex-side architectural primitive is well-grounded; the symmetric-application novelty carries the principal evidential burden and should be tested experimentally rather than declared from biology.
