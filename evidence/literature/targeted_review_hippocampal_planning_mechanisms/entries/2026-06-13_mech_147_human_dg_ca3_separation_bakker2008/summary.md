# Human DG/CA3 pattern separation vs CA1 completion (Bakker et al. 2008) — MECH-147

**Claim:** MECH-147 — a DG-equivalent sparse layer must decorrelate similar z_world states before rollout proposals are generated.

## What the paper did

Bakker, Kirwan, Miller, and Stark used high-resolution functional MRI (1.5 mm isotropic voxels — fine enough to resolve hippocampal subfields) while human participants incidentally encoded a stream of images, some of which were *lures* — items similar but not identical to previously seen ones. The logic: a region that performs pattern separation should treat a similar lure as *new* (so its activity rebounds, as for a novel item), whereas a region biased toward pattern completion should treat the lure as a *repeat* (activity stays suppressed). The dissociation was clean. Activity consistent with a strong separation bias was found in, and limited to, the CA3/dentate gyrus. Activity consistent with completion — treating the similar lure as the old item — was found in CA1, the subiculum, and entorhinal/parahippocampal cortex.

## Why it matters for REE

This brings the rodent result (Leutgeb 2007) into humans and, for the assembly plan, does something the rodent paper does less explicitly: it **localises the separation/completion division in a single map**. Separation is a CA3/DG property; completion is a CA1/EC property. That is precisely the completion-set structure MECH-147 needs to respect — the separation layer and the completion/readout stage are anatomically distinct sub-computations, and a faithful REE substrate needs both, wired so the separation output feeds a completion stage rather than standing alone. It also reinforces that the *bias* matters: the same input is pushed toward "new" or "old" depending on which subfield dominates, which is the tunable knob (separate vs generalise) a REE planner would have to set.

## Caveats and confidence

The honest limit is that BOLD is an indirect, population-level proxy. The study infers separation versus completion from how the aggregate signal changes to similar-versus-repeated items, not from single-unit sparse-code decorrelation. So this is corroborating, mechanism-localising evidence rather than a direct measurement of the computation. Set against that, the transfer risk is *lower* than for rodent work — these are humans doing a memory task — and the subfield localisation is about as good as non-invasive imaging allows. Confidence 0.80 (supports), complementing the Leutgeb primary: together they give converging cross-species evidence for both halves of the MECH-147 circuit.

*According to PubMed.* Source: Bakker A, Kirwan CB, Miller M, Stark CEL (2008), *Science* 319(5870):1640–2. [DOI](https://doi.org/10.1126/science.1152882)
