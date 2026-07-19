# Failure Autopsy -- V3-EXQ-708 (MECH-440) RE-ADJUDICATION

**Generated:** 2026-07-19T20:48:49Z
**Session:** elastic-benz-a7366d
**Scope:** single (re-adjudication of a landed result; NOT a re-run, NOT a re-queue)
**Status:** confirmed (user-adjudicated at the Step 8 gate)

**Target:** `v3_exq_708_mech440_noisy_selection_head_propagation_falsifier_20260628T220908Z_v3`
**Queue id:** V3-EXQ-708 | **Claim:** MECH-440 | **Machine:** ree-cloud-3

**Supersedes the 708 target of:** `failure_autopsy_700d-708-single-arena-ceiling_2026-06-29`
(that cluster autopsy's 700d target is untouched by this document)

---

## 0. Why this re-adjudication exists

The 2026-07-19 corpus audit (session `upbeat-gauss-918164`) identified V3-EXQ-708 as **the single
case in the ~52-script affected set where the stale-E3-diagnostics defect reaches a reported DV**
rather than merely a tick count. This document re-adjudicates the landed result on that basis.

It does **not** re-run, re-queue, or edit any manifest, claim, or index.

---

## 1. The defect, as it applies to 708

`ree_core/predictors/e3_selector.py` sets `last_score_diagnostics` / `last_precommit_probs` only
inside `select()`. E3 `select()` does not run every env step: `agent.py:5429` returns the held or
stepped action when `ticks["e3_tick"]` is False, before the `e3.select()` call at `agent.py:7011`.

The cadence is **not fixed**. `heartbeat.e3_steps_per_tick` defaults to 10
(`ree_core/utils/config.py:2017`), but MECH-093 modulates it with z_beta arousal between
`beta_rate_min_steps=5` and `beta_rate_max_steps=20`
(`ree_core/heartbeat/clock.py:52-70`), and MECH-091 phase resets can end a cycle early.

708's driver reads `last_score_diagnostics` at **line 780** and `last_precommit_probs` at
**line 809**, both after `agent.select_action` at **line 776**, with **no clear and no freshness
guard** (`grep` for `last_score_diagnostics = None` / `last_precommit_probs = None` in the driver
returns 0 occurrences). The `ppv.numel() == len(candidates)` check at **line 812** is **not** a
freshness guard: the candidate count is constant across ticks, so a stale vector passes it.

**Confirmed empirically, not merely by code inspection:** `n_precommit_ticks == n_p2_ticks`
*exactly*, on all 24 arm-seeds. The precommit vector was re-recorded on every env step.

---

## 2. Facts reconstruction

Manifest: `outcome=FAIL`, `evidence_direction=non_contributory`, `non_degenerate=false`,
`interpretation_label=substrate_not_ready_requeue`, `experiment_purpose=diagnostic`,
6 seeds x 4 arms = 24 completed.

Two readiness preconditions failed, and **both read the pre-commit entropy DV**:

| precondition | measured | threshold | met |
|---|---|---|---|
| `temperature_control_raises_precommit_entropy` | 0.0 | 2.0 | FAIL |
| `weight_noise_raises_precommit_entropy` | 0.0 | 2.0 | FAIL |

All five other preconditions passed (`enough_divergent_seeds`, `noise_bias_range_supra_floor_vs_raw`
0.2216, `dacc_suppression_live`, `loopseg_arm_carries_live_cross_loop_variance`,
`learning_engaged_finer_channels_dissociable`).

### 2a. The gate is a SEED COUNT, not the arm-mean delta

The commissioning brief cited -0.037 and -0.074 against a +0.05 margin. Those are the correct
**arm-mean** deltas (`1.026984 - 0.989725` and `1.026984 - 0.953191`), but they are **not the
quantity the gate tests**. `measured=0.0 / threshold=2.0` is a count of *divergent seeds* whose
paired lift clears +0.05 (driver lines 1151-1170; `MIN_SEEDS_FOR_PASS=2`,
`DIVERGENT_PASS_FRACTION=0.5`).

The divergent pool is the intersection of `gapa_divergence` over OFF + TEMP + NOISE_SINGLE, which
is **{44, 45, 46}** (n=3, matching the reported `n_divergent_seeds`). **Seed 47 is excluded** --
it is non-divergent on ARM_NOISE_SINGLE.

Per-seed lift vs A0_OFF, within the divergent pool:

| seed | ARM_TEMP lift | ARM_NOISE_SINGLE lift | short of +0.05 by (NOISE) |
|---|---|---|---|
| 44 | +0.012714 | **-0.317265** | 0.367 |
| 45 | -0.074910 | **+0.046734** | **0.003** |
| 46 | -0.069727 | **-0.209161** | 0.259 |

---

## 3. Finding 1 -- the recorded route is NOT demonstrably a weighting artifact

The commissioning hypothesis was that the readiness route is an artifact of the mass-weighting.
**On the recorded evidence it is not, and this autopsy declines to claim otherwise.**

Flipping `weight_noise_raises_precommit_entropy` requires **two** of {44, 45, 46} to clear +0.05.
Seed 45 is 0.003 nats away -- well inside artifact range. But seeds 44 and 46 are **0.26 and 0.37
nats** away. A de-duplication correction of that magnitude on a bounded entropy is not a
defensible claim. The same holds for ARM_TEMP (nearest seed short by 0.037; other two by 0.12+).

So `substrate_not_ready_requeue` **stands as the route**. The correction cannot be shown to flip it.

---

## 4. Finding 2 -- but the DV is uninterpretable in BOTH directions

Three independent observations, all from recorded data:

1. **Replication is confirmed and total.** `n_precommit_ticks == n_p2_ticks` on every arm-seed.

2. **The weighting is ARM-DEPENDENT, which is what makes it directional.** Uniform replication
   would cancel under normalization (mass scales by a constant; entropy is unchanged; only `n`
   inflates). It is not uniform:

   | seed | OFF ticks | TEMP ticks | NOISE_SINGLE ticks | NS vs OFF |
   |---|---|---|---|---|
   | 44 | 1857 | 1857 | 1888 | +1.7% |
   | 45 | 4963 | 4963 | 7818 | **+57.5%** |
   | 46 | 1612 | 1612 | 2129 | **+32.1%** |

   OFF and TEMP are tick-identical on *every* seed; NOISE_SINGLE diverges by up to +58%. The arms
   are **not exposure-matched**, so the between-arm delta is contaminated by an arm-dependent
   hold-duration distribution. Compounding this, the cadence is arousal-modulated (MECH-093), so
   the replication weight is *correlated with the agent's internal state*, not independent of it.

3. **The large negative lifts are mechanistically backwards.** The noisy selection head is applied
   at `e3_selector.py:2582`, and `last_precommit_probs` is set at `e3_selector.py:2687` -- i.e.
   the noise **is** reflected in the DV. Injecting supra-floor noise into pre-selection scores
   should tend to *flatten* the accumulated class marginal, not depress it. A **-0.317 nat**
   depression on seed 44 (and -0.209 on seed 46) is not a shape this mechanism produces. That is
   positive evidence the contamination is **large**, not that it is small and ignorable.

**Consequence.** The DV cannot support an inference in either direction. The route survives, but
708's *scientific content* -- the claim that noise was injected and pre-commit entropy did not
move -- does not.

---

## 5. Finding 3 -- what actually breaks: the prior autopsy's learning, and MECH-440's claim state

The 2026-06-29 cluster autopsy recorded, as 708's load-bearing learning:

> "Supra-floor exploration noise can be injected and still raise pre-commit entropy by **0.0** --
> it washes at the F-dominated single-arena argmax (the 687 non-propagation root, restated at the
> selection layer)."

That `0.0` **is** `measured=0.0` on the contaminated DV. The statement is a claim *about the
distorted quantity*, and it does not survive Finding 2.

`MECH-440` in `claims.yaml` currently carries `epistemic_category: substrate_ceiling`, and an
`evidence_quality_note` written **solely** from this run ("...BOTH the temperature control and the
weight noise raised pre-commit class entropy by 0.0 -- the injection washes out at the
F-dominate[d]..."). The claim-layer state therefore rests entirely on a readout that cannot bear it.

### 5a. Illusory-conflict check (mandatory pairing)

Per the standing rule, a non_contributory / substrate-limitation reading must be paired with an
explicit check of what the remaining support looks like.

The cluster's convergence argument was:

> "two structurally-different mechanisms (same-layer-null construction, noise injection) converge
> on one ceiling"

Withdrawing 708's DV **removes one of those two legs**. The ceiling reading is not thereby refuted
-- it retains 700d plus the 700b / 700c / 704b-706b lineage, and V3-EXQ-707b subsequently returned
a `non_degenerate: true` valid null concluding the conversion ceiling is **intrinsic to MECH-439
F-dominance, not a single-arena artefact**. But the *convergence* claim specifically is now
single-legged and should not be restated in its two-mechanism form.

This is recorded so the narrowing is visible rather than silently absorbed.

---

## 6. Recoverability -- NOT recoverable from the recorded emission

Checked exhaustively:

- Flat manifest: **no** `custom_information`, **no** `per_tick_sink`, no per-row list.
- Run pack `runs/<run_id>/manifest.json`: `experiment_pack/v1`, no per-row data.
- Run pack `metrics.json`: **46 characters** -- effectively empty.
- What survives: per-arm-seed **scalar aggregates** only (`precommit_class_entropy_nats`,
  `n_precommit_ticks`, `committed_class_counts`, ...).

There is a **structural** reason, documented by the V3-EXQ-785 precedent: Phase 3 cloud workers
POST only `manifest_bytes`, so even a *declared* per-tick sink is not transported. 708 ran on
`ree-cloud-3`. 785 declared a sink and it was still never transported.

**Therefore the entropy cannot be recomputed over de-duplicated / fresh-selection rows.** The
correction is not recoverable from the recorded emission, and the question 708 was built to answer
requires a corrected re-run under a new letter.

---

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | MECH-440 was never validly tested; the DV that would have tested it is contaminated. Not weakened, not strengthened. |
| Biological reference | partial | NoisyNet-style parameter-space exploration is a formal/ML import; the biological analogue (tonic DA/NE-modulated selection variability in BG action selection) is real but the translation is not lit-grounded for MECH-440. Not load-bearing here -- the run failed at measurement, before biology could be probed. |
| Prerequisites | present | All five non-DV preconditions passed; noise was genuinely injected (bias range 0.2216 supra-floor). |
| Implementation | complete | The noisy selection head worked. The **driver instrumentation** is what is defective, not the substrate. |
| Environment | adequate | Not implicated. |
| **Measurement** | **misleading** | **Dominant layer.** Mass-weighted mixture over arm-dependent, arousal-correlated hold durations, read per env step with no clear. |
| Integration | isolated | Not implicated. |
| Scale / capacity | unknown | Cannot be assessed through a contaminated DV. |

**Recommended `epistemic_category`: `measurement_test_design_defect`** (replacing `substrate_ceiling`).

This follows the V3-EXQ-785 precedent exactly: 785 was likewise re-read as
`measurement_test_design_defect` on this same defect, and its corrected re-run (785a) returned a
clean, well-powered null -- demonstrating that the corrected instrument yields a decidable answer.

### 7a. Recording-debt vs measurement-debt

This is **both**, and the distinction routes the repair:

- **Measurement-debt (primary):** the per-step-without-clear read is a *metric construction* error.
  Re-running blind reproduces it. The repair is the 785a clear-before-select pattern.
- **Recording-debt (secondary):** no per-row sink survived, so the already-executed run cannot be
  re-analysed. The re-run must *record* fresh-selection rows, per the Experimental Recording
  Standard (`experimental_recording_standard_2026-07-12.md` Sec 3b/3c), and must not rely on a
  declared-but-untransported sink on a cloud worker.

---

## 8. Re-derive brake (MOVE-3)

**Not fired.** Recommended category is `measurement_test_design_defect`, not
`substrate_ceiling` / `non_contributory`-as-ceiling, so the brake's counting rule is not met.
The prior 708 autopsy stamped `fired: false` (1st for MECH-440); this re-adjudication *withdraws*
that reading rather than adding a second one, so the MECH-440 ceiling count moves to **0, not 2**.

**A corrected re-run is not the behaviour the brake exists to prevent.** The brake stops a claim
being re-tested at the same granularity against the same substrate ceiling, letter after letter.
708a is **instrument repair**: the prior run never validly measured its DV. This is precisely the
785 -> 785a shape, which the corpus already sanctions.

### 8a. Granularity-debt recurrence trigger

**Not fired.** A prior autopsy on this target exists
(`failure_autopsy_700d-708-single-arena-ceiling_2026-06-29`), which is normally the recurrence
signal. It is honestly stamped as not firing here because this document is a **re-adjudication of
the same run**, not a second experiment circling MECH-440 with a different failure signature. There
is one experiment and one dataset. Recording it as recurrence would inflate the granularity-debt
signal with a bookkeeping artifact.

---

## 9. Learning extracted

1. **708 is the one case in the ~52-script affected set where the stale-E3 defect reaches a
   reported DV.** The audit's targeting was correct, and the reason is structural: 705 and 709 gate
   on *counts with exact-zero seeds* (see Sec 11), which duplication cannot manufacture; 708 gates
   on a *continuous mass-weighted entropy*, which has no such invariance.
2. **Uniform replication is harmless; arm-dependent replication is not.** The distortion here is
   real only because exposure differs by arm (up to +58% on a matched seed). This is the general
   test to apply to the rest of the affected corpus -- inflated `n` alone is not sufficient for
   contamination.
3. **A mechanistically-backwards effect sign is a contamination detector.** Noise injected upstream
   of the readout producing a 0.3-nat entropy *depression* is the tell that flagged this run's DV
   as untrustworthy, independent of any margin arithmetic.
4. **A defective instrument can leave the ROUTE correct while destroying the CONTENT.** 708 landed
   on a defensible route for an indefensible reason. Adjudicating only the route would have
   preserved a false learning and a false claim-layer note.
5. **Declared per-tick sinks do not survive Phase 3 cloud transport.** Any experiment relying on
   row-level re-analysis must not assume a declared sink will exist; this is now twice-confirmed
   (785, 708).

---

## 10. Routing

**`queue-experiment` -- corrected re-run as V3-EXQ-708a (RECOMMENDATION ONLY; NOT QUEUED).**

Per the commissioning constraint, this session does not re-queue. Verified before recommending:
`ree-v3/experiment_queue.json` is **empty (depth 0)**; no 708/705/709 entry is in flight; no
active TASK_CLAIMS entry covers a 708 re-queue.

Required properties of 708a (same scientific question -> alphabetic suffix):

1. **Clear before every select.** Set `agent.e3.last_score_diagnostics = None` and
   `agent.e3.last_precommit_probs = None` immediately before every `agent.select_action(...)`;
   record a row **only if repopulated**. Reference implementation:
   `ree-v3/experiments/v3_exq_785a_mech463_arousal_exogenous_urgency_decomp.py` (lines 525-543).
2. **Report the yield.** Emit `n_fresh_select`, `n_latched`, and `fresh_select_yield` as telemetry,
   so the replication factor is visible in the manifest rather than inferred.
3. **Exposure-match the arms, or report the imbalance.** The +58% OFF-vs-NOISE tick divergence must
   be either controlled or recorded per arm-seed, since it is the mechanism of the distortion.
4. **Record per-seed fresh-selection counts in the manifest itself** -- do NOT rely on a declared
   `per_tick_sink` (not transported on cloud workers; see Sec 6).
5. `supersedes: "V3-EXQ-708"` on the queue entry, and `supersedes` on the run manifest.
6. Stamp the recording core via `experiments/_lib/manifest_core.stamp_recording_core(...)`.

**Note on venue:** the prior autopsy's recommended next step ("the ARC-110-gated ARM_NOISE_LOOPSEG
arm, not a single-arena 708 letter") has since been answered -- V3-EXQ-707b returned
`weakens` on the single-arena-artefact sub-hypothesis with a valid null. So 708a should be designed
against the current MECH-439 F-dominance reading, not as a bet that loop segregation relieves the
ceiling.

---

## 11. Secondary targets -- V3-EXQ-705 and V3-EXQ-709: defect PRESENT, verdicts INVARIANT

Both were assessed. In both, the defect is confirmed present exactly as described (unconditional
per-env-step reads, no clear anywhere, gated only on coarse phase flags). **Neither verdict moves,
and neither prior autopsy's conclusion is undermined.** Neither needs re-adjudication.

**V3-EXQ-705** (MECH-314; already `superseded` by 705b; prior autopsies exist for both).
Read at driver line 574, no clear. The failing quantity (`f_eligibility_excluded_count_mean`) *is*
a duration-weighted mean over replicated rows, as the audit suspected. But the gate is a seed count
(`legC_seeds_non_degenerate=1`, needs 2), and **two of three seeds record `excluded_count` of
exactly 0.0 and `envelope_size` of exactly 32.0 across their entire windows**. Duplication can only
repeat an already-observed genuine value; it cannot manufacture a non-zero from an all-zero genuine
record, nor suppress a non-zero into an exact zero. So those seeds are all-admit in the *genuine*
record, and no correction magnitude flips the gate. The prior autopsy's reading ("a correctly-caught
invalid precondition... NOT a MECH-314 weakening") **survives**. 705b's failing criterion is
`committed_class_entropy`, computed from actions actually emitted, and does not touch
`last_score_diagnostics` at all -- untouched by the defect.

**V3-EXQ-709** (MECH-439 / ARC-108 / ARC-110). Read at driver line 801, no clear;
`clg_active_ticks == n_p2_ticks` exactly on every seed, directly confirming per-step recording.
The failing gate `limbic_loop_can_win` (measured 1.0, threshold 2.0) is a count of seeds whose
underlying tick count is `> 0`. Among the four GAP-A-divergent seeds, **three record exactly 0** and
one records 1795. Deflating an inflated count cannot make a zero positive, and cannot zero out a
positive (at least one genuine occurrence must have originated the duplicated value). **The
classification is invariant in both directions.** The audit's concern that this was "one seed short
of clearing" does not hold: the shortfall is in hard-zero seeds, not marginal ones. The prior
autopsy's `substrate_ceiling` / `implement-substrate` routing and its re-derive-brake firing
(MECH-439 8th, ARC-108 6th) are **unaffected**.

---

## 12. Draft `evidence_quality_note` for governance (EXACT TEXT -- not applied here)

### 12a. For the V3-EXQ-708 manifest

> RE-ADJUDICATED 2026-07-19 (failure_autopsy_V3-EXQ-708_2026-07-19), superseding the 708 target of
> failure_autopsy_700d-708-single-arena-ceiling_2026-06-29. This run's pre-commit class entropy DV
> is INVALID. The driver read agent.e3.last_precommit_probs (line 809) and last_score_diagnostics
> (line 780) once per ENV STEP with no clear and no freshness guard; the numel()==len(candidates)
> check at line 812 is not a freshness guard because the candidate count is constant. E3 select()
> runs only on an E3 tick (agent.py:5429 returns the held action before the e3.select() call at
> agent.py:7011), at a cadence that VARIES 5-20 steps under MECH-093 arousal modulation
> (clock.py:52-70, default 10 at config.py:2017). Confirmed empirically: n_precommit_ticks ==
> n_p2_ticks exactly on all 24 arm-seeds. The DV is therefore a mass-weighted mixture in which each
> probability vector is replicated by its hold duration. This is DIRECTIONAL, not merely an inflated
> n, because exposure is ARM-DEPENDENT: A0_OFF and ARM_TEMP are tick-identical on every seed while
> ARM_NOISE_SINGLE diverges by +1.7% / +57.5% / +32.1% on divergent seeds 44/45/46. Corroborating
> sign check: the noisy head is applied at e3_selector.py:2582, upstream of last_precommit_probs at
> :2687, so noise should FLATTEN the class marginal; the recorded -0.317 and -0.209 nat DEPRESSIONS
> on seeds 44 and 46 are mechanistically backwards and indicate the contamination is large. WHAT
> STANDS: the substrate_not_ready_requeue ROUTE survives -- flipping weight_noise_raises_precommit_
> entropy needs 2 of {44,45,46} to clear +0.05, and although seed 45 is only 0.003 nats short,
> seeds 44 and 46 are 0.26 and 0.37 nats short, which no de-duplication can supply. WHAT DOES NOT
> STAND: the finding that "noise was injected supra-floor and raised pre-commit entropy by 0.0",
> which is a statement about the contaminated quantity and cannot be sustained in either direction.
> Epistemic category CORRECTED substrate_ceiling -> measurement_test_design_defect. NOT RECOVERABLE:
> no custom_information, no per_tick_sink, metrics.json is 46 chars, only per-arm-seed scalars
> survive; Phase 3 cloud workers POST only manifest_bytes so a declared sink would not have been
> transported either (this run: ree-cloud-3). Routes to queue-experiment for a corrected V3-EXQ-708a
> using the clear-before-select pattern of v3_exq_785a. See also: this withdrawal leaves the
> 700d-708 cluster's two-mechanism convergence claim single-legged (700d is unaffected).

### 12b. For MECH-440 in `claims.yaml`

Recommend **clearing `epistemic_category: substrate_ceiling`** (its sole basis is withdrawn; the
claim reverts to untested rather than ceiling-limited), and replacing the `evidence_quality_note`:

> V3-EXQ-708 (MECH-440 NoisyNet propagation falsifier) was RE-ADJUDICATED 2026-07-19
> (failure_autopsy_V3-EXQ-708_2026-07-19). Its pre-commit class entropy DV is invalid: the driver
> read e3.last_precommit_probs once per env step with no clear, and E3 select() runs on a 5-20-step
> arousal-modulated cadence, so each probability vector was replicated by its hold duration. The
> weighting is arm-dependent (matched-seed exposure differs by up to +58% between the OFF and NOISE
> arms), so the between-arm delta is distorted, not merely imprecise. The previously recorded
> finding -- that supra-floor weight noise raised pre-commit entropy by 0.0 and therefore "washes
> out at the F-dominated single-arena argmax" -- is a claim about the contaminated quantity and is
> WITHDRAWN. The run's substrate_not_ready_requeue route survives on margin arithmetic, but MECH-440
> was never validly tested. Noise injection itself was genuine (bias range 0.2216, supra-floor), and
> all five non-DV preconditions passed, so the defect is in driver instrumentation, not in the
> substrate. epistemic_category substrate_ceiling CLEARED -- MECH-440 is untested, not
> ceiling-limited. The correction is not recoverable from the recorded emission (no per-row sink;
> Phase 3 cloud workers transport only manifest_bytes). Pending a corrected re-run V3-EXQ-708a using
> the clear-before-select pattern of v3_exq_785a. MECH-440 remains candidate / v3_pending.

---

## 13. Hypothesis-space ledger (Step 9b) -- INTENT ONLY, not written

The registry write is **deliberately skipped**. Session `elastic-newton-d18328` holds an active
TASK_CLAIMS entry on `evidence/planning/hypothesis_space_registry.v1.json`, and a large uncommitted
derived-artifact regen was present in the REE_assembly working tree at autopsy time. A whole-file
read-modify-write would have risked adopting another session's uncommitted edits under this
session's commit.

Intent is recorded machine-readably in the companion JSON under `hypothesis_space_ledger_pending`
for the claim holder or the next `/governance` walk to apply. In summary: this re-adjudication
opens no fan-out and eliminates no leg. It **withdraws** the evidentiary basis of an existing
resolution, so any registry leg resolved by 708's pre-commit entropy readout should revert from a
resolved state to `alive`, with `resolving_runs` retained and a basis noting the withdrawal.
