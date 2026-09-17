# Failure autopsy -- V3-EXQ-1046 (SD-082)

Status: confirmed (user gate 2026-09-17)
Generated: 2026-09-17T17:57:22Z
Run: `v3_exq_1046_sd082_consequence_trained_readout_20260917T053813Z_v3`
Purpose: diagnostic | Outcome: FAIL | Direction: weakens

## 1. Facts

Dry-run gate: `check_dry_run_citations.py` run over the cited id -- CLEAN (not a smoke).
Recording: `validate_recording.py` OK, 0 always-core gaps. substrate_hash
`751475cf...`, machine `ree-cloud-2`, 7 seeds [611,622,633,644,655,666,677],
elapsed 58898.6 s.

All 8 readiness gates green on all 7 seeds (56/56). Self-yoke positive control
(TRAINED_INTACT vs REF_SELF) 0 divergent ticks on 7/7 over 18509 ticks.
`cross_pair_raw_mismatch` 0 everywhere; the raw-identical filter excluded 0 ticks.

| criterion | load-bearing | threshold | measured | result |
|---|---|---|---|---|
| C1 trained-over-init paired | YES | 4 seeds | 0 of 7 | FAIL |
| C1neg init-over-trained (routing) | no | 4 seeds | 4 of 7 | PASS -> weakens |
| C4 two-sided equivalence | no | 7 | 2 | FAIL |
| C2 trained pair itself divergent | no | 4 | 2 (init pair: 7) | FAIL |
| C3 fresh-seed reproduces | no | n/a | applies:false | -- |

Mean paired DV -0.0837 against a +0.05 floor.

**Which criterion failed:** the discrimination criterion. The absolute-floor criteria
and the positive control passed.

## 2. Claim layer

SD-082 (design_decision, status `candidate_substrate_landed`, implementation_phase v3,
epistemic_category `standard`, diagnostic_evidence_adjudicated true,
pending_retest_after_substrate false, depends_on SD-008/066/077/033a, ARC-063, SD-078).

This is the **first `weakens` of any kind on SD-082**. Prior record: 0 weakens,
0 experimental posterior entries, overall_confidence 0.828 entirely from literature.
The claim could express itself here: the readiness conjunction was fully green and the
init pair was live on every seed.

## 3. Biological-reference triage

Closest mechanism: corticostriatal rule-to-action bias (PFC rule_state -> striatal
action bias) shaped by dopaminergic RPE. Dependencies: a CLOSED action-outcome loop,
and a credit signal that is candidate-specific rather than global.

**Formal-definition import, and the divergence is load-bearing.** REINFORCE on an OPEN
loop is not the biological credit signal. `lit_status: partial`. This is the likeliest
locus of the failure: a head trained by a global, open-loop surrogate has no pressure to
make its output rule-CONDITIONED, only to make it good on average.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | tested under conditions where it could express itself |
| Biological reference | partial | open-loop REINFORCE vs closed-loop RPE: load-bearing |
| Prerequisites | present | head built and trained; authority active 35/35 |
| Implementation | complete | it trains and has authority; the defect is WHAT it learned |
| Environment | adequate | 7 seeds, 2583-2859 ticks each |
| Measurement | adequate | paired, raw-identical filtered, known-zero control |
| Integration | coupled but unstable | has authority, uses it on a rule-independent basis |
| Scale | adequate | -- |

**Failure-location summary (GOV-FAILLOC-1): MECHANISM.** Measurement adequate and
environment adequate, but Implementation-completeness is `complete` only in the sense
that the code runs -- the trained artefact does not carry the asserted property. Net:
single-bucket MECHANISM, **not** REE FAILED (measurement and environment are both
established, mechanism is the locus).

## 5. The mechanism -- CORRECTED at the Step 7c pass

The first draft of this autopsy said "common-mode collapse toward a candidate-UNIFORM
output". **That was wrong, and inverted.** `authority_scale_factor_median` is a DIVISOR:
`scale_factor = target_range / modulatory_spread` (`ree_core/predictors/e3_selector.py:3425`),
and `raw_score_range_mean` is identical between TRAINED_INTACT and INIT_INTACT on all 7
seeds by construction. A 6-43x SMALLER trained scale factor therefore means the trained
head's cross-candidate spread is **6.13x-42.80x LARGER** than init's:

| seed | 611 | 622 | 633 | 644 | 655 | 666 | 677 |
|---|---|---|---|---|---|---|---|
| spread trained/init | 20.99 | 27.61 | 24.69 | 6.13 | 30.79 | 6.38 | 42.80 |
| head_effect argmin div | 0.8208 | 0.2089 | 0.3017 | 0.2058 | 0.8343 | 0.2193 | 0.2355 |

The trained head reorders E3's top preference relative to init on 21-83% of raw-identical
co-fresh ticks. Meanwhile it has stopped responding to the RULE: `trained_head_flip_fraction`
0.01807 vs init 0.20076 (11.1x), and rule-zeroing moves the trained pair only 0.0028-0.0315
against the init pair's 0.0377-0.2115.

**Reading: training made the readout RULE-INVARIANT while leaving it strongly
candidate-opinionated.** The open-loop REINFORCE surrogate learned a large, confident
candidate preference that is essentially independent of `rule_state` -- the precise inverse
of SD-082's asserted content (a rule-CONDITIONED per-candidate action bias).

## 6. No contradiction with V3-EXQ-1029 -- for a corrected reason

The draft asserted these measure different quantities (committed vs preference argmin).
**That premise is false.** 1029's 0/1694 is `off_pair` PREFERENCE argmin
(sum n_cofresh = 1694, d_argmin = 0), and `n_both_committed` = 0 across all 40 runners --
1029 could not have measured a committed argmin at all. Verified directly.

The conclusion survives for a stronger reason: 1029's 0/1694 was measured with authority
**OFF**; 1046 measures with authority **ON**, which is the leg's own stated condition. 1046's
init pair under authority (0.0377-0.2115) reproduces 1029's authority-ON `on_pair` reference
(stored verbatim in `diagnostics.x1029_on_pair_reference_by_seed`). So 1046 **corroborates**
`H-selection-authority-bounded` rather than merely not contradicting it.

## 7. The C1neg knife edge -- real, and conservative

C1neg's threshold (4) equals the number of seeds on which it was REACHABLE (4): seeds 622,
666, 677 have `init_div_in_joint` < 0.05 and `DV >= -init` by construction, so `DV <= -0.05`
was unattainable there. `n_ready_seeds_c1neg_unreachable` = 3 records this.

The bias runs the **conservative** way: with max attainable = threshold = 4, C1neg demanded a
**unanimous sweep of every reachable seed**. A single miss would have dropped routing to
`unknown`. It cannot manufacture a false `weakens`.

Worth recording: the driver's guard ("SEED_MAJORITY is absolute, never a fraction of the
realised ready count") governs the DENOMINATOR, not REACHABILITY. Reachability is handled
separately and honestly, per-seed. The guard does not cover this mechanism -- it did not
need to here, but a future design should not assume it does.

## 8. Re-derive brake

**Does not fire.** SD-082's literal count is 3 (822b, 822c, 822d) against a threshold of 2,
but this target does not COUNT: category `standard` and direction `weakens` fail the R1-R3
predicate's first gate, so `counts()` returns False immediately. Count stays 3.
Independently verified by the Step 7c pass running the predicate and scan verbatim over the
live committed corpus.

## 9. Granularity-debt recurrence trigger

**Does not fire.** `granularity_debt_cluster.py SD-082` reports 9 targets across 8 files with
alignment distribution `unclear=9` before this autopsy -- **no target read `weakened`**, which
is the reader's own stated disqualifier ("measurement or implementation debt, NOT granularity
debt, regardless of the count"). 1046 is the first `weakened`. One is not a recurrence; a
second structurally-different `weakened` would make the trigger live.

## 10. Step 7b / 7c

- **7b mechanical pre-routing checks:** 0 fires. C5 and C7 report `inapplicable` -- recorded
  as "could not look", not as "no fire".
- **7c adversarial pass: CONTESTED.** Model: `claude-opus-5` -- the SESSION model, **not**
  cross-model. `claude-fable-5-1` was attempted twice and returned HTTP 429 (monthly spend
  limit); re-spawned once on the session model per SKILL.md Step 7c. A same-model pass shares
  the drafter's priors and blind spots and is weaker evidence than a cross-model one.
  Three findings, all accepted and all independently re-verified before acceptance:
  F1 the mechanism was inverted (section 5); F2 "positive evidence" for two alive legs was
  wrong in one case and half-wrong in the other (recorded as `read_across_not_adjudicated`);
  F3 the no-contradiction premise was false (section 6). Two attacks FAILED and the draft
  held: the brake assertion, and the C1neg knife edge.

## 11. Routing

`queue-experiment` -- a redesign attacking the RULE-CONDITIONING of the credit signal.
The head's capacity and authority are not the constraint (spread 6-43x larger than init,
authority active 35/35); the constraint is that the open-loop surrogate provides no pressure
for the bias to depend on `rule_state`. Substrate entry: `amend` SD-082 (severity unchanged
at `corrupting`), adding the failure record above.

Per-claim disposition, evidence_quality_note text, and the `-> stamp this artifact` citation
change are in the companion `.json`. `/governance` applies them; this skill applies nothing.
