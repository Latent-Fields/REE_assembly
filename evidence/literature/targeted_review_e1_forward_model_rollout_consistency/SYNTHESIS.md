# Synthesis: E1 forward-model multi-step rollout consistency

**Date:** 2026-08-03
**Session:** metaworker-chip-20260803-litpull-e1-rollout-consistency
**Commissioning context:** Primary routing of the confirmed [failure_autopsy_V3-EXQ-108b_2026-08-03](../../planning/failure_autopsy_V3-EXQ-108b_2026-08-03.md), and the sole `depends_on_unresolved` entry blocking `substrate_queue.json` `sd_id: SD-e1-rollout-consistency-training` (`ready: false`, priority 2, unblocks INV-088 / MECH-135).

**Research question as commissioned:** what training-objective modifications fix single-step-trained dynamics models' rollout collapse under long-horizon autoregressive use? Verify and ground the three candidates the autopsy named -- latent overshooting, scheduled multi-step unrolling, contrastive next-state -- and identify others.

---

## 0. Headline: the commissioned question is answered, and a prior defect was found while answering it

The autopsy's diagnosis is **confirmed by the literature as a real, named, and well-studied failure family**, and all three named candidates are grounded in actual anchor papers (Section 1). A fourth candidate the autopsy did not name turns out to fit REE's usage better than any of the three (Section 1, Asadi). The biology row of the autopsy's four-layer diagnosis, recorded as `absent (for this specific axis)`, is now discharged with two citations (Section 2).

But the lit-pull surfaced something that changes the recommendation, and it is the most important thing in this document:

> **Every one of the four literature fixes presupposes an *action-conditioned* transition model. REE's E1 has no action input at all.**

This is not an inference from the manifest. It is code, verified this session:

- `ree_core/predictors/e1_deep.py` -- `forward(self, current_state, horizon=None, z_goal=None)` and `predict_long_horizon(self, current_state, horizon=None)`. There is no action parameter on either. (The `action_bias` in that file is the MECH-151 E1-to-E2 affordance *output*, not a transition input.)
- `experiments/v3_exq_108b_...py:303` (training) and `:460` (scoring) -- both call `agent.e1(total_curr, horizon=1)`. No action is passed in either place.
- In `_score_sequence_e1coe_with_endpoint`, the candidate action reaches z_world only by a second-order path: `action -> agent.e2.predict_next_self -> z_self -> E1's prior_generator`. And inside `predict_long_horizon` the LSTM input is `prior_full = cat([zeros(self_dim), prior])` -- **the z_self half is zeroed**, so the LSTM never sees z_self directly; the entire action signal is squeezed through one `world_dim`-wide projection.

Compare the four fixes: PlaNet regularises `p(s_t | s_{t-1}, a_{t-1})`; DaD's controlled variant corrects `(state, action)` rollouts; TD-MPC's consistency term is literally `|| d(z_i, a_i) - h(s_{i+1}) ||^2`; Asadi's model takes a state *and an action sequence*. All four constrain how the predicted trajectory differs **across actions**. That is the quantity C3 measures -- `e1coe_score_var` is the variance of goal-proximity across forty different action sequences -- and it is a quantity an action-blind transition cannot express however well it is trained.

**Consequence for the substrate entry.** `substrate_queue.json`'s current `implementation_hint` reads "Add a multi-step/rollout-consistency term to E1's training objective." Taken literally and applied to E1 as it stands, that would make E1's single trajectory more self-consistent while leaving the forty candidates exactly as indistinguishable as they are now. The hint understates the work: the fix is an **interface change plus an objective change**, not an objective change alone.

**This also better explains the magnitude.** Compounding error degrades distinctiveness; it does not usually annihilate it. `e1coe_score_var` at 1.65e-13 / 2.25e-14 against a 0.002 threshold, with scores clustered at ~0.908, is eleven orders of magnitude -- which is what a near-absent causal channel looks like, not what a noisy one looks like. There is an internal precedent for exactly this signature in the same file: the EXQ-449a comment at `e1_deep.py:251-256` records `cue_action_proj` output having per-channel std ~2.7e-8 because its input was constant across batch, fixed by concatenating `z_world` to guarantee per-input variation. Same family of defect, same file, already seen once.

I am flagging this as a **code-verified structural observation, not a settled diagnosis.** Both mechanisms -- horizon mismatch and weak action-conditioning -- are present and would each produce collapse. Which dominates is measurable and has not been measured. Section 4 proposes the probe.

---

## 1. ML evidence: four training-objective levers, and what each one actually claims

| Mechanism | Paper | Lever | Direction | Confidence |
|---|---|---|---|---|
| Latent overshooting | [Hafner et al. 2019 (PlaNet)](entries/2026-08-03_e1_rollout_consistency_latent_overshooting_hafner2019/) | Multi-step variational bound: KL between d-step prior and filtered posterior, all d <= D, in latent space, posterior gradients stopped for d>1 | mixed | 0.62 |
| Scheduled multi-step unrolling | [Venkatraman, Hebert & Bagnell 2015 (DaD)](entries/2026-08-03_e1_rollout_consistency_dad_multistep_venkatraman2015/) | Treat rollout as imitation learning; harvest the model's own drifted states, pair with ground-truth continuations, refit. No architecture or loss-form change | supports | 0.74 |
| Multi-step latent consistency | [Hansen, Wang & Su 2022 (TD-MPC)](entries/2026-08-03_e1_rollout_consistency_latent_consistency_tdmpc_hansen2022/) | L2 between action-conditioned latent prediction and target-encoder next-state, accumulated over an H-step training unroll | supports | 0.76 |
| Direct sequence-conditioned model | [Asadi, Misra, Kim & Littman 2019](entries/2026-08-03_e1_rollout_consistency_multistep_model_asadi2019/) | Abandon self-composition: learn (state, action sequence) -> outcome directly | mixed | 0.68 |
| **Boundary condition on all of the above** | [Somalwar, Lee, Pappas & Matni 2025](entries/2026-08-03_e1_rollout_consistency_when_multistep_helps_somalwar2025/) | Multi-step training wins under model **misspecification**; single-step wins when the model class is well-specified | mixed | 0.58 |

**Candidate 1 (latent overshooting) is grounded but NOT endorsed by its own source.** This is the finding I least expected. PlaNet's Appendix D reports latent overshooting substantially helping purely stochastic models (DRNN) and **slightly reducing** RSSM performance on all six tasks; the paper says "our final agent using the RSSM model does not require it"; and Dreamer (ICLR 2020) states outright "We did not find latent overshooting for learning the model ... necessary." The benefit is architecture-conditional, and E1's deterministic LSTM sits on the side of that split where it did not help. Anyone treating latent overshooting as the default because it is the most quotable name should read the ablation first.

**Candidate 2 (scheduled multi-step unrolling) has the cleanest diagnosis and the cheapest implementation.** DaD's reframing is the most useful sentence in this whole review: compounding error is a *distribution-shift* problem, not merely an accuracy problem -- iterating the model "change[s] the input distribution for future prediction steps, breaking the train-test i.i.d assumption common in supervised learning." Because DaD changes only the training data, not the architecture or the loss form, it is the lowest-cost intervention available. It is also the one least likely to fix C3 on its own, for the Section 0 reason.

**Candidate 3 (contrastive next-state) is the weakest of the three, and the sibling E2 review is the reason it was on the list.** I found no paper making the case for contrastive objectives as a fix for *long-horizon rollout* collapse specifically; the contrastive work in this area (including the Contrastive RSSM entry in the E2 review) targets *single-step action identifiability*. The one directly relevant data point runs mildly against it: TD-MPC's authors compared latent consistency against reconstruction and contrastive alternatives and adopted consistency, reporting it as the more consistent choice. That is a different setting and a different failure, so it is not decisive -- but combined with the absence of a long-horizon contrastive anchor, **candidate 3 should be de-prioritised relative to candidates 2 and 4**, and the presumption that the E2 conclusions transfer should be dropped. This vindicates the autopsy's own instruction to treat the E2 review as a prior and not a substitute.

**A fourth candidate the autopsy did not name, and it fits REE's usage unusually well.** `_score_sequence_e1coe_with_endpoint` iterates E1 thirty times and then uses **only the endpoint** -- `goal_state.goal_proximity(z_world_curr)` on the final z_world; every intermediate prediction is discarded. Asadi et al.'s formulation, (state, action sequence) -> outcome, gives the evaluator exactly what it consumes and removes the self-composition where error magnification happens. The objection is combinatorial: the sequence space is |A|^H, astronomically larger than the forty sequences scored, so the model must generalise across unseen sequences and the paper's empirical scale is far smaller. It also could not *replace* E1 -- E1's other consumers (HippocampalModule priors via `generate_prior`, MECH-151 `action_bias`, MECH-216 schema salience) all need the per-step trajectory -- so it would be an evaluator-specific head alongside E1.

**What the ML literature does NOT give us.** No paper found reports *per-candidate endpoint distinctiveness under long-horizon rollout* as a headline metric. The field measures compounding error by prediction error against ground truth, or by downstream task return. REE's `CR_rollout/CR_real` ratio -- contrast among imagined endpoints, normalised by contrast among real states -- appears to be an instrument the field does not have. This is the same methodological gap the sibling E2 review flagged for the one-step case, now confirmed to extend to the multi-step case. Two independent reviews finding the same measurement absent is a reasonable basis for treating it as a genuine contribution rather than an idiosyncrasy.

**And the boundary condition.** Somalwar et al. 2025 is the only paper that asks when multi-step training is *worth* it. For linear systems: single-step wins when the model class is well-specified; multi-step wins when it is misspecified due to partial observability. Applied to REE the criterion points favourably -- E1 predicts a learned latent from partial grid-world observation through a `world_dim=32` bottleneck -- but it is a linear-systems asymptotic result and E1 is a nonlinear LSTM, so it is a well-motivated heuristic, not an applicable theorem. Its real value is converting `node_class: complex (probe-gated)` from a label into a question with a determinate answer.

---

## 2. Biology evidence: the autopsy's `absent` row, discharged

| Finding | Paper | Mechanism | Direction | Confidence |
|---|---|---|---|---|
| Imagination dissociates from perception | [Hassabis, Kumaran, Vann & Maguire 2007](entries/2026-08-03_e1_rollout_consistency_scene_construction_amnesia_hassabis2007/) | Bilateral hippocampal damage markedly impairs construction of new imagined experiences; imagined content is fragmented, lacking holistic spatial context | mixed | 0.55 |
| Simulation depth demands its own machinery | [Addis & Schacter 2008](entries/2026-08-03_e1_rollout_consistency_temporal_distance_hippocampus_addis2008/) | Bilateral hippocampal activity scales with the increasing remoteness of imagined future events; interpreted as relational integration of increasingly disparate details | supports | 0.60 |

The autopsy recorded `Biological reference: absent (for this specific axis)` and asked this pull to verify the parallel with real citations. Both halves are now cited, and they say different things.

**Hassabis 2007 confirms the separability premise.** Multi-step constructive simulation is a distinct system layered on perception, and it fails on its own -- exactly the shape of REE's healthy CR_real (0.193/0.201, holdout probe accuracy 0.80-0.94) alongside a collapsed CR_rollout.

**But the failure signatures differ, arguably invert, and I have set the entry's direction to `mixed` accordingly.** The patients' imagined experiences "lacked spatial coherence, consisting instead of fragmented images in the absence of a holistic representation" -- a loss of *binding*, producing scattered content. E1 fails by *convergence*: forty trajectories onto near-identical endpoints, a loss of *variance*. Excessive coherence. Both are degenerate simulation; they are not the same pathology, and the biological result does not predict REE's form. The autopsy's proposed parallel is confirmed at the level of architecture and **not** at the level of signature, and that distinction should survive into any governance note that cites it.

**Addis & Schacter 2008 is the more architecturally informative of the two**, despite Hassabis being the more famous paper. Hippocampal recruitment *scales with simulated remoteness* -- deeper simulation recruits more machinery, not the same machinery run longer. E1 does the opposite: `predict_long_horizon` composes one LSTM step thirty times in a plain loop, trained throughout at `horizon=1`, with nothing whose contribution grows with depth. Biology builds at the horizon it plans at. That converges with the ML side's recommendation from a methodologically unrelated direction, which is the strongest structural signal in this review.

**What the biology does not give us.** A quantitative target. Nothing here says "imagined endpoints for distinct action sequences should differ by at least X." As in the E2 review, that magnitude is REE's to determine from its own consumers -- here, the `C3_VAR_THRESHOLD = 0.002` and `CR_ROLLOUT_COLLAPSE_RATIO = 0.1` the 108b driver already pre-registered.

---

## 3. Verdict on the commissioned question

**Confirmed.** Single-step-trained dynamics models do collapse under long-horizon autoregressive use; this is a named, theorised failure family with anchor papers spanning 2015 to 2025, and V3-EXQ-108b's diagnosis is a textbook instance of it. The autopsy was right.

**Candidate ranking, on the evidence:**

1. **Multi-step latent consistency over an action-conditioned transition (TD-MPC-style)** -- the strongest template. Its objective form transposes to E1's deterministic MSE with no reinterpretation; its H-step unroll is the concrete form of "train at the horizon you plan at"; and it is action-conditioned, which Section 0 identifies as the property that decides whether C3 can move at all. Caveat: TOLD is *task*-oriented and E1 is a general world model with several consumers, so this must be additive, not a replacement of E1's training signal.
2. **Scheduled multi-step unrolling (DaD)** -- cheapest by a wide margin, correct diagnosis, no architecture change. Best value as a *first* intervention, but not expected to move C3 alone.
3. **Direct sequence-conditioned endpoint model (Asadi)** -- best fit to what the evaluator actually consumes, and removes the composition rather than regularising it. Held at 3 only because of the |A|^H generalisation question at horizon 30 and because it is an added head rather than a fix to E1.
4. **Latent overshooting (PlaNet)** -- grounded, canonical, and not endorsed by its own ablation for E1's architecture class. Do not adopt by default.
5. **Contrastive next-state** -- de-prioritised. No long-horizon anchor found; the one relevant comparison (TD-MPC) went the other way; the E2 review's contrastive recommendation addresses single-step action identifiability, which is a different problem.

**But the ranking is provisional on a question nobody has answered**, and this is where the `complex (probe-gated)` classification earns its keep. Two mechanisms are simultaneously present in the code:

- **(a) horizon mismatch** -- trained at 1, used at 30, no objective covering steps 2-30;
- **(b) action-blindness** -- E1's transition takes no action, so the candidate signal reaches z_world only through a zeroed-z_self, `world_dim`-wide `prior_generator` bottleneck.

Every fix above targets (a) and presupposes (b) is already solved. If (b) dominates, all five candidates fail and the substrate work is misdirected.

---

## 4. Recommended next step: a cheap probe, before the build

The honest reading of `node_class: complex (probe-gated)` is that a probe is still owed, and the lit-pull has sharpened what it should measure. A **diagnostic, not an experiment** -- it needs no new claim and no queue entry beyond a standard `/queue-experiment` pass:

1. **Horizon sweep of the collapse.** Record `CR_rollout(h)` for h = 1, 2, 3, 5, 10, 20, 30 on the existing trained E1, rather than only at h=30. Compounding error predicts smooth degradation with depth. Action-blindness predicts the ratio is already near-floor **at h=1**, before any compounding can have occurred. These are cleanly distinguishable and the instrumentation is a loop change in code the 108b driver already has.
2. **One-step per-action divergence.** Pairwise distance between predicted z_world at h=1 across the K actions -- the direct analogue of the E2 review's `cand_world_pairwise_dist`, applied to E1. Near-zero confirms (b) directly.
3. **Only then choose an objective.** If the collapse is smooth in depth, the ranking in Section 3 stands and TD-MPC-style consistency is the target. If it is already floored at h=1, the substrate entry needs rewriting: the first work item is action-conditioning E1's transition, and the multi-step objective is second.

Probe (1) alone would likely settle it, and it is hours of work against a substrate change that touches E1's interface and every call site.

---

## 5. Reading list (with REE-linked claim_ids)

### ML

- [Venkatraman, Hebert & Bagnell 2015 -- Improving Multi-step Prediction of Learned Time Series Models (DaD)](https://ojs.aaai.org/index.php/AAAI/article/view/9590). AAAI 2015. claim_ids: MECH-135.
- [Hafner et al. 2019 -- Learning Latent Dynamics for Planning from Pixels (PlaNet, latent overshooting)](https://arxiv.org/abs/1811.04551). ICML 2019, PMLR 97. claim_ids: MECH-135.
- [Asadi, Misra, Kim & Littman 2019 -- Combating the Compounding-Error Problem with a Multi-step Model](https://arxiv.org/abs/1905.13320). arXiv preprint. claim_ids: MECH-135, INV-088.
- [Hansen, Wang & Su 2022 -- Temporal Difference Learning for Model Predictive Control (TD-MPC)](https://arxiv.org/abs/2203.04955). ICML 2022, PMLR 162. claim_ids: MECH-135.
- [Somalwar, Lee, Pappas & Matni 2025 -- Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error](https://arxiv.org/abs/2504.01766). arXiv preprint. claim_ids: MECH-135, INV-088.

Consulted and deliberately not given entries: Hafner et al. 2020 (Dreamer, ICLR 2020, [arXiv:1912.01603](https://arxiv.org/abs/1912.01603)) -- cited inside the PlaNet entry for its "did not find latent overshooting ... necessary" statement, which is evidence *about* the PlaNet technique rather than a separate lever.

### Biology

- [Hassabis, Kumaran, Vann & Maguire 2007 -- Patients with hippocampal amnesia cannot imagine new experiences](https://doi.org/10.1073/pnas.0610561104). PNAS 104(5):1726-31. claim_ids: MECH-135.
- [Addis & Schacter 2008 -- Constructive episodic simulation: temporal distance and detail modulate hippocampal engagement](https://doi.org/10.1002/hipo.20405). Hippocampus 18(2):227-37. claim_ids: MECH-135.

Both retrieved via PubMed.

### Existing dirs not duplicated

- [`targeted_review_e2_forward_model_action_divergence`](../targeted_review_e2_forward_model_action_divergence/) (2026-05-28) -- the sibling the autopsy named as a strong methodological prior. Read in full before this pull. It covers **single-step action identifiability** (K actions collapsing to one predicted next-z_self) via PLSM, Contrastive RSSM and SWIRL, plus cerebellar/prefrontal forward-model biology. It does **not** address horizon depth, which is this review's entire axis. Its value here turned out to be double-edged: it is the reason "contrastive next-state" was on the candidate list, and Section 1 concludes that candidate does not carry over. The autopsy's instruction to treat it as a prior and not a substitute was correct.
- [`targeted_review_mech_135`](../targeted_review_mech_135/) (2026-03-29) -- cerebellar mental simulation (Ito 2008), MOSAIC parallel forward models (Wolpert 1998), cerebro-cerebellar forward model (Tanaka 2020), parallel world-model planning (Psenka 2026). Covers *parallel* forward models and their biological substrate; does not address multi-step rollout consistency or training-objective/usage-horizon mismatch. This review adds the depth axis to that claim's evidence.
- [`targeted_review_inv_088`](../targeted_review_inv_088/) (2026-07-13) -- tethering hypothesis, value-generalisation bounds, developmental axes. Concerns the representational-capacity framing of INV-088; does not address the rollout-dynamics pathway that V3-EXQ-108b dissociated from it.
- [`targeted_review_v3_hippocampal_rollout`](../targeted_review_v3_hippocampal_rollout/) and [`targeted_review_mech269b_vs_rollout_gating`](../targeted_review_mech269b_vs_rollout_gating/) -- "rollout" in the hippocampal-replay and gating senses respectively, not the learned-forward-model sense used here.

---

## What this synthesis does NOT do

- **Does not edit `substrate_queue.json`.** Two sessions held active `TASK_CLAIMS.json` claims on that exact file at start time -- `metaworker-chip-20260803-route-decomp-gate-fix` (13:49:53Z) and `metaworker-chip-20260803-sd094-causal-grid-world-fix` (14:15:42Z) -- so per the arbitration rule this session does not own it. **SD-e1-rollout-consistency-training therefore still reads `ready: false` with this lit-pull listed as unresolved.** The dependency is discharged by this document; flipping the flag, and revising the `implementation_hint` per Section 0 and Section 4, is left to whoever next holds that file. Flagged in the closing report and in `WORKSPACE_STATE.md`.
- **Does not edit `claims.yaml`.** MECH-135 and INV-088 dispositions are governance's, and the confirmed autopsy already carries the draft `evidence_quality_note` for INV-088.
- **Does not queue any experiments.** Section 4 recommends a probe; commissioning it is a `/queue-experiment` pass, not this skill's job.
- **Does not settle the (a)-versus-(b) question.** Section 0's action-blindness finding is code-verified as a fact about the interface; its *relative contribution* to the observed collapse is measured by Section 4's probe and is not asserted here.

---

*Author session: metaworker-chip-20260803-litpull-e1-rollout-consistency (chip_ref `chip-20260803-litpull-e1-rollout-consistency`), spawned from `/governance` session `epic-mirzakhani-4928b5`. Commissioned 2026-08-03T11:45:20Z; pull executed 2026-08-03T14:22:13Z.*
