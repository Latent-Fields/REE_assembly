# Kolling, Behrens, Mars & Rushworth 2012 — Neural mechanisms of foraging

**Source:** *Science* 336(6077):95-98, [10.1126/science.1216930](https://doi.org/10.1126/science.1216930). Via PubMed (PMID 22491854).

## What the paper does

Kolling et al. scanned humans making sequential foraging choices (stay with a current option or search elsewhere in an environment whose average value changes over time) interleaved with classical economic choices (compare two simultaneously presented reward-probability options). They designed the task so the same two values (current option's worth, search alternative's expected worth) could be varied independently, letting them tease apart what each prefrontal region encodes. They find two dissociable circuits: dorsal ACC tracks the average value of the foraging environment and the cost of searching, in an invariant reference frame (what-alternative-is-available); vmPFC tracks the identity and value of the concretely presented option. The dACC signal is particularly striking because it does not rescale with the chosen option — it represents the environment-level alternative rather than the option that was picked.

## Key findings relevant to the claim

- **dACC encodes environment average and search cost, not immediate option value.** The activity rises when the environment is rich and the search is cheap — exactly when breaking commitment is worth considering.
- **vmPFC encodes currently-presented-option value.** The two regions work in opposing frames: vmPFC in option-coordinates, dACC in search-coordinates.
- **Foraging and economic choice recruit distinct networks.** The paper establishes "foraging-mode" as a computationally distinct choice regime, not just a slower version of normal valuation.
- **Search cost is a first-class dACC variable.** Cost is not derived from option value; it is independently tracked, consistent with Rushworth lab's broader cost-benefit decomposition line.

## How this maps onto REE (the translation)

This is the clearest formulation in the literature of what the dACC-analog (SD-032b) should output: a signal that compares *the expected value of breaking commitment and searching* against *the expected value of continuing*. ree-v3 currently has no substrate that tracks a running estimate of the alternative-environment's value. The closest thing is the urgency_weight stub, which is local (scales a threshold on the current action) rather than comparative. The Kolling frame suggests the dACC-analog needs two inputs that ree-v3 does not yet maintain as first-class: an environment-average-value register (effectively a slow-moving baseline of what the world has been paying) and a search-cost register (effectively a prior on how costly commitment-breaking typically is in this environment).

For the salience-network-coordinator (SD-032a), the Kolling frame clarifies *why* breaking commitment is computationally non-trivial — the switch must be justified against an environment model, not just triggered by a local pain or surprise spike. This is the structural reason the urgency-interrupt (SD-032c) needs to route through the salience-network coordinator rather than firing directly as a MECH-091 phase-reset: the interrupt decision itself depends on a comparison that only the dACC-analog can compute.

For the minimum-viable implementation path, this paper sharpens the specification: SD-032b is not just "a consumer of z_harm_a that gates trajectory scoring." It is a substrate that maintains an environment-average-value estimate and emits a continuous signal proportional to `EV(break-and-search) − EV(continue)`. When the signal crosses threshold (MECH-259 switch threshold), the salience-network-coordinator triggers mode transition. This is a richer substrate than the z_harm_a wiring patch we originally considered.

## Limitations and caveats

Kolling's interpretation is contested. Shenhav, Straccia, Cohen & Botvinick 2014 reanalysed the original dataset and argued much of the dACC signal is explained by choice difficulty rather than foraging value specifically (and 2016 extended this with new experiments — see separate entry). The Rushworth group pushed back in later papers. The unresolved debate is about whether dACC primarily encodes "the value of changing what you are doing" (Kolling) or "the cognitive control needed to choose well here" (Shenhav/Botvinick EVC). Both camps agree dACC is centrally involved; they disagree about what exactly it outputs.

The task is human fMRI with artificial visual cues. Whether the same computation runs in a closed-loop embodied agent is a genuine transfer risk — foraging in a rich natural environment involves perceptual sampling costs, memory of visited patches, and locomotor effort that the 2012 paradigm does not capture.

## Confidence reasoning

0.82. Science-level paper, clean experimental dissociation, clean theoretical formulation that maps directly onto a piece of architecture ree-v3 is missing. Source quality is high. Mapping fidelity is good because the search-vs-engage primitive is exactly what the commitment/interrupt substrate needs. Transfer risk is moderate; the contested interpretation is the main reason for the discount. This paper defines the *positive hypothesis* for what SD-032b does; the Shenhav/Straccia paper in the same pull defines the *alternative hypothesis* that we also need to account for.
