# Baliki, Mansour, Baria & Apkarian (2014) — Functional reorganization of the DMN across chronic pain conditions

## What the paper does

Baliki and colleagues acquire resting-state fMRI in three clinically distinct chronic pain populations (chronic back pain, complex regional pain syndrome, knee osteoarthritis) and in healthy controls, decompose the data into canonical resting-state networks via ICA, and ask whether any of the networks show disease-general reorganization. Only the default mode network does. Specifically: medial prefrontal cortex shows reduced connectivity with posterior DMN components and increased connectivity with insular cortex, scaling with pain intensity; mPFC also shows elevated high-frequency oscillations and reduced phase-locking with parietal attention regions. Some effects scale with pain duration.

## Key findings relevant to SD-011 context-stability

This paper is one of the cleanest tests in the literature of whether the insular/affective stream's downstream integration is fixed across contexts. The finding is that it is not. In chronic pain context, insula acquires a novel coupling with mPFC (and through it, DMN) that is weak or absent in healthy controls and in the acute pain literature. The coupling strength scales with the intensity of the sustained noxious context. The magnitude of the effect is substantial and is replicated across three clinically distinct pain syndromes, which is strong evidence that it is not condition-specific but reflects a general consequence of sustained nociceptive context.

For SD-011 the reading is two-sided. On the one hand, the insula remains identifiable across all conditions — it does not merge with S1 or disappear. The structural separation of z_harm_s and z_harm_a is preserved. On the other hand, z_harm_a's downstream consumers are shown to be context-plastic: new coupling partners appear under sustained context. This complicates any SD-011 implementation that wires z_harm_a to a single fixed downstream module.

## How this translates to REE

The architectural implication is calibration rather than refutation. SD-011 should treat z_harm_a's downstream integration as gated by a context/drive signal rather than fixed — under sustained high-drive conditions, additional downstream modules can recruit z_harm_a. This is compatible with how ARC-016 harm-variance gating was already designed (precision-weighted consumption), but extends the principle: the set of modules that consume z_harm_a should itself be context-dependent, not just the weighting on a fixed consumer.

More concretely: if a V3 experiment sustains high harm exposure over many episodes, one would predict that mPFC-analogue modules (e.g. goal-state maintainers, drive regulators) that were not originally coupled to z_harm_a should start showing stronger coupling. This is testable in V3 via cross-episode connectivity tracking, though not a current queue item.

## Limitations and caveats

The paper studies chronic patients at rest, not acute nociception across context shifts. It therefore cannot distinguish between "sustained pain context reorganizes z_harm_a integration" and "patients who develop chronic pain have pre-existing atypical z_harm_a integration." Cross-sectional designs with clinical cohorts are always vulnerable to this. Sample sizes are modest (10-16 per group). The effect correlates with pain duration in some cohorts, which supports the causal reading, but the timescales (months to years) are far from V3 experimental timescales (seconds to minutes).

## Confidence reasoning

I put this at 0.68 — mid-range. The paper is the best direct empirical test of z_harm_a downstream integration stability under sustained context that I could find in one pull, and it replicates across three conditions, which is a strong design feature. But the inferential chain from "resting-state DMN reorganization in clinical chronic pain" to "SD-011 z_harm_a consumers are context-plastic" is not short. The honest reading is: this paper provides moderate evidence that the SD-011 architecture should allow z_harm_a integration to drift with context, and clearly supports the claim that z_harm_s and z_harm_a do not merge even under extreme context perturbation.
