**Status: RESOLVED AND APPLIED 2026-09-25. Nothing in this file has been written to claims.yaml or substrate_queue.json; the experiment IS now queued (see section 6).**

*(This file was staged AWAITING USER REVIEW when the design was refused at red-team pass 1. The
decision came back the same day and has been applied -- section 6 records what was chosen, what was
built, and what the second red-team pass then found. Read section 6 before sections 1-5, which
describe the pre-decision state.)*

# V3-EXQ-1099 contamination-truncation extension probe -- red-team BLOCKING, design NOT queued

- Session: `metaworker-science-20260925-orchc-contamination-probe` (headless, ree-cloud-4), campaign `science-20260925-orchc-contamination-probe`
- Chip: `chip-20260924-contamination-extension-probe` (governance-20260924's own spawn off the confirmed `failure_autopsy_V3-EXQ-1080_2026-09-24`, section 7 "Optional follow-on")
- Script authored, smoke-tested and LANDED (not queued): `ree-v3` `03a76b0a9f`, `experiments/v3_exq_1099_contamination_truncation_extension_probe.py`
- EXQ slot reserved: **V3-EXQ-1099** (1098 was taken by a sibling science worker two minutes earlier)
- **Queue entry NOT appended. The experiment will not run.** This is a refusal at `/queue-experiment` Step 4.5, recorded per that step's own instruction.
- Red-team: **Fable** (drafting session is Opus 5), one pass, not iterated. Verdict **BLOCKING**.

## 1. What was built, and why it is not queued

The chip asked for a same-pattern extension of V3-EXQ-1080 covering the three claims 1080's
confirmed autopsy left uncovered: **INV-054** (V3-EXQ-278/435), **MECH-427** (883), **MECH-106** (231a).
Each target is re-executed through its own loop twice -- ARM_STOCK as written, ARM_OPTOUT with
`hazard_free_contamination_gate=True` -- and the load-bearing criterion is whether any target's own
verdict tuple differs between the arms.

The design cleared every pre-flight gate (2.4 GOV-REUSE-1, 2.5, 2.5a, 2.5b, 2.5c, 2.5d, 2.6), smoked
clean three times, and passed `validate_experiments.py --strict` on all 40 checks. The Step 4.5
adversarial design review then found that **the probe as designed cannot honestly clear any of its
three target claims**, for three independent reasons. Both decisive findings were re-verified from
source by the authoring session before this was written; the figures below are this session's own
measurements, not the reviewer's report taken at face value.

## 2. Findings that survived verification

### F2 (BLOCKING) -- MECH-427 / V3-EXQ-883: the exposure lands entirely on an arm whose DV is pinned at zero

Measured at FULL scale, both arms, all 3 seeds (`.scratch/verify_f2.log`, reproducible in ~30 s):

| arm | cell | `parent_goal_norm_final` | episode |
|---|---|---|---|
| ARM_STOCK | ATTAINED seed 42/43/44 | 0.14265922 / 0.17506921 / 0.12496483 | 40 steps, health 1.0, **0 contacts** |
| ARM_STOCK | NO_ATTAINMENT seed 42/43/44 | **0.00000000** (all three) | **7 steps, health_depleted, 3 contacts** |
| ARM_OPTOUT | ATTAINED seed 42/43/44 | 0.14291425 / 0.17527708 / 0.12509361 | 40 steps, health 1.0, 0 contacts |
| ARM_OPTOUT | NO_ATTAINMENT seed 42/43/44 | **0.00000000** (all three) | 40 steps, health 1.0, 0 contacts |

- 883's NO_ATTAINMENT arm plays `STAY_ACTION` every step (`v3_exq_883...py:171-172`), so it sits on one
  cell, contaminates it in 4 entries, and dies at step **7 of 40** -- 82.5% window loss, on every seed.
  The footgun fires about as hard as it can.
- But that arm's DV is `parent_goal_norm_final`, and it is **exactly 0.0 in both arms** because STAY
  never attains a waypoint, so the sole write path (`credit_subgoal_attainment`) is never called.
  Truncating an episode whose DV is structurally 0 cannot change that DV.
- Both of 883's criteria (`c1: attained > no_attain`, `c2: attained > floor`,
  `v3_exq_883...py:280-285`) therefore depend only on the **ATTAINED** arm, which is **never exposed**
  (0 contacts, full 40 steps, in both arms). The gate moves ATTAINED's norm only in the 4th decimal.
- Verdict is `PASS / supports` in both arms by construction.

**Why this is worse than a null result.** The probe would compute `stock_dv_death_frac = 3/6 = 0.5`,
clear the 0.10 materiality bar, find the verdict unchanged, and emit
`classification: truncated_verdict_robust` -- which in 1080's pre-registered taxonomy means
"materially exposed AND verdict-robust", i.e. *a passed sensitivity test*. It would then record
MECH-427 under `direct_claims_cleared_no_rerun_owed`. The reading would be the strongest one the
taxonomy can produce, on a test that cannot fail. 1080's own autopsy already named this shape for
V3-EXQ-904 ("904 / ARC-070 is 'clean', not 'robust': it was never exposed"; "insensitive by
construction and not merely unexposed") -- and the extension inherits the gap without a class for it.

Two pre-registered criteria (`883::stock_dv_death_frac_below_material`,
`883::verdict_unchanged_stock_vs_optout`) cannot discriminate under any outcome. That is the BLOCKING
definition.

### F1 (CONFIRMED) -- V3-EXQ-435's baseline direction is a hand-applied reclassification, not the driver's output

`evidence/experiments/v3_exq_435_.../v3_exq_435_..._1776660122.json`:

> `evidence_direction_note`: "Reclassified non_contributory 2026-04-22: ree-v3 substrate has only
> smooth/graded updates; phase_transition recovery requires discrete operating_mode primitive
> (SD-032a + MECH-259). Graded recovery in 3/3 seeds is the only output the substrate can produce.
> pending_retest_after_substrate."

Re-running the driver's own `_aggregate` over the landed `per_seed_results` returns
**`('FAIL', 'does_not_support')`** (dep_established 3/3, onsets 1/2/3, all `graded`). So:

1. The probe's `original.evidence_direction = "non_contributory"` literal makes
   `stock_reproduces_original` **False by construction** for 435, manufacturing a phantom
   `historical_verdict_not_reproduced` "substrate drift" entry for `/governance` to chase.
2. The docstring premise that 435 is *a priori degenerate* (and the claims-vs-targets readiness rule
   justified by it) is **false**: `does_not_support` is not degenerate, so 435 will be determinable.

**The generalisable lesson, which is the most reusable thing in this file:** a landed manifest's
`evidence_direction` is **not necessarily the driver's own verdict** -- governance amends that field.
Any probe whose DV is "does the target's own verdict change" must compare against what the DRIVER
emits, i.e. re-aggregate the landed per-seed rows, not read the amended field. Checked across all
four of this probe's targets and 1080's four: **435 is the only reclassified one**, so 1080's own
readings are not retroactively suspect -- but the exposure was structural, not bad luck.

### F4/F5 (CONFIRMED by the reviewer's measurement, not re-measured here) -- INV-054's DV is at the floor, and the gate cannot reach the phase that sets the verdict

- 278's STOCK recovery latency is already **1** (the floor) at full-scale phase 1, reproducing the
  April result exactly. A verdict flip needs latency > 50 on 2/3 seeds, and the gate can only *raise*
  benefit exposure, so OPTOUT cannot recover later. `278::verdict_unchanged` is pinned in practice.
- The "depression" 278/435 measure is established in **phase 1**, the 3-hazard LONG_HORIZON env, where
  the agent dies in 2-7 steps from proximity harm and where **the gate is inert by design**
  (`num_hazards != 0`). Phase 2's hazard-free self-contamination is real (100% of DV episodes die --
  this session's positive control measured 20/20 on that exact geometry) but sits downstream of where
  the verdict is decided. `claims.yaml` INV-054 already carries `pending_substrate_reconfirmation`.
- Net: of the three mandatory claims, MECH-427's test is vacuous (F2) and INV-054's is pinned and
  out of the gate's reach (F4/F5), leaving **MECH-106 / 231a as the only live input to C_PREV** -- and
  the reviewer's F6 notes the route cannot separate 231a's sensitivity from substrate drift, because
  it ignores `stock_reproduces_original` and `monostrategy_suspect` when choosing the rerun label.

At ~6 hours of measured worker time (231a ~110 min/arm, 278/435 ~19-33 min/arm, both measured this
session), that is a run that would produce a confident, wrongly-labelled clearance for MECH-427 and
nothing defensible for the other two.

## 3. What the session did NOT do, and why

The fixes the review implies all change **what gets measured** -- which targets, which pre-registered
criteria, which claims become clearable, and what a clean result licenses. Under the dispatch brief's
consent rule those are the user's decisions, and the brief is explicit that a red-team refusal is a
result to record and report rather than to re-design around unattended. So no criterion was relaxed,
no target dropped, no threshold moved.

## 4. Options for the user (the decision chip states these too)

- **(A) Drop 883, score two claims.** Cheapest and fully honest: INV-054 (278/435) + MECH-106 (231a),
  `MIN_DETERMINABLE_CLAIMS` 2, MECH-427 explicitly moved to `claims_not_covered` with F2 as the
  recorded reason. Loses MECH-427 coverage; ~4 h.
- **(B) Add an `insensitive_by_construction` class and keep 883 as a recorded negative.** 883 still
  runs (~1 min) but can never clear MECH-427; the class makes the 904-shaped gap explicit in the
  taxonomy for every future re-use of this pattern. Recommended if MECH-427's status should reflect
  "not answerable by this instrument" rather than silently staying uncovered.
- **(C) Re-pose 883 so the exposure reaches a live DV.** The exposed arm would need a DV that can move
  -- e.g. expose ATTAINED (longer episodes, or a revisiting waypoint schedule). This is a new
  experimental design for MECH-427, not an audit of its existing evidence, so it is a separate EXQ
  number and outside this chip's scope.
- **(D) Also fix the 435 baseline (orthogonal to A-C, and cheap).** Derive each target's `original`
  from its driver's own `_aggregate` over the landed per-seed rows instead of the manifest's amended
  `evidence_direction`. Removes the phantom drift entry and corrects the readiness rationale.
- **(E) Abandon the extension.** State in `claims.yaml` that INV-054/MECH-427/MECH-106's contamination
  caveat is not resolvable by the 1080 pattern, with F2/F4/F5 as the reason, and leave the three
  claims' caveat standing as 1080 left it.

**This session's recommendation: (B) + (D).** (B) keeps all three claims in the frame and converts a
silent vacuity into a named, reusable taxonomy class -- the 904 gap has now cost two probes, and
naming it is what stops a third. (D) is a small correctness fix whose absence would otherwise emit a
false substrate-drift finding. Together they keep the run at ~4 h and make every one of the three
claims' outcomes readable: INV-054 scoped to phase 2 and explicitly not cleared on phase-1 grounds,
MECH-427 recorded as not answerable by this instrument, MECH-106 answered subject to the drift and
monostrategy caveats already recorded per target.

## 5. Provenance

- Red-team findings verbatim (Fable, 47 tool calls): `.scratch/redteam_1099.md` in the session
  worktree, reproduced in substance above. Its own scratch probes were `rt1099_*.py`.
- This session's independent verifications: F1 by re-aggregating 435's landed rows; F2 by running 883
  at full scale under both arms through the probe's own instrument.
- Pre-flight gate results, the three smokes, and the measured runtimes are in the driver's module
  docstring and in this session's `TASK_CLAIMS` completion note.


---

## 6. RESOLUTION -- decision applied, experiment queued (2026-09-25)

**Decision** by `orchestrate-20260924-1707` under the user's standing delegation
(`rec-20260924-fb429c72`) on `chip-20260925-exq1099-redteam-blocking`: this session's recommendation
**(B) + (D)**, plus two additions -- pre-register INV-054 as phase-2-only and explicitly not cleared
on phase-1 grounds (F4/F5), and make the routing grid READ `stock_reproduces_original` and
`monostrategy_suspect` so drift and contamination-sensitivity are separable (F6).

**Queued: V3-EXQ-1099**, `ree-v3` `1fdfd4e05e` (entry) on top of `236fb2d927` (final script).
Verified reconciled into the coordinator DB by snapshot survival: the phase3 queue writer's
snapshot `58e33c21` re-materialised `experiment_queue.json` from the DB *after* the entry commit and
V3-EXQ-1099 survived it, so it will be claimed by a runner. `estimated_minutes` 360 is an upper
bound measured on a contended 2-core box.

### What was implemented

| Decision | Implementation |
|---|---|
| (B) `insensitive_by_construction` class | `dv_exposure_coupling` is **measured** per target (`coupled`/`decoupled`/`unknown`; `unknown` deliberately does not trigger the class). A material exposure that is `decoupled` classifies `insensitive_by_construction`: determinable, an informative negative, `can_clear_its_claim = False`, excluded from readiness. Verified at FULL scale for 883: `n_exposed_and_dv_moved = 0`, 3 moved-but-unexposed -> `decoupled`, so MECH-427 lands in `claims_not_covered` as NOT ANSWERABLE BY THIS INSTRUMENT. |
| (D) driver-derived baselines | `_resolve_original()` uses each driver's own `_aggregate` over the landed per-seed rows, else a manifest with no amendment note, else **None** (never False). 435 now resolves via `driver_aggregate` to `does_not_support`, killing the phantom drift entry. |
| INV-054 phase-2 scoping | `CLAIM_SCOPE` pre-registers it before any run and the scope string travels with any clearance into `direct_claims_clearance_scope`, so a bare id cannot be read as an unconditional clear. |
| Drift/monostrategy-aware routing | Sensitivity splits into `attributable` / `confounded`; an all-confounded set routes to `contamination_sensitivity_present_but_not_attributable_adjudicate_drift_first`. A not-ready run whose only uncovered claims are non-reproducing routes to `historical_verdicts_not_reproduced_adjudicate_drift_first` rather than reading as an instrument fault. |

### Two bugs the new machinery found in itself, before any real run

Both were caught by reading the detector's own per-cell output, not by review -- which is the case
for recording that detail rather than a bare verdict:

1. **Positional pairing of DV rows to episodes was wrong.** A dying episode is recorded at its own
   `done` tick while a survivor is only recorded by `_flush_live()` at the end of the cell, so the
   episode list is in COMPLETION order, not creation order. It mis-attributed NO_ATTAINMENT's
   step-7 death to ATTAINED. Now paired BY NAME via a per-cell `phase` tag, asserted, and returns
   `unknown` rather than a wrong answer if it stops holding. It had failed *safe* (reported
   `coupled`, so the class did not fire), but it was wrong.
2. **The readiness bar became unsatisfiable.** With MECH-427 permanently unanswerable, a 3-of-3
   claim-coverage bar was unreachable by construction. The remedy is to **scope the gate, never
   lower it**: an unanswerable claim is scoped out of the denominator with its reason recorded, and
   `MIN_ANSWERABLE_CLAIMS = 2` keeps the gate falsifiable -- it still fails if 231a or both of
   278/435 go degenerate.

### Red-team pass 2 (fable, on the revised causal chain): CONTESTED

It confirmed every pass-1 fix from source and independently re-verified the four `intended_units`
literals. Four live findings, all **fixed**:

- **P2-1 (the real one).** Attribution was one-sided -- applied only to SENSITIVE targets. A target
  whose verdict was ROBUST but which never reproduced its driver-derived baseline could still clear
  its claim and drive `outcome: PASS`, while the same manifest listed it under
  `historical_verdict_not_reproduced`. Asserting a claim's historical evidence is contamination-safe
  is unsupportable when that historical verdict did not reproduce at all. Clearance now requires
  STOCK reproduction and no monostrategy collapse.
- **P2-2.** A gate-RESTORES-history outcome (STOCK fails, OPTOUT reproduces the baseline) is the
  strongest contamination attribution available and was routed `not_attributable`, because only
  STOCK was ever examined. Attribution now accepts either arm, and
  `optout_restores_historical_verdict` is recorded.
- **P2-3.** `reruns` could name an unanswerable claim (a re-run of this design cannot decide it), and
  a claim could land in no run-level bucket at all, visible only in `per_claim_disposition`.
- **P2-5.** `criteria_non_degenerate` was keyed on `determinable` alone, so an
  `insensitive_by_construction` target's two non-discriminating criteria were labelled
  NON-degenerate -- the opposite of the finding, in the one field built to report it.

Two **dismissed with reasons**, recorded in the manifest at
`interpretation.residual_caveats_pass2`:

- **P2-6.** Coupling is measurable only for 883, so it is `unknown` for 231a -- the sole load-bearing
  input to C_PREV -- and the F2-style vacuity cannot be positively *ruled out* there. Accepted as a
  stated limitation rather than silently: the risk is bounded by the P2-1 fix (231a cannot clear
  MECH-106 unless it reproduced its baseline), and a derivable 231a coupling detector (per-seed
  `da_pos` plus the same per-cell tagging 883 uses) is **named follow-on**. Separately, `coupled`
  tests DV movement rather than reach-to-criterion.
- **P2-4.** If 435 is `cannot_determine`, INV-054's clearance rests on 278 alone, whose
  recovery-latency criterion is pinned at its floor of 1. `CLAIM_SCOPE` already states this.

### The generalisable lesson, restated because it outlives this probe

**A landed manifest's `evidence_direction` is not necessarily the driver's own verdict** --
governance amends that field in place. Any probe whose DV is "does the target's own verdict change"
must re-aggregate the landed per-seed rows rather than read the amended field. Checked across this
probe's four targets and V3-EXQ-1080's four: 435 is the only amended one, so 1080's readings are not
retroactively suspect, but the exposure was structural rather than bad luck.
