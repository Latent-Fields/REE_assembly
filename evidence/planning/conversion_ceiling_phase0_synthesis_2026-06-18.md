# Committed-Action-Diversity "Conversion Ceiling" — Phase 0 Disambiguation Synthesis

**Date:** 2026-06-18
**Method:** 7-agent characterize -> synthesize -> adversarial-critic workflow (read-only over manifests, confirmed failure-autopsies, and ree-v3 code). Run `wf_c03ff4f4-d45`.
**Question:** Is the recurring "diversity exists at the scoring/proposer layer but collapses at committed action (committed_action_class_entropy ~ 0)" failure ONE root mechanism or several?

## Verdict: NOT one wall. A constellation of four mechanistically-distinct loci sharing one surface symptom.

The "single root = z_world candidate collapse (GAP-A)" hypothesis is **falsified**. The load-bearing disproof: in `V3-EXQ-569h` the upstream candidate pool is demonstrably diverse at the moment selection fails (`cand_world_pairwise_dist 0.095`, `modulatory_channel_route_range 0.31`, both supra-floor on 3/3 seeds, the range reaching the E3 accumulator) — yet the committed-action distribution does not robustly diversify. Diverse input, flat output. If A were the sole root those statistics would be ~0.

| Root | Layer | Status (2026-06-18) | Disposition |
|------|-------|---------------------|-------------|
| **A** — candidate `z_world` collapse (all K candidates identical after one E2 forward step) | representation-geometry | **mitigated** (SD-056 / ARC-065 GAP-A `candidate_summary_source=e2_world_forward` re-sourcing) | necessary upstream *gate*, no longer the live blocker |
| **B** — F-dominance at the committed argmax | selection-structure | **LIVE ROOT** | attack first |
| **C** — de-commit authority magnitude | commitment-dynamics | **open, orthogonal** | own amend (commitment-closure-control-plane); not bundled with B |
| **D** — CRF conflict-gate lockout | gating-calibration | **CLOSED** (`V3-EXQ-654f`: `crf_frac_active` 0.0 -> 0.83-0.97 via the crf-availability-maintenance amend, A held constant) | resolved |
| **E** — within-class diversity (MECH-341) | — | **downstream symptom of B** (gated by A) | not a root |

## The live root, stated plainly: F-dominance

The primary harm/goal score **F accounts for ~88-89% of E3 committed-selection variance** (`V3-EXQ-571`: 0.886 baseline, 0.894 with the full diversity stack — **the diversity stack does not dent F's share**). Consequently every diversity channel — modulatory (B), within-class (E), and the now-unlocked CRF rule-bias (D-post-fix) — **drowns at the same F-dominated committed argmax.** Decisive proof of convergence: `V3-EXQ-654f` shows that with D's gate unlocked the CRF counterfactual delta (0.01-0.025) *reaches* the accumulator, yet committed-class entropy is **bit-identical** ARM_ON vs ARM_OFF per seed. Three nominally-separate channels feed one bottleneck.

**Causal map:**
`A (identical z_world -> class-uniform pool)` and `B (F = 88-89% of E3 variance)` are **parallel** contributors to the `committed_entropy ~ 0` surface symptom (not A->B: 569h shows B fails with A's output supra-floor). Both `A` and `B` gate `E` (within-class branch only fires with >=2 candidates per class, and its lift cannot move an F-dominated argmin). `C` (fixed 5-tick de-commit refractory cannot move a between-arm occupancy statistic against ~530-560 natural-commit steps) is a separate control-plane gap — dissociated from A/B by the 460e "inverse tell" (beta engagement fails on the *high*-rule-bias/saturated seeds and passes on the low-bias seed). `D` was independent of A (654d armed the GAP-A de-collapse and CRF `n_matched` *rose* to 7-8) and is now closed at the CRF locus alone.

## Decisive attack point

**B, via the `569i` top-k k=3 shortlist-then-modulate lever** (`ree-v3/ree_core/predictors/e3_selector.py:1157-1172`): restrict the eligible set to the k F-best, then let the modulatory channel pick within it, bounding F-dominance so diversity can act at the margin. Validated discriminator: `569i` (top-k k=3) PASSES 2/3 seeds strict-above both controls where `569h`/`684` (margin / whole-set shortlist, size 6.25-8.54) failed. Wire it into the next composite re-queue (654g / 625-series) — **not** another A-geometry or D re-queue (both resolved/mitigated).

## The hard-ceiling risk (carry as a gate on the attack)

Because F's variance share is **structural and unmoved by the diversity stack** (571), a shortlist-then-modulate can only act at **near-ties** and may cap achievable committed entropy *below the proposer's own ceiling* regardless of lever. The standalone `569i` margin is **thin** (ARM_1 0.711 vs proposer 0.650, ~0.06 nats, 2/3 seeds). If the thin margin does not survive the full composite (C+D active, foraging-substrate natural monostrategy), the real target is not a better selection lever but **F's 88-89% monopoly itself** — i.e. rebalancing the primary-vs-modulatory variance share. This is registered as **MECH-439**.

## Discriminating experiment (pre-registered)

A 2x2 isolation — **(A de-collapsed ON/OFF) x (B top-k k=3 shortlist ON/OFF)**, holding C and the fixed-D constant, reading committed `selected_action_class_entropy` strict-above BOTH the collapsed-proposer and matched-noise controls on >=2/3 seeds, **run under the composite (C+D active)** since the standalone 569i margin is thin. Predicted pattern confirming the N-root hierarchy: lift ONLY in `(A-ON, B-topk-ON)`; `(A-ON, B-OFF)` stays flat (diverse input + F-dominated argmin); `(A-OFF, B-topk-ON)` stays flat (lever needs a diverse pool). The "one root A" alternative predicts `(A-ON, B-OFF)` already lifts — already falsified by 569h.

## Open questions (from the critic)

1. Does the thin `569i` top-k margin (0.711 vs 0.650, 2/3 seeds) survive the full 625d/654g composite, or does F-dominance reassert under the foraging substrate's natural monostrategy?
2. Is F's 88-89% E3 variance share an intrinsic primary-score property that a shortlist can only locally circumvent (near-ties), capping committed entropy below the proposer ceiling — i.e. is there a hard substrate ceiling even with the best selection lever? (= the MECH-439 question.)
3. Will fixing B re-open D? A top-k shortlist that changes which candidates reach the CRF `gate_and_select` MATCH context could perturb `n_matched` — re-verify `crf_frac_active` under the B fix.
4. Is C (de-commit) truly orthogonal, or does the bistable latch's commit-ENTRY decisiveness share a hidden upstream with B's F-dominated argmin (both need a decisive `result.committed`)? The 460e dissociation is strong but C and A co-occur on the same monostrategy seeds.
5. For C, is the underpowered between-arm occupancy DV masking a real-but-small de-commit effect? A within-arm pre/post-closure delta DV must run before C is adjudicated substrate_ceiling vs measurement artifact.

## Correction note (critic-adjudicated)

The synthesis originally stated `569h` "collapses to entropy 0.0 with diverse input." That is a factual error: `569h` ARM_1 entropy is **0.785** (the highest of its three arms, above proposer 0.611); its real failure is a **non-robust lift** (strict-above-both on 1/3 seeds, need 2/3). The entropy-0.0 figures belong to `625d` and `687` (and `687`'s preconditions failed — `pre_mech260=false`, `pre_nondegen=false` — so it is non-load-bearing). The conclusion (A and B are parallel; B is the live root) survives on the corrected reading: A supra-floor yields only a 1/3-seed lift, so an A-fix alone does not deliver robust committed diversity.

## Evidence anchors

`V3-EXQ-571` (F variance share), `569g/569h/569i` (conversion lineage), `684/684a` (shortlist-mode discriminator), `625d` (A+B composite), `654c/654d/654f` (D lineage, now closed), `460d/460e/460f` (C lineage), `614c/614d/614e/660/660a/660b/616` (E lineage), confirmed autopsies `failure_autopsy_V3-EXQ-{614e,569h,460f,460e,654c,654d,660b}_*`.

---

# Phase 1 — Biology grounding + fork resolution (2026-06-18)

**Method:** biology-grounding workflow (run `wf_baf2ddeb-0a3`) — 5 motifs for "how does the brain stop one dominant value channel from monopolizing action selection?" -> hypothesis synthesis -> adversarial critic. Server throttling limited the completed sweep to 2 of 5 motifs (basal-ganglia selection + divisive normalization — the two fork horns); synthesis + critic ran on those two plus the experimental record. The 3 un-run motifs (directed-exploration/max-entropy commit, output-null preparatory geometry, quality-diversity archive) are an open back-fill, but cannot overturn a verdict anchored in 569h/569i.

## FORK RESOLVED (critic-adjudicated): structural BOUNDING, not F-variance rebalancing.

The synthesis initially favored *rebalancing* F (divisive normalization). The critic overturned it: the synthesis reasoned from the `V3-EXQ-684` MEAN-entropy ranking (where the shortlist arm was the known-collapsing **margin** mode, not top-k) and never engaged the decisive runs. The experimental record settles the fork the other way:
- **569h** (rebalance lever = std-basis additive authority) -> **FAILED**, 1/3 seeds.
- **569i** (structural-bound lever = top-k shortlist) -> **PASSED, resolved GAP-A**, 2/3 seeds.

So the rebalance answer is already-tried and seed-fragile; the structural bound already works. The BG and divisive-normalization motifs converge on one principle — *no single afferent drives the gated output past threshold alone* — but the **V3-tractable realization is structural (keep F out of the final arbitration), not a normalization layer.**

## Decisive next lever: conflict-graded shortlist (BG hyperdirect "hold")

Replace the fixed `modulatory_shortlist_k=3` (e3_selector.py top-k block ~1148-1197) with a **conflict-graded** width: `k = clamp(round(k_max - (k_max-1)*gap_norm), 1, K)`, where `gap_norm` is the normalized top-F-score gap (already in scope via `raw_scores`/`raw_score_range`). Near-ties (small gap) -> wider k / slower commit (the STN threshold-raise); decisive F-gap -> k->1 / fast commit. F gates eligibility only; it is absent from the final modulatory argmin. Pure-arithmetic, no new substrate, **V3-tractable now**.

**Falsifier (sharp):** the committed-entropy lift must **correlate with per-tick F-gap** (bin ticks by top-F-gap, regress committed entropy on gap). If it lifts uniformly regardless of gap, it has reduced to "just a bigger shortlist" and the conflict-grading adds nothing. Non-vacuity precondition: k must actually VARY across ticks (a flat k is the 684 margin-collapse failure mode) AND the eligible set must be genuinely diverse (SD-056 + ARC-065 GAP-A divergent pool — else top_k over a class-uniform pool is vacuous).

## Hypothesis ranking (synthesis, critic-corrected)

1. **conflict_graded_shortlist** — V3-tractable, principled extension of the one lever (569i top-k) that delivered a robust result. PURSUE FIRST.
2. **divisive_normalization** — its V3-tractable form IS the std-basis authority that already FAILED (569h); only the true pooled-denominator form is novel, and that is **secretly V4** (needs per-channel score decomposition not available at the select site). PARK as a V4 candidate.
3. **rank_preserving_F_to_eligibility_demotion** — F removed from the final argmin entirely, used only as a graded eligibility envelope; a stronger structural variant, mid-tractability. Fallback if conflict-graded-k's margin stays thin.
4. **quality_diversity_archive** (MAP-Elites / CDQ-003) — a per-niche committed-action archive; lowest V3-tractability (stateful machinery), strongest as a V4 direction.

## Discriminating experiment (Phase 2/3)

2x2 on the foraging substrate with a trained `e2.world_forward` + ARC-065 GAP-A divergent candidates (the non-vacuity precondition): **Factor A** fixed-k=3 vs conflict-graded k; **Factor B** additive authority OFF vs (deferred) normalization ON. Primary readout: the V3-EXQ-571 per-channel F-variance-share decomposition + committed_action_class_entropy strict-above the matched-noise control on >=2/3 seeds, AND the per-tick F-gap x entropy correlation (the conflict-grading falsifier). Self-route `substrate_not_ready_requeue` if the eligible set is not diverse (vacuous top_k).

**Net:** the campaign's V3 answer is the conflict-graded shortlist; F-variance rebalancing (divisive normalization) is the V4 direction for if/when the structural bound proves it caps committed diversity below the proposer ceiling.

## Phase 1 backfill (3 throttled motifs, single-agent pass 2026-06-18)

The 3 motifs the workflow couldn't complete were back-filled read-only. Verdict: the standing recommendation STANDS, with one refinement — a co-primary V3 lever the synthesis never scored.

- **Directed-exploration / max-entropy commit — NEW co-primary V3 lever.** REE's committed branch (`e3_selector.py:1219`) is a HARD `argmin` over F-dominated `scores`; the *uncommitted* branch already softmaxes but the monostrategy lives in the committed branch. An **entropy-regularized commit** — a value-gap-scaled commit temperature `T_eff = T_base + alpha*f(top-F gap)`, then `multinomial(softmax(-scores/T_eff))` over the eligible set — softens the argmax itself (vs conflict-graded-k which bounds the eligible set). It is genuinely V3-tractable (pure arithmetic on in-scope tensors), distinct from MECH-313 (gap-blind, pre-select) and from the existing uncommitted multinomial. Evidence: Wilson&Cohen 2014 (directed vs random exploration), Daw 2006, Niv 2007 (tonic-DA vigor), Ziebart 2010 / Haarnoja SAC 2018 (max-entropy RL). **Critical unification:** conflict-graded-k and gap-scaled-commit-T are TWO RENDERINGS OF ONE PRINCIPLE — the BG hyperdirect conflict-grade (*grade the decision by the top-F gap*). k-grading bounds the set (HARD safety guarantee: harmful candidates stay ineligible); T-grading softens the argmax (softer; needs a safety check so a near-tie doesn't softmax-promote a clearly-harmful candidate). They COMPLEMENT -> the discriminating experiment becomes a **2-factor design: k=f(gap) x commit-T=f(gap)**, sharing the same falsifier (lift must correlate with per-tick top-F gap; non-vacuity: k or T must actually vary across ticks). A FLAT commit-T reduces to the 569g temperature control that under-lifted -- the gap-scaling is load-bearing.
- **Output-null preparatory geometry — confirms V4.** Faithful rendering needs a learned candidate subspace orthogonal to the F-readout (null/potent decomposition, Kaufman/Churchland/Shenoy 2014; Elsayed 2016); REE has no such learned projection. A pure-arithmetic V3 mimic collapses to the additive-authority lever that already FAILED 569h. V4 roadmap; it does usefully reframe WHY top-k works (a crude discrete null-space keeping F out of within-set arbitration).
- **Quality-Diversity / MAP-Elites (CDQ-003) — within-pool form already exists; cross-tick form is V4.** The within-pool niche-archive reading IS MECH-341 `stratified_select` (already built). The actual MAP-Elites contribution (a persistent cross-tick niche store with eviction/draw policy) is new state, architecturally precedented (IncentiveTokenBank / CandidateRuleField) but heavier than conflict-graded-k for the same near-tie-arbitration goal. V4-leaning.

**Refined recommendation:** conflict-graded-k STAYS the lead lever (the structural bound is the validated direction: 569i PASS / 569h FAIL), now paired with an **entropy-regularized-commit arm as a co-primary factor in the SAME discriminating experiment** (both are gap-grading; k-grading is the safety-hard primary, T-grading the complement). Fallback unchanged: `rank_preserving_F_to_eligibility_demotion`. V4 directions (if the structural bound caps committed diversity below the proposer ceiling, the MECH-439 hard-ceiling branch): divisive normalization (pooled-denominator), output-null subspace, cross-tick QD archive.

