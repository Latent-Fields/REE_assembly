# Synthesis: E2 world-forward per-candidate signal collapse

**Date:** 2026-05-28
**Session:** lit-pull-e2-forward-action-divergence-20260528T171510Z
**Commissioning context:** Disposition #1 of [v3_exq_571_root_cause_2026-05-25.md](../../planning/v3_exq_571_root_cause_2026-05-25.md) named three candidate fixes for the V3-EXQ-571 collapse and flagged the choice as governance-side. This lit-pull surveys ML and biology literatures to inform that choice -- especially option (ii) (fix E2's world-forward predictor).

The full lit-pull commissioning brief is preserved in `TASK_CLAIMS.json` entry `lit-pull-e2-forward-action-divergence-20260528T171510Z`.

---

## 1. ML world-model evidence on action-conditional latent divergence

Three independent training-objective levers in the recent ML literature directly address the failure mode REE-v3 has surfaced.

| Mechanism | Paper | Lever | Confidence |
|---|---|---|---|
| Action-effect factorisation via MI minimisation | [Saanum, Dayan, Schulz 2024 (PLSM)](entries/2026-05-28_e2_action_divergence_plsm_saanum2024/) | Regulariser minimises MI between latent state and action-induced change, forcing factorisation of state-prior plus action-conditioned delta | 0.78 |
| Action-conditional contrastive prediction | [Srivastava et al. 2021 (Contrastive RSSM)](entries/2026-05-28_e2_action_divergence_contrastive_rssm_srivastava2021/) | Discriminative next-state objective: cannot win the contrastive task if K actions collapse to the same predicted latent | 0.68 |
| Action-identifiability via MI maximisation | [Qiu et al. 2026 (SWIRL)](entries/2026-05-28_e2_action_divergence_swirl_qiu2026/) | Maximise conditional MI between (state, action) and predicted next-state; penalises loss of action identity at the prediction step | 0.60 |

**Common observation across all three.** Reconstruction-based latent dynamics objectives -- which is essentially what E2 currently uses -- do not, by construction, prevent K-action collapse. The cheapest reconstruction-fit solution when action effect is small relative to state dynamics is a state-dominated predictor that ignores action almost entirely. Gradient descent will find that solution unless an additional objective forbids it. The three papers above are three structurally distinct ways to add that constraint.

**What the literature does *not* give us.** A direct empirical benchmark of the form "did K candidates collapse to identical predicted latents under condition X versus condition Y." The collapse mode V3-EXQ-571 documents is recognised qualitatively in the literature (PLSM names it as the absence of "systematic representation of action effects"), but I did not find a paper that publishes a per-candidate pairwise-distance metric across actions at one-step horizons as its headline measurement. This is a methodological gap REE could close on its own substrate.

**What the literature does *not* recommend.** None of the three papers proposes solving the problem at downstream consumers via action one-hot concatenation, i.e. option (i)'s GAP-B extension. That approach is not absent from the field -- decision-time augmentation is a known trick -- but the published architecture-level work goes after the forward model itself.

---

## 2. Biology forward-model evidence

Three biology entries from different anatomical levels of the forward-model literature converge on the same architectural commitment: biological forward models preserve action identity through the prediction step itself.

| Region | Paper | Mechanism | Confidence |
|---|---|---|---|
| Cerebro-cerebellum (motor + cognitive) | [Tanaka, Ishikawa, Lee, Kakei 2020](entries/2026-05-28_e2_action_divergence_cerebro_cerebellum_tanaka2020/) | Dentate-nucleus outputs are predictive for mossy-fibre inputs; cerebellar ataxia loses the predictive signature (kinematics revert from leading to lagging) | 0.74 |
| Prefrontal counterfactual rollout | [Miyamoto, Rushworth, Shea 2023](entries/2026-05-28_e2_action_divergence_fpc_counterfactual_miyamoto2023/) | FPC tracks alternative choices; alPFC compares simulated future scenarios -- the comparison function is computationally undefined if simulations collapse to the same neural state | 0.70 |
| Vestibular cerebellum + corollary discharge | [Cullen 2023](entries/2026-05-28_e2_action_divergence_vestibular_cerebellum_cullen2023/) | The vestibular cerebellum's prediction is gated by the specific motor command via corollary discharge, not by an action-averaged proxy | 0.71 |

**Common observation across all three.** Biological forward models -- whether the cerebro-cerebellar motor model, the prefrontal counterfactual comparator, or the vestibular cerebellar self-motion model -- preserve action-specificity *at the prediction step itself* via dedicated structural mechanisms (corollary-discharge gating, separate mossy-fibre projections, the granule-cell combinatorial expansion, the alPFC-vs-FPC dissociation). None of these substrates achieve action-distinguishability by emitting an action-averaged prediction and asking a downstream consumer to add the action one-hot back in.

**What the biology does *not* tell us.** A quantitative target: "predicted latents for different actions should differ by at least X under condition Y." The biological literature is firm on the qualitative architectural commitment without prescribing a magnitude. That magnitude is REE's to determine, by behavioural endpoint (Rung-1 entropy on SD-054 etc.) or by E3-consumer sensitivity analysis.

**What the biology *does* tell us.** Option (ii) (fix E2) is the architecturally faithful target. The cerebellar reference does not have an analogue of option (i)'s downstream one-hot bypass -- the corollary-discharge machinery is the biological analogue of building action-specificity into the prediction step. The prefrontal counterfactual literature treats per-action distinguishability of simulated futures as constitutive of the comparator function, not as a property to be repaired downstream.

---

## 3. Verdict on option (ii)

**The V3-EXQ-571 collapse is a substrate bug, not an inherited ML-side limitation.**

- The ML literature has named the failure family (Saanum et al. 2024 frames it as "lack of systematic representation of action effects") and offers at least three independent training-objective fixes (PLSM, contrastive next-state, SWIRL-style MI maximisation). The problem is tractable; the field has moved past "is this a real failure mode" into "which of several solutions is best."
- The biology converges on the same architectural commitment. The cerebellar forward model and the prefrontal counterfactual comparator both preserve action identity *at the prediction step* via dedicated mechanisms. The biological reference does not need an option (i)-style downstream workaround.

**Implication for the option (i)/(ii)/(iii) choice:**

- **Option (i) (extend GAP-B first-action one-hot bypass to all consumers)** remains the fastest path to a working substrate and is not contradicted by anything in this lit-pull -- it correctly produces the right answer at each consumer. What the literature tells us is that it commits REE to an architecture the biology does not have and that the ML field has moved away from. If option (i) is chosen, it should be understood as a known-quantity workaround rather than a faithful substrate.
- **Option (ii) (fix E2's world-forward predictor)** is supported by both literatures as the architecturally correct target. The lit-pull confirms (a) the field has converged training-objective levers (PLSM, contrastive RSSM, SWIRL) that target exactly this failure, and (b) biological forward models preserve action identity through the prediction step as a structural commitment. Option (ii) is also the heaviest of the three -- it requires either an additional auxiliary loss on E2 or an architectural change to E2's action fan-in, and either choice needs a design pass.
- **Option (iii) (source per-candidate signal from non-z_world channels)** is partially de-emphasised by the lit-pull: for the *novelty* signal (MECH-314a) specifically, sourcing from non-z_world (e.g. a rolling z_world prototype buffer, candidate-pool relative rank, or hippocampal anchor identity) remains sensible and is already queued as the MECH-314a-Phase-2 design question in `substrate_queue.json`. But option (iii) does not fix the substrate-level problem for the other consumers (MECH-320 tonic_vigor, MECH-295 liking, SD-033a/b lateral PFC and OFC), all of which read from E2's predicted z_world. So option (iii) is an MECH-314a-specific patch, not a system-wide solution.

**Recommended sequencing (governance-side):**

1. **Land option (i) as a tactical step** if and only if the matched-entropy FP-2 falsifier (V3-EXQ-569a, GAP-A R1.a/R1.b on the plan-of-record) needs to fire on the existing substrate within a short cycle. This is a workaround acknowledged as such. Open question: do we actually need to fire R1 on the current substrate, or is the option (ii) work fast enough to make R1 a one-shot on the fixed substrate?
2. **Pursue option (ii) as the architecturally correct fix.** Choice of training-objective lever among PLSM-style factorisation, contrastive next-state, or SWIRL-style MI maximisation is a design question; PLSM has the highest empirical maturity, contrastive RSSM has the simplest implementation, and SWIRL is the most recent. A short design memo weighing the three against REE's specific E2 architecture is the next concrete step.
3. **Keep option (iii) for MECH-314a only** via the existing Phase-2 design question. It is the right MECH-314a-specific patch and does not need to displace the system-wide option (ii) work.

---

## 4. Reading list (with REE-linked claim_ids)

### ML

- [Saanum, Dayan, Schulz 2024 -- PLSM](https://arxiv.org/abs/2401.17835). NeurIPS 2024. claim_ids: ARC-065, MECH-314a, MECH-320, SD-033a.
- [Srivastava et al. 2021 -- Contrastive RSSM](https://arxiv.org/abs/2112.01163). NeurIPS Deep RL Workshop 2021. claim_ids: ARC-065, MECH-314a, MECH-320.
- [Qiu et al. 2026 -- SWIRL](https://arxiv.org/abs/2602.06130). arXiv preprint Feb 2026. claim_ids: ARC-065, MECH-314a.

### Biology

- [Tanaka, Ishikawa, Lee, Kakei 2020 -- Cerebro-Cerebellum as Forward Model](https://doi.org/10.3389/fnsys.2020.00019). Frontiers in Systems Neuroscience. claim_ids: ARC-065, MECH-094, MECH-314a.
- [Miyamoto, Rushworth, Shea 2023 -- Imagining the future self](https://doi.org/10.1016/j.tics.2023.01.005). Trends in Cognitive Sciences. claim_ids: ARC-065, ARC-062, MECH-094, SD-033a.
- [Cullen 2023 -- Vestibular cerebellum internal models](https://doi.org/10.1016/j.tins.2023.08.009). Trends in Neurosciences. claim_ids: ARC-065, MECH-094.

### MECH-094 cross-link

Three of the six entries (Tanaka 2020, Miyamoto 2023, Cullen 2023) are tagged with MECH-094 (hypothesis tag / categorical write-gate). The connection is indirect but worth flagging for the governance audit trail: the cerebellar and prefrontal forward-model substrates do not just predict next-state action-specifically; they also gate *which* predictions write back to the world model versus stay quarantined as simulations. MECH-094's write-gate function and the per-action divergence preservation function are two faces of the same architectural commitment -- the prediction step has to be both action-specific (so different counterfactuals are distinguishable) and gated (so simulated counterfactuals don't contaminate the world model). Worth carrying into any future MECH-094 lit-pull.

### Existing dirs not duplicated

This new cross-cutting directory does not duplicate any of the existing lit pulls on the related claims:
- [`targeted_review_arc_065_behavioral_diversity_generation`](../targeted_review_arc_065_behavioral_diversity_generation/) -- covers diversity-generation breadth (active inference, curiosity, LC-NE tonic/phasic, striatal novelty, hippocampal trajectory sampling); does not address forward-model action-divergence preservation specifically.
- [`targeted_review_connectome_mech_320`](../targeted_review_connectome_mech_320/) -- covers tonic-vigor / opportunity-cost dopamine; does not address the bias-channel propagation issue.
- [`targeted_review_connectome_mech_094`](../targeted_review_connectome_mech_094/) -- covers reality monitoring / PTSD / source memory; does not address the per-action divergence preservation angle that connects to MECH-094's write-gate function.
- [`targeted_review_sd_033a`](../targeted_review_sd_033a/) -- covers lateral PFC top-down bias, rule-selective neurons, dynamic coding; does not address whether the input the lateral PFC reads carries per-candidate action specificity.
- [`targeted_review_arc_062_rule_apprehension`](../targeted_review_arc_062_rule_apprehension/) -- covers MD thalamus, mixed selectivity, rule cells, hippocampal goal preplay; the 2026-05-09 Pfeiffer-Foster entry there is the closest existing biological reference for action-conditional hippocampal forward sweep, but the rule-apprehension framing makes it tangential to E2's per-step forward model.

### Methodological follow-up

A specific empirical gap surfaced by this lit-pull: I could not find a published paper that reports per-action pairwise distance between predicted latents at one-step horizons as a headline metric for evaluating learned forward models. PLSM measures action-effect factorisation indirectly via the MI regulariser; contrastive RSSM measures via discriminative accuracy; SWIRL measures via downstream benchmark gains. None of these is the obvious diagnostic for the failure V3-EXQ-571 documents. There may be an opportunity for REE to publish the `cand_world_pairwise_dist`-style metric as a standalone diagnostic for the model-based RL community, since the failure mode appears to be real, common, and under-measured.

---

## What this synthesis does NOT do

- Does not edit `claims.yaml`. The MECH-314a, MECH-320, MECH-295, SD-033a, SD-033b, ARC-065, ARC-062, MECH-094 entries are unchanged. Concurrent sibling sessions hold those resources; their governance status is theirs to update.
- Does not edit `substrate_queue.json` or `behavioral_diversity_isolation_plan.md`. The MECH-341 retune session (`implement-substrate-mech-341-retune`) and the GAP-A resync session (`igw-008-gap-a-stale-resync`) already touched these earlier in the day; the GAP-C and GAP-D doc-syncs are in-flight.
- Does not queue any experiments.
- Does not pre-commit to a specific E2 fix. Governance choice between PLSM / contrastive / SWIRL / architectural restructure is downstream of this lit-pull.

---

*Author session: lit-pull-e2-forward-action-divergence-20260528T171510Z. Commissioned 2026-05-28T17:15:10Z. Per `REE_Working/CLAUDE.md` "biology before formal definitions" feedback memory and the 2026-05-25 v3_exq_571 root-cause doc disposition #1.*
