# SYNTHESIS -- MECH-318 rule-state abstraction (ARC-064 Pull-2 follow-on)

**Pull 2 follow-on** to the ARC-064 bottom-up rule discovery cluster lit-pull (2026-05-10).
**Date:** 2026-05-11. **Entries:** 4 papers (foundational meta-RL framework + AI-tradition RL² architecture + fast-and-slow integration review + primate empirical anchor for rule-switch inference).
**Source attribution:** per-paper records cite PubMed / arXiv and include DOI links; this synthesis aggregates and adjudicates.

---

## Why this pull was commissioned

Pull 1 (ARC-064 bottom-up rule discovery, 2026-05-10) identified MECH-318 as a candidate substrate for the rule-state-abstraction role with provisional-registration status (`registration_provisional_pending_meta_rl_absorption_check` flag). The 2026-05-10 absorption check ([`docs/architecture/mech_318_absorption_check.md`](../../../docs/architecture/mech_318_absorption_check.md)) reached verdict B: PARTIALLY ABSORBED. The within-V3 portion of MECH-318 (W1 recurrent topology, W3 hidden-state encodes task identity, W4 biases action selection) was determined to be substantially covered by the existing SD-033a LateralPFCAnalog rule_state buffer + ARC-062 Phase 1 gated_policy discriminator + planned Phase 3 GAP-C wiring cluster. The W2 multi-task-training and W5 cross-episode-continuity properties were determined NOT ABSORBED. The empirical retire-vs-promote verdict was deferred to V3-EXQ-543c-successor on multi-rule-context substrate.

Pull 2 returns to the literature with the absorption-check verdict as the architectural prior and tests it against the canonical meta-RL framework (Wang 2018, Duan 2016, Botvinick 2019) plus the strongest primate empirical anchor for rule-state inference (Sarafyazd & Jazayeri 2019). The questions Pull 2 is asked to settle are: does the absorption-check verdict survive contact with the canonical meta-RL literature, where are the residual gaps, and how should MECH-318 integrate with the rest of the existing REE substrate inventory?

---

## R1 -- Does MECH-318 need a dedicated substrate or does the SD-033a + ARC-062 cluster suffice?

### Verdict: ABSORPTION-CHECK VERDICT B SUPPORTED. The within-V3 portion of MECH-318 absorbs into SD-033a + ARC-062 + Phase-3-wiring; the residual W2 and W5 gaps remain as legitimate MECH-318 scope if the empirical verdict requires a dedicated substrate. Confidence 0.78.

The literature does not flat-out resolve the absorption question -- substrate-design verdicts genuinely cannot be made from literature alone -- but it does support the architectural framework the absorption check committed to. Four threads converge:

- **Wang 2018 framework**: meta-RL via a recurrent network whose weights are trained across a task family, with the hidden state encoding task identity within an episode. The W1+W3+W4 properties are foundational to this framework and are what SD-033a + ARC-062 + Phase-3-wiring covers within V3 (with SD-033a's EMA as recurrence-as-EMA, ARC-062's discriminator as the per-tick identity-encoding signal, and the dacc_score_bias additive composition as the downstream action-selection coupling). The match is not perfect (LSTM-style recurrence is stronger than gate-modulated EMA) but it is structural, and the substrate-design alternative -- adding an explicit LSTM-as-rule-state component -- would require commissioning a new substrate that the absorption check already determined is not necessary for the within-V3 portion.

- **Duan 2016 RL² architecture**: the cross-episode hidden-state continuity property (W5) is foundational. None of the current V3 substrates implement it. The literature supports the absorption-check verdict that W5 is not absorbed -- but also supports the architectural reading that W5 is V4-scope rather than V3-tractable, because the per-episode reset is load-bearing for the rest of the agent's state machine.

- **Botvinick 2019 fast-and-slow review**: the strongest agents integrate meta-RL with episodic memory. The within-V3 SD-033a + ARC-062 cluster IS the meta-RL component; REE's existing MECH-269 anchor sets + MECH-292/293 ghost-goal substrates are the episodic-memory component. The architectural integration is already largely in place; what is missing is the explicit composition pattern (trigger-layer, readout-layer, or training-layer integration). This is a substrate-design call, but the literature supports treating the integration as the V3 architectural commitment rather than as a separate-MECH-318 commitment.

- **Sarafyazd & Jazayeri 2019 primate empirical**: rule-state inference in frontal cortex is sequential (DMFC accumulates evidence, ACC encodes the categorical rule-switch inference). The architectural sequencing maps cleanly onto ARC-062 GatedPolicy (DMFC-analog) feeding into SD-033a rule_state buffer (ACC-analog) via the planned Phase 3 wiring. The biology supports the absorption-check verdict that the within-V3 portion is hierarchical-inference-substrate-ready.

The combined verdict is therefore that the absorption-check verdict B (partially absorbed) is supported by the literature. The within-V3 portion of MECH-318 absorbs into the SD-033a + ARC-062 cluster with Phase 3 GAP-C wiring; the W2 and W5 properties remain legitimate residual scope.

Confidence 0.78 because the literature is converging but the empirical retire-vs-promote verdict on the multi-rule-context substrate -- which is the actual gate the absorption check named -- has not yet been run.

---

## R2 -- Is the absorption-check verdict B supported by the literature?

### Verdict: YES, with strengthened framing. The within-V3 SD-033a + ARC-062 cluster IS the meta-RL substrate; the architecture should be made explicit at the cluster level. Confidence 0.80.

The 2026-05-10 absorption check (`mech_318_absorption_check.md`) audited the W1-W5 mapping at the substrate level. This lit-pull reaches the same architectural conclusion via the literature anchoring. The strengthened framing the literature adds:

- **The cluster is hierarchical-inference-substrate by design**, not just by accident. The ARC-062 + SD-033a sequencing (Phase 3 GAP-C wiring) is the same architectural sequencing the Sarafyazd-Jazayeri primate biology anchors. The cluster should be documented as the V3 instantiation of frontal-cortex hierarchical rule-inference, with ARC-062 covering the evidence-accumulation arm and SD-033a covering the categorical rule-state-attribution arm.
- **The within-episode portion of meta-RL is V3-tractable**, the cross-episode portion is V4-deferred. Wang 2018 + Duan 2016 + Botvinick 2019 all support this decomposition. The W5 RL²-strict property is V4-scope; the within-episode W1+W3+W4 portion is V3-instantiable and largely already in place.
- **The integration with episodic substrates is part of the architecture**, not a separate concern. Botvinick 2019 anchors the fast-and-slow framework. REE's MECH-269 anchor sets + MECH-292/293 ghost-goal substrates ARE the fast-retrieval component; SD-033a + ARC-062 + Phase-3-wiring IS the slow-meta-RL component. The composition between them needs to be made explicit as part of the substrate-design pass.

The architectural recommendation: rather than treating MECH-318 as a pending claim awaiting a dedicated substrate landing, treat the SD-033a + ARC-062 + Phase-3-wiring cluster as the V3 instantiation of the within-episode portion of MECH-318. Document it as such in the next governance pass. The MECH-318 claim itself can remain as the residual-scope marker for W2 + W5 (which retain their legitimate independent substrate-design implications).

---

## R3 -- Is the W5 cross-episode-continuity gap V4-scope or V3-tractable?

### Verdict: PROBABLY V4-SCOPE, with one V3-tractable softening via episodic substrates. Confidence 0.72.

The W5 question is whether the meta-RL substrate's hidden state should persist across episodes. Duan 2016 RL² anchors this as the defining property of recurrent meta-RL. The 2026-05-10 absorption check determined that none of the current V3 substrates implement W5: all reset per episode by design, and the per-episode reset is load-bearing for the rest of the agent's state machine.

Two paths exist:

- **STRICT-W5 path**: build a substrate that explicitly preserves hidden state across episodes. This conflicts with the per-episode reset semantics that anchor anchor-set partitioning, sleep transitions, harm accumulation, ghost-goal bank cleanup, etc. The architectural cost is high; the right place to make the commitment is in V4 ARC-063 strong-reading work, not V3.

- **SOFT-W5 path**: read 'cross-episode continuity' off the episodic substrates rather than off the meta-RL substrate's own hidden state. MECH-269 anchor sets persist across episodes (within their accumulation window); MECH-292 ranked ghost-goal bank persists across episodes (across the relevant accumulation window). If MECH-318's rule-state-attribution component reads its 'task identity' input from the episodic substrates, the cross-episode continuity is provided by the episodic substrates rather than by the meta-RL substrate's hidden state itself. This is a softer form of W5 but may be empirically sufficient.

The SOFT-W5 path is V3-tractable and is consistent with the Botvinick 2019 fast-and-slow framework (R4 verdict). The STRICT-W5 path is V4-scope. The substrate-design pass should adopt the SOFT-W5 path as the V3 commitment, with the STRICT-W5 path as the V4 extension if the empirical verdict on multi-rule-context substrate requires it.

Confidence 0.72 reflects the architectural commitment being made on substrate-design grounds (the per-episode reset is load-bearing) rather than on direct literature evidence.

---

## R4 -- How should MECH-318 integrate with the existing episodic substrates per the fast-and-slow framework?

### Verdict: TRAINING-LAYER INTEGRATION is the most architecturally interesting and likely the most empirically tractable. Confidence 0.70.

Botvinick 2019 supplies the fast-and-slow framework but does not specify how the integration should work at the substrate level. The 2026-05-10 absorption check named three integration patterns:

- **Trigger-layer integration**: episodic retrieval signals when the meta-RL substrate should be active.
- **Readout-layer integration**: both substrates feed into action selection in parallel via additive composition into dacc_score_bias.
- **Training-layer integration**: episodic substrates supply training data for the meta-RL substrate's weight learning.

The readout-layer integration is the easiest because it is already largely in place: SD-033a compute_bias and ARC-062 gated_policy heads both add into dacc_score_bias, and MECH-269 / MECH-292 / MECH-293 substrate outputs also feed into the action-selection layer via the existing E3 selection machinery. This is the baseline.

The trigger-layer integration is a meaningful extension: the episodic retrieval signal could gate when the meta-RL substrate becomes the primary action-selection driver vs when the episodic-retrieval direct-policy bias suffices. The architectural implication is a learned gating mechanism that arbitrates between the two systems based on familiarity.

The training-layer integration is the most architecturally interesting and addresses the W2 gap directly. If the agent's accumulated trajectory record across many anchor-clusters constitutes the 'task family' over which the meta-RL substrate's weights should be shaped, the W2 multi-task-training-distribution gap may be closeable within V3. The trajectory record IS the multi-task training distribution. This is a substrate-design hypothesis worth testing.

The substrate-design pass should explore the training-layer integration as the V3 candidate for closing the W2 gap. If it works, MECH-318 may absorb fully into the existing cluster (SD-033a + ARC-062 + Phase-3-wiring + episodic-substrate-derived training-distribution) and retire as superseded. If it doesn't, the W2 gap remains as residual MECH-318 scope and motivates a separate substrate landing.

---

## What this pull does NOT settle

1. **The empirical retire-vs-promote verdict.** This is gated on V3-EXQ-543c-successor on multi-rule-context substrate. The substrate-readiness work (likely SD-054 extended with multi-rule-context) is the prerequisite. The lit-pull adjudicates the architectural framing; the empirical verdict awaits the substrate-readiness and validation work.

2. **The specific implementation of the training-layer integration.** R4 recommends exploring the training-layer integration as the V3 candidate for closing W2. The substrate-design call is which episodic substrate's output is used as training data (anchor sets? ghost-goal bank? trajectory record directly?) and how the meta-RL weight learning is parameterised over this data. None of these are literature-decidable.

3. **The relationship between MECH-318 and the parallel-session-registered MECH-323 (ARC-071 chunk-formation operator).** MECH-318 is the rule-state-abstraction substrate; MECH-323 is the chunk-formation operator. The two are structurally related -- both operate on the trajectory record, both produce reusable behavioural units -- but the relationship between them is not literature-decidable. The substrate-design pass should treat them as cluster-coupled but architecturally distinct.

4. **The V4 boundary for the cross-episode-continuity portion.** R3 recommends V4-deferral of the W5 STRICT property. The exact boundary between V3 and V4 for this property -- specifically whether the SOFT-W5 path is sufficient for all empirical demands or whether some demands genuinely require the STRICT-W5 substrate -- is an open architectural question that V4 substrate-design will need to resolve.

---

## Per-paper summary index

| Entry | DOI | Role | Direction | Confidence |
|---|---|---|---|---|
| Wang et al. 2018 | [10.1038/s41593-018-0147-8](https://doi.org/10.1038/s41593-018-0147-8) | foundational meta-RL framework anchor | supports | 0.84 |
| Duan et al. 2016 | [arXiv:1611.02779](https://arxiv.org/abs/1611.02779) | AI-tradition recurrent-meta-RL anchor (W5 property) | supports | 0.78 |
| Botvinick et al. 2019 | [10.1016/j.tics.2019.02.006](https://doi.org/10.1016/j.tics.2019.02.006) | fast-and-slow integration framework | supports | 0.78 |
| Sarafyazd & Jazayeri 2019 | [10.1126/science.aav8911](https://doi.org/10.1126/science.aav8911) | primate empirical anchor (DMFC+ACC rule-switch) | supports | 0.84 |

**Aggregate MECH-318 lit_conf** (post-indexer): expected to land in the 0.78-0.82 range, supports-direction-dominant, 4-entry cohort. All four entries support the absorption-check verdict B (partially absorbed). The architectural reading is that the within-V3 portion of MECH-318 absorbs into SD-033a + ARC-062 + Phase-3-wiring cluster; the W2 multi-task-training gap may be closeable within V3 via training-layer integration with episodic substrates; the W5 cross-episode-continuity gap is V4-deferred via SOFT-W5 reading (cross-episode continuity provided by episodic substrates rather than meta-RL hidden state).

The substrate-design pass that follows this lit-pull should: (a) document the SD-033a + ARC-062 + Phase-3-wiring cluster as the V3 instantiation of the within-episode portion of MECH-318; (b) test the training-layer integration with episodic substrates as the V3 candidate for closing W2; (c) defer STRICT-W5 to V4 ARC-063 strong-reading work; (d) sequence the empirical verdict experiment (V3-EXQ-543c-successor on multi-rule-context substrate) after the training-layer integration is in place.

According to PubMed and arXiv, all entries in this synthesis are sourced as cited above; DOIs are linked per-entry.
