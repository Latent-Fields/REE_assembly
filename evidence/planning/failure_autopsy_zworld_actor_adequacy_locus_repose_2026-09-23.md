# `zworld_actor_adequacy_locus`: question re-pose and registry correction (GFLAG-0312 / GFLAG-0329 / GFLAG-0387 residual)

- **Generated:** 2026-09-23T19:53:37Z. Session `vigilant-colden-ac4766`, chip `chip-20260923-zworld-locus-repose`.
- **Status:** CONFIRMED at the Step 8 gate. The user chose the recommended option on all four questions (RECOMMENDATION_LOG `rec-20260923-a861459d`, `-6cdf6030`, `-acb6a44b`, `-aced97a9`).
- **Scope:** question-level. No run is adjudicated here, and no claim's direction or category moves. Every write goes to `hypothesis_space_registry.v1.json` (Step 9b), plus one fix to the integrity checker.
- **Machine-readable twin:** `failure_autopsy_zworld_actor_adequacy_locus_repose_2026-09-23.json`.

## 1. Headline

1. **GFLAG-0329: one defect, not two, and not back-dating.** The flag reported "3 unwitnessed legs" and "4 unaccounted legs". Both come from a single citation of a ree-v3 driver that the integrity checker could not read. All four legs were written down before V3-EXQ-1041 ran, so the Mode-C test is rejected. The flag is fixed by citing each leg's earliest witness and teaching the checker to read ree-v3 history. The audit is now b=0 for this question.
2. **GFLAG-0312: the question was mis-posed by conflation.** Its registered locus question was answered at V3-EXQ-1010. Later designs attached here because they carry the same claims, but they asked about SD-106, the fix that answer named. The question is now closed by a `growth_restriction`. The leg that still mattered is superseded here and carried to a new question, `sd106_objective_consumer_transfer`. The recurrence alarm now reads ACKNOWLEDGED.
3. **GFLAG-0387 residual: MECH-567 does not need to wait for the rotation,** under two conditions (section 5).

## 2. Facts (GFLAG-0329)

| Leg | Earliest durable witness | Date | Before the run? |
|---|---|---|---|
| H-metric-mismatch | `failure_autopsy_V3-EXQ-1023_2026-09-14.json`, outcome (1) | REE_assembly `8418b0ed762`, 2026-09-14T17:13:28Z (staging draft; confirmed unchanged 2026-09-15T01:14:02Z, `beb47bca`) | yes, by ~27 h |
| H-under-budgeted-p0a | same, outcome (2) | same | yes |
| H-mechanism-defect | same, outcome (3); the inert / below-ceiling split appears only in the driver (red-team F2) | same; driver `febce39` | yes |
| H-anchor-off-distribution | driver only, line 94 ("THE ANCHOR IS NOT REPRODUCIBLE ON THIS DISTRIBUTION -- measured while authoring") | ree-v3 `febce39` (its only commit), 2026-09-15T20:33:32Z | yes, by 2 min 33 s |

**Run start** = manifest write 2026-09-15T20:37:43Z minus `elapsed_seconds` 97.31 s = **20:36:05.7Z**. The manifest's `substrate_identity.resolved_at_utc` of 20:36:10Z corroborates it. `febce39` is an ancestor of the run's `substrate_commit` `311789f5`. The manifest is not a dry run.

**Mode-C discrimination test: REJECTED for all four legs.** Mode C is for a leg nobody anticipated before the run's own data revealed it. All four were anticipated in writing before the run. Filing them as discoveries would be the anticipated-rival escape hatch that the `discovery_growth` invariant forbids. This question's H-D leg got the same ruling on 2026-09-05, as did red-team F9 of the V3-EXQ-1041 autopsy.

**Root cause.**
- `fanout_growth_events[2]` cited the ree-v3 driver as its only source. Its own note said why: "the one document that witnesses all four".
- `check_hypothesis_space_integrity.py::_artifact_first_commit` searched only REE_assembly git. So it fell back to each leg's first commit in the registry (2026-09-16), which is after the 2026-09-15 resolution, and reported the legs unwitnessed.
- `_validate_fanout_events` rejects a whole event when any one leg fails. So all 4 legs went unaccounted, even though H-under-budgeted-p0a cleared on its own.
- The earlier 1023 witness was already named in that event's note at registration commit `bee93548e` on 2026-09-16, a day before the flag was raised. Re-pointing to it is therefore not source-shopping.

**Applied:**
- **Three legs re-pointed.** H-metric-mismatch, H-under-budgeted-p0a and H-mechanism-defect now cite the 1023 autopsy, with `pre_registered_utc` set to 2026-09-14T17:13:28Z. The prior values are kept under `pre_registration_correction`.
- **Event split.** The event is now a 3-leg event sourced to the 1023 autopsy plus a 1-leg event sourced to the driver. The original is kept verbatim under `split_from`.
  - Totals are unchanged: delta 4, `initial_frozen_count` 11, `initial_frozen_count_at_registration` 2.
  - Side effect, recorded in both events: one fan-out design now counts as two artifact-keyed portfolios, 5 in total.
- **Checker fix.** A new `SIBLING_WITNESS_REPOS = ("ree-v3",)` and `_witness_repo_for()` let `_artifact_first_commit` resolve a `ree-v3/...` source in the sibling repo. If that repo is absent, it falls back to today's behaviour and never produces a false "witnessed".
  - **Self-test.** It gains 4 discriminations on the pure router. The existing witness self-test stubs `_artifact_first_commit` wholesale, so a stubbed test would have asserted nothing.
  - **Blind spot measured on the real repos.** For the driver path the old code returns `''` and the new code returns `'2026-09-15'`. The REE_assembly path is unchanged at `'2026-09-14'`. A nonexistent ree-v3 path returns `''` under both.
  - **Tests.** `--self-test` passes, and `test_build_hypothesis_space.py` plus `test_check_hypothesis_space_ledger_pending.py` pass (26 tests).
- **H-anchor-off-distribution note.** Its `pre_registration_witness_note` records the cross-repo witness. It also records that the leg is a **measured fact**, known true before the run, that nothing discriminated.

## 3. The re-pose (GFLAG-0312)

**The registered question** asks where the SHIPPED encoder's actor-adequacy deficit lies. V3-EXQ-1010 answered it:

| Leg | Result | Run |
|---|---|---|
| H-B, consumer learning | eliminated | V3-EXQ-1002 |
| H-E, channel-input width | eliminated | V3-EXQ-1008 |
| H-D, warmup | confirmed not the locus | — |
| H-C, geometry | split: about a third of the gap | — |
| H-F, content discarded at encode | confirmed | V3-EXQ-1010 |

The registry's own synthesis block said "fully resolved and the locus is named", and `decidable` was true.

**What attached afterwards** did so by Step 9b's claims+theme matching: every design carries MECH-457 and INV-088. But these designs asked two OTHER questions about SD-106, the repair that H-F motivated:

- **(i) Readout comparability.** The V3-EXQ-1041 grid, with legs metric / budget / mechanism-defect / anchor. It asks whether SD-106's preservation readout is comparable to its design anchor. This is on the encoder plane, and all of it is resolved.
- **(ii) Transfer.** The V3-EXQ-1041 autopsy portfolio, with legs transfer-amplification / which-directions. It asks why SD-106's trained objective does not reach the consumer. In V3-EXQ-1023a, 3.3x the steps bought +0.1184 held-out R^2 but only +0.0081 agreement.

A locus partition cannot carve a transfer phenomenon. That is exactly what `h_other_events[0]` recorded on 2026-09-17. So the recurrence (2 legs growing to 11 across 4 designs) is the footprint of this conflation: 6 of the 9 grown legs belong to (i) and (ii).

*Red-team correction:* my first draft called all 6 of those legs "transfer". Only (ii) is. Portfolio 3 is readout comparability, and H-which-directions is itself locus-shaped for SD-106's code.

**Precedent confronted.** `failure_autopsy_V3-EXQ-1041_2026-09-16` opened a standalone question for these legs, then withdrew it at its gate, because that draft booked zero growth here. That was a dodge of the growth accounting. This re-pose is different: every leg and all growth stay booked on this question, and the split applies only going forward.

**Applied (user-ratified):**
- **`growth_restriction`: closed to further fan-out.**
  - Transfer legs go to `sd106_objective_consumer_transfer`. Any other SD-106 or z_world question pre-registers its own qid.
  - Resolving legs already registered here stays permitted.
  - One sanctioned exception: a leg that localises H-F's content loss to a named layer of the shipped observation->z_world path.
- **H-which-directions: superseded.** The shape follows the precedents in `policy_decomposition_discrimination` and `mech467_legc_event_denominator_cause`.
  - `control_passed` stays true, because it records V3-EXQ-1023a's passed controls rather than a new adjudication.
  - `met_elimination_bar` is false, and the prior resolution is preserved.
- **New question `sd106_objective_consumer_transfer`.** Its claims are SD-106, MECH-567 and MECH-566. It has two alive legs, registered before any run (Mode A):
  - **H-which-directions-sd106:** SD-106 keeps generic variance but not the decision-relevant directions. Axis: representation.
  - **H-target-absent-mech567:** the objective carries no term whose target is the consumer's target. Axis: learning-signal. Its nulls are taken verbatim from MECH-567's `what_would_answer`.

  Both legs are adjudicated by the not-yet-queued MECH-567 experiment. They are **nested, not exclusive**: MECH-567 names the mechanism, and which-directions is the phenomenon.

  MECH-566 is listed for routing only. V3-EXQ-1065 narrowed it without opening a leg: its ZCA member was falsified, and its standardisation member *is* the baseline.
- **Refreshed stale blocks.** `synthesis`, `decision` and `fanout_growth_note` were refreshed; they still described H-F as ALIVE and the V3-EXQ-1010 sweep as NOT YET QUEUED. `decision_log_ref` stays null, because a human owns "decided".
- **H-other event annotated, not rewritten.** `h_other_events[0].repose_disposition` was appended.

**Rotation (user decision).** The question side of the rotation is discharged here. The claim side is **still owed**: the `/claim-synthesis` on MECH-457/INV-088 that `h_other_events[0]` routed has not run. CDQ-010 was a convergence intake that fed this re-pose. It was not that synthesis.

**Provenance gap noted.** The event's `source` artifact (`failure_autopsy_V3-EXQ-1023a_2026-09-17`) contains no H-other text. The event was written directly into the registry by `eeeb0550ed5`.

**GOV-ROTATE-1 note (for governance; this artifact adjudicates nothing about it).** Before the rotation, the next step on this lineage was a full re-run of the v3_exq_1010 decoder ladder. The rotated framing produced V3-EXQ-1065 instead: a 183-second pre-registered post-hoc falsifier on an existing frozen code. That is a candidate instance of GOV-ROTATE-1's build-discipline test.

## 4. Audit after the edit

`check_hypothesis_space_integrity.py`: **a=0, b=0, d=0.**
- The two **c** items are `mech467_legc_event_denominator_cause` H-commitment and H-cadence. They were already there, and they are GFLAG-0404, owned by `eloquent-lichterman-824f74`.
- All 11 legs of this question are git-witnessed.
- The recurrence is **ACKNOWLEDGED**.
- This question's H-other CANDIDATE and stale-synthesis signals have cleared.
- The new question raises no flag.

Before this edit the audit read b=2: 3 unwitnessed legs and 4 unaccounted.

## 5. MECH-567 (GFLAG-0387 residual)

**Answer (user decision): the build does not need to wait for the rotation.**

The 2026-09-17 ordering constraint forbids a rescue run on a *surviving leg of this question*. MECH-567 is not that. It is a new mechanism from the transfer framing. The one leg a MECH-567 run would in effect settle, H-which-directions, is now superseded here and carried to the transfer question. The build is registration-only (`proposed_REGISTRATION_ONLY_not_a_build_authorisation`).

**Conditions:**
1. The run is adjudicated against `sd106_objective_consumer_transfer`, whose legs are already pre-registered, and never against this question.
2. It is read on held-out episodes, with MECH-567's mandatory grounding-head co-measurement. Any co-train arm also needs the participation-ratio degeneracy pre-check. An oracle-action head scored on oracle-action agreement comes close to training on the DV.

## 6. Pre-routing checks and red-team

**Step 7b.** No fires. C1, C2 and C3 were inapplicable because there is no claim-keyed target. C5 was inapplicable because no sibling `.md` existed at check time.

**Step 7c.** The red-team ran on **fable** (claude-fable-5-1), a different model from the drafting session (Opus 5.5). Verdict: **CONTESTED**, on two recommendation-level defects, both fixed at the gate:

- **D1.** A growth_restriction that leaves H-which-directions alive can never acknowledge the recurrence, because `_recurrence_acknowledged` requires `alive == 0`.
- **D2.** "Pre-register MECH-567's legs before the run" could not be satisfied while the new question's registration was deferred.

Every GFLAG-0329 fact was re-derived independently. The red-team also re-ran the checker simulation of the correction and got the same result. All eight hygiene items were applied (listed in the JSON).

## 7. Coupling and hand-off

- **GFLAG-0404 coupling.** The superseded leg here carries `control_passed: true`, so it does not add to GFLAG-0404's open question (ratified dispositions without a passed control). If that session changes rule (c), this supersession should be re-read under the new rule.
- **For `/governance`:**
  - Resolve GFLAG-0312 and GFLAG-0329 on reading this artifact.
  - Chip: (a) `/claim-synthesis` on MECH-457 / INV-088, the claim-side rotation that is still owed. (b) When the MECH-567 build is authorised, a `/queue-experiment` whose interpretation grid names both `sd106_objective_consumer_transfer` legs and carries the section 5 conditions.
  - This session spawns nothing from its own routing (Step 8 rule).

## 8. Learning extracted

- **Answered questions attract follow-on legs.** Step 9b matches an existing question by claims+theme. When a question's answer names a build, later questions *about that build* match the same claims and land on the answered question, inflating it. The fan-out recurrence overlay caught this, but only four portfolios late.
- **Trace a violation count to its mechanism before treating it as several defects.** Here, one cross-repo citation looked like three back-dated legs and four unaccounted ones.
- **A growth_restriction alone does not close a recurrence while any leg is still alive.** That leg has to be resolved or superseded first.
