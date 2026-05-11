# Q-044 Lit-Pull Synthesis — MECH-314a/b/c sub-flavour independence

**Claim under review.** Q-044: Are MECH-314a (striatal novelty), MECH-314b (frontopolar uncertainty-driven curiosity), and MECH-314c (learning-progress curiosity) three distinct substrates with independent contributions, or three different readings of one mechanism with different upstream inputs?

**Anchor set.** Five papers: Wittmann et al. 2007 (SN/VTA novelty anchor for 314a); Daw et al. 2006 (frontopolar uncertainty anchor for 314b); Kaplan & Oudeyer 2007 (learning-progress anchor for 314c); Friston et al. 2015 (unification thesis); Schulz & Gershman 2019 (algorithmic-architecture review).

**Aggregate.** Four supports + one mixed. Indexer-derived lit_conf will be in the 0.65–0.75 range. Evidence quadrant expected: `plausible_unproven` (high lit, low exp).

---

## R1 — Is MECH-314a (striatal novelty) substrate-distinct from MECH-314b (frontopolar uncertainty)?

**Verdict.** **SUBSTRATE-LEVEL SEPARATION SUPPORTED.** Wittmann 2007 localises novelty-anticipation to SN/VTA + hippocampus (a dopaminergic-midbrain circuit). Daw 2006 localises uncertainty-driven exploratory choice to frontopolar cortex + intraparietal sulcus (a prefrontal-parietal circuit). The two substrates are anatomically distinct in the human-fMRI literature. The Daw paradigm's design confound between novelty and uncertainty (less-sampled arms are both newer AND more uncertain) means the frontopolar BOLD signal includes some novelty component, but the substrate-level distinction is robust.

**Implication for REE.** MECH-314a and MECH-314b are licensed as independent substrate slots.

## R2 — Is MECH-314c (learning progress) substrate-distinct from 314a and 314b?

**Verdict.** **WEAKER SUPPORT, MORE THEORETICAL THAN EMPIRICAL.** Kaplan & Oudeyer 2007 supplies the algorithmic case for learning-progress as a distinct intrinsic-motivation flavour: it is a DERIVATIVE quantity (rate of change of prediction error), not the error itself. The empirical neural anchoring is much thinner than for 314a or 314b — the tonic-dopamine ↔ learning-progress hypothesis is a prediction rather than a finding, and dissociating learning-progress from uncertainty experimentally requires tasks where they decorrelate (irreducibly noisy regions vs plateaued mastery regions), which is not standard in the human curiosity literature.

**Implication for REE.** MECH-314c is licensed as a candidate substrate slot on algorithmic grounds, but expect the strongest experimental support to come from REE's own falsifier rather than from human-fMRI analogues. The 314c-OFF ablation prediction is "stuck in plateaus and stuck in noisy regions" — a behavioural signature distinct from 314a-OFF "won't visit new states" and 314b-OFF "won't choose uncertain options". The SD-054 reef substrate may need enrichment (irreducible-noise zones, plateaued-mastery zones) to make this dissociation testable.

## R3 — Is there a unification framework that would COLLAPSE all three sub-flavours?

**Verdict.** **EXISTS NORMATIVELY; SUBSTRATE-LEVEL IMPLEMENTATION UNCERTAIN.** Friston 2015 active-inference framework provides the normative collapse: expected free energy minimisation generates novelty, uncertainty-driven, and (loosely) learning-progress behaviour as task-conditional readings of a single epistemic-value computation. Schulz & Gershman 2019 review the related machine-learning unification (information-theoretic exploration objectives subsuming UCB, Thompson sampling, and information-gain bandits).

The empirical question — whether the brain implements the normative unification as a single substrate or as three specialised approximations — is unresolved. Substrate-level evidence (Wittmann 2007 vs Daw 2006) supports at least partial separation, which is compatible with normative unification + multi-substrate implementation.

**Implication for REE.** The COLLAPSE-ALL outcome from Q-044's resolution table is the active-inference-consistent outcome at the normative level, but R1+R2 substrate evidence makes a "three independent substrates implementing one normative quantity" outcome equally plausible. Q-044's three-arm ablation is the right experimental question; the COLLAPSE-ALL outcome should not be ruled out a priori, but neither should it be assumed.

## R4 — Is SD-054 reef substrate sufficient for the three-arm ablation?

**Verdict.** **PROBABLY INSUFFICIENT WITHOUT ENRICHMENT.** SD-054 reef supplies a rule-discriminative environment with hazard-vs-resource dynamics. The novelty/uncertainty/learning-progress decomposition Q-044 asks about requires a substrate where these three quantities can be MANIPULATED INDEPENDENTLY for at least some state subsets — e.g., regions with stable absolute novelty (rarely visited but reliable dynamics), regions with high uncertainty but stable novelty (sampled but variance never resolves due to irreducible noise), and regions with decreasing prediction error (active learning in newly-encountered dynamics). SD-054 does not by default supply these contrasts; the Q-044 falsifier may need a companion substrate enrichment.

The Q-044 claim notes already flag this: "SD-054 alone may be insufficient; substrate enrichment may be needed. Defer empirical resolution to ARC-064-Pull-2-follow-on (the bottom-up rule-discovery cluster surfaces the same independence questions for MECH-316/317/318)." The lit-pull confirms the substrate-readiness concern.

**Implication for REE.** When Q-044's three-arm ablation is queued, the substrate-readiness diagnostic should verify that novelty, uncertainty, and learning-progress are independently manipulable at the agent's z-state representation. If they are not (e.g., novelty and uncertainty are perfectly correlated in SD-054 reef by construction), the experiment cannot dissociate the three sub-flavours regardless of substrate independence.

---

## Recommended next actions

1. Update Q-044 `evidence_quality_note` in claims.yaml to cite this synthesis and capture R1–R4 verdicts.
2. Q-044 three-arm ablation should be deferred until a substrate that decorrelates novelty / uncertainty / learning progress is available, OR until a substrate-readiness diagnostic confirms SD-054 reef supplies that decorrelation.
3. The ARC-064-Pull-2-follow-on for MECH-316/317/318 (the bottom-up rule-discovery cluster) is structurally related and may inform the substrate enrichment needed here. Plan the two follow-ons together if possible.

---

*Authored 2026-05-11, automated lit-pull skill run. Five papers extracted; one mixed-direction entry (Friston 2015) preserves the unification alternative.*
