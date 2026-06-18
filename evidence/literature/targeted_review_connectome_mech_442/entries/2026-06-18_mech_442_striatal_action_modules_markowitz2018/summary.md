# Markowitz et al. 2018 -- the striatum holds and selects over a structured repertoire of behavioral modules

*According to PubMed.* Markowitz, Gillis, Beron, ... Sabatini & Datta 2018, *Cell* ([DOI](https://doi.org/10.1016/j.cell.2018.04.019)).

## What the paper did
Using 3D depth imaging and unsupervised motif segmentation (MoSeq), the authors decomposed freely-moving mouse behavior into a discrete set of sub-second 3D "behavioral modules" expressed in sequence. They then recorded direct- and indirect-pathway activity in dorsolateral striatum (DLS) as mice spontaneously behaved, and lesioned DLS to test its causal role. DLS neurons systematically encode both the *identity* and the *ordering* of behavioral modules; fast-timescale decorrelation between the two pathways facilitates this encoding; and DLS lesions prevent appropriate sequence assembly during exploration and odor-evoked behavior.

## Key findings relevant to MECH-442
This is the closest biological analog to MECH-442's behavioral-descriptor archive: a *structured repertoire of discrete behavioral modules* that the basal ganglia indexes and selects over. The brain does represent behavior as a set of named, reusable units and does run moment-to-moment selection over that set -- which is exactly the "candidate set partitioned by a behavioral descriptor" picture the MAP-Elites adapter borrows. The archive-of-behavioral-types is real, and it lives in the striatal action-selection machinery.

## How it translates to REE
It supports the existence half of MECH-442: a behavioral-module repertoire that the committed selection draws from is a defensible biological object, and the natural REE rendering is a behavioral-descriptor partition of the E3 candidate set (first-action / committed-action class / e2.world_forward strategy signature). It does *not*, however, show the load-bearing MAP-Elites property -- that behaviorally-distinct modules are *retained as per-niche elites against a strong value gradient*. If anything, the fast direct/indirect-pathway decorrelation that facilitates selection reads as competitive winner-take-all gating (pick one module now), consistent with a single-winner commit rather than simultaneous multi-niche retention at the output.

## Limitations and confidence
Methods and venue are strong. The mapping is partial: it evidences a repertoire and selection-over-it (the archive exists; the basal ganglia selects from it) but not per-niche-elite preservation under reward pressure, which is the specific mechanism MECH-442 asserts. Transfer risk is moderate (rodent spontaneous behavior to an REE E3 committed-trajectory selection). Net confidence 0.72, direction supports -- it grounds the behavioral-module-archive object, while leaving the "survives the value argmax" claim to be tested in REE rather than imported.
