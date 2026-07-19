# Failure Autopsy -- V3-EXQ-778h (SD-068 REM unpaired-null, anchor-fix re-run)

- **Generated (UTC):** 2026-07-19T11:26:39Z
- **Scope:** single
- **Status:** confirmed
- **Target:** `v3_exq_sd068_rem_unpaired_null_anchorfix_diagnostic_20260718T183746Z_v3`
- **Queue ID:** V3-EXQ-778h (`supersedes` V3-EXQ-778d / `v3_exq_sd068_rem_unpaired_null_diagnostic_20260718T124216Z_v3`)
- **Claims:** SD-068, MECH-168, INV-047, MECH-169
- **Outcome:** PASS (diagnostic), self-route `rem_clamp_artifact_confirmed_but_readout_still_content_free`
- **Adjudicated leg:** `H-rem-clamp-artifact` (axis `measurement`), question `consolidation_readout_validity`
- **Why autopsied:** decision-routing diagnostic PASS surfaced by `/governance` Step 1.5a -- it adjudicates a
  pre-registered ledger leg and bears on SD-068 instrument validity. Invoked INLINE from the governance
  cycle (route A) under claim `silly-jepsen-926d36`.

---

## 1. Facts reconstruction

Recording provenance is **complete** -- `validate_recording.py` reports 0 always-core gaps
(`recording_schema: rec/v1`, `substrate_hash 41940642...`, `machine ree-cloud-2`,
`machine_class linux-x86_64-py3.10`, full `config`, explicit 8-seed list, `elapsed_seconds 414.15`).
No recording-debt; the `substrate_hash` is present, so any substrate-level reading here is falsifiable.

Three arms (`INJECTED`, `NULL_ZERO`, `NULL_UNPAIRED`) over sigma grid `[0.0, 0.25, 0.5, 1.0, 2.0]`,
8 seeds, `null_slope_ratio_ceiling = 0.25`.

| Criterion | Role | Result | Detail |
|---|---|---|---|
| C1 `unpaired_null_derails` | **LOAD-BEARING** | **PASS** 7/8 | `n_seeds_derailed = 7`; clamp_frac `[0.0, 0.0, 0.0, 0.2, 0.0, 0.6, 0.2, 0.2]`; unclamped sigmas `[5, 5, 5, 4, 5, 2, 4, 4]` |
| C2 `unpaired_ratio_content_contingent` | discriminator | **FAIL** 1/8 | `n_seeds_content_contingent = 1`; unclamped ratios `[0.995, 0.901, 0.877, 0.0011, 0.577, 85.18, 0.574, 3.295]` vs ceiling 0.25 |
| C3 `anchor_reproduces_778c` | readiness anchor | **PASS** 8/8 | `railed_frac = 1.0` (5 saturation, 3 positivity_floor_collapse) vs the >= 75% bar |

**Expected vs observed.** The design expected that fixing the readiness-anchor specification and
using an unpaired-target null (the Bar et al. 2020 "same odour, no prior pairing" analog) would let
the REM readout show content-contingency once the 1e-3 positivity clamp no longer railed the series.
Observed: the clamp artifact is confirmed real (C3 reproduces 778c's railed signature on every seed;
C1 shows the unpaired null does leave the rails), but with the artifact removed the readout **still
does not track content** -- the median unclamped `null_slope_ratio` is ~0.89 against a 0.25 ceiling,
i.e. the null series tracks corruption essentially as strongly as the injected-content series does.

**Failed criterion class:** discrimination (C2). The absolute/readiness criteria (C1, C3) passed --
the classic "negative control passes, discrimination fails" shape, here landing on *measurement*
rather than substrate.

### 1b. Analysis defect found in C2's interval (does not change the conclusion)

The manifest reports `ceiling_inside_ci95: True` (mean 11.55, sd 29.77, CI95 `[-9.078, 32.179]`),
which reads as "underpowered, cannot conclude". **It is not.** That interval is computed over **all 8
seeds**, but seed index 5 (`7777`) is exactly the seed that **failed C1's de-rail predicate**
(`clamp_frac 0.6` > the 0.2 ceiling, and 2 unclamped sigmas < the 3-point minimum). A seed that did
not de-rail has no business inside a statistic defined on the de-railed subgroup, and it contributes
the entire 85.18 outlier that inflates the interval.

Restricting to the 7 C1-passing seeds: ratios `[0.995, 0.901, 0.877, 0.0011, 0.577, 0.574, 3.295]`
-- **6 of 7 remain above the 0.25 ceiling**, median ~0.877. The conclusion is therefore *tighter*
than the manifest's own interval suggests, not weaker. This is an instrument-hygiene defect in the
harness's C2 aggregation, not a reason to withhold adjudication.

---

## 2. Claim-layer mapping

All four tagged claims are correctly tagged (the tags are inherited from the 778-series REM lineage
and remain accurate -- this run tests the SD-068 consolidation-phase readout that MECH-168 / MECH-169
/ INV-047 depend on for their evidence).

The critical layer distinction: **this result constrains the REM READOUT, not the claims' mechanisms.**
A content-free readout means the instrument cannot see whether REM consolidation preserves content --
it does not mean REM consolidation fails to preserve content. Nothing here licenses a mechanism-level
demotion of SD-068, MECH-168, MECH-169 or INV-047.

---

## 3. Biological-reference triage

- **Closest reference mechanism:** targeted memory reactivation with an unpaired-cue control
  (Bar et al. 2020) -- present a cue that was never paired with the to-be-consolidated content and
  verify the consolidation readout does *not* respond to it.
- **Is this a formal-definition import?** No. The unpaired-target null is a faithful translation of a
  real experimental control, not a formal-theoretic construct. `lit_status: present`.
- **Divergence:** none at the design level. The design is biologically correct; the failure is that
  REE's REM readout channel (`calibration_error` slope vs sigma) is not a content-sensitive measure
  in the first place, so a correct control cannot rescue it.
- **Does the failure resemble a missing biological dependency?** No -- it resembles recording from the
  wrong channel. The biological analog would be measuring a global arousal index and concluding
  nothing about memory content.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | The claims could not express themselves through this readout; no mechanism-level pressure either way. |
| Biological reference | clear | Bar et al. 2020 unpaired-cue control; faithfully translated. |
| Prerequisites / dependencies | present | The anchor-spec fix verifiably took effect (C3 8/8). |
| Implementation completeness | complete | The null arm is correctly implemented; this is not a wiring gap. |
| Environment adequacy | adequate | Sigma grid spans the railed and unrailed regimes. |
| **Measurement adequacy** | **misleading (DOMINANT)** | The REM `calibration_error` slope responds to corruption magnitude irrespective of content. De-clamping revealed that the clamp was masking a readout that was already content-free. |
| Integration adequacy | coupled | Arms are arm-identical apart from the manipulated factor. |
| Scale / capacity | adequate for the median reading | 8 seeds supports the median conclusion; the CI is thin and mis-subgrouped (section 1b). |

**Recommended `epistemic_category`:** `measurement_gap` -- matching its three siblings in
`failure_autopsy_SD-068-rem-fanout-cluster_2026-07-18`.

---

## 5. Re-derive brake (MOVE-3)

**Does NOT fire.** Prior `substrate_ceiling` / `non_contributory` autopsies tagging each claim:
SD-068 = 0, MECH-168 = 0, INV-047 = 0, MECH-169 = 0. (The sibling REM autopsies scored
`weakens` / `measurement_gap`, which do not count toward the brake.) No re-queue is refused by the
brake here.

**Forward note:** this autopsy records `non_contributory` (section 6), so it becomes the **first**
brake-eligible reading on all four claims. A second such reading will fire the brake and force
`implement-substrate` routing rather than another lettered REM readout iteration.

---

## 6. Adjudication and routing (user-confirmed at the Step 8 gate)

**The self-route `rem_clamp_artifact_confirmed_but_readout_still_content_free` is ACCEPTED.** It is
supported by C1 + C3 (the clamp artifact is real and the null does de-rail) and by C2's failure with
the outlier correctly excluded (6/7 above ceiling).

**`recommended_evidence_direction: non_contributory`** (user decision at the Step 8 gate, in
preference to `weakens`). Rationale: V3-EXQ-778h is a **same-question alphabetic-suffix re-run of
V3-EXQ-778d whose only change is a readiness-anchor specification fix**. The science is identical --
same arms, seeds, sigma grid, RNG streams, thresholds and criteria. Scoring it `weakens` would
**double-count one scientific result** across a superseded/superseding pair. It is ledger hygiene
that adds provenance, not weight.

**Illusory-conflict-resolution check (mandatory pairing).** Recording `non_contributory` here, plus
marking the predecessor 778d `superseded`, must not silently delete the REM `weakens` signal. It does
not: **V3-EXQ-778e** (`rem_declamped_readout_diagnostic`) and **V3-EXQ-778f**
(`rem_gen_gain_content_scale_diagnostic`) independently carry `weakens` / `measurement_gap` from
`failure_autopsy_SD-068-rem-fanout-cluster_2026-07-18`, and both remain active. The REM leg's
weakens is therefore preserved by two runs after this bookkeeping. Verified before confirming.
(Note additionally that SD-068's current `claim_evidence.v1.json` entry shows `genuine_exp_count: 0`
with all 4 entries literature-sourced, so none of these diagnostics is presently weighting the
claim's experimental confidence in any case.)

**`pending_retest_after_substrate: false`** -- the repair is a readout redesign, not a substrate build.

**`recommended_substrate_queue_entry.action: none`.**

**Routing: `governance-adjudication`** -- two bookkeeping writes, no claim-status change:
1. Mark V3-EXQ-778d's manifest `evidence_direction: "superseded"` with an `evidence_direction_note`
   naming V3-EXQ-778h as the anchor-fixed successor, and rebuild the index.
2. Record V3-EXQ-778h `non_contributory` with the note in section 7.

**PROMOTES AND DEMOTES NOTHING.**

---

## 7. Draft `evidence_quality_note` for governance

> V3-EXQ-778h (diagnostic, run_id `v3_exq_sd068_rem_unpaired_null_anchorfix_diagnostic_20260718T183746Z_v3`)
> is a same-question anchor-fix re-run of V3-EXQ-778d and PROMOTES AND DEMOTES NOTHING. Scored
> non_contributory to avoid double-counting one scientific result across a superseded/superseding pair;
> the REM content-free finding continues to be carried by V3-EXQ-778e and V3-EXQ-778f. Its content:
> the 1e-3 positivity-clamp artifact is CONFIRMED real (readiness anchor reproduced 778c's railed
> signature on 8/8 seeds -- 5 saturation, 3 positivity-floor collapse -- and the unpaired-target null
> de-railed on 7/8), but removing the artifact did NOT reveal content-contingency: the unclamped
> null_slope_ratio median is ~0.88 against a 0.25 ceiling, with 6 of the 7 de-railed seeds above the
> ceiling. The REM calibration_error readout responds to corruption MAGNITUDE irrespective of content,
> so it cannot adjudicate whether REM consolidation preserves content. This constrains the INSTRUMENT,
> not the mechanism -- no mechanism-level pressure on SD-068 / MECH-168 / MECH-169 / INV-047 either way.
> The manifest's own `ceiling_inside_ci95: true` OVERSTATES the uncertainty: that CI95 is computed over
> all 8 seeds including seed 7777, which failed the C1 de-rail predicate (clamp_frac 0.6 > 0.2,
> 2 unclamped sigmas < 3) and supplies the entire 85.18 outlier; on the C1-passing subgroup the
> conclusion is tighter, not weaker.

---

## 8. Learning extracted

1. **Removing a measurement artifact can reveal that the underlying readout was already blind.** The
   clamp was real and worth fixing, but it was masking a content-free readout rather than causing one.
   Confirming an artifact is not the same as validating the instrument behind it -- these are two
   separate findings and the portfolio needed both.
2. **A subgroup statistic must honour the predicate that defines the subgroup.** C2's CI95 included a
   seed that failed C1's de-rail gate, which inflated the interval enough to make the manifest report
   `ceiling_inside_ci95: true` and read as underpowered. A gate-defined subgroup analysis that ignores
   its own gate reports the wrong uncertainty -- and in the conservative direction here only by luck.
3. **Same-question re-runs need an explicit non-double-counting rule.** An alphabetic-suffix re-run
   that reproduces its predecessor's science should carry provenance, not a second unit of evidential
   weight; the supersession bookkeeping and the direction choice have to be decided together, and the
   illusory-conflict check run against the pair, or a `weakens` can silently evaporate.
4. **The SD-068 REM leg now needs a content-sensitive readout, not another null-design iteration.**
   Three separate REM probes (778d/e/f) plus this anchor-fix re-run have all bottomed out on the same
   readout channel. The next move is a different measurement axis, not another letter.

---

## 9. Hypothesis-space ledger (Step 9b)

`H-rem-clamp-artifact` (question `consolidation_readout_validity`) was **already resolved**
`confirmed` / `supports` by V3-EXQ-778d. This run supersedes 778d and reproduces that science on a
corrected readiness anchor.

**Edit made:** append `V3-EXQ-778h` to the leg's `adjudicating_runs` and to
`resolution.resolving_runs`, so the ledger cites the valid (non-superseded) run, and extend
`resolution.basis` to record the anchor-fix provenance.

**No state change, no denominator change, no bar change** -- `initial_frozen_count` stays 6,
`len(hypotheses)` stays 6, `resolution.state` stays `confirmed`, `control_passed` stays true. Frozen-set
invariants 1-7 are untouched by construction; this is a provenance pointer update, not growth.
