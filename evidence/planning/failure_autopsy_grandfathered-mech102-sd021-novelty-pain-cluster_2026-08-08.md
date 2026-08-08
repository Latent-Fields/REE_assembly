# Failure Autopsy: MECH-102/SD-010 + ARC-007/SD-004 + MECH-111 + SD-021/SD-032c, 21 nominal / 19 formal targets

**Generated:** 2026-08-08T19:22:21Z
**Scope:** cluster (4 threads, round-4 grandfathered-backlog sweep)
**Status:** confirmed (Step 8 interactive gate: user confirmed flagging the 397d finding to governance rather than accepting the standing dismissal, and flagging SD-032c/ARC-065 as newly unblocked)

## Dry-run gate

`check_dry_run_citations.py`: 0 dry cited on all 21. One **untagged smoke** found by content (`046`@151533Z: `dry_run` not set truthy but structurally a shakedown -- 2ep warmup/eval vs siblings' 600/50/30, all-zero metrics) -- excluded from evidentiary weight, degenerate `criteria_met=3/5`.

## Thread A -- SD-010/ARC-027/MECH-102 (4 runs: 2 duplicates, 2 genuinely new)

`056`x2 (both batch-form timestamps): byte-identical to the already-confirmed `failure_autopsy_grandfathered-goalseeding-cluster_2026-08-08.json` target (`competence_implementation_gap`, SD-010+ARC-027). No new work.

**`059`x2 (genuinely new)**: not covered anywhere (`failure_autopsy_V3-EXQ-059c-533_2026-07-26.json` covers only the *lettered successor* `059c`, not this predecessor). Source-verified (`ree-v3/experiments/v3_exq_059_sd010_mech102_advantage.py`): calls `agent.sense()` only -- zero `record_transition`/`act(`/`act_with_split_obs`/`act_with_log_prob`/`_e1_tick` calls -- feeding losses into `optimizer.step()` on `standard_params`, which therefore never receives a gradient; `z_world` is random-init for the whole run. Identical mechanism to the already-confirmed V3-EXQ-032-family finding and to this same claim's own successor 059c. The two nominally-identical seed-0 runs show wildly inconsistent results (`advantage_sig~0` vs `~0.005-0.008` with an inverted ordering) -- consistent with an untrained, effectively-random `z_world`.

**Recommended (059x2)**: `competence_implementation_gap`, `non_contributory`, `amend` (fold into the existing V3-EXQ-032-family substrate_queue entry, not a new one), `governance-note-only`.

## MECH-102 singleton -- `079` (pre-rename duplicate)

Git history (`ree-v3` commit `3da3e81`): "Renamed from v3_exq_079_mech102_depletion_ordering to v3_exq_080 to avoid an ID conflict." The renamed successor (`080`, 45 min later, identical signature) is already confirmed in `failure_autopsy_grandfathered-betagate-reafference-cluster_2026-08-08.json`. Mark `superseded_by` that rename, same disposition. **Biological-reference correction carried forward**: MECH-102 is "violence as terminal error-correction" (frustration-aggression theory, Berkowitz 1989; General Aggression Model, Anderson & Bushman 2002), not energy/depletion homeostasis.

## Thread B -- ARC-007/SD-004 hippocampal path-memory (3 runs + 397d) -- THE MOST CONSEQUENTIAL FINDING THIS ROUND

None of `046`@143303Z, `046`@162327Z, or `397d` had ever been cited in any prior `failure_autopsy_*.json` (the confirmed `046`@121655Z target names `046`@162327Z as its own `superseded_by` field, but that citation was never itself adjudicated -- a dropped thread).

**The persistent signal**: `hippo_quality_gap_intact` is strongly negative and essentially invariant across every independent measurement of this family from March through April, spanning two distinct metric formulations:

| Run | Date | Metric formulation | Value |
|---|---|---|---|
| 046@121655Z (confirmed superseded) | 03-23 | raw | -1.6403 (implied, same family) |
| 046@143303Z (this batch) | 03-23 | raw | -1.640282 |
| 046@162327Z (this batch) | 03-23 | raw | -1.639694 |
| 397 (superseded, already adjudicated) | 04-19 | raw | -1.640248 |
| 397c x2 (superseded) | 04-21 | raw | -1.638432 / -1.640019 |
| **397d (this batch)** | 04-23 | **matched-endpoint, confound-corrected** | **-1.639377** |

Governance's 2026-04-22 note reclassified 397/397c `non_contributory`: "the hippo_quality_gap internal probe metric is sign-inverted... probe broken, not the mechanism." **397d is a matched-endpoint redesign built specifically to test that dismissal** -- its docstring explains the actual mechanism as a destination-choice/path-choice confound (residue accumulates near goal-adjacent, hazard-proximate cells by env design; hippocampal trajectories correctly target those cells) and implements a matched-endpoint fix to remove it. **With the confound removed, 397d reproduces the identical value.** 397d itself has never been adjudicated (`evidence_direction: weakens`, no note, not superseded, not reclassified).

**Step 8 decision (user-confirmed, recommended option)**: flag this to governance as a needs-review item revising the 2026-04-22 closure, rather than accepting it as final. This finding also interacts with ARC-007's independent 2026-07-25 demotion (active->provisional, EXQ-114's 99.2% figure found to be a denominator artefact) -- that demotion was leg-scoped to the behavioural translation and never folded in this internal-probe thread.

**Recommended**: `standard`/`weakens` for 046x3 (excluding the untagged smoke @151533Z as non-evidentiary) and 397d, `narrow_supports_flag: true` on the load-bearing entries, `governance-note-only` with an explicit re-review request -- not a substrate build, this is a request to re-examine a prior metric-validity call.

## Thread C -- MECH-111 novelty-drive lineage (6 runs: 1 new, 5 backfill)

**073b (genuinely new)**: the only prior-round hit for this run_id (`20260402T021831Z_v3`) is confirmed **dedup/superseded** of *this* target -- sha1-identical, attributed to a known runner regex bug active ~03-27..03-30, fixed in `071f1fc`. This batch's `20260328T145319Z_v3` is the **original**, still unadjudicated. Same `weight=0.1` as 141/141b (near-zero entropy_gap/cell_gap); almost certainly the same measurement-invalidity defect 141b's governance note retrospectively diagnosed. Recommended: `competence_implementation_gap`, `non_contributory`, folded into 141b's disposition, `governance-note-only`.

**141, 141b, 141c x2, 141d (backfill/formalization only)**: already extensively adjudicated inline (manifest notes + claims.yaml MECH-111 evidence_quality_note, 2026-05-08 to 2026-05-25), never before formalized into an artifact. Converged campaign, not circling: each letter fixed a specific named instrumentation bug (weight scale 4-6 OOM too small -> nav_bias tie-breaking bug -> RNG desync) until 141d finally discriminated cleanly (action_divergence~0.56, real) and returned a genuine negative: action perturbation does NOT translate to expanded state-coverage (entropy_gap~0, cell_gap negative). Cross-linked 2026-05-10 to the ARC-065 cluster's BOTH-CHANNELS-NEEDED verdict (structured curiosity alone insufficient without an LC-NE tonic noise floor, MECH-313), corroborated by V3-EXQ-590a (2026-05-25, byte-identical coverage across a full novelty-weight sweep).

**Recommended**: `governance-note-only` for all 5, formalizing the existing narrative; 141d carries `narrow_supports_flag: true` and an `amend` note cross-linking to MECH-313.

## Thread D -- SD-021/SD-032c descending pain modulation (7 runs, backfill + one live finding)

Already fully adjudicated end-to-end via inline governance notes (claims.yaml SD-021/SD-032c notes, 2026-04-11 through 2026-04-22): `325` (commitment substrate gap, `n_committed_steps=0`) -> `325a`x3 (condition-dispatch bug -> V_s-monostrategy lock-in, gated on MECH-269) -> `325d` (SD-032c's own AIC test, same monostrategy read, independently reconfirmed 2026-05-25).

**Label-correction gap found**: `325a`@065916Z shows the identical `z_harm_s_ratio=1.0` signature as its sibling `325a`@212923Z one day later -- but the sibling **was** reclassified `non_contributory` 2026-04-19 while this one was left with an empty note and `evidence_direction: does_not_support`. Recommend applying the same reclassification for consistency.

**Live, actionable finding (Step 8 confirmed, recommended option)**: SD-032c's `pending_retest_after_substrate: ARC-065` condition has been resolved since **2026-06-17** (V3-EXQ-569i PASS, GAP-A top-k shortlist conversion closes the E3-commit-readout gap; ARC-065 claims.yaml status now `stable`). The 2026-05-25 claim-level entry (`failure_autopsy_V3-EXQ-455a_2026-05-25.json`) predates this by 3 weeks and was never revisited -- exactly the "stale conditional epistemic_category" trap Step 5 warns about. **SD-021's own separate `MECH-269` ("V_s landing") condition remains open** (candidate/v3_pending), so SD-021 itself stays blocked, but **SD-032c specifically now looks re-testable.** Flagged for `/queue-experiment` to pick up.

## Biological-reference triage

SD-021 carries 8 literature entries (lit_conf=0.852: Chen 2023, Crawford 2021, Tracey & Mantyh 2007, Basbaum & Fields 1984, Petrovic 2002, Hofbauer 2001, Hohmann 2005, Wager 2004) -- well grounded. MECH-111: `targeted_review_connectome_mech_111` present. MECH-102/SD-010: present, correctly re-scoped per the biological-reference correction above.

## Re-derive brake state (R1-R3)

**Zero `substrate_ceiling` hits for every claim in this batch** (MECH-111, SD-021, SD-032c, ARC-007, SD-010, MECH-102, SD-004): confirmed corpus already stamps this territory `competence_implementation_gap`/`measurement_test_design_defect`/`standard`/`precondition_unmet`, never `substrate_ceiling`. **The brake does not fire anywhere in this batch.**

## Recommended routing summary

- **Thread A**: 056x2 no action. 059x2 `governance-note-only`, `amend` V3-EXQ-032-family.
- **MECH-102 singleton**: `governance-note-only`, mark superseded.
- **Thread B**: `governance-note-only`, flag to governance for re-review (Step 8 confirmed) -- do NOT close as "probe broken" without re-examination.
- **Thread C**: 073b `governance-note-only`, fold into 141b. 141/141b/141c x2/141d `governance-note-only`, formalize; 141d also cross-links to MECH-313.
- **Thread D**: `governance-note-only` for the whole lineage, formalizing existing narrative; 325a@065916Z label correction; SD-032c flagged `/queue-experiment` as newly unblocked.

## Learning extracted

1. A metric redesign built specifically to test a "probe is broken" dismissal, that reproduces the identical value with the confound removed, is itself evidence the dismissal needs re-examination -- don't let a corrected-metric replication silently inherit its predecessor's disposition.
2. A claim's `pending_retest_after_substrate` condition needs re-checking against CURRENT claims.yaml state, not the state at the time it was written -- ARC-065 cleared 3+ weeks before anyone noticed SD-032c was still citing it as blocking.
3. Cross-thread reinforcement of the sense()-only driver defect class (059, extending the already-confirmed V3-EXQ-032-family) -- the fourth or fifth independent confirmation of this convention bug across this round's batches.
4. A duplicate-manifest confirmation (073b's regex-bug replay) points backward to an original run that itself was never formally adjudicated -- always trace `superseded_by`/`supersedes` fields to their target and confirm the target has coverage, not just the replay.
