# Summary: Everitt et al. 2003 — BLA/CeA Double Dissociation in Appetitive Learning

**Source:** Everitt, Cardinal, Parkinson & Robbins (2003). *Appetitive behavior: impact of amygdala-dependent mechanisms of emotional learning.* Annals of the New York Academy of Sciences 985: 233–250. [DOI: 10.1196/annals.1280.022](https://doi.org/10.1196/annals.1280.022)

## What the paper did

This canonical review from the Everitt-Robbins group synthesised lesion studies across appetitive conditioning paradigms — Pavlovian approach (autoshaping), Pavlovian-to-instrumental transfer (PIT), conditioned reinforcement, and instrumental action-outcome learning. Across paradigms, the group documented double dissociations between the basolateral amygdala (BLA: basolateral, basomedial, and lateral nuclei) and the central nucleus of the amygdala (CeA). The review additionally frames the dissociation in evolutionary terms: BLA as phylogenetically recent, encoding specific CS-UCS value associations; CeA as phylogenetically older, mediating generalised incentive-motivational invigoration of behaviour.

## Key findings

BLA lesions impaired: (1) the ability of a CS to gain access to the *current* affective value of its paired UCS (devaluation sensitivity), and (2) conditioned reinforcement (CRf) — the ability of a previously rewarded cue to motivate new instrumental learning. CeA lesions impaired: (1) appetitive Pavlovian autoshaping (conditioned approach), and (2) specific aspects of incentive motivation, while leaving CRf and devaluation sensitivity intact.

The theoretical synthesis is explicit: BLA is required when behaviour must be guided by the *specific outcome value* encoded during learning; CeA is required when behaviour must be *invigorated* by conditioned stimuli through incentive motivational mechanisms. These are not competing accounts of amygdala function — they describe two layers of the same architecture operating together.

The review also establishes that BLA and CeA normally function cooperatively: BLA-encoded outcome representations feed CeA's motivational output in many paradigms. But the dissociation is cleanest when tasks pit specific outcome-value sensitivity against general motivational invigoration.

## REE mapping

SD-035 directly implements this two-module architecture. BLAAnalog handles encoding_gain (MECH-074a: BLA-mediated arousal-weighted memory writing), retrieval_bias (MECH-074b: BLA-mediated CS-UCS value retrieval), and remap_signal (MECH-074d: reconsolidation/PE-triggered map update) — all of which correspond to the BLA's CS-UCS specific value function documented here. CeAAnalog handles mode_prior (MECH-046: CeA-mediated motivational mode switch into SalienceCoordinator) and fast_prime (MECH-074c: rapid CeA subcortical priming of the harm channel) — which correspond to the CeA's incentive-motivational invigoration function.

The evolutionary framing (BLA as recent, CeA as older) maps to SD-035's design in a subtle but important way: CeAAnalog is the *simpler* non-trainable arithmetic module (magnitude thresholding on z_harm_a, pre-softmax log-odds addition) while BLAAnalog carries the more computationally elaborate associative retrieval and PE-driven remap functions. The architecture thus tracks the phylogenetic gradient the review describes.

## Limitations and caveats

The review synthesises appetitive conditioning paradigms; SD-035 is implemented primarily in a harm-avoidance context. For aversive conditioning, the dissociation is broadly preserved but the details differ: in some aversive tasks, BLA lesions also impair CeA-like outputs (e.g. freezing) because CeA receives strong BLA input. The two-module architecture is most cleanly visible when tasks isolate specific outcome-value sensitivity (BLA) from generalised conditioned invigoration (CeA).

The review predates optogenetic methods and thus cannot speak to the CeA's internal microcircuit structure (CEl/CEm), which is relevant to CeAAnalog's fast_prime timing. For that detail, see Ciocchi et al. 2010 in this directory.

## Confidence

0.80. High confidence because this is the definitive double-dissociation review for the BLA/CeA architecture that SD-035 registers, written by the group that produced most of the key lesion evidence. The moderating factor is the appetitive-to-aversive transfer and the omission of internal CeA microcircuit detail.
