# Schapiro, Turk-Browne, Botvinick & Norman 2017 — Complementary learning systems WITHIN the hippocampus

According to PubMed: Schapiro, Turk-Browne, Botvinick & Norman. *Phil Trans R Soc B* 372(1711):20160049 (2017). [DOI 10.1098/rstb.2016.0049](https://doi.org/10.1098/rstb.2016.0049). PMID 27872368.

## What the paper did

The Complementary Learning Systems (CLS) framework — McClelland, McNaughton & O'Reilly 1995 — argued that the brain handles the trade-off between memorising individual episodes and extracting regularities by allocating each to a separate substrate: hippocampus for episodes, neocortex for slow generalisation. The Schapiro et al. 2017 paper makes a more architecturally precise claim. The same trade-off, they argue, is handled *within* hippocampus, by **two anatomically distinct pathways**.

They built a neural-network model that instantiates known hippocampal subfield topology — DG sparsification, CA3 recurrence, CA1 read-out, and the direct EC → CA1 monosynaptic bypass. They exposed it to sequences with embedded temporal community structure (items that cluster into co-occurrence groups). The result: the trisynaptic pathway (EC → DG → CA3 → CA1) learned individual episodes — sparse, pattern-separated representations of specific item sequences. The monosynaptic pathway (EC → CA1 directly) supported statistical learning — representations whose similarity geometry tracks community membership rather than specific co-occurrence.

The model output matches the empirical fMRI signature from Schapiro et al. 2013/2016 — community-structured representations in CA1 — and reconciles it with the long-standing CA3 evidence for pattern-separated episodic encoding.

## Why this matters for REE's question

This is the architecturally decisive paper for Daniel's first sub-question. The biology supports a **two-level substrate within HPC**, not a single substrate that does both jobs at different abstraction levels. REE V3 currently has the AnchorSet substrate, which is functionally trisynaptic-analogous: it pattern-separates instances by `(scale, segment_id, stream_mixture)` keys. The monosynaptic-analogue — a substrate that takes the same input but extracts the *regularity* across instances — is what's missing.

The architectural shape this licenses for REE: a new substrate (provisional SD-N) that takes the same upstream input as AnchorSet (the LatentState fed in via the agent's `sense()` path) but processes it through a different operator — one that extracts statistical regularity rather than instance-specific snapshots. The two substrates would converge at a common downstream interface (the proposer / CA1-analogue) where both episodic and regularity-based content can drive trajectory generation.

For the sleep substrates (MECH-273, MECH-275, MECH-285), the architectural inference is that the sleep operator should write to **both** levels — consolidating anchors *and* extracting prototypes — and that the existing aggregator/writeback operations are doing only the consolidation half.

## What it does NOT settle

The model is a computational instantiation of an anatomical hypothesis. It is consistent with the behavioural and fMRI data from the same lab's earlier empirical work, but the dual-pathway functional dissociation is not derived from lesion or optogenetic dissociation — it is built into the model architecture and shown to fit the data. Subsequent work (Schapiro et al. 2017 in *Cognitive, Affective & Behavioral Neuroscience* with amnesic patients showing dissociated impairments) provides converging support, but the claim is partly inferred from the model's match to behaviour rather than measured directly.

The "statistical learning" the monosynaptic pathway supports here is **temporal community structure** — which items co-occur in sequence — not category-prototype extraction in the Quiroga 2005 sense. The mapping from temporal community structure to category prototype is plausible (both are abstractions over instances), but it is not directly demonstrated. An REE prototype substrate that extracts category-level invariants might or might not be served by the same monosynaptic-analogue architecture.

The paper does not address sleep. The dual-pathway dissociation is shown for waking learning. Whether the sleep operator preferentially affects one pathway over the other is a separate question.

## Confidence reasoning

I sit this at 0.83. Source quality 0.82 — *Phil Trans R Soc B*, special issue, careful mechanistic model with empirical match. Mapping fidelity 0.85 because the dual-pathway architectural claim directly answers the first sub-question of the lit-pull: whether REE's type-prototype substrate should be biologically distinct from the anchor substrate. Transfer risk 0.30 because the temporal-regularity-to-general-prototype generalisation is plausible but not directly evidenced.
