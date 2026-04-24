# Schlichting, Mumford & Preston 2015 -- integration prefers established memories

## What the paper did

Adult humans encoded pairs of related events in an associative-inference paradigm. In some trials the two events were encoded simultaneously; in others, one event was established first and the related event followed. Representational similarity analysis on high-resolution fMRI asked whether anterior and posterior hippocampus, and anterior and posterior medial prefrontal cortex, showed learning-related changes in how the related events were represented.

## Key findings relevant to MECH-285

Two findings bear on MECH-285's timing question. First, integration (increased representational similarity across related events) was regionally dissociable from separation (decreased similarity) -- anterior hippocampus and posterior MPFC integrated, while posterior HPC and anterior MPFC maintained distinct representations. Second, and more directly relevant, integration was more likely when one of the two events had been established in memory prior to the encoding of the other -- simultaneously encoded pairs showed weaker integration.

## Translation to REE

MECH-285's third architectural question is timing: does the sleep consumer integrate recently-invalidated traces on the first post-invalidation sleep bout, or only with a delay? Schlichting et al. do not directly measure sleep-phase integration, but their "established-first advantage" suggests a general principle: the system prefers to integrate stable prior representations with new ones, rather than trying to integrate two freshly-encoded traces. Translated to MECH-285: an anchor that was only just marked inactive (its replacement trace is still being established) may be a poor integration target on the immediately following sleep bout. The biology appears to favour letting the winning trace consolidate first, then integrating the loser. This supports a temporal-gating parameter ("broad-window-N") rather than a stateless sampler.

The signal here is weak, however. The paper is an fMRI integration study, not a sleep-replay study. It does not measure start-state distributions and does not manipulate sleep. Its contribution is as a general-principle constraint on the timing of integration, not a direct test of MECH-285.

## Limitations and caveats

Human, not rat. fMRI, not electrophysiology. Encoding paradigm, not sleep. The translation depends on assuming that the "established-first-integrates-more" principle generalises from human episodic encoding to rodent sleep-phase Bayesian aggregation -- a reasonable theoretical bet but not a direct empirical bridge. The paper also does not address priority shape or salience dissociation.

## Confidence reasoning

Moderate source quality (well-executed fMRI). Low mapping fidelity -- the paper addresses only the timing question, and only indirectly. Moderate-to-high transfer risk (human fMRI to rodent sleep SWR is a substantial leap). Aggregate confidence 0.55: informative as a boundary condition, not as direct evidence.
