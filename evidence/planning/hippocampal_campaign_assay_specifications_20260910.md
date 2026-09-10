# Hippocampal campaign: implementation-ready specifications for assays A and B

**Date:** 2026-09-10T07:08:58Z
**Status:** design specification only. This document registers no claim, changes no claim state, allocates no EXQ id, writes no experiment script, mutates no queue, starts no runner, and mints no evidence entry.
**Session:** `hippocampal-assay-spec-20260910` (Mac `DLAPTOP`, throwaway worktree off `origin/master` `5eace972fa`).
**Parents:**
- [campaign adjudication](../../docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md) §7A, §7B (the assay families this specifies)
- [replay-maintenance supplement](../../docs/thoughts/2026-09-09_hippocampal_replay_interface_maintenance_supplement.md) §6 (assay B revision, executable rival, staged gates)
- [literature tranche 3](hippocampal_translation_maps_literature_tranche_3_receiver_conditioning_temporal.md) §9 (amendments A1-A4, folded in below)
- [mutual-legibility implementation assays](../../docs/thoughts/2026-09-07_mutual_legibility_implementation_assays.md) §3, §4, §8, §9, §10, §20, §21, §22 (baseline hierarchy, bridge ladder, causal audit, manifold guard, the read-only-harness recommendation)
- [campaign scaffold](hippocampal_translation_maps_biology_campaign_20260909.md) (R1-R5)
**Claims in scope, none modified:** ARC-139, MECH-537, MECH-538, MECH-539, MECH-540, MECH-547, MECH-548, INV-105, INV-088, MECH-457.

---

## 0. Readiness verdict, stated before the designs

Three findings change what can be specified. All three were checked against the live repository, not assumed.

### 0.1 V3-EXQ-1010 has landed and it disqualifies the obvious sender

`evidence/experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3.json`, run `20260909T195348Z`, `outcome: PASS`, `interpretation.label: H-F-confirmed`.

Verbatim from the manifest: *the decision-relevant content is DESTROYED AT ENCODE TIME: no decoder in the capacity ladder recovers the oracle above the bar from the frozen latent, on a protocol the calibration anchor shows is sound and at a capacity that demonstrably memorises the training split.* Instrument gate green; `guards.anchor_sound = True`; `guards.can_memorise = True` (worst-seed train agreement 0.9996); `guards.diverged_rungs = []`; `n_seeds_clearing_at_some_capacity = 0`.

The adjudication §7A V3 gate said: *if 1010 confirms an inadequate sender under valid probe guards, test this family on a known information-preserving synthetic source or adequate PCA/raw control.* That gate has now fired. **The trained `z_world` is not an admissible source for either assay.** Using it would confound "no conditional-transformation gain" with "nothing to transform", which is exactly the H-F/H-C conflation the 978→1002→1008→1010 lineage spent four runs separating.

Two sources are measured-adequate on this same protocol, and both are already implemented:

| Source | Definition | Measured held-out oracle agreement | Provenance |
|---|---|---|---|
| `rawfield25` | the 25-dim agent-centred `resource_field_view` | 0.9735 worst seed | 1010 `instrument.rawfield_worst_seed_agreement`, worst cell `rawfield_ceiling|seed44` |
| `ws250_pca32` | PCA-32 of the 250-dim `world_state` | 0.868 mean, all seeds above the 0.80 bar | 1008 manifest; used in 1010 as the calibration anchor, `anchor_sound = True` |

`rawfield25` is the primary source for both assays. `ws250_pca32` is a **replication source**, run only after the primary source has produced a verdict — it is not a second factor.

### 0.2 The instrument does not exist

`ree-v3` contains **no** communication-subspace estimator, bridge ladder, principal-angle metric, causal-replacement harness, receiver-manifold guard, or dynamic-compatibility scorer. Verified by search over every `.py` in the repo for `latent_interfaces`, `reduced_rank`, `subspace_metrics`, `manifold_guard`, `principal_angle`, `communication_subspace`: zero hits. `ree-v3/analysis/` does not exist. `experiments/_lib/stats.py` contains `spearman` and `_average_ranks` and nothing else; there is no equivalence test anywhere in `experiments/`, and both assays require equivalence tests rather than non-significant differences.

So both assays are **instrument-blocked, not substrate-blocked**. In the work-graph vocabulary: the scientific question at each assay is `complex (probe-gated)` — running the assay is the probe. The gate in front of it is `complicated (buildable)`: prerequisite P0 in §4 is buildable on demand, needs no unknown, and needs no `ree_core` change. Neither assay is *blocked*.

### 0.3 Assay B's maintenance machinery is also absent, but belongs at the experiment layer

`ree_core/sleep/replay_sampler.py` (`SleepReplaySampler`, MECH-285 Phase B) is by its own docstring *a NO-OP CONSUMER* — draws are recorded as diagnostics and no downstream consumer sees them. `ree_core/sleep/cross_module_consolidation.py` (`CrossModuleConsolidator`) runs interleaved-vs-blocked gradient schedules over *module losses*; it carries no `(sender_episode, receiver_episode)` pairing and therefore cannot express correct-versus-shuffled pairing at matched marginals.

This is not a reason to build a `ree_core` pairing mechanism. §21 of the mutual-legibility assays doc forbids adding a universal `LatentBridge` to `ree_core` at this stage, and the diagnosis-without-changing-the-organism rule applies with full force. Assay B's maintenance arms are **experiment-layer**, on the `consolidation_lesion_harness.py` / V3-EXQ-702 injected-content precedent, over frozen endpoints. No `ree_core` change is specified by this document.

### 0.4 One repository divergence, reported not resolved

`docs/thoughts/2026-09-09_hippocampal_replay_interface_maintenance_supplement.md` exists in two different revisions: `origin/master` `38bf293cd9` (2026-09-10T06:28Z, 37,473 B) and the shared checkout's local commit `853e336bbb` (2026-09-10T06:34Z, 41,265 B). They are independent rewrites of the same path by two sessions, not one edited by the other. This specification is written against the **later, longer** revision (`853e336bbb`), whose §6.1-§6.6 supply assay B's gate structure and outcome table; the earlier revision's substantive content is a subset. Reconciling the two is not this session's work and nothing here depends on which one wins — the §6 content used below is present in the later revision only, and is cited as such.

---

## 1. Shared apparatus

Everything in §1 binds both assays. §2 and §3 state only what differs.

### 1.1 The seven rungs are reported separately, always

INV-105's ladder is the reporting contract, not a summary device. Every arm reports all seven, and no arm's verdict may be stated in the vocabulary of a rung it did not measure:

1. **encoded** — statistically present in the source (linear + capacity-laddered probe R², `_content_witness`)
2. **decodable** — recoverable by an external probe above the pre-registered bar
3. **natively accessible** — the frozen consumer uses it with no bridge (`L0_native`)
4. **bridgeable** — a constrained map at a declared complexity rung restores consumer use
5. **pairing-specific** — correct beats mismatched at matched marginals
6. **causally used** — ablating the message changes the consumer's committed action
7. **behaviourally useful** — `foraging_competence` moves on held-out environments

Local recall, decodability, pairing specificity, causal use and behaviour are five separate columns in every results table. A rescue at rung 4 is never written up as a result at rung 6 or 7.

### 1.2 Frozen endpoints

Both assays freeze both endpoints for the whole run. "Frozen" means: parameters are snapshotted before the first evaluation, hashed, and re-verified against the snapshot hash at every evaluation boundary; a mismatch aborts the cell. Only the declared bridge (assay A) or the declared maintenance machinery (assay B) may hold trainable parameters.

The consumer is pre-trained once per seed, before any arm, then frozen:

> **Frozen consumer C** — a `mlp128` (2-layer, hidden 128) policy head, trained by behaviour cloning on the *canonical* source encoding under the *canonical* frame and query, using `_make_decoder("mlp128", ...)` and `_train_decoder` from 1010. It is the same capacity rung 1010 used for its consumer readout (`off_consumer_rung_*`), so its capacity is calibrated against a measured reference rather than chosen fresh.

Consumer training data is disjoint from every episode block used to fit or evaluate a bridge (§1.5).

### 1.3 Budget matching — capacity, data, plasticity, optimisation

Every comparison in both assays is at **four** matched budgets, reported per arm in the manifest:

| Budget | Matched quantity | How |
|---|---|---|
| Capacity | total trainable parameter count of the arm's fitted object | `_capacity_report()` (1010) per arm; arms padded to the maximum by widening the lowest-capacity arm's bottleneck, never by adding depth |
| Data | number of training rows and number of distinct episodes | identical row indices across arms, by construction from one stored episode set |
| Optimisation | number of passes, optimiser, learning rate, grad-clip norm | `_train_decoder(..., passes=P)` with one shared `P`; `guards.grad_clip_norm = 1.0` as in 1010 |
| Plasticity (assay B only) | number of weight updates, total absolute weight change, update magnitude distribution | recorded per arm; arms outside a pre-declared band are red, not silently reported |

A conditional bridge has more inputs than an unconditional one. Capacity matching is therefore done on **parameter count**, and the unconditional arms receive the conditioning input as a **constant zero vector of the same width**, so the two differ in the *information* on that channel and not in its dimensionality. Whether a difference survives that control is the whole question.

### 1.4 Source, consumer, and the receiver-only control

- **Source** `S(e)`: `rawfield25` (primary). Replication: `ws250_pca32`.
- **Consumer** `C`: the frozen head of §1.2.
- **Receiver-only predictor** `R_only`: the same capacity rung, fitted on the receiver-side information *alone* (query index, receiver state index, receiver identity index, previous executed action) with the message channel zeroed. This is a mandatory arm in both assays, not an optional control.

The interpretive rule the adjudication states and tranche 3 §4.2(5) makes concrete: **a conditional bridge can recover performance by supplying information from the receiver rather than by translating the sender.** Therefore three decodings are reported separately and never summed:

1. `D_sender` — sender-only decoding of the target;
2. `D_surface` — decoding from the communication surface actually presented to the consumer;
3. `D_joint` — conditional joint decoding from (message, receiver state).

`D_joint > D_sender` with `R_only` already high is a receiver contribution, not translation. This is scored automatically, not left to prose.

### 1.5 Splits and leakage guards

`_split_episodes` (1002) splits by **episode**, never by step, because consecutive grid-world steps are strongly correlated. That is necessary and not sufficient here. Both assays use a three-level split:

| Level | Unit | Use |
|---|---|---|
| **E-block** | environment seed family (`seed*1000 + ep`, blocks of contiguous `ep`) | consumer pre-training (block 0) / bridge fitting (block 1) / model selection (block 2) / final test (block 3). Block 3 is opened once per assay. |
| **Compositional holdout** | (frame level × query level) cells | at least two cells are held out of *every* fitting and selection block and appear only in block 3 |
| **Repeated-use holdout** | trailing episodes of block 3 | used only for the stability measurement of §1.8 |

Leakage guards, each an abort condition rather than a note:

1. no episode index appears in two blocks;
2. no environment seed appears in two blocks;
3. the compositional holdout cells have zero rows in blocks 0-2, asserted by count;
4. model selection touches block 2 only; block 3 is read once, after all arms are frozen;
5. the previous-executed-action column (`_prev_action_vector`, 1002) is recorded as a first-class trivial predictor and every agreement is reported both raw and elevated over it — it is the strongest trivial predictor on this task at 0.568-0.582 held-out;
6. permutation controls preserve marginal difficulty and stay on-distribution (shuffle *within* the same frame/query/context stratum), because an off-distribution permutation measures distribution sensitivity rather than pairing specificity.

### 1.6 Primary metric and threshold

**Primary metric for both assays:** held-out **consumer-use agreement** — the fraction of held-out block-3 steps on which the *frozen consumer*, driven through the arm's interface, commits the query-specific oracle's action.

Not decoder accuracy: the object scored is the frozen consumer's committed action, so the metric sits at rung 6 (causally used) and not at rung 2 (decodable).

**Threshold.** The absolute bars are inherited, not invented: `AGREEMENT_BAR = 0.80` and `AGREEMENT_ELEVATION_MIN = 0.20` over the strongest trivial predictor, pre-registered in 1002 and carried unchanged through 1008 and 1010 (`pre_registered.agreement_bar`, `pre_registered.agreement_elevation_min`). They are calibrated on this exact task, this oracle, and this trivial-predictor family, which is why they are reused rather than re-derived.

The **primary estimand is a difference**, so it needs a difference bar. Following the standing effect-size rule (scale on the SD of the paired delta, plus an absolute floor):

> A contrast is **positive** iff, on block 3, the paired per-seed difference satisfies **both** `mean(Δ) >= 0.05` absolute agreement **and** `mean(Δ) >= 2 x SD(Δ)` across seeds, on at least `seed_majority = 2` of 3 seeds individually.

The absolute floor of 0.05 is set at roughly one third of the measured elevation of the trained latent over the trivial predictor in this lineage (1002: trained latent 0.664 against a trivial predictor at ~0.58), so an effect below it is not distinguishable from the noise band the lineage has already characterised. `seed_majority = 2` is 1010's own pre-registered value.

**Equivalence, where the design requires sameness rather than difference** (matched local competence, sender-state nulls, stable-interface arms), is asserted by a **two one-sided tests** procedure at a pre-declared band, never by a non-significant difference. The band is `±0.05` agreement — the same magnitude as the positivity floor, so "different" and "equivalent" cannot both be satisfiable.

### 1.7 Instrument-readiness gates

Both assays are refused, before any scientific arm runs, unless every one of these is green. Each is measured in-run, never imported as a threshold from a prior run.

| Gate | Condition | Source of the number |
|---|---|---|
| G1 source adequacy | the primary source clears `AGREEMENT_BAR` at some capacity rung, worst seed | 1010's `rawfield_ceiling` design; re-measured in-run |
| G2 consumer range | oracle competence − random competence spans a usable range on the same env rung | 1010 `instrument.oracle_competence_worst_seed = 45.75` against a random policy; re-measured |
| G3 consumer floor | the frozen consumer, at `L0_native` on the canonical frame/query, clears the bar | re-measured |
| G4 known-inverse positive control | applying the declared invertible transform and its exact analytic inverse returns the consumer to within the §1.6 equivalence band of `L0_native` | in-run |
| G5 negative-control floor | zero message and moment-matched random message both sit at or below the trivial-predictor level | in-run |
| G6 capacity witness | the highest ladder rung memorises the fitting block (train agreement ≥ `memorise_floor = 0.95`) | 1010 `guards.memorise_floor` |
| G7 no divergence | no arm's optimisation diverged; `diverged_rungs` empty | 1010 `guards.diverged_rungs` |
| G8 degeneracy | every reported DV passes `metric_is_degenerate` / `check_degeneracy` and the declared `dv_headroom_check` | `experiments/_metrics.py` |

A red gate is a **refusal with a record**, not a FAIL: the run stops, the manifest carries the gate state, and no scientific leg is adjudicated. This is the same combination discipline 1010 used, where `PASS` meant the instrument was sound and the hypothesis leg reached a verdict, and the science lived in `hypothesis_verdict` rather than in `PASS`/`FAIL`.

### 1.8 Repeated-use stability (MECH-548)

Both assays measure it, because a one-step rescue that collapses under repetition does not license architectural adoption. On the repeated-use holdout, the interface is applied closed-loop for `N = 20` consecutive consumer steps, feeding the consumer's own resulting state forward. Reported: agreement at step 1, agreement at step N, the fitted decay slope, and the step index at which agreement first crosses below the trivial-predictor level (or `None`).

An arm whose step-1 agreement is positive and whose step-N agreement is not is recorded as **one-step-only**, never as a rescue.

### 1.9 Manifest and provenance contract

Both assays write through `experiments/pack_writer.write_flat_manifest` and `experiment_protocol.emit_outcome`, with `architecture_epoch: "ree_hybrid_guardrails_v1"`, `run_id` ending `_v3`, `experiment_purpose: "diagnostic"`, per-arm `arm_cell` fingerprints (`experiments/_lib/arm_fingerprint.py`), a `substrate_pin` and `substrate_scope_guard`, and a `precondition_gate` entry per arm. Per-arm fields are indexed `(arm_id, seed)`, seed-major. Timestamps come from the system clock in UTC. All printed output is ASCII.

---

## 2. Assay A — frozen-endpoint index/native retrieval and fixed routing versus frame-conditioned and receiver-conditioned access

### 2.1 Question

At a frozen interface with an adequate source, does a **conditional** transformation add held-out consumer use beyond good retrieval, fixed partner-specific routing, and frame conditioning — and if it does, is the gain attributable to the sender's content or to information the receiver supplied?

### 2.2 Manipulated variables

One factor at Gate A1: **access mechanism**, seven levels, all at matched budgets (§1.3).

| Arm | Mechanism | What it stands for |
|---|---|---|
| `A0_native` | no bridge; consumer reads the source directly | rung 3, native accessibility |
| `A1_source_only` | low-rank affine bridge (MECH-538 rung L3), source only | the unconditional constrained bridge |
| `A2_index_route` | episode-index lookup returning the stored native associate, then a fixed partner-specific linear route | the rival: indexed associative reinstatement + routing, no conditional transform |
| `A3_frame_cond` | bridge conditioned on the frame label only | R2, frame mediation |
| `A4_receiver_state_cond` | bridge conditioned on receiver *state* | MECH-547 strong reading, `T(A,B)` |
| `A5_receiver_ident_cond` | bridge conditioned on receiver *identity* | tranche 3 A1: conditioning on who is listening |
| `A6_selector_k` | message constrained to a k-way discrete frame/rule index; receiver plus query supply the mapping | tranche 3 A3, motivated by T3-10 |
| `A7_receiver_only` | message channel zeroed; receiver-side information only | the receiver-only information control (§1.4) |

**Frame** and **receiver query** are manipulated independently over the *same stored episodes*, so nothing depends on two separately-driven rollouts coinciding — the paired-step discipline 1002 established in `_collect_episodes`.

- **Frame levels:** (i) egocentric native (the 5×5 `resource_field_view` as emitted); (ii) a known invertible rotation of the local field by 90°/180°/270° with the action-label set rotated correspondingly — information-preserving with an exact analytic inverse, which is G4's positive control; (iii) an allocentric region index derived from `env.agent_x`/`env.agent_y` via `rebinding_functional_harness.region_of(env, g_partition)`; (iv) **event/segment index** from `ree_core/hippocampal/event_segmenter.py` (tranche 3 A4); (v) **elapsed-tick coordinate** within episode (tranche 3 A4).
- **Receiver query levels:** k=3 query heads with oracle labels computable from env ground truth — `approach_nearest_resource` (the `LocalViewGreedyPolicy` target), `avoid_nearest_hazard`, `hold_position`. Receiver *state* is which query the head is currently executing; receiver *identity* is which of the k frozen heads the message is aimed at. Splitting these is tranche 3 A1, and it is the difference between conditional access and fixed routing.

### 2.3 Held constant

Frozen source and consumer weights (hash-verified per §1.2); the stored episode set and its row order; capacity, data, optimisation and conditioning-channel width (§1.3); the receiver's query information, which every arm receives; output norms, checked by the manifold guard; the oracle label function per query; the environment rung (`x734._env_kwargs_for_rung(RUNG)`, `STEPS_PER_EPISODE = 200`); model selection on block 2 only.

### 2.4 Positive controls

1. **Known invertible frame transform with its exact inverse** (G4). If this does not restore the consumer, the instrument cannot detect any transformation effect and the run is refused.
2. **Adequate-source ceiling** — `rawfield25` at the capacity ladder's top rung, the direct analogue of 1010's `rawfield_ceiling` (0.9735 worst seed).
3. **A query-selection task with no format conversion** — a condition in which the correct answer requires selecting *which* stored item to return but no change of format. An arm that cannot solve this has a retrieval defect, not a translation defect.

### 2.5 Negative controls

1. zero message;
2. moment-matched random message (mean/variance preserved, content destroyed);
3. wrong-episode message drawn from the same frame/query stratum;
4. **receiver-state permutation** within query stratum;
5. **receiver-identity permutation** within query stratum — separate from (4), per tranche 3 A1;
6. shuffled frame label;
7. `A7_receiver_only`;
8. **sender-state null** (tranche 3 A2): re-run `A1_source_only` under each receiver state and require equivalence at the §1.6 band. If `S(e)` differs across receiver states, part of any `T(A,B)` advantage is a sender effect, and the T3-04 phenotype — an internal state degrading the sender's code with inputs matched — is a named biological instance of exactly that;
9. same-action mismatch (another state sharing the action label), to separate action-class traffic from state-specific content.

All permutations are within-stratum, so marginal difficulty is preserved (§1.5 guard 6).

### 2.6 Staging — decisive contrasts before any factorial

**Gate A0 — instrument.** G1-G8 of §1.7, plus the three positive controls. Refuse on red.

**Gate A1 — the decisive contrast.** The eight arms of §2.2 on the canonical frame and the canonical query only. One factor, no crossing.

> **Primary estimand:** the block-3 consumer-use gain of `A4_receiver_state_cond` over the **best-performing** of {`A1_source_only`, `A2_index_route`, `A3_frame_cond`, `A5_receiver_ident_cond`, `A6_selector_k`}, at matched budget, judged by §1.6.

Taking the best rival rather than a mean is deliberate: the question is whether conditional access is *necessary*, and a mean lets a weak rival flatter it.

**Gate A2 — specificity, only if A1 is positive.** Receiver-state permutation, receiver-identity permutation, `A7_receiver_only`, the sender-state null, the three separated decodings (`D_sender`, `D_surface`, `D_joint`), the manifold guard, and repeated-use stability. A gain that survives state permutation but dies under identity permutation is **fixed routing** and is reported as such.

**Gate A3 — frame × receiver factorial, and the temporal-frame levels.** Only after A1 and A2. Adds the compositional holdout cells (frame level × query level unseen in fitting) as the decisive test of whether the mechanism composes.

**Replication.** `ws250_pca32` repeats Gate A1 only, after Gate A3 has completed on the primary source.

### 2.7 Strongest falsifier

> A well-trained `A2_index_route`, or the k-way `A6_selector_k`, matches `A4_receiver_state_cond` on the compositional holdout cells at matched capacity, data, optimisation and conditioning-channel width — **or** `A4`'s advantage survives receiver-state permutation intact.

Either result makes the strong reading of R3 / MECH-547 unnecessary at this interface. The second is the sharper of the two: an advantage that a state permutation cannot touch was never conditioned on state.

This falsifier is not a formality. Tranche 3 §4.2(2) records that the single most discriminating located study (T3-10, Julian et al. 2026) points the other way — a fixed reactivated hippocampal message that selects a rule, with the receiver and the cue supplying the mapping — and that MECH-547's confirming signature has no biological counterpart at all. The prior favours the falsifier.

### 2.8 Interpretation of every outcome

| Result | Permitted statement | Forbidden statement |
|---|---|---|
| `A4 > A5 > all others`, gain dies under state permutation, `A7` low, `D_joint ≈ D_sender` | receiver-state-conditioned access adds held-out consumer use at this interface, attributable to sender content | that a biological hippocampal mechanism does this |
| `A4 > others`, gain survives state permutation, dies under identity permutation | fixed partner-specific routing, not conditioning (T3-02/T3-03 phenotype) | receiver conditioning |
| `A4 ≈ A6_selector_k` | a low-cardinality frame/rule selector plus the receiver's own query suffices; the strong R3 reading is unnecessary here | that the interface is unconditional in general |
| `A4 ≈ A2_index_route` | indexed reinstatement plus routing suffices; the conditional transform earns nothing | any interface claim |
| `A3_frame_cond ≈ A4`, both > `A1` | frame mediation (R2) accounts for the gain; receiver state adds nothing beyond it | receiver conditioning |
| `A7_receiver_only` high and `D_joint >> D_sender` | the receiver supplied the information; the bridge introduced rather than translated it | translation, rescue, or access restoration |
| sender-state null fails equivalence | the sender's code differs across receiver states; the `T(A,B)` contrast is confounded and unadjudicable as designed | any conditional-access conclusion |
| all arms ≈ `A0_native` | no interface failure at this locus under this source; nothing to translate | that translation mechanisms are unnecessary generally |
| decoding high, consumer use flat | the ladder stops at *decodable*/*bridgeable*; the consumer is insensitive | causally used, behaviourally useful |
| consumer use up, `foraging_competence` flat | rung 6 without rung 7; the behavioural instrument may lack range — report the measured range | behavioural benefit |
| step-1 positive, step-N at trivial level | one-step-only; recurrent instability (MECH-548) blocks adoption | rescue or maintenance |
| mapped states fail the manifold guard | off-manifold shortcut; the consumer was driven with states it never natively occupies | interface repair |

### 2.9 Compute

Frozen endpoints and a field/PCA source mean **no agent warm-up per cell** — which is what made 1010 expensive (92,211 s wall on `DLAPTOP` for 48 cells, dominated by `_warm_off_agent`). The cost here is episode collection, adapter fits, and rollouts.

Reference points: 1002 = 18,851 s on `ree-cloud-2` (3 seeds, agent-warmed arms); 1008 = 32,260 s on `ree-worker-3` (3 seeds, agent-warmed).

| Stage | Cells | Estimate (cloud worker) |
|---|---|---|
| Gate A0 | 3 seeds × 4 | ~0.5 h |
| Gate A1 | 3 seeds × 8 arms | ~2.5 h |
| Gate A2 | 3 seeds × 9 controls | ~2 h |
| Gate A3 | 3 seeds × (5 frames × 3 queries, holdout-scored) | ~4 h |
| Replication (`ws250_pca32`, A1 only) | 3 seeds × 8 | ~2.5 h |
| **Total** | | **~11.5 h**, one cloud worker, single run |

Route to a cloud worker, not the Mac. Estimate carries roughly a 2× uncertainty band until P0's self-test measures a per-cell cost; if Gate A0 exceeds 1.5 h, stop and re-cost rather than continuing.

### 2.10 Exact reusable code components

Reused verbatim, no modification:

| Path | Symbols |
|---|---|
| `ree-v3/experiments/v3_exq_1002_zworld_actor_adequacy_oracle_adapter.py` | `_collect_episodes`, `_split_episodes`, `_localfield_vector`, `_rawfield_features`, `_prev_action_vector`, `_fit_standardiser`, `_apply_standardiser`, `_standardiser_report`, `_StandardisedNet`, `_agreement`, `_state_blind_agreement`, `RawFieldAdapterPolicy`, `_participation_ratio`, `AGREEMENT_BAR`, `AGREEMENT_ELEVATION_MIN`, `BC_TRAIN_FRAC`, `LOCALFIELD_KEY`, `RESOURCE_FIELD_DIM` |
| `ree-v3/experiments/v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis.py` | `_world_state_features`, `_world_state_pca_stats`, `_random_orthonormal`, `_LinearProjection`, `_inv_sqrt_psd`, `_ZCAWhiten`, `_decision_subspace_retention`, `_oracle_rule_actions`, `_decode_oracle_agreement`, `_TransformedNet`, `WorldStateAdapterPolicy`, `_r2`, `_lin_decode_r2` |
| `ree-v3/experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py` | `_rung_spec`, `_make_decoder`, `_capacity_report`, `_train_decoder`, `_train_field_decoder`, `_agreement`, `_content_witness`, `_r2_per_coord`, `_best_over_rungs`, `_LinearReadout`, `_DeepReadout`, the capacity ladder |
| `ree-v3/experiments/v3_exq_734_env_difficulty_competence_recovery_sweep.py` | `_make_env`, `_env_kwargs_for_rung`, `STEPS_PER_EPISODE`, `PPOPolicyNet` |
| `ree-v3/experiments/_lib/capability_eval.py` | `Policy`, `RandomPolicy`, `OraclePolicy`, `LocalViewGreedyPolicy`, `rollout_episode`, `nearest_resource_manhattan` |
| `ree-v3/experiments/_lib/rebinding_functional_harness.py` | `region_of`, `min_region_visits_floor`, `label_shuffle_alignment`, `anchor_shuffle_alignment` |
| `ree-v3/experiments/_lib/arm_fingerprint.py` | `arm_cell`, `reset_all_rng` |
| `ree-v3/experiments/_lib/precondition_gate.py` | per-arm gate construction and adjudication |
| `ree-v3/experiments/_lib/substrate_pin.py`, `substrate_scope_guard.py` | substrate identity and scope pinning |
| `ree-v3/experiments/_metrics.py` | `metric_is_degenerate`, `metric_groups_are_degenerate`, `check_degeneracy`, `dv_achievable`, `dv_headroom_check`, `dv_floor_control_check`, `p0_readiness_gate` |
| `ree-v3/experiments/pack_writer.py` | `write_flat_manifest` |
| `ree-v3/experiment_protocol.py` | `emit_outcome` |
| `ree-v3/ree_core/hippocampal/event_segmenter.py` | `EventSegmenter`, `BoundaryEvent` (frame level iv only) |
| `ree-v3/ree_core/environment/causal_grid_world.py` | `CausalGridWorld` (`agent_x`, `agent_y`, `resource_field_view`, `world_state`) |

Required from prerequisite P0 (§4), which does not exist yet: `interface_probe.bridge_ladder`, `interface_probe.causal_replacement`, `interface_probe.manifold_guard`, `interface_probe.communication_subspace`, `interface_probe.principal_angles`, `stats.tost_equivalence`.

---

## 3. Assay B — controlled task-relevant drift with correct versus shuffled intersystem replay, against local rehearsal and adaptation

### 3.1 Question

After a controlled change breaks an established interface while both endpoints keep their local information and competence, does **correctly paired** intersystem replay restore the receiver's causal use of the sender — beyond shuffled pairing, beyond receiver-local self-healing, and beyond ordinary paired co-exposure?

### 3.2 Operational object

A trained interface from `S(e)` to the frozen consumer `C`, required for a held-out consumer-dependent task. Before any maintenance phase, freeze and snapshot-hash: the endpoint-local probes (sender information, consumer competence), the native transfer readout, the held-out consumer-use evaluation, the replay item set and their identities, and the no-drift reference geometry and communication subspace.

### 3.3 Manipulated variables

Staged, per the supplement's §6.3 gate structure. Pairing and timing are **separate contrasts**; the interaction is tested only if each instrument is independently valid.

**Gate B0 — validate the failure as interface-specific.** Drift factor, four levels, no maintenance:

| Arm | Drift | Expected |
|---|---|---|
| `B0_nodrift` | none | transfer intact |
| `B0_relevant` | known invertible rotation applied to the source encoding **within** the consumer's decision subspace | transfer lost, endpoints intact |
| `B0_unused` | same-magnitude rotation confined to the **null space** of the decision subspace | transfer intact — the instrument's negative control |
| `B0_inverse` | `B0_relevant` plus the exact analytic inverse adapter | transfer restored — the positive control |

The decision subspace is identified with `_decision_subspace_retention` (1008), which already computes retention of the decision-relevant directions of a linear map; the rotation is generated with `_random_orthonormal` (1008) restricted to that subspace and to its complement respectively.

Proceed only if `B0_relevant` loses transfer while both endpoints' local probes stay inside the §1.6 equivalence band, `B0_unused` preserves transfer, and `B0_inverse` restores it. Any other pattern refuses the assay: no interface problem was created, so there is nothing for maintenance to repair.

**Gate B1 — decisive mechanism set**, under the validated relevant drift. Maintenance factor, six levels:

| Arm | Maintenance | Role |
|---|---|---|
| `B1_none` | no update | floor |
| `B1_paired` | correctly paired `(S(e), C-activation(e))` intersystem replay | the hypothesis |
| `B1_shuffled` | independently shuffled sender-receiver pairs, **identical marginals** per side | pairing-specificity control |
| `B1_selfheal` | receiver-local self-healing: pre-drift low-dimensional receiver scaffold, label-free Hebbian updates from sender activity and the receiver's own current output, homeostatic gain/bias restoring pre-drift mean and variance targets, receiver-local completion from its recurrent state | the executable rival (Rule-O'Leary + cortical completion) |
| `B1_rehearsal` | ordinary full-example co-exposure at matched data | matched-data upper bound |
| `B1_activity` | matched plasticity with content-free activity | activity/plasticity control |

`B1_selfheal` receives the same sender samples, receiver activations, update count, parameter budget and plasticity magnitude as `B1_paired`, and **must not** receive the correct sender-receiver episode labels. That asymmetry is the entire content of the contrast.

> **Primary estimand:** the block-3 held-out consumer-use gain of `B1_paired` over `B1_shuffled` under relevant drift, **relative to the same contrast under `B0_nodrift`** (a difference of differences, so a generic pairing effect that exists without drift cannot be read as repair).
> **Decisive rival contrast:** `B1_paired` versus `B1_selfheal`.
> **Specificity check:** `B1_paired` versus `B1_rehearsal` — whether the effect is replay-specific or merely relearning from paired data.

**Gate B2 — timing, only after content specificity is established.** Pairing held fixed at `B1_paired`; consumer plasticity enabled in the empirically effective window versus the same window shifted versus independently shuffled. Match event count, phase occupancy, activity magnitude and total absolute weight change. Do **not** interpret a timing interaction if the shifted condition changes data exposure or update magnitude.

**Two interfaces, as MECH-540 requires.** Every gate runs on two interfaces simultaneously: `I_drift` (`rawfield25` → consumer head 1, drifted) and `I_stable` (`ws250_pca32` → consumer head 2, undrifted). A maintenance mechanism that improves both equally is generic plasticity; the claim is a plasticity/stability division of labour, so selectivity is part of the primary reporting, not a follow-up.

### 3.4 Held constant

Endpoint snapshots re-verified before each evaluation; local task information and competence at both endpoints (asserted by equivalence test, §1.6, not by a non-significant difference); replay item set, item frequencies, activity magnitude, number of updates, and plasticity capacity across maintenance arms; the drift transformation, which is applied to the source encoding only and leaves the source's *local* task content intact by construction (rotation is invertible); only the designated maintenance machinery may update anything.

**Prospective matching of local memory quality.** The supplement is explicit that matching must be designed or titrated *before* outcomes are seen, never produced by conditioning post hoc on a treatment-affected memory score. Concretely: the per-arm update budget is titrated in Gate B0 so that every arm's post-maintenance endpoint-local probe lands inside the equivalence band, and that titration is frozen before Gate B1 runs.

### 3.5 Positive and negative controls

**Positive:** `B0_inverse` (known inverse adapter restores access); a deliberate disruption of decision-relevant coordinates that reduces transfer while local competence stays inside the equivalence band.

**Negative:** `B0_unused` (non-task-direction drift); `B1_shuffled` with each side's replay histogram unchanged; `B1_activity` (matched plasticity, no content); matched event count at the wrong update phase (Gate B2); `A7`-style receiver-only predictor.

**Ceiling guard:** if `B0_nodrift` transfer is at ceiling, the difference-of-differences estimand is undefined. Tune task difficulty via the environment rung, or report the ceiling. Do not manufacture a maintenance interaction by leaving a ceiling in place.

### 3.6 Dependent variables, kept separate

Pre/post cross-system consumer use; correct-episode specificity; **sender local decodability**; **consumer local recall and competence**; estimated bridge complexity (the minimum ladder rung clearing the criterion) and output dimensionality, as two distinct measures — Kerrén-style retrieval expansion and MECH-538 bridge complexity can move independently; communication-subspace overlap by principal angles; transition compatibility (MECH-539, one-step and multi-step); repeated-use stability (§1.8); **per-code drift rates** — transfer-relevant versus transfer-irrelevant directions measured separately, which tranche 3 debt 9 identifies as precisely the condition Gate B0 must verify and which T3-22 shows can differ within one population.

Subspace overlap and transfer are reported separately. A stable subspace with intact behaviour is evidence that repair was *unnecessary*; a rotated subspace without behaviour rescue is not repair.

**Intrinsic-drift rival.** Tranche 3 debt 8 adds a rival the supplement's list does not carry: drift that offline activity does not arrest (T3-25, LEC drift continuing through sleep with an apparently intrinsic origin). Its computational counterpart here is an arm in which drift continues *during* the maintenance phase at the same rate as during the pre-maintenance phase. Include it as `B1_none` measured across the maintenance interval rather than only at its endpoints — that is the observation that separates "maintenance arrested drift" from "drift stopped anyway".

### 3.7 Strongest falsifier

> Under a verified transfer-breaking but locally information-preserving drift, `B1_selfheal` — label-free — restores held-out consumer use to the same level and the same repeated-use durability as `B1_paired`, while `B1_shuffled` is no better than `B1_none` after update and every local-memory measure stays inside the equivalence band.

That result attributes the effect to invariant geometry plus local co-adaptation, and pair-specific interface repair is unnecessary in the tested regime.

Two earlier stop conditions carry equal weight and must be checked first:

1. if relevant drift does not impair native transfer, active repair was not needed and the assay has no object;
2. if `B1_paired` improves local memory quality, the result is consolidation-contaminated and cannot answer the target question.

### 3.8 Interpretation of every outcome

| Result | Permitted statement | Forbidden statement |
|---|---|---|
| `B1_paired > B1_shuffled` and `> B1_selfheal`, local memory equivalent, consumer-required behaviour restored, stable at step N, selective across the two interfaces | supports pair-specific interface repair **in this assay** | that biological replay does this; that the hippocampus does this |
| `B1_paired ≈ B1_selfheal > B1_shuffled` | access can be maintained by a local adaptive readout; pair-specific replay is not necessary | interface repair |
| `B1_paired ≈ B1_rehearsal > B1_shuffled` | paired experience relearns the mapping; replay specificity is unearned | replay-dependent maintenance |
| all maintenance arms rescue equally | generic plasticity, invariant subspace, or an insufficiently selective perturbation | selectivity of any kind |
| `B1_paired` improves local memory **and** transfer together | consolidation-compatible; the target question is unresolved | interface repair |
| subspace stable and native transfer intact after drift | no interface failure under this transformation; repair unnecessary | that repair mechanisms do not exist |
| geometry changes, no consumer-use recovery | representational reorganisation | functional repair |
| rescue at step 1, collapse by step N | one-step-only; MECH-548 instability blocks adoption | maintenance |
| both interfaces improve equally | generic; MECH-540's plasticity/stability division of labour is unsupported | selective interface maintenance |
| drift continues at the same rate through the maintenance interval in `B1_none` and in the rescued arm | drift is intrinsic and not arrested; any rescue is compensation, not stabilisation | that maintenance arrested drift |
| local recall improves only | consolidation | interface repair |

### 3.9 Compute

| Stage | Cells | Estimate (cloud worker) |
|---|---|---|
| Gate B0 (2 interfaces × 4 drift arms × 3 seeds) | 24 | ~2 h |
| Budget titration (frozen before B1) | — | ~1 h |
| Gate B1 (2 interfaces × 6 maintenance arms × 3 seeds) | 36 | ~5 h |
| Gate B2 (2 interfaces × 3 timing arms × 3 seeds), conditional | 18 | ~3 h |
| Repeated-use stability, all surviving arms | — | ~1.5 h |
| **Total** | | **~12.5 h** if B2 runs, ~9.5 h if it does not |

Same 2× uncertainty band and the same stop rule as §2.9. Assay B should not be costed or scheduled until assay A's Gate A0 has produced a measured per-cell cost on the shared apparatus.

### 3.10 Exact reusable code components

Everything in §2.10, plus:

| Path | Symbols | Use |
|---|---|---|
| `ree-v3/experiments/_lib/consolidation_lesion_harness.py` | `build_pipeline_agent`, `diffuse_perturb`, `phase_integrity_at_sigma`, `_rms` | the experiment-layer offline-phase precedent and its per-phase output-quality readouts |
| `ree-v3/experiments/_lib/gradient_reencode.py` | `ObservationCapture`, `reencode_z_with_grad`, `reencode_batch_z`, `latent_stack_param_snapshot`, `latent_stack_moved` | asserting that the arms which must not move an endpoint did not move it, and that the arms which must did |
| `ree-v3/experiments/_lib/trace_store.py`, `stream_recorder.py` | trace sink, per-step recorder | replay item storage with stable identities |
| `ree-v3/experiments/_lib/matched_aux_targets.py` | matched auxiliary target construction | budget matching across maintenance arms |
| `ree-v3/experiments/_lib/rebinding_functional_harness.py` | `label_shuffle_alignment`, `anchor_shuffle_alignment`, `reacq_latencies` | shuffle controls with preserved marginals; re-acquisition latency |
| `ree-v3/ree_core/sleep/cross_module_consolidation.py` | `CrossModuleConsolidator`, `CrossModuleConsolidatorConfig`, `VALID_SCHEDULES` | **read for its interleaved/blocked schedule contract only** — it carries no pairing and is not the maintenance mechanism |
| `ree-v3/ree_core/sleep/replay_sampler.py` | `SleepReplaySampler` | **read for the broad-pool draw semantics only** — it is a declared no-op consumer |

Required from P0, additionally to §2.10: `interface_probe.dynamic_compatibility`, `interface_probe.per_code_drift`.

---

## 4. Prerequisite P0 — the smallest thing that must exist first

**Not built by this session, by instruction and by scope.** Specified so that the build is a `complicated (buildable)` step with no design left in it.

P0 is exactly the read-only harness §22 of the mutual-legibility assays doc already recommends, plus one statistics helper. It changes no `ree_core` file, adds no module to the agent, and is used only over frozen checkpoints and recorded trajectories.

### 4.1 `ree-v3/experiments/_lib/interface_probe.py`

| Function | Contract |
|---|---|
| `capture(...)` | records, per aligned step: run/seed/episode/timestep, environment and layout identifiers suitable for block splitting, the sender tensor before any bridge, the receiver input tensor **at the actual consumption point**, receiver pre/post-activation, candidate/action identity, task targets, committed action, behaviour variables, provenance (observed / replayed / simulated), phase, endpoint weight hashes, and any active gates or precision weights. The receiver variable must be the signal the live consumer actually reads, not a convenient neighbouring tensor. |
| `communication_subspace(X, Y, ranks)` | cross-validated reduced-rank regression, ranks `1..min(16, dim)`; returns per-rank held-out receiver-prediction score and the selected rank. |
| `principal_angles(U, V)` | principal angles and subspace overlap between two bases; used for pre/post and cross-seed stability. |
| `bridge_ladder(...)` | L0 identity/native, L1 orthogonal Procrustes, L2 affine, L3 low-rank affine, L4 constrained nonlinear (narrow bottleneck, weight decay, no recurrence), L5 high-capacity upper bound. Returns, per level: parameter count, training row count, held-out receiver-state error, downstream behavioural effect, out-of-distribution receiver-state score. L5 success is reported as an information-in-principle statement and is never reported as a plausible interface. |
| `causal_replacement(...)` | correct / mismatched (same gross distribution) / zero / moment-matched random / same-action mismatch / same-context mismatch, all within-stratum. Returns the five interpretive categories of the assays doc §10 as an enum, not as prose. |
| `manifold_guard(...)` | Mahalanobis distance under native receiver-state covariance, k-NN distance to native states, per-dimension norm checks, receiver activation saturation rate, and consumer hidden-state trajectory distance after one and after N steps. |
| `dynamic_compatibility(...)` | one-step and multi-step compatibility of `receiver_transition(T(x_t), a_t)` against `T(x_{t+1})` (MECH-539). |
| `per_code_drift(...)` | drift rate measured separately in transfer-relevant and transfer-irrelevant directions of a declared decision subspace (tranche 3 debt 9). |

Every function is pure over its inputs, holds no agent reference, and writes nothing.

### 4.2 `ree-v3/experiments/_lib/stats.py` — one addition

`tost_equivalence(a, b, band)` — two one-sided tests at a caller-declared band, returning the decision and both one-sided p-values. Required because §1.6 forbids asserting sameness from a non-significant difference, and no equivalence test exists anywhere in `experiments/` today.

### 4.3 Self-test and contract tests

`interface_probe` ships a `--selftest` that runs the whole ladder on a **synthetic** sender/receiver pair with a known invertible relation, and asserts: L1 recovers a pure rotation; L0 fails and L3 succeeds on a known low-rank relation; `causal_replacement` returns `correct >> mismatched ≈ random` on a pairing-specific synthetic and `correct ≈ mismatched >> zero` on a generic-channel synthetic; `manifold_guard` fires on a deliberately off-manifold map. Contract tests land under `ree-v3/tests/contracts/`.

The self-test is also the **cost meter**: it reports per-cell wall time, which is what converts §2.9 and §3.9 from estimates into schedulable numbers.

### 4.4 What P0 must not become

No `LatentBridge` in `ree_core`. No global CKA/RSA alignment objective. No optimisation of communication-subspace rank without a competence constraint. No treatment of L5 success as evidence the source was adequate. No probe success substituted for a causal content test. And no sleep-side interface assay until a waking interface metric has demonstrated stability and range — which is Gate A0 and Gate B0 doing their job.

---

## 5. Boundaries of this document

- No EXQ id is allocated. No entry is added to `ree-v3/experiment_queue.json` (0 pending at the time of writing). No experiment script is written. No runner is started.
- No claim is registered, promoted, demoted, or edited. ARC-139, MECH-537-540, MECH-547, MECH-548, INV-105 and INV-088 are cited as the scope this design bears on and are unchanged.
- No experiment is marked reviewed and no evidence entry is minted.
- Assay C (developmental path at matched mature interface) is **not** specified here. The adjudication routes it to a later developmental substrate consistent with MECH-362/Q-057, and states that A and B have higher immediate information value. Nothing in this document changes that routing.
- Tranche 3's amendments A1-A4 are folded into assay A above (A1 → §2.2 arms `A4`/`A5` and §2.5 controls 4/5; A2 → §2.5 control 8; A3 → §2.2 arm `A6_selector_k`; A4 → §2.2 frame levels iv/v with the recognition/order and per-code-drift reporting requirements). Tranche 3 §12 records that those amendments require a separate governed decision; this document is the specification of them, not that decision.
- Implementation requires the standard route: `/queue-experiment` for any script and queue entry, and a governed decision on whether to spend the compute. Prerequisite P0 (§4) is `/implement-substrate`-shaped experiment-layer work, not a `ree_core` change.
- Four pending-review items and a diverged `REE_assembly` shared checkout were present at session start; neither was touched.

## 6. Immediate next step, stated as one thing

Build P0 (§4) and run its `--selftest`. Nothing in §2 or §3 can start before it exists, and its self-test is what turns both compute estimates into commitments. Assay A Gate A0 is the first scientific step after that, and its result decides whether Gate A1 is worth its ~2.5 h.
