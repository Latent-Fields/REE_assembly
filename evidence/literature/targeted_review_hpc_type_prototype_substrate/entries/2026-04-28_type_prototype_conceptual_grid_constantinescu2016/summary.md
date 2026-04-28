# Constantinescu, O'Reilly & Behrens 2016 — Organizing conceptual knowledge with a gridlike code

According to PubMed: Constantinescu, O'Reilly & Behrens. *Science* 352(6292):1464-1468 (2016). [DOI 10.1126/science.aaf0941](https://doi.org/10.1126/science.aaf0941). PMID 27313047.

## What the paper did

28 human subjects learned a 2D conceptual space defined by morphing a bird image along two continuous dimensions — leg length and neck length — and then navigated this space during fMRI by watching morph trajectories and judging the trajectory direction. The authors then tested whether the same hexagonal-symmetric BOLD signature that grid cells produce during spatial navigation would also appear when subjects traverse this *conceptual* space.

It did. The hexagonal six-fold-symmetric signal appeared in entorhinal cortex, posterior cingulate, ventromedial prefrontal cortex, and a handful of other regions — strikingly similar to the regions activated during spatial navigation. The signal was stable across sessions: hexagonal alignment present in one session was preserved in a follow-up scan more than a week later.

## Why this matters for REE's question

This is an architecturally important paper for sub-question 3: is the type-prototype substrate one HPC code with multiple input streams, or two distinct codes? Constantinescu 2016 evidences the **one-machinery-multiple-domains** answer at least partially. The same grid-like cognitive-map architecture that handles spatial navigation handles conceptual navigation. The brain doesn't appear to maintain separate cognitive-map primitives for "where you are in space" and "where you are in conceptual relations" — it reuses the spatial machinery for both.

For REE this licenses a specific architectural simplification. Instead of adding a fully separate type-prototype substrate (provisional SD-N as a parallel codebook), the prototype machinery could be implemented as a **new input projection onto existing machinery**. The AnchorSet operates on z_world (spatial-residue input); a parallel projection from a different latent — say, a category-relevant stream extracted from `LatentState` — could feed into the same anchor-pool primitive but produce category-keyed anchors rather than location-keyed ones. The architectural primitive is shared; the input is different.

This is a less-invasive architectural extension than the dual-substrate reading the Schapiro et al. 2017 modelling paper would suggest. The two readings are not strictly incompatible — Constantinescu 2016 evidences shared *cognitive-map machinery*, while Schapiro 2017 evidences distinct *learning pathways within HPC*. Both can be true: a unified cognitive-map output produced by complementary instance-vs-regularity learning pathways. But for an REE V3 implementation pass, the parsimonious starting point is the Constantinescu reading — one substrate, multiple input projections.

## What it does NOT settle

The signal is strongest in **entorhinal cortex and frontomedial regions**, not in HPC proper. The cognitive-map machinery is more accurately described as EC-resident, with HPC providing instance binding rather than the relational geometry itself. REE's mapping needs to respect this: if a type-substrate is added, its biological grounding is more EC-analogue than HPC-anchor-pool-analogue. REE has no EC-analogue substrate currently; the AnchorSet sits closer to CA1/CA3 functional territory.

The conceptual space tested is **2D continuous** (bird-shape morphing). REE's category prototypes would be discrete-category — "hazard," "resource," "wall" are not points on a continuous manifold; they are distinct types. Grid cells are biologically a continuous-relation primitive. Whether the same architecture extends to discrete category codes is a separate empirical question — Bellmund et al. 2018 *Science* (related work, not pulled in this review) extends the framework toward generalisation but still works with continuous structures.

The paper does not address sleep. The conceptual-grid signal develops during the learning session. Whether sleep enhances or stabilises it is unaddressed.

## Confidence reasoning

I sit this at 0.82. Source quality 0.88 — *Science*, careful task design, robust replication across sessions over a week-plus interval. Mapping fidelity 0.75 because the unified cognitive-map machinery licenses the architectural option of *not* adding a fully separate prototype substrate but instead adding a new input projection to existing machinery — that's directly the architectural choice REE would face. Transfer risk 0.35 because the continuous-conceptual-to-discrete-category gap is the main uncertainty, and the EC-vs-HPC localisation needs respecting in any REE substrate-mapping decision.
