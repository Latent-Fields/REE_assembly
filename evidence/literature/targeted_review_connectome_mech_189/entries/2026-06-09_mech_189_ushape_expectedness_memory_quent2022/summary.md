# Quent, Greve & Henson 2022 — The U-shaped relationship between memory and expectedness

According to PubMed. Source: Quent JA, Greve A, Henson RN. *Psychological Science* 33(12):2084-2097, 2022. [DOI](https://doi.org/10.1177/09567976221109134)

## What the paper did

Using immersive virtual reality, the authors placed 20 objects in a kitchen at locations that varied in how congruent they were with a kitchen schema, and tested memory for those locations. Across four preregistered experiments (137 adults), Bayes factors confirmed a U-shaped function: memory was better for *highly expected* and *highly unexpected* locations than for neutral ones. The pattern held in both recall and forced-choice recognition with expectancy-matched foils, ruling out a guessing-bias explanation. This is a direct test of the SLIMM (Schema-Linked Interactions between Medial prefrontal and Medial temporal regions) model, which predicts that both schema assimilation and prediction-error-driven encoding strengthen memory, while moderately-expected events fall into an encoding trough.

## Why it matters for MECH-189

This is the entry that most sharply constrains the *shape* of MECH-189's complexity gate, and the reason I lean against the current default. The substrate's `super_ordinal_complexity_mode="novelty"` computes `complexity = 1 - max cosine similarity to the goal-anchor keys` — a *monotonic* function: the more dissimilar the context, the higher the complexity, the more likely the write. Quent et al. show that the brain's encoding strength is *not* monotonic in expectedness. The most schema-*congruent* events are written as well as the most surprising ones; it is the *neutral middle* that is poorly encoded.

A monotonic novelty gate captures only the unexpected arm of the U. It would correctly write a high-value contact in a wildly novel context, but it would *fail to write* a high-value contact that fits an existing schema strongly — even though biology encodes that case well too. Conversely, it would happily write moderately-novel neutral contacts that biology treats as forgettable. The mismatch is structural, not a matter of threshold tuning.

The constructive reading is that an encoding signal driven by *prediction-error magnitude* — or a *signed* PE term that admits two write regimes (congruent assimilation vs incongruent encoding) — fits the data, and an external PE signal produces the unexpected-arm sensitivity automatically. MECH-189's own narrative ("adult routine contexts are low-complexity and do not trigger writes") corresponds to the *neutral trough*, which the U-shape vindicates — but only if "complexity" is reformulated away from raw dissimilarity.

## Limitations and caveats

This is object-location *episodic* memory in a spatial-schema VR task, not a cross-episode super-ordinal *goal/value* write. The U-shape is established for declarative item memory; whether value or goal anchors show the same nonmonotonicity is an inference, not a measured result. The transfer from a kitchen-schema task to abstract z_world/z_goal anchors is real risk, which is why I keep mapping fidelity at 0.62 and flag transfer risk at 0.45.

## Confidence reasoning

Confidence 0.7, direction `mixed`. The methodology is excellent — preregistered, Bayes-factor-quantified, replicated four times — so I trust the nonmonotonicity finding strongly. Its bearing on MECH-189 is to *weaken* the monotonic novelty-vs-anchors proxy and to *support* a prediction-error-magnitude formulation of gate (b). Lit confidence only; not blended into experimental confidence.
