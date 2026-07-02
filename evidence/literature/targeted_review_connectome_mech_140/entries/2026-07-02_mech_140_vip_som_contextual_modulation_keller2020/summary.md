# MECH-140 <- Keller, Dipoppa, Roth, Caudill, Ingrosso, Miller & Scanziani (Neuron 2020)

**"A Disinhibitory Circuit for Contextual Modulation in Primary Visual Cortex"** -- Neuron 108(6):1181-1193.e8, DOI 10.1016/j.neuron.2020.11.013, PMID 33301712.

## What the paper did

This is the canonical cellular dissection of a cortical disinhibitory circuit. Using cell-type-specific 2-photon imaging, optogenetic gain- and loss-of-function, and a recurrent-network model in mouse V1, the authors traced how context modulates responses. The mechanism: VIP-expressing interneurons inhibit somatostatin-expressing (SOM) interneurons. When the surround differs from the center (an "interesting" context), VIP neurons fire, suppress SOM neurons, and thereby *relieve* excitatory neurons from SOM-mediated suppression. When center and surround match, VIP falls silent and SOM suppression returns. Parvalbumin (PV) interneurons, by contrast, track excitatory activity and are context-independent. Optogenetic perturbation showed the VIP->SOM limb is both necessary and sufficient for the contextual effect, and -- an important mechanistic detail -- it works chiefly by modulating *recurrent* excitation rather than acting as a feedforward subtraction.

## Why it speaks to MECH-140

MECH-140 asks REE to arbitrate with graded, soft-competitive disinhibition instead of winner-take-all. The value of this paper is that it grounds the "disinhibition is a real, causally load-bearing, graded control primitive" half of the claim in about as clean a piece of biology as exists: a named cellular circuit, causally established as necessary and sufficient, that produces context-dependent *relief from suppression* rather than hard gating. That is precisely the flavour of control MECH-140 argues for -- suppression that is lifted or applied by degree, carried by inhibition acting on inhibition.

## The honest caveat

The "context" in this paper is stimulus center-surround congruence within a sensory area -- a much narrower and more concrete thing than the tri-loop conflict / task-rule context MECH-140 is really about. And the substrate is cortical VIP/SOM, not the basal-ganglia indirect pathway that MECH-140 specifically names (via Lee & Sabatini 2021 and Morita 2016). So this is grounding for the *principle and its cellular plausibility*, not evidence for the particular arbitration locus. It pairs with the Aquino 2026 entry: Aquino 2026 shows the disinhibitory motif carries top-down *task* context in a trained network and breaks switching when ablated; Keller 2020 shows the concrete cortical cellular circuit that implements graded relief-from-suppression. Together they support the computational principle from two angles without either one landing squarely on the BG tri-loop substrate.

## Confidence

0.58, supports. Source quality is very high (causal, cell-type-specific, canonical). The evidence_class token is an imperfect fit -- the method is imaging plus optogenetics, and `electrophysiology_single_unit` is the nearest available label for cellular-resolution causal recording. Mapping fidelity (0.5) is the limiting factor for the same locus and context-granularity reasons noted above.
