# Failure autopsy (diagnostic adjudication) -- V3-EXQ-1012c, SD-E3-CHANNEL-COMMENSURABILITY rung 3 at the eligibility stage

- **Status:** `awaiting_human_confirmation` -- STAGING-MODE DRAFT (headless subagent inside `/governance` session `governance-20260924-workset`). The Step 8 interactive gate is OWED at the governance walk. Nothing marked reviewed; `claims.yaml`, `substrate_queue.json`, `review_tracker.json`, manifests and `hypothesis_space_registry.v1.json` untouched. No claim opened; nothing committed.
- **Generated (UTC):** 2026-09-24T06:07:19Z (red-team applied 2026-09-24T06:23:36Z)
- **Scope:** single
- **Target:** `v3_exq_1012c_e3_commensurability_eligibility_stage_validation_20260923T215322Z_v3` (queue_id `V3-EXQ-1012c`), `experiment_purpose: diagnostic`, outcome **PASS**, self-route `commensurate_at_eligibility_both_regimes`, tagged MECH-439.
- **Trigger:** diagnostic PASS (trigger 2). The question is whether it passed for a real reason.
- **Dry-run gate:** `check_dry_run_citations.py` over the run_id, `V3-EXQ-1012c`, `V3-EXQ-1012a`: 0 dry cited, 1 clean. `--family v3_exq_1012c`: 0 dry / 1 real. `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- **Headline:** the PASS is real. The instrument is sound, the criterion can fail, and the reference arms behave as designed. It validates rung 3 **as scoped**: 3 of 5 channels, eligibility stage only, 936 regime. It validates it against a readiness target that **has not been ratified by the user** as the rung's acceptance condition. That ratification is the load-bearing governance step (section 7a).

---

## 1. Facts (no interpretation)

### 1a. Why the run exists

The rung-3 operator (ree-v3 `c47b885`, 2026-09-07) divides each E3 channel's per-candidate term by an EMA of that channel's own cross-candidate SD. Its validation target has changed twice:

1. **Original:** >= 2 channels above a 1e-3 relative variance share. Found to be an arithmetic identity of the operator (GFLAG-0234, 2026-09-10).
2. **GFLAG-0234 amendment (user-approved):** commit-flip rate under same-tick shadow OFF/ON. V3-EXQ-1012a measured it (0.82 / 0.72). The confirmed 1012a autopsy found the number had no reference value and asked for a placebo null.
3. **GFLAG-0297 design (`gflag0297_mech439_rung3_null_design.md`, 2026-09-23):** the design argues on paper that every primary-stage null is an identity, depends on a free knob, or answers a different question. The placebo is one of these. In this regime the primary score reaches the executed action only through membership of a range-denominated margin-eligible set E, so the design moves the test there. The DV is the per-channel knockout authority ratio `R = min_c J_c / max_c J_c`, where `J_c` is the tick-mean Jaccard distance between E and E with channel c knocked out. Same-tick references: **OFF** (monopoly anchor) and **ORACLE** (tick-local SD normalisation). C1: `R_ON >= 0.25` in >= 3 of 4 seeds, per regime. GFLAG-0297 was resolved by the design chip. It was not resolved by a user-approved target amendment.

### 1b. Design

There are two arms, both with the operator ON: `C_fed_operator_on` and `C_starved_operator_on`. Each runs 4 seeds (42/43/45/46), P0 60 episodes, then P1 up to 200 genuine latch-gated selections. The regime is byte-identical to 1012a/571c. Instrument gates are routed first:
- I1: live score vs reconstructed channel sum.
- I1b: replay self-check.
- I1c: an independent genuine operator-OFF replay vs reconstructed S_OFF.
- I2: float32 eligible-set size vs the live shortlist size, on a 1% rate.

The verdict grid is a partition: instrument > readiness > per-regime class {not_ready, moot, commensurate, ema_lag, shape_range}.

### 1c. What the manifest reports

| arm | seed | fresh | R_ON | R_OFF | R_ORACLE | top-J channel ON / ORACLE | mean \|E\| live | final_commit_by_primary |
|---|---|---|---|---|---|---|---|---|
| fed | 42 | 209 | 0.653 | 0.000 | 0.726 | f / f | 7.00 | 0.024 |
| fed | 43 | 201 | 0.599 | 0.001 | 0.618 | f / residue | 10.24 | 0.124 |
| fed | 45 | 258 | 0.408 | 0.000 | 0.833 | f / f | 7.81 | 0.054 |
| fed | 46 | 220 | 0.858 | 0.000 | 0.860 | harm / harm | 6.64 | 0.055 |
| starved | 42 | 158 | 0.437 | 0.047 | 0.651 | f / f | 8.02 | 0.013 |
| starved | 43 | 200 | 0.454 | 0.043 | 0.594 | f / harm | 13.94 | 0.015 |
| starved | 45 | 205 | 0.531 | 0.104 | 0.685 | f / residue | 6.91 | 0.044 |
| starved | 46 | 205 | 0.620 | 0.062 | 0.961 | f / harm | 7.08 | 0.049 |

- **Criteria.** `C1_eligibility_authority_fed` passed 4/4 (bar 3). `C1_eligibility_authority_starved` passed 4/4. `instrument_clean` passed: residual 0, self-check 0 and OFF cross-check 0 failures, worst I2 mismatch rate 0.0, max I1 relative residual 1.4e-07.
- **Readiness.** All 10 preconditions met. Worst-seed fresh selections 201 fed / 158 starved (floor 60). `operator_engaged`, `clamp_config_landed` and `residue_protocol_landed` read 1.0. `n_content_channels` is 3 in every cell (f, harm, residue). This gate is own-scale-relative, so it certifies only non-dead channels; see sec. 2.
- **Flags.** `criteria_non_degenerate` is true for both regimes. `on_off_separated` is true.
- **Shortlist and k.** The shortlist is active on 100% of scored ticks. k = 32 on every tick. The live selected index was inside E on every tick.
- **Channel scales (fed seed 42).** f 6.6e-05, harm 2.6e-03, residue 0.675. benefit and goal are 0.0 in all 8 cells, with 0 content ticks each. `z_goal_stream`: ticks_active 0 of 53,837 (writer_defect false).
- **Realised spread vs EMA, r_c(t).** Medians are 0.12-1.09 across all channels. Maxima: f 2.3-22.3; harm/residue 5.0-178 (starved seed 45 harm: 178). f exceeds 10x its EMA in 6/8 cells, so all three channels burst.
- **Shape indices** (max-median)/sd and (median-min)/sd. Medians are near-symmetric, ~1.6-2.6, in 7/8 cells; the Gaussian k=32 expectation is ~2 and a single-candidate spike is ~5.6. **Starved seed 43 is the exception:** harm and residue are sparse-HIGH (high-index median 3.4/3.1 vs low 1.2/1.2), with the eligible set inflated to 13.9. Per-tick maxima reach 5.76, which is above the single-candidate-spike value of 5.57 that the design quotes: the index is not bounded by the spike case. Spike-shaped ticks occur, but they are not typical.
- **Manifest direction.** `evidence_direction: non_contributory` and `evidence_direction_per_claim` `{MECH-439: non_contributory}`. The flat manifest also carries an `evidence_direction_note`; the run pack does not (converter whitelist). No re-inference guard is needed, because `non_contributory` is in the indexer's allowed set. The live index row reads non_contributory / `scoring_excluded: diagnostic_probe`, so the 1012a sec. 5g defect is closed for this run.

### 1d. Recording provenance

`validate_recording.py` reports 1 complete manifest with 0 always-core gaps. It includes `config`, `seeds`, `elapsed_seconds` (7356 s), `recording_schema rec/v1`, `substrate_hash`, a clean `substrate_commit` (846ae16), `machine ree-cloud-2` and the machine class. Advisory: 3 load-bearing criteria and no *top-level* `combination_rule`. The rule exists, under `interpretation.combination_rule`. Hygiene only.

### 1e. Same trajectories as V3-EXQ-1012a (measured here, not stated anywhere in the manifest)

Per cell, 1012c's final `channel_scale_estimates.scales`, `n_fresh_select`, `n_latched` and `p1_episodes_run` are **identical** to 1012a's in 8/8 cells. The `substrate_hash` differs only because the driver is in the hash. So 1012c is a re-instrumented replay of the same 8 trajectories. It is **not** an independent replication. The continuity readout (`primary_argmin_flip_rate`) matches 1012a in 7/8 cells. Starved seed 43 reads 0.3450 against 0.3400 (69 vs 68 of 200): 1012c recomputes the argmin on float64 reconstructed sums, 1012a on float32 replayed scores, so a single near-tie can differ. Hygiene.

### 1f. Expected vs observed

- **Expected.** The docstring and `interpretation.prior_note` state that PASS is the prior under Gaussian or sparse-HIGH shapes at r ~ 1, and that the moot branch is expected dead.
- **Observed.** Shapes are near-symmetric in 7/8 cells, with one sparse-HIGH cell. Median r is <= ~1, R_OFF is ~0, and the result is PASS in both regimes.
- **Failed criteria.** None.

---

## 2. Claim-layer mapping

| Field | MECH-439 (current, claims.yaml 2026-09-24) |
|---|---|
| claim_type | mechanism_hypothesis |
| status | candidate |
| epistemic_category | standard |
| ceiling_decision | exhausted |
| pending_retest_after_substrate | true |
| diagnostic_evidence_adjudicated | true |
| live_status.evidence.from | failure_autopsy_V3-EXQ-1012a_2026-09-14 |

**Could the claim express itself here?** No, and it was not meant to. This is the acceptance instrument for a substrate rung, and the driver declares `non_contributory` on every branch. **`non_contributory` is correct. No status, category or flag moves.**

**Read-across (not adjudicated).** MECH-439's `what_would_answer` opens with a NON-DEGENERACY PRECONDITION: >= 2 channels carry non-trivial cross-candidate variance SHARE on the same ticks (571c's n_live_channels >= 2). With the operator ON, that share condition is the GFLAG-0234 identity: shares tend to 1/k. So it cannot be read off this run. The eligibility-stage analogue is met: R_ON >= 0.408 in 8/8 cells. That is a **substituted operationalisation**, and any retest should say so.

`n_content_channels = 3` is **not** evidence for the precondition:
- It is own-scale-relative: "live by EMA" and sd_c(t) >= 0.1 * s_hat_c, with no cross-channel term (driver L706-708).
- So it holds for every non-dead channel, including in the fed OFF-scored cells where R_OFF = 0.000.
- It is not 571c's relative-share gate, which could fail and did.
- The design's own red-team F6 called it "a formality".

MECH-439's CONFIRMING branch, meanwhile, is "F's share stays above 0.85". That is **unreachable by construction** with the operator ON. 571c also found that the fed-regime monopolist is residue, not F. Any retest under the operator needs a restated confirming branch. That is a claim-text matter for governance.

## 3. Biological-reference triage

- **Closest mechanism.** Divisive normalisation / gain control before value integration: Carandini & Heeger 2012; Louie, Khaw & Glimcher 2013. The operator is faithful in kind, and literature is present (`targeted_review_connectome_mech_439`). **No `/lit-pull` owed.**
- **Divergence carried from 1012a.** Equal cross-candidate SD is *a* normalisation, not obviously *the* one.
- **New, measured divergence.** Canonical DN normalises by the **concurrent** pool, which is this run's ORACLE arm. REE uses a running EMA because `score_trajectory` scores one candidate at a time, so it sits closer to slow adaptation than to divisive normalisation. The run measures what that costs: **R_ON < R_ORACLE in 8/8 cells, mean gap 0.17**. This is not load-bearing here, because ON still clears the bar in every cell. It is the first measurement of the gap.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | not exercised (correctly) | substrate validation; precondition read-across in sec. 2 |
| Biological reference | partial | faithful in kind; the EMA-vs-concurrent-pool divergence is now measured |
| Dependency prerequisites | present, scope-bounded | operator engaged, clamp and residue protocols landed, 3 non-dead channels in 8/8 (own-scale gate, a formality); benefit/goal never entered |
| Implementation completeness | complete (3 live channels) | wired, stable, exercised: R_OFF ~0 vs R_ON 0.41-0.86 on the same ticks; not inert |
| Environment adequacy | adequate | 936/571c/1012a regime; real fed/starved manipulation; known upstream limitation (open corrupting contextmemory write-path entry) |
| Measurement adequacy | adequate | reference-bearing (OFF + ORACLE), triple instrument gate + I2, one failable criterion per regime with no disjunct, 1012a-owed readouts emitted. Caveats in sec. 5 |
| Integration adequacy | coupled and exercised at the eligibility stage | final pick within E (`_modulatory_accum`) not measured, by design |
| Scale / capacity | adequate denominator, thin between-seed | 158-258 selections/cell; 4 seeds/regime; same trajectories as 1012a |

**Failure-location (GOV-FAILLOC-1):**
- MECHANISM: established.
- MEASURES: established.
- ENVIRONMENT: established.
- **Net: n/a -- PASS, with no failure to locate.** `ree` is stamped false because REE FAILED also requires the competence to be absent, and here it was demonstrated.

## 5. The diagnosis: did it pass for a real reason?

**Yes.** Each vacuity route was checked against the manifest and driver:

1. **Not an identity.**
   - The operator equalises SD. The margin is range-denominated. So R depends on each channel's per-tick realised spread relative to its EMA and on each channel's per-candidate shape, and the operator fixes neither.
   - The design's Monte Carlo gives failing R on gate-green runs: sparse-LOW ~0.21-0.23 even at perfect equalisation, 5x lag 0.26, 10x lag 0.135.
   - The red-team at queue time independently reproduced the sparse-LOW failure (0.207).
2. **The DV discriminates on this run's own cells.** On the same ticks, the same candidates and the same content-tick set, R_OFF is 0.000-0.104 and R_ON is 0.41-0.86. That is the monopoly anchor behaving as predicted and the operator removing it.
3. **The instrument is independently checked.**
   - The I1c genuine OFF replay reproduces the reconstructed S_OFF, which proves the captured per-channel terms are the terms the selector used. That was red-team F1's worst case: a capture bug would have made E(S_ON) = E(S_OFF).
   - I2 reproduces the live eligible-set size on every shortlist-active tick.
4. **J magnitudes are non-trivial** (0.13-0.81 under ON), so R is not a ratio of near-zeros. |E| is 6.6-13.9 of 32, which is neither swallowing nor starving.
5. **The criterion has no always-true disjunct** (the 1012a defect). It is one threshold per regime.
6. **The stage is decision-relevant.** `final_commit_by_primary_frac` is 0.013-0.124, so ~88-99% of executed picks are made within E by the modulatory accumulator. The primary score reaches the action through E, which is exactly where this run measures.

**What bounds the PASS (carry these; none moves the verdict):**

- **(a) PASS was the stated prior (red-team F4).** Low surprise, but the test was genuinely failable. The information is in the shapes:
  - They came out near-symmetric in 7/8 cells.
  - The one skewed cell, starved seed 43, is sparse-HIGH, with |E| 13.9 and R_ON 0.454. That is the benign direction per the design MC (sparse-HIGH passes at r <= ~2).
  - No sparse-LOW channel, the shape that fails even at perfect equalisation, was observed.
  - The design doc flagged shape as a live risk, from 571c's inflated OFF shortlists.
- **(b) The tick-mean hides a heavy-tailed EMA error.**
  - R_ON < R_ORACLE in 8/8 cells *in sign* (mean gap 0.17). The gap exceeds 0.05 in 6/8 cells; fed43 (0.019) and fed46 (0.001) are effectively ties.
  - All three live channels burst: max r_c(t) is f 2.3-22.3 and harm/residue 5.0-178.
  - Harm and residue have the heavier tails and the lower typical-tick r (medians 0.12-0.65 in 7/8 cells).
  - f has content on ~100% of ticks, and its typical-tick r is closest to 1 (0.55-1.09).
  - Under ON, **f takes the largest eligibility authority in 7/8 cells, vs 3/8 under the ORACLE**. f's share of summed J is 0.31-0.53 under ON vs 0.26-0.40 under ORACLE.
  - A candidate mechanism, consistent with this but **not established**: burst-inflated EMAs under-weight harm/residue on typical ticks. f is top under the ORACLE too in 3/8 cells, so part of its authority is not an EMA artefact.
  - Consequence: the operator removes the residue/harm monopoly partly by promoting f's micro-spread (~1e-4 of its mean; ~10^3 ULP at float32 score magnitudes, so it is numerically real). The driver's docstring states this is by design. Whether that micro-spread carries decision-relevant content is the "principled?" question the design doc scoped out. The follow-on falsifier's matched-noise control is what would catch a noise-driven lift.
- **(c) 3 of 5 channels.** benefit and goal were never entered (goal: `z_goal_stream` 0 active ticks). Reviving them is a harness change.
- **(d) Eligibility stage only.** The pick within E is not validated.
- **(e) Not an independent replication of 1012a** (sec. 1e). It is a second, stronger measurement on the same 8 trajectories.
- **(f) The regime is tied to the open corrupting `contextmemory-write-path-addressing-degeneracy` entry**, which is also the regime the conversion falsifiers run in. A later default flip of `contextmemory_write_usage_balancing` changes the regime.

## 6. Cluster

Not a cluster.

## 7. Learning and routing

### 7a. The load-bearing governance step: ratify the target before admitting the PASS

The rung's registered readiness target lives in four carriers: `docs/architecture/sd_e3_channel_commensurability.md`, the 571c autopsy .md/.json, and `substrate_queue.json`. All four still carry the GFLAG-0234 commit-flip DV. `depends_on_unresolved[2]` on `f_dominance_conversion_ceiling` literally asks for *"a reference-bearing successor (placebo differential rescaling matched to the operator's log-spread; final_commit_by_primary_frac recorded per cell)"*.

1012c meets that in spirit: it is reference-bearing, and `final_commit_by_primary_frac` is recorded. It does not meet it in letter, because there is no placebo. The GFLAG-0297 design argues, on arithmetic this autopsy finds sound, that every primary-stage null is non-validating. **That argument has not been put to the user as a target amendment.** GFLAG-0234 was user-approved; GFLAG-0297 was closed by the design chip. Admitting the PASS as "rung 3 VALIDATED" without that ratification would repeat, in reverse, the move the lineage has twice caught: grading a rung against a target no one ratified.

### 7b. Routing: `governance` (nothing to build)

Work-graph class: **none on this node**. No build, probe or fact is owed. What remains is a user decision gate (ratification and refusal release) plus bookkeeping. The entry itself is `implementation_status: wontfix` and `status_phase: closed`.

**All of the following is HAND-APPLIED at the walk.** Governance Step 6a-iv's mechanical `amend` path only appends `failure_record_entry` (null here) and updates severity/paths (unchanged here). It does not process `resolves_prior_failure_record`, `depends_on` moves, carrier amends, the ladder or doc flips. `validation_record_entry` has no Step 9 schema precedent, and GOV-APPLY-1 does not read it. No standing backstop catches a dropped item here.

1. **User decision:** ratify the eligibility-stage target (R_ON >= 0.25 in >= 3/4 seeds per regime, with OFF/ORACLE anchors) as rung 3's acceptance condition.
2. **If ratified, amend `f_dominance_conversion_ceiling`:**
   - Move `depends_on_unresolved[2]` to `depends_on_resolved`, with the scope stated.
   - **Amend the two remaining target carriers, as GFLAG-0234 did for all four together.** These are the target sentence in the 571c autopsy .md/.json, and the 571c `failure_record` item's own `target` field, which still ends on the GFLAG-0234 commit-flip text. Append the ratified eligibility-stage target and preserve the prior text verbatim.
   - Then mark the 1012a and 571c `failure_record` items `resolved` **against the ratified target**. The currently registered commit-flip target was never validated by any run. 571c is resolved *by a build*: the raw-substrate monopoly with the operator OFF is unchanged, and R_OFF reproduces it.
   - Refresh the stale `fallback_ladder` rung-3 row ("V4-leaning ... recoup-to-V3").
   - Leave severity and substrate_paths unchanged.
   - Append no failure record, since this is a PASS. A validation note is drafted in the JSON.
   - Flip SD-E3-CHANNEL-COMMENSURABILITY IMPLEMENTED -> **VALIDATED (eligibility stage)** in the ree-v3 CLAUDE.md index, `docs/substrate/SD-E3-CHANNEL-COMMENSURABILITY-*.md` and the REE_assembly architecture doc.
3. **User decision:** release of the 936-family / 654h-class conversion-falsifier refusal that `depends_on_unresolved[2]` gates. Its release condition is now met at the stage where the action is decided. The recommendation is to release only for falsifiers run in this same regime with the operator ON and the 3-channel scope stated. `ready` stays false: items [0] (SD-018 field-head validation) and [1] (SD-e1 var-bar re-registration) are untouched.
4. **MECH-439:** append the drafted evidence_quality_note and move the citation stamp to this artifact.

**Follow-on named, not spawned** (governance chips once ratified):
- If (3) releases: a **redesigned conversion falsifier with the operator ON** (new EXQ, different question: does committed-action-class entropy lift over collapsed-proposer and matched-noise controls once eligibility is commensurate?). MECH-439's confirming branch should be restated first.
- Optional: revive benefit/goal channels in this regime.
- Optional: final-commit-stage replay. It stays reserved.
- Registry hygiene: refresh the arc131 `H-operator-amplifies` basis and the question's `distance_phrase`.

**Explicitly not recommended:**
- Reading the PASS as MECH-439 evidence.
- Treating the literal placebo residual as satisfied without ratification.
- Counting 1012c as independent of 1012a.
- Another lettered MECH-439 re-test against the same substrate.

### 7c. Re-derive brake

- The R1-R3 recipe (re-run 2026-09-24) gives MECH-439 **15 counted hits**, the same list as 1012a, against a threshold of 2. **The brake remains fired for MECH-439.**
- This run adds **0**: its per-claim category is `standard`, and it is substrate-validation work, which is what the brake routes *to*.
- `re_derive_brake.fired: false` on this target means only that this run does not count. It does not mean the claim is released.
- Of the upstream work, rung 3 is now validated; items [0] and [1] are not. A same-granularity lettered re-test of MECH-439 is still refused. The permitted shape is the redesigned, operator-ON falsifier in 7b, and that is a user release decision.

### 7d. Granularity-debt trigger: does not fire

`granularity_debt_cluster.py` finds 21 tagging targets. No target reads `weakened`, so this is measurement/substrate debt, not granularity debt.

### 7e. `pending_retest_after_substrate`

It stays **true**, because the claim's own retest has never run and items [0] and [1] are open. Narrow-supports check: MECH-439 carries no supports entries to narrow.

## 8. Draft evidence_quality_note (MECH-439)

See the JSON `recommended_evidence_quality_note`. In summary, it records:
- The validation, the R figures and the anchors.
- The instrument cleanliness.
- The failability of the criterion.
- The five scope bounds: 3/5 channels; eligibility stage only; the EMA-vs-ORACLE gap and f promotion; the same trajectories as 1012a; the corrupting contextmemory regime.
- That MECH-439's retest has never run.

## 9. Step 7b pre-routing checks

`fire_count: 0`. C5 reported `inapplicable` (prose-keyed, no sibling narrative at check time). **`inapplicable` is not "no fire"**, so Step 7c carries that load.

## 10. Step 9b: staged only

`hypothesis_space_ledger_pending` records:
- **Text refresh only on `arc131_sd091_recruitment_scale_invariance / H-operator-amplifies`.**
  - The leg's basis names V3-EXQ-1012a as its open adjudicating run. That run is now confirmed non-validating.
  - 1012c is the operator's successor validation, but it records no margin-dispersion statistic (the leg's DV).
  - So the default is: **do not** append 1012c to `resolving_runs`, and **do not** write `control_passed` / `non_degenerate` on the leg. 1012c's instrument gates are not a control on that DV, and `resolving_runs` feeds the derived counts.
  - Apply only the drafted basis and `distance_phrase` replacements. They record that the EMA error is heavy-tailed: consistent with the leg, but not discriminating it. State stays `alive`.
  - The first draft appended 1012c as a Mode B resolving run. That was withdrawn at Step 7c (F3).
  - No `growth_restriction` on that question. No new hypothesis, no fan-out, no Mode D signal.
- **`e3_fdominance_causal_discrimination` (MECH-439):** nothing adjudicated. 1012c is downstream-consistent with the already-confirmed H5-score-scale-uncontrolled.

## 11. Step 7c red-team

**Verdict: CONTESTED.** Run on **Fable 5.1**. This drafting subagent runs on Opus 5.5, so this was a **cross-model** pass. The findings file is in the session scratchpad and was not committed.

**The science stood.** The red-team independently recomputed:
- R = min/max jbar, reproduced in 8/8 cells.
- C1 4/4 in both regimes; instrument 0/0/0.
- R_ON < R_ORACLE in 8/8 cells, mean gap 0.1708.
- f top-J in 7/8 cells under ON vs 3/8 under ORACLE.
- Scales, fresh, latch and P1 counts byte-identical to 1012a in 8/8 cells.

It also confirmed that GFLAG-0297 was never user-ratified: there is no decision_log entry.

**Four findings moved the text. All were applied, and all were in the recommendations or assertions, not the arithmetic:**
- **F1 (recommendation, HIGH).** The if-ratified amend omitted the 571c autopsy carriers and the 571c item's own `target` field, while still marking that item resolved. *Applied:* carrier amend added, and the resolution is now explicitly against the ratified target.
- **F2 (assertion).** "f is stationary" is false: f's max r is 11.8-22.3x in 6/8 cells. *Applied:* struck. The mechanism is restated as consistent but not established, and f is noted as top under ORACLE in 3/8 cells.
- **F3 (recommendation).** Step 9b must not append 1012c as a resolving run on a leg whose DV it never measured. *Applied:* the default is now a text refresh only.
- **F4 (assertion).** `n_content_channels` is own-scale-relative and holds even under OFF at R_OFF 0.000, so it neither restores 571c's gate nor evidences MECH-439's precondition. *Applied:* rewritten to rest on R_ON alone.

**Hygiene applied:** H1-H8 (gap in sign vs beyond noise, max-r ranges by channel, table rounding, the hand-apply warning, the run pack lacking the direction note, the work-graph token, and the shape index exceeding the spike ceiling). H9 needed nothing.

**Attacks that failed:**
- The never-ratified claim.
- Routing `governance` (48 corpus precedents).
- The brake reasoning.
- The conditional resolution of the 1012a item.
- "Primary score absent from the within-E pick" (e3_selector L4229-4284).
- "Anything recommended already exists or already happened" (nothing does).

## 12. What is OWED before this can be applied

1. The **Step 8 interactive gate**, at the /governance walk. This draft's routing is a proposal. Ask the user:
   - (a) Ratify the eligibility-stage target?
   - (b) Release the 936-family / 654h-class refusal?
2. Nothing was marked reviewed. `review_tracker.json`, `claims.yaml`, `substrate_queue.json`, the queue and the registry are untouched.
3. This autopsy does not `spawn_task` its own follow-on. Governance chips the operator-ON conversion falsifier once (a) and (b) are decided.
