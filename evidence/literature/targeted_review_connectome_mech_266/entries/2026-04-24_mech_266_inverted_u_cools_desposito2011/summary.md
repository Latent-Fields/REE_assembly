# Cools & D'Esposito 2011 -- Inverted-U dopamine and stability-flexibility tradeoff

## Source
Cools R, D'Esposito M. Inverted-U-shaped dopamine actions on human working memory and cognitive control. Biological Psychiatry 69(12):e113-e125. DOI: 10.1016/j.biopsych.2011.03.028

## Finding
Dopamine effects on cognitive control follow an inverted-U: both too-little and too-much DA impair working memory and task-set control, and the optimum depends on baseline, individual differences, and region. The stability-flexibility tradeoff is dissociable across regions: PFC DA primarily supports stability (maintaining current task set against distraction); striatal DA primarily supports flexibility (switching task set). Manipulating DA (L-DOPA, methylphenidate) has paradoxical consequences because it moves different regions and different individuals in different directions relative to their optima.

## Why it maps to MECH-266
MECH-266 posits that entering vs exiting an operating mode uses different thresholds on the aggregate salience signal (asymmetric Schmitt-trigger hysteresis), and that the asymmetry is mode-specific.

Cools & D'Esposito's framing provides the biological rationale: stability (mode entry / holding) and flexibility (mode exit / switching) are supported by different dopaminergic substrates with different optima. Because the two directions of mode-transition recruit distinguishable neural mechanisms, the aggregate-signal thresholds for entry and exit are structurally different, not symmetric. This is the canonical piece of biology that MECH-266 is translating.

## Confidence: 0.68 (supports)
- source_quality 0.82 (Biol Psychiatry review, canonical framing, >1500 citations)
- mapping_fidelity 0.65 (biological rationale solid; specific threshold asymmetry not directly measured)
- transfer_risk 0.40 (REE's aggregate-signal Schmitt-trigger is one implementation consistent with the biology, not the only one)

## Key limitations
- Review, not a direct test of asymmetric thresholds. Infers asymmetry from pharmacological dissociations.
- Inverted-U is a gradient phenomenon; MECH-266 is a discrete-threshold framing. Gradient vs discrete is a modelling choice.
- The paper attributes stability and flexibility to different regions. REE collapses this into a single SalienceCoordinator; if the region-split matters, MECH-266 at this granularity may miss something.

## Failure signatures
- If biological mode switching is best described as continuous noisy integration rather than threshold-crossing, MECH-266's Schmitt-trigger framing is off.
- If the asymmetry between entry and exit is better modelled as different timescales rather than different thresholds, MECH-266 may be the wrong mechanism description.
- If stability and flexibility live on different regional substrates and REE's single-SalienceCoordinator abstraction loses critical structure, MECH-266 needs to be split across sub-modules.
