# Quiroga, Reddy, Kreiman, Koch & Fried 2005 — Concept cells in human MTL

According to PubMed: Quiroga, Reddy, Kreiman, Koch & Fried. *Nature* 435:1102-1107 (2005). [DOI 10.1038/nature03687](https://doi.org/10.1038/nature03687). PMID 15973409.

## What the paper did

Eight epilepsy patients with depth electrodes placed in medial temporal lobe (hippocampus, entorhinal, parahippocampal, amygdala) for presurgical seizure mapping participated in single-unit recording sessions while viewing photographs of famous people, landmarks, animals, objects — and, in a striking subset of trials, written and spoken names of the same identities. Across 132 sessions and 993 selectively responsive units, the authors identified a remarkable subset of cells that fire for many strikingly different views of one specific identity.

The Jennifer Aniston neuron is the canonical example: a single MTL neuron in one patient fired robustly for seven different photographs of Jennifer Aniston (different angles, hairstyles, outfits) and stayed silent for non-Aniston photographs. Other neurons did the same for Halle Berry, the Sydney Opera House, Luke Skywalker. Some of these cells additionally fired for the *written or spoken name* of their preferred identity — establishing that the representation is not view-tied or even visual-tied; it's an abstract identity code.

## Why this matters for REE's question

This paper is the canonical empirical anchor for biological type-prototype representations. It demonstrates that the medial temporal lobe contains cells whose firing pattern realises a sparse, invariant, multimodal, abstract identity code — exactly the architectural primitive Daniel was reaching for when he asked whether HPC holds "high-level representations that can be filtered by verisimilitude to identify the currently observed version of the universal principle for that object or action type."

A concept cell is, computationally, a verisimilitude filter on a stored prototype. It "asks" of every incoming sensory event: does this match my stored abstract identity? It fires when the answer is yes, regardless of surface variation. An REE codebook of prototype entries that get cosine-matched against current `LatentState` would be doing the same operation in vector form rather than spike form.

The biology supports the existence of the substrate. It does *not*, on its own, settle whether the substrate is anatomically distinct from the place/anchor substrate or whether it lives at a different abstraction level on the same code. The Schapiro et al. 2017 entry in this same review addresses that question directly.

## What it does NOT settle

The cells respond to specific identities — *this* person, *this* landmark — not to category prototypes of the form "hazard-type" or "resource-type." The mapping from individual-identity invariance to category-prototype matching is plausible but not directly tested here. REE's proposed prototype substrate would need to support both, and the paper only directly evidences the former.

The cells are sparse and rare. The original estimate is that fewer than 1% of recorded MTL neurons fire selectively for any given concept. This constrains the architectural shape of an REE codebook — it should be sparse (few slots fire per input, each input matches few slots), not dense (every input lights every slot at varying intensities).

The paper does not localise the cells to a single substrate within MTL. They appear in hippocampus, entorhinal, parahippocampal cortex, and amygdala, with somewhat different prevalence in each. REE's substrate-mapping decision (codebook attached to AnchorSet vs separate substrate vs distributed across substrates) is therefore not narrowed by Quiroga 2005 alone.

The patient population is presurgical epilepsy — not a representative healthy sample. This is the standard caveat for human single-unit work. Subsequent recordings in healthy primates and in non-epileptogenic regions of the same patients have replicated the basic finding, so the caveat is mitigated but not eliminated.

## Confidence reasoning

I sit this at 0.88. Source quality 0.92 — *Nature*, the canonical clinical platform for human single-unit recording. Mapping fidelity 0.78 because the existence of instance-invariant abstract representations is exactly what REE's hypothetical prototype substrate needs, and the gap (individual identity vs category prototype) is plausibly the same architectural primitive at different abstraction levels. Transfer risk 0.30 — the patient-population caveat is real but well-understood and partially mitigated by replication in other species and contexts.
