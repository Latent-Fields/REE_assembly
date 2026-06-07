# Midbrain circuits for defensive behaviour (Tovote et al., 2016)

**Claim tested:** MECH-279 (PAG-analog freeze gate driven by amygdala harm input)
**Direction:** supports | **Confidence:** 0.80

## What the paper did

Tovote and colleagues set out to define, causally, the midbrain circuitry that selects and executes defensive behaviour. Using optogenetic gain- and loss-of-function, in vivo and in vitro electrophysiology, and neuroanatomical tracing in mice, they dissected the periaqueductal grey (PAG) and its amygdalar inputs to ask how the brain chooses between a passive defensive response (freezing) and an active one (flight), and how each is executed down to premotor output.

## Key findings relevant to the claim

The central result is a specific, causally-demonstrated pathway: an inhibitory projection from the central nucleus of the amygdala (CeA) to the ventrolateral PAG (vlPAG) "produces freezing by disinhibition of ventrolateral periaqueductal grey excitatory outputs to pre-motor targets in the magnocellular nucleus of the medulla." So freezing is gated at the PAG by amygdala input, and the PAG's excitatory output reaches the motor system. The authors further show that this freezing pathway interacts -- anatomically and functionally -- with long-range and local circuits mediating flight, establishing that freeze and flight are *distinct, competing* midbrain programmes rather than one graded output. They frame the PAG as the locus of "selection and rapid execution of an appropriate active or passive defensive response," an evolutionarily conserved survival circuit whose dysregulation is implicated in human anxiety disorders.

## How this translates to REE

This is the direct biological substrate for MECH-279, which posits a PAG-analog freeze gate that commits when amygdala harm drive (z_harm_a) is sustained and exits when it decays. Two elements transfer cleanly. First, the topology: CeA upstream of the freeze gate matches MECH-279's dependency on SD-035 (amygdala analogue), confirming the design's wiring direction. Second, the freeze/flight dissociation validates representing the freeze gate as a distinct output rather than folding all defensive behaviour into one channel.

But the more important contribution of this paper to the *current* question is a scope warning, and I have written the record to make that load-bearing. Tovote et al. characterise defensive **response selection and execution** -- not avoidance **learning**. The CeA->vlPAG pathway tells the animal *how to freeze*; it does not tell us how the animal *learns to avoid*. Read against the V3-EXQ-603g failure (isolated hazard Stage-H, G_H 0/3), this is exactly the trap the cluster autopsy is trying to avoid: REE already has the freeze-output side (MECH-279) and the salience side (SD-035), but a freeze-only substrate will produce defensive immobility and still fail to *learn to avoid*. The survival-learning leg additionally needs an active escape/avoidance pathway and a mechanism to suppress the freeze reaction in favour of the learned action -- which is precisely the prefrontal-suppression result in the companion entry (Moscarello & LeDoux 2013).

## Limitations and confidence reasoning

Confidence 0.80, the highest in this review, because the source is top-tier (Nature; Lüthi, Arber, Deisseroth) with gold-standard causal optogenetics, and the circuit is highly conserved, so species transfer risk is low. It sits below 0.85 only because of the scope boundary above: it strongly supports MECH-279 *as a freeze-output substrate* but speaks only indirectly to the avoidance-learning question this lit-pull was commissioned to inform. That boundary is itself useful -- it tells us that confirming the freeze gate is not the same as fixing the learning leg.
