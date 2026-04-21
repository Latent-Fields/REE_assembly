# SD-011 Context-Stability Synthesis — 2026-04-21

## Focused question

Does the sensory-discriminative (A-delta / S1-S2) vs affective-motivational (C-fiber / ACC-insula) nociceptive dissociation SURVIVE environmental/context change, and on what timescale? Can the dual-stream architecture be cited as stable across task conditions, or does it require per-context re-training?

## Four entries in this pull

1. **Apkarian, Hashmi & Baliki (2011), Pain** — chronic pain as extreme sustained-context perturbation. Direction: mixed (0.72). Anatomical substrates persist; functional engagement and downstream integration drift.
2. **Baliki, Mansour, Baria & Apkarian (2014), PLoS One** — DMN reorganization across three chronic pain conditions. Direction: mixed (0.68). Insula acquires novel mPFC/DMN couplings under sustained noxious context, scaling with pain intensity.
3. **Bouton & Todd (2014), Behavioural Processes** — fundamental role of context in instrumental learning and extinction. Direction: mixed (0.60). Proxy for Bouton 2004. Affective/motivational learning is context-bound; renewal effects imply z_harm_a's behavioural meaning is context-response-gated.
4. **Strigo & Craig (2016), Phil Trans R Soc B** — interoception, homeostatic emotions, sympathovagal balance. Direction: supports (0.75). Interoceptive architecture is stable across affective states; bivalent feelings encoded as asymmetric activation patterns on a stable substrate, not through reorganization.

## Bottom-line synthesis

The SD-011 dual-stream architecture — z_harm_s (A-delta/S1, sensory-discriminative, forward-predictable) and z_harm_a (C-fiber/medial-thalamic/ACC-insula, affective-motivational, integrative) — is **architecturally stable across context change**. No paper in the pull provides evidence that the two streams merge, swap, or reorganize into different configurations as context changes. The Strigo & Craig synthesis makes this claim explicit: interoceptive architecture is fixed; context-dependent feeling states are encoded as asymmetric activation patterns on the stable architecture, not as architectural reorganization.

**However, the downstream integration of z_harm_a is plastic under sustained context.** Apkarian 2011 and Baliki 2014 show that under chronic noxious context, the insular stream acquires novel couplings with mPFC, NAc, and DMN components that are weak or absent in acute contexts. Bouton 2014 provides the complementary principle from operant learning: the behavioural meaning of "this context is dangerous" is encoded as context-response inhibitory associations, not as context-free valuations.

**Implications for SD-011 implementation:**

1. The dual-stream encoder architecture itself should be fixed — not dynamically reorganizing per context. This matches Daniel's existing implementation note (HarmEncoderS and HarmEncoderA as distinct fixed modules trained on distinct targets, both receiving the same harm_obs input).

2. z_harm_s should be context-robust by construction because it tracks physical regularities (stimulus proximity as predicted from action). The E2_harm_s forward model (ARC-033) relies on z_harm_s's context-stability for SD-003 counterfactual attribution to transfer across contexts — this is supported by the lit.

3. z_harm_a's downstream consumers should be treated as context-plastic. ARC-016 harm-variance gating should be context-conditional rather than fully pre-wired. Under sustained high-harm exposure, additional downstream modules may start coupling to z_harm_a — this is predicted, not pathological (within a limit; unlimited coupling drift would be chronic-pain-analogue).

4. E3's use of z_harm_a for avoidance learning should implement context-response bindings (per Bouton), predicting renewal effects: after training avoidance in one context and "extinguishing" in another, return to the original context should partially renew avoidance strength. This is testable in V3 and currently not in the queue.

**Timescale note.** All the context-stability evidence is at timescales longer than V3 experiments operate at. Chronic pain reorganization unfolds over months to years; Bouton's paradigms involve many dozens of trials per context; Strigo & Craig's synthesis spans the broad architectural question without specifying timescales. On V3's episode-level timescales (seconds to minutes), the architectural-stability claim should hold a fortiori, but short-timescale plasticity of downstream integration is not directly tested.

**Confidence calibration.** The existing SD-011 folder already has the foundational dual-pathway grounding (Melzack & Casey, Craig 2002, Rainville 1997, Price 1987, Willis 1997, Basbaum 2009). This pull adds the context-stability layer: the architecture is stable, the downstream couplings are plastic. Net literature support for SD-011 as written is strengthened; one implementation nudge (treat z_harm_a downstream as context-gated rather than fixed) is newly licensed.

## Direction distribution

- supports: 1 (Strigo & Craig)
- mixed: 3 (Apkarian, Baliki, Bouton)
- weakens: 0

The "mixed" direction reflects genuine two-sidedness: architectural stability is supported, but implementation naivety (treating z_harm_a integration as fixed) would be weakened. The pull does not contradict SD-011; it refines what "stable dual-stream" should mean for V3 implementation.
