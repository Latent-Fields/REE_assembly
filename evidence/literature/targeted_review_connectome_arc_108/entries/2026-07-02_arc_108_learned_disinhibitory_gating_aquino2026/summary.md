# ARC-108 <- Gallo Aquino, Kim & Rungratsameetaweemana (PLOS Biology 2026)

**"Disinhibitory signaling enables flexible coding of top-down information in cortical networks"** -- DOI 10.1371/journal.pbio.3003831. Columbia Engineering.

## Why this paper lands on ARC-108 at all

ARC-108 is the claim that the gating weights deciding which channel wins committed selection should be **learned** -- and its diagnosis of the F-dominance conversion ceiling (MECH-439) is that the current ARC-107 arbitration layer is pure arithmetic with no learned parameters, so F monopolises ~88-89% of selection variance because nothing can re-weight channels through experience. The relevance of this paper is narrow but real: it is a demonstration that when you actually *let the gating structure be learned* on a context-switching task, the network discovers a disinhibitory routing solution, and that solution -- the learned inhibition-on-inhibition weights -- is the causally load-bearing part. Ablate those learned connections and flexible switching collapses; ablate others and nothing happens.

That is support for ARC-108's premise, not its mechanism. The premise -- "hand-specified arithmetic gating cannot reach the flexible context-routing solution that learning finds" -- is exactly the wedge ARC-108 drives between itself and the pure-arithmetic ARC-107 layer. This paper is a clean external instance of learning finding a gating solution that a fixed rule would not obviously reach.

## The caveat that keeps confidence at 0.5

The paper learns its weights by **gradient-based training of the RNN**. ARC-108's actual novel content is a *biologically-local* learning rule: a signed dopaminergic reward-prediction-error teaching signal driving three-factor plasticity (Hebbian channel co-activation x RPE), with the D1-LTP / D2-LTD asymmetry. This paper says nothing about dopamine, RPE, or three-factor plasticity. So it cannot tell us whether ARC-108's proposed *local* rule can discover the same solution that end-to-end gradient descent found here -- indeed, it leaves open the uncomfortable possibility that gradient training reaches a solution the local rule cannot. The dopamine-mechanism grounding for ARC-108 lives in the sibling entries already in this directory (Warnberg 2023 on vector-valued dopamine three-factor plasticity; Gilbertson 2019 on D1/D2 asymmetry; Mah 2024 on RPE). This entry deliberately complements those: it evidences "learned, not arithmetic, and disinhibitory," where they evidence "dopaminergic RPE is a feasible teaching signal."

## Confidence

0.50, supports. High source quality (0.85), but for an architectural-commitment claim I weight mapping fidelity heaviest, and here it is only 0.45 -- squarely on the "must be learned" premise, absent on the dopaminergic-RPE learning rule that is the substance of ARC-108. Logged because the premise it supports is the exact one that motivates pulling the ARC-108 / MECH-450 build forward, but scored honestly for the mechanism gap.
