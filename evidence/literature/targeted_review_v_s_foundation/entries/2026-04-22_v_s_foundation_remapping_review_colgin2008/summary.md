# Colgin, Moser & Moser 2008 -- Understanding memory through hippocampal remapping

DOI: [10.1016/j.tins.2008.06.008](https://doi.org/10.1016/j.tins.2008.06.008) -- Trends in Neurosciences (PubMed 18687478)

## What the paper did

A conceptual review by the Moser lab of the hippocampal remapping literature, framed around: how does the brain represent two similar experiences as distinct without losing the ability to retrieve the right one from a partial cue? Authors trace the dissociation between rate remapping (same place-cell ensemble, different relative firing rates) and global remapping (a near-orthogonal new ensemble), arguing these implement different points along a decorrelation-vs-generalisation tradeoff. CA3 supports global, attractor-like transitions; CA1 inherits a more graded mixture; DG sits upstream as the orthogonalising stage.

## Findings relevant to V_s foundation

Three things matter for the substrate plan. First, the existence of two distinct remapping regimes is not in dispute. Second, the regime engaged is not arbitrary: small input perturbations tend to produce rate remapping (preserves the spatial map and re-weights it), while large or qualitatively different perturbations push the system to global remapping. Third, multiple maps for the same physical location can coexist in the sense that the same animal can hold distinct CA3 representations for the same arena depending on context cues -- but the route into one vs the other is a discrete attractor transition, not a continuous mixture under steady-state conditions.

## Translation to REE / MECH-269 / MECH-272

The dual-trace mechanism in MECH-269 (keep inactive anchors in the anchor set; route via MECH-272) maps cleanly onto global remapping. The architectural commitment is biologically defensible at the global-remapping end. But the review insists biology also does rate remapping, a soft re-weighting across a single underlying ensemble. If the in-silico anchor set always behaves like global-remap ensembles (hard active/inactive flags), it will miss the regime where biology smoothly re-weights overlapping representations as inputs drift. A more general implementation would let MECH-272 routing produce either a one-hot active flag (global-remap analogue) or a soft mixture (rate-remap analogue), with the regime determined by the magnitude of the V_s drop on the active anchor.

The review reinforces heterogeneity-by-subfield: CA3 is more attractor-like (good for hard switches), CA1 inherits a more graded code, DG decorrelates aggressively but does not itself store the alternate representation. This argues against a single uniform anchor mechanism in the substrate.

## Limitations and caveats

The review predates much of the schema-cell and event-segmentation literature, so it does not address granularity directly. It is rodent in vivo only. The review is silent on the trigger that flips a network from rate to global remapping -- exactly the gap MECH-284/287 is trying to fill.

## Confidence reasoning

Source quality very high (Trends Neurosci, Moser lab). Mapping fidelity moderate -- architectural translation requires interpretation; biology offers two regimes the substrate plan currently treats as one. Transfer risk low for the qualitative substrate claim; higher for the quantitative claim that the substrate should default to hard active/inactive flags -- the review pushes back on that default.