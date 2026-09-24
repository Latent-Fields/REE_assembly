# McClelland, McNaughton & O'Reilly 1995, "Complementary Learning Systems" -- INV-024

## What the paper did

This is the foundational theoretical paper establishing why the brain uses two separate memory
systems rather than one. Drawing on connectionist simulations showing that a single network
learning new patterns quickly suffers catastrophic interference with previously stored patterns,
the authors argue the hippocampus (sparse, pattern-separated, fast-learning) and neocortex
(distributed, overlapping, slow-learning) are complementary: the hippocampus rapidly encodes new
episodes and then, via replay/reinstatement (notably during sleep), lets neocortex integrate that
content gradually, at a learning rate slow enough not to disturb existing structure.

## Findings relevant to INV-024

The paper's central architectural argument is precisely the motivation INV-024 assumes: a system
that tries to both consolidate slowly-learned structure AND commit to fast, responsibility-bearing
actions within the same substrate will corrupt one or the other unless the two processes are kept
functionally separate. CLS is the reason two systems (and, by extension, two write regimes) exist
at all in biological memory architecture.

## How this translates to REE

INV-024 claims REE's offline (sleep-phase) consolidation and online (waking) commitment must
remain isolated at specific "responsibility-bearing write loci" -- the residue field, BetaGate
latch, and E3 committed_trajectory state. CLS is the deep architectural ancestor of this
separation, generalized from two whole memory *systems* down to specific *write loci* within a
single artificial agent's architecture.

## Limitations and caveats -- why this is moderate, not strong, support

CLS's argument is about representational interference avoidance via different learning rates and
overlap statistics -- both systems still write, on different schedules. INV-024's claim, as tested
by V3-EXQ-1072, is considerably stricter: it requires that specific offline-pass authority stores
be BIT-IDENTICAL before and after a sleep cycle (no write at all, not merely a slow one), and that
every online durable write be lineage-traceable to a commitment event. This is closer to a
write-access/provenance invariant than to CLS's rate-based interference-avoidance mechanism. CLS
supports the general architectural motivation for INV-024's existence; it is not itself a prior
statement of INV-024's specific "no write at these loci at all" / "every write lineage-gated"
formalization, which appears to be REE's own sharpening translated into an audit-checkable claim.

## Confidence reasoning

`source_quality` 0.9 (among the most foundational, most cited papers in the field).
`mapping_fidelity` 0.4 (motivates the general separation; does not state or test the specific
write-locus isolation / lineage-gating mechanism). `transfer_risk` 0.5 (biological
learning-systems theory to an artificial agent's specific module boundaries). Aggregate
confidence 0.5.

## Bearing on the novel_discovery question (searches run)

Queries run: "McClelland McNaughton O'Reilly 1995 complementary learning systems hippocampus
neocortex catastrophic interference"; the chip also suggested checking whether the Saltzer 1975
complete-mediation entry under targeted_review_mech_067 bears on INV-024 -- it was located and
read (see below) but is a systems-security design principle (complete mediation of every
access), not neuroscience, and was judged a weaker, more abstract analog than CLS. Verdict: at
the level of the general architectural motivation -- two functionally separated systems/regimes
for consolidation versus commitment -- INV-024 does NOT survive as a novel-discovery candidate;
CLS has stated this since 1995 and it is one of the most replicated ideas in systems
neuroscience. At the level of the SPECIFIC formalization INV-024 actually tests (bit-identical
authority-store hashes across a sleep cycle; lineage-traceability of every durable online write
to a commitment event) -- no paper in this search states or tests that specific, stricter
write-provenance claim. That gap between the general motivation (well-established) and the
specific audit-checkable formalization (not found stated anywhere) is the honest boundary of
what is and is not novel here.
