# Sleep selectively enhances memory expected to be of future relevance (Wilhelm et al., 2011)

Subjects learned declarative material (word paired associates), visuospatial material (a
two-dimensional object-location task) and a procedural finger-tapping sequence. After learning --
and this is the part that matters -- half were told there would be a retrieval test and half were
not. Retention intervals then either contained sleep or did not. Post-learning sleep produced a
strong improvement at delayed retrieval only in the informed group. In the uninformed group,
retrieval after a night of sleep did not differ from retrieval after an equivalent period awake.

The result is a null, and it is the most useful null available to CDQ-011, because it is a null
with a mechanism attached. Sleep did not fail to consolidate; it consolidated something else. The
material that was not flagged as future-relevant simply was not in the set the offline process
operated on, and a measure taken over that material returned nothing.

The translation to INV-063 leg B is close to mechanical. REE's sleep world-forward trainer draws
its replay batch from `_world_experience_buffer` -- a selected subset of what the agent
experienced. The frozen battery that reads leg B out is held-out and unselected. That is exactly
Wilhelm's uninformed condition: a consolidation process operating on one population, measured over
another. The prediction that follows is not that the readout should be replaced but that its
support should be stratified -- split the held-out battery by replay coverage and score within
stratum rather than averaging across it. If the effect is real and diluted, it should appear in the
covered stratum and be absent in the uncovered one. That is a change to where the readout is
scored, not a third candidate objective, which is the distinction CDQ-011 was explicit about.

There is a limit to how far this can be pushed, and it is a sharp one. Selection-dilution predicts
an effect of approximately zero on unselected material. INV-063 leg B did not measure approximately
zero -- it measured a consistent NEGATIVE across-sleep delta, 9/9 cells, on a converged base. The
deltas are small (-7.14e-05, -6.72e-04, -9.22e-04), which is consistent with dilution, but their
sign is consistent, which dilution does not predict. So this paper can account for the magnitude
and cannot account for the direction. Anything registered from it must be paired with a separate
account of the sign, or it under-determines what was actually observed. I would rather say that
here than let a plausible story cover a residual it does not explain.

A second caution, on the source side: the manipulation is a verbal instruction, which changes what
subjects do while awake as well as what sleep does with the trace. The design cannot fully separate
preferential offline consolidation from differential waking rehearsal, and the REE reading assumes
the cleaner of the two. Confidence 0.71, with mapping fidelity 0.7 -- the transferred proposition
(overlap between the consolidated set and the probed set gates the measurable effect) is structural
and maps onto a concrete asymmetry in the substrate -- and transfer risk 0.45, dominated by that
instruction confound rather than by the species gap.
