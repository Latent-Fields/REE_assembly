# Failure Autopsy — V3-EXQ-907 (SD-016 GOV-FANOUT-1 portfolio, H1 drive axis)

**Generated:** 2026-08-10T06:27:24Z
**Scope:** single (diagnostic, claim-free — part of the SD-016 GOV-FANOUT-1 discrimination portfolio)
**Status:** confirmed (interactive gate run 2026-08-10)

*See also `failure_autopsy_V3-EXQ-908_2026-08-10.md` — the H3 (algorithm axis) sibling leg of the same portfolio, adjudicated together at the same interactive gate.*

## 1. Facts

`v3_exq_907_sd016_h1_ctxdiv_20260809T130845Z_v3`, `claim_ids: []`, `experiment_purpose: diagnostic`, `outcome: PASS`. Run: 71.4s, `ree-cloud-2`, 3 seeds `[42,43,44]`. `validate_recording.py`: 0 always-core gaps, not a dry run.

Per the SD-016 fan-out portfolio (`sd016_selection_fanout_portfolio_scope_staged_20260809.md`), H1's hypothesis: the cue-slot tagger *can* represent context-selective slot distributions but the loss landscape never rewards them (`terrain_loss` is satisfied equally well by the uniform-softmax attractor, `sel_entropy_mean → ln(16)=2.7726`). Fix tested: an auxiliary objective directly rewarding `sel_context_divergence` during P1, swept over λ∈{0.1, 0.5, 2.0}.

**Acceptance:** `overall_pass = C2_pass AND (any A2 lambda arm clears C1 AND C1b on majority ready seeds)`, `attribution_clean` additionally requires the matched-budget baseline (A1) NOT to break the saddle.

| Arm | entropy_mean | ctxdiv_mean | breaks saddle |
|---|---|---|---|
| A0_OFF (control) | 2.7726 | 0.0001 | n/a — stays near uniform |
| A1_tagger (matched-budget baseline, no ctxdiv loss) | 2.7506 | 0.0221 | **No** |
| A2_ctxdiv_λ0.1 | 2.4570 | 0.5655 | **Yes** |
| A2_ctxdiv_λ0.5 | 2.4573 | 0.5655 | **Yes** |
| A2_ctxdiv_λ2.0 | 2.4575 | 0.5655 | **Yes** |

C2 (off-arm-on-saddle control) passes 3/3. All three λ sub-cells break the saddle consistently (robust to hyperparameter choice, not fragile/threshold-dependent). `attribution_clean: true` — the matched-budget baseline does NOT itself break the saddle, ruling out "it was just extra capacity" as a confound.

## 2. Claim-layer mapping

`claim_ids: []` — this is a claim-free diagnostic feeding the SD-016 (`docs/architecture` ContextMemory cue-indexed retrieval) substrate work, per the GOV-FANOUT-1 portfolio commissioned by `failure_autopsy_V3-EXQ-898_2026-08-08`. No claims.yaml entry to update.

## 3. Biological-reference triage

Not applicable in the usual sense — this is a mechanistic/algorithmic diagnostic, not a claim-layer biological triage. The portfolio's own design document grounds the H3 sibling leg (hard selection) in dentate-gyrus lateral inhibition / CA3 competitive retrieval; H1 (this leg) is a training-signal/objective question rather than an architectural-biology one.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free diagnostic) | |
| Biological reference | n/a | this leg tests a training-objective hypothesis, not an architectural-biology one |
| Prerequisites | present | encoder already proven to vary (SD-070 fix) |
| Implementation | complete | ctxdiv auxiliary loss cleanly implemented and effective |
| Environment | adequate | |
| Measurement | adequate | robust across 3 λ values; clean attribution control |
| Integration | coupled, non-degenerate | |
| Scale/capacity | adequate | |

**Failure-location:** not applicable — this is a PASS with no ambiguity in the acceptance logic (`criteria_non_degenerate` both `true`, hardcoded by the author with a stated, reasonable justification).

## 5. Learning extracted

- H1 (drive/objective axis) is confirmed: a context-divergence auxiliary loss is sufficient to break the uniform-softmax saddle, robustly across three λ values, with a clean matched-budget attribution control.
- This is a narrow, mechanistic confirmation — it does not by itself confirm the full architectural SD-016 claim, only that the training-signal gap identified by V3-EXQ-898 was real and addressable this way.

## 6. Routing (confirmed at interactive gate)

**User-confirmed disposition:** `H1-drive-context-divergence` resolves to `confirmed` in the frozen hypothesis-space ledger (`sd016_retrieval_selectivity_mechanism` qid). `narrow_supports_flag: true` (this confirms a narrow, mechanistic leg — not the full SD-016 architectural claim). No `claims.yaml` update (claim-free). Routing: feeds `SD-016`'s substrate_queue.json entry toward `/implement-substrate`, combined with the H3 (Gumbel-softmax) confirmation — see `failure_autopsy_V3-EXQ-908_2026-08-10.md` for the combined routing decision, applied once via that file's `recommended_substrate_queue_entry` (action: amend) to avoid a duplicate substrate_queue write.

Step 9b: this run RESOLVES an already-pre-registered hypothesis (Mode B) — `sd016_retrieval_selectivity_mechanism` qid, `H1-drive-context-divergence`. See the combined Step 9b registry update applied alongside V3-EXQ-908 (both legs of one portfolio, one ledger edit).
