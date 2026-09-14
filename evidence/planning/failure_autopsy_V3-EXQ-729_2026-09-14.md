# Failure autopsy: V3-EXQ-729 (MECH-268), 2026-09-14

**Status: AWAITING HUMAN CONFIRMATION.** Written headlessly (chip `chip-20260910-gflag0070-mech268-degenerate-pass-autopsy`, dispatched session, no live interactive user for the Step 8 gate) in staging mode per `/failure-autopsy` SKILL.md Step 2's "delegating a whole autopsy... run in staging mode" pattern. Nothing here has been applied to `claims.yaml`. The machine-readable companion is `failure_autopsy_V3-EXQ-729_2026-09-14.json`.

**Trigger.** GFLAG-0070 (`governance_flags.v1.json`), raised 2026-08-27, originally misdiagnosed a "same-day-requeue indexer bug." That diagnosis was independently found false twice (governance triage 2026-09-01, and the 2026-09-09/10 flag-backlog adjudication) and corrected in `claims.yaml` (2026-09-01, commit `3e032f4c78`). The real, still-open residual GFLAG-0070 names: **can a PASS carrying `non_degenerate: false` discharge MECH-268's ecological demonstration bar at all?** Neither V3-EXQ-729 run had ever had a `failure_autopsy`. This artifact is that autopsy.

---

## 1. Facts

Two runs, same `queue_id` (V3-EXQ-729), same experiment type (`v3_exq_729_mech268_dacc_saturation_liveloop`), both 2026-07-10:

| run_id | machine | timestamp_utc |
|---|---|---|
| `..._20260710T065147Z_v3` | `ree-cloud-4` | 06:51:47 |
| `..._20260710T113825Z_v3` | `DLAPTOP-4.local` | 11:38:25 |

Both `outcome: PASS`, `evidence_direction: supports`, `n_seeds_pass: 3/3`. Both carry `non_degenerate: false`, `degeneracy_reason: "harm_class_fraction_on: zero spread (constant=1, spread=0<=eps=1e-09)"`, and both are `scoring_excluded: "degenerate"` in `claim_evidence.v1.json` -- confirmed correct, intentional indexer behaviour (CLAUDE.md's documented degeneracy-exclusion rule), not a bug. `supersedes: null` on both -- these are independent replications on different machines, not a requeue of one run.

**Dry-run gate (Step 2a):** both run_ids checked via `scripts/check_dry_run_citations.py` -- `0 dry cited, 2 clean`. Neither is a smoke.

**Recording provenance (`validate_recording.py`):** both manifests are missing the always-core fields (`recording_schema`, `substrate_hash` top-level, `substrate_commit`, `machine_class`, `elapsed_seconds`, `config`, `seeds`) and carry no numeric `metrics.values` array (flat-scalar-readout finding). This run predates the 2026-07-12 Experimental Recording Standard by two days -- grandfathered, not itself a defect, but see Section 7 (recording-debt: the driver's own per-step series were never written to any pack file and cannot now be recovered).

**Driver (`ree-v3/experiments/v3_exq_729_mech268_dacc_saturation_liveloop.py`):** runs the real agent loop (sense -> generate_trajectories -> select_action) in a chronic-harm env, makes NO manual `record_outcome` call, and uses a counting spy to prove the DACC `_outcome_history` FIFO is populated by the live `select_action` tail. Five pre-registered criteria (C1-C5), 2/3-seed majority PASS rule. **Queue entry:** already removed from `ree-v3/experiment_queue.json` (normal post-completion behaviour); no `supersedes` chain.

**Per-seed results (both runs, all 6 cells identical in shape):**

| | ARM_ON sat_final3 | ARM_OFF sat_final3 | ON harm_class_fraction | ON live_calls/fifo_end | OFF live_calls/fifo_end | C1-C5 |
|---|---|---|---|---|---|---|
| every seed, both runs | **0.25** (bit-identical) | **1.0** (bit-identical) | **1.0** (bit-identical) | 50 / 16 | 0 / 0 | all PASS |

`mean_z_harm_a_norm` varies 2.85x across the 12 cells (0.510-1.452), all 10-29x above the 0.05 threshold -- `harm_class_fraction`'s constancy is not explained by the harm signal itself being constant.

---

## 2. Claim-layer map

**MECH-268** (`claims.yaml:44468`): "dACC conflict saturation... caps and habituates under repeated identical outcomes; does not grow unboundedly." `claim_type: mechanism_hypothesis`, `status: provisional`, `claim_level: mechanistic`. Prerequisites `SD-032b, MECH-258, MECH-260, SD-034` all implemented. Registered distinguishing property (lit-pull rec #1, `evidence_quality_note`): **"graded learning-rate adapter rather than a binary habituation cap."** `what_would_answer` currently reads "ESTABLISHED (do not re-test) -- all three registered levels PASSED," crediting V3-EXQ-729 with satisfying V3-EXQ-468's commitment-vs-contradiction falsifier "in spirit" and calling the mechanism "fully validated." Both of those specific claims are contested below (Section 6).

**Did the run test the claim where it could express itself?** Yes, for the live-wiring/binary-firing bar specifically. No, for the claim's registered graded/adapter property -- that property was never in play in this run's measurable range (Section 4).

---

## 3. Biological-reference triage

Closest mechanism: primate/rodent dACC PE habituation under repeated identical outcomes (Bryden et al 2011 -- **not** 2019 as `claims.yaml`'s `functional_restatement` states; the filed lit entry and `evidence_quality_note` both say 2011). Shenhav et al 2013/2016 EVC framework; Behrens et al 2007 volatility-adaptive learning-rate signal. Lit-pull is **complete, 8 entries** in `evidence/literature/targeted_review_connectome_mech_268/entries/` (two more were added 2026-05-16 after `claims.yaml`'s "6 entries" text was written -- stale count, minor hygiene). Not a formal-definition import; a direct biological translation. No divergence newly found here.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact, narrowly | live-wiring bar tested and could express itself; graded property was not exercised |
| Biological reference | clear | see Section 3 |
| Prerequisites | present; SD-034 not exercised | closure never reset the FIFO in the measured window of any cell (sat_factor is exactly 0.25 for the entire 150-step final third, every cell) |
| Implementation | complete | `dacc.py:229-253`, live-wired via `agent.py`'s `select_action` tail; spy-confirmed 50 calls / 16 fifo_end in every ON cell, 0/0 in every OFF cell |
| Environment | under-determined (H1 vs H2, see below) | deliberately hazard-dense by design, OR the confirmation metric is near-vacuous for any harm-stream-enabled run -- the data do not distinguish these |
| Measurement | adequate for wiring only | sat_factor's ON value (0.25) is arithmetic, not measured, once the precondition saturates; only pre-saturation PE is recorded, nothing post-saturation |
| Integration | coupled and stable | end-to-end spy-confirmed, 2 machines, 3 seeds; one substrate-hash provenance anomaly in run 2 (see below) |
| Scale/capacity | adequate | P0 converged, no aborts, all 12 cells |

**Failure-location summary (GOV-FAILLOC-1):** not applicable -- both runs are PASSes; no organism-level "REE failed" observation is being made or is at issue here.

---

## 5. The core adjudication: does the degenerate flag void the PASS?

**No, for the narrow claim this run was built to test.**

Of the five pre-registered criteria:

| criterion | content | status |
|---|---|---|
| C1 `ON sat < 0.95` | contingent on chronic harm holding | arithmetic once C4's precondition saturates (see below) |
| C2 `OFF sat >= 0.99` | tautology | `dacc.py:237-238`'s early return when `dacc_saturation_enabled=False` -- the OFF arm never sets it |
| C3 `ON sat < OFF sat` | tautology | follows from C1+C2 |
| C4a `live_calls>0 AND fifo_end>0` | **genuinely contingent -- the real F-C3 wiring test** | PASS: 50/16 vs 0/0, every cell |
| C4b `harm_class_fraction>=0.5 AND live_record_harm_fraction>=0.5` | this is the flagged metric | near-vacuous: constant 1.0 across all 12 cells |
| C5 `OFF: 0 calls, 0 fifo` | tautology | same gating flag as C2 |

**The `harm_class_fraction_on` metric the manifest's non-degeneracy self-report flags is a direct conjunct of C4 (driver line 511) -- not an auxiliary side-check separate from the pass criteria.** The genuinely informative content in these five criteria is narrower than "5/5 PASS" suggests: it is C4a alone. And C4a **is** exactly what V3-EXQ-729 was built to establish -- that `DACC.record_outcome` is called from the live `select_action` path, not only from V3-EXQ-463b's synthetic per-step injection. That result is real, non-degenerate by any test, and reproduced independently on two machines across three seeds each.

**The ON-vs-OFF sat_factor contrast (0.25 vs 1.0) is NOT itself independent confirmation of "the effect is real."** It passes the indexer's own `sat_factor_arm_contrast` degeneracy check, but that check (`metric_groups_are_degenerate`) only asks whether the two arm values differ within a seed -- and they are GUARANTEED to differ here regardless of any measurement, because OFF's `1.0` is a hard-coded early return and ON's `0.25` is the arithmetic constant `1/(1+0.5*(8-2))` once the FIFO fills with one outcome class (exact in binary floating point; independently corroborated by V3-EXQ-463's `UC4_monotone_in_recurrences` ladder at the same `excess=6`). Citing that check's pass as evidence the saturation effect "is real" would be circular. It is real in the sense that mattered for this run's registered purpose -- record_outcome genuinely fires live -- but the specific 0.25 attenuation magnitude carries zero seed- or behaviour-sensitive information, and "saturation attenuates PE" itself is an entailment of the `pe_saturated = pe_capped * f_sat` formula, not a directly recorded observation (only pre-saturation PE is written to either manifest).

**Verdict: YES, this PASS discharges MECH-268's live-wiring/ecological bar -- narrowly.** It does NOT discharge, and `what_would_answer` currently over-claims on, two points: (1) satisfying V3-EXQ-468's commitment-vs-contradiction falsifier "in spirit" (729 has no commitment manipulation at all -- 468 is an unrelated SD-034/MECH-090 cluster); (2) demonstrating graded saturation (the claim's own registered distinguishing property vs. a binary cap) -- gradedness has zero loop-level evidence to date, validated only at the unit/arithmetic level (V3-EXQ-463's UC4/UC5).

---

## 6. Environment adequacy: an open question, not resolved here

`mean_z_harm_a_norm` varies 2.85x across the 12 cells while `harm_class_fraction` never moves off `1.0`, 10-29x above its own 0.05 threshold. Two readings are both consistent with this:

- **H1 (as the driver's docstring frames it):** the eval env is deliberately hazard-dense (`num_hazards=6, size=7`) specifically so the chronic-harm precondition holds "regardless of policy" -- by design, not a defect.
- **H2:** `harm_class_fraction` is near-vacuous for *any* run with the affective-harm stream enabled, because the encoder is never trained (driver docstring: "z_harm_a is a fixed projection of harm_obs_a") -- the metric may simply not be able to fall below its own threshold in this substrate regardless of hazard density.

The recorded data cannot discriminate H1 from H2 (Section 8's routing addresses this).

---

## 7. Recording-debt and a provenance anomaly

The driver builds full per-step series (`sat_factor_series`, `pe_unsaturated_series`, `z_harm_a_norm_series`, driver lines 303-305) and collapses them to three means before writing the manifest. Neither run's pack directory contains a per-step artifact -- only `manifest.json`/`metrics.json`/`summary.md`. This is **recording-debt** in the Experimental Recording Standard's sense (data that existed at run time and was never durably recorded), not a measurement gap requiring a redesign -- see routing.

Separately: 11 of 12 arm-cells across both runs carry `substrate_hash: 80c468f3964c...`; run 2's seed-42 `ARM_OFF` cell alone carries a different hash (`7dfebe5cf458...`). Since `run_seed` executes OFF before ON per seed, in order 42/43/44, the `ree-v3` tree changed under the run after its first cell -- breaking the driver's own "training identical to ARM_OFF -> bit-identical weights" premise for that one seed, and that cell is the designated `reuse_eligible:true` minted OFF baseline. Flagged for the record; it does not change this autopsy's numerical verdict (the affected cell is not the outlier on any criterion).

Also unresolved: seed-44 `ARM_OFF`'s `mean_pe_unsaturated_final_third` is bit-identical to 17 significant digits across both runs, on different machines, despite OS-entropy env seeding and non-identical `mean_z_harm_a_norm` between the two runs' seed-44 OFF cells. Could not be explained from the artifacts on disk. Recorded as a loose thread, not adjudicated.

---

## 8. Granularity-debt recurrence check

`granularity_debt_cluster.py MECH-268`: 5 prior targets (all `SD-034`/`MECH-268`/`MECH-090` closure-control-plane behavioural tests -- `failure_autopsy_SD-034-closure-cluster_2026-06-12`, `-control-plane-d_2026-06-13`, `V3-EXQ-460b-461b-464b-466b_2026-06-04`, `V3-EXQ-468e_2026-06-18`, `V3-EXQ-468f_2026-06-20`). Alignment distribution: `intact=2, other=2, unstamped=1` -- no target reads `weakened`, so the trigger does not formally fire.

**However**, reading the "other"/"unstamped" prose (as the tool's own printed warning requires before concluding): `V3-EXQ-468f_2026-06-20` reads *"MECH-268 not fairly tested... C1's 3/3 pass is degenerate (natural release, not closure-coupled)"* -- a structurally similar vacuous-criterion pattern (a criterion PASSing without exercising the claim mechanism it targets) to this autopsy's own C2/C3/C5-tautology finding above, though on a different specific criterion (closure-coupled release, not saturation magnitude) and different specific sub-mechanism (SD-034 closure authority, not dACC PE saturation itself). **Borderline** -- flagged for `/claim-synthesis` to weigh, not unilaterally asserted.

**Re-derive brake:** 3 of the 5 prior autopsies carry literal `category=substrate_ceiling`, meeting the N=2 threshold for MECH-268 generically -- but all 5 concern the SD-034 closure-control-plane *behavioural* question (commit/decommit authority), a different substrate gap from this autopsy's live-wiring question (already confirmed complete, Section 9). The recommended follow-up below (non-saturating harm regime) is a new measurement question, not a same-ceiling re-derive of that cluster, so the brake does not fire against it.

---

## 9. Learning extracted and repair pathway

1. `check_degeneracy`'s zero-spread test fires before any floor/ceiling rail is consulted, so a ceiling-saturated precondition (every seed pinned at maximum, by design or near-vacuity) reads identically in the reason string to a genuinely dead metric -- only the manifest's `degenerate_metrics` dict plus the driver's own docstring let a reader tell the two apart, and this autopsy could not fully resolve which case applies here (Section 6).
2. A run-level `scoring_excluded: degenerate` tag on the indexer is coarser than the underlying defect: only one of the two load-bearing metrics `check_degeneracy` evaluated is genuinely degenerate; the paired ON-vs-OFF contrast passes the same check **by construction** (one arm value is a code early-return, the other an arithmetic constant), not because it carries independently-verified empirical content. Recovering a run's qualitative interpretability from a coarse exclusion tag requires checking each surviving criterion's own empirical content, not just whether the pass/fail bit survived.
3. The recurring `0.25` value is fully explained by `f_sat = 1/(1+0.5*(8-2)) = 0.25` (`dacc.py:245-252`) once `n_rec` saturates at the FIFO window -- worth citing explicitly for any future reader who might otherwise read a bit-identical cross-seed, cross-machine result as evidence of fabrication rather than a predictable consequence of a saturating precondition.

**Repair pathway.** `complicated (buildable)`: none -- `recommended_substrate_queue_entry.action: none`; nothing in the implementation is broken (attacked directly in red-team review, confirmed clean). `complex (probe-gated)`: yes -- two live hypotheses (H1/H2 above) plus the claim's own untested gradedness property both resolve with one cheap follow-up design: a non-saturating harm regime (lower `EVAL_HAZARDS` or raise `contextual_safety_harm_threshold`) with a post-saturation PE readout and per-step recording added. **Routing: `governance-note-only` (registry text correction, below) + `queue-experiment` (the follow-up design).**

---

## 10. Recommended registry edits (drafted, not applied)

Exact text in the JSON companion's `recommended_evidence_quality_note`, `recommended_what_would_answer_amendment`, and `recommended_implementation_note_amendment` fields. Summary:

- **`evidence_quality_note`:** append the full narrowed adjudication (what C4a establishes vs. what C2/C3/C5's tautologies and C4b's near-vacuity do not).
- **`what_would_answer` point 3 (ECOLOGICAL LEVEL):** replace -- strike the V3-EXQ-468 "satisfies in spirit" claim (468 has no commitment manipulation-relevant content to this run), and qualify the sat_factor description to note it is arithmetic, not graded.
- **`implementation_note`:** append a note that the "QUEUED"/"OUTSTANDING" language is stale (predates the 2026-07-10 PASS), and qualify "fully validated" to "validated for live-path wiring and binary on/off firing; graded ecological sensitivity is untested."
- **`epistemic_category`:** set to `standard` (no field currently exists on this claim).
- **`status`:** unchanged, stays `provisional`.

---

## 11. Red-team pass (Step 7c)

Run cross-model (drafting session: Sonnet 5; red-team: **Opus**), independently, without sight of the drafting session's reasoning, per SKILL.md Step 7c ordering (manifests -> driver -> substrate -> `_metrics.py` -> recompute -> draft JSON -> `claims.yaml`).

**Verdict: CONTESTED** (not refuted). The core conclusion -- live wiring is proven, the degenerate flag does not void that -- survived. Eight findings changed this final artifact relative to the pre-red-team draft (full list in the JSON's `red_team_pass.change_log`); the most consequential:

- The pre-red-team draft mischaracterized `harm_class_fraction_on` as "not itself a PASS/FAIL criterion" -- it is a direct conjunct of C4 (driver line 511). **Corrected.**
- The pre-red-team draft cited the ON-vs-OFF contrast's survival of the degeneracy check as evidence the effect "is real" -- circular, since that check is passed by code construction (OFF's `1.0` is a hard-coded early return; ON's `0.25` is arithmetic). **Corrected** -- Section 5 above now states precisely which criterion clauses carry genuine content (C4a alone).
- `claims.yaml`'s `what_would_answer` text was blessed as needing "no further correction" -- it does need correction (the V3-EXQ-468 "satisfies in spirit" claim is false; "fully validated" overstates). **Corrected** -- Section 10 above.
- `routing: governance-note-only` alone was under-responsive given recording-debt (per-step series existed and were never recorded) and a cheap, named follow-up design. **Corrected** to `governance-note-only + queue-experiment`.
- `re_derive_brake.prior_substrate_ceiling_autopsies` was stamped `[]`; the skill's own R1-R3 counting snippet returns 5 hits for MECH-268. **Corrected**, with reasoning for why the brake still does not fire (different substrate question).
- Citation hygiene: Bryden 2011 not 2019; 8 lit entries not 6; gradedness citation corrected (V3-EXQ-463's UC4/UC5 test it at the unit level; V3-EXQ-468 is unrelated).

**Single strongest point against the draft** (Opus's phrasing): the entire load-bearing ON-vs-OFF contrast is determined by code structure rather than measured -- ARM_OFF's `1.0` is a literal early return under a flag the driver never sets, and ARM_ON's `0.25` is the fixed value of `1/(1+0.5*(8-2))` once the FIFO fills with one class. The honest formulation is that V3-EXQ-729 measures exactly one contingent thing -- is `record_outcome` called from the live loop at all -- and that this is, in fact, precisely the question it was built to answer.

**Single strongest point for the draft:** the arithmetic-ceiling diagnosis is correct, non-obvious, and independently reproducible from V3-EXQ-463's own data (`UC4` yields `0.25` at `excess=6` from the same `strength=0.5`). Without it, six bit-identical cross-seed, cross-machine `0.25`s would read as suspicious in their own right.

---

## 12. Mechanical pre-routing checks (Step 7b)

`autopsy_pre_routing_checks.py` on the pre-red-team draft: **1 fire (C2, x2 duplicate)** -- `substrate_queue.json`'s `commitment-closure-control-plane` entry already "unblocks" `MECH-268` (among `SD-034, MECH-260, MECH-090, MECH-261`) and was not mentioned by `action: none`. **Dismissed**: that entry addresses the SD-034 closure-control-plane *behavioural* wiring gap (commit/decommit authority, beta-gate engagement) -- confirmed by reading its `implementation_hint` -- which is unrelated to what this autopsy adjudicates (dACC `record_outcome` live-path wiring, confirmed complete). No new substrate entry needed or created by this autopsy; the pre-existing entry is neither resolved nor duplicated by it.

---

## 13. Deviation from the skill's coordination-plane pause step (recorded per headless-worker judgment)

Step 1 of `/failure-autopsy` instructs opening a second claim pausing the coordination plane (`COORDINATION_PLANE_PATHS`) for the duration of the diagnosis. That claim was attempted and refused by the coordinator's arbitration: `substrate_queue.json` and `ree-v3/experiment_queue.json` are both actively owned by genuinely live, unrelated work sessions (`queue-batch1-20260914`, `metaworker-chip-20260908-sleep-integrated-world-model-update-validation`) at the time this autopsy ran. Forcing the pause would have contended with real, in-progress work for a diagnosis that (a) does not itself write to any coordination-plane file, and (b) was already substantially complete by the time the pause was attempted. Judgment call: proceeded without the pause, and confirmed this autopsy makes no write to `claims.yaml`, `substrate_queue.json`, or `experiment_queue.json` at any point (only the two new planning-directory artifacts named at the top of this file). Recorded here rather than silently skipped.

---

## 14. GFLAG-0070 disposition

Recommend: resolve GFLAG-0070 (`governance_flag.py resolve`, never a hand-edit) citing this artifact. The flag's own "correct edit" text (`governance_flag_adjudication_20260909.md`) asked for exactly this autopsy to be run; it now exists, with a narrowed-but-affirmative answer to the flag's residual question plus a recommended follow-up. Final application of the registry edits above is `/governance`'s job (Step 4/6a), gated on this artifact's own `status: awaiting_human_confirmation` being confirmed first.
