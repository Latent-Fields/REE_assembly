# Failure Autopsy: V3-EXQ-871a (MECH-090 / ARC-071 commit-latch cross-tick persistence, post-fix validation)

**Generated:** 2026-08-03T09:51:33Z
**Scope:** single (2-seed instrumented diagnostic)
**Status:** confirmed (user-gated, all 3 questions confirmed)

## 0. Lineage

V3-EXQ-841 (2026-07-31) found that wherever `use_chunk_proposal_injection=True` is
live-tested, the official realised-commit-length readout pins at exactly 1 step in
100% of committing cells. Two live hypotheses were fanned out: H1 (wiring defect --
the latch does not survive across E3 ticks) vs H2 (readout artifact -- the true
internal state persists but the read path misreports it).

An ad hoc (non-EXQ) probe by a parallel session (`diagnostic_arc071_commit_latch_
h1h2_probe_2026-07-31.md`) resolved H1 CONFIRMED / H2 REFUTED using a monkeypatched
guaranteed-selectable chunk. The landed fix (ree-v3 main `278599a`) adds a fallback
to `agent.e3._persistent_committed_trajectory` (SD-084, the one handle NOT torn down
every tick) in the between-E3-tick fast path, gated behind `use_persistent_committed_
program_handle` (default False).

V3-EXQ-871 (script on disk as `v3_exq_855_...`) applied the flag to the WHOLE cell
(formation + probe), which perturbed formation itself via RNG-coupled environment
dynamics -- confirmed pure probe-construction defect (`failure_autopsy_V3-EXQ-871_
2026-08-02`, `measurement_test_design_defect`), not a substrate finding.

**V3-EXQ-871a (this run)** re-scopes the flag to the PROBE PHASE ONLY (flipped on
the live agent config after `_run_formation()`, before `_run_instrumented_probe()`),
so formation replays V3-EXQ-841's proven 2/2-chunk dynamics unperturbed. This is the
first run that actually tests the open question: **does the landed fix restore
meaningful multi-step commit-latch persistence under REAL organic chunk formation,
or does "gap (b)" -- E3 unconditionally re-committing a brand-new trajectory object
every E3 tick, regardless of an existing unexpired commitment -- still dominate?**

## 1. Facts (dry-run check + manifest reconstruction)

**Dry-run gate:** `scripts/check_dry_run_citations.py` -- both `v3_exq_871a_...` and
its cited lineage members (`671a`, `671b` checked incidentally) are clean (not dry).
`dry_run: false` on the manifest; `ANCHOR_REACHABILITY_EXEMPT` confirms the
readiness gate is reachable by construction at the real (non-dry-run) schedule.

**Recording completeness:** `validate_recording.py` -- OK, 0 always-core gaps.
`substrate_hash`, `substrate_commit` (`b49d6ab5...`/dirty=false — actually
`46b986ba...` for this run; see manifest), `config`, `seeds` all present.

**Design:** `A_HIER_S2`, `chunk_max_size=2`, seeds `[101, 505]` (the two seeds where
V3-EXQ-841's effect reproduced most cleanly, per its own `fanout_recommendation.
suggested_probes`). Formation: 120 episodes x 72 steps (identical to `arc071_
chunking`'s proven schedule; V3-EXQ-810a: 8/8 seeds formed chunks; V3-EXQ-841: 32/32
chunking cells committed >=1 chunk on this exact schedule). Probe: 10 episodes, no
devaluation, per-tick instrumentation via `StepHooks`. Assertion in `_run_cell`
verifies the flag is genuinely False entering formation (fails loudly if not) --
the exact assumption V3-EXQ-871 violated.

**Preconditions (P0):** `arc071_chunk_commitments_observed_supra_floor` -- worst-seed
`n_persistent_present_ticks` = 147 (seed 505) vs floor 10. **MET.** 147 total genuine
ARC-071-chunk-sourced commitments observed across the two seeds -- ample power.

**Criteria:**
- C1 `sufficient_commitments_observed` (load-bearing): **PASS** (147 >> 10).
- C2 `discrimination_reached` (load-bearing): **FAIL** at the aggregate level --
  the per-seed verdicts landed on OPPOSITE sides of the definitive thresholds:

| Seed | `official_readout_mean_realised_length` | vs floor(3.0)/ceil(1.5) | `cell_verdict` | `n_probe_ticks` | `n_e3_ticks` | `e3_tick_rate` |
|---|---|---|---|---|---|---|
| 101 | 6.372 | >= 3.0 floor | `persistence_restored_post_fix` | 720 | 103 | 0.1431 |
| 505 | 1.427 | <= 1.5 ceil | `persistence_still_broken_post_fix` | 147 | 93 | 0.6327 |

Self-routed label: `mixed_across_seeds` (the script's own `run_experiment()` treats
this as a genuine discrimination-not-reached outcome and assigns `direction_mech090
= "unknown"` -- by design, this label does not resolve a direction; that's exactly
what this autopsy is for).

## 2. The key finding: the "bistability" is a tick-rate confound, not a real seed effect

Both `official_readout_mean_realised_length` and the independent identity-based
`mean_true_dwell_ticks` are (to full precision) **identical** within each seed --
confirming the between-tick fast path's official readout and raw object-identity
tracking agree perfectly post-fix (fix (a) genuinely works: the readout is no
longer misreporting a persisting handle as resetting).

But both numbers are also **exactly** reproduced by a trivial formula:

```
n_genuine_commits_identity_based = n_e3_ticks + n_episodes_probe   (EXACT, not approximate)
  seed 101: 113 = 103 + 10
  seed 505: 103 =  93 + 10

mean_true_dwell_ticks = n_persistent_present_ticks / n_genuine_commits
  seed 101: 720 / 113 = 6.3717   (matches manifest exactly)
  seed 505: 147 / 103 = 1.4272   (matches manifest exactly)
```

The `+10` offset is exactly `N_EPISODES_PROBE` in both seeds -- consistent with one
extra identity-reset per episode (at `agent.reset()`), on top of exactly one fresh
commit per E3 tick. This is an **exact, deterministic** relationship, not a
statistical tendency: **every single E3 tick produces a brand-new committed-
trajectory object, with zero exceptions, in both seeds.** There is no seed in which
the persistent handle sometimes survives an E3 tick and sometimes doesn't -- it
NEVER survives one, in either seed.

What differs between seeds is `e3_tick_rate` alone (0.143 vs 0.633, a ~4.4x
difference -- itself likely downstream of per-seed differences in precision/
running-variance dynamics or episode length, seed 505's probe ran only 147 ticks
across 10 episodes vs seed 101's full 720, i.e. episodes ended far earlier for
seed 505). Because dwell length is definitionally `n_probe_ticks / (n_e3_ticks +
n_episodes)`, and the numerator/denominator both track episode/tick structure
that is orthogonal to whether the latch itself "holds," **the readout's floor
(3.0) / ceiling (1.5) thresholds were calibrated without controlling for this
confound** -- a seed that happens to have a low `e3_tick_rate` clears the floor
not because persistence holds in the sense MECH-090 asserts (resisting premature
re-deliberation) but purely because E3 ticks less often for that seed's
trajectory. Seed 101's "restored" reading is exactly this: an artifact of a lower
tick rate, not a qualitatively different commit-latch mechanism.

**Conclusion (user-confirmed):** the two per-seed verdicts are not evidence of a
real seed-dependent effect. Both seeds show the identical underlying mechanism --
gap (b) fires on every E3 tick, unconditionally -- and the surface "mixed" label is
an artifact of an uncontrolled nuisance variable (tick rate) in the verdict
statistic, not genuine discrimination failure.

## 3. Claim-layer mapping

**MECH-090** ("BG-level beta oscillations gate E3-to-action-selection propagation,
**not E3 internal updating**") -- status `active`, extensively validated elsewhere:
EXQ-049e PASS (5/5, two-condition committed/uncommitted design), EXQ-062b PASS
(surprise-gated selective interrupt), EXQ-049a PASS (bistable concordance). The
core mechanism (gate propagation, not internal computation) is well-supported. This
run does not re-test that core claim -- it tests a narrower, more recent extension:
does the gate's output (the committed object) survive across E3's own internal
re-evaluation cycles, specifically when the committed content is an ARC-071-
injected chunk? Already carries 7 confirmed `substrate_ceiling` autopsies from an
unrelated V2-era sub-question (delayed-reward persistence / decommit-hold
behavioural, SD-034 cluster) -- **not the same question as this run**; the
re-derive brake does not apply here since this run is not itself recommending
`substrate_ceiling`.

**ARC-071** ("policy_composition_via_repeated_grounding") -- `candidate/v3_pending`,
no `substrate_ceiling` hits. Formation/transfer already has its own evidence
(V3-EXQ-810a/810b, `supports/standard`). This run exercises ARC-071's chunk-
injection pathway only as the VEHICLE that exposes the MECH-090 cross-tick
question -- exactly the same precedent V3-EXQ-841 itself used to exclude MECH-323
(chunk *formation* is a precondition, not itself in question). ARC-071's own
formation/transfer claim is untouched by this run.

**Granularity-debt check** (`scripts/granularity_debt_cluster.py`): MECH-090's
7-target cluster has NO `weakened` alignment (`intact`=7, `strengthened`=1,
`other`=3, `unclear`=1 -- the `other`/`unclear` entries concern the unrelated
delayed-reward-persistence / decommit-hold sub-questions, read individually, none
weakened). ARC-071's 5-target cluster likewise has no `weakened` (2 `strengthened`,
2 `unclear`, 1 `intact`). **Trigger does NOT fire for either claim** -- this is
implementation debt on a specific interaction, not granularity debt on either
claim's definition.

## 4. Biological-reference triage

MECH-090's own functional restatement predicts exactly the invariant gap (b)
violates: *"E3 continues updating its internal model but propagation of updated
model state to action selection is gated."* I.e., ongoing internal deliberation
(E3 ticking) should NOT overwrite or recreate the committed output object -- the
whole point of the gate is to decouple internal computation from the externally
visible commitment. The literature anchoring this (Cisek & Kalaska 2010 affordance-
competition persistence; Hanes & Schall 1996 accumulator-to-threshold, where the
accumulator's *decision* output is a stable, persisting state once threshold is
crossed, distinct from ongoing accumulator dynamics) supports the same separation:
a winner-take-all selection, once made, is read out as a stable committed plan by
downstream structures while upstream competition continues. Gap (b) -- E3
unconditionally minting a fresh trajectory object at every internal tick,
regardless of an existing unexpired commitment -- is a violation of MECH-090's own
stated architecture within this one interaction (the between-AT-tick selection
site), even though the surrounding architecture (the between-tick fast path, now
fixed) correctly implements the same separation. This is therefore read as an
**implementation gap specific to the at-tick selection site**, not evidence against
MECH-090's core mechanism (which remains well-supported by its other PASSes) and
not a biology-vs-substrate divergence requiring a `/lit-pull`.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (MECH-090 core); not exercised (ARC-071) | MECH-090's gate-propagation principle is violated only at this one wiring site, not challenged in general; ARC-071 exercised as precondition/vehicle only |
| Biological reference | clear | Cisek & Kalaska 2010, Hanes & Schall 1996; MECH-090's own stated principle predicts the invariant this run finds violated |
| Developmental / dependency prerequisites | present | ARC-071 formation (MECH-323/324) already validated (810a/810b); SD-084 persistent handle already exists and correctly used by the fixed between-tick path |
| Implementation completeness | partial | fix (a) (between-tick fast path) confirmed working; the AT-E3-tick selection site (gap (b)) still unconditionally recreates the trajectory object every tick, in 100% of ticks, both seeds |
| Environment adequacy | adequate | 147 genuine chunk-sourced commitments observed, well above floor; formation schedule proven (810a/841) |
| Measurement adequacy | **misleading** | `official_readout_mean_realised_length` is confounded by `e3_tick_rate`, an uncontrolled nuisance variable that differs ~4.4x between seeds; the floor/ceiling thresholds do not account for it, producing an apparent bistability that is fully explained by the confound (exact arithmetic, Section 2) |
| Integration adequacy | partially coupled but unstable | ARC-071 chunks correctly enter the persistent handle and correctly survive `_committed_trajectory` teardown (fix a); the AT-tick commit path does not yet consult the persistent handle before creating a new one |
| Scale / capacity | adequate | 2 seeds sufficed to expose the deterministic (not probabilistic) nature of gap (b) once the tick-rate confound is accounted for; a future readout redesign should still use more seeds to characterise `e3_tick_rate` variance itself |

## 6. Learning extracted

1. **Gap (b) is confirmed, universally and deterministically** (not merely
   "still dominant in some seeds"): `n_genuine_commits == n_e3_ticks +
   n_episodes` exactly, in both seeds -- every E3 tick recreates the committed
   trajectory object, no exceptions.
2. **The apparent seed-dependent bistability is a measurement-design artifact**:
   the verdict statistic (`official_readout_mean_realised_length`) is
   definitionally `n_probe_ticks / (n_e3_ticks + n_episodes)`, so it tracks
   `e3_tick_rate` (itself driven by unrelated per-seed precision/episode-length
   dynamics) rather than commit-latch behaviour. The fixed floor/ceiling
   thresholds (3.0 / 1.5) were not validated against this confound.
3. **Fix (a) (the between-tick fast path fallback to the persistent handle) is
   confirmed working correctly** in both seeds -- the official readout and the
   independent identity-based reading agree exactly, meaning the readout itself
   is no longer misreporting. What remains broken is upstream of the readout:
   the AT-tick commit-creation logic itself.
4. **A concrete, named fix exists**: extend the same persistent-handle-aware
   check used in the between-tick fast path (agent.py:5965-5987 / 6009-6012 per
   the driver's own static-source citations) to the AT-E3-tick selection site
   (wherever `agent.e3.select(...)` / `post_action_update` decides to create a
   new committed trajectory), so that an existing unexpired
   `_persistent_committed_trajectory` sourced from an ARC-071 chunk is
   preferentially continued rather than unconditionally replaced.
5. **A future validation of this fix should not reuse the current DV.** Once
   gap (b) is fixed, the correct discriminating statistic is something like
   `n_genuine_commits / n_e3_ticks` (should drop well below 1.0 post-fix, since
   most E3 ticks should reaffirm/extend the same chunk rather than recreate it)
   or a tick-rate-normalised persistence measure -- not raw
   `official_readout_mean_realised_length`, which will keep tracking
   `e3_tick_rate` regardless of whether gap (b) is fixed.

## 7. Repair pathway and classification

**Work-graph debt classification:** `complicated (buildable)` -- the fix is a
named, already-diagnosed code change (extend an existing check to a second call
site) with no open scientific question. This is NOT a `complex (probe-gated)`
spike; the static-source citations in the driver's own docstring (agent.py line
numbers, e3_selector.py torn-down-every-tick behaviour) already pinpoint exactly
where and what to change.

**Routing: `/implement-substrate`** (user-confirmed). `recommended_substrate_
queue_entry`:
- `action`: `create` (no existing `substrate_queue.json` entry covers this --
  confirmed via grep; the 3 MECH-090-tagged entries there, sd_id 89/90/99, are
  BetaGate readiness-conjunction / curriculum-decomposition / closure-wiring
  work, unrelated to this AT-tick recommit defect).
- `sd_id_suggested`: `mech090-arc071-attick-persistent-handle-fix`
- `title`: "E3 AT-tick commit selection should preserve an existing unexpired
  persistent committed trajectory (ARC-071 chunk-sourced) instead of
  unconditionally recreating it every E3 tick"
- `implementation_hint`: "Mirror the between-tick fast path's fallback to
  `agent.e3._persistent_committed_trajectory` (landed ree-v3 `278599a`, flag
  `use_persistent_committed_program_handle`) at the AT-E3-tick selection site
  itself (`agent.e3.select(...)` / the commit-creation branch in `select_action`
  / `post_action_update`'s unconditional `_committed_trajectory = None` teardown
  path) -- if an unexpired `_persistent_committed_trajectory` sourced from an
  ARC-071 chunk already exists and the chunk has not been fully executed/
  exhausted, continue it rather than creating a fresh trajectory object.
  Validate with a redesigned DV: `n_genuine_commits / n_e3_ticks` (or equivalent
  tick-rate-normalised statistic), not raw mean segment length."
- `unblocks_claims`: `["MECH-090", "ARC-071"]`
- `depends_on_unresolved`: `[]` (SD-084 persistent handle and fix (a) already
  land; this is the one remaining wiring gap)
- `priority_suggested`: 2 (medium -- confirmed implementation gap on a specific,
  well-diagnosed interaction; blocks a clean future validation of ARC-071 chunk
  commit-latch persistence, but neither claim is at a ceiling and no downstream
  work is currently stalled waiting on it)
- `failure_record_entry`: `{"run_id": "v3_exq_871a_mech090_commit_latch_persistence_diagnostic_20260802T174141Z_v3", "experiment_type": "v3_exq_871a_mech090_commit_latch_persistence_diagnostic", "metric": "n_genuine_commits_identity_based == n_e3_ticks + n_episodes_probe (exact, both seeds) -- every E3 tick recreates the committed trajectory object", "target": "post-fix, n_genuine_commits / n_e3_ticks should drop well below 1.0 for an ARC-071-chunk-sourced commitment not yet exhausted"}`

**Draft `evidence_quality_note` (for governance to apply, verbatim or near-verbatim):**

> [2026-08-03 governance, V3-EXQ-871a, confirmed failure_autopsy_V3-EXQ-871a_2026-08-03, MECH-090/ARC-071 commit-latch AT-tick persistence]: post-fix validation of ree-v3 278599a (between-tick fast path fallback to the SD-084 persistent handle) under REAL organic chunk formation (V3-EXQ-871's whole-cell-flag defect corrected by scoping the flag to the probe phase only). Self-routed `mixed_across_seeds` (seed 101 mean-length 6.37 "restored"; seed 505 1.43 "still broken") is resolved by exact arithmetic as a tick-rate confound, not real seed-dependent discrimination: `n_genuine_commits_identity_based == n_e3_ticks + n_episodes_probe` exactly in BOTH seeds (113=103+10; 103=93+10) -- every single E3 tick recreates the committed-trajectory object, with zero exceptions, in both seeds. The readout's floor/ceiling thresholds (3.0/1.5) were not validated against `e3_tick_rate` (which differs ~4.4x between seeds for reasons unrelated to the latch), so a low-tick-rate seed clears the floor purely from a longer natural gap between E3 re-evaluations, not from genuine persistence. Fix (a) (between-tick fast path) is confirmed CORRECTLY implemented (official readout and independent identity-based reading agree exactly in both seeds); the still-open "gap (b)" (E3 unconditionally recreating a fresh trajectory object at the AT-tick selection site, regardless of an existing unexpired commitment) is CONFIRMED as the dominant remaining defect, universally, not merely in some seeds. Read as `non_contributory/competence_implementation_gap` for MECH-090 (narrow to this AT-tick wiring interaction; the core gate-propagation mechanism remains well-supported by EXQ-049e/062b/049a) -- no change to MECH-090 status/confidence. ARC-071 unaffected (exercised only as the chunk-injection vehicle, per the same precedent V3-EXQ-841 used to exclude MECH-323; no evidence change, still candidate/v3_pending). Routed `/implement-substrate`: create sd_id `mech090-arc071-attick-persistent-handle-fix` (extend the between-tick fix to the AT-tick selection site). A future validation of the fix should use a tick-rate-normalised DV (e.g. `n_genuine_commits/n_e3_ticks`), not raw mean segment length, which will keep tracking tick rate regardless of whether gap (b) is fixed. pending_retest_after_substrate=true. narrow_supports_flag=false.

**User-confirmed routing (all 3 gate questions):** (1) bistability resolved as a
consistent gap-(b) confirmation via the tick-rate-confound reading; (2) routed
`/implement-substrate` now (named build, not an open question); (3) MECH-090
`non_contributory/competence_implementation_gap`, ARC-071 unaffected/no evidence
change.

## 8. Hypothesis-space ledger (Step 9b)

Pre-existing question `arc071-commit-latch-postfix-persistence` (registered from
V3-EXQ-841's `fanout_recommendation`) carried two live hypotheses:
`H-postfix-persistence-restored` (H1) and `H-postfix-persistence-still-broken`
(H2). This run is their adjudicating run.

- **H1 (fix (a) restores persistence) -> `eliminated`.** Seed 101's apparent
  "restoration" is fully explained by the tick-rate confound (Section 2's exact
  arithmetic), not genuine persistence in the sense the hypothesis asserts. Bar:
  `met_elimination_bar=true`, `control_passed=true` (P0 readiness gate cleared,
  147 >> 10), `non_degenerate=true` (`criteria_non_degenerate.C1/C2=true` in the
  manifest).
- **H2 (fix (a) alone is insufficient, gap (b) dominates) -> `confirmed`.** Both
  seeds show gap (b) firing on literally every E3 tick (exact formula, Section
  2). `control_passed=true`, `non_degenerate=true`.

Both resolutions use `resolving_runs: ["V3-EXQ-871a"]`, `resolved_utc` = this
run's `timestamp_utc` (2026-08-02T17:41:41Z), `pre_registered_utc` (already <=
that, registered at V3-EXQ-841's fanout on 2026-07-31). Ran
`build_hypothesis_space.py` + `check_hypothesis_space_integrity.py` after the
append: 0 new flags on this question.
