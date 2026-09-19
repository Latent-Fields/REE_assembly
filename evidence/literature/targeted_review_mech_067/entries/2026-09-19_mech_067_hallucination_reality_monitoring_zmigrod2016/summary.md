# Reality monitoring failure as provenance corruption (Zmigrod, Garrison, Carr & Simons, Neurosci Biobehav Rev 2016)

## What the paper did

An activation-likelihood-estimation meta-analysis of functional neuroimaging studies of
hallucinations, covering both auditory-verbal and visual modalities. The modality-specific
findings are unsurprising and reassuring as a sanity check: auditory-verbal hallucinations
recruit auditory cortex along with Wernicke's and Broca's areas; visual hallucinations recruit
visual cortex. People hallucinate in the sensory machinery of the modality they hallucinate in.

The finding that matters for MECH-067 is the *cross-modality* one. Convergent across both kinds
of hallucination are the medial temporal lobe, the insula, and the **paracingulate region of
medial prefrontal cortex** -- the region independently implicated in reality monitoring, the
capacity to discriminate internally generated information from information that originated
outside. The authors' reading is that hallucination involves misattribution of self-generated
information as externally perceived, with sensory over-stimulation supplying the content and the
attribution failure supplying the error.

## Why a clinician might care about this for a write-permission matrix

Because it is the same bug.

Strip the psychiatry and the failure is: content produced internally, by a simulation, reaches a
store and is subsequently read back carrying the provenance of something that actually happened.
MECH-067's CONFIRMING clause names the machine version explicitly -- "hypothesis-tagged rollout
content reaching residue through a path that bypasses accumulate's flag" -- and the consequence
in both cases is identical in kind. Nothing about the *content* is corrupt. What is corrupt is the
attribution, and the store looks internally consistent while being wrong about where its contents
came from. That is the property that makes this failure so hard to detect from inside: the residue
field with contaminated content is a perfectly well-formed residue field, just as a hallucinating
patient's percept is a perfectly well-formed percept.

The second thing worth taking is the **modality-independence**. The brain does not appear to have
evolved a separate provenance gate for auditory memory and another for visual memory. The same
paracingulate region shows up for both. Architecturally that is one check spanning store classes,
not one gate per store -- which is exactly the shape MECH-067 proposes when it asks for a single
(phase, store, actor) matrix over typed store classes rather than the current arrangement of
locally-defended sites. Given the repo's stated preference for reasoning from biology before
formal definitions, that structural convergence is worth recording even though the evidential
weight is modest.

The medial temporal lobe finding adds a third note: memory intrusions participate in the
hallucinatory experience. Durable-store content re-entering the perceptual stream without its
provenance tag is, in REE's terms, exactly the pre-commit/post-commit confusion V1 EXQ-005 probed
from the other direction.

## Where the mapping strains -- and one way it cuts against the claim

Three strains, and I want to be direct that the first is not merely a caveat; it is a reason the
claim's own designers should think harder.

**Reality monitoring is retrieval-time, not write-time.** What this literature describes is an
attribution *judgement* made about content that is already present -- deciding, after the fact,
where something came from. MECH-067 proposes a write-time *gate*: preventing the content from
arriving mislabelled in the first place. Those are different architectures solving the same
problem at different points in the pipeline, and it is at least arguable that biology's choice of
the former is evidence *against* the necessity of the latter. Brains apparently found it cheaper
to tag and adjudicate than to mediate every write. If a governance cycle wanted to use this entry
against the claim rather than for it, that is the argument, and it is not a weak one. I have
recorded the direction as `supports` because the entry's principal contribution is the
store-spanning shared-check structure and the corruption signature, both of which fit MECH-067 --
but the timing mismatch should not be smoothed over.

**A convergent activation locus is not a permission matrix.** ALE tells you which voxels recur
across studies. It does not tell you that paracingulate cortex implements a default-deny policy
over anything; a shared locus is equally consistent with a shared heuristic monitor that is often
wrong, which -- given how common ordinary source-memory confusions are in healthy people -- may be
the better reading.

**Reverse inference.** Co-activation during hallucination does not establish that the region's
normal job is provenance checking. The convergence with the independent source-monitoring
literature (Simons, Garrison & Johnson 2017, *Trends Cogn Sci* 21:462-473, which reviews reality
monitoring across health and disease) makes the reading more than speculative, but it remains an
inference from where the blood went.

Standard ALE limitations apply on top: heterogeneous paradigms, small patient samples,
predominantly schizophrenia-spectrum populations, publication bias in the underlying studies.

## Confidence

0.45, the lowest in this directory and deliberately so. Source quality is respectable (0.75) --
a quantitative meta-analysis in a strong review journal. Mapping fidelity is the binding
constraint at 0.45, because retrieval-time attribution is not write-time mediation and for an
architectural claim I weight mapping fidelity hardest. Transfer risk is 0.6, the highest here:
clinical human neuroimaging to a tensor-based agent substrate is a long way to carry anything.

This entry earns its place as biological grounding for the *shape* of the claim -- a shared,
store-spanning provenance check whose failure corrupts attribution rather than content -- and not
as evidence for its truth. If it disappeared from the directory, the case for MECH-067 would be
essentially unchanged; what would be lost is the reason to believe the problem is worth solving at
all, which is that evolution bothered to solve it.
