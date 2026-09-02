# Failure autopsy -- V4-EXQ-002 / V4-EXQ-003 falsifiers, and V3-EXQ-259

Generated 2026-09-02T05:04:59Z. Status: **confirmed** (interactive gate, 2026-09-02).

These three share a **surfacing mechanism, not a defect**: all entered `pending_review.md` by the
net widening rather than by any new result. The V4 pair surfaced via the purpose-keyed
"Diagnostic -- autopsy required" section (both were already reviewed with user sign-off on
2026-07-01, via `discussed_experiment_dirs`); 259 surfaced via the GFLAG-0111 flat-manifest
discovery fix (`76921a56ce`, 2026-09-01T19:08Z). Dry-run gate: all three clean.

The two V4 runs additionally share a real defect class with each other. 259 does not.

## V4-EXQ-003 (DR-10) -- the gate is tautological

The load-bearing precondition is `high_sv = cell_gap + DECISIVENESS_MARGIN` (driver:128, margin
1.0), then tested as `high_sv > gap` (driver:179) -- i.e. `gap + 1.0 > gap`. The manifest's
`"measured": 1.0, "threshold": 1.0` is a **boolean rendered as a float** (driver:252), not a
measurement. C2 is annotated in the source itself -- `"C2_uniform_inert": True,  # uniform
self-viability range == 0 by construction` (driver:259) -- and flagged `load_bearing: false`.
C1 is arithmetically forced once the lever is connected: a penalty of `gap + 1.0` pushes the
argmin 1.0 past second-best.

**The only reachable FAIL state in the whole DR-10 design is "the lever is not connected."** The
cost is caller-supplied; no `z_self` is read anywhere in the driver, and the ecological source is
a documented follow-on.

## V4-EXQ-002 (DR-13) -- the one reachable criterion is compared to the wrong thing

`C1_carries_history` is genuinely reachable-false -- the single non-degenerate criterion across
both V4 runs -- but it is compared against a **fixed floor of 0.001**, not against the OFF arm.
The A0_OFF arm (EMA, no recurrence) scores **0.330 / 0.154 / 0.174**, clearing that floor
comfortably and **beating the recurrence arm on 2 of 3 seeds**. The ON-vs-OFF contrast exists only
in `summary.secondary_recur_vs_ema_hist_disc`, explicitly labelled "NOT a gate".

The DR-13 design doc's falsifier is about going "beyond the EMA snapshot" and whether recurrence
"buys nothing over the EMA". The implementation never gates on that contrast, so the run cannot
distinguish "recurrence delivers a stateful subject" from "an EMA does the same job".

Across both runs, **all six `criteria_non_degenerate` flags are constants** -- hardcoded `True`, or
`bool(SEQ_LEN >= 2)` / `bool(K >= 2)` over module constants. None is data-derived.

**Scope:** both carry `architecture_epoch: ree_self_model_v1`, `generation: v4`, `claim_ids: []`,
`unblocks_claims: [ARC-081, MECH-215]`. Neither meets the V3 tagging conditions, by design --
V4 sits outside the V3 denominator (`docs/architecture/version_layering_doctrine.md`). So there is
no claim-layer disposition here; the finding is recorded so the two self-routes are not later read
as confirmations.

## V3-EXQ-259 -- bookkeeping, not a fresh diagnosis

Correcting a premise this session first worked from: **the manifest exists and always has**, at
`evidence/experiments/v3_exq_259_wanting_gradient_navigation/`, committed once in `e9f85337a2`
(2026-04-08) and never modified. The dry-run checker's "not a file, run_id, or queue_id" is a
run_id-index lookup miss; the path form resolves. `runner_status.json` corroborates a completed
288.7s run on DLAPTOP-4.local (16:48:13 -> 16:53:02). It is a **real completed FAIL**, not a crash
record, and does not route to `/diagnose-errors`. Epoch `1775666895` = 2026-04-08T16:48:15Z (a
start stamp; the manifest's `timestamp` 16:53:01 is the write stamp).

It should be marked **superseded** rather than adjudicated on its merits, for three converging
reasons:

1. Every metric is exactly 0.0 in both arms -- it discriminates nothing.
2. It tags **MECH-112, which is `deprecated: True`**, split into MECH-229 / MECH-230 on
   2026-04-13, five days after the run. Its evidence weighs against a claim that no longer exists
   in that form.
3. Functional successors already exist -- `v3_exq_326_wanting_gradient_nav_fix` (FAIL, itself
   marked superseded) and `v3_exq_326a` (PASS, `supports`, tagging the post-split MECH-229) -- but
   **nothing carries a `supersedes` pointer back to 259**. The gap is the missing pointer.

## Failure-location (GOV-FAILLOC-1)

**MEASURES** for both V4 runs (a falsifier whose gate cannot fail). **MIXED / uncertain** for 259 --
a degenerate run superseded in fact but not in metadata. None is chargeable to REE.

## Pre-routing checks -- two recorded dismissals

C1 and C2 fire on this artifact against the 259 target, naming
`v3_exq_226_arc030_combined_selector_redesign`, `v3_exq_235_mech112_arc030_clean_goal_gate`,
`v3_exq_238_sd012_drive_weight_ablation_fix`, and the substrate entries
`scaffolded-curriculum-hazard-rebalance` and `sd_blocked_agency_mismatch_floor_calibration`. Both
are **dismissed with reason, not silenced**: 259's routing is `governance-note-only`, and the
checks aggregate routing across targets -- the two `queue-experiment` routings belong to the V4
targets, which carry `claim_ids: []`. Substantively, `v3_exq_235` targets the deprecated MECH-112
and should not be revived on this autopsy's account; whether 226 and 238 should run is a live
question for the governance walk, but it is neither created nor answered here.

## Routing (confirmed at gate)

V4 pair: `queue-experiment` -- recorded, no claim impact; a successor DR-10 probe needs a
precondition that can fail, and a DR-13 probe must gate on the ON-vs-OFF contrast its own design
doc specifies. 259: `governance-note-only` -- set `evidence_direction: superseded` on its four
claim entries and add the missing `supersedes` pointer.
