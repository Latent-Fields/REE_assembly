# Failure autopsy -- V3-EXQ-964b (MECH-482 / SD-102 epistemic-deficit accumulator: corrected reachability instrument + verify-lift ladder)

- **Status:** `confirmed` -- Step 8 gate answered by the user 2026-09-16 (all three staged decisions approved; recorded 2026-09-16T11:10:54Z by the account-handover session, see "Step 8 gate outcome" below). Originally staged `awaiting_human_confirmation` by a non-interactive session.
- **Generated:** 2026-09-16T04:42:21Z
- **Run:** `v3_exq_964b_mech482_reachability_verify_lift_20260915T215220Z_v3` (ree-cloud-2, 704 s, seeds 71/101/202, 3 ep x 60 steps, env SEEDED)
- **Supersedes:** `V3-EXQ-964a` (`failure_autopsy_V3-EXQ-964a_20260914`, confirmed 2026-09-15T01:14:02Z), itself superseding `V3-EXQ-964` (`failure_autopsy_V3-EXQ-964_2026-08-30`, confirmed). Both prior artifacts were read end to end (Step 1 re-adjudication rule), as was the driver docstring including its red-team record.
- **Purpose:** `diagnostic`, `claim_ids: ["MECH-482"]`. Indexer adjudication flag: **`vacuous_pass`** (adjudicated in Section 2 -- NOT sustained).
- **Dry-run gate:** clean (`check_dry_run_citations.py`: 3 clean, 0 dry, run over 964b/1039/1041 during target selection; `dry_run: false`, run_id not of dry shape).
- **Recording:** `validate_recording.py` OK, 0 always-core gaps; `substrate_hash 36cd8e8f...`, `substrate_commit bd83702b` (clean, `main`).

## 1. Facts

| Criterion | Load-bearing | Measured | Threshold | Result |
|---|---|---|---|---|
| C1 detector sensitivity -- top rung (s=10) fires | yes (gate on everything else) | 3 seeds | >= 2 | **PASS** |
| C2 minimum effective authority (smallest `curiosity_bias_scale` rung firing on a seed majority) | yes | **0.1 == SHIPPED** | <= 10 | **PASS** (left-censored, see Sec. 2) |
| C3 subject (ARM_READINESS) moves the selected candidate | yes | 0 seeds | >= 2 | **FAIL** |

All 9 preconditions met (DV headroom analytic; paired control 0.0 on BOTH DVs; injected ramp range 1000; top-rung headroom 4.447 over the subject's worst |margin| 4.497; fresh-tick denominator skew 0; E3-fresh ticks worst 33; multitarget regime worst 10; readout range worst 2.12e-3; vacuous-readout rate 0).

**Ladder, selection divergence over E3-fresh ticks (seed 71 / 101 / 202; n fresh = 33 / 101 / 38):**

| Arm | post-clamp range | s71 | s101 | s202 | seeds firing |
|---|---|---|---|---|---|
| ARM_READINESS (subject: real readout, weight 0.05, scale 0.1) | 5.5e-3 / 2.1e-3 / 4.2e-3 | 0/33 | 0/101 | 0/38 | **0** |
| VERIFY_LIFT_S0.1 (synthetic ramp, **shipped** authority) | 0.200 (clamp saturated 1.0) | 1/33 = 0.030 | 12/101 = 0.119 | 8/38 = 0.211 | **3** |
| VERIFY_LIFT_S0.5 | 1.0 | 0.121 | 0.505 | 0.395 | 3 |
| VERIFY_LIFT_S2 | 4.0 | 0.394 | 0.574 | 0.474 | 3 |
| VERIFY_LIFT_S10 | 20.0 | 0.576 | 0.693 | 0.553 | 3 |

Action-projection divergence (964a's DV) for the subject: 0/180 on every seed (0/540). For the shipped-authority rung: 0 / 17 / 11 of 180. The DV response is monotone in authority on every seed with no plateau below the top rung (the clamp itself is, by design, fully saturated at the two bottom rungs: `max_clamp_saturated_frac` 1.0 / 1.0 / 0.94 / 0.63).

**Subject arm, corrected instrument:** `clamp_saturated_frac` **0.0** on all seeds; `corrected_max_pert_over_margin` 0.022 / 0.320 / 2.963; `corrected_min_positive_margin` 0.0291 / 0.0066 / 0.0003; strict-reachable ticks 0 / 0 / 1 (the one reachable tick, seed 202, did not flip); positive-range readout on 31/33, 99/101, 36/38 lp reads; `max_n_targets` 10 / 16 / 14. All negative-margin ticks (1/5/5) were `committed_now=False` (sampling ticks), none on a committed tick.

**Instrument arm-sensitivity (964a's F3, demoted by the driver's own red-team to a recorded diagnostic -- NOT evidence):** corrected PERTURBATION keys differ between ARM_READINESS and ARM_PREREADINESS on 3/3 seeds, but those keys are functions of `_last_bias_range`, which is identically 0 on the constant-readout control, so they cannot fail to differ; the corrected COUNT partition (the family 964a actually found byte-identical) still differs on 0/3 seeds. The instrument question is closed by C1 (a behavioural demonstration), not by this; 964a's legacy byte-identity reproduced on seed 71 only (the env is now seeded, so 101/202 differ from 964a's unseeded rollouts).

## 2. Adjudication of the self-route and of the indexer flag

**Self-route label `mechanism_inert_at_own_magnitude_detector_verified` -- SUSTAINED as a label.** The detector demonstrably fires (C1), the controls hold, and the real mechanism moves neither selection nor action. This is the first instrument-verified null in the 964 chain: 964's zero was arithmetic (constant readout), 964a's was uncertified (uninformative instrument).

**The route text's INTERPRETATION of that label is CORRECTED by the run's own cells.** The driver pre-wrote, for this branch: "C2's measured minimum effective magnitude says HOW FAR the real perturbation sits from the one that does move it ... a minimum effective magnitude orders of magnitude above the real one is an F-dominance finding about the committed-selection layer (ARC-110 / MECH-439 territory)". But C2 = 0.1 = the shipped value. The bottom rung -- a railed synthetic at the SUBJECT'S OWN authority -- already moves selection on 3-21% of E3-fresh ticks. So the subject is not short of authority: its clamp never binds (`saturated_frac 0.0`) and its realised post-clamp contrast (2.1e-3..5.5e-3) is **1-3% of the 0.2 rail it is allowed**. The shortfall is **content contrast**, i.e. the integration gain (`curiosity_learning_progress_weight` 0.05 x a raw readout range of 0.11 / 0.042 / 0.084 across seeds), not selection authority, and no F-dominance ceiling at the selection layer is demonstrated by this run.

The driver's own design premise is refuted the same way. Its docstring states, as a load-bearing consequence of the authoring probe: "A MAGNITUDE-ONLY POSITIVE CONTROL IS UNREACHABLE BY CONSTRUCTION ... the maximum argmin-relevant perturbation curiosity can EVER contribute is a range of 0.2 -- below the smallest positive margin [0.5986]". In the full run the subject arm's smallest positive margins are 0.029 / 0.0066 / 0.0003 (across all arms 0.0026 / 0.0018 / 0.00017) and the range-0.2 rung fires on 3/3 seeds. The abandoned first-draft **magnitude** ladder was the design that would have sized the missing quantity; it was killed by a 40-step smoke that saw too few fresh ticks -- a smoke-power failure read as a construction impossibility.

**C2 is not an independent criterion and is left-censored.** In the driver, `c2 := (min_effective is not None)`, and `min_effective` exists whenever any rung fires on a majority; C1 asserts the top rung fires, so C1 implies C2 unconditionally (monotonicity is not needed). Its VALUE is the information, and that value is censored at the bottom rung: the ladder has no rung below shipped, and every rung injects m=1000, railing the clamp, so the ladder sweeps authority only. It cannot locate a minimum effective authority once the bottom rung fires, and it cannot measure the minimum effective **content** magnitude at all. (Hygiene, not a defect in C1 or C3.)

**Indexer `vacuous_pass` -- NOT SUSTAINED.** `build_experiment_indexes.py` rule (3b) fires on any PASS with a `load_bearing:true` criterion `passed:false`. The driver's `combination_rule` is an ORDERED GATE: `outcome` is PASS when the run ADJUDICATED (gate green and C1 met) and C3 is the *selector* between two labels, never an AND-gate member. This is exactly the false-flag class recorded in `failure_autopsy_V3-EXQ-946_2026-08-25.md` Sec. 6. The PASS rests on a real detector, not on nothing. Recommendation to driver authors of this shape: declare the selector semantics so (3b) stops firing on legitimately-adjudicated diagnostics.

## 3. Claim-layer map

MECH-482 (`mechanism_hypothesis`, `candidate`, `epistemic_category: substrate_conditional`, `v3_pending: true`, `pending_retest_after_substrate: true`, `diagnostic_evidence_adjudicated: true`; `depends_on` MECH-313/314/314a/314b/314c; `live_status.evidence.from` currently cites `failure_autopsy_V3-EXQ-964a_20260914`; no scoring experimental entries in `claim_evidence.v1.json`; no MECH-482-specific literature review -- Q-089's targeted review carries three directed-exploration entries).

**Did the experiment test the claim under conditions where it could express itself?** No -- and it did not try to. The claim's confirming signature (a consequential uncertainty that accumulates while raw novelty/PE fall, then quenches on resolution) and falsifying signature (novelty or raw uncertainty predict information-seeking equally well; no satiation) are not measured. What was measured is whether the SD-102 *realisation* has any behavioural authority at shipped parameters. It does not, for the reason in Section 2. That is an integration-gain fact about the substrate; it is **non_contributory** to the claim's hypothesis and must not be read as `weakens`. Tags are accurate (MECH-482 is the only claim; the run is a substrate-integration diagnostic for exactly that claim).

**Stored-category-condition check (Step 5):** the stored `substrate_conditional` was re-affirmed by governance-20260915 with the explicit condition "retest owed with a corrected reachability instrument and/or a positive-control arm ... before either a supports or weakens verdict". This run IS that retest and yields a null that is still not a claim verdict -- the category's own condition is met without being discharged; it stays `substrate_conditional` on a new, narrower condition (the content discrimination in Section 7).

## 4. Biological-reference triage

Closest mechanism: learning-progress / epistemic-deficit driven directed exploration over persistent uncertainty loci (Gottlieb 2013; Wilson 2014 directed vs random exploration; Frank 2009 -- all filed under Q-089). The SD-102 accumulator is a formal import of that idea (an LP-style accumulator feeding a score bias) and is faithful in KIND. Where the translation diverges is **authority allocation**: a biological information-seeking drive has enough behavioural authority to override exploitation on some fraction of decisions; here the drive's maximal argmin-relevant authority is bounded to a range of 0.2 against score margins of 1-4.5, and the realised signal uses 1-3% of even that bound. A drive with no gain is the symbol of the mechanism without its functional role. This divergence is load-bearing for the ROUTING (it names the discrimination owed) and says nothing about the claim's truth. No `/lit-pull` is commissioned by this autopsy: the missing fact is a substrate measurement, not literature (a MECH-482-specific review remains a standing gap, noted, not routed).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | the run does not test the claim's signatures; it measures substrate integration gain |
| Biological reference | partial | drive-gain translation gap (Sec. 4); lit present only under Q-089 |
| Prerequisites | **present** | first time in the chain: multitarget regime, differentiating readout, verified detector, bit-identical control, seeded env |
| Implementation | complete / **partial at the integration gain** | accumulator, corrected instrument and positive control complete; the realised bias contrast is 1-3% of the rail the mechanism is bounded by |
| Environment | adequate | the same rollouts contain flippable ticks (synthetic at shipped authority moves 3-21%; positive margins down to 3e-4) |
| Measurement | adequate (with one acknowledged vacuity) | detector proven by C1; both DVs and exact denominators recorded. C2 is a load-bearing criterion that cannot discriminate by construction (implied by C1, left-censored) -- acknowledged rather than graded away, since C1/C3 carry the finding; indexer flag is the ordered-gate false-flag class |
| Integration | coupled but under-scaled | live path on 93.9% / 98.0% / 94.7% of E3-fresh ticks with positive range; one strict-reachable tick in 172 (seed 202, own perturbation ~3x the margin), no flip -- an n=1 datum FOR H-pat, noted |
| Scale | adequate for the authority question; insufficient for the content question | 172 E3-fresh paired comparisons; a content ladder, not more seeds, is what is missing |

**Failure-location (GOV-FAILLOC-1): MIXED -- MEASURES established (adequate), ENVIRONMENT established (adequate), MECHANISM partial (integration gain / authority allocation). REE FAILED not reachable and not asserted.** Recorded per-target in the JSON as `failure_location`.

**Recommended `epistemic_category`: `substrate_conditional` (STAYS).** Not `substrate_ceiling`: minimum effective authority equals shipped, so no ceiling at the selection layer is shown; the remaining gate is a content-contrast discrimination that is a spike, not yet a build. Not `standard`: the claim remains gated on the SD-102 integration question.

## 6. Cluster pattern

Single scope. No other pending FAIL/diagnostic shares this substrate or shape. The 964a artifact flagged a resemblance to the "single-arena F-dominated selector" pattern (V3-EXQ-569g/684/700/709/710; MECH-439 / ARC-110); **this run does not support counting 964b as an F-dominance instance** (Section 2) -- recorded under `read_across_not_adjudicated` for governance's cross-claim pattern tracking. The F-dominance question re-opens only if the real pattern needs authority above the rail, or if H-pat wins (Section 7).

## 7. Learning extracted and repair pathway

See `learning_extracted` in the JSON for the full list. The load-bearing items: (1) first instrument-verified null in the chain -- real readout at shipped gain moves selection on 0/172 E3-fresh ticks; (2) the shortfall is content contrast (1-3% of rail), not authority; (3) the driver's "unreachable by construction" absolute is contradicted by its own cells, and the abandoned magnitude ladder was the right design; (4) C2 implied by C1 and left-censored; (5) the pre-written F-dominance route text assumed C2 >> shipped; (6) integration gain is a first-class substrate parameter (k to rail 37-94x across seeds); (7) `vacuous_pass` here is the V3-EXQ-946 class; (8) the 964a brake release was explicitly terminating and this run is the hit it anticipated.

**Node classification:** `complex (probe-gated) / puzzle (known rules)`. The frame is well-posed and one fact is missing: does the REAL readout pattern, scaled to the rail where a same-authority synthetic already moves selection, move E3's committed selection? If yes -> **magnitude-limited**: a gain of ~37x / ~94x / ~48x (seeds 71/101/202; ~100x to clear the rail everywhere) on `curiosity_learning_progress_weight` is a *measured* config fix (the sizing 964a said must come from a working instrument), and MECH-482's first genuine behavioural test follows. If no, while range-matched synthetic and permuted-real controls do fire -> **pattern-limited**: the readout's cross-candidate structure is selection-irrelevant at any gain; that is a genuine substrate_ceiling reading, the brake fires, and the route is `/implement-substrate` (readout / target-frame, or ARC-110 authority segregation). No unambiguous build exists TODAY, so `/implement-substrate` now would be building before knowing which build.

**Routing: `queue-experiment` -- a NEW EXQ number (new question: magnitude- vs pattern-limited), NOT a lettered 964 re-test, carrying a GOV-FANOUT-1 `fanout_recommendation`** (two live hypotheses, two probes on different axes, both in ONE yoked diagnostic: 12 followers, ~2x 964b's streams, est. 22-28 min):

- **H-mag (axis: drive):** amplified-REAL-readout ladder, k in {1, 10, 40, 100} at SHIPPED `curiosity_bias_scale`, top rung sized off the WORST seed (k to reach the 0.2 rail = 36.6 / 94.2 / 47.5; k=40 alone reaches it on seed 71 only -- red-team F1), same yoked harness and DV (selection divergence over E3-fresh ticks, seed majority), per-rung realised post-clamp range and `clamp_saturated_frac` recorded. Null, stated on the realised quantity: the real pattern does not fire on a seed majority even on rungs whose recorded post-clamp range has crossed the rail.
- **H-pat (axis: representation):** per-rung range-matched controls -- a synthetic ramp rescaled to the real x k range, and the real vector permuted across candidates within each tick -- plus the sign of the real bias on the runner-up at each committed tick. Pattern-limited iff real fires strictly less than both controls at the same range on a majority. Null: real fires at the rate of its range-matched controls.
- Eliminated by THIS run (do not re-pose): H-auth (authority is the bottleneck) and H-instr (detector cannot fire).

**Substrate queue: `amend` `sd_epistemic_deficit_multitarget_readiness`** -- mark the 964a item `resolved` (the corrected instrument and the positive control it asked for were built and the detector verified by C1 -- the instrument's arm-sensitivity is deliberately NOT cited, per the driver's own F3), append an `open` 964b item naming the content-contrast finding and the discrimination owed, and refresh `implementation_hint` with the finding; `severity` stays `degrading`, `substrate_paths` unchanged, `status_phase` stays at its current value `validation_pending`, `ready` stays false.

**Manifest correction (routed to governance, red-team F3):** `evidence_direction` was written as `unknown`, so `claim_evidence.v1.json` currently derives **`supports`** (0.75, "PASS with supporting direction", `scoring_excluded: diagnostic_probe`) for MECH-482 from this run. Correct it to `non_contributory` on flat + run pack, exactly as governance did for 964 and 964a. No other path applies it.

**Re-derive brake (MOVE-3): literal count 3 with this target (964, 964a, 964b; threshold 2). RECOMMENDED: explicit producer release, NOT fired -- a USER decision at the gate.** Reasons: (a) neither prior hit is a genuine ceiling reading (structurally-unsatisfiable C2; uninformative instrument) and both count only via the step-4 direction fallback; (b) every letter changed the substrate or instrument -- the "substrate genuinely being enriched between letters" case the rule names; (c) the node is a puzzle with no unambiguous build; (d) the next experiment is a new question under a new number. **Terminating condition:** if the spike shows the real pattern does not move selection on a seed majority once its recorded post-clamp range has crossed the rail (ladder bracketed off the worst seed so the null is not right-censored), the brake FIRES on that autopsy and the route is `/implement-substrate`, no further letter. **Mechanical caveat:** with `action: amend` the tool predicate will NOT honour this release (`sd_epistemic_deficit_multitarget_readiness` has no IMPLEMENTED/VALIDATED line in `ree-v3/CLAUDE.md`), so `validate_queue` will WARN (not block) on the spike's queue entry unless its note records the brake clearance (its count reads 2 today, since this draft is skipped while `awaiting_human_confirmation`, and 3 on confirmation). Alternatives for the user: raise `RE_DERIVE_BRAKE_THRESHOLD` for MECH-482; accept `action: none` so the release binds mechanically (a predicate-fitting contortion -- not recommended); or fire the brake now.

**Draft `evidence_quality_note`:** see `recommended_evidence_quality_note` in the JSON (written for governance to append verbatim).

**Per-claim disposition (MECH-482):** direction `non_contributory`; `epistemic_category` STAYS `substrate_conditional`; status STAYS `candidate`; `pending_retest_after_substrate` STAYS true; `diagnostic_evidence_adjudicated` already true. What moves: the manifest `evidence_direction` (unknown -> non_contributory, flat + pack), the `evidence_quality_note` (append) and the `live_status.evidence` citation (964a -> this artifact); `change` tail: `-> stamp failure_autopsy_V3-EXQ-964b_2026-09-16`.

## 8. Step 9b -- frozen hypothesis ledger (DRAFT ONLY, not written)

New question `mech482_deficit_selection_authority` (claims: MECH-482), 4 hypotheses: **H-instr** and **H-auth** pre-registered by the 964b driver (queued 2026-09-15) and ELIMINATED by this run with the full bar (control passed, non-degenerate, discriminating non_contributory); **H-mag** and **H-pat** pre-registered by this autopsy, alive, adjudicating run = the spike above. `initial_frozen_count = 4`. Growth-restriction check: n/a (new question; the registry has no MECH-482 / epistemic_deficit question). Not written because (i) staging mode and (ii) `hypothesis_space_registry.v1.json` is under an active claim by `science-batch4-20260915` at the time of drafting. Full block in the JSON `hypothesis_space_ledger_pending`; the confirming session applies it, runs `build_hypothesis_space.py` + `check_hypothesis_space_integrity.py`, and adds the `drive` axis row to `axis_families.map` (-> `process`) in the same edit.

## 9. Step 7b -- mechanical pre-routing checks

`autopsy_pre_routing_checks.py --json`: **`fire_count: 0`** (run on the draft and re-run after the red-team corrections). C1/C2/C3/C5 applicable and silent; C6/C7 inapplicable to this manifest's shape (3 `arm_results` rows). The red-team independently grepped the wrapper seam `_curiosity_per_candidate_learning_progress` across `ree-v3/experiments/`: only 964b uses it, so no existing driver already does the amplified-real-readout ladder.

## 10. Step 7c -- adversarial red-team pass: VERDICT **CONTESTED** (model: **Opus 5**, cross-model; this session drafts on Fable 5.1)

Given the draft JSON, raw manifest, driver, substrate source, predecessor autopsies, claim entry and SKILL.md with this session's reasoning withheld; JSON first, ~30 load-bearing numbers recomputed from the cells (all matched), rules, then this `.md` last.

**The central inference survived every attack**: the verify-lift wrapper REPLACES the real readout and returns `None` exactly when it does (content-vs-content at identical authority on the identical tick set); `_last_bias_range` is the clamped deviation, i.e. the argmin-relevant quantity, offset argmin-inert; no downstream rescale (`normalize_score_bias_to_e3_range` / `use_modulatory_selection_authority` both off); 314a/314b off, so `max_post_clamp_bias_range == max_lp_dev_range` to 16 digits; C1 implies C2 and the left-censoring reading is exact; the brake count (3 with this target) and the `action: amend` caveat verified in `validate_queue.py`; `non_contributory` over `weakens` correct; fanout a genuine discrimination; `change` tail machine-checkable and not already true.

**Three contesting findings, all confirmed by this session and APPLIED above:**

1. **F1 (load-bearing, recommendation):** the first-draft H-mag ladder topped out at k=40, which reaches the 0.2 rail on seed 71 only (k to rail = 36.6 / 94.2 / 47.5: 109% / 42% / 84% of the rail at k=40), so its null was right-censored on 2/3 seeds -- while the terminating condition converted that null into a brake firing and a `substrate_ceiling` route. The same "bracket the quantity you size" defect this artifact diagnoses in C2. Fixed: ladder {1, 10, 40, 100} sized off the worst seed; null restated on the realised post-clamp range crossing the rail; "~40x" replaced with per-seed figures.
2. **F2 (durable text):** the verbatim-append `evidence_quality_note` and the `resolved_note` cited the corrected instrument's perturbation-key arm-sensitivity as evidence -- a test the driver's own red-team (F3, `:891-897`) demoted as unfalsifiable (the count partition is still byte-identical on 3/3 seeds). Fixed: clause deleted from both; C1 carries the instrument closure.
3. **F3 (routing gap):** no manifest `evidence_direction` correction was routed, and `claim_evidence.v1.json` derives `supports` from PASS + `unknown`. Fixed: added to the per-claim `change` prose and as `recommended_manifest_correction`.

**Hygiene applied:** C2's vacuity acknowledged against the `adequate` grade (Sec. 5); the monotonicity premise dropped from the C1=>C2 argument; "full run's" -> "subject arm's" margins; 93.9/98.0/94.7% for the live-path fraction; raw readout range per seed (0.11/0.042/0.084); the clamp-saturation sentence in Sec. 1; cost estimate 22-28 min; `status_phase` marked as the entry's current value; consumer count 2 today / 3 on confirmation; the seed-202 reachable-tick datum weighed for H-pat; the ordered-gate producer fix (declare selector semantics so indexer rule (3b) stops false-flagging) is chipped at session close rather than left only in `learning_extracted`.

**A CONFIRMED-after-corrections is not proof the artifact is clean; the 7b silence and the 7c verdict are independent layers, both recorded.**

## 11. Step 8 gate outcome -- CONFIRMED 2026-09-16T11:10:54Z

The `/failure-autopsy` session (844a9d73) that staged this draft presented the three gate decisions below and the user approved all three; the session then died on the weekly usage limit before recording them, so the answers were relayed through the account-handover session of 2026-09-16 and applied here.

1. **Re-derive brake -- explicit producer release (approved).** Literal R1-R3 count for MECH-482 is 3 (threshold 2); the brake is NOT fired: no unambiguous build exists, each letter changed substrate or instrument, and the next experiment is a new question. The release is not open-ended (Sec. 7 / `re_derive_brake.note`).
2. **Routing -- `queue-experiment`, new EXQ (approved).** Amplified-real-readout ladder k in {1, 10, 40, 100} with range-matched synthetic and permuted-real controls, discriminating H-mag (magnitude-limited) from H-pat (pattern-limited), GOV-FANOUT-1. If pattern-limited, the brake fires on that autopsy. Not chipped here (SKILL Step 8); `/governance` Step 2b chips it.
3. **Dispositions for governance (approved).** MECH-482 stays `candidate` / `substrate_conditional` / `pending_retest_after_substrate`; manifest `evidence_direction` unknown -> `non_contributory` (flat + run pack); amend `sd_epistemic_deficit_multitarget_readiness` (resolve the 964a item, append the 964b item); the hypothesis-ledger question `mech482_deficit_selection_authority` (4 hypotheses, H-instr/H-auth eliminated, H-mag/H-pat alive) was REGISTERED in `hypothesis_space_registry.v1.json` in this same edit (Step 9b, Mode A+B on a new question).
