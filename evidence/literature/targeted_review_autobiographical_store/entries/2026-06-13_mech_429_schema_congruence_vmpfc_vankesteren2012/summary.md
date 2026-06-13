# How schema and novelty augment memory formation (van Kesteren, Ruiter, Fernández & Henson, 2012)

**Claim grounded:** MECH-429 (schema-congruence as a consolidation write-weight and routing variable) — closing the reap-only gap from the first ABM-9 pass, where MECH-429 was registered as a completion-set partner with no literature_evidence entry behind it.

## Why this entry exists

In the first ABM-9 pull (2026-06-13) the schema-congruence partner was *reaped* into claims.yaml as MECH-429 but left ungrounded — its notes carry the instruction to "pull a targeted review before any build, per biology-before-formal-definitions," naming van Kesteren 2012 and Tse 2007 as the anchors. The FINISH pass's job is to confirm each ABM-9 strand has a landed grounding entry and to add the missing one where a child claim was registered reap-only. This is that entry: it gives the L3 (imagination-learning / schema) strand's reaped partner its biological warrant.

## What the paper says

van Kesteren and colleagues review why information that fits an existing schema is usually remembered better and consolidated faster than information that does not. Their synthesis is the SLIMM model (schema-linked interactions between medial temporal lobe and neocortex). The central proposal: medial PFC evaluates the *congruency* — they call it "resonance" — between incoming information and the schemas already stored in neocortex. When resonance is high, mPFC promotes rapid neocortical integration and *suppresses* the slow, hippocampal/MTL-dependent encoding route; when resonance is low, MTL-dependent encoding dominates. They also account for the apparent paradox that strongly *novel* (incongruent) information is sometimes better remembered, via a separate mechanism.

## How it translates to REE

This maps almost one-to-one onto MECH-429. The claim is that schema-fit is a consolidation *write-weight* and *routing* variable — congruent content gets preferential, more direct routing into the durable/semantic store via a fast vmPFC-gated route, while incongruent content needs prolonged hippocampal-dependent consolidation or is gated out. SLIMM's mPFC-resonance gate is exactly that fast route, and the mPFC/MTL dissociation is exactly the two-route structure. Importantly, this is the route that REE's *existing* consolidation gates already presupposed without naming: MECH-261 (mode-conditioned write gating) and MECH-285 (consolidation priority by V_s residual) both decide *whether* and *how strongly* to write, but neither carried a schema-fit term. MECH-429 adds schema-fit as a second write-weight axis beside affect (MECH-361), and this paper is its mechanism.

Two caveats are logged rather than smoothed over. First, the relationship is not a monotone "more congruent → more consolidation": SLIMM itself predicts a novelty boost at the incongruent end, so a faithful model has to represent the U-shaped congruence/novelty interaction, not a single linear schema gain (this is the entry's failure signature). Second — and this is MECH-429's own falsifier — the paper does *not* show that schema-fit explains consolidation variance *independent of* affect and V_s residual. That orthogonality is REE's synthesis, and remains the thing a V4 experiment would have to demonstrate before MECH-429 earns its keep. Tse et al. (2007, *Science*) is the canonical empirical anchor for schema-accelerated consolidation, and Schapiro et al. (2017) covers the complementary-learning-systems-within-hippocampus angle; both are named in MECH-429's notes and sit behind this review.

## Confidence reasoning

I set this at 0.77. Source quality is high (*Trends in Neurosciences*, integrating the strong Tse-2007 animal findings into a named mechanism), and mapping fidelity is high for the congruence-routing core of the claim. I held it below ~0.8 because the affect-orthogonality axis — the part that makes MECH-429 more than a restatement of known schema effects — is REE's contribution, not something this paper tests. Transfer risk is the standard neural-systems-to-architecture analogy. exp_conf is unchanged at 0; this raises literature confidence only and promotes nothing.
