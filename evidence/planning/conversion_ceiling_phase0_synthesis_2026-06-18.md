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
