# REE Evidence Map (Neuroscience Anchors)

Lightweight mapping from REE architecture prompts to empirical anchors. These are not direct anatomical claims; they are
biological evidence points that inform constraints and plausibility.

---

## P1 — Hippocampal rollouts (explicit trajectories)
Evidence: Hippocampal place-cell sequences replay in sleep and waking and can depict future paths to goals.  
REE implication: Support for hippocampus as the explicit multi-step rollout generator.  
Sources: [Wilson & McNaughton 1994](https://pubmed.ncbi.nlm.nih.gov/8036517/), [Foster & Wilson 2006](https://pubmed.ncbi.nlm.nih.gov/16474382/), [Pfeiffer & Foster 2013](https://pubmed.ncbi.nlm.nih.gov/23594744/).

## P2 — Post-commitment viability mapping
Evidence: Replay occurs immediately after experience and is temporally structured, consistent with updating a path model after execution.  
REE implication: Hippocampus can update a viability map from executed trajectories without being a value optimizer.  
Sources: [Foster & Wilson 2006](https://pubmed.ncbi.nlm.nih.gov/16474382/), [Wilson & McNaughton 1994](https://pubmed.ncbi.nlm.nih.gov/8036517/).

## P3 — Selection and gating of action
Evidence: Basal ganglia direct/indirect pathways modulate action initiation and suppression; pathways co-activate during action.  
REE implication: E3-style selection can be interpreted as a gating mechanism rather than a value module.  
Sources: [Kravitz et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20613723/), [Cui et al. 2013](https://pubmed.ncbi.nlm.nih.gov/23354054/).

## P4 — Precision/arousal control (control-plane analogue)
Evidence: Locus coeruleus (LC) activity correlates with attention and performance fluctuations in cognitive tasks.  
REE implication: Precision and gain control can be modeled as state-dependent tuning rather than representational content.  
Sources: [Aston-Jones et al. 1994](https://pubmed.ncbi.nlm.nih.gov/8027789/), [Usher et al. 1999](https://pubmed.ncbi.nlm.nih.gov/9915705/).

## P5 — Self-impact attribution (efference copy / reafference)
Evidence: Self-generated tactile sensations are centrally canceled via prediction of sensory consequences.  
REE implication: SELF_SENSORY vs WORLD separation and SELF_IMPACT comparison are biologically grounded.  
Sources: [Blakemore et al. 1998](https://pubmed.ncbi.nlm.nih.gov/10196573/).

## P6 — Prediction-error signaling (predictive coding)
Evidence: Cortical circuits can be modeled as top-down predictions with feedforward error residuals.  
REE implication: Prediction vs prediction-error channels are a viable architectural primitive.  
Sources: [Rao & Ballard 1999](https://pubmed.ncbi.nlm.nih.gov/10195184/).

## P7 — Reward prediction error signals (dopamine)
Evidence: Dopamine neurons encode errors in reward prediction and timing during learning.  
REE implication: Reward-like signals are naturally emergent prediction-error channels, not required as explicit objectives.  
Sources: [Hollerman & Schultz 1998](https://pubmed.ncbi.nlm.nih.gov/10195164/), [Bayer & Glimcher 2005](https://pubmed.ncbi.nlm.nih.gov/15996553/).

## P8 — Mirroring for action understanding
Evidence: Premotor neurons respond both to performed actions and observed actions.  
REE implication: Mirror modeling can reuse self representations for other-agent inference.  
Sources: [Gallese et al. 1996](https://pubmed.ncbi.nlm.nih.gov/8800951/), [Rizzolatti et al. 1996](https://pubmed.ncbi.nlm.nih.gov/8713554/).

## P9 — Empathy via shared affective components
Evidence: Observing another’s pain engages affective pain circuitry without primary sensory pain activation.  
REE implication: Empathy coupling can weight inferred other-harm without full sensory equivalence.  
Sources: [Singer et al. 2004](https://pubmed.ncbi.nlm.nih.gov/14976305/).

## P10 — Joint attention as developmental anchor
Evidence: Infants reliably follow gaze and coordinate visual attention with adults early in development.  
REE implication: Joint attention can be treated as a precursor to language and coordination pressure.  
Sources: [Scaife & Bruner 1975](https://www.nature.com/articles/253265a0).

## P11 — Language as emergent coordination
Evidence: Iterated learning experiments show language structure emerges from transmission pressure.  
REE implication: Language can be modeled as a compression/coordination layer without new cognitive primitives.  
Sources: [Kirby et al. 2008](https://pubmed.ncbi.nlm.nih.gov/18667697/).

## P12 — Papez-like provenance gating / confabulation
Evidence: The Papez circuit is a memory-related loop linking hippocampus, fornix, mammillary bodies, anterior thalamus,
cingulate gyrus, and entorhinal cortex. Confabulation is characterized as a memory disorder involving failure of
reality filtering (suppression of currently irrelevant memory traces).  
REE implication: A Papez-like loop can be treated as a provenance gate that withholds high-precision commitment unless
trace/ordering support exists.  
Sources: [NCBI Bookshelf: Papez circuit overview](https://www.ncbi.nlm.nih.gov/books/NBK575732/), [Papez circuit MRI anatomy (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10569190/), [Schnider 2003, Nat Rev Neurosci](https://www.nature.com/articles/nrn1179), [Schnider & Ptak 1999, Nat Neurosci](https://www.nature.com/articles/nn0799_677).

## P13 — Arcuate fasciculus and language pathways
Evidence: Comparative DTI shows a prominent temporal projection of the human arcuate fasciculus that is much smaller or
absent in nonhuman primates. Language is best described as a dual dorsal–ventral system, with dorsal streams supporting
sensorimotor mapping and ventral streams supporting comprehension; conduction aphasia data suggest the arcuate is
important but not sufficient alone.  
REE implication: a dorsal‑style sequence → motor channel is a useful nudge for language emergence, but the system should
remain distributed rather than relying on a single tract analog.  
Sources: [Rilling et al. 2008, Nat Neurosci](https://www.nature.com/articles/nn2072), [Hickok & Poeppel 2007, Nat Rev Neurosci](https://www.nature.com/articles/nrn2113), [Bernal & Ardila 2009, Brain](https://academic.oup.com/brain/article/132/9/2309/359715).

---

## Notes

- These anchors suggest constraints and plausibility, not direct one-to-one anatomy.
- Conflicting evidence should be logged as explicit conflicts if it challenges a canonical claim.
