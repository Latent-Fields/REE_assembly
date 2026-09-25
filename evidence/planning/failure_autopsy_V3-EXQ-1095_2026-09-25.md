# Failure autopsy -- V3-EXQ-1095, MECH-439 operator-ON conversion falsifier (evidence FAIL, flagged degenerate)

- **Generated:** 2026-09-25T05:20:03Z
- **Status:** confirmed (Step 8 gate, 2026-09-25T05:42:23Z)
- **Scope:** single
- **Run:** `v3_exq_1095_mech439_operator_on_conversion_falsifier_20260925T040330Z_v3` (ree-worker-3, 30170 s)
- **Claim:** MECH-439
- **Purpose:** evidence
- **Self-route:** `matched_noise_control_unmeetable`
- **Manifest direction:** `non_contributory`
- **Flag:** `non_degenerate: false`, with every arm red on `candidate_first_action_classes`

**Bottom line.** The recommendation is **non_contributory / standard**. That is robust to each measurement defect at the pre-registered 3-of-4 bar. The operator worked at the eligibility stage. The run cannot attribute a committed-diversity lift to it: C1b is 2/4. The run also vacated on two test-design gates:

- **MECH-439's registered matched-noise control does not verifiably lift.** This is its fourth failed construction in the lineage, after 689c, 689i and 700d; 700d was magnitude-matched at 1.0x.
- **The pool-width readiness gate aggregates by the worst seed.** It sits beside verdicts that aggregate >=3/4 seeds.

On the pre-registered grid, the ungated result sits in the **H3 cell** (summary-source-not-operator).

The routing recommendation is **governance**: restate the control set, folding into GFLAG-0471 or sitting alongside GFLAG-0480. There is no re-queue, no calibration sweep and no build.

## 1. Facts

### 1a. Dry-run gate

- `check_dry_run_citations.py` covered the run_id, V3-EXQ-1095 and `--family v3_exq_1095`: 0 dry, 1 real.
- The comparison run V3-EXQ-689i (`v3_exq_689i_..._20260722T162850Z_v3`) is also real.

### 1b. Why it exists

Governance 2026-09-24 released the 936-family refusal, scoped to operator-ON falsifiers in this regime. This run is the named follow-on. Its lineage:

- confirmed failure_autopsy_V3-EXQ-1012c_2026-09-24 sec 7b
- chip-20260924-mech439-operator-on-falsifier
- GFLAG-0471 (open, unratified restatement of the confirming branch)
- GFLAG-0480 (the starved regime is out)

### 1c. Design

The regime is residue-FED only, 4 arms x 4 seeds (42/43/45/46), with a fixed N=200 committed samples per cell and the DV on Miller-Madow committed-class entropy.

| Arm | Summary source | Operator |
|---|---|---|
| PROPOSER_CTRL | proposer | OFF |
| MATCHED_NOISE | proposer | OFF, plus Factor B gap-scaled commit (alpha 1.0) |
| OFF | e2wf | OFF |
| ON | e2wf | ON |

Verdict chain, in order:

1. instrument
2. control-distinct
3. **C_NOISE_LIFTS** (gating)
4. readiness
5. C2 eligibility
6. C1 (ON above both controls)
7. C1b (ON above OFF)

PASS needs both C1 and C1b. **The design cannot emit weakens.** The operator reduces F's variance share, so MECH-439's falsifying antecedent has no instance.

### 1d. Observed

| Seed | pool FA classes (worst arm) | R_ON | R_OFF | H_ON | H_OFF | H_PROP | H_NOISE | C1 margin | C1b ON-OFF | noise lifts |
|---|---|---|---|---|---|---|---|---|---|---|
| 42 | 4.14 | 0.653 | 0.000 | 1.446 | 1.200 | 1.028 | 1.292 | +0.155 | +0.246 | yes |
| 43 | **2.00** | 0.697 | 0.011 | 0.676 | 0.676 | 0.349 | 0.359 | +0.316 | **0.000** | yes |
| 45 | 2.945 (PROP) | 0.291 | 0.000 | 0.893 | 0.525 | 0.794 | 0.659 | +0.099 | +0.368 | no |
| 46 | 3.23 | 0.814 | 0.000 | 1.021 | 1.074 | 0.918 | 0.905 | +0.103 | -0.053 | no |

Criterion results, by the counts:

| Criterion | Result | Gated green? |
|---|---|---|
| Instrument clean | 0 / 0 / 0; worst I2 0.0000 | -- |
| Control-distinct | 0 identical pairs | -- |
| C2 | 4/4 at R>=0.25 | not gated green |
| C1 | 4/4 | not gated green |
| C1b | 2/4 | -- |
| Noise lifts | 2/4 (bar 3) | -- |

- **Readiness is RED in all four arms on `candidate_first_action_classes`** (worst seed, threshold 3.0). The offending cell is seed 43 in every arm, and PROPOSER_CTRL seed 45 is also below at 2.945.
- **Factor B `gap_scaled_commit_active_frac`** is 0.987 / 0.937 / 1.000 / 0.909 in the matched-noise arm and 0 elsewhere.
- **`committed_frac`** is 1.0 in 16/16 cells.
- **At seed 43**, ON and OFF committed counts are identical: {1:80, 2:120}. The binary pool bounds H at ln 2 but does not force a tie: PROPOSER split 178/22 in the same pool. With the operator engaged (R_ON 0.70), this is a genuine commit-stage null.

### 1e. Recording provenance

- `validate_recording.py`: complete, with no always-core gaps. Its advisory about a missing top-level `combination_rule` is moot, since the rule is present under `interpretation.combination_rule`.
- **Recording gap:** the driver never reads `gap_scaled_commit_temperature_eff` / `gap_norm` / `conflict_gap_norm`, which the selector emits per tick (e3_selector.py:2320-2334, 4183-4194).
- All 16 cells share `substrate_hash` 946f8c56...
- `substrate_commit` 5da79b9c names the post-drift disk state (`commit_describes_recorded_hash: false`). That is benign, and `substrate_hash` is authoritative.

### 1f. Expected vs observed

The driver's own red-team (F8) predicted this: "a null here is the expected-value outcome". On the closest prior, 689i, no seed satisfies C1, C1b and noise-lift together.

### 1g. The pre-registered H1-H4 grid (queue entry, ree-v3 f8288e1)

| Hypothesis | Signature | Observed (ungated) |
|---|---|---|
| H1 monopoly-at-eligibility | C1, C1b, C2 all true | partial: C1b only 2/4 |
| H2 ceiling-is-downstream | C1 false, C2 true | **did NOT occur** (C1 4/4) |
| **H3 summary-source-not-operator** | C1 true, C1b false | **observed**; ARM_OFF also clears both controls on 2/4 |
| H4 pool-geometry | proposer not below ON/OFF; pool tracks entropy across arms | proposer below ON 4/4, so fails; pool is arm-invariant but does track entropy across seeds |

The mapping is **gated, not adjudicated**: the run vacated before C1 or C1b could carry a direction.

## 2. Claim-layer mapping

MECH-439 today:

- `candidate` / `standard`
- `ceiling_decision: exhausted`
- `pending_retest_after_substrate: true`
- `diagnostic_evidence_adjudicated: true`
- `live_status.evidence.from` = failure_autopsy_V3-EXQ-1012c_2026-09-24

**Could the claim express itself?** Only on its supports side, and only under GFLAG-0471's proposed restatement, which the user has not ratified. The run could support or route. It could never weaken. It did neither.

`non_contributory` is correct. There is no status, category or flag move. Only the note is appended and the citation stamp moved.

## 3. Biological-reference triage

The closest mechanism is divisive normalisation before value integration (Carandini & Heeger 2012; Louie, Khaw & Glimcher 2013), followed by BG commitment. It is faithful in kind, the literature is present, and **no /lit-pull is owed**.

The 1012c divergence carries over unchanged: an EMA normaliser vs normalisation by the concurrent pool. R_ON < R_ORACLE in 3/4 cells here. It is not load-bearing.

The failure resembles two biological missing-dependency signatures, both named in the four-layer table:

- an upstream candidate generator offering only a binary choice (seed 43)
- a downstream commitment stage that does not read the normalised value

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | support-or-route design against an unratified restatement |
| Biological reference | partial | divisive normalisation plus commitment; lit present |
| Prerequisites | partial | the operator was validated and re-measured in situ, but `f_dominance_conversion_ceiling` items [0]/[1] are untouched. **SD-056's open 571b item** (clamp-armed E3 score-range collapse) applies in 16/16 cells and was not in the driver's Step 2.5c list. It is arm-uniform and its magnitude was not recorded. |
| Implementation | complete | operator engaged 4/4 ON cells; instrument clean; Factor B live in the noise arm |
| Environment | partial | seed 43 has a binary candidate pool in every arm (bounds H at ln 2); seed 45 is at threshold (PROPOSER_CTRL/45 below it) |
| Measurement | under-instrumented (control layer) | (a) the matched-noise control fires but does not lift (2/4); it is the fourth failed construction (689c, 689i, 700d at 1.0x, 1095); (b) the worst-seed readiness gate mismatches the >=3/4 verdicts; (c) T_eff / gap_norm are not recorded |
| Integration | partially coupled | live at eligibility 4/4; operator-attributable committed lift on 2/4; seed 43 is a genuine commit-stage null (operator engaged, split byte-identical to OFF) |
| Scale | likely insufficient | 4 seeds x 200 samples against a >=3/4 strict bar for a +0.14-nat mean C1b effect |

**Failure location (GOV-FAILLOC-1):**

- MECHANISM: established
- MEASURES: not established
- ENVIRONMENT: partial
- **Net: MIXED (MEASURES + ENVIRONMENT), not chargeable to REE.**

**Counterfactual: the verdict is robust to both measurement defects at the pre-registered 3-of-4 bar.**

- *Per-seed gating, dropping seed 43 only:* C1b is 2/3 and noise-lift 1/3. Noise-lift drops to 1/2 if PROPOSER_CTRL/45 is also excluded. Both fail.
- *No noise gate:* C1 passes 4/4 but C1b fails 2/4, so the run lands on `conversion_not_attributable_to_operator`, which is also non_contributory.

Only a triple-stacked relaxation reaches supports: per-seed exclusion, plus no noise gate, plus MECH-439's registered >=2/3 fraction in place of 3-of-4. The pre-registered thresholds bind.

## 5. The confound the red-team's C1b caught

C1, ON above both controls on 4/4 seeds, looks like conversion. It is not operator-specific:

- ARM_OFF (e2wf source, operator OFF) also exceeds both controls on 2/4 seeds.
- Mean H_OFF is 0.869, above both control means (0.772 / 0.804).

So a good share of the lift over the controls comes from the candidate-summary source, which is ARC-065 GAP-A's own conversion mechanism. The C1b fix was load-bearing. Without it, this run would have read as a clean MECH-439 support.

## 6. Cluster

This is not a cluster autopsy. The noise-control finding is **cross-run** (689i + 1095) and is stated as a measurement learning, not as a shared failure shape.

## 7. Learning and routing

### Learning

1. **The registered matched-noise control is not usable on this substrate. This is the fourth instance, not a new finding.** MECH-439's "collapsed-proposer plus magnitude-matched-noise control, both verified lifting" has failed in four constructions:

   | Run | Construction | Result |
   |---|---|---|
   | 689c | Factor B on the e2wf source | T_eff ~2.3-2.4; lifts <= +0.025 or negative. Substrate ladder rung 1: "REFUTED ... DO NOT re-propose" |
   | 689i | Factor B on the proposer | 1/4, including a single-class-collapse cell |
   | 700d | field noise magnitude-matched at 1.0x | 0/2, destructive; already in MECH-439's notes |
   | 1095 | Factor B on the proposer | 2/4 |

   One construction was explicitly magnitude-calibrated. So "verified lifting" is plausibly unmeetable **by thesis**: injected diversity failing to convert is the F-monopoly / score-scale reading itself. It is not a calibration fault. This is the same family as GFLAG-0480.
2. **Test-design template.** The readiness gate aggregates worst-seed-per-arm; the verdicts aggregate >=3/4. That is the regression shape the driver already fixed for C_CONTROL_DISTINCT (pass-2 F3), left in place for this gate.
3. **Pre-registered grid: H3.** The ungated result is the queue entry's H3 cell (summary-source-not-operator).
   - H2 (ceiling-is-downstream, C1 false) did not occur.
   - The only seed-level observation that speaks to H2 is seed 43's genuine commit-stage null.
   - An earlier draft reading ("attribution does not track R_ON, so the bottleneck is downstream") is **withdrawn**. It rested on 3 free points against a pre-registered grid that places the run elsewhere (red-team F2).
4. **Scope bound found by Step 7b.** SD-056's open 571b item says that with the clamp armed, E3 score range collapses ~800x and 92-97% of rollouts pin. It applies in 16/16 cells.
   - It is arm-uniform and does not threaten the verdict.
   - Magnitude unrecorded.
5. **Recording gaps:**
   - committed score range and max||z_w||/ceiling (SD-056)
   - `gap_scaled_commit_temperature_eff` / `gap_norm` distributions and per-tick eligible-set class composition (red-team F3, pass-1 F3)

   Without these, a magnitude shortfall cannot be told apart from a near-uniform softmax over a class-poor E.
6. **Environment.** Seed 43's binary pool appears in every arm. That is read-across to e3_fdominance H3-upstream-insufficiency (not adjudicated).

### Routing

**Recommended routing: `governance`.** The work-graph class is **complex (probe-gated) / mystery (known data)**. Four constructions already show the control does not lift, so the move is to reframe it, not to gather more.

**At the walk:**

- Record non_contributory / standard on MECH-439 with the drafted note, and stamp this artifact.
- **The user decides a restatement of MECH-439's control set.** It can fold into GFLAG-0471 or be raised as its own evidence_discrepancy beside GFLAG-0480.
  - **Recommended: option (ii).** Stop gating the SUPPORTS branch on "verified lifting" and keep that requirement only for interpreting a NULL. It is a sensitivity check. C1's proposer half already certifies the bar is real, and four constructions, one magnitude-matched, show that noise does not lift on this substrate, which is what the claim predicts.
  - **Option (i), a calibration sweep, is not recommended.** The calibrated measurements already exist (689c T_eff, 700d at 1.0x).

**Follow-on, named and not spawned:**

- **Recording only, not an experiment:** any future driver in this lineage records T_eff / gap_norm, E class composition, committed score range and clamp-pinned fraction per cell.
- **The reserved final-commit-stage replay** (1012c sec 7b) stays reserved and remains a user release decision. **This run gives it no new motivation** beyond seed 43's single commit-stage null. The only prior attempt, `chip-20260914-mech439-e3-final-commit-shadow-replay`, is withdrawn.
- **A driver-template fix:** per-seed exclusion for readiness preconditions in the mech439 baseline lineage.

**Explicitly not recommended:**

- a lettered 1095a with the same control
- a Factor B alpha sweep / noise calibration diagnostic (known data)
- reading C1 4/4 as MECH-439 support (H3: not operator-attributable)
- any weakens reading

**Substrate queue.** `action: none`.

### Re-derive brake

- The R1-R3 recipe, re-run 2026-09-25, gives MECH-439 **15 hits** (threshold 2). That is unchanged.
- **This target adds 0.** Its category is `standard` with a test-design marker, and it owes no build.
- The lineage brake stays fired. Governance's 2026-09-24 release was scoped to exactly this operator-ON shape, and that shape has now run.

### Granularity-debt recurrence trigger: does not fire

`granularity_debt_cluster.py MECH-439` finds 22 tagging targets across 20 files. None reads `weakened` (the alignments are intact, unclear or other), so this is measurement/substrate debt.

### pending_retest_after_substrate

It stays true. MECH-439 has no supports entries, so there is no narrow-supports risk.

## 8. Draft evidence_quality_note (MECH-439)

See the JSON `recommended_evidence_quality_note`.

## 9. Step 7b pre-routing checks

`fire_count: 1`. That is one C2 fire naming two entries.

- **C2 on SD-056: ACTED ON.** It is added as an arm-uniform scope bound and a recording gap. There is no failure_record entry, since there is no score-range measurement to add.
- **C2 on q092-behavioural-discriminability-umpire-harness: DISMISSED.** It is registration-only, a behavioural-trajectory harness, and does not bear on this DV or either gate.
- **C5: inapplicable.** It is prose-keyed and no .md existed at check time, so Step 7c carries that load.

## 10. Step 9b: nothing to write

- 1095 is the adjudicating run of no leg.
- It opens no fan-out.
- It does not measure the DV of any `e3_fdominance_causal_discrimination` leg.

Following the 1012c F3 precedent, it is not appended as a resolving run. Bears-on only: H2 (eligibility commensuration was not sufficient) and H3 (seed-43 binary pool).

**Mode D was checked:** no H-other signal comes from this run. The question's pre-existing CANDIDATE signal (2 confirmed legs, 4 alive) is untouched.

## 11. Step 7c red-team

**Verdict: CONTESTED.** It ran on **Fable 5.1**, a cross-model pass (the drafter is on Opus 5.5). The findings file is in the session scratchpad and is not committed.

**The load-bearing outputs survived.** The red-team recomputed every number exactly:

- C1 4/4
- C1b 2/4, with margins +0.246 / 0.000 / +0.368 / -0.053
- noise-lift 2/4
- OFF above both controls 2/4
- R_ON < R_ORACLE 3/4
- the counterfactual

It also confirmed:

- the 689i/1095 pooling is the same operationalisation
- nothing is already queued or chipped
- the brake count reproduces at 15 with this target excluded
- the SD-056 scope bound holds
- the option (ii) reasoning is sound

**Findings applied:**

- **F1 (medium).** The "new / two runs / no run has measured" noise-control premise was stale. 689c and 700d already hold the calibrated measurements. The count is now four constructions, the calibration follow-on is dropped and option (ii) is recommended.
- **F2 (medium).** The result is now mapped onto the pre-registered grid as H3, and the "measured motivation" for the final-commit replay is withdrawn.
- **F3 (low-medium).** The T_eff / gap_norm / E-composition recording gap is added.
- **F4 (low).** The counterfactual is scoped to the pre-registered 3-of-4 bar.
- **F5 (low).** Seed 43 is re-read as a genuine commit-stage null, not a forced tie.
- **Hygiene:** H1 (seed-45 per-seed note), H2/H3 (689i collapse cell, DV key name), H4 (withdrawn replay chip), H6 (fire_count), H7 (combination_rule location).

## 12. Step 8 gate -- user confirmation (2026-09-25T05:42:23Z)

- **Noise control (rec-20260925-5988ba61):** Option (ii). Governance should restate MECH-439's control set, folding into GFLAG-0471 or raising a flag beside GFLAG-0480. "Verified lifting" stays a requirement only for interpreting a NULL and no longer gates the supports branch.
- **Disposition (rec-20260925-001951da):** confirmed as drafted.
  - non_contributory / standard on MECH-439
  - routing: governance
  - no re-queue
  - the final-commit replay stays reserved, with no new motivation

## 13. Handoff

1. Nothing has been marked reviewed. claims.yaml, review_tracker, substrate_queue, the queue and the hypothesis registry are all untouched; `/governance` applies the recommendations.
2. This autopsy does not `spawn_task` its own routing follow-on. Governance chips it once the restatement is ratified.
