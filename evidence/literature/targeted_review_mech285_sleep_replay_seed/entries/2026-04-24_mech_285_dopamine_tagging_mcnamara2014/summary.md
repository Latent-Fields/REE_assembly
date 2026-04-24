# McNamara et al. 2014 -- dopamine promotes SWR reactivation

## What the paper did

Mice exploring novel environments received optogenetic burst stimulation of midbrain dopaminergic fibers projecting to hippocampus during specific encoding episodes. CA1 activity was recorded during exploration and during the subsequent rest period. The experimenters asked whether DA activation at encoding altered the subsequent replay pattern, and whether it altered later spatial memory performance.

## Key findings relevant to MECH-285

Optogenetic DA activation during novel exploration enhanced the subsequent reactivation of the cell assemblies formed during those stimulated episodes -- SWR-associated replay over-represented the DA-tagged content. This was reflected downstream in improved recall and stabilised memory performance on goal locations. The priority signal was therefore written at encoding (via DA release) and read out at SWR selection (via enhanced reactivation), with measurable behavioural consequence.

## Translation to REE

MECH-285 bets that epistemic staleness provides a priority signal dissociable from the canonical DA/salience arm. McNamara et al. are the cleanest causal demonstration of the salience arm itself, and their paper is therefore a kind of sibling to MECH-285 rather than a direct test. Two things are architecturally useful here. First, they show the SWR-selection stage *can* be modulated by an upstream tag -- which is exactly the architectural slot MECH-285 needs to plug into. Second, they establish that salience-lineage priority is implemented at encoding but manifests at replay selection, pointing to a pipeline in which priority tags ride with their associated traces into offline processing. If MECH-285's staleness arm operates analogously, the V_s residual would be a tag on the anchor that persists until it is consumed by the sleep-phase sampler.

The dissociation question -- whether a staleness signal can modulate SWR selection independently of DA -- is not tested. This paper is compatible with both a dissociable-arms reading (staleness and salience converge at the sampler) and a composed-priority reading (a single weighted score that happens to be dominated by DA in this paradigm). The canonical test for MECH-285 would be a low-arousal high-novelty paradigm in which DA signals are flat but schema-staleness is high -- McNamara et al. do not provide that contrast.

## Limitations and caveats

Gain-of-function optogenetics in the salience arm, with no measurement of the staleness arm. A negative finding on MECH-285 would not falsify this paper, and vice versa. Mouse, not rat; though both species' hippocampal physiology is broadly comparable for these purposes. Encoding-time DA manipulation, so the priority signal is timed to experience, not to offline deliberation -- MECH-285 posits continuous accumulation between experience and sleep, which is compatible but not directly shown.

## Confidence reasoning

Excellent methods (optogenetic causal manipulation is the right tool for this question). Mapping fidelity moderate because the paper lives on the salience arm rather than the staleness arm. Transfer risk low for the substrate-architecture question (priority-modulation slots exist), higher for direct dissociation claims. Aggregate confidence 0.72.
