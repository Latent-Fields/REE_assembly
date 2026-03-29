# Summary: Semyanov 2019 -- Multi-Timescale Architecture of Astrocyte Ca Signaling

**Entry ID:** 2026-03-29_q004_svr_threshold_slow_ca_semyanov2019
**Claim:** Q-004 -- How to calibrate tau_R relative to E1/E2?
**Source:** Semyanov A. *Cell Calcium* 78:15-25 (2019). DOI: 10.1016/j.ceca.2018.12.007

## What the paper did

This review of astrocytic Ca dynamics (also cited for Q-003) is equally useful for Q-004 because it articulates a structural model of why Ca signaling in astrocytes naturally operates at multiple timescales. Semyanov draws a distinction between two morphological compartments -- organelle-free leaflets contacting individual synapses, and organelle-containing branchlets that integrate signals from multiple leaflets -- and shows that these compartments have different signal integration properties determined by their surface-to-volume ratios (SVR). Fast events at leaflets are then either absorbed or amplified and propagated at the branchlet level, with a morphologically determined threshold.

## Key findings for Q-004

The multi-timescale picture that emerges is: (1) individual synaptic Ca events at leaflets are fast (sub-second to seconds) and spatially confined; (2) branchlet-level Ca integration operates over a longer window determined by SVR-dependent threshold dynamics; (3) inter-astrocyte propagation via gap junctions and extracellular ATP extends this to minutes and involves slow diffusive spread. The result is that a single astrocytic domain integrates over a temporal hierarchy that spans at least two orders of magnitude -- from sub-second leaflet events to minute-scale network propagation. The SVR of branchlets is proposed as the morphological parameter that determines whether a given level of synaptic input is sufficient to engage the slow, spreading component.

## Translation to REE

Q-004 asks how tau_R should be calibrated relative to E1 (prediction_horizon=20) and E2 (rollout_horizon=30). Semyanov's framework implies tau_R should not be a single number but should be parameterized with at least two timescale constants. The fast component (tau_R_fast) should be calibrated to be comparable to or slightly longer than E1's prediction horizon -- capturing within-episode regulatory history. The slow component (tau_R_slow) should be much longer -- capturing cross-episode, multi-trial regulatory history at the network propagation scale. In REE's context, the fast component governs how quickly R responds to within-episode harm/goal signals; the slow component governs how long harm history from previous episodes persists to influence current precision weighting.

## Limitations

The numerical timescales inferred from this review are approximate. The review synthesizes data from multiple experimental preparations (slice, in vitro, some in vivo) with varying stimulation conditions, making precise quantitative claims unreliable. The SVR threshold concept is theoretically motivated but not directly measured; the review cites indirect evidence from morphological studies rather than time-course measurements under controlled SVR manipulation. Human astrocyte SVR and leaflet/branchlet architecture may differ from rodent.

## Confidence reasoning

The multi-timescale framework is broadly accepted in the astrocyte Ca field and is consistent with the Cahill et al. 2024 empirical findings. However, as a review that infers timescales from a synthesis rather than measuring them directly, the quantitative guidance for tau_R calibration is approximate. Confidence is 0.65: useful conceptual architecture for Q-004, with the numerical calibration requiring supplementation from empirical measurement studies.
