# Diagnostic adjudication -- V3-EXQ-778g (SD-068 content-scored SWS readout validation)

- **Generated:** 2026-07-18T18:06:59Z
- **Session:** mech-063-experiment-2ffd19 (`autopsy 783 + 778g diagnostic adjudication`)
- **Target:** `v3_exq_sd068_sws_content_scored_readout_diagnostic_20260718T130139Z_v3`
- **Queue id:** V3-EXQ-778g | **Outcome:** PASS | **Purpose:** DIAGNOSTIC
- **Claims tagged:** SD-068, MECH-168, INV-047, MECH-169
- **Self-route:** `sws_readout_content_contingent_validated`
- **Indexer adjudication:** clean (NOT flagged -- no `precondition_unmet`, no `vacuous_pass`)
- **Status:** confirmed (user-adjudicated at the Step 8 gate, 2026-07-18)

> **HEADLINE -- THE LIVE DECISION IS ALREADY DISCHARGED.** The brief for this adjudication
> stated that re-widening SD-068's non-vacuity contract to re-admit the sws leg was "flagged
> in-note as a /governance adjudication, not performed," and asked for a recommendation to
> hand to the next /governance cycle. **It has since been performed and landed** --
> `REE_assembly` `9a31d79acc`, 2026-07-18T15:32:10Z, on `origin/master`, by session
> `practical-kapitsa-66ec83`. This autopsy therefore RATIFIES an applied adjudication and
> recommends **NO further claims.yaml write**. See section 5.

## 1. Why this run was adjudicated at all

Unlike its sibling target V3-EXQ-783, this run carries **no blocking adjudication flag**. Both
preconditions MET, all three `criteria_non_degenerate` true, both LOAD-BEARING criteria passed
on 8/8 seeds. A clean diagnostic PASS normally clears at the `/governance` walk without an
autopsy.

It was adjudicated because the brief identified a live governance decision it was thought to
make actionable. That decision turned out to be already discharged. The adjudication is
retained as a ratification record: an independent read of the run's merits, against the
already-applied claims.yaml text, confirming the two agree.

## 2. Facts reconstruction

Recording provenance is COMPLETE -- `validate_recording.py` reports OK, no always-core gaps
(`recording_schema` rec/v1, `substrate_hash`
3cd1aa9cf922715013f6ce8f0e7be91c32a5025c1e77d9c2a0ac5b60b9766a07, `machine` ree-cloud-2,
`machine_class` linux-x86_64-py3.10, `elapsed_seconds` 1160.9, full `config`, 8 `seeds`).

### 2a. Preconditions -- both MET

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| `injected_arm_sws_sigma_slope_supra_floor` | 0.3232 | >= 1e-06 | yes |
| `ladder_content_slope_spread_supra_floor` | 0.1108 | >= 0.01 | yes |

The first asserts the ratio's DENOMINATOR on the known-damaged positive control -- without it
the ratio is 0/0 and the control cannot discriminate. Injected-arm slopes range 0.3232-0.3578
across seeds, five orders of magnitude above the floor.

### 2b. Criteria -- both load-bearing criteria passed

```
criteria_non_degenerate: C1 true | C2 true | C3 true
criteria:  C1_sws_content_contingent  load_bearing TRUE   passed TRUE
           C2_ratio_interpretable     load_bearing FALSE  passed TRUE
           C3_ladder_tracks_content   load_bearing TRUE   passed TRUE
```

C1: `null_slope_ratio_sws` mean **0.1495** (sd 0.0218, CI95 [0.1344, 0.1646]) against the
**0.25** ceiling, `ceiling_inside_ci95` **FALSE**, content-contingent on **8/8** seeds --
against the retired readout's analytic **1.0000** (sd 2.7e-8, 8/8 confounded) in V3-EXQ-778c.

C3: content-scale ladder slope spread **0.1108** > the 0.01 floor.

**C3 is the criterion that carries the adjudication's weight**, and it was pre-registered
before the run for exactly the right reason: the replacement readout is cosine-based and
therefore scale-invariant, so its null arm is flat in sigma **partly by construction** and a
low null ratio alone is a weaker check than it looks. C3 passing is what discharges that
caveat. The result does not rest on the null ratio alone. This is good pre-registration
practice and it is what makes the run's PASS meaningful rather than tautological.

## 3. Scope -- what is and is not validated

**Validated:** the sws INSTRUMENT's content-contingency. `_sws_pattern_completion` (cosine
retrieval margin of the post-SHY store against the injected prototypes, probed with the
UNSCALED base; `ree-v3` main 8b18338, experiment-layer, zero `ree_core` change) measures
content fidelity rather than raw noise sensitivity.

**NOT validated -- and correctly so:** the reverse-dependency STAGING ORDER. `gated_phase` is
`sws` ALONE; `context_phases_not_gated` is `["nrem", "rem"]`, measured and reported as context
only. The rem leg is degenerate at both clamp rails and is owned by the separate GOV-FANOUT-1
portfolio V3-EXQ-778d/e/f (`rem_leg_owner` is stamped in the manifest's `interpretation`).

That gating choice is **sound, not a dodge**: gating on all three phases would have FAILED
regardless of whether the sws repair worked, and would have answered nothing. Scoping the gate
to the leg under repair is what makes the run informative. Staging order is a CROSS-phase
ranking and cannot be supported while one of the three ranked legs has no interpretable
readout -- and in any case no run has re-measured the staging order with the repaired
instrument.

**778c is NOT superseded.** Its finding concerns the RETIRED readout (`sws_denoising_snr`,
content-free by construction -- `noise_power` identical with and without injected content, so
the content term differentiates away analytically) and is what motivated this build. 778g
validates a DIFFERENT instrument. The manifest's own `supersedes` field is correctly `null`.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact; SD-068 instrument leg strengthened | Diagnostic. Tests the readout, not the staging claim. `evidence_direction_per_claim` is correctly `supports` for SD-068 and `unknown` for MECH-168 / INV-047 / MECH-169. |
| Biological reference | clear | Follows the Bar et al. 2020 "same odour, no prior pairing" null-contingency design: the null arm receives a real, arm-identical probe that is simply not planted, rather than a 0/0-degenerate zero. This is the methodological precedent SD-068 declares. |
| Developmental / dependency prerequisites | present | The replacement readout landed (8b18338) before the run; substrate_hash changed with it. |
| Implementation completeness | complete, experiment-layer only | Zero `ree_core` change; no substrate_queue entry needed. |
| Environment adequacy | adequate | Injected-arm sigma sweep moves the readout across the full grid (slopes 0.323-0.358). |
| Measurement adequacy | adequate, and independently anti-artifact-checked | C3 discharges the scale-invariance caveat that C1 alone could not. |
| Integration adequacy | isolated by design | sws leg gated alone; nrem/rem context-only. Appropriate for an instrument-validation run. |
| Scale / capacity | adequate | n=8 seeds; `ceiling_inside_ci95` FALSE; the earlier 3-seed local smoke is superseded by this 8-seed cloud run. |

**Recommended `epistemic_category`: `instrument_repair_validated`.**
**Recommended `evidence_direction`: `supports` (SD-068 only); `unknown` for MECH-168 / INV-047
/ MECH-169** -- i.e. exactly what the manifest already declares. No change recommended.

## 5. The live decision -- ALREADY APPLIED, ratified here

The brief asked this autopsy to adjudicate the re-widening of SD-068's non-vacuity contract
and hand a recommendation to the next `/governance` cycle. **That adjudication has already been
performed and landed.**

- **Commit:** `REE_assembly` `9a31d79acc` -- *"SD-068: partially re-widen non-vacuity contract
  -- re-admit sws leg (V3-EXQ-778g), staging order still excluded"*
- **Landed:** 2026-07-18T15:32:10Z, on `origin/master` (verified present in
  `git show origin/master:docs/claims/claims.yaml`)
- **Session:** `practical-kapitsa-66ec83` (closed in umbrella commit `c13996d`)
- **Text:** `docs/claims/claims.yaml:49603-49665`, the
  `[PARTIALLY RE-WIDENED 2026-07-18 -- V3-EXQ-778g]` block on SD-068's
  `evidence_quality_note`.

The in-note sentence quoted by the brief ("...is a GOVERNANCE adjudication for a /governance
cycle, not something this implementation_note performs", `claims.yaml:49548`) sits in the
**`implementation_note`**, which was written earlier at `72f842fe88` (15:09Z) and correctly
declined to perform the adjudication. The adjudication then landed 23 minutes later in the
`evidence_quality_note`. The `implementation_note` sentence is now **stale as a description of
the current state**, though historically accurate as a record of what that note did.

### 5a. Independent verification of the applied text

I checked the landed re-widening against the manifest line by line. **It is accurate on every
number and correct on every scope boundary:**

| Applied claim | Manifest | Verdict |
|---|---|---|
| C1 mean 0.1495, sd 0.0218, CI95 [0.1344, 0.1646] | 0.14950301781, 0.021831491734, [0.13437456588, 0.16463146974] | correct |
| `ceiling_inside_ci95` FALSE | false | correct |
| 8/8 seeds | `n_seeds_content_contingent` 8 | correct |
| Retired readout 1.0000, sd 2.7e-8 | `prior_778c_ratio` 1.0, `prior_778c_sd` 2.7e-08 | correct |
| C3 spread 0.1108 > 0.01 floor | 0.11084844688, threshold 0.01 | correct |
| Preconditions met, injected slope 0.323 (range 0.323-0.358) | 0.32317587708; per-seed 0.3232-0.3578 | correct |
| Same 0.25 ceiling that admitted the nrem leg | `C1` acceptance text: `<= 0.25` | correct -- symmetry of criterion holds |
| Staging order still UNSUPPORTED; rem owned by 778d/e/f | `gated_phase` sws; `rem_leg_owner` "V3-EXQ-778d/e/f" | correct |
| 778c NOT superseded | `supersedes` null | correct |
| Narrow-supports flag STILL raised on narrower ground | consistent with H-gen-gain-content-free still alive in the ledger | correct |
| No status/confidence change (diagnostic) | `experiment_purpose` diagnostic | correct |

The applied note also self-corrects a phrase from the 778c narrowing that 778g made false
("no leg ... is currently supported by a validated instrument"), replacing it with the
accurate statement that no leg's staging POSITION is established, two of three legs now have
validated content-contingent instruments, and the third does not. That is exactly the right
correction.

**My independent reading of 778g on the merits AGREES with what landed.** Re-recommending it
would be the duplicate re-application of landed governance writes that CLAUDE.md's Session
Startup Protocol warns about.

## 6. Re-derive brake and recurrence checks

- **Re-derive brake: does NOT fire.** SD-068 carries one prior autopsy
  (`failure_autopsy_V3-EXQ-778c_2026-07-18`) whose category is `measurement_gap`, not
  `substrate_ceiling` / `non_contributory`. The counted total is 0. No re-queue is refused.
- **Granularity-debt recurrence trigger: checked, does NOT fire.** SD-068 has a prior autopsy,
  so the count condition is met, but the substance is not: 778c diagnosed a measurement gap and
  routed a repair; 778g validates that repair. This is a diagnose-repair-validate sequence
  converging on one instrument, not repeated circling with distinct failure signatures. No
  `/claim-synthesis` handoff.

## 7. Learning extracted

1. **Scoping a gate to the leg under repair is what makes an instrument-validation run
   informative.** Gating all three phases would have FAILED regardless of whether the sws
   repair worked. The manifest stamps `gated_phase`, `context_phases_not_gated` and
   `rem_leg_owner` in `interpretation`, which is what makes the narrow scope legible to
   governance rather than something a reader has to reconstruct. Good pattern to repeat.
2. **Pre-registering an anti-artifact criterion against your own readout's known form is what
   converts a PASS from tautological to meaningful.** C3 exists because the replacement is
   cosine-based and hence scale-invariant, so its null arm is flat in sigma partly by
   construction. Without C3, C1's low null ratio would have been partly implied by the
   readout's form.
3. **Re-admission on the SAME criterion that excluded the leg is the load-bearing fairness
   property.** The sws leg was excluded on one ground (content-free by construction) and
   re-admitted by clearing the same load-bearing C1 at the same 0.25 ceiling that admitted the
   nrem leg. Re-admitting on a weaker test would have been motivated reasoning.
4. **A brief can be stale on the state of the claim registry.** The live decision this
   adjudication was convened to make had landed three hours before the session opened. Verifying
   against `origin/master` before recommending a governance write -- rather than trusting the
   in-note description of what was outstanding -- is what caught it. Note also that the stale
   pointer was an `implementation_note` describing its own scope, while the live carrier of
   scope is the `evidence_quality_note`; the two can disagree by design, and the
   `evidence_quality_note` is authoritative.

## 8. Routing (user-confirmed)

**RATIFY -- recommend NO new claims.yaml write on SD-068.**

1. **No re-application of the re-widening.** It landed at `9a31d79acc`; this autopsy verifies
   it and concurs. Governance should make no further write to SD-068's `evidence_quality_note`
   on account of 778g.
2. **No status, confidence, promotion or demotion change.** `experiment_purpose` is diagnostic;
   diagnostic evidence does not weight governance confidence. SD-068 remains `candidate`,
   `implementation_phase` v3.
3. **MECH-121 hold remains RESPECTED.** 778g deliberately does not tag MECH-121.
4. **`evidence_direction` stands as declared** -- `supports` for SD-068, `unknown` for
   MECH-168 / INV-047 / MECH-169. No amendment.
5. **One optional tidy, flagged not required:** the `implementation_note` sentence at
   `claims.yaml:49548-49550` ("Whether SD-068's non-vacuity contract should now be re-widened
   ... is a GOVERNANCE adjudication for a /governance cycle, not something this
   implementation_note performs") is now stale as a description of the current state, since
   that adjudication landed 23 minutes later at `9a31d79acc`. A one-line forward pointer would
   prevent a future session re-opening a closed decision, as this session's brief did. It is
   NOT a correctness defect -- the sentence accurately describes what the `implementation_note`
   itself did, and the `evidence_quality_note` is the live carrier of scope.
6. **Mark reviewed at the `/governance` walk.** Per skill policy this autopsy does not touch
   `review_tracker.json`.

**No `/queue-experiment`, no `/implement-substrate`, no substrate_queue entry.** The rem leg
is already owned by the queued GOV-FANOUT-1 portfolio V3-EXQ-778d/e/f; nothing here duplicates
or pre-empts it.

### Draft note for governance

**None required.** The recommendation is a NO-OP on claims.yaml. If governance wants a
provenance breadcrumb, the minimal form is a single line appended to SD-068's
`implementation_note` immediately after the stale sentence:

```
[POINTER 2026-07-18] That adjudication WAS subsequently performed and landed the same day at
REE_assembly 9a31d79acc (2026-07-18T15:32:10Z) -- see the "[PARTIALLY RE-WIDENED 2026-07-18 --
V3-EXQ-778g]" block in evidence_quality_note below, which is the live carrier of scope.
Independently ratified by evidence/planning/failure_autopsy_V3-EXQ-778g_2026-07-18.
```
