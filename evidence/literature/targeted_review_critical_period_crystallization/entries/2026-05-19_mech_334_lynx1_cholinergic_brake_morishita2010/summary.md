# Morishita, Miwa, Heintz & Hensch (2010) — Lynx1, a cholinergic brake, limits plasticity in adult visual cortex

*According to PubMed. Science 330(6008):1238-40. [DOI](https://doi.org/10.1126/science.1195320) · PMID 21071629 · PMC3387538.*

## What the paper did

Morishita and colleagues found a second lock — and a different kind of lock. Lynx1, an endogenous protein that dampens nicotinic acetylcholine receptor signalling, rises with cortical maturation. In adult primary visual cortex its presence prevents ocular-dominance plasticity. Delete the gene, and the brake is gone: Lynx1-knockout mice keep a juvenile-like capacity for plasticity into adulthood. Pharmacologically enhancing cholinergic signalling reproduces the effect. The framing the authors give is the one that matters here: closure requires *active molecular braking*, and Lynx1 maintains the stability of mature networks in the continued presence of cholinergic drive.

## Why it matters for MECH-334

There is a real risk, when a single landmark paper (Pizzorusso) supports a claim, that the claim is only as strong as that one mechanism. Morishita et al. remove that worry. Lynx1 is molecularly orthogonal to perineuronal nets — a cholinergic brake versus an extracellular-matrix scaffold — and it independently confirms the same abstract property MECH-334 asserts: closure is something actively expressed and maintained, and its genetic removal leaves the window perpetually open. That convergence from two unrelated molecular routes is exactly what raises confidence that the *property* (active, maintained, removable locking), not the specific biochemistry, is the real invariant — which is the only part REE can or should inherit.

## Limitations and the honest caveat

The single most consequential fact for REE is in the knockout: remove one brake and plasticity never closes. That tells us the default state of a learning system is *not* "closed and stable"; it is "perpetually overwritable", and closure is an engineered addition that must be deliberately built and maintained. This is the same proposition INV-074 makes from the necessity side, seen here from the mechanism side, and I have logged it as a failure signature because it disciplines the REE implementation: a MECH-334 that treats closure as the natural resting state would have the polarity backwards. The second logged signature is multi-lock redundancy — biology uses at least two partially-redundant brakes; a single-mechanism REE closure may be more brittle than the biology it models, and that brittleness should be tested, not assumed away. As with Pizzorusso, the transfer is to an abstract property, not to nicotinic signalling.

## Confidence

0.85, `supports`. Source quality is high (Science, Hensch lab). Its evidential value is precisely that it is *mechanistically independent* of Pizzorusso, so it corroborates rather than echoes. Held just below Pizzorusso for the coarser visual-evoked-potential readout and the same structural-to-algorithmic abstraction step. With Pizzorusso, MECH-334's active-locking thesis now has two convergent causal anchors; Aton (2013) adds the sleep-gated execution.
