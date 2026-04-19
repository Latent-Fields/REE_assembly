# Pain predictive-coding substrate: do E2_harm_a and E2_harm_s share substrate?

**Pull date.** 2026-04-19
**Claim targets.** MECH-258 (precision-weighted pain PE against E2_harm_a), SD-032b (dACC/aMCC-analog consuming that PE).
**Entries.** 9 (1 canonical + 5 empirical fMRI/EEG + 1 computational model + 2 reviews).

## The question

Should the REE implementation keep `E2_harm_a` (affective-pain forward model, predicting z_harm_a) and `E2_harm_s` (sensory-discriminative-pain forward model, predicting z_harm_s) as:

- **(a) Shared substrate** -- one common trunk with stream-specific heads,
- **(b) Parallel but separate** -- two independent modules with no shared parameters, or
- **(c) Inconclusive** -- ship (b) because it is simpler and revisit?

The question bears directly on compute cost, sample efficiency, and whether the internal model has a coherent "pain" latent that precedes its split into sub-streams.

## What the biology says

The nine entries in this pull, taken together, support a specific architectural shape:

1. **Consumers are parallel.** Posterior insula encodes stimulus intensity (sensory-discriminative). Anterior insula integrates expectations with sensory input (predictive coding). They are not the same region doing both jobs (Geuter 2017, Fazeli 2018, Sharvit 2019, Ploghaus 1999).

2. **Signed prediction errors are modality-specific.** Horing 2022 is the single most informative entry: unsigned PE (a shared magnitude-of-surprise signal) is modality-independent in anterior insula; signed PE (direction information the consumer uses for learning) is modality-specific, with a pain-only signed PE in dorsal posterior insula. This is the shape of "shared trunk, per-stream heads".

3. **The predictive machinery is pain-indexed, not generic aversiveness.** Fazeli 2018 rules out a shared predictor pooling over all aversive modalities. Whatever E2_harm_a predicts, it predicts pain, not a pooled negative-affect signal. Sharvit 2019 generalises this: the anterior insula maintains sensory-specific prospective models, one per aversive modality, in the same anatomy.

4. **S1 and ACC are coupled but distinct populations in computational-model fits.** Song et al. 2021 built a biophysical predictive-coding model with explicit S1 (sensory-discriminative) and ACC (affective) populations plus coupling terms, fit to rat LFPs in naive and chronic-pain animals. The model needs two populations and a coupling, not one unified population and not two fully independent populations. This is the closest direct analog to REE's proposed E2_harm_s + E2_harm_a architecture.

5. **The whole network operates as a hierarchical generative model.** Chen 2023 argues explicitly for hierarchical predictive coding across the cingulate-insula network. Under that framing, fully independent per-subdivision forward models are unparsimonious: if the network is running one hierarchical inference, the forward predictors share upstream structure.

6. **Precision-weighting is modality-crossing but stream-sensitive.** Habermann et al. 2024 and Strube et al. 2021 both show that precision effects (controllability, expectation strength) modulate pain PE computation in a way that interacts with the predictive coding substrate. A precision signal applied at the trunk level is biologically plausible; applying it independently to two unconnected forward models is less parsimonious.

## Corollary discharge?

The user asked specifically about corollary-discharge-like cancellation in nociception. The search returned essentially nothing direct (only one 2000 cat-decerebrate paper, Steffens et al., on rubrospinal nociceptive integration -- relevant to sensorimotor control, not to predictive cancellation of self-produced pain). This is a literature gap. The active-inference framing (Chen 2023, Habermann 2024) treats pain reduction via control as precision-weighted expectation, not as corollary-discharge cancellation in the classical sense. If there is a cancellation mechanism for self-produced nociception, it has not surfaced in recent predictive-coding work at a resolvable level. For REE: do not commit to corollary-discharge-style cancellation for z_harm; use precision-weighted expectation instead.

## Recommendation

**(a) Shared substrate with stream-specific heads.** **Confidence: 0.75.**

The weight of evidence favours a common expectation-generating trunk with per-stream (affective, sensory-discriminative) heads over either option (b) fully independent modules or (c) inconclusive-so-ship-parallel. Key reasoning:

- Horing 2022's unsigned/signed PE decomposition is the architectural fingerprint of shared-trunk + stream-specific-head.
- Song 2021's computational model that fits the rat LFP biology uses coupled-not-independent populations.
- Sharvit 2019 names the architecture explicitly at the sensory-modality level (pain-vs-disgust) in the same region; the within-pain extrapolation is by analogy but consistent.
- Chen 2023's hierarchical framing makes independent forward models structurally unparsimonious.
- Fazeli 2018 disallows a generic aversive trunk pooling across modalities -- but that constrains the trunk to be pain-indexed, not to be split per sub-stream.

**Implementation translation.** Build `E2_harm` as a single forward model with:
- one shared encoder/trunk consuming a pain-family context signal,
- two heads: `head_s` (predicting z_harm_s) and `head_a` (predicting z_harm_a),
- per-head precision-weighted PE outputs (MECH-258 applies per-head).

MECH-258's functional_restatement already describes this ("E2_harm_a shares substrate with E2_harm_s (ARC-033) -- same forward model architecture, different input stream"); this lit pull vindicates that choice and sharpens it: not merely same architecture, but same trunk with different heads.

**Why not (b).** Two fully independent modules would miss the biology's parsimony (one shared surprise computation in anterior insula), would ignore Song 2021's coupling term, and would cost twice the parameters for little expected gain.

**Why not (c).** The literature is not sparse; it is consistent. A decision is defensible on these grounds.

## Confidence caveats

- No empirical paper in the corpus directly compares within-pain A-delta vs C-fiber forward models; the extrapolation rests on analogies from between-modality (pain-vs-disgust, pain-vs-sound) and from the S1-vs-ACC dissociation.
- Rodent data (Song 2021) does not tile one-to-one with human fMRI data (Geuter, Fazeli, Horing); I treat the convergence as supportive rather than proof.
- Corollary-discharge mechanisms for self-produced nociception are a literature gap. If REE wants the "agent as cause of its own pain" signal, that must come from SD-003-like counterfactual attribution, not from a cancellation mechanism built into E2_harm.

## Strongest single entry

Horing & Buchel 2022, PLoS Biology ([DOI](https://doi.org/10.1371/journal.pbio.3001540)) -- the unsigned/signed PE decomposition across modalities is the architectural fingerprint of option (a).
