# Compte, Brunel, Goldman-Rakic & Wang (2000) — Recurrent-attractor model of working-memory persistent activity

**Claim:** ARC-063 (CandidateRule field with tolerance-gated availability). **Direction:** mixed (fork-A mechanism, but bounds fork A away from the CRF's regime). **Confidence:** 0.70.

## What the paper did

This is the canonical spiking-network model of *how* prefrontal delay activity sustains itself. Compte et al. built an integrate-and-fire cortical network with a columnar architecture: structured recurrent excitation (deliberately dominated by slow NMDA-receptor kinetics) balanced against feedback inhibition. With the right balance the network settles into a self-sustaining localized "bump" of elevated firing that survives removal of the external cue — reproducing the Funahashi delayed-response phenomenology from first principles. The slow NMDA time constant is load-bearing: it is what lets reverberation persist without runaway or collapse. This is the mechanistic backbone of the "recurrent-attractor working memory" account named as fork A in the V3-EXQ-666 autopsy (the "Wang recurrent-attractor WM" anchor).

## Why it matters for the CRF — and why it is *mixed*, not a clean support

On the supporting side: if the CRF is to maintain a rule by sustained activity, this paper is the blueprint. The transferable idea is a **recurrent self-sustaining term** — after a rule is matched and selected, a positive feedback loop keeps its availability elevated for a while even though its context has vanished. That is a legitimate, biologically-grounded option for the CRF's *engaged* rule, and it pairs naturally with Funahashi's empirical demonstration.

On the weakening side — and this is why I marked it mixed for ARC-063 — the very same model exposes fork A's ceiling for the CRF's *actual* problem. A continuous-attractor network holds **one bump**. Capacity is small; pushing several simultaneously-active memoranda into the network makes bumps merge or competitively suppress each other. It is metabolically expensive (everything being maintained fires tonically at elevated rates for the whole delay), and the bump *drifts* over time and is *disrupted by distractors*. None of that scales to the CRF's V3-EXQ-666 ARM_2 regime, where 10–16 differentiated rules must each remain available across ~2000–3900 ticks while matching only a sparse slice of contexts and being unselected almost always. You cannot hold 16 differentiated rules as 16 persistent bumps — the architecture does not have the capacity, and even if it did, the cost and drift would be prohibitive.

## The reading for the substrate fix

Compte/Wang give fork A its mechanism *and* its boundary. They tell us that persistent-firing maintenance is real and well-understood for the engaged item, but they argue *against* using per-tick sustained firing as the maintenance substrate for an availability **pool**. This is the pivot that motivates fork B: if the brain needed to keep many unselected items available, it could not afford to keep them all spiking — which is precisely the gap the synaptic-maintenance literature (Mongillo 2008; Stokes 2015; Lundqvist 2018) fills.

## Confidence reasoning

Source quality is high (landmark, reproduced model). Mapping fidelity is moderate (0.6): right mechanism for fork A, wrong scale for the CRF pool. Transfer risk is elevated (0.4) because a continuous *spatial* attractor maps only loosely onto a discrete slot-based rule field — the transferable content is "recurrent self-sustaining maintenance of the engaged item," not the bump geometry itself.
