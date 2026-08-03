# Failure Autopsy: V3-EXQ-869a (MECH-267, mode-conditioned hippocampal proposal content persistence — retest with both mechanisms active)

**Generated:** 2026-08-03T08:33:56Z
**Run:** `v3_exq_869a_mech267_mode_conditioning_content_persistence_retest_20260802T195943Z_v3`
**Queue ID:** V3-EXQ-869a
**Claim IDs:** MECH-267
**Status:** confirmed
**Supersedes:** `v3_exq_869_mech267_mode_conditioning_content_persistence_20260802T035422Z_v3` (V3-EXQ-869)
**Dry-run check:** both `v3_exq_869a...` and `v3_exq_869...` confirmed non-dry via `check_dry_run_citations.py` (0 dry cited, 2 clean).

## 1. Facts

**Why this is a lettered retest, not a redesign.** Same DV (`action_object_decoder_raw_output_stats.std_by_action_dim`, `mean_raw_std_by_dim`), same pairwise-gap floors (`FLOOR_DIAGNOSTIC=0.015`, `FLOOR_PRODUCTION=0.01`), same modes, same seeds (30), same `HippocampalModule` construction as V3-EXQ-869. The **only** substantive change: `HippocampalConfig.mode_horizon_scale` now has live, non-empty defaults (`external_task=0.5, internal_planning=1.0, internal_replay=0.7, offline_consolidation=1.0`), because the second of MECH-267's two named mechanisms (horizon-depth modulation of the CEM elite-selection scoring window — `SD-MECH267-HORIZON-DEPTH`, ree-v3 `e0117eea8b`) was built between 869 and 869a, per 869's own confirmed-autopsy routing.

**Mechanism-activation check (new in 869a).** Every cell records `mode_noise_scale_used` and `mode_horizon_scale_used`/`effective_horizon_used`. Confirmed at runtime: `mechanism_activation.both_mechanisms_active: true`, `distinct_effective_horizons: [2, 3, 4]`, `effective_horizon_by_mode: {external_task: 2, internal_replay: 3, internal_planning: 4, offline_consolidation: 4}` — non-degenerate (not all four equal). Both mechanisms genuinely fire in every cell of this run; this is not a silent no-op.

**Criteria:**
- **C0 (manipulation check, iters=1):** mean gaps internal_planning−external_task 0.0546, external_task−internal_replay 0.0918, internal_replay−offline_consolidation 0.0311 — all clear the 0.015 floor. **PASSED**, non-degenerate.
- **C1 (production content persistence, iters=3, load-bearing):** mean gaps +0.00078, +0.00242, −0.00375 — essentially flat, all below the 0.01 floor. **FAILED.**
- **C2 (non-gating, per-seed corroboration):** 0 of 30 seeds show the full predicted mode ordering.

**Outcome:** FAIL. `non_degenerate: True`. Label: `mode_conditioning_content_effect_still_washed_out_with_both_mechanisms`. Manifest `evidence_direction: weakens` (not yet reclassified — this autopsy recommends `non_contributory`, see Step 7 below).

**The load-bearing comparison is 869a's C1 numbers against 869's own C1 numbers**, not against the floor alone: 869 (noise-scale only) read −0.0003, +0.0035, −0.0037; 869a (both mechanisms) reads +0.0008, +0.0024, −0.0037. **Nearly identical**, despite a second, genuinely-firing upstream mechanism being added. Building the recommended fix did not move the production-settings result.

## 2. Claim-layer mapping

MECH-267 (`docs/claims/claims.yaml:28830`): status `provisional`, `implementation_phase: v3`, `v3_pending: false`, `pending_retest_after_substrate: true` (set 2026-08-02 pending exactly this retest). `depends_on`: SD-004 (HippocampalModule), SD-032a (SalienceCoordinator — operating_mode source), MECH-261 (write-gate registry, read-side analogue), MECH-092 (micro-quiescence replay) — all IMPLEMENTED. The claim's own `implementation_note` documents both the 2026-04-20 noise-scale build and the 2026-08-02 horizon-depth build in full, including the explicit statement that the horizon-depth mechanism "Modulates the CEM elite-selection SCORING WINDOW... NOT the physical rollout length" — i.e. it changes how much of an already-generated rollout counts toward a candidate's score, not what states are reachable or what value function scores them.

**Did the test let the claim express itself this time?** Materially further than 869 (both named mechanisms now active, confirmed at runtime), but the *locus* of both mechanisms is still upstream of CEM's elite-selection value function — one perturbs the initial sampling variance, the other perturbs how much of the rollout is read into the score. Neither mechanism changes the value function that actually selects elites across refit iterations. This is the load-bearing continuity between 869 and 869a: the claim was given a materially fairer test (an actual implementation gap was closed), and it still didn't express — which sharpens rather than resolves the diagnosis.

## 3. Biological reference

Unchanged from 869 and still strong: Pfeiffer & Foster 2013 (goal-directed forward replay), Tambini 2019 (task-relevant reactivation bias), Olafsdottir 2018 (state-dependent replay content), Mattar & Daw 2018 (prioritized memory access, gain/need mode-dependent), Wikenheiser & Redish 2015 (theta-cycle look-ahead distance scales with goal distance — the literature basis for the horizon-depth mechanism specifically, now built and confirmed firing). The biology supports mode-conditioned content robustly at multiple independent levels (breadth AND depth); this FAIL is not a biology mismatch at either mechanism.

Is there a plausible mammalian analogue for "two independently-motivated upstream signals both wash out under downstream iterative refinement"? Plausibly yes: in the CEM elite-refit analogy, the "downstream refinement" step is not itself claimed to be a modeled biological process (it's an REE V3 architectural device standing in for a proposal-and-selection scheme) — its mode-independence is an REE implementation property, not a hypothesized brain property. So this reads as a translation-layer property of the CURRENT proposal-generation pipeline, not a discovered biological prerequisite.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (sharper than 869, still not a fair full test) | both named mechanisms now confirmed active; neither touches the elite-selection value function itself |
| Biological reference | strong, multi-source, both mechanisms independently lit-grounded | Wikenheiser & Redish 2015 specifically supports the mechanism just built and shown insufficient alone |
| Prerequisites | present | SD-004, SD-032a, MECH-261, MECH-092 all IMPLEMENTED |
| Implementation | complete for both named mechanisms; **the actual bottleneck (elite-selection scoring criterion) was never named by the claim and remains unbuilt** | the claim's own two-mechanism text is now fully instantiated, and that instantiation is demonstrably insufficient |
| Environment | adequate, well-powered | 30 seeds, unchanged design, clean C0/C1 separation preserved |
| Measurement | excellent | mechanism-activation check is new and directly confirms both mechanisms fire non-trivially before trusting the verdict |
| Integration | CEM elite-refit's iterative convergence is the suspected culprit | with enough refit iterations, elite selection under a mode-independent VALUE FUNCTION converges toward the same optimum regardless of the initial distribution's variance (869) or scoring window (869a) |
| Scale | untested axis: iteration count | only iters=1 and iters=3 have ever been run; iters=2 (or any intermediate) has never been measured — a real gap, not an oversight this autopsy is inventing |

## 5. Learning extracted

1. **Two consecutive same-signature wash-outs after closing a confirmed implementation gap is stronger evidence than either FAIL alone** — it shifts the most likely locus from "missing upstream mechanism" toward "the downstream elite-selection criterion is what needs to change," without yet proving it (see Section 7 — this reading was NOT adopted this cycle; see user note).
2. **`num_cem_iterations` has only ever been tested at its two extremes (1 and 3)** for this question — no run has asked whether the wash-out is iteration-count-dependent at all (e.g. does it survive at 2?). This is a cheap, previously-unasked question.
3. **Both built mechanisms perturb the CEM elite-refit's *inputs* (initial variance, scoring window) — neither perturbs its *decision rule* (the value function used to rank and retain elites).** If mode-independence lives in the decision rule, no amount of upstream input-shaping will survive enough refit iterations. This is a generalizable design principle for any future mode-conditioning mechanism layered on top of an iterative-refit optimizer, extending 869's own Learning #2.
4. **Re-derive brake check:** MECH-267 carries 0 prior `substrate_ceiling` autopsies (869's reading was `competence_implementation_gap`, which does not count under the R1–R3 convention). This target's own recommended category (Section 7) is `competence_implementation_gap`, per user direction below — so the ceiling-hit count for MECH-267 remains **0** after this autopsy, and the brake does not fire. Flagging explicitly for whoever reads this next: **a third same-question letter that tries yet another single upstream mechanism, without addressing the elite-selection criterion itself, would be the pattern the brake exists to catch** — hence this autopsy's routing (Section 7) is a discrimination portfolio, not a fourth sequential letter.
5. **Granularity-debt recurrence trigger:** checked via `granularity_debt_cluster.py MECH-267` — 1 prior tagging target (869), `claim_alignment` bucketed `other` (free text, not `weakened`). This target's own `claim_alignment` is also `unclear`/other, not `weakened`. Per the trigger rule (fire only when at least one target reads `weakened`), **does not fire** — this reads as one recurring structural property (the refit convergence), not evidence the claim itself is too coarse and needs splitting.

## 6. Interactive gate (user-confirmed 2026-08-03)

Two questions were put to the user:

1. **Routing choice** among (a) a GOV-FANOUT-1 discrimination portfolio across 3 distinct design axes, (b) a single best-guess sequential re-letter (869b), (c) stop and route to a governance demotion-review discussion. **User chose (a), the fan-out portfolio.**
2. **Category/direction choice** among (a) upgrade to `substrate_ceiling`/`non_contributory` (this autopsy's own suggested reading, on the grounds that two consecutive identical wash-outs after closing a confirmed implementation gap is evidence the ceiling is structural), (b) keep `competence_implementation_gap`/`non_contributory` (stay conservative — a third, still-unbuilt mechanism may yet be the missing piece; let the fan-out portfolio's own results decide whether to upgrade), (c) `weakens` (read this as evidence against the claim). **User chose (b) — keep `competence_implementation_gap`.**

The routing (portfolio, not a fourth sequential letter) and the category (still `competence_implementation_gap`, not yet `substrate_ceiling`) are therefore **not in tension**: the user's read is that we don't yet have enough evidence to call this a structural ceiling — but we also have enough evidence (two independent, confirmed-active mechanisms both washing out identically) to know that repeating the same "build one more upstream mechanism" move for a third time would not be the efficient next step. The fan-out portfolio is what will supply the evidence needed to decide the category question properly.

## 7. Learning extracted and repair pathway (finalized per user direction)

**Recommended `epistemic_category`:** `competence_implementation_gap` (retained from 869, per user direction — not upgraded to `substrate_ceiling` this cycle).
**Recommended `evidence_direction`:** `non_contributory` (still informative about implementation completeness/locus, not evidence against MECH-267 as a claim — biology remains solid at both mechanisms tested so far).
**`pending_retest_after_substrate`:** not applicable this cycle in the strict substrate_queue sense — the next step is a **diagnostic portfolio** (`/queue-experiment`), not a substrate build; whichever leg of the portfolio succeeds is what should drive a `recommended_substrate_queue_entry` in a follow-up autopsy.

**Routing: `/queue-experiment` — GOV-FANOUT-1 discrimination portfolio, NOT a fourth sequential same-question letter.** Three live hypotheses on three distinct design axes (see `fanout_recommendation` in the JSON artifact for the full structured form):

- **H1 (`selection`/process axis) — iteration-count dependence.** Does the wash-out depend on refit iteration count itself? Only `iters=1` and `iters=3` have ever been measured; `iters=2` (or any intermediate) is untested. Cheapest probe: same DV/design, add an `iters=2` condition. Null: gaps at iters=2 are as flat as iters=3 (wash-out is not iteration-count-dependent, at least not smoothly).
- **H2 (`representation` axis) — mode-aware elite-selection scoring.** Does making the CEM elite-selection VALUE FUNCTION itself carry an explicit mode-dependent term (as opposed to windowing an already mode-independent score, which is what the horizon-depth mechanism does) preserve differentiation through refit? Null: even an explicitly mode-dependent scoring term washes out by iters=3 (would point toward H3 or a genuinely different architecture).
- **H3 (`algorithm` axis) — hard-partitioned per-mode candidate pools.** Does eliminating cross-mode elite mixing entirely (separate candidate pools refit independently per mode, no shared elite set) preserve differentiation? This is the most structurally different of the three — it changes the CEM algorithm's own architecture rather than any input to it. Null: even fully-partitioned refit converges toward mode-independent content (would be the strongest evidence yet for a true representational ceiling elsewhere in the pipeline, e.g. the decoder itself).

Each leg declares its own null per the fan-out convention; a design-audit for coverage/verdict-aliasing across the three should happen before queuing (per GOV-FANOUT-1 producer/consumer split — this autopsy is the producer, `/queue-experiment` Step 2.5b is the consumer).

**Draft `evidence_quality_note` for governance to write (if this routing is accepted):**
> "V3-EXQ-869a (2026-08-03, confirmed autopsy `failure_autopsy_V3-EXQ-869a_2026-08-03`): retest of V3-EXQ-869 with BOTH named mechanisms (noise-scale + horizon-depth, the latter built 2026-08-02 per 869's own routing) confirmed active at runtime. Production-settings (iters=3) content persistence still washes out, nearly identical numbers to 869's noise-scale-only result. epistemic_category retained as competence_implementation_gap (user-confirmed, not yet substrate_ceiling); evidence_direction non_contributory. Routed to a GOV-FANOUT-1 discrimination portfolio (3 legs: iteration-count, mode-aware scoring, partitioned pools) rather than a third sequential same-question letter — see fanout_recommendation in the linked JSON artifact."
