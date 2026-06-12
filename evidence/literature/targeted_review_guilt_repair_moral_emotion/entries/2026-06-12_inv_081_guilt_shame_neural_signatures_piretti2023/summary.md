# Piretti et al. (2023) — The Neural Signatures of Shame, Embarrassment, and Guilt: A Voxel-Based Meta-Analysis

**Claims grounded:** INV-081 (no-global-self-badness write), ARC-097 (guilt-as-repair routing)
**Direction:** supports · **Confidence:** 0.70

*According to PubMed* ([DOI: 10.3390/brainsci13040559](https://doi.org/10.3390/brainsci13040559)).

## What the paper did

This is a quantitative, voxel-based meta-analysis of the functional-neuroimaging literature on the self-conscious emotions. The authors ran a systematic review and aggregated the activation coordinates from 34 task-fMRI studies of healthy adults — 17 investigating guilt and 17 investigating shame/embarrassment — to ask whether the two emotion families have *dissociable* neural substrates. Unlike a single fMRI study (which, at typical sample sizes of a dozen or two, is underpowered for this question), the meta-analytic approach pools across studies and stimuli, which is why I chose it over the available single-study pilots as the biology anchor for this cluster.

## Key findings relevant to the claim

The result is a *partial dissociation* with a functionally suggestive structure. Both guilt and shame/embarrassment engaged the **left anterior insula**, which the authors read as a shared substrate for emotional awareness and arousal — the two emotions are not neurally orthogonal. But the *specific* substrates diverged in a way that tracks their action tendencies. Guilt was associated with the **left temporo-parietal junction**, a hub of social-cognitive / mentalising processing — i.e., representing other minds. Shame/embarrassment recruited **social-pain** regions (dorsal anterior cingulate cortex and thalamus) together with a **premotor / behavioural-inhibition** network. The authors explicitly interpret this contrast as reflecting the distinct *action tendencies* of the two emotions: guilt's outward, other-directed, repair-relevant orientation versus shame's painful, inhibiting, withdrawal-oriented one.

## How it translates to REE

This is the neural-level corroboration of the design split that ARC-097 and INV-081 encode. The guilt branch carrying a *social-cognitive / other-modelling* signature is consistent with REE routing self-attributed harm toward a repair action defined over a represented other (ARC-097, and ultimately the other-directed repair target of MECH-411). The shame branch carrying a *behavioural-inhibition + social-pain* signature is consistent with the failure mode INV-081 is built to prohibit: a withdrawing, self-focused response rather than an action-binding one. Crucially, the meta-analysis supplies the kind of biology grounding the project's own `feedback_biology_before_formal_definitions` rule asks for — evidence that guilt-as-repair and shame-as-withdrawal are not just folk-psychological labels but partially distinct systems with different downstream action tendencies, which is the premise that makes routing them to *different* architectural pathways principled rather than arbitrary.

## Limitations and caveats

Three honest boundaries. First, the dissociation is *partial* — the shared anterior-insula activation means a synthetic design that treats guilt and shame as cleanly separate streams overstates the neural evidence. Second, the analysis pools shame *with embarrassment*, which is considerably less morally loaded; the "shame" signature is therefore not a pure index of the moral global-self-condemnation that INV-081 specifically targets. Third, and most fundamental for a literature-to-architecture mapping: meta-analytic neuroimaging localises activation foci and assigns them functional labels by reverse inference. It does not measure the self-attribution-to-action computation REE prescribes, and the transfer from human haemodynamic maps to a synthetic E3/self-model is an analogy of *function*, not of mechanism.

## Confidence reasoning

I set confidence at 0.70. Source quality is good — a quantitative meta-analysis aggregating 34 studies is materially stronger than any single underpowered fMRI run. I hold mapping fidelity to moderate because the dissociable signatures corroborate the two-branch *design* but the reverse-inference labelling, the partial overlap, and the shame+embarrassment pooling all dilute the specific mapping to INV-081's exact target. The human-fMRI-to-synthetic-architecture transfer keeps the aggregate in the upper-moderate band, on par with the Weiner theoretical anchor and a notch below the Tangney review.
