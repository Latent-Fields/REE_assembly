# Failure Autopsy -- V3-EXQ-621a (scaffolded SD-054 onboarding substrate-readiness diagnostic)

- **Generated (UTC):** 2026-06-06T09:47:32Z
- **Run:** `v3_exq_621a_scaffolded_sd054_onboarding_substrate_readiness_20260531T230932Z_v3`
- **Queue ID:** V3-EXQ-621a (supersedes V3-EXQ-621)
- **Outcome:** PASS (`experiment_purpose: diagnostic`; `evidence_direction: non_contributory`; `scoring_excluded: diagnostic_probe`)
- **claim_ids (tagged, reclassified non_contributory):** Q-045, MECH-313, MECH-260
- **Scope:** single
- **Status:** confirmed (interactive gate answered 2026-06-06 -- "Contained-correction")
- **Priority:** #1 in `retrospective_diagnostic_selfroute_audit_2026-06-06.md` (closest legacy analogue to the V3-EXQ-642 vacuous-pass pattern that moved governance)

---

## 1. Verdict (one line)

`overall_pass: true` is a **VACUOUS_PASS**: the one load-bearing scientific criterion
(C2 z_goal floor) FAILED, and it failed **by construction** -- the substrate as-run
was structurally incapable of producing a non-zero z_goal -- while the PASS was carried
by a **degenerate C1** (inflated by 3 by-construction baseline auto-completions) and a
**vacuous C3** (an "approach-commit lift" attributed to a goal cascade that cannot exist
when z_goal is identically 0). This is the same precondition-unmet fault class as
V3-EXQ-642 (`failure_autopsy_V3-EXQ-642_2026-06-06`).

**However, the blast radius was contained.** The 2026-06-01T05:50Z "cleared
substrate-readiness diagnostic" declaration overclaimed, but (a) no claim confidence
moved (the run was `non_contributory` / `scoring_excluded`), (b) the system's own
behavioural successor V3-EXQ-603d -- queued *by* this clear -- re-exposed the same
z_goal=0 wiring fault within ~12 hours and re-opened the substrate as `amend_pending`,
and (c) `substrate_queue.ready` stayed `false` throughout and GAP-C stayed
`blocked_pending_substrate` (prereq (2) still the load-bearing blocker). The durable
state is therefore already correct; the only lingering artifact is overclaiming language
in two `evidence_quality_note` blocks.

**Route: `implement-substrate` action=`none`** (the substrate gap was already diagnosed
by 603d and the amend chain has landed; the genuine substrate-readiness gate is the
pending full-scale run that `ready=false` already enforces). Governance should append a
one-line correction to the two `evidence_quality_note` blocks recording that 621a was a
vacuous pass and did not actually clear substrate-readiness. The V3-EXQ-621 supersession
stands (manifest hygiene). **Do NOT re-run 621a** -- the substrate it tested no longer
exists (>=4 amends since).

---

## 2. Facts reconstruction (no interpretation)

### Acceptance block (manifest)

```
C1_cells_completed:    true   C1_n_completed: 6   C1_n_total: 12
C2_z_goal_floor_met:   false  C2_arm_passed: ""
C3_cascade_consequential: true  C3_reason: "approach_commit_lift in ARM_2_SCAFFOLD_AND_ANNEAL"
overall_pass:          true
```

Decision rule (script `evaluate_acceptance`, [v3_exq_621a...py:347-399](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_621a_scaffolded_sd054_onboarding_substrate_readiness.py)):
`overall = C1 AND (C2 OR C3)`.

### Per-cell (12 cells = 4 arms x 3 seeds)

| arm | seed | cell_completed | p1_survival | z_goal_norm_peak_max | approach_commit_rate | abort_reason |
|---|---|---|---|---|---|---|
| ARM_0_ALL_OFF | 42 | **true** (by construction) | n/a | 0.0 | 0.0 | -- |
| ARM_0_ALL_OFF | 43 | **true** (by construction) | n/a | 0.0 | 0.0 | -- |
| ARM_0_ALL_OFF | 44 | **true** (by construction) | n/a | 0.0 | 0.0 | -- |
| ARM_1_SCAFFOLD_ONLY | 42 | false | false | 0.0 | 0.0 | p1_survival_gate_failed |
| ARM_1_SCAFFOLD_ONLY | 43 | false | false | 0.0 | 0.0 | p1_survival_gate_failed |
| ARM_1_SCAFFOLD_ONLY | 44 | false | false | 0.0 | 0.0 | p1_survival_gate_failed |
| ARM_2_SCAFFOLD_AND_ANNEAL | 42 | true | true | **0.0** | **1.0** | -- |
| ARM_2_SCAFFOLD_AND_ANNEAL | 43 | false | false | 0.0 | 0.0 | p1_survival_gate_failed |
| ARM_2_SCAFFOLD_AND_ANNEAL | 44 | true | true | **0.0** | **1.0** | -- |
| ARM_3_..._FROM_SCRATCH | 42 | true | true | 0.0 | 1.0 | -- |
| ARM_3_..._FROM_SCRATCH | 43 | false | false | 0.0 | 0.0 | p1_survival_gate_failed |
| ARM_3_..._FROM_SCRATCH | 44 | false | false | 0.0 | 0.0 | p1_survival_gate_failed |

- **z_goal_norm_peak_max = 0.0 in every cell of every arm and seed.** This is the
  single most important fact in the manifest.
- Scaffolded-arm survival (excluding the by-construction ARM_0 baseline): ARM_1 0/3,
  ARM_2 2/3, ARM_3 1/3 -> **3/9 = 33%**.
- `approach_commit_rate` = 1.0 in the 3 completed scaffold cells (ARM_2 s42/s44, ARM_3
  s42); 0.0 in all ARM_0 baseline cells.

### Which criterion failed, and the fingerprint

- **C2 (z_goal floor) -- the load-bearing substrate-readiness criterion -- FAILED.**
  C2 is precisely the test of prereq (2) of `behavioral_diversity_isolation:GAP-C`:
  *"goal-pipeline training regime produces non-trivial z_goal."* z_goal was 0 everywhere.
- **C1 passed at exactly the floor (6/12)** but only because the 3 `ARM_0_ALL_OFF` cells
  are hardcoded `cell_completed = True  # baseline always "completes"`
  ([v3_exq_621a...py:290](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_621a_scaffolded_sd054_onboarding_substrate_readiness.py)).
  The numerator and denominator both include baseline auto-completes.
- **C3 passed** via `np.mean(approach_commit_rate over completed ARM_2 cells) -
  baseline_rate = 1.0 - 0.0 = 1.0 >= 0.10`.
- Shape: "the substantive (discrimination) criterion fails; a partial/structural
  criterion + a cascade criterion carry the PASS." This is the
  `overall_pass=true with the headline criterion false` machine-detectable vacuity
  named in the retrospective audit Section 5.

---

## 3. Vacuity analysis (criterion by criterion)

### C1 is degenerate (baseline-inflated)

The "cells complete" criterion is meant to test *"the scaffolded onboarding lets the
agent survive the target env after the curriculum"* (script docstring). But ARM_0 is the
no-scaffold baseline and its 3 cells complete by definition (`cell_completed = True`,
because the baseline "measurement IS the comparison"). Counting them in both numerator
and denominator inflates C1 from the real scaffolded survival of **3/9 (33%)** up to
**6/12 (50%)** -- exactly clearing the `n_total//2` floor. The scaffold's own survival
question fails on its own terms.

### C3 is vacuous (a goal cascade with z_goal=0)

C3 is defined as *"goal pipeline behaviourally consequential."* Its `approach_commit_lift`
route attributes the ARM_2 approach-commit rate (1.0) to the goal pipeline. But z_goal is
**identically 0** in those very cells -- there is no goal-pipeline output for any cascade
to be consequential *of*. Compounding this, `approach_commit_rate` is computed by two
different code paths: ARM_0 via `measure_arm0_baseline` (counts `beta_gate.is_elevated`
steps) and the scaffold arms via `scheduler.run_p2`. The 0.0-vs-1.0 contrast is therefore
not even a like-for-like measurement, and whatever the 1.0 reflects (commitment / beta
elevation) it cannot be goal-directed approach when z_goal=0.

### C2 -- the only substantive criterion -- failed by construction (see Section 4)

So `overall = C1(degenerate) AND (C2(false) OR C3(vacuous))` resolves to `true` while the
load-bearing claim is unsupported. Textbook vacuous pass.

---

## 4. Root cause -- z_goal=0 was structurally guaranteed (precondition_unmet)

z_goal could not have been non-zero in this run, for two **independently sufficient**
reasons:

1. **The scheduler never called `update_z_goal`.** The
   `ScaffoldedSD054OnboardingScheduler` as it existed on 2026-05-31 (the 621a run date)
   did not call `agent.update_z_goal` in either `_train_episode` (P1) or `_eval_episode`
   (P2), so `GoalState.update` was never reached and z_goal stayed at its zero
   initialisation on every step of every arm. The `update_z_goal` wiring amend landed
   **2026-06-02** -- *after* the 2026-05-31 run. Confirmed in `substrate_queue.json`
   amend_hint: *"...never call agent.update_z_goal, so GoalState.update is never reached
   and z_goal stays at zero-init (confirmed: zero update_z_goal matches in the module)."*
   The 621a-era scheduler commit (`1febd73`, before 2026-06-02) is the diagnose-errors
   emit_outcome fix; the post-amend module has 20 `update_z_goal` matches, the 621a-era
   module had 0.

2. **The agent was built without `z_goal_enabled`.** `build_agent`
   ([v3_exq_621a...py:124](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_621a_scaffolded_sd054_onboarding_substrate_readiness.py))
   calls `REEConfig.from_dims(...)` with `use_mech295_liking_bridge=True` +
   `use_mech307_conjunction=True` but **no `z_goal_enabled=True` and no `drive_weight`**.
   With `from_dims` defaulting `z_goal_enabled=False`, `agent.goal_state` is `None` and
   `update_z_goal` early-returns (agent.py:4791) -- so even after the 2026-06-02 wiring
   amend, the *621a config* would still produce z_goal=0. (The working reference runner
   V3-EXQ-622 sets `z_goal_enabled=True` + `drive_weight=2.0` explicitly; the 603e
   validation config had to add the same -- see CLAUDE.md "two-part fix".)

C2 therefore carries **no information** about substrate capability: it measured a
quantity that was floored to 0 by the experiment's own setup, not by any substrate
ceiling. This is the identical fault class as V3-EXQ-642 (`pred_mag` floored to 0 on a
frozen random encoder): an untrained / unwired substrate produces a degenerate
measurement that the self-route then mis-reads.

**The self-route's interpretation is doubly wrong here:** (i) the manifest reports
`overall_pass=true` (a PASS that, per the substrate-readiness-diagnostic convention,
"clears" the gate), yet the substantive criterion is false; and (ii) the C2=false it does
report is itself a precondition_unmet artifact, not a real substrate-capability signal.

---

## 5. Claim-layer mapping

- **claim_ids = [Q-045, MECH-313, MECH-260]** were inherited verbatim from the
  V3-EXQ-603c claim trio per the substrate-design memo's "What does NOT change"
  disclaimer (script docstring lines 48-52). For a **substrate-readiness diagnostic** that
  tags is debatable (the run tests substrate wiring, not those claims), but it is moot
  here: the 2026-06-01T05:50Z cycle reclassified all three to `non_contributory`
  per-claim, and the run is `scoring_excluded: diagnostic_probe`. **No claim confidence
  was moved**; `pending_retest_after_substrate` was retained on all three.
- **Q-045** (MECH-313 vs MECH-260 collapse falsifier), **MECH-313** (stochastic noise
  floor), **MECH-260** (dACC bias suppression): none were tested by this run in any
  load-bearing way, and none had their status or confidence changed. Correctly inert.
- **The experiment did not let any tagged claim express itself** (z_goal=0 means the
  whole goal->approach cascade the trio bears on never ran). Not weakened, not
  strengthened -- untested, exactly as the non_contributory reclassification records.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | z_goal=0 -> the goal/approach cascade the tagged trio bears on never ran. Correctly recorded `non_contributory`; no status moved. |
| Biological reference | n/a | Substrate-readiness wiring diagnostic, not a formal-import-vs-biology claim test. No lit-pull warranted (cf. 642). |
| Developmental / dependency prerequisites | **missing** | The goal-seeding call (`update_z_goal`) was absent from the scheduler at run time; `z_goal_enabled`/`drive_weight` unset in the agent build. Two confirmed prerequisites, both absent. |
| Implementation completeness | **stub (at run time)** | The 2026-05-31 scheduler had no z_goal seeding path; z_goal was structurally pinned at 0. Fixed by the 2026-06-02 wiring amend (+ later nursery / developmental-window / seeding-calibration / foraging-competence amends). |
| Environment adequacy | adequate-but-hard | P2 target env (`hazard_food_attraction=0.7`) starves benefit; 2/3 scaffold seeds die in P1 (3/9 survival). Real but secondary to the z_goal wiring gap. |
| Measurement adequacy | **misleading** | `overall_pass=true` with C2 (load-bearing) false; C1 baseline-inflated; C3 attributes a goal cascade on z_goal=0. The acceptance rule lets degenerate side-criteria carry the PASS. |
| Integration adequacy | **isolated** | Goal pipeline never engaged (z_goal=0), so downstream consumers (MECH-295 bridge, approach commit) could not be driven by it. |
| Scale / capacity | insufficient (budget) | P0/P1=30/30 vs 603c 100/50; seed-fragility present but not the primary cause. |

**Recommended `epistemic_category`:** none for any claim status change (claimless-in-effect
substrate-readiness diagnostic; already `non_contributory`). The run is best characterised
as a **measurement / precondition-unmet (test-design) artifact**. Do **not** record
`substrate_ceiling` on any claim from this run.

---

## 7. Governance impact and self-correction (what actually moved)

The **2026-06-01T05:50Z** governance cycle (cited at `claims.yaml` ~L19989 and ~L29286;
`substrate_queue.json` L3658):
- declared *"cleared substrate-readiness diagnostic"* and *"Clears prereq (2) of
  behavioral_diversity_isolation:GAP-C"*;
- marked V3-EXQ-621 `superseded` by V3-EXQ-621a;
- declared *"Behavioural cluster validation V3-EXQ-603d / 591b queueable"*;
- reclassified Q-045/MECH-313/MECH-260 per-claim `non_contributory` (NOT promoted);
- retained `pending_retest_after_substrate`.

The **prereq-(2)-cleared declaration was unjustified** on its face: prereq (2) is exactly
"produces non-trivial z_goal," and z_goal was 0 in the run that "cleared" it.

**The system self-corrected within ~12 hours.** The **2026-06-01T17:56Z** cycle ran the
"queueable" V3-EXQ-603d, whose autopsy found the **load-bearing** fact:
`ScaffoldedSD054OnboardingScheduler._train_episode` and the eval path *never call
agent.update_z_goal* -> z_goal zero-init for every step of every arm; the C4
z_goal=0 / SUBSTRATE_FAILURE label is a **Class-1 harness/wiring artifact (same fault as
V3-EXQ-626), NOT a substrate ceiling** -- and explicitly *"This is the true content of
621a's 'z_goal feeding not yet wired'."* The substrate was re-opened (`amend_pending`),
the update_z_goal wiring landed 2026-06-02, and a chain of further amends followed
(Stage-0 nursery, developmental window, seeding calibration, foraging-competence
residual). **`substrate_queue.ready` stayed `false` throughout** (the genuine
substrate-readiness gate is a pending full-scale run requiring `z_goal_at_contact>0.4 AND
P1 survival AND P2 contact`, each >=2/3 seeds -- `substrate_queue.json` L3775). GAP-C
remained `blocked_pending_substrate` with prereq (2) still the load-bearing blocker.

**Net:** the *evidence claim* was vacuous and the prereq-cleared *language* overclaimed,
but the *operative state* (ready=false, claims non_contributory + pending_retest, prereq
(2) still open) is already correct, and no claim confidence was corrupted. The lingering
residue is the overclaiming text in the two `evidence_quality_note` blocks.

---

## 8. Learning extracted

1. **A diagnostic acceptance rule of the form `C1 AND (C2 OR C3)` can pass with the only
   substantive criterion (C2) false**, when C1 is structurally inflated and C3 is
   vacuous. The `OR` makes a load-bearing criterion bypassable. Substrate-readiness
   diagnostics whose headline quantity is `false` should not self-route `overall_pass=true`
   -- the retrospective audit's proposed indexer detector ("flag when `overall_pass` is
   true but a load-bearing-tagged criterion is false") would have caught this.
2. **z_goal=0 here is precondition_unmet, not a substrate ceiling** -- a missing
   `update_z_goal` call + an agent built without `z_goal_enabled`. The 642 lesson recurs:
   assert the measured quantity clears its non-triviality floor (here: a Stage-0 forced-feed
   positive control producing non-zero z_goal *under the scheduler*) **before** reading the
   criterion. The 2026-06-02 amend added exactly that Stage-0 positive control -- it is
   structurally unshippable for a z_goal=0 scheduler to pass now.
3. **C1 "cells complete" must exclude by-construction baseline auto-completions** from the
   survival fraction, or report scaffolded-only survival separately. Counting baseline
   cells in both numerator and denominator inflated 3/9 to 6/12.
4. **A vacuous substrate-readiness PASS that drives a "prereq cleared" declaration is a
   real governance hazard even when the run is `non_contributory`** -- the blast radius
   here was bounded only because the immediately-queued behavioural successor (603d)
   re-exposed the fault. The clear should not have been issued from 621a alone.

---

## 9. Routing decision (user-confirmed: Contained-correction)

**Primary route: `/implement-substrate` action = `none`.** The substrate gap (missing
z_goal seeding) was already diagnosed by failure_autopsy_V3-EXQ-603d_2026-06-01, the
amend chain has landed (update_z_goal wiring 2026-06-02 -> nursery -> developmental
window -> seeding calibration -> foraging-competence residual), and the genuine
substrate-readiness gate is the pending full-scale run that `substrate_queue.ready=false`
already enforces. No new substrate task; no re-run of 621a (its substrate no longer
exists); no claim status change (already `non_contributory` + `pending_retest_after_substrate`).

**Governance-facing correction (recommended write, NOT applied here):** append a one-line
correction to the two `evidence_quality_note` blocks that cite 621a (`claims.yaml`
~L19989 and ~L29286) and to the `substrate_queue.json` 621a note (L3658):

> Correction (failure_autopsy_V3-EXQ-621a_2026-06-06): V3-EXQ-621a `overall_pass=true`
> was a VACUOUS_PASS -- the load-bearing C2 z_goal floor was FALSE (z_goal=0 across all
> 12 cells) and z_goal=0 was guaranteed by construction (the 2026-05-31 scheduler never
> called update_z_goal AND the agent was built without z_goal_enabled). The PASS rested on
> a baseline-inflated C1 (real scaffolded survival 3/9) and a vacuous C3 (approach-commit
> lift attributed to a goal cascade that cannot exist at z_goal=0). 621a did NOT actually
> clear substrate-readiness or GAP-C prereq (2); that gate remains the pending full-scale
> run (ready=false). The V3-EXQ-621 supersession stands (runner-emit_outcome-misclassification
> recovery; independent of the vacuity). The fault was confirmed and re-opened by
> failure_autopsy_V3-EXQ-603d_2026-06-01 (Class-1 harness/wiring); no claim confidence
> moved (run non_contributory / scoring_excluded).

**`evidence_direction`:** keep `non_contributory` (already correct -- no manifest edit
needed). The manifest's own `evidence_direction_note` already records C2=false; an
optional governance addition is an `adjudication: vacuous_pass` tag, but the user selected
the contained reading (no manifest annotation required).

**MECH-353 / sibling claims:** N/A.

This autopsy makes **no** claims.yaml / manifest / `evidence_direction` /
review_tracker.json / substrate_queue.json edits (analysis + handoff only; governance
applies the recommended correction interactively).

---

## 10. Cross-references

- Retrospective audit (this run is #1 priority): `evidence/planning/retrospective_diagnostic_selfroute_audit_2026-06-06.md`
- Canonical vacuous-pass / precondition-unmet analogue: `evidence/planning/failure_autopsy_V3-EXQ-642_2026-06-06.{md,json}`
- Starting-point triage (not a closure): `evidence/planning/z_goal_collapse_triage_2026-05-31.md`
- The fault's confirming successor autopsy: `evidence/planning/failure_autopsy_V3-EXQ-603d_2026-06-01.{md,json}`
- Manifest: `evidence/experiments/v3_exq_621a_scaffolded_sd054_onboarding_substrate_readiness_20260531T230932Z_v3.json`
- Script: `ree-v3/experiments/v3_exq_621a_scaffolded_sd054_onboarding_substrate_readiness.py`
- Substrate + amend chain: `ree-v3/CLAUDE.md` "scaffolded_sd054_onboarding" sections (initial 2026-05-31; update_z_goal wiring 2026-06-02; nursery / developmental-window / seeding-calibration / foraging-competence amends 2026-06-03..05).
- Substrate queue entry: `evidence/planning/substrate_queue.json` (`sd_id: scaffolded_sd054_onboarding`; ready=false; L3658 / L3489 / L3775).
- claims.yaml citation blocks: ~L19989 and ~L29286 (the two `evidence_quality_note` blocks carrying the 2026-06-01T05:50Z clear).
- Related in-flight: `evidence/planning/proposal_trivial_prediction_readiness_gate_2026-06-06.md` (generalises the trivial-prediction / overall_pass-with-failed-load-bearing-criterion detector -- 621a is the 621a-named case in that proposal).
