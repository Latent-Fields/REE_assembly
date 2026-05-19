# Pizzorusso et al. (2002) — Reactivation of ocular dominance plasticity in the adult visual cortex

*According to PubMed. Science 298(5596):1248-51. [DOI](https://doi.org/10.1126/science.1072699) · PMID 12424383.*

## What the paper did

If Fagiolini & Hensch showed how the window opens, Pizzorusso and colleagues showed that it does not so much *close* as get *locked*. They tracked chondroitin-sulphate-proteoglycan perineuronal nets — a component of the extracellular matrix — and found their organisation around cortical neurons coincides with the end of the critical period, and is delayed when animals are dark-reared (closure tracks experience, not just the calendar). Then the decisive manipulation: degrade the nets in an adult rat with chondroitinase-ABC, impose monocular deprivation, and ocular dominance shifts again — adult plasticity is restored. The mature matrix is not inert scaffolding; it is an actively inhibitory structure holding the circuit in place.

## Why it matters for MECH-334

MECH-334's whole content is that closure is *active locking* — "a complementary closure mechanism reduces plasticity for the crystallized diversity distribution while restoring full dominant-pathway update scale" — and that without it the diversity representations stay overwritable forever. Pizzorusso et al. are the cleanest causal evidence in the literature that closure is exactly this kind of thing: a maintained constraint, removable in principle, whose presence is what protects the consolidated circuit. This is the biological warrant for REE's design choice to write-protect the crystallized diversity distribution post-window rather than merely letting learning rates decay. For a claim that had zero literature entries, this is the load-bearing anchor.

## Limitations and the honest caveat

Two facts in this paper are not decorations — they are constraints on any faithful MECH-334 implementation, and I have logged both as failure signatures. First, reactivation required *active enzymatic removal*; the lock did not spontaneously weaken. So MECH-334 must be a *maintained* write-protection, not a one-shot event at the window boundary, or the crystallized distribution will quietly erode and the claim's protective guarantee will be hollow. Second, closure timing tracked net assembly and was delayed by dark rearing — closure is experience-modulated. A MECH-334 that fires at a fixed epoch regardless of the realised learning trajectory would diverge from this biology; the closure trigger should be coupled to the state of consolidation, echoing the Aton (2013) "instruction must be correct before crystallization" logic in the same folder. The transfer itself is an abstraction: perineuronal nets are a physical structure, REE's analogue is an algorithmic penalty on crystallized weights. What transfers is the *property* — actively maintained, in-principle reversible — not the matrix biology.

## Confidence

0.88, `supports`. Source quality is near-ceiling (landmark Science paper, much replicated). Mapping fidelity is high for the active-locking property that is MECH-334's core, discounted for the structural-to-algorithmic abstraction. I set it just below the claims.yaml anchor's 0.92 to keep honest headroom for that substrate-transfer gap.
