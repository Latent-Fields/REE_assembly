# Espinoza, Guzman, Zhang & Jonas (2018) — PV+ lateral-inhibition microcircuit in dentate gyrus

**Source:** Nature Communications 9:4605. DOI [10.1038/s41467-018-06899-3](https://doi.org/10.1038/s41467-018-06899-3). PMID 30389916 / PMC6214995. Retrieved via PubMed.

**Claim:** SD-016 (selection mechanism leg — GOV-FANOUT-1 H3).
**Direction:** supports. **Confidence:** 0.84.

## What the paper did

Jonas's group asked a question that is unusually well-matched to what SD-016 needs answered. The
idea that the dentate gyrus performs pattern separation by a winner-take-all mechanism has been
around since Marr, but as the authors point out, it had an awkward problem: a WTA circuit requires
*lateral* inhibition (an active principal cell suppressing its neighbours) and is actively harmed by
*recurrent* inhibition (an active cell suppressing itself, which would suppress the very winners the
circuit is trying to select). And in every circuit anyone had measured — neocortex, entorhinal
cortex, presubiculum — recurrent and lateral inhibition are roughly equally abundant. The authors
state the tension plainly: such a design "would seem incompatible with efficient pattern separation."

So they measured it. Simultaneous whole-cell patch-clamp from up to eight neurons at once (up to
seven granule cells and up to four interneurons), 9098 tested connections across 270 slices, with
PV+, SST+ and CCK+ interneurons genetically labelled. The result is a clean dissociation. In 1301
GC–PV pairs they found 296 unidirectional inhibitory connections against only 32 bidirectional ones
— a lateral:recurrent ratio of **9.25**, an order of magnitude away from every other circuit in their
comparison table. PV+ interneurons also dominate: for pairs within 100 µm, connection probability was
11.0% (GC→PV) and 28.8% (PV→GC), against 1.4/2.8% for SST+ and 1.2/12.1% for CCK+. Direct excitatory
GC–GC interactions were entirely absent.

The spatial structure is the second finding, and it is asymmetric in a way that matters. Excitatory
drive onto interneurons is **focal** (peak connection probability 11.3%, space constant 144 µm);
inhibitory return onto granule cells is **broader and stronger** (28.9%, 215 µm), both differences
significant by bootstrap (p < 0.0001 and p = 0.0042). Overall inhibition outnumbers excitation by a
connection-probability ratio of 3.83. Motif analysis against a distance-matched random network
(10,000 bootstrap replications, Benjamini–Hochberg corrected) found convergence motifs, divergence
motifs, and PV–PV mutual-inhibition/gap-junction motifs significantly enriched — but, contrary to the
neocortical prior, reciprocal GC–PV motifs were *not*.

## Why this matters for SD-016

The V3-EXQ-898 autopsy's central diagnosis was that REE's tagger is a "formal-definition import": a
plain feedforward network trained end-to-end by downstream task losses, with no local competitive
dynamics, no lateral inhibition, no k-winner-take-all, and no sparsification pressure. The autopsy's
sharpest sentence was that "biological pattern separation does not wait for a downstream task loss to
demand sparsity — it is a structural property of the circuit."

This paper is the direct evidence for exactly that sentence, and it is the reason I weight it as the
load-bearing entry in this pull. The competitive machinery in the dentate gyrus is not an objective
function. It is wiring. It is present in the connectivity statistics before any learning signal
arrives, and it is *specialised* — the same measurement in neocortex gives the opposite answer. That
converts the H3 leg's premise from a plausible analogy into a grounded one: three independently
designed REE selection mechanisms have now converged on the identical uniform-softmax saddle
(`sel_entropy_mean` → ln(16) = 2.7726), and on this evidence the thing they all lack is not a better
loss but a competitive operator.

The design guidance is more specific than "add competition," which is what makes it useful rather
than merely encouraging. Three concrete constraints fall out:

1. **Inhibition must be lateral, not recurrent.** Slot *i* should suppress slots *j ≠ i* and must not
   suppress itself. The authors are explicit that recurrent inhibition "may be counter-productive,
   because it could suppress potential winners." An REE implementation that adds an undifferentiated
   normalisation or inhibition term across all 16 slots — self included — would be importing the
   neocortical motif, which is the one measured *not* to support separation. This is a real and easy
   mistake, and it is worth stating in the H3 build spec.
2. **Suppressive reach should exceed excitatory reach.** The 3.83 inhibition:excitation ratio and the
   215 µm vs 144 µm space constants both say the same thing: a winner's suppressive footprint is
   wider than the drive that made it a winner.
3. **Winners are decided relatively, against a shared inhibitory pool** — not by an absolute
   per-slot threshold. The in vivo recordings sharpen this: unitary GC→PV EPSPs averaged 1.79 mV
   against a 10.3 mV baseline-to-threshold gap, so no single input drives the interneuron. Competition
   only engages through spatial summation over many converging units.

## Limitations, and the two that are genuinely load-bearing

The honest caveats are that this is a slice preparation at room temperature in juvenile mice, and —
more importantly — that the paper measures *connectivity statistics* and argues from them that the
circuit **affords** winner-take-all. It does not observe WTA dynamics during behaviour. The authors
are careful about this themselves, noting that whether pattern separation and gamma-oscillation
generation can coexist in the same circuit "remains to be determined." So what this licenses is the
*shape* of an REE competitive operator, not a parameterisation.

Two disanalogies deserve to be flagged before anyone treats this as a blueprint, because neither is
something the paper can adjudicate:

**Scale.** The dentate gyrus runs competition over roughly a million granule cells at ~5% activation.
SD-016 selects over **16** slots. Those are not the same regime, and the difference is not a detail.
A k-WTA over 16 slots with k small is arguably closer to a hard argmax than to biological sparse
coding, and hard argmax carries its own well-known problem — it is not differentiable, so it cannot be
trained by the gradient path SD-016 currently relies on (`terrain_loss`). The H3 build will have to
choose a relaxation (straight-through estimator, Gumbel-softmax with annealed temperature, or an
explicit lateral-inhibition term inside a softmax), and this paper does not tell us which. That is a
genuine open design question, not a gap in the evidence.

**Topology.** The measured lateral structure is *spatially graded* — inhibition falls off with
intersomatic distance on a 215 µm constant. An REE slot array has no metric topology at all. The
honest import is therefore all-to-all-minus-self inhibition, which is a real simplification of what
was measured, and it discards whatever computational work the spatial grading was doing.

I have set mapping_fidelity at 0.80 and transfer_risk at 0.30 to reflect those two. The confidence
stays high (0.84) because REE is importing an *architectural motif*, which is precisely the level at
which this paper is strongest and the level at which the rodent-to-artificial-agent transfer worry
bites least — this is a statistical property of a microcircuit, not a behavioural effect size that
would need to survive a species jump.

One last note on what this entry does *not* do. It grounds H3 (the operator). It speaks only
indirectly to H2 (the structured retrieval unit), because it takes the granule-cell population as
given and asks how selection over it works. The Neunuebel & Knierim 2014 and Cayco-Gajic & Silver 2019
entries in this directory carry the H2 side.
