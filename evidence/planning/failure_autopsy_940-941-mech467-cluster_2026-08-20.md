# Failure autopsy -- V3-EXQ-940 + V3-EXQ-941 (MECH-467 GOV-FANOUT-1 leg-(c) denominator portfolio)

- **Generated (UTC):** 2026-08-20T02:39:17Z
- **Scope:** cluster (2 runs, one designed portfolio)
- **Status:** confirmed (user gate 2026-08-20)
- **Session:** failure-autopsy-multi-20260819
- **Dry-run gate:** both manifests checked, top-level `dry_run` absent on both -- neither is a smoke. No dry run_id is cited anywhere in this artifact.

## 0. Why these two are one autopsy

They are a single GOV-FANOUT-1 discrimination portfolio, queued together
(`ree-v3` `034d584`), each naming the other in `portfolio.sibling_legs`, both
pre-registered as legs of `mech467_legc_event_denominator_cause` from
`failure_autopsy_V3-EXQ-874b_2026-08-17.json`. Adjudicating either alone
misreads the discrimination.

| leg | queue_id | axis | outcome | label |
|---|---|---|---|---|
| H-energy | V3-EXQ-940 | environment | PASS | `window_restored_rate_unchanged` |
| H-denominator | V3-EXQ-941 | measurement | FAIL | `denominator_lost_at_approach_initiation` |

**Outcome polarity is inverted on both legs**, by design and stated in both
queue notes: 940's PASS *is* its declared null; 941's FAIL *is* its informative
result. Read the label, not the outcome.

`H-commitment` and `H-cadence` were deliberately not queued (answered at
substrate level; the deeper causal question is owned by the ACTIVE
hypothesis-space line `e3_fdominance_causal_discrimination`). That 4->2 shrink
was warranted by `navigation_immobility_scoping_2026-08-18.md`, which is still
**AWAITING USER REVIEW** -- if that spike is revised, the shrink loses its
warrant retroactively.

## 1. Facts

### 1a. 940 -- per-arm pooled (the load-bearing table)

| arm | consumption events | realised ticks | events/tick | window_completeness | truncated cells |
|---|---|---|---|---|---|
| ARM_STOCK | **0** | 2249 | **0.0** | 0.832963 | 2 |
| ARM_CONTAM_OFF | 2 | 2700 | 0.00074074 | 1.0 | 0 |
| ARM_HEALTH_DECOUPLED | **4** | 2700 | **0.00148148** | 1.0 | 0 |

C1 (`window_completeness_lifts_when_contamination_gated`, load-bearing) passed:
lift 0.167037 vs threshold 0.15 -- **margin 0.017, 11% over the floor**, and the
lift comes entirely from ARM_STOCK's two truncated cells (seeds 42, 44); seed 43's
stock cell realised 1.0. Per-seed stock window completeness [0.764, 1.000, 0.734].
C1's non-degeneracy gate (`n_truncated_cells > 0`) is satisfied by one cell.

C2 (`event_rate_lifts_when_window_decoupled`) reports `measured_ratio: null`,
`passed: false`, `load_bearing: false`.

### 1b. 941 -- absolute event counts (not rates)

| seed | arm | ticks | initiations | arrivals | consumption | position changes | blocked |
|---|---|---|---|---|---|---|---|
| 42 | ARM_PRECOMMIT | 342 | 1 | 1 | 1 | 10 | 332 |
| 42 | ARM_REPLAY | 653 | 0 | 0 | 1 | 14 | 639 |
| 43 | ARM_PRECOMMIT | 900 | **0** | **0** | **0** | **0** | 900 |
| 43 | ARM_REPLAY | 900 | **0** | **0** | **0** | **0** | 900 |
| 44 | ARM_PRECOMMIT | 496 | 0 | 0 | 1 | 10 | 486 |
| 44 | ARM_REPLAY | 390 | 5 | 1 | 1 | 10 | 380 |

**Grand totals: 6 initiations, 2 arrivals, 4 consumption events, 3681 realised ticks.**
`pooled_move_efficacy` 0.0115 / 0.0124 (**98.8% of movement actions blocked**);
`e3_tick_fraction_mean` 0.104 / 0.103 (**89-91% of ticks latched, not re-selection**);
`approach_run_length_max = 1` in both arms -- no approach run ever exceeded a single step.

### 1c. Recording provenance

`validate_recording.py`: both manifests complete, 0 always-core gaps, 0 schema
warnings. Every quantitative statement in this artifact was recomputed from the
manifests without re-running anything.

## 2. The substrate_hash divergence is NOT a confound (checked, and closed)

The two legs report different `substrate_hash` (`cef75e59...` vs `1b39ad11...`)
on different machines 13 minutes apart. This is an artefact of driver-script
folding, not substrate divergence:

1. `arm_fingerprint.py:653` folds the driver script into the hash
   (`driver_script_in_substrate_hash: true` in every arm fingerprint of both runs);
   `_SUBSTRATE_GLOBS` (`:68-73`) does **not** include experiment drivers. Two
   different drivers therefore give two different hashes unavoidably.
2. `git diff --stat 78ec9de 4c66e69 -- ree_core/ experiments/_harness.py
   experiments/_metrics.py experiments/_lib/` is **empty**. The only files
   differing between the two recorded commits are `experiment_queue.json` and an
   unrelated new driver (`v3_exq_937b_...`), neither in the glob set.
3. No `ree_core/` commit landed in the window (last before both: `76cbf84`
   01:26:49Z; next after both: `692f852` 14:56:06Z, after 941's manifest write).

`machine_class` is identical on both (`linux-x86_64-py3.10-torch2.12.0+cpu`),
which is the granularity at which the known `torch.multinomial` cross-machine-class
divergence operates. **Comparing leg A to leg B is sound.** Recorded here so a
later session does not re-derive it.

## 3. Four-layer diagnosis (cluster)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear -- not tested** | Neither leg measures MECH-467's falsifier (wrong-target rate elevated with rule drift at floor). 940 recorded 3 wrong-target events total; 941 has zero wrong-target instrumentation. Both disclaim rule-state reads under the MECH-262 constraint. Correctly scoped as denominator diagnostics. |
| Biological reference | n/a | No mechanism translation is under test in a denominator diagnostic. |
| Prerequisites | **missing** | The exposure window cannot produce a measurable event denominator. Live gate (>=15 pooled events in one arm) missed at 4. |
| Implementation | partial | Instrument defects in the criteria themselves -- see section 4. |
| Environment | **too sparse / wrong pressures** | 98.8% of movement actions blocked; 2.33 unique cells visited on average; seed 43 fully immobile for 900/900 ticks in both arms. |
| Measurement | **under-instrumented / misleading** | 940's C2 undefined; 941's C3 does not measure conversion; `approach_is_definable` floor set to 0.0 cannot fire. |
| Integration | n/a | |
| Scale / capacity | **likely insufficient** | At the best observed rate (0.00148/tick) the >=15-event floor needs ~10,100 ticks/arm against 2700 budgeted -- inside 874b's own 8380-17200 estimate. |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED:** not_established -- MECH-467's mechanism was never exercised.
- **MEASURES FAILED:** **established** -- 940 C2 undefined, 941 C3 mis-measuring.
- **ENVIRONMENT FAILED:** **established** -- near-total immobility.
- **REE FAILED:** false.

**Net classification: MIXED (measures + environment) -- not chargeable to REE.**

## 4. Instrument defects found (these are the durable output)

**(D1) 940's C2 is UNCOMPUTABLE, not null -- and the emitted label asserts the
opposite of what the data show.** `rate_lift_ratio = best/stock if stock_rate > 0
else None` (`v3_exq_940...py:751`). ARM_STOCK produced exactly 0 events, so the
ratio is `None` and `c2_pass` is False. But the underlying rates rose
**monotonically with the strength of the decoupling manipulation, from exactly
zero**: 0.0 -> 0.00074 -> 0.00148. The arm that ate at the highest rate in the
entire portfolio is the health-decoupled one; the stock arm never ate at all.
The emitted note -- *"the event rate per realised tick does not lift ... The
residual rate problem is not an energy problem"* -- is contradicted by the run's
own `per_arm_pooled` table.

The non-degeneracy guard tests the **wrong quantity**:
`c2_non_degenerate = total_events_all_arms > 0` (`:763`) checks for events
*anywhere*, when a ratio needs events in the **denominator** arm. So C2 is
stamped `non_degenerate: true` while being arithmetically undefined. This is a
verdict-aliasing defect of exactly the class the driver's own Step-2.5b
adversarial audit hardened C1 against (`:764-771`) and did not apply to C2.

**Consequence, and it is the load-bearing consequence of this autopsy:
H-energy must NOT be recorded as eliminated.** On 4 events the directional
signal is not significant either -- so the honest state is unresolved, not null.

**(D2) 940's `combination_rule` contradicts C2's `load_bearing: false`.**
`outcome = PASS if (non_degenerate and (c1_pass or c2_pass))` (`:842`) -- C2 can
independently produce a PASS, which makes it load-bearing by definition. Combined
with D1, 940's entire PASS rests on **C1 alone**, at a 0.017 margin over 2 of 3 cells.

**(D3) 941's C3 does not measure conversion, and consumption exceeds arrivals 2:1.**
`c3_pass = total_events > 0` (`:885`) is a pooled existence test across both arms,
despite `owned_by_arms: ["ARM_PRECOMMIT"]`. 4 consumption events against 2 arrivals,
with 2 of the 4 in cells recording **zero** initiations and **zero** arrivals --
plausibly the agent standing on a respawning resource cell. The
`denominator_lost_at_consumption` branch (`:937`) is therefore unreachable in
practice on this env.

**(D4) 941's C2 reports a pooled statistic under a single-arm ownership label**
(0.333333 pooled vs ARM_REPLAY's own 0.2). Cosmetic here (both clear the floor),
but the ownership/statistic mismatch is systematic across 941's criteria.

**(D5) 941's `approach_is_definable` precondition cannot fire.** It was written to
catch exactly the seed-43 aliasing case (a near-zero mean distance producing an
initiation rate of ~0 that aliases onto `never_approached` while meaning the
opposite). Its threshold is 0.0; seed 43 sat at `mean_distance_to_goal = 1.0`
exactly -- one step from a target, on a grid where one step is arrival -- for 900
consecutive ticks. Correctly reasoned, set to a floor that cannot fire.

**(D6) Neither C2 nor C3's manifest notes describe what happened.** Both name
degeneracy conditions that did not fire (940 C2: *"Degenerate when no arm produced
any consumption event"* -- six were produced). A reader trusting the notes
misdiagnoses D1 as degeneracy.

## 5. What the portfolio DID establish

Stated plainly, because it is real and should not be lost in the defect list:

1. **The denominator is lost upstream of arrival.** 6 initiations / 2 arrivals /
   3681 ticks, `approach_run_length_max = 1`. The agent does not head for
   benefit-bearing targets at all. 941 is the first run to localise this.
2. **Neither survival nor contamination explains it.** 940's ARM_HEALTH_DECOUPLED
   delivered the live gate's own precondition -- a fully-realised 2700-tick window
   with contamination gated and health clamped -- and still produced only 4 events.
   The gate's framing assumed the window was the binding constraint. It was not.
3. **874b's arithmetic is independently reconfirmed.** Best-arm event rate has not
   moved off ~0.0015/tick across three designs (874b 0.00117; 940 best 0.00148;
   941 pooled 0.00109), against a probe rate of 0.0100 that was itself insufficient.
   Lengthening the window cannot rescue this design.
4. **New quantification of the immobility**, not previously measured at battery
   level: 98.8% of movement actions blocked, 89-91% of ticks latched, 2.33 unique
   cells visited. This is consistent with, and quantifies, the 2026-08-18
   navigation-immobility scoping spike.

**Caveat on the MECH-439 cross-reference.** 941's note says it "confirms at battery
level" the MECH-439 F-dominance conversion ceiling, and asks the reader to read
`pooled_move_efficacy` and `e3_tick_fraction_mean` alongside as a decomposition of
"how much is wall-blocking and how much is cadence rather than selection". Those
two scalars **cannot decompose it**: at 98.8% blocked and 89-91% latched both are
near-ceiling simultaneously and are consistent with any mixture. 941 took no
selection-layer measurement. Read "confirms" as *is consistent with and quantifies
at battery level*, not as independent confirmation. The causal question remains
owned by `e3_fdominance_causal_discrimination`.

## 6. Cluster pattern

**One structural property, not two independent bugs.** Both legs are instances of
the same shape: a criterion keyed to a rate whose denominator the substrate does
not supply. 940 divides by a zero event rate; 941 divides arrivals by 6
initiations and consumption by 2 arrivals. Where the denominator is absent the
criterion does not return a null -- it returns an artefact that reads like one.

Two readings are live and this autopsy does not choose between them:
- **substrate_enrichment** -- the agent cannot move or re-select often enough to
  generate events; fix mobility/cadence upstream.
- **test_design_ceiling** -- leg (c)'s event-denominator DV is the wrong readout
  for this substrate at any window length.

The planning decision forced: **do not queue a fourth denominator design.**

## 7. Routing -- CONFIRMED at the user gate (2026-08-20)

**`governance`**, with an explicit refusal attached.

- **REFUSED: a fourth denominator attempt.** The re-derive brake does not fire by
  the letter (MECH-467 ceiling hits = 0 under R1-R3), but this is its spirit:
  three consecutive designs, best-arm event count unmoved at 4, and 940 has now
  removed both candidate explanations. Recorded as spirit-not-letter.
- **`recommended_substrate_queue_entry.action: "none"`** -- deliberately, and for
  the same reason 874b's autopsy gave: naming a substrate build now picks one
  hypothesis before the discrimination has run. The mobility question is already
  owned by the ACTIVE `e3_fdominance_causal_discrimination` line, and minting a
  MECH-467-specific substrate item would duplicate an in-flight investigation.
- **Neither run bears on MECH-467 in either direction.** `evidence_direction`
  `non_contributory` for both; `epistemic_category` `standard` (behaviour-preserving
  -- this is a "the run told us nothing about the claim" reading, not an assertion
  that MECH-467's answer is gated on substrate).
- **Leg (c) is blocked on agent mobility**, which is not MECH-467's own substrate.
  Record it as such rather than as a MECH-467 substrate gap.
- **Owed to any future battery:** 874b's `mandatory_in_any_successor` item 5
  (align `selection_path_rule_read_live`'s code with its stated control) is still
  outstanding -- items 1-4 are satisfied in both manifests, item 5 is not
  applicable to these two legs and remains owed.
- **Driver fixes owed before any successor** (D1-D5 above), in priority order:
  C2's ratio guard must test the denominator arm; C3 must measure its owning arm's
  conversion; `approach_is_definable` needs a floor that can fire.

## 8. Hypothesis-space ledger (Step 9b, Mode B)

Question `mech467_legc_event_denominator_cause` (registered 2026-08-17,
`initial_frozen_count` 4, `growth_restriction` absent). No growth: these are the
pre-registered legs' own adjudicating runs, so `initial_frozen_count` is unchanged
at 4 and no growth event is recorded.

- **H-denominator -> `confirmed`** (resolving run V3-EXQ-941). The decomposition
  succeeded and localised the loss upstream of arrival. `control_passed: true`
  (`movement_instrument_live` 4/4 distinct movement actions changed position),
  `non_degenerate: true`. `met_elimination_bar: false` -- this confirms the leg
  rather than eliminating it, and the basis is thin (6 initiations, with 49% of
  the denominator contributed by a fully-immobile cell), which is recorded in the
  basis string rather than smoothed over.
- **H-energy -> STAYS `alive`** (resolving run recorded, state unchanged --
  user-confirmed 2026-08-20). Its deciding criterion never evaluated (D1). The
  only directional evidence available points the other way. An uninformative run
  narrows nothing; recording an elimination on a criterion that never computed is
  the frozen-set discipline's core failure mode.
- **H-commitment, H-cadence** -- untouched, not queued, unchanged.
- `decision.distance_phrase` ("4 legs pre-registered, none yet run") and
  `observation_bottleneck` ("two consecutive designs") are now stale; the
  bottleneck is three designs deep.

## 9. Learning extracted

1. **A rate criterion whose denominator arm can legitimately be zero needs a
   non-degeneracy guard on the DENOMINATOR, not on the pooled numerator.** 940's
   C2 is the worked example: it is stamped non-degenerate while being undefined.
2. **A criterion that can independently produce a PASS is load-bearing**, whatever
   the flag says. 940's `combination_rule` and its `load_bearing: false` disagree.
3. **An existence test is not a conversion test.** 941's C3 certifies only that
   >=1 consumption happened somewhere -- a weaker statement than the floor it was
   built downstream of, and satisfiable with zero approaches.
4. **Removing the two candidate explanations and finding the rate unchanged is a
   real result**, and it is the portfolio's most valuable output even though the
   leg it was meant to decide never computed.
5. **A precondition written against a known aliasing case must have a threshold
   that can fire.** D5.
