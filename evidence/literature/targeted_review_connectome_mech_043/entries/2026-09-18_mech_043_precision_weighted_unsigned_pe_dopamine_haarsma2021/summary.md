# Precision weighting of cortical unsigned prediction error signals benefits learning, is mediated by dopamine, and is impaired in psychosis

Haarsma, Fletcher, Griffin, Taverne, Ziauddeen, Spencer, Miller, Katthagen, Goodyer, Diederen & Murray (2021), *Molecular Psychiatry* 26(9):5320-5333. DOI [10.1038/s41380-020-0803-8](https://doi.org/10.1038/s41380-020-0803-8) · PMID 32576965 · PMC8589669

**Claim tested:** MECH-043 — *Dopamine-like modulation of precision-weighting for unsigned prediction errors.*
**Direction:** supports (confidence 0.86)

## What the paper did

Two human studies, run under the hierarchical-Bayesian framing that the brain weights prediction errors by their precision. The first is a between-subject pharmacological fMRI study (n = 59 healthy volunteers) with placebo, the D2 agonist bromocriptine, or the D2 antagonist sulpiride, performing a probabilistic learning task whose outcome precision was varied block-by-block. The second is a clinical study (n = 74: 20 first-episode psychosis, 30 controls, 24 at-risk mental state) on the same paradigm, with a further schizotypy correlation in 86 healthy volunteers. Critically, the design separates *unsigned* prediction error — surprise magnitude, no valence — from *signed* prediction error, and asks whether each is scaled by outcome precision.

The headline result is a conjunction rather than a single effect. Precision-weighted unsigned prediction error was coded in superior frontal cortex, and this replicated across the two independent samples (combined n = 133). That signal was perturbed by dopaminergic manipulation in both directions, was impaired in first-episode psychosis, and covaried with task performance and with schizotypy. Behavioural computational modelling showed that taking outcome precision into account benefits learning in health and that patients fail to do so.

## How this translates to REE

MECH-043 asserts that REE's precision term is the functional analogue of a dopamine-modulated precision channel and — the load-bearing half — that it is specific to *unsigned* error magnitude rather than to signed value. In `ree_core/predictors/e3_selector.py`, `current_precision` is `1.0 / (running_variance + 1e-6)`, where `running_variance` is an EMA over squared prediction error. It is unsigned by construction; no valence information can reach it. This paper is the closest thing in the human literature to a direct existence proof for that conjunction: precision applied to an unsigned surprise signal, with the gain under dopaminergic control.

The more interesting contribution is to the falsifiers. MECH-043's falsifier (i) is that the computation incorporates signed/valence information, and falsifier (iv) is that the effect is fully explained by a shared precision-scale parameter also governing MECH-054's signed channels identically. Haarsma et al. cut in the direction MECH-043 needs on both: the dopamine-sensitive precision effect they find is on the *unsigned* channel, and — candidly reported — they failed to replicate their own earlier finding of precision-weighted *signed* PE in midbrain and ventral striatum. That is a dissociation in the right direction, though it is a null rather than a demonstrated double dissociation, and it should be read with the caution a non-replication deserves. Falsifier (ii), collapse into a scalar reward objective, is likewise not met: the modelled quantity is an inverse-variance weight on surprise, not a reward scalar.

## Limitations and caveats

Three boundaries matter, and I would not want the mapping to be read more strongly than it is.

First, the two "precisions" are not the same object. Theirs is an estimate of *outcome* precision supplied by the task's generative structure and inferred by a Bayesian learner; REE's is a running EMA of its own squared prediction error — a self-generated reliability estimate, not an estimate of an externally-set noise level. These coincide only when the agent's error variance tracks true environmental variance, and REE has not shown that it does. This is the main reason mapping fidelity sits at 0.82 rather than higher.

Second, the anatomy points somewhere REE does not. The effect is in superior frontal cortex, not midbrain or striatum, while REE wires `current_precision` into the E3 commitment gate and dACC affective-PE weighting. The paper does not license any claim about which REE module is the correct homologue, and an implementation that ties its dopamine-like precision channel to a striatal selection locus is not supported by this result.

Third — and this is the real gap — the study measures a learning benefit and a clinical contrast, not a hallucination-like dependent variable under a gain sweep. MECH-043's CONFIRMING condition asks for an ablation or sweep of this channel's gain producing a measured increase in hallucination-like output attributable to *this* channel specifically, isolated from ARC-108/109 and MECH-054. This paper supports the channel's existence and its dopamine dependence. It does not close the behavioural half, and no amount of literature will: that half is an experiment REE has to run.

One further note for calibration. Dopaminergic modulation perturbed the signal rather than scaling it monotonically. If a REE sweep is designed on the assumption that more dopamine-like gain yields more precision in a clean linear fashion, the biology here does not obviously back that assumption — an inverted-U is at least as consistent with the data.
