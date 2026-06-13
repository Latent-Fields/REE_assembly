# Amygdala-modulated consolidation as the biology of affect-as-write-weight

**McGaugh (2004), *Annual Review of Neuroscience* 27:1-28. [DOI](https://doi.org/10.1146/annurev.neuro.27.070203.144157)** (PMID 15217324).
Claims grounded: **MECH-361** (primary), **MECH-368** (secondary). *According to PubMed.*

## What the paper does

McGaugh reviews three decades of convergent animal and human evidence for one mechanism: the **basolateral amygdala (BLA) modulates how strongly a memory is consolidated**, as a function of emotional arousal. The causal animal work is the backbone — posttraining (i.e. *after* the experience, during the consolidation window) systemic or intra-amygdala infusions of adrenal stress hormones and neurotransmitters, and selective BLA lesions, bidirectionally raise or lower how well the experience is later remembered. The effect converges on noradrenergic and muscarinic-cholinergic activation within the BLA, and the BLA exerts it via projections to caudate, nucleus accumbens, and cortex — it modulates consolidation of *many* memory types rather than storing the memory itself. Human fMRI dovetails: the degree of amygdala activation while encoding arousing material predicts later recall.

## Why it grounds MECH-361 and MECH-368

MECH-361's core seam is **affect as a memory write-weight** — high-affective-gradient episodes are preferentially written and written more deeply. McGaugh's review is the direct biological mechanism for that seam. "Posttraining BLA manipulation bidirectionally scales subsequent memory strength" *is* "affect sets write depth," stated in neurochemistry. This is exactly the upgrade MECH-361 makes on REE's existing MECH-074 (BLA arousal-modulated hippocampal write depth): the claim that the affect signal is a *write-weight*, not merely a retrieval cue, is what this paper licenses.

For MECH-368 the relevance is narrower but real. MECH-368's event-level write-authority gate is conditioned on `f(prediction_error, salience, ..., plasticity_eligibility)`. McGaugh grounds the **salience/affect input** to that function: emotionally salient events are biologically privileged for durable write. The gate idea — that not every event writes equally, and an affect/arousal signal arbitrates — is the abstraction of the BLA modulation story.

## Where the mapping strains (honest boundary)

Two gaps, both recorded as `failure_signatures`.

First, the amygdala modulates a largely **scalar arousal magnitude** — how emotionally intense the episode was. MECH-361 asks for something finer: a **per-candidate affective gradient**, a vector over the options *considered* during deliberation, used as the write-weight. The candidate-differentiation is MECH-361's actual novelty, and it is `substrate_conditional` on the off-plan MECH-359 affect substrate. McGaugh grounds "affect scales write strength"; he does not ground "the *gradient across candidates* is the write-weight." That is the part still owed evidence.

Second, BLA modulation acts on **episodic/declarative and procedural consolidation** — the memory write path. MECH-368's genuinely under-covered target is the **durable world-model / policy weight-update** path (E1/E2 weights), not episodic memory. So McGaugh supports the *principle* (salience gates durable write) on the path where REE already has coverage, and the transfer to the model-update path is by analogy, not evidence.

## Confidence

0.76, `supports`. Source quality near-ceiling — the originator's field-defining review, with strong causal animal pharmacology and converging human imaging. The discount is mapping fidelity: arousal-magnitude vs candidate-gradient, and episodic-write vs model-update path. The shared core — affect is a write-weight, not just a cue — is solidly grounded for both claims. Raises literature_confidence only; promotes nothing (both claims V4, `substrate_conditional`).
