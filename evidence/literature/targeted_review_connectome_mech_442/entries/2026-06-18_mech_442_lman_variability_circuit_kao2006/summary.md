# Kao & Brainard 2006 -- a basal-ganglia circuit that generates and regulates behavioral variability, separate from the motor output

*According to PubMed.* Kao & Brainard 2006, *Journal of Neurophysiology* ([DOI](https://doi.org/10.1152/jn.01138.2005)).

## What the paper did
The authors asked where the trial-to-trial variability of adult birdsong comes from, and whether it is regulated. Adult zebra finches sing more variably alone (undirected) than to a female (directed). They lesioned LMAN -- the output nucleus of the anterior forebrain pathway (AFP), an avian basal-ganglia-forebrain circuit -- and measured moment-by-moment variability of syllable structure. LMAN lesions reduced undirected-song variability to the directed-song level and abolished the social modulation of that variability, immediately and durably, while leaving sequencing, motif counts, and motivational aspects of courtship intact.

## Key findings relevant to MECH-442
The convergence-relevant point is a clean dissociation: the variability is not noise leaking through the motor pathway; it is actively *generated and regulated* by a dedicated basal-ganglia circuit that sits in parallel with the premotor output. Remove that circuit and the behavior keeps working -- it just stops being variable. This is the biological shape of "diversity is a maintained property with its own substrate," which is the necessity MECH-442 rests on. Crucially, the variability-generating structure is *separate from* the selection/output machinery -- it is not a property of the motor argmax itself.

## How it translates to REE
This favors locating MECH-442's diversity-preserving structure on the candidate-pool / generation side (ARC-065) and a dedicated variability mechanism (MECH-313 noise floor), rather than asserting a per-niche-elite store living at the committed argmax. In REE terms: the brain keeps a separate "variability injector" coupled to selection, not a behavioral-descriptor archive read by the value-maximizer per niche. That is a meaningful refinement of the MAP-Elites adapter -- the archive is upstream of / parallel to the commit, and the F-dominated argmax (MECH-439) is the *output*, not the place diversity is stored.

## Limitations and confidence
LMAN regulates variability of syllable *structure* but not *sequencing* -- the variability circuit is content-specific, so no single "behavioral-descriptor archive" cleanly covers all behavioral axes. And a songbird vocal-motor system is an analogy, not a homology, for an E3 trajectory-selection locus. The lesion logic is strong and the system is canonical, so source quality is high; mapping fidelity is moderate because the evidence speaks to a *generator separate from selector*, which is adjacent to but not identical with MECH-442's per-niche-elite proposal. Net confidence 0.74, direction supports (with the explicit caveat that it supports the generation-side reading more than the at-argmax archive reading).
