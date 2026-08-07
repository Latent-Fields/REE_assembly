# Nuiten et al. 2024 — Catecholamine Elevation Improves Perceptual Decisions, Not Metacognition

**Claim tested:** ARC-005 ("Control plane routes precision and modes")
**Direction:** mixed · **Confidence:** 0.70

## What the paper did

A double-blind, placebo-controlled crossover in 27 healthy adults. Participants performed a visual discrimination task with confidence ratings under three drug states: atomoxetine (a noradrenergic reuptake blocker, elevating catecholamines), donepezil (a cholinesterase inhibitor, elevating acetylcholine), and placebo, with concurrent EEG. Atomoxetine is, functionally, a direct manipulation of the noradrenergic gain channel — the biological cousin of stepping REE's precision channel along its ladder.

## The number this review was commissioned to find

According to PubMed / eNeuro, atomoxetine improved perceptual sensitivity **d' with a Cohen's d of 0.39** (t(26) = 2.06, p = 0.02) — a small-to-medium effect. Crucially, the effect was *readout-specific*: metacognitive sensitivity (meta-d') was **unaffected** (d = 0.16, Bayes factor BF01 = 3.55 favouring the null), and neurally the drug enhanced centroparietal evidence-accumulation signals while leaving early sensory representations and impoverishing frontal metacognitive markers.

This is the empirical yardstick for the ARC-005 sub-question. A noradrenergic precision/gain manipulation moves a downstream behavioral readout by **~0.39 standard deviations** of the cross-condition variance. The commensurable REE quantity is its effect-over-cross-seed-SD ratio, which is ~1e-3 / 0.18 ≈ **0.006** — i.e. REE's channel-1 footprint is roughly **65× smaller** than this biological benchmark. Because Cohen's d *is* effect divided by SD, and REE's reported ratio is the same construction, the 0.39-vs-0.006 comparison is genuinely apples-to-apples on the standardized scale even though the raw units differ.

## Why this is "mixed" and not simply "supports"

It cuts both ways for ARC-005, honestly. It *supports* the core claim that a control-plane channel routes a real, causal downstream effect (atomoxetine's d' effect is real and neurally specific). But it simultaneously supplies the yardstick that makes REE's own result look anomalous: the biology predicts a precision channel manipulation should produce a fifth-to-a-half-SD downstream footprint, not one ~180× below noise. The readout-specificity is also double-edged — it vindicates REE's expectation that channel 2 is architecturally null (precision manipulations have localized footprints), but it gives no cover to channel 1, whose footprint is ~2 orders of magnitude below any biologically detectable effect. On balance this is evidence that REE's channel-1 implementation is *underperforming a functioning biological precision channel*, i.e. it favours the undertrained-dACC-adapter reading (848a: the adapter never trained on non-degenerate goal_proximity, response 4–7 orders of magnitude off scale) over a genuine biological ceiling.

## Caveats I am keeping in view

Atomoxetine 40 mg is a supra-physiological pharmacological push and likely an *upper* bound on what a within-normal-range channel step would elicit — but even discounting it heavily cannot close a 65× gap. The sample is small (N=27) and male-only, which is why source_quality sits at 0.75. And the underlying readouts differ (visual-discrimination d' vs an E3 log10-precision readout); the defence is that the *ratio* is the transfer-invariant quantity, not the raw units.

*According to PubMed. Nuiten SA, de Gee JW, Zantvoord JB, Fahrenfort JJ, van Gaal S. eNeuro 2024;11(7). [DOI](https://doi.org/10.1523/ENEURO.0019-24.2024)*
