# Failure Autopsy — V3-EXQ-908 (SD-016 GOV-FANOUT-1 portfolio, H3 algorithm axis)

**Generated:** 2026-08-10T06:27:24Z
**Scope:** single (diagnostic, claim-free — part of the SD-016 GOV-FANOUT-1 discrimination portfolio)
**Status:** confirmed (interactive gate run 2026-08-10)

*See also `failure_autopsy_V3-EXQ-907_2026-08-10.md` — the H1 (drive axis) sibling leg of the same portfolio, adjudicated together at the same interactive gate. This file carries the combined SD-016 routing decision and Step 9b registry application for both legs.*

## 1. Facts

`v3_exq_908_sd016_h3_hard_selection_20260809T131209Z_v3`, `claim_ids: []`, `experiment_purpose: diagnostic`, `outcome: PASS`. Run: 67.7s, `ree-cloud-2`, 3 seeds `[42,43,44]`. `validate_recording.py`: 0 always-core gaps, not a dry run.

**Flagged `vacuous_pass` by the indexer** (`pending_review.md`: "Diagnostic adjudication required (self-route unverified)"). This is investigated and resolved below as a **false positive**.

H3's hypothesis (per the fan-out portfolio doc): a soft, end-to-end differentiable softmax gate cannot *hold* a sparse, context-selective optimum — gradient descent relaxes it back toward the uniform attractor even when correctly rewarded. Fix tested: structurally competitive selectors — annealed Gumbel-softmax and straight-through top-k (k=1, k=2) — that force sparsification independent of downstream loss demands, matching the biological reference (dentate-gyrus lateral inhibition / CA3 competitive retrieval).

**Acceptance:** `overall_pass = C2_off_arm_on_saddle.pass AND any(per_arm verdict == 'pass')`, where per-arm verdict requires C1 (entropy<2.5) AND C1b (ctxdiv>0.1), both independently measured with their own seeds_pass count.

| Arm | entropy_mean | ctxdiv_mean | C1 | C1b | Verdict |
|---|---|---|---|---|---|
| A0_OFF (control) | 2.7726 | 0.0001 | n/a | n/a | control |
| A1_tagger_soft (baseline) | 2.7506 | 0.0221 | fail (0/3) | fail (0/3) | fail |
| **A2_tagger_gumbel** | 1.22e-08 | **0.6875** | pass (3/3) | **pass (3/3)** | **pass** |
| A3a_topk_k1 | 1.84e-08 | 0.0000 | pass (3/3) | fail (0/3) | constant_peaky_degenerate |
| A3b_topk_k2 | 0.6801 | 0.0196 | pass (3/3) | fail (0/3) | constant_peaky_degenerate |

`overall_pass = true` (C2 clears 3/3; A2_tagger_gumbel clears both C1 AND C1b).

### Why `vacuous_pass` is a false positive (4th sub-case of a known indexer defect class)

The indexer's `_compute_adjudication` (`build_experiment_indexes.py`) has fixed three prior name/join-mismatch sub-cases (V3-EXQ-783 name-spelling, V3-EXQ-830 direction-reversal, and the aggregate-criterion exclusion landed earlier today for V3-EXQ-906/665/664). This manifest is a **fourth, distinct** sub-case: its `interpretation` block has `label`, `preconditions`, `criteria_non_degenerate` — **no `criteria[]` array at all**. With nothing to match against, the indexer falls to its legacy fallback: any `criteria_non_degenerate` key that is `False` and doesn't end in `_branch` flags `vacuous_pass`. Three such keys exist here: `A2_tagger_gumbel::C1_breaks_saddle`, `A3a_topk_k1::C1_breaks_saddle`, `A3b_topk_k2::C1_breaks_saddle` — all `False`.

But the driver's own docstring (`v3_exq_908_sd016_h3_hard_selection.py`, "DV-SYMMETRY CHECK" section) explains exactly why: for hard-selection arms, near-zero entropy is expected *by construction* of the operator itself (topk k=1 forces exactly 0; k=2 caps at ln(2)=0.693; annealed Gumbel anneals toward 0) — regardless of whether the tagger learned anything context-discriminative. The author deliberately marked C1 non-degenerate=`False` for these three arms because C1 alone is a necessary sanity check, not evidence of discrimination — **the real, load-bearing gate is C1b**, which is genuinely and independently measured, and which correctly discriminates: passes 3/3 for Gumbel, fails 0/3 for both top-k variants. `overall_pass` rests on Gumbel's measured C1b (0.6875, well above the 0.1 threshold), not on any hardcoded or degenerate value.

The indexer has no way to see this stated rationale because no `criteria[]` array exists to carry a `load_bearing: false` tag on the C1 sub-checks. This is a tooling gap, not a finding about the run.

## 2. Claim-layer mapping

`claim_ids: []` — claim-free diagnostic, same portfolio as V3-EXQ-907. No claims.yaml entry.

## 3. Biological-reference triage

The portfolio's own design grounds H3 in dentate-gyrus lateral inhibition / CA3 pattern-separation-via-competitive-retrieval — a genuinely different biological analog from H1's training-objective question. The differentiated result (Gumbel succeeds, top-k fails) sharpens this: annealed soft-to-hard competition (Gumbel) achieves genuine context-conditioned sparsification; immediately-hard, non-differentiable-until-forward top-k collapses to a context-*independent* peaky pattern ("constant_peaky_degenerate" — the exact failure mode C1b exists to catch). This favors the "gradual competitive sharpening" reading of the biological analog over "hard winner-take-all from the start."

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free diagnostic) | |
| Biological reference | clear, differentiates within the axis | Gumbel (gradual competition) succeeds; top-k (immediate hard selection) fails |
| Prerequisites | present | |
| Implementation | complete | all three selector variants correctly implemented |
| Environment | adequate | |
| Measurement | adequate, but flagged by a tooling gap | the `vacuous_pass` flag is a false positive of the indexer, not the run |
| Integration | coupled, non-degenerate on the load-bearing gate (C1b) | |
| Scale/capacity | adequate | |

## 5. Learning extracted

- H3 (algorithm axis) is confirmed for Gumbel-softmax specifically, not for hard selection in general: annealed soft-to-hard competition breaks the saddle genuinely (C1b clears 3/3); immediately-hard straight-through top-k collapses to a context-independent "constant_peaky" pattern (C1 trivially clears, C1b genuinely fails).
- This differentiates within H3 — a `split` resolution, not a blanket confirm.
- The `vacuous_pass` indexer flag is a genuine false positive: a 4th sub-case of the `criteria_non_degenerate`↔`criteria[]` join-mismatch class, distinct from the three sub-cases already fixed (this manifest has no `criteria[]` array at all).

## 6. Routing (confirmed at interactive gate)

**User-confirmed disposition:** `H3-algorithm-competitive-gating` resolves to **`split`** in the frozen hypothesis-space ledger — Gumbel-softmax `confirmed`, straight-through top-k `eliminated`. The `vacuous_pass` flag is confirmed a false positive; recommend a follow-up chip for the indexer (4th join-mismatch sub-case: manifests with no `criteria[]` array at all should not fall to the blanket legacy fallback without checking for an author-declared non-degeneracy rationale, or the fallback should require the flagging key's aggregate/gating counterpart to also have failed). `severity: cosmetic` (does not corrupt evidence; mis-flags a legitimate result for manual review, exactly what this autopsy did).

**Combined SD-016 substrate routing (H1 + H3 together):** `recommended_substrate_queue_entry.action: amend`, `target_sd_id: SD-016`. Both a viable training objective (H1: ctxdiv auxiliary loss) and a viable algorithm (H3: annealed Gumbel-softmax, not top-k) are now confirmed. Recommend `/implement-substrate` combine both into SD-016's actual selection-mechanism build — updating status from `parked_pending_selection_mechanism_fix` toward implementation-ready — superseding the stale `validation_experiment: V3-EXQ-418h` reference. H2 (representation axis) remains gated on lit-pull + unbuilt deps per the portfolio's own design and is not blocking.

**Draft note for SD-016's substrate_queue.json entry (governance to apply):**
> [2026-08-10 governance, V3-EXQ-907+908, confirmed failure_autopsy_V3-EXQ-907_2026-08-10 + failure_autopsy_V3-EXQ-908_2026-08-10]: GOV-FANOUT-1 portfolio legs H1 (drive) and H3 (algorithm) both resolved. H1 CONFIRMED: ctxdiv auxiliary loss (any lambda in {0.1,0.5,2.0}) breaks the uniform-softmax saddle, clean attribution control. H3 SPLIT: annealed Gumbel-softmax CONFIRMED (C1b passes 3/3, genuine context-conditioned sparsification); straight-through top-k ELIMINATED (constant_peaky_degenerate -- context-independent collapse). V3-EXQ-908's indexer vacuous_pass flag confirmed a false positive (4th join-mismatch sub-case, tooling gap not a finding). Recommend combining H1's objective with H3's Gumbel-softmax operator into SD-016's actual implementation; H2 (representation axis) remains gated on lit-pull, not blocking.

Step 9b: both legs resolved via Mode B in the same registry edit (see `step_9b_resolution` below and in `failure_autopsy_V3-EXQ-907_2026-08-10.json`).
