# SD-PP-B5 inverted-action-map ratio: the "~1.0" bar is confounded by battery-difficulty nuisance

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry). No experiment was queued and no EXQ id was consumed.**

- Raised by: `metaworker-science-20260924-orchb-sdppb5-inverted-map` (headless science worker, campaign `science-20260924-orchb-sdppb5-inverted-map`), 2026-09-24
- Chip: `chip-20260924-sdppb5-inverted-map-probe` (unclaimed and left OPEN; not resolved)
- Decision chip: `chip-20260924-sdppb5-invmap-ratio-bar-decision`
- Subject: `failure_autopsy_V3-EXQ-1082_2026-09-24.json` `targets[0].fanout_recommendation.suggested_probes[0]`
- Bears on: SD-PP-B5-z-world-per-step-displacement-range, MECH-573
- Reserved-but-unused id: none consumed. `V3-EXQ-1092` was verified free and claimed as a slot reservation only.

## 1. What I was asked to queue

The confirmed V3-EXQ-1082 autopsy routes one cheap measurement probe (verbatim from
`suggested_probes[0].sketch`):

> OFF-only head, live reset-on-done battery, 3 seeds, TWO arms alpha_world 0.3 and 0.9 in one run:
> inverted-action-map battery MSE / original MSE **with a bar excluding the degenerate ~1.0**
> (reuse 1079's `_make_env(invert_action_map=True)` and
> `experiments/_lib/action_sensitivity_gate.readiness_verdict`), beside d_act and skill_vs_identity.

Declared null: *"at 0.9 the ratio stays <= ~1.0 despite d_act > 0 ..., or the 0.3 and 0.9 arms do not differ."*

Every premise in the pre-flight checked out against live source (see section 5). The design is
ratified and buildable. I stopped on ONE thing: **what the bar is measured against.**

## 2. The defect: a cross-battery ratio has a nuisance term, and its null is not 1.0

`readiness_verdict` supports two forms, and they have *different* nulls:

| form | how it is built | correct null | why |
|---|---|---|---|
| `action_shuffle_ratio` (SD-031 form, `counterfactual_battery=None`) | **SAME rows**, actions permuted in place | **1.0, exactly** | the row set is identical, so intrinsic transition difficulty cancels by construction |
| `battery_pair_ratio` (V3-EXQ-1073 form, `counterfactual_battery=cf`) | **TWO DIFFERENT batteries**, one collected in an inverted-action-map env | **not 1.0** -- it is the action-blind ratio | the two row sets have different intrinsic |dz|, which moves the ratio with no action-reading at all |

The autopsy asks for the **second** form (an inverted-map *env*, `_make_env(invert_action_map=True)`)
but keeps the **first** form's bar (`~1.0`, i.e. `RATIO_FLOOR = 1.0`). That is the conflation.

The nuisance term is already measured. V3-EXQ-1079 records it per cell as
`blind_null_1075_order` = `identity_predictor_mse(cf)/identity_predictor_mse(orig)` on the
**same battery pair** as `ratio_1075_order` -- an action-blind predictor's ratio over those two row
sets. If the head merely tracked battery difficulty, its ratio would land there, not at 1.0.

## 3. On recorded data the two bars disagree on 6 of 9 cells -- and invert the routing verdict at alpha 0.9

From the landed V3-EXQ-1079 manifest
(`v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3.json`,
substrate_hash `17e203f335387880` -- the same hash 1082 ran on):

| cell | `ratio_1075_order` | `blind_null_1075_order` | verdict, bar = 1.0 | verdict, bar = blind null | agree? |
|---|---|---|---|---|---|
| ALPHA_0.3 s42  | 0.8336 | 0.5632 | blind | **READS** | FLIP |
| ALPHA_0.9 s42  | 0.9303 | 1.1756 | blind | blind | agree |
| ALPHA_1.0 s42  | 1.1081 | 1.1901 | **READS** | blind | FLIP |
| ALPHA_0.3 s123 | 0.8790 | 0.5824 | blind | **READS** | FLIP |
| ALPHA_0.9 s123 | 1.2563 | 1.3181 | **READS** | blind | FLIP |
| ALPHA_1.0 s123 | 1.2586 | 1.3357 | **READS** | blind | FLIP |
| ALPHA_0.3 s456 | 0.7068 | 0.5063 | blind | **READS** | FLIP |
| ALPHA_0.9 s456 | 1.2755 | 1.0826 | READS | READS | agree |
| ALPHA_1.0 s456 | 1.1626 | 1.0948 | READS | READS | agree |

**At alpha 0.9 -- the arm the declared null is about -- the bars route oppositely:**

- bar = 1.0: 2 of 3 seeds READ (s123 1.2563, s456 1.2755) -> "the head reads its action" -> **PASS**
- bar = blind null: 1 of 3 seeds READS (s456 only) -> "does not clear its action-blind baseline" -> **FAIL**

The autopsy's own `routing_note` says what a PASS here licenses: *"on a pass at 0.9 the V3-EXQ-1073
MECH-572 contradiction design re-posed at alpha 0.9 becomes posable."* So the bar choice decides
whether an expensive downstream contradiction build is authorised.

This is the precise hazard `action_sensitivity_gate.py`'s own docstring is written against -- it is a
NEGATIVE INSTRUMENT that "authorises STARTING work on the strength of a negative". Gating it at 1.0
in the cross-battery form can return `status: "ready"` for a head whose ratio sits *below* what an
action-blind predictor achieves on the same two row sets.

**Caveat, stated rather than hidden:** these are 1079's **post-death** batteries (the 1075/1079
collector never read `done`), and the probe under discussion uses 1082's **live** reset-on-done
collector, so the *numbers* will differ. The finding is structural, not numeric: a cross-battery
ratio carries a difficulty nuisance whatever the rows, and `blind_null` is its measured size. The
6-of-9 table shows the nuisance is large enough to flip verdicts in practice, not that these
particular values will recur.

## 4. Why this is a STOP and not an authoring choice

Under the campaign's consent rule, seeds / episode counts / logging are mine; **criteria, the
falsifier, and what the evidence licenses are not.** Choosing the bar changes the pre-registered
criterion and flips the run's PASS/FAIL at the arm of interest, so it is the user's call.

Note also that **no artifact in this lineage has ever routed on this ratio.** V3-EXQ-1073 measured
it and self-routed `confidently_wrong_condition_unposeable_on_this_head`; V3-EXQ-1079 recorded it
and its own interpretation block states the ratio "and its nulls ... are RECORDED and do not gate"
(driver line 759). The autopsy is promoting a never-routed recorded statistic to the routed DV --
which is reasonable, but it is exactly when the bar has to be right.

## 5. Premises re-measured (all held)

Checked against live `ree-v3` main, per CLAUDE.md's premise-audit rule:

- `alpha_world`: `REEConfig.from_dims` param default 0.3 (`ree_core/utils/config.py:7635`), threaded
  at `:9029`. 1079's `_build` asserts it landed (`RuntimeError("from_dims did not thread alpha_world")`).
- `_make_env(seed, invert_action_map=True)` exists at `v3_exq_1079...py:258-267`; it swaps actions
  0<->1 and 2<->3 and preserves indices > 3.
- `experiments/_lib/action_sensitivity_gate.py`: `readiness_verdict` L249, `battery_pair_ratio` L224,
  `action_shuffle_ratio` L167, `MIN_ROWS=16`, `MIN_DISTINCT_ACTIONS=2`, `RATIO_FLOOR=1.0`,
  `SKILL_FLOOR=0.0`, plus a three-valued `cannot_determine` and a `CANARY_V3_EXQ_1073` -- a
  well-built negative instrument; the gate itself is not the problem, the bar it is handed is.
- 1082's live reset-on-done collector `_collect_live_battery` at `:292-333`; OFF cells recorded
  `battery_n_postdeath_rows: 0`, 512 rows, 5 distinct actions, d_act 0.3415/0.2160/0.2266 with CI>0
  on 3/3 -- so `d_act > 0` in the declared null is real and the DV is not floor-pinned.
- Governance flags: none of the 16 currently-open items in `governance_flags.v1.json` (origin)
  names SD-PP-B5, MECH-573 or V3-EXQ-1082. GFLAG-0454 matches the string "inverted" but is SD-081
  familiarity AUC, unrelated. No open user design gate blocks this work.
- Not duplicated: no inverted-action-map SD-PP-B5 probe in the queue (`V3-EXQ-1067/1083/1089`) or in
  `experiments/`; `V3-EXQ-1092` free across queue, script tree and git log.
- GOV-REUSE-1 (Step 2.4): the decisive readout is **partially** recorded and **not** recoverable.
  1079 has the ratio at both alphas but on post-death rows; 1082 has the live battery but no ratio
  (its autopsy says the readout "is still unmeasured at 0.9"). Deriving it post hoc is impossible --
  it needs a live inverted-map battery, which needs a run.
- Re-derive brake (Step 2.5b): does not hold. `claim_ids: []`, a new EXQ *number* not a lettered
  re-run, `experiment_purpose: diagnostic`, and the confirmed autopsy is itself the producer-half
  that routes this probe to `/queue-experiment`. GOV-DIAG-1 counts the full SD-PP-B5 token at 2
  (1079 + 1082), below N=3, and the autopsy notes the chain "is converging ..., not circling".

## 6. The options

**(A) Literal -- gate on raw cross-battery ratio > 1.0**, exactly as the sketch reads.
Faithful to the ratified text. Risk: the section-3 aliasing; at 0.9 it would likely PASS on a head
below its action-blind baseline on 2 of 3 seeds, and that PASS authorises the MECH-572 contradiction
re-pose.

**(B) Nuisance-corrected -- load-bearing criterion is `ratio > blind_null` on the same battery
pair**, with the raw ratio and the raw `>1.0` verdict both RECORDED so the autopsy's literal declared
null stays evaluable and the artifact stays comparable to 1073/1079. Same DV, same manipulation, same
helpers; only the bar is denominated correctly.

**(C) Both forms (recommended) -- (B) plus the same-rows `action_shuffle_ratio`.**
`readiness_verdict(..., counterfactual_battery=None)` computes the shuffle form on the SAME rows,
where `RATIO_FLOOR = 1.0` *is* the correct null and needs no second battery and no nuisance
correction. Record all three -- shuffle-form verdict, cross-battery raw, cross-battery vs blind null
-- and declare ONE load-bearing. This is a superset of (A) and (B) at near-zero extra compute, and it
gives the autopsy's "~1.0 bar via readiness_verdict" a form in which that bar is exactly right.

**Recommendation: (C), with the same-rows shuffle-form verdict as the load-bearing criterion and the
cross-battery pair reported against its blind null.** Reason: it honours the autopsy's chosen
instrument and its 1.0 bar in the one form where 1.0 is the true null, keeps the inverted-map env
readout the autopsy actually asked for, and cannot return "ready" off a difficulty artefact. If only
one bar may be kept, (B).

A fourth option exists and I do **not** recommend it: re-collect the counterfactual battery with
row-matching (same z0/action sequence, inverted-map successor) so the nuisance cancels. It is the
cleanest fix in principle but it is a new collector, not a composition of 1079 and 1082, and it
exceeds what this chip authorises.

## 7. What I did not do

- No EXQ id consumed, no queue entry, no experiment script. `V3-EXQ-1092` was only slot-reserved.
- No edit to the autopsy, `claims.yaml`, `substrate_queue.json` or `experiment_proposals.v1.json`.
- The science chip is left OPEN and unclaimed so a later cycle can resume once the bar is chosen.

---

# ADDENDUM 2026-09-24 (second stop): option C was implemented, and its LOAD-BEARING criterion turns out to be already answered by landed data

**Status: AWAITING USER REVIEW. V3-EXQ-1092 was NOT queued. The script is on `ree-v3` main but is INERT (no queue entry) and must not be queued as written.**

The user chose **option C** (2026-09-24, via orchestrate-20260924-b): load-bearing = the same-rows
`action_shuffle_ratio` verdict at `RATIO_FLOOR=1.0`; the cross-battery inverted-map ratio, its raw
`>1.0` verdict and its action-blind null RECORDED but never gating. That was implemented in
`ree-v3/experiments/v3_exq_1092_sdppb5_inverted_action_map_alpha_operating_point.py`
(`43fb9e9f75`), which passes `validate_experiments --strict` (1 OK, 0 warnings of any kind),
`validate_recording --strict` (complete), and a full-budget dry run (2 seeds x 2 arms, rc=0, PASS).

The mandatory Step 4.5 adversarial red-team (Fable, foreground, one pass) returned **BLOCKING**.
Every claim below was then re-verified by this session directly against the source and the landed
manifests -- they are confirmed, not taken on the reviewer's word.

## F1 (BLOCKING, confirmed): the shuffle-form ratio clause IS `d_act > 0` restated, and the 0.9 arm is a bit-exact replay of V3-EXQ-1082

`d_act := (S - T)/(S + T)` where `T = sum(per_row_se_true)` and `S = sum(per_row_se_swap_mean)`
(the per-row mean over all alternative actions). Therefore `(1 + d_act)/(1 - d_act) = S/T`
**identically** -- it is algebra, not an empirical finding. And the gate's random derangement
draws each row's replacement action ~uniformly from the 4 alternatives, so the measured
`shuffle_ratio` estimates that same `S/T`. Measured on the dry-run manifest:

| cell | shuffle_ratio (1 draw) | 16-draw mean | S/T | (1+d)/(1-d) | d_act |
|---|---|---|---|---|---|
| 0.3 s42  | 1.4875 | 1.5305 | 1.5324 | 1.5324 | 0.2102 |
| 0.9 s42  | 1.9789 | 2.0473 | 2.0371 | 2.0371 | 0.3415 |
| 0.3 s123 | 1.3015 | 1.2775 | 1.2741 | 1.2741 | 0.1205 |
| 0.9 s123 | 1.5603 | 1.5397 | 1.5512 | 1.5512 | 0.2160 |

So `shuffle_ratio > 1.0` <=> `d_act > 0`. Consequences:

1. **The declared null N1 is self-contradictory under option C.** "At 0.9 the ratio stays <= ~1.0
   *despite d_act > 0*" was a real null for the CROSS-BATTERY form (different row sets -- 1073
   measured 0.760/0.901/0.881 with positive d_act). For the same-rows form it cannot happen: the
   ratio clause fails only if d_act <= 0.
2. **The 0.9 arm is a bit-exact replay of V3-EXQ-1082's ARM_OFF.** Verified: `battery_hash`
   `02ab0ea563a9f764` (s42) and `63f4eda43ca7ad0b` (s123) are identical in both manifests;
   `d_act` agrees to all 17 digits (0.3414696952878022 / 0.21604278160114015); `skill_vs_identity`
   identical; `per_row_se_true` lists identical element-for-element. Same cell, different machine,
   different substrate_hash.
3. **C1's answer for ALL THREE seeds is computable from 1082's landed manifest by one division**,
   including the seed the dry run never reached:

   | seed | S/T from 1082 ARM_OFF | skill from 1082 | C1 "ready"? |
   |---|---|---|---|
   | 42  | 2.0371 | +0.3486 | yes |
   | 123 | 1.5512 | +0.2194 | yes |
   | 456 | 1.5858 | +0.2149 | yes |

   C1 = 3/3 before the run starts, so the queued outcome is fixed at PASS and the pre-registration
   is post hoc relative to data already on origin.

**This is a GOV-REUSE-1 (Step 2.4) hit that the original check could not have caught.** The Step
2.4 analysis in section 5 above is still correct *as run*: it tested the CROSS-BATTERY ratio, which
was the load-bearing DV at the time, and that quantity genuinely is not recoverable (1082 collected
no inverted-map battery). Option C moved the load-bearing criterion to the same-rows form, and the
check was not re-run against the new criterion. **The lesson is specific and worth recording: when
a decision moves which statistic is load-bearing, Step 2.4 must be re-run against the NEW
statistic -- a recoverability verdict is a property of the criterion, not of the experiment.**

## F2 (confirmed): C2's alpha contrast is a property of the BATTERY, not of the head's action read

alpha_world is the EMA coefficient (`z_world = a*z_inst + (1-a)*z_prev`), so it changes the
displacement scale and structure -- and every reader's d_act moves with it, including the
closed-form ridge positive control:

| seed | head d_act 0.3 -> 0.9 (delta) | ridge PC 0.3 -> 0.9 (delta) | head delta - PC delta | head/PC @0.3 | @0.9 |
|---|---|---|---|---|---|
| 42  | 0.2102 -> 0.3415 (+0.1312) | 0.2754 -> 0.4245 (+0.1490) | **-0.0178** | 0.763 | 0.805 |
| 123 | 0.1205 -> 0.2160 (+0.0955) | 0.2310 -> 0.3379 (+0.1068) | **-0.0113** | 0.522 | 0.639 |

The head's contrast is *smaller* than the action-aware ceiling's. So a C2 PASS supports "z_world's
displacement is more action-explainable at 0.9 for ANY reader", not "the head reads its action
better at 0.9" -- which is what the label and combination_rule attribute it to. V3-EXQ-1079 carried
exactly this attribution rule (a PC contrast, and a label split conditioned on it, 1079 :84-91,
:755-758) and V3-EXQ-1092 as written drops it.

Also: the driver's DV-symmetry paragraph argues "d_act moves with alpha, therefore alpha is not a
pure rescaling". That inference is invalid for a head **retrained per arm**: identity MSE differs
9.5x / 9.4x and rms |dz| 3.08x / 3.06x across the arms, and at 0.3 the trained head's skill is
NEGATIVE (-0.106 / -0.265, i.e. worse than copy-the-input), so d_act at 0.3 is diluted by a fixed
LR/step budget against a 9x smaller target rather than by the encoder's action content.

## F3 (confirmed): one verdict label is false in the only state it can fire

`action_read_absent_at_operating_point_despite_d_act` fires when no valid seed reads at 0.9. By F1
the ratio clause cannot fail while d_act > 0, so that branch is reachable only via the skill clause
-- i.e. with `ratio > 1` and `d_act` CI > 0, a head that demonstrably DOES read its action. Both
0.3 cells in the dry run are that exact shape: `status=action_blind`, `reason: skill -0.1057 <= 0`,
`ratio=1.4875`, `d_act` CI [0.196, 0.225]. The label would assert "read absent" about a reading
head. (Lower severity: a finite CI containing 0 and an unpairable contrast both land on
`..._alpha_contrast_undetermined`, so "N2 measured to hold" and "N2 not testable" are not
distinguished unless NO seed aligns.)

## Verified and NOT findings

Row pairing for C2's joint bootstrap is sound (both arms share env seed and battery rng; the env
sees only the action, and `battery_mean/max_world_state_norm`, `n_resets` and `done_causes` are
bit-identical per seed, so the `acts_hash` check is adequate). The positive control is a different
head, so it certifies the battery rather than itself. A failing control routes to
`substrate_not_ready_requeue`, never to a substrate verdict. The recorded cross-battery ratio's
confound is acknowledged and its blind null recorded.

## Incidental result worth keeping: on a LIVE battery the section-3 aliasing does NOT bite

The dry run measures `cross_blind_null` at **0.949 / 0.958** -- BELOW 1.0 -- in every cell, and the
raw `>1.0` bar and the blind-null bar AGREE on both seeds (`bars_agree=True`). The 1.09-2.41 blind
nulls in section 3 were an artefact of 1079's POST-DEATH rows, exactly as section 3's caveat
predicted. This does not retire GFLAG-0470 -- the bar still has to be denominated correctly, and
agreement on two seeds of a live battery is not a general guarantee -- but it does mean option B's
correction is cheap insurance rather than a verdict-flipping change on live data.

## Options (no third decision chip will be raised; see "two stops means stop")

**(1) Switch the load-bearing criterion to the CROSS-BATTERY ratio vs its action-blind null
(i.e. the original option B), and add 1079's PC contrast for C2 (RECOMMENDED).**
This is the one variant that measures something not already on origin: 1082 collected no
inverted-map battery, so neither the cross-battery ratio nor its blind null is recoverable at any
alpha on a live battery. It also restores the head-vs-ceiling attribution F2 says C2 needs. The
same-rows shuffle verdict stays RECORDED (it is free, and it is the quantity that is comparable to
1082). Cost: a criterion edit to an already-written, already-validated driver; no new collector.

**(2) Do not run it; emit a REANALYSIS artifact instead.** F1 shows C1 is fully recoverable from
1082's landed per-row errors, so `reanalysis_query.py emit` can settle "does the OFF head read its
action at 0.9 on a live battery" for all three seeds at zero compute, citing 1082's run_id. This
discharges the shuffle-form question honestly and leaves the inverted-map question open for (1).
Note (1) and (2) are complements, not alternatives.

**(3) Queue it as written.** Not recommended: the outcome is fixed at PASS, C1 re-derives landed
data, the PASS label names an "inverted-map readout" that never gates, and F3's label is false in
the state it fires. This spends ~35 min of cloud compute to restate 1082.

**Recommendation: (2) now for the recoverable half, then (1) for the genuinely unmeasured half.**
Both are the user's call: each changes which statistic is load-bearing, which is the same class of
decision as the first stop.

## Second stop, and the staleness finding it implies

This is the SECOND stop on `chip-20260924-sdppb5-inverted-map-probe`. Per the campaign's "two stops
means stop", no third decision chip will be raised, and the finding is recorded instead: **the
1082 autopsy's `suggested_probes[0]` is internally inconsistent, not merely under-specified.** It
pairs the cross-battery inverted-map *manipulation* with the same-rows form's *bar* (~1.0) and with
a declared null ("ratio <= ~1.0 despite d_act > 0") that is coherent only for the cross-battery
form. Whichever form is chosen, one of the three parts does not fit: choose the cross-battery form
and the bar is mis-denominated (stop 1); choose the same-rows form and the null is self-contradictory
and the criterion is already answered (stop 2). The pre-flight rated this GREEN with "Unratified
scientific choice: None found", which was wrong in both directions. That, rather than either
individual bar question, is the finding worth carrying back into how fanout probes are specified.
