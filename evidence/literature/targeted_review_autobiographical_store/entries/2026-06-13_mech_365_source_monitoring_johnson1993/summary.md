# Source monitoring as the biology of MECH-365's provenance field

**Johnson, Hashtroudi & Lindsay (1993), *Psychological Bulletin* 114(1):3-28. [DOI](https://doi.org/10.1037/0033-2909.114.1.3)** (PMID 8346328).
Claims grounded: **MECH-365** (primary), **ARC-085** (secondary).

## What the paper does

This is the field-defining statement of the **source-monitoring framework**. Its central claim is deceptively simple and exactly the one MECH-365 leans on: memories do not arrive stamped with their origin. There is no stored "I perceived this" vs "I imagined this" label. Instead, the system *attributes* a source at retrieval, by running decision processes over the qualitative characteristics of the memory record — how much perceptual and contextual detail it carries, whether it bears traces of the cognitive operations that would have generated it internally, how it coheres with other knowledge. **Reality monitoring** — telling internally generated from externally derived memories — is presented as one important sub-case. Crucially, the authors insist "source" is *multidimensional*: not a real/imagined dichotomy but indefinitely many possible origins (which external source, who said it, when, generated-by-me vs by-another). The review spans recognition, eyewitness suggestibility, cryptomnesia, incorporation of fiction into fact, and the breakdown of source monitoring in confabulation, amnesia and aging.

## Why it grounds MECH-365

MECH-365 makes provenance a *first-class, represented attribute of an event token* — `event_token = {..., source_status, committed_vs_imagined}` — rather than an implicit mode bit. The source-monitoring framework is the biological warrant for that move: in humans, source genuinely *is* a represented attribute the system reasons about, and reality monitoring is the direct analogue of `committed_vs_imagined`. Without this anchor, MECH-365 would be asserting a data structure by engineering fiat; with it, the structure is the synthetic instantiation of a well-established cognitive function. It also reinforces ARC-085's framing that event tokens are bound to source and self-state, not neutral storage.

## Where the mapping strains — and partly *weakens* the claim

This is the honest part. The human substrate's provenance is **reconstructed and fallible**. Source attribution is a heuristic judgement, and the entire literature on false memory, eyewitness misinformation, and confabulation is a catalogue of it going *wrong* — imagined or suggested content being confidently attributed to perception. That is the opposite of MECH-365's strong commitment: a **one-way gate** that imagined tokens can *never* cross into committed status. So the biology supports the existence and dimensionality of the provenance field while simultaneously showing that the natural version is leaky. MECH-365 is therefore better read as a *normative* design — REE chooses to enforce, at the substrate level, a guarantee that biology only approximates — than as a description of how brains work. That is a legitimate architectural stance (REE is allowed to be safer than the brain), but the lit does not evidence the gate's absoluteness; it evidences the field and, on the gate, leans gently against it. Recorded as a `failure_signature`.

A second strain: because biological "source" is multidimensional, a single binary `committed_vs_imagined` bit may under-specify provenance. Provenance can fail along many axes at once. This feeds the harvest note (below) about whether MECH-365's two provenance fields should be a richer source vector.

## Confidence

0.74. Source quality is near-ceiling (foundational *Psych Bulletin* review). The discount is mapping fidelity: the paper grounds MECH-365's *field* strongly and its *one-way gate* weakly-to-negatively. Net direction `supports`, because the load-bearing content of MECH-365 is the data structure, not a claim that biology already enforces the gate. Raises literature_confidence only; promotes nothing.
